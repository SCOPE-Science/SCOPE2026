"""Supplementary finite checks for weighted-square Fourier packing.

The accompanying proof, not these finite examples, proves the real-parameter theorem.
Run: python3 CHECK.py
"""
from fractions import Fraction
from math import acos, cos, pi, sqrt
from cmath import exp
from itertools import product

EPS=2e-9

def P(weights, z, w):
    a,b,c,d=weights
    return a+b*z+c*w+d*z*w

def pair(weights):
    a,b,c,d=weights
    H=a*a+b*b-c*c-d*d
    J=a*b-c*d
    return abs(H)<=2*abs(J)  # handles J=H=0

def triple(weights):
    a,b,c,d=weights
    return ((a==d and b==c and 2*min(a,b)>=max(a,b))
            or (a==d and a==b+c)
            or (b==c and b==a+d))

def maximum(weights):
    a,b,c,d=weights
    if a==b==c==d: return 4
    if triple(weights): return 3
    return 2 if pair(weights) else 1

def positive_roots(weights):
    a,b,c,d=map(float,weights)
    H=a*a+b*b-c*c-d*d
    J=a*b-c*d
    if abs(J)<1e-11:
        return None
    h=-H/(2*J)
    if abs(h)>1+1e-10: return []
    h=max(-1,min(1,h))
    theta=acos(h)
    vals=[]
    for t in (theta,-theta):
        z=exp(1j*t)
        if abs(c+d*z)<1e-11: return None
        w=-(a+b*z)/(c+d*z)
        if abs(abs(w)-1)>1e-8: raise AssertionError('non-unit w')
        vals.append((z,w))
    return vals

count=0
for W in product(range(1,13),repeat=4):
    count+=1
    m=maximum(W)
    assert (m>=2)==pair(W),W
    if m==4: assert len(set(W))==1
    if m==3: assert max(W)*3<=sum(W),W
    roots=positive_roots(W)
    if roots is not None:
        if not roots: assert not pair(W)
        else:
            assert len(roots)==2
            for z,w in roots: assert abs(P(W,z,w))<=EPS*sum(W), W
            if (abs(roots[0][0]-roots[1][0])>1e-8):
                cycle=(abs(roots[0][0]**3-1)<EPS and
                       abs(roots[0][1]**3-1)<EPS)
                assert cycle==triple(W),(W,cycle,triple(W))
            else: assert not triple(W),W

# Explicit three-character non-torsion curves on the opposite-equal-weight locus.
checked=0
for a,b in product(range(1,16), repeat=2):
    if a==b or max(a,b)>2*min(a,b): continue
    r=min(a,b)/max(a,b)
    C=sqrt((1-r)/2)
    angle=acos(C)/(2*pi)
    other=acos(-C/r)/(2*pi)
    if a>=b:
        u,v=angle,other
        t=(u+v,u-v); s=(-u+v,-u-v)
    else:
        u,v=other,angle
        t=(u+v,u-v); s=(u-v,u+v)
    weights=(a,b,b,a)
    for x,y in (t,s,(t[0]-s[0],t[1]-s[1])):
        z=exp(2j*pi*x);w=exp(2j*pi*y)
        assert abs(P(weights,z,w)) < EPS*sum(weights),(a,b,x,y)
        checked+=1

# Algebraic torsion resonance on both unbalanced loci.
omega=exp(2j*pi/3)
for b,c in product(range(1,20),repeat=2):
    a=d=b+c
    assert abs(P((a,b,c,d),omega,omega))<EPS*sum((a,b,c,d))
for a,d in product(range(1,20),repeat=2):
    b=c=a+d
    assert abs(P((a,b,c,d),omega,omega.conjugate()))<EPS*sum((a,b,c,d))
print(f'PASS: {count} positive integer weight quadruples; {checked} nonuniform constructed zero relations; 722 order-three resonance verifications')
