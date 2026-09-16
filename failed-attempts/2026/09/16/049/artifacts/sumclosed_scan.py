"""Bounded scan of sum-closed growth rates near lambda_B.

Sum-closed class with indecomposable counts (a_1..a_k) has growth rate gamma
solving sum_n a_n gamma^{-n} = 1, i.e. A(r)=1 with r=1/gamma, A(x)=sum a_n x^n.
We enumerate small profiles and solve for gamma, then look at values near lambda_B.
Finite profiles can only give isolated values (intervals need infinite languages),
so this is a bounded recovery test, not a proof.
"""
import itertools
import numpy as np

LAMBDA_B = 2.3569834130780735

def growth_of_profile(a):
    # a[0] = a_1; polynomial: sum a_n r^n - 1 = 0, smallest positive root r -> gamma=1/r
    # coeffs highest-degree-first: [a_k, ..., a_1, -1]
    coeff = [float(v) for v in reversed(a)] + [-1.0]
    roots = np.roots(coeff)
    rmin = None
    for r in roots:
        if abs(r.imag) < 1e-8 and r.real > 1e-9:
            if rmin is None or r.real < rmin:
                rmin = r.real
    return (1.0 / rmin) if rmin else None

vals = set()
profiles = {}
# enumerate a_1 in 1..3, a_2..a_6 in 0..3, keep it bounded
ranges = [range(1, 4)] + [range(0, 4)] * 5
count = 0
for a in itertools.product(*ranges):
    if sum(a) == 0:
        continue
    g = growth_of_profile(a)
    count += 1
    if g is not None and 2.0 < g < 2.8:
        vals.add(round(g, 6))
        profiles.setdefault(round(g, 6), a)

sv = sorted(vals)
print(f"enumerated {count} profiles, {len(sv)} distinct rounded values in (2.0,2.8)")
print(f"lambda_B = {LAMBDA_B}")
below = [v for v in sv if LAMBDA_B - 0.12 <= v < LAMBDA_B]
above = [v for v in sv if LAMBDA_B <= v <= LAMBDA_B + 0.12]
print(f"values in [lambda_B-0.12, lambda_B): n={len(below)}")
for v in below:
    print(f"  {v:.6f}  profile={profiles[v]}")
print(f"values in [lambda_B, lambda_B+0.12]: n={len(above)}")
for v in above:
    print(f"  {v:.6f}  profile={profiles[v]}")
# gap check just below lambda_B among these finite profiles
if below:
    gaps = [below[i + 1] - below[i] for i in range(len(below) - 1)]
    print(f"max consecutive gap below window: {max(gaps) if gaps else 0:.6f}")
    print(f"distance of closest below-value to lambda_B: {LAMBDA_B - max(below):.6f}")
print("NOTE: finite profiles yield isolated points by construction; absence/presence")
print("of nearby points says nothing about infinite-language interval covering")
print("nor about non-sum-closed classes. Recovery test: INCONCLUSIVE (expected).")
