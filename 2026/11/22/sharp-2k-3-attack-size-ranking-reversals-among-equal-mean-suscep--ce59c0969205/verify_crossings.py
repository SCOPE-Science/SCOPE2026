"""Numerical stress tests for sharp equal-mean epidemic ranking reversals.
Finite checks are illustrative; the general proof uses exponential-sum zero counts.
"""
import math
from fractions import Fraction
import numpy as np

s0, i0, r0 = .9, .1, 0.0

def poly_mul(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def laws(k):
    qs=[Fraction(j,2*k-2) for j in range(1,2*k-2)]
    p=[Fraction(1)]
    for q in [Fraction(1),Fraction(1)]+qs:
        p=poly_mul(p,[-q,Fraction(1)])
    assert len(p)==2*k
    assert sum(p)==0
    assert sum((j+1)*p[j] for j in range(len(p)))==0
    a=sum(c for c in p if c>0)
    b=sum(-c for c in p if c<0)
    assert a==b and a>0
    pos=[(j+1,float(c/a)) for j,c in enumerate(p) if c>0]
    neg=[(j+1,float(-c/a)) for j,c in enumerate(p) if c<0]
    assert len(pos)==len(neg)==k
    return qs,pos,neg

def g(a,law):return sum(w*math.exp(-lam*a) for lam,w in law)
def eta_at_a(a, law):return a/(1-r0-s0*g(a,law))
def root(eta,law):
    left,right=0.,eta*(1-r0)
    for _ in range(100):
        mid=(left+right)/2
        if 1-r0-s0*g(mid,law)-mid/eta>0:left=mid
        else:right=mid
    return (left+right)/2

def attack(eta,law):return root(eta,law)/eta-i0

assert laws(2)[1] == [(2,2/3),(4,1/3)]
assert laws(2)[2] == [(1,1/6),(3,5/6)]
checks=0
for k in (2,3,4,5):
    qs, law_a, law_b=laws(k)
    mean_a=sum(x*w for x,w in law_a)
    mean_b=sum(x*w for x,w in law_b)
    assert abs(mean_a-mean_b)<1e-12
    crossings=sorted(-math.log(float(q)) for q in qs)
    for a in crossings:
        eta_a=eta_at_a(a,law_a)
        eta_b=eta_at_a(a,law_b)
        assert abs(eta_a-eta_b)<2e-12
        assert abs(attack(eta_a,law_a)-attack(eta_a,law_b))<2e-12
        checks+=3
    bounds=[0.2]+crossings+[crossings[-1]+1]
    for j in range(len(bounds)-1):
        a=(bounds[j]+bounds[j+1])/2
        eta=eta_at_a(a,law_a)
        sa=attack(eta,law_a);sb=attack(eta,law_b)
        assert abs(sa-sb)>2e-11
        checks+=1
q,la,lb=laws(2)
assert q==[Fraction(1,2)]
a=math.log(2)
assert abs(eta_at_a(a,la)-160*math.log(2)/133)<1e-12
print('PASS:',checks,'crossing and equal-mean checks; k=2..5; exact rational polynomial construction.')
