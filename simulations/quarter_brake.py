"""Braking with the drive at w0/4 only: branching law u = branch of (-R a/kappa4)^{1/4}, a estimated by a lock-in
amplifier at w0.  The resonant amplitude is reported from y minus the (known, leading-order) non-resonant response."""
import numpy as np
from quarterdrive import *
from quarter_validate2 import particular
dt = 0.02
def brake(name, a0=0.05, R=0.01, T=1500.0, tau=6.0, phase0=0.0):
    a0 = a0*np.exp(1j*phase0)
    y, yd, t = a0.real, -a0.imag, 0.0; u = 0j
    li = LockIn(tau); li.z1 = li.z2 = a0; rep = LockIn(tau); rep.z1 = rep.z2 = a0
    n = int(T/dt); amp = np.empty(n); umax = 0.0; ymax = 0.0
    for i in range(n):
        a_est = li(y, yd, t, dt)
        if name == "branching":
            roots = (-R*a_est/kappa4 + 0j)**0.25 * 1j**np.arange(4)
            u = roots[0] if i == 0 else roots[np.argmin(abs(roots-u))]
        y, yd = step(t, y, yd, u, dt); t += dt
        py, pyd = particular(u, t)
        amp[i] = abs(rep(y-py, yd-pyd, t, dt)); umax = max(umax, abs(u)); ymax = max(ymax, abs(y))
    first = lambda lev: (np.argmax(amp < lev)+1)*dt if (amp < lev).any() else float('inf')
    return amp, umax, ymax, first
R = 0.01
print(f"Q=1e4: natural time to 1/e = {1/gam:.0f};  target rate R={R}: time to 1/e = {1/(R+gam):.0f}")
for name in ("none", "branching"):
    for ph in ((0.0,) if name == "none" else (0.0, 1.0, 2.0, 3.0)):
        amp, umax, ymax, first = brake(name, phase0=ph)
        print(f"{name:9s} phase0={ph:.1f}: |a| at t=100 {amp[int(100/dt)]:.4f}, t=300 {amp[int(300/dt)]:.5f}, "
              f"t=1500 {amp[-1]:.2e}; t(|a|<0.005)={first(0.005):.0f}; max|u|={umax:.3f}, max|y|={ymax:.3f}")
