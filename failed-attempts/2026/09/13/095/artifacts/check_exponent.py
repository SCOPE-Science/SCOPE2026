"""Repaired check: floored radius r=max(3d,3), explicit N0=12, downgrade 3/8->1/4.
Verifies arm<=C*(d/N)^{1/4} in arm regime and trivial cover otherwise.
Placeholders C_arm, c0 are finiteness stand-ins, not published values.
"""
import math
alpha, beta = 3/8, 1/4
C_arm, c0, m = 8.0, 0.01, 6
N0 = 12
C_main = C_arm * (12**alpha) * (c0**(-m))
C_triv = max(12**0.25, N0**0.25)
C = max(C_main, C_triv)
print(f"C_main={C_main:.6g} C_triv={C_triv:.6g} C={C:.6g} N0={N0}")
ok = True
# arm regime: d>=1, N>=N0, 3d<N/4  -> r=3d (floor inactive since d>=1), r/R=12d/N<1
for N in [12, 20, 100, 1000]:
    for d in [1, 2, 5, N//13, max(1, N//50)]:
        if not (3*d < N/4):
            continue
        ratio = d/N
        arm = C_arm * ((3*d)/(N/4))**alpha * (c0**(-m))
        claim = C_main * ratio**beta
        if not (arm <= claim*(1+1e-9)):
            ok = False
            print(f"FAIL N={N} d={d} arm={arm:.3e} claim={claim:.3e}")
# trivial regime: d/N>=1/12 -> 1<=12^{1/4}(d/N)^{1/4}; small N: 1<=N0^{1/4}(d/N)^{1/4} since d>=1
for ratio in [1/12, 1/4, 1/N0, 0.5]:
    assert 1.0 <= C_triv * ratio**beta + 1e-12, f"trivial cover failed at {ratio}"
print("ARM_REGIME_OK" if ok else "ARM_REGIME_FAIL")
print("TRIVIAL_AND_SMALLN_COVER_OK")
assert math.isfinite(C) and C > 0
print("C_FINITE_OK")
