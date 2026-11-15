"""High-Q resonator driven electrostatically at HALF its resonance frequency, no DC bias:
    y'' + 2*gam*y' + w0^2 y = c V(t)^2,   V(t) = Re(u e^{i w0 t/2}),  u = complex drive amplitude (2 real controls).
V^2 = |u|^2/2 + Re(u^2 e^{i w0 t})/2: a static (non-resonant) part and a resonant part ~ u^2.
Averaging with y = Re(a e^{i w0 t}) gives the envelope equation
    a' = -gam a + kappa u^2,   kappa = -i c/(4 w0)          (our model x' = u^2, plus weak damping)
Task (Q-control / active braking): make a decay at a prescribed rate R >> gam.
Branching feedback (coupling manifold a = F(z) = -kappa z^2/R, reference z' = -(R/2) z, coupling u = z):
    u = branch of sqrt(-R a / kappa),  closed loop a' = -(gam+R) a.
No continuous s(a) can give kappa s(a)^2 ~ -R a near 0 (s^2 has even winding, -a has winding 1)."""
import numpy as np
w0, Q, c = 1.0, 1e4, 1.0
gam = w0/(2*Q); kappa = -1j*c/(4*w0)
def envelope(y, yd, t):                       # demodulated complex amplitude
    return (y - 1j*yd/w0)*np.exp(-1j*w0*t)
def law(name, a, uprev, R):
    if name == "none": return 0j
    if name == "branching":
        r = np.sqrt(-R*a/kappa + 0j)          # one branch; the other is -r
        return r if abs(r-uprev) <= abs(-r-uprev) else -r     # keep the branch (internal state)
    if name == "linear":                      # a continuous single-valued attempt, u = beta*a
        beta = np.sqrt(R/abs(kappa)); return beta*a
def simulate(name, R=0.02, T=600.0, dt=0.01, y0=1.0, noise=0.0, seed=0):
    rng = np.random.default_rng(seed)
    y, yd, u = y0, 0.0, 0j; t = 0.0; n = int(T/dt)
    amp = np.empty(n); umax = 0.0; Vmax = 0.0
    def rhs(t, y, yd, u):
        V = (u*np.exp(1j*w0*t/2)).real
        return yd, -2*gam*yd - w0**2*y + c*V*V
    for i in range(n):
        a = envelope(y + noise*rng.standard_normal(), yd + noise*rng.standard_normal(), t)
        u = law(name, a, u, R)
        k1 = rhs(t, y, yd, u); k2 = rhs(t+dt/2, y+dt/2*k1[0], yd+dt/2*k1[1], u)
        k3 = rhs(t+dt/2, y+dt/2*k2[0], yd+dt/2*k2[1], u); k4 = rhs(t+dt, y+dt*k3[0], yd+dt*k3[1], u)
        y += dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]); yd += dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]); t += dt
        amp[i] = abs(envelope(y, yd, t)); umax = max(umax, abs(u))
        Vmax = max(Vmax, abs((u*np.exp(1j*w0*t/2)).real))
    return amp, umax, Vmax, dt
if __name__ == "__main__":
    R = 0.02
    print(f"natural decay rate gam={gam:.1e} (time to 1/e: {1/gam:.0f}); target R={R} (time to 1/e: {1/(gam+R):.0f})")
    for noise in (0.0, 1e-3):
        for name in ("none", "linear", "branching"):
            amp, umax, Vmax, dt = simulate(name, R=R, noise=noise)
            def tcross(lev):
                k = np.argmax(amp < lev); return (k+1)*dt if amp[k] < lev else float('inf')
            print(f"noise={noise:.0e} {name:9s} |a| at t=100: {amp[int(100/dt)-1]:.3e}  at t=600: {amp[-1]:.3e}"
                  f"  t(|a|<1e-1)={tcross(1e-1):7.1f}  t(|a|<1e-2)={tcross(1e-2):7.1f}  max|u|={umax:.3f} max|V|={Vmax:.3f}")
