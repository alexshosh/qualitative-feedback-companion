# Resonator simulations (Companion, Section 3.4)

Python 3 with NumPy. Run from this folder.

- `python3 halfdrive_qcontrol.py` — drive at w0/2 (n = 2), model y'' + 2 gam y' + y = V^2, Q = 1e4.
  Prints the time for a tenfold fall of the amplitude (114.3 time units = 18.2 periods for the branching law).
- `python3 quarter_brake.py` — drive at w0/4 (n = 4), parallel-plate model y'' + 2 gam y' + y = V^2/(1 - y)^2, Q = 1e4,
  initial amplitude 0.05 with phases 0, 1, 2, 3. Prints the time for a tenfold fall
  (106 to 173 time units = 16.9 to 27.5 periods).
- `quarterdrive.py` — the n = 4 model, its averaged coefficient kappa4 = -i/6, and the lock-in amplifier.
- `quarter_validate2.py` — compares the averaged n = 4 model with the full model and gives the
  leading-order non-resonant response that is subtracted when the amplitude is reported.

## Settings (moved here from the paper)

- Time normalised so that w0 = 1; quality factor Q = 1e4 (gam = 5e-5).
- Voltage V = Re(u e^{it/n}); u is a branch of (-R a/kappa)^{1/n}, where a is the amplitude read by the controller,
  R the damping rate added by the feedback (0.02 for n = 2, 0.01 for n = 4), kappa = -i/4 for n = 2 and -i/6 for n = 4
  (for n = 4 this averaged coefficient comes from the gap term). The first value is the principal root; after that the
  root nearest the previous control is kept.
- n = 2: starts from y = 1, y' = 0; the amplitude is read as (y - i y') e^{-it}.
- n = 4: starts from amplitude 0.05 with initial phases 0, 1, 2, 3. The controller reads the amplitude from y by a
  lock-in at w0 (two first-order low-pass filters, time constant 6). The amplitude reported is read by a second such
  lock-in after subtracting the leading-order non-resonant response |u|^2/2 + Re((2/3) u^2 e^{it/2}).
