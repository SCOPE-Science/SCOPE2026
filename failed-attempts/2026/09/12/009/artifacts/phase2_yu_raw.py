"""Compute RAW Yu-style p-adic bound for ord_{50069}(x(1-x)) from first principles traceable data.
We implement the de Weger/Smart reduction-ready raw bound following Smart 'The algorithmic
resolution of Diophantine equations' + Yu 2007 (Compositio 91:241) shape, conservatively.

S-unit eq x+y=1, S={2,3,7,11,50069}, s=|S|=5. Write x = prod p_i^{e_i} (signed).
Standard: n=4 ratios, D=1 (Q), use Yu Thm: ord_p(Lambda) < C(n,D,...) * max(log B, ...) etc.
We compute EXPLICIT constants per formula quoted in draft (from Smart Ch.IV / Yu Thm 1),
with every parameter logged, then take max with archimedean Baker-Wustholz bound.
Goal per target claim: raw cap below 1e8. If our computed raw cap is below 1e8, Step-a of
target is reproduced; then LLL reduction must tighten to <=3.
"""
import math
P=50069; S=[2,3,7,11,50069]; s=len(S); n=s-1; D=1
print(f"S={S} s={s} n={n} D={D} P={P}")
# ---- Archimedean raw bound (Baker-Wustholz via Smart): generous explicit overestimate ----
# Max exponent B0: standard S-unit height bound h < C_arch; we take documented Smart-style
# bound B0 = 10^30 as safe overestimate? Instead compute real one:
# Use Evertse-type: max|e_i| <= C1 * P * (prod log p_i) * log log? Let's compute both, log them.
logs=[math.log(p) for p in S]
print("log p_i:", [round(v,4) for v in logs], "prod:", math.exp(sum(logs)))
# Baker-Wustholz constant (Thm 2.1, n=4 forms in 4 logs): C_BW ~ 18*(n+1)!*n^{n+1}*(32D)^{n+2}*log(2nD)
# times product of heights; then B0 ~ C_BW * log stuff. Compute transparently:
nBW=4
C_BW = 18*math.factorial(nBW+1)*(nBW**(nBW+1))*((32*D)**(nBW+2))*math.log(2*nBW*D)
print(f"C_BW(n=4) = {C_BW:.4e}")
hmax=max(logs)  # heights of p_i as algebraic numbers
B0_arch = C_BW*(math.prod(logs))*(math.log(max(math.exp(1),C_BW))+50)
print(f"archimedean raw B0 ~ {B0_arch:.4e}  (log10={math.log10(B0_arch):.2f})")
# ---- p-adic Yu raw bound (Yu 2007 Thm 1 shape, as instantiated in Smart/S-unit solvers) ----
# ord_p bound: v <= C_Yu * log B, C_Yu = (16*e*D)^{2n+2} * n^{5/2} * ... * (prod h) * log-factors.
# We use the explicit simplified majorant from von Kanel/Matschke code docs (Yu_bound):
# C1* = (something) — here computed conservatively with all factors shown.
e=math.e
C_Yu = (16*e*D)**(2*n+2) * (n**2.5) * math.log(P) * math.prod(max(h,1.0) for h in logs)
print(f"base C_Yu = {C_Yu:.4e} (log10={math.log10(C_Yu):.2f})")
logB = math.log(max(B0_arch, math.e))
raw_cap = C_Yu*(logB+math.log(max(math.log(P),1))+5)
print(f"raw ord_p cap ~ {raw_cap:.4e} (log10={math.log10(raw_cap):.2f})")
print("raw cap < 1e8 ?", raw_cap < 1e8)
# Also report Sage-doc reference constant scale (~9e9 per admission) for comparison.
