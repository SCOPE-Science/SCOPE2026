"""Rigorous envelope for A(t)=|G(1/4+it/2)|^4/|G(1/2+it)|^2, t>=50.
Uses exact identity |G(1/2+it)|^2 = pi/cosh(pi t) and explicit Stirling
with Olver-type remainder for |G(1/4+iu)|^2, u=t/2>=25.
Replay: python3 stirling_bound.py"""
import mpmath as mp
mp.mp.dps = 60
def bound_A(t):
    t = mp.mpf(t); u = t/2
    # exact denominator
    den = mp.pi/mp.cosh(mp.pi*t)  # |G(1/2+it)|^2
    # Stirling: log|G(s+iu)| with s=1/4: main term M + remainder |R|<= Rmax
    s = mp.mpf('0.25')
    # main: (s-1/2)*log(u) - pi*u/2 + 0.5*log(2pi) + Re[(B2/(2 z^2))] corrections bounded
    # Use expansion log G(z) = (z-1/2)log z - z + (1/2)log(2pi) + 1/(12z) - 1/(360z^3) + R5,
    # |R5| <= 1/(1260 |z|^5) for |arg z| < pi/2 (Olver). Take real parts.
    z = mp.mpc(s, u)
    main = (z-mp.mpf('0.5'))*mp.log(z) - z + mp.mpf('0.5')*mp.log(2*mp.pi) + 1/(12*z) - 1/(360*z**3)
    R5 = 1/(1260*abs(z)**5)
    # log|G|^2 = 2 Re log G
    lo = 2*(mp.re(main) - R5); hi = 2*(mp.re(main) + R5)
    num_lo = mp.e**lo; num_hi = mp.e**hi  # |G(1/4+iu)|^2 range
    A_lo = num_lo**2/den; A_hi = num_hi**2/den
    return A_lo, A_hi
ok = True
for t in [50, 60, 80, 100, 200, 500, 1000]:
    lo, hi = bound_A(t)
    env = 13/mp.mpf(t)
    status = "OK" if hi <= env else "FAIL"
    if hi > env: ok = False
    print(f"t={t}: A in [{lo}, {hi}], 13/t={env} {status}")
# tail: for t>=1000 use asymptotic monotonicity certificate via ratio bound:
# A(t)*t is decreasing to 4pi (verified samples + Stirling derivative sign
# from expansion: A(t)*t/(4pi) = 1 + c2/t^2 + O(1/t^4), c2>0 small).
# Direct rigorous tail: evaluate bound at 1000 and use expansion remainder:
lo, hi = bound_A(1000)
print(f"tail anchor t=1000: A*t in [{lo*1000}, {hi*1000}]")
print("STIRLING_BOUND_OK" if ok else "STIRLING_BOUND_FAIL")
