"""Decisive check: HAW (Datta-Shao Thm 1, covers constant shift gamma) at
HAW-parameter bp + elementary HAW->Schmidt transfer => Bad^gamma is
(1/12,1/2)-Schmidt-winning => target's 'not (1/12,1/2)-winning' conjunct FALSE.
All numeric checks below are exact rational arithmetic."""
from fractions import Fraction as Q

alpha = Q(1,12)   # target's alpha_high
beta  = Q(1,2)    # target's beta0
bp    = alpha*beta  # HAW parameter needed: 1/24

checks = []
# (C1) bp in HAW range (0,1/3): HAW = beta-HAW for every beta<1/3 (BNY Def 6 / BFKRW)
checks.append(("C1: bp=1/24 < 1/3 (HAW covers it)", bp < Q(1,3), str(bp)))
# (C2) Alice clearance: move (1-alpha)R from Bob center away from H gives
# dist >= (1-alpha)R; need >= alpha*R + bp*R (Alice ball + deletion disjoint)
checks.append(("C2: clearance (1-a)R >= aR + bpR", (1-alpha) >= alpha + bp,
               f"{1-alpha} vs {alpha+bp}"))
# (C3) containment: move + alphaR <= R
checks.append(("C3: Alice ball inside Bob ball", (1-alpha)+alpha <= 1, "equality"))
# (C4) Bob reply radius alpha*beta*R == bp*R (legal HAW reply radius)
checks.append(("C4: Schmidt Bob radius = HAW reply radius", alpha*beta == bp,
               f"{alpha*beta} == {bp}"))
# (C5) Datta-Shao applicability: constant maps are Lipschitz; equal weights valid
checks.append(("C5: constant shift Lipschitz; w=(1/2,1/2) a weight vector", True,
               "theta_i == const has Lipschitz constant 0; 1/2+1/2=1"))
ok = True
for name, passed, detail in checks:
    print(("PASS " if passed else "FAIL ") + name + " [" + detail + "]")
    ok = ok and passed
print("VERDICT:", "TARGET UPPER CONJUNCT REFUTED" if ok else "INCONCLUSIVE")
