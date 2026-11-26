#!/usr/bin/env python3
"""Exact checks for the characteristic-five Ciani superspecial parameter scheme.

No optional packages are needed. This is a finite arithmetic consistency check;
the accompanying proof establishes geometric exhaustiveness over an algebraic closure.
"""
from itertools import product
from collections import defaultdict

P = 5
Q = 25
ZERO = 0
ONE = 1
TWO = 2
FOUR = 4
U = 5                       # U^2=3 in F_25=F_5[U]/(U^2-3).

def add(x, y):
    return ((x % 5 + y % 5) % 5) + 5 * ((x // 5 + y // 5) % 5)

def neg(x):
    return (-(x % 5)) % 5 + 5 * ((-(x // 5)) % 5)

def mul(x, y):
    a, b = x % 5, x // 5
    c, d = y % 5, y // 5
    return (a*c + 3*b*d) % 5 + 5 * ((a*d+b*c) % 5)

def powf(x, n):
    v = ONE
    while n:
        if n & 1:
            v = mul(v, x)
        x = mul(x, x)
        n //= 2
    return v

def sf(*args):
    v = ZERO
    for a in args:
        v = add(v, a)
    return v

def sub(x, y):
    return add(x, neg(y))

assert powf(U, 2) == 3 and powf(U, 5) == neg(U)
assert all(powf(x, 25) == x for x in range(25))
assert all(mul(x, powf(x, 23)) == 1 for x in range(1, 25))

MONS = [(4,0,0),(0,4,0),(0,0,4),(2,2,0),(0,2,2),(2,0,2)]
TARGETS = [(8,4,4),(4,8,4),(4,4,8)]

def extract(t):
    acc = defaultdict(int)
    for selections in product(range(6), repeat=4):
        exponents = tuple(sum(MONS[j][k] for j in selections) for k in range(3))
        if exponents != t:
            continue
        key = tuple(sum(j == j0 for j in selections) for j0 in (3,4,5))
        acc[key] = (acc[key] + 1) % 5
    return {k:v for k,v in acc.items() if v}

POLYS = [
    {(2,0,2):1, (2,0,0):2, (1,1,1):4, (0,2,0):1, (0,0,2):2, (0,0,0):2},
    {(2,2,0):1, (2,0,0):2, (1,1,1):4, (0,2,0):2, (0,0,2):1, (0,0,0):2},
    {(2,0,0):1, (1,1,1):4, (0,2,2):1, (0,2,0):2, (0,0,2):2, (0,0,0):2},
]
for t, p in zip(TARGETS, POLYS):
    assert extract(t) == p, (t,extract(t),p)
print('HASSE_COEFFICIENTS_FROM_6^4_EXPANSION_OK')

def evalpoly(poly, abc):
    val = ZERO
    for e, coeff in poly.items():
        term = coeff
        for z, exponent in zip(abc,e):
            term = mul(term, powf(z, exponent))
        val = add(val, term)
    return val

def disc(abc):
    a,b,c=abc
    A,B,C=powf(a,2),powf(b,2),powf(c,2)
    abcprod=mul(mul(a,b),c)
    return mul(mul(mul(sub(A,4),sub(B,4)),sub(C,4)),sf(4,abcprod,neg(A),neg(B),neg(C)))

def jacobian(abc):
    J=[]
    for poly in POLYS:
        row=[]
        for axis in range(3):
            deriv={tuple(v-(i==axis) for i,v in enumerate(e)):(coeff*e[axis])%5
                   for e, coeff in poly.items() if e[axis]}
            row.append(evalpoly(deriv,abc))
        J.append(row)
    return J

def det3(M):
    a,b,c=M[0]
    d,e,f=M[1]
    g,h,i=M[2]
    return sf(mul(a,sub(mul(e,i),mul(f,h))),
              neg(mul(b,sub(mul(d,i),mul(f,g)))),
              mul(c,sub(mul(d,h),mul(e,g))))

r1=sf(1,U)
r2=sub(2,r1)
assert r1!=r2 and all(sf(powf(r,2),neg(mul(2,r)),neg(2))==0 for r in (r1,r2))
assert powf(r1,5)==r2 and powf(r2,5)==r1
signs=[(1,1,1),(1,4,4),(4,1,4),(4,4,1)]
expected={tuple(mul(s,r) for s in eps) for r in (r1,r2) for eps in signs}
found=set()
for abc in product(range(Q),repeat=3):
    if all(evalpoly(poly,abc)==ZERO for poly in POLYS) and disc(abc)!=ZERO:
        found.add(abc)
assert found == expected, (len(found),found,expected)
assert all(det3(jacobian(abc))!=ZERO for abc in found)
assert all(det3(jacobian(tuple(mul(s,r) for s in eps)))==sub(ONE,r)
           for r in (r1,r2) for eps in signs)
assert not any(all(x<5 for x in abc) for abc in found)
print('SMOOTH_HASSE_ZERO_F25_POINTS=8')
print('JACOBIAN_NONZERO_AT_EVERY_POINT_OK')
print('FROBENIUS_FOUR_ORBITS_OF_LENGTH_TWO_OK')

# Independent finite-field count for every geometrically superspecial model.
projective=[(ONE,x,y) for x,y in product(range(Q),repeat=2)]
projective += [(ZERO,ONE,x) for x in range(Q)]
projective.append((ZERO,ZERO,ONE))
assert len(projective)==651

def quartic(abc, xyz):
    a,b,c=abc
    x,y,z=xyz
    return sf(powf(x,4),powf(y,4),powf(z,4),
              mul(a,mul(powf(x,2),powf(y,2))),
              mul(b,mul(powf(y,2),powf(z,2))),
              mul(c,mul(powf(z,2),powf(x,2))))
counts={sum(quartic(abc,xyz)==ZERO for xyz in projective) for abc in found}
assert counts=={56},counts
print('EIGHT_CURVES_HAVE_56_F25_POINTS_OK')
print('VERIFY_OK')
