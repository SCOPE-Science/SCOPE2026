#!/usr/bin/env python3
"""Finite checks for the old-age power-weight recursive-tree variance expansion.
This checker tests finite identities and numerical examples, not an infinite proof.
"""
from fractions import Fraction
from itertools import product
from decimal import Decimal, localcontext
from math import factorial

assertions=0

def require(condition,description):
    global assertions
    if not condition: raise AssertionError(description)
    assertions+=1

def exact_variance_by_enumeration(n, positive_integer_t):
    weights = [Fraction(0)] + [Fraction(1, k**positive_integer_t) for k in range(1, n+1)]
    total = [Fraction(0)]
    for k in range(1,n+1): total.append(total[-1]+weights[k])
    ex=Fraction(0); ex2=Fraction(0); total_prob=Fraction(0)
    for parents in product(*(range(1,j) for j in range(2,n+1))):
        depths=[0]*(n+1)
        probability=Fraction(1)
        for j,parent in enumerate(parents,2):
            depths[j]=1+depths[parent]
            probability*=weights[parent]/total[j-1]
        path=sum(depths)
        ex+=probability*path
        ex2+=probability*path*path
        total_prob+=probability
    require(total_prob==1, 'parent-vector probabilities sum to 1')
    return ex2-ex*ex

def exact_variance_by_innovations(n, positive_integer_t):
    ws=[Fraction(0)]+[Fraction(1,k**positive_integer_t) for k in range(1,n+1)]
    W=Fraction(0);v=Fraction(0);var=Fraction(0)
    for j in range(1,n+1):
        W+=ws[j]
        p=ws[j]/W
        if j>=2:
            var+=(1+(n-j)*p)**2*v
            v=(1-p*p)*v+p*(1-p)
    return var

for t in (1,2,3):
    for n in range(3,8):
        direct=exact_variance_by_enumeration(n,t)
        via=exact_variance_by_innovations(n,t)
        require(direct==via,f'exact finite variance n={n} alpha=-{t}')
        require(direct>0,f'nonzero variance n={n} t={t}')

# Compute the variance coefficient using the established innovation recurrence.
def sigma_decimal(t,terms=160):
    with localcontext() as ctx:
        ctx.prec=125
        W=Decimal(0);v=Decimal(0);s=Decimal(0)
        for j in range(1,terms+1):
            w=Decimal(j)**Decimal(-t)
            W+=w
            p=w/W
            if j>=3: s+=p*p*v
            if j>=2: v=(1-p*p)*v+p*(1-p)
        return +s

for t in (8,16,32,64):
    with localcontext() as ctx:
        ctx.prec=125
        sig=sigma_decimal(t)
        lead=Decimal(18)**(-t)
        next_term=Decimal(32)**(-t)
        rel1=sig/lead
        rel2=(sig-lead)/next_term
        print(f'alpha={-t}, sigma2={sig:.16E}, sigma2/18^alpha={rel1:.12f}, (sigma2-18^alpha)/32^alpha={rel2:.12f}')
        if t==8: require(abs(rel1-1)<Decimal('.02'),'leading ratio t8')
        if t==16: require(abs(rel1-1)<Decimal('.001'),'leading ratio t16')
        if t==32: require(abs(rel2-1)<Decimal('.1'),'second ratio t32')
        if t==64: require(abs(rel2-1)<Decimal('.01'),'second ratio t64')

print(f'PASS: {assertions} exact/projection/numerical assertions')
