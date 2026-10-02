"""Stdlib-only verification that the target conjunction is arithmetically impossible.

Checks:
 1. Expand F_claim = (1+y1)(1+y1*y2)(1+y3) + y1*y2*y3*(2+y1+y3) exactly.
 2. Sum all coefficients = F_claim(1,1,1).
 3. Compare with claimed 13 perfect matchings (MSW: F(1,1,1) = #matchings).
"""
from collections import Counter

def poly_mul(a, b):
    out = Counter()
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(x + y for x, y in zip(ma, mb))
            out[m] += ca * cb
    return dict(out)

def poly_add(a, b):
    out = Counter(a)
    for m, c in b.items():
        out[m] += c
    return dict(out)

e1 = (1, 0, 0)
e12 = (1, 1, 0)
e3 = (0, 0, 1)
e123 = (1, 1, 1)
e113 = (2, 1, 1)   # y1^2 y2 y3 = y1*(y1*y2)*y3
e1223 = (1, 1, 2)  # y1*y2*y3^2
zero = (0, 0, 0)

one = {zero: 1}
t1 = {zero: 1, e1: 1}            # (1+y1)
t2 = {zero: 1, e12: 1}           # (1+y1*y2)
t3 = {zero: 1, e3: 1}            # (1+y3)
base = poly_mul(poly_mul(t1, t2), t3)
extra = {e123: 2, e113: 1, e1223: 1}  # y1y2y3*(2+y1+y3)
F = poly_add(base, extra)

print("monomial (e1,e2,e3) -> coeff:")
for m in sorted(F):
    print(f"  {m} -> {F[m]}")
nterms_distinct = len(F)
coeff_sum = sum(F.values())
print(f"distinct monomials: {nterms_distinct}")
print(f"coefficient sum F(1,1,1): {coeff_sum}")
print(f"claimed matchings: 13")
assert coeff_sum == 12, coeff_sum
assert nterms_distinct == 9, nterms_distinct
assert coeff_sum != 13
print("REFUTATION_OK: F_claim(1,1,1)=12 != 13 = claimed #matchings")
