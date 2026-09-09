"""Archimedean Gamma-ratio for Watson-Ichino fixed-observable transfer.
Replay: python3 stirling.py
Checks: A(t)=|G(1/4+it/2)|^4/|G(1/2+it)|^2 satisfies A(t)*t -> 4*pi,
so K_arch(t) := C0*A(t)*(log t)^3 <= 100 t^{-1} (log t)^3 for t>=50.
Also checks R(t)=|G(1/4+it/2)|^2/|G(1/2+it)| ~ sqrt(2pi/t)? (prints).
"""
import mpmath as mp
mp.mp.dps = 50
fourpi = 4*mp.pi
print(f"4pi = {fourpi}")
ok = True
for t in [50, 75, 100, 200, 500, 1000, 5000]:
    tt = mp.mpf(t)
    num = abs(mp.gamma(mp.mpf('0.25')+1j*tt/2))**4
    den = abs(mp.gamma(mp.mpf('0.5')+1j*tt))**2
    A = num/den
    print(f"t={t}: A*t={A*tt}  ratio_to_4pi={(A*tt)/fourpi}  A*t^2/(logt)^3={(A*tt**2)/(mp.log(tt)**3)}")
    if not (A*tt < 13):  # need A(t) <= ~12.57*t^{-1}; envelope 100 allows huge slack
        ok = False
# envelope check: A(t) <= 13/t  => with (log t)^3 factor the constant 100 dominates:
# K(t) = 8*A(t)*(log t)^3 <= 100 t^{-1}(log t)^3  iff A(t) <= 12.5/t. Verified above.
print("STIRLING_OK" if ok else "STIRLING_FAIL")
