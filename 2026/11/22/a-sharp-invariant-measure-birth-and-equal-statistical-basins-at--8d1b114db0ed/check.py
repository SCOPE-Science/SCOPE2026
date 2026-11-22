#!/usr/bin/env python3
"""Exact polynomial and algebraic certificate for a piecewise-quadratic interval map.

Standard-library only: run python check.py.
The continuum statements in RESULT.md are proved analytically, not by the tests here.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    return trim([((a[i] if i < len(a) else 0) +
                  (b[i] if i < len(b) else 0)) for i in range(max(len(a), len(b)))])


def neg(a):
    return [-v for v in a]


def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def sc(a, s):
    return trim([v*s for v in a])


def ev(p, t):
    v = 0
    for a in reversed(p):
        v = v*t + a
    return v


# Polynomial G_c(x)=16c x^2(1-x)^2, with H_c=G_c-x.
x = [Q(0), Q(1)]
base = mul(mul(x, x), mul([Q(1), Q(-1)], [Q(1), Q(-1)]))
assert base == [Q(0), Q(0), Q(1), Q(-2), Q(1)]

def H(c):
    return add(sc(base, 16*c), neg(x))

crit = Q(27,64)
assert H(crit) == sc(mul(mul(x, [Q(-4), Q(3)]), mul([Q(-1), Q(3)], [Q(-1), Q(3)])), Q(1,4))
assert H(Q(1,2)) == mul(mul(x, [Q(-1), Q(2)]), [Q(1), Q(-6), Q(4)])
assert ev(H(crit), Q(1,3)) == 0
assert ev(H(crit), Q(1,2)) < 0
assert ev(H(Q(1,2)), Q(1,2)) == 0
assert ev(H(Q(1,8)), Q(1,3)) < 0

# Exact saddle-node coefficients: H(x,c)= (64/81)(c-c*)-(9/4)(x-1/3)^2+...
Hc = sc(base,16)
Hcrit = H(crit)
Hxx_half = sum(Hcrit[i]*Q(i*(i-1),2)*Q(1,3)**(i-2) for i in range(2,len(Hcrit)))
assert ev(Hc, Q(1,3)) == Q(64,81)
assert Hxx_half == -Q(9,4)
assert Q(16,27)**2 == -Q(64,81)/Hxx_half

# Computations in the exact quadratic number field Q(sqrt(5)).
def pair(a=0,b=0):
    return Q(a),Q(b)

def plus(u,v):
    return u[0]+v[0], u[1]+v[1]

def minus(u,v):
    return u[0]-v[0], u[1]-v[1]

def times(u,v):
    return u[0]*v[0]+5*u[1]*v[1],u[0]*v[1]+u[1]*v[0]

def pwr(u,n):
    o=pair(1)
    for _ in range(n):o=times(o,u)
    return o

r=(Q(3,4),-Q(1,4))
s=(Q(1,4),Q(1,4))
P=lambda u:plus(pair(Q(1,2)),minus(times(pair(2),u),times(pair(2),pwr(u,2))))
V=lambda u:times(pair(2),pwr(minus(u,pair(Q(1,2))),2))
assert P(r)==s and V(s)==r
assert plus(r,s)==pair(1)
assert plus(r,minus(s,pair(Q(1,2))))==pair(Q(1,2))
assert minus(pair(1),plus(r,minus(s,pair(Q(1,2)))))==pair(Q(1,2))
# G'(r)=16*r*(1-r)*(1-2*r)=6-2 sqrt(5)>1.
Gprime_r=times(pair(16),times(r,times(minus(pair(1),r),minus(pair(1),times(pair(2),r)))))
assert Gprime_r == pair(6,-2)

# Critical right-hand separator and exact basin lengths.
assert 4*crit*(Q(17,18)-Q(1,2))**2 == Q(1,3)
assert Q(1,3)+(Q(17,18)-Q(1,2)) == Q(7,9)
assert Q(1)-Q(7,9) == Q(2,9)

# Selected high-precision orbit diagnostics. Not an exhaustive proof.
with localcontext() as ctx:
    ctx.prec = 85
    def dec(q):
        return Decimal(q.numerator)/Decimal(q.denominator)
    def G(z,c):
        return 16*c*z*z*(1-z)*(1-z)
    c = dec(Q(1,2))
    rdec=(Decimal(3)-Decimal(5).sqrt())/4
    sdec=(Decimal(1)+Decimal(5).sqrt())/4
    assert abs(G(rdec,c)-rdec) < Decimal('1e-75')
    assert abs(Decimal(2)*(sdec-Decimal('0.5'))**2-rdec)<Decimal('1e-75')
    z=Decimal('0.1')
    for _ in range(16):z=G(z,c)
    assert z<Decimal('1e-30')
    z=Decimal('0.4')
    for _ in range(7):z=G(z,c)
    assert Decimal('0.49999')<z<=Decimal('0.5')
    c=dec(crit)
    z=Decimal('0.4')
    for _ in range(8000):z=G(z,c)
    assert Decimal('0.33333')<z<Decimal('0.33340')
    assert abs(Decimal(8000)*(z-Decimal(1)/3)-dec(Q(4,9)))<Decimal('0.002')

print('PASS: exact polynomial identities, critical fold, quadratic-field cycles, basin fractions, and orbit diagnostics')
