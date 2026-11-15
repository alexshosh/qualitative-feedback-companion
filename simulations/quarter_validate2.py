import numpy as np
from quarterdrive import *
dt = 0.02
def particular(u, t):            # leading-order non-resonant response: static offset + w0/2 component
    y0 = beta*abs(u)**2/2; Y = (2*beta/3)*u**2
    return y0 + (Y*np.exp(1j*t/2)).real, (0.5j*Y*np.exp(1j*t/2)).real
def validate(u, a0=0j, T=300.0, tau=6.0):
    py, pyd = particular(u, 0.0)
    y = py + (a0).real; yd = pyd - (a0).imag      # y = Re(a e^{it}) + particular, at t=0
    t = 0.0; a_avg = a0; li = LockIn(tau); li_m = LockIn(tau); li.z1 = li.z2 = li_m.z1 = li_m.z2 = a0
    errs = []; amps = []
    for i in range(int(T/dt)):
        y, yd = step(t, y, yd, u, dt); t += dt
        a_avg += dt*avg_rhs(a_avg, u)
        est = li(y, yd, t, dt)
        my, myd = (a_avg*np.exp(1j*t)).real, (1j*a_avg*np.exp(1j*t)).real
        py, pyd = particular(u, t)
        ref = li_m(my+py, myd+pyd, t, dt)
        if t > 50: errs.append(abs(est-ref)); amps.append(abs(ref))
    return max(amps), max(errs)
for u in (0.2, 0.25*np.exp(0.3j), 0.3):
    A, E = validate(u)
    print(f"u={u:.3f}: model |a| up to {A:.4f}; max |full - model| {E:.5f} (relative {E/A:.1%}); "
          f"predicted resonant forcing |kappa4 u^4| = {abs(kappa4)*abs(u)**4:.2e}")
# drive off: check that a pure free oscillation is reproduced (sanity)
A, E = validate(0.0, a0=0.05)
print(f"u=0: |a|={A:.4f}, err {E:.2e}")
