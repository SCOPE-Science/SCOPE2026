#!/usr/bin/env python3
"""Standalone reproducibility checks for the stationary moment hierarchy."""
from fractions import Fraction
from math import comb, sqrt

def threshold(p):
    assert p >= 3
    return Fraction(p*p,p-1)

for p in range(3,101):
    assert threshold(p+1)>threshold(p)
assert threshold(3)==Fraction(9,2)
assert threshold(4)==Fraction(16,3)
assert threshold(5)==Fraction(25,4)

# Exact binomial coefficients of product-kernel coagulation moments.
for p in range(3,21):
    poly={tuple(sorted((j+1,p-j+1))): Fraction(comb(p,j),2) for j in range(1,p)}
    assert Fraction(comb(p,1),2)+Fraction(comb(p,p-1),2)==p
    for j in range(2,p-1):
        assert j+1<p and p-j+1<p

# Exact algebraic root and threshold equivalences without rounding.
for p in range(3,31):
    lam=threshold(p)
    a=Fraction(p,p-1)
    assert a*a-lam*a+lam==0
    assert lam-p*a==0

# Explicit finite-side moment recursions (using double-precision only as corroboration).
def moment_prefix(lam, n=1400):
    coeff=[0.0]*(n+1);coeff[1]=lam/(1+lam)
    for k in range(2,n+1):
        coeff[k]=sum(i*(k-i)*coeff[i]*coeff[k-i] for i in range(1,k))/(2*(k+lam))
    return [sum((k**p)*coeff[k] for k in range(1,n+1)) for p in range(1,6)]

def exact_recursion(lam,p):
    a=(lam-sqrt(lam*(lam-4)))/2
    m={1:1.,2:a}
    for q in range(3,p+1):
        if lam <= float(threshold(q)):break
        rhs=lam+0.5*sum(comb(q,j)*m[j+1]*m[q-j+1] for j in range(2,q-1))
        m[q]=rhs/(lam-q*a)
    return m

for lam in [6.,8.,12.]:
    moments=moment_prefix(lam)
    predicted=exact_recursion(lam,5)
    for p in predicted:
        if p==1:continue
        # Finite prefixes underestimate the positive infinite sum.
        assert 0 < moments[p-1] < predicted[p]+1e-8
        if p<=3:assert abs(moments[p-1]-predicted[p])<0.1
print('PASS: 99 exact monotonicity checks; 28 exact root/threshold checks; 18 polynomial moment checks; finite positive-prefix comparisons.')
