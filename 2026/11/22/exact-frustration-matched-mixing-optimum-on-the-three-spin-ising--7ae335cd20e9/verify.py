#!/usr/bin/env python3
"""Exact finite-state checks for a signed three-spin heat-bath Ising system.

The analytical all-parameter proof is in RESULT.md. This script verifies the
finite-state generator reductions for a grid of rational bond Boltzmann factors.
Uses only the Python standard library.
"""
from fractions import Fraction as F
from itertools import product

CONFIGS = tuple(product((-1, 1), repeat=3))
MONOMIALS = ((), (0,), (1,), (2,), (0,1), (1,2), (0,2), (0,1,2))


def monomial(state, vertices):
    out = 1
    for i in vertices:
        out *= state[i]
    return out


def exact_parameters(x, y):
    # x=exp(2 beta K)>1, y=exp(2 beta H)>1
    z = (x*y-1)/(x*y+1)
    w = (x-y)/(x+y)
    a = (z+w)/2
    b = (z-w)/2
    c = (x*x-1)/(2*(x*x+1))
    return a,b,c


def full_generator(x,y):
    # J12=J23=+K, J13=-H
    edges = ((0,1,x,1),(1,2,x,1),(0,2,y,-1))
    Q = [[F(0) for _ in CONFIGS] for _ in CONFIGS]
    index = {s:i for i,s in enumerate(CONFIGS)}
    for i,s in enumerate(CONFIGS):
        for v in range(3):
            odds = F(1)
            for u,w,activity,sgn in edges:
                if v in (u,w):
                    other = w if u==v else u
                    power = sgn*s[v]*s[other]
                    odds *= activity if power==1 else 1/activity
            rate = 1/(1+odds)
            flipped = list(s)
            flipped[v] = -flipped[v]
            j=index[tuple(flipped)]
            Q[i][j]=rate
            Q[i][i]-=rate
    return Q


def expected_action(s, mon, a,b,c):
    x,y,z=s
    if mon==(): return F(0)
    if mon==(0,): return -x+a*y-b*z
    if mon==(1,): return -y+c*x+c*z
    if mon==(2,): return -z+a*y-b*x
    if mon==(0,1): return a+c-2*x*y-b*y*z+c*x*z
    if mon==(1,2): return a+c-2*y*z-b*x*y+c*x*z
    if mon==(0,2): return -2*b-2*x*z+a*(x*y+y*z)
    if mon==(0,1,2): return -3*x*y*z+(a+c)*(x+z)-2*b*y
    raise AssertionError(mon)


def check_pair(xval,yval):
    x,y=F(xval), F(yval)
    a,b,c=exact_parameters(x,y)
    assert 0<a<1 and 0<b<1 and 0<c<F(1,2)
    Q=full_generator(x,y)
    for state_index,s in enumerate(CONFIGS):
        assert sum(Q[state_index])==0
        for mon in MONOMIALS:
            direct = sum(Q[state_index][j]*monomial(ss,mon)
                         for j,ss in enumerate(CONFIGS))
            expected=expected_action(s,mon,a,b,c)
            assert direct==expected,(x,y,mon,s,direct,expected)
    # Distinct spectral blocks can be read off from these monomial identities.
    # Their characteristic polynomial has factors
    # z(z-3)(z-1+b)(z-2+b)
    # [(z-1)^2-b(z-1)-2ac][(z-2)^2-b(z-2)-2ac].
    if y < x:
        assert b<c<a
    elif y==x:
        assert a==b==c
    else:
        assert a<c<b
    return 8*len(MONOMIALS)


def main():
    checked=0
    for x in (F(6,5),F(3,2),F(2),F(3),F(5),F(11),F(17),F(31)):
        for y in (F(11,10),F(7,5),F(2),F(4),F(8),F(13),F(27),F(43)):
            checked+=check_pair(x,y)
    print('GENERATOR_MONOMIAL_IDENTITIES_OK', checked)
    print('INDEPENDENT_EXACT_RATIONAL_PARAMETER_PAIRS', 64)

if __name__=='__main__':
    main()
