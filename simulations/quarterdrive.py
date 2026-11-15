"""Parallel-plate electrostatic resonator, normalised (w0 = 1, gap = 1, stiffness = 1):
    y'' + 2 gam y' + y = beta V^2 / (1 - y)^2,      V(t) = Re(u e^{i t/4})   (drive at w0/4, no DC bias)
Derivation (averaging, leading order in beta):
  V^2 = |u|^2/2 + Re(u^2 e^{it/2})/2.
  Off-resonant response at w0/2:  y_h = Re(Y e^{it/2}),  Y = (beta/2) u^2 / (1 - 1/4) = (2 beta/3) u^2.
  Gap term 2 beta V^2 y:  (u^2 e^{it/2}) x (Y e^{it/2}) gives a resonant force (beta^2/3) Re(u^4 e^{it}),
                          the DC part beta |u|^2 y softens the spring (detuning -beta|u|^2/2).
  Envelope y = Re(a e^{it}):   a' = -gam a - i (beta |u|^2/2) a + kappa4 u^4,   kappa4 = -i beta^2/6.
So the drive at w0/4 acts on the resonance as  a' = kappa4 u^4 :  our model with n = 4 (phase multiplied by 4)."""
import numpy as np
beta, Q = 1.0, 1e4
gam = 1/(2*Q); kappa4 = -1j*beta**2/6
def rhs(t, y, yd, u):
    V = (u*np.exp(1j*t/4)).real
    return yd, -2*gam*yd - y + beta*V*V/(1-y)**2
def step(t, y, yd, u, dt):
    k1 = rhs(t, y, yd, u); k2 = rhs(t+dt/2, y+dt/2*k1[0], yd+dt/2*k1[1], u)
    k3 = rhs(t+dt/2, y+dt/2*k2[0], yd+dt/2*k2[1], u); k4 = rhs(t+dt, y+dt*k3[0], yd+dt*k3[1], u)
    return y+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]), yd+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
class LockIn:                      # demodulate at w0, two cascaded first-order low-pass filters (time constant tau)
    def __init__(s, tau): s.tau = tau; s.z1 = 0j; s.z2 = 0j
    def __call__(s, y, yd, t, dt):
        raw = (y - 1j*yd)*np.exp(-1j*t)
        s.z1 += dt/s.tau*(raw - s.z1); s.z2 += dt/s.tau*(s.z1 - s.z2); return s.z2
def avg_rhs(a, u): return -gam*a - 1j*beta*abs(u)**2/2*a + kappa4*u**4
