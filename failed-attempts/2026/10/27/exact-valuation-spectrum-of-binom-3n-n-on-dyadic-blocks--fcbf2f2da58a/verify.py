#!/usr/bin/env python3
"""Finite cross-checks of the stated binomial-valuation block formulas."""
from fractions import Fraction
from collections import Counter

def sub(a,b):
    z=Counter(a)
    for k,v in b.items():z[k]-=v
    return {k:v for k,v in z.items() if v}
def add(a,b):
    z=Counter(a)
    for k,v in b.items():z[k]+=v
    return {k:v for k,v in z.items() if v}
def mult(a,b):
    z=Counter()
    for k,v in a.items():
        for l,w in b.items():z[k+l]+=v*w
    return {k:v for k,v in z.items() if v}

def mean(L):
    return Fraction(L,2)-Fraction(2,3)+Fraction(3+(-1)**L,6*2**L)
def variance(L):
    return (Fraction(11*L,12)-Fraction(14,9)
            +Fraction(5+(-1)**L,3*2**L)
            -Fraction((3+(-1)**L)**2,36*4**L))
P=[{0:1},{0:2},{0:3,2:1}]
for L in range(13):
    if L>=3:
        P.append(add(sub(add(mult({0:1,1:1},P[L-1]),mult({0:1,2:1},P[L-2])),mult({1:1},P[L-2])),{k:-v for k,v in mult({1:1,2:1},P[L-3]).items()}))
    observed=Counter(2*n.bit_count()-(3*n).bit_count() for n in range(1<<L))
    assert dict(observed)==P[L],(L,observed,P[L])
    assert sum(P[L].values())==1<<L
    m=Fraction(sum(k*v for k,v in P[L].items()),1<<L)
    v=Fraction(sum(k*k*v for k,v in P[L].items()),1<<L)-m*m
    assert m==mean(L),(L,m,mean(L))
    assert v==variance(L),(L,v,variance(L))

# A separate carry-by-carry computation checks the terminal-state output.
for L in range(10):
    for n in range(1<<L):
        c=0
        total=0
        for i in range(L):
            x=(n>>i)&1
            y=(3*x+c)&1
            d=(3*x+c)//2
            total+=2*x-y
            c=d
        total-=c.bit_count()
        assert total==2*n.bit_count()-(3*n).bit_count()
print('VERIFY_OK: exact 13 block polynomials, normalized moments, 1023 independent carry words')
