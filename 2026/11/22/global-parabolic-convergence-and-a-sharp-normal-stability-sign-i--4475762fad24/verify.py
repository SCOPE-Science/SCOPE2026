#!/usr/bin/env python3
"""Exact polynomial identities for a balanced cubic Lorenz-like flow.

All coefficients are Fractions. Polynomial comparisons are coefficientwise.
No numerical trajectory or finite sample is treated as an infinite proof.
"""
from fractions import Fraction

NV = 7  # x, y, z, a, beta, gamma, s
ZERO = (0,) * NV

def constant(v):
    q = Fraction(v)
    return {} if not q else {ZERO: q}

def symbol(j):
    e = [0] * NV
    e[j] = 1
    return {tuple(e): Fraction(1)}

def add(*args):
    d = {}
    for a in args:
        for k, v in a.items():
            d[k] = d.get(k, Fraction(0)) + v
            if not d[k]:
                del d[k]
    return d

def neg(a):
    return {k: -v for k, v in a.items()}

def sub(a, b):
    return add(a, neg(b))

def mul(*args):
    z = constant(1)
    for a in args:
        out = {}
        for i, v in z.items():
            for j, w in a.items():
                k = tuple(p + q for p, q in zip(i, j))
                out[k] = out.get(k, Fraction(0)) + v*w
                if not out[k]:
                    del out[k]
        z = out
    return z

def sq(a):
    return mul(a, a)

def der(a, j):
    return {tuple(e-(1 if q==j else 0) for q,e in enumerate(k)): v*k[j]
            for k,v in a.items() if k[j]}

def equal(a,b,what):
    rem=sub(a,b)
    if rem:
        raise AssertionError(f'{what}: {len(rem)} nonzero monomials: {rem}')
    print('PASS', what)

x,y,z,a,b,g,s=(symbol(j) for j in range(NV))
u=sub(y,x)
w=sub(mul(constant(2),a,z),sq(x))
xd=mul(a,u)
yd=add(neg(mul(add(mul(constant(2),a,b),g),y,z)),mul(g,x,z),mul(b,sq(x),y))
zd=add(neg(mul(constant(2),a,z)),sq(y))
ud=sub(yd,xd)
wd=sub(mul(constant(2),a,zd),mul(constant(2),x,xd))
e=add(mul(a,sq(u)),mul(constant(Fraction(1,2)),b,sq(w)))
ed=add(mul(der(e,0),xd),mul(der(e,1),yd),mul(der(e,2),zd))
equal(ud, sub(neg(mul(add(a,mul(g,z)),u)),mul(b,y,w)), 'transverse u equation')
equal(wd,add(neg(mul(constant(2),a,w)),mul(constant(2),a,y,u)), 'transverse w equation')
equal(ed,neg(add(mul(constant(2),a,add(a,mul(g,z)),sq(u)),mul(constant(2),a,b,sq(w)))), 'energy derivative identity')
# Normal linearization, with the symbolic gamma*s^2/(2a) temporarily
# represented by scaling the first row by 2a.
m11_scaled=neg(add(mul(constant(2),sq(a)),mul(g,sq(s))))
m12=neg(mul(b,s))
m21=mul(constant(2),a,s)
m22=neg(mul(constant(2),a))
trace_scaled=add(m11_scaled,mul(constant(2),a,m22))
equal(trace_scaled,neg(add(mul(constant(6),sq(a)),mul(g,sq(s)))), 'scaled normal trace')
det_scaled=sub(mul(m11_scaled,m22),mul(constant(2),a,m12,m21))
expected=mul(constant(2),a,add(mul(constant(2),sq(a)),mul(add(mul(constant(2),a,b),g),sq(s))))
equal(det_scaled,expected,'scaled normal determinant')
for aa,gg in ((1,Fraction(-1,2)),(2,-3),(5,-1)):
    witness=Fraction(7)*aa*aa/(-gg)
    assert -3*aa-Fraction(gg)*witness/(2*aa)>0
print('PASS negative-coupling spectral witnesses')
print('ALL EXACT IDENTITIES VERIFIED')
