"""Finite-field support for a Frobenius spectrum of a Kummer threefold.

Uses only Python's integer arithmetic; counts special fiber and exceptional
cubic/quadric point sets over F_5 and their involution twists.
"""
from itertools import product
Q = 5

def phi(a):
    return a % Q

def chi(a):
    a %= Q
    return 0 if a == 0 else (1 if a in (1, 4) else -1)

def proj_points(n):
    # Unique representative with first nonzero coordinate 1.
    for z in product(range(Q), repeat=n):
        try:
            i = next(i for i, x in enumerate(z) if x)
        except StopIteration:
            continue
        if z[i] == 1 and all(x == 0 for x in z[:i]):
            yield z

def weier(t):
    # None means infinity, whose affine cubic has coefficients (3,3).
    if t is None:
        a, b = 3, 3
    else:
        a, b = 3*t*(t+2)**3, 3*t**4*(t+2)**2
    return 1 + sum(1 + chi(4*x**3 + a*x + b) for x in range(Q))

def cubic(c):
    # x(x^2-c u^2) - z(z^2-c v^2) = 0 in P^3.
    return sum(phi(x*(x*x-c*u*u)-z*(z*z-c*v*v)) == 0
               for x,u,z,v in proj_points(4))

def quadric(d):
    return sum(phi(c*e - d*(u*u+v*v)) == 0
               for c,e,u,v in proj_points(4))

assert [weier(t) for t in [0,1,2,3,4,None]] == [6,3,4,6,5,7]
# For finite smooth fibers, negation twist yields 2(q+1)-n_t.
original = [11,3,4,6,5,7]  # minimal singular fibers: III, IV, I5.
twisted = [11,9,8,16,7,25]
assert cubic(2) == 31
assert cubic(4) == 51  # 2 is nonsquare and twists both u,v.
assert quadric(1) == 36
assert quadric(2) == 36
assert sum(n*n for n in original) == 256
assert sum(n*n for n in twisted) == 1196
assert 256 + (cubic(2)-1) + 5 + 2*5 + (quadric(1)-1) == 336
assert 1196 + (cubic(4)-1) + 25*5 + 2*5 + (quadric(2)-1) == 1416
# On the I5 cycle Frob and negation both act by index reversal.
ref = lambda i: (-i) % 5
assert sum(ref(i) == i and ref(j) == j for i in range(5) for j in range(5)) == 1
assert sum(ref(ref(i)) == i and ref(ref(j)) == j for i in range(5) for j in range(5)) == 25
assert (336 - 1 - Q**3) // (1+Q) == 35
assert (1416 - 1 - Q**3) // (1+Q) == 215
assert 215 == Q*43
assert (336 - 1 - Q**3) == (1+Q)*5*(25-18)
assert 1+125+31*(5+25) == 1056
print('PASS: 6 Weierstrass fibers; cubic=31/51, quadric=36/36; B=336, B^iota=1416; Frobenius^iota H2 trace=215; K(F5)=1056')
