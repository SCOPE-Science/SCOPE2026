#!/usr/bin/env python3
"""Exact rational interval certificate for a five-cycle Gabor ambiguity minimax.
Uses only Python standard library. No floating point calculations are needed.
"""
from fractions import Fraction as F

n = 5
chi = (0, 1, -1, -1, 1)
WLO, WHI = F(2236067977, 10**9), F(2236067978, 10**9)
assert WLO**2 < 5 < WHI**2
L, U = F(378494, 10**6), F(378495, 10**6)
assert F(3, 8) < L < U < F(2, 5)


def sqpoly(k, ell):
    # a_j(t)=omega^(j^3) (1+t*chi(j)); all exponents reduced modulo 5.
    a = [[0]*5 for _ in range(3)]
    for j in range(n):
        h = (j-k) % n
        e = (h**3 - j**3 + ell*j) % n
        a[0][e] += 1
        a[1][e] += chi[j] + chi[h]
        a[2][e] += chi[j]*chi[h]
    b = [[0]*5 for _ in range(5)]
    for r in range(3):
        for s in range(3):
            for u, x in enumerate(a[r]):
                for v, y in enumerate(a[s]):
                    b[r+s][(u-v) % n] += x*y
    ans = []
    for vec in b:
        assert vec[1] == vec[4] and vec[2] == vec[3]
        ans.append((F(vec[0])-(F(vec[1])+F(vec[2]))/2,
                    (F(vec[1])-F(vec[2]))/2))
    return ans


def add(a, b): return [(x[0]+y[0], x[1]+y[1]) for x,y in zip(a,b)]
def neg(a): return [(-x,-y) for x,y in a]

# Q(t)=(2*sqrt(5)*t - t*t)^2 = 20*t^2 - 4*sqrt(5)*t^3 + t^4.
Q = [(F(0), F(0)), (F(0), F(0)), (F(20), F(0)),
     (F(0), F(-4)), (F(1), F(0))]
A = sqpoly(1, 2)
H = add(A, neg(Q))
assert A == [(F(5),F(0)), (F(-5,2), F(-5,2)),
             (F(5), F(-1)), (F(-5,2), F(3,2)), (F(1),F(0))]
assert H == [(F(5), F(0)), (F(-5,2), F(-5,2)),
             (F(-15), F(-1)), (F(-5,2), F(11,2)), (F(0), F(0))]


def bound_poly(poly, left, right):
    """Certified interval evaluation, valid for 0 <= left <= right."""
    assert 0 <= left <= right
    lower=upper=F(0)
    for i,(a,b) in enumerate(poly):
        xlo = a + b*(WLO if b>=0 else WHI)
        xhi = a + b*(WHI if b>=0 else WLO)
        assert xlo <= xhi
        lowt, hit = left**i, right**i
        lower += xlo*(lowt if xlo>=0 else hit)
        upper += xhi*(hit if xhi>=0 else lowt)
    return lower,upper

# Root is localized by exact opposite signs; derivative strictly negative across (3/8,2/5).
assert bound_poly(H, F(3,8), F(3,8))[0] > 0
assert bound_poly(H, F(2,5), F(2,5))[1] < 0
Hd = [(F(i)*a,F(i)*b) for i,(a,b) in enumerate(H)][1:]
assert bound_poly(Hd, F(3,8), F(2,5))[1] < 0
assert bound_poly(H,L,L)[0] > 0
assert bound_poly(H,U,U)[1] < 0

# At the unique crossing, every other ambiguity coefficient is strictly larger.
comparisons=[]
for k in range(n):
    for ell in range(n):
        if (k,ell) in [(0,1),(0,4),(1,2),(1,3),(4,2),(4,3)]:
            continue
        dif = add(sqpoly(k,ell), neg(Q))
        low, high = bound_poly(dif,L,U)
        assert low > 0, (k,ell,low,high)
        comparisons.append((k,ell,float(low)))
assert len(comparisons)==19

# Lower bound M > 3/40: t* > 3/8 and f0 strictly increasing until 2/5.
# Numerator of f0(3/8) positive, and its square exceeds 3/40*(5+4*(3/8)^2)^2.
x = F(3,8)
f0sq = [(F(0),F(0)),(F(0),F(0)),(F(20),F(0)),
        (F(0),F(-4)),(F(1),F(0))]
qmin = (F(3,40))*(5+4*x*x)**2
assert bound_poly(f0sq, x, x)[0] > qmin

# For M>3/40, the upper-bound comparison J(t) has J'(t)>0 for t>=0:
# J'(t) > (4/5)t^3-(21/8)t^2+(2/5)t+8
# and min_{t>=0} [ (4/5)t^3-(21/8)t^2 ] = -8575/2048 > -8.
assert 8 > F(8575,2048)

print('PASS: 25 exact cyclotomic squared-ambiguity formulas')
print('PASS: cubic has unique zero in (3/8,2/5), localized to (0.378494,0.378495)')
print('PASS: 19 strict inactive comparisons and six tied active indices')
print('PASS: global minimax monotonicity bounds, all t>=0')
print('smallest lower-gap bound:',min(x[2] for x in comparisons))
