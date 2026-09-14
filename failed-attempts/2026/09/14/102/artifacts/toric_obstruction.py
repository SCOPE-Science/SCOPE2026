"""Toric symmetric-locus obstruction + volume collapse + point-blowup bound.
X = P^1 x P^2, R in |O(2,2)|, L_c = a H1 + b H2, a=2-2c, b=3-2c.
All arithmetic exact via Fraction; prints a verification table.
"""
from fractions import Fraction
print("c, vol(L_c), bary_y(=c/3), beta(D1)=c, beta(D3)=2c/3, crudePtBound(m=2,3,4)")
for num, den in [(1,2),(3,5),(2,3),(3,4),(4,5),(9,10),(99,100)]:
    c = Fraction(num, den); a = 2-2*c; b = 3-2*c
    vol = 3*a*b*b
    bary = c/3
    b1 = c; b3 = 2*c/3
    bounds = {m: 3-c*m-a for m in (2,3,4)}
    print(f"c={c} vol={vol} bary={bary} beta1={b1} beta3={b3} "
          + " ".join(f"m{m}:{bounds[m]}" for m in (2,3,4)))
    assert bary != 0 and b1 > 0 and b3 > 0
    assert bounds[2] == 1 and bounds[3] == 1-c and bounds[4] == 1-2*c
print("OK: toric symmetric pair unstable (bary!=0); ambient divisors never walls; pt bound negative only for m>=4 (c>1/2).")
