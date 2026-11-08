#!/usr/bin/env python3
"""Exact finite examples for the local convolution factorization theorem.

This verifies only finite algebraic identities; the general proof is analytical.
"""
from fractions import Fraction as Q
from functools import reduce

COUNT = 0

def eq(a, b):
    global COUNT
    assert a == b, (a, b)
    COUNT += 1

def cv(x,y):
    z = [Q(0)]*8
    for i, u in enumerate(x):
        for j,v in enumerate(y):
            z[i^j] += u*v
    return z

def prod(xs):
    return reduce(cv, xs, [Q(1)]+[Q(0)]*7)

def scale(x,t): return [t*u for u in x]
def add(x,y): return [u+v for u,v in zip(x,y)]
def sub(x,y): return [u-v for u,v in zip(x,y)]
def norm(x): return sum(map(abs,x),Q(0))

def projection(chi):
    # On Z_2^2 inside Z_2^3, characters (-1)^<chi,g>.
    z=[Q(0)]*8
    for h in range(4):
        z[h] = Q((-1)**((chi & h).bit_count()%2),4)
    return z

P=[projection(chi) for chi in range(4)]
I=[Q(1)]+[Q(0)]*7
ZERO=[Q(0)]*8

def coefficient_on_H(x,chi):
    return sum(x[h]*(-1)**((chi & h).bit_count()%2) for h in range(4))

for chi in range(4):
    eq(cv(P[chi],P[chi]),P[chi]); eq(norm(P[chi]),Q(1))
    for psi in range(4):
        eq(cv(P[chi],P[psi]),P[chi] if chi==psi else ZERO)
eq([sum(P[chi][i] for chi in range(4)) for i in range(8)],I)

for k in range(2,6):
    for m in range(k+1):
        spectra=[]
        for j in range(k):
            row=[Q(2+j+chi,2+j) for chi in range(4)]
            if j<m: row[0]=Q(0)
            if k>=3 and j==k-1 and m<k-1: row[2]=Q(0)
            spectra.append(row)
        base=[ [sum((spectra[j][chi]*P[chi][g] for chi in range(4)),Q(0)) for g in range(8)] for j in range(k)]
        s=prod(base)
        t=Q(1,80)
        zero_counts=[sum(spectra[j][chi]==0 for j in range(k)) for chi in range(4)]
        exponent=max(1,max(zero_counts))
        minc=min((reduce(lambda x,y:x*y,(abs(spectra[j][chi]) for j in range(k) if spectra[j][chi]!=0), Q(1)) for chi in range(4)),default=Q(1))
        delta=minc*t**exponent/Q(2)
        outside=[Q(0)]*8; outside[4]=delta
        target=add(s,outside)
        blocks=[[scale(P[chi],spectra[j][chi]) for chi in range(4)] for j in range(k)]
        for chi in range(4):
            zeros=[j for j in range(k) if spectra[j][chi]==0]
            qchi=cv(P[chi],target)
            if not zeros:
                denom=reduce(lambda x,y:x*y, (spectra[j][chi] for j in range(1,k)),Q(1))
                blocks[0][chi]=add(blocks[0][chi],scale(sub(qchi,cv(P[chi],s)),Q(1)/denom))
            else:
                for j in zeros[:-1]: blocks[j][chi]=scale(P[chi],t)
                denom=t**(len(zeros)-1)*reduce(lambda x,y:x*y,(spectra[j][chi] for j in range(k) if j not in zeros),Q(1))
                blocks[zeros[-1]][chi]=scale(qchi,Q(1)/denom)
        factors=[[sum((blocks[j][chi][g] for chi in range(4)),Q(0)) for g in range(8)] for j in range(k)]
        eq(prod(factors),target)
        for j in range(k):
            assert norm(sub(factors[j],base[j])) < Q(1,10)
            eq(sum(coefficient_on_H(base[j],chi)*P[chi][g] for chi in range(4) for g in [0]),base[j][0])
        for chi in range(4):
            eq(cv(P[chi],prod(factors)),cv(P[chi],target))
        eq(delta>0,True)

print(f"EXACT_FINITE_CONVOLUTION_MODULI_OK {COUNT}")
