"""Exact rational tests for a planar annulus plank-rigidity argument.

The proof (not this finite test) is in RESULT.md. Standard library only.
"""
from fractions import Fraction as F
from itertools import product

checks = 0

def assert_true(test):
    global checks
    assert test
    checks += 1

# Every (a,b) below is a nonnegative rational Euclidean unit normal.
normals = [(F(1), F(0)), (F(0), F(1))]
for u,v,c in [(3,4,5),(5,12,13),(8,15,17),(7,24,25),(20,21,29),(9,40,41)]:
    normals.extend([(F(u,c),F(v,c)),(F(v,c),F(u,c))])

for a,b in normals:
    assert_true(a*a+b*b == 1)
    for lam in [F(3,2),F(2),F(3),F(5),F(17),F(123,7)]:
        lhs = ((lam-1)*a+lam*b)/(a*a+lam*b*b)
        rhs = 1+(lam-1)*a/(a+b)
        assert_true(lhs <= rhs)
        if a > 0 and b > 0:
            assert_true(lhs < rhs)
        # The coordinate-free budget allocation sums to one.
        assert_true(a/(a+b)+b/(a+b) == 1)

weights = [F(1,10),F(1,7),F(3,10),F(1,4)]
for combo in product(range(len(normals)), repeat=3):
    ns = [normals[i] for i in combo]
    ws = weights[:3]
    W = sum(ws)
    R1 = sum(w*a/(a+b) for w,(a,b) in zip(ws,ns))
    R2 = sum(w*b/(a+b) for w,(a,b) in zip(ws,ns))
    assert_true(R1+R2 == W)
    for lam in [F(2),F(5),F(11)]:
        X1 = sum(w*a/(a*a+lam*b*b) for w,(a,b) in zip(ws,ns))
        X2 = sum(w*lam*b/(a*a+lam*b*b) for w,(a,b) in zip(ws,ns))
        assert_true((lam-1)*X1+X2 <= W+(lam-1)*R1)
        if any(a*b>0 for a,b in ns):
            assert_true((lam-1)*X1+X2 < W+(lam-1)*R1)
        assert_true(X2 <= sum(w/b if b else 0 for w,(a,b) in zip(ws,ns)))

# Canonical two outer layers in each coordinate, including noncentral holes.
interval_holes = [(F(1,8),F(7,8),F(1,16),F(15,16)),
                  (F(1,40),F(9,10),F(1,20),F(19,20)),
                  (F(1,5),F(9,10),F(1,3),F(23,24))]
for (l1,r1,l2,r2) in interval_holes:
    assert_true(0 < l1 < r1 < 1 and 0 < l2 < r2 < 1)
    h1, h2 = r1-l1, r2-l2
    delta1, delta2 = 1-h1,1-h2
    strips = [l1,1-r1,l2,1-r2]
    assert_true(sum(strips) == delta1+delta2)
    assert_true(min(F(1),sum(strips)) <= sum(strips))

print(f"PASS {checks} exact rational assertions")
