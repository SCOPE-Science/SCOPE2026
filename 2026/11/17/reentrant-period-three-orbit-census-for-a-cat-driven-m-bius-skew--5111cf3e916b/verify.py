#!/usr/bin/env python3
"""Exact periodic-base census and Laurent-polynomial SU(1,1) trace identities.

Requires only the Python 3 standard library; all assertions are exact except
explicitly marked floating-point illustrations.
"""
from fractions import Fraction
from itertools import product
from math import sqrt, acos, pi, cos

# Enumerate every fixed point of A^3 using |det(A^3-I)|=16 and its quarter grid.
def cat(p):
    t,s=p
    return ((2*t+s)%1,(t+s)%1)
pts={(Fraction(i,4), Fraction(j,4)) for i,j in product(range(4),repeat=2)}
assert len(pts)==16
assert all(cat(cat(cat(p)))==p for p in pts)
assert sum(cat(p)==p for p in pts)==1
cycles=[]
while pts:
    p=min(pts)
    cyc=[p]
    q=cat(p)
    while q!=p:
        assert q not in cyc
        cyc.append(q)
        q=cat(q)
    pts.difference_update(cyc)
    cycles.append(cyc)
assert sorted(map(len,cycles))==[1,3,3,3,3,3]

# Laurent-polynomial bivariate monomials eps^i z^j over Z, z=e^{i pi mu}.
def mon(i,j=0,c=1):return {(i,j):c}
def add(a,b):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
def mul(a,b):
    out={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            key=(i+k,j+l)
            out[key]=out.get(key,0)+v*w
    return {k:v for k,v in out.items() if v}
def matmul(a,b):
    return [[add(mul(a[i][0],b[0][j]),mul(a[i][1],b[1][j])) for j in range(2)] for i in range(2)]
def matrix(k):
    return [[mon(0,k),mon(1,k)],[mon(1,-k),mon(0,-k)]]
def trace(p):return add(p[0][0],p[1][1])
def decode(t):
    v=[]
    for x,_ in t:
        if x==Fraction(0):v.append(0)
        elif x==Fraction(1,4):v.append(1)
        elif x==Fraction(1,2):v.append(0)
        elif x==Fraction(3,4):v.append(-1)
        else:raise AssertionError('unexpected base itinerary')
    return v

def iter_trace(word):
    p=[[mon(0),{}],[{},mon(0)]]
    for k in word:
        p=matmul(matrix(k),p)
    return trace(p)
exp_null={(0,0):2,(2,0):6}
exp_opp={(0,0):2,(2,0):2,(2,2):2,(2,-2):2}
exp_same={(0,2):1,(0,-2):1,(2,2):1,(2,-2):1,(2,0):4}
seen={}
for cyc in cycles:
    if len(cyc)==1:continue
    w=decode(cyc)
    t=iter_trace(w)
    if sorted(w)==[0,0,0]:kind='zero';expected=exp_null
    elif sorted(w)==[-1,0,1]:kind='opposing';expected=exp_opp
    elif sorted(w)==[0,1,1] or sorted(w)==[-1,-1,0]:kind='same';expected=exp_same
    else:raise AssertionError(w)
    assert t==expected,(w,t,expected)
    seen[kind]=seen.get(kind,0)+1
assert seen=={'opposing':2,'zero':1,'same':2},seen

# In the same-sign case the (1,2) entry of the unnormalized matrix product
# is eps*((1+eps^2)*z^2+2), with a cyclically chosen phase order (1,0,1).
p=[[mon(0),{}],[{},mon(0)]]
for k in (1,0,1):p=matmul(matrix(k),p)
assert p[0][1]=={(1,2):1,(3,2):1,(1,0):2},p[0][1]

for e in (0.03,0.2,0.4,0.8,0.99):
    d=1-e*e
    h=d**1.5
    plus=(h-2*e*e)/(1+e*e)
    minus=(-h-2*e*e)/(1+e*e)
    assert -1<minus<plus<1
    mp=acos(plus)/(2*pi)
    mm=acos(minus)/(2*pi)
    assert 0<mp<mm<.5
    def t_same(mu):return 2*((1+e*e)*cos(2*pi*mu)+2*e*e)/h
    assert t_same(0)>2 and t_same(.5)<-2
    assert abs(t_same(mp)-2)<1e-9
    assert abs(t_same(mm)+2)<1e-9
    assert abs(t_same((mp+mm)/2))<2
    assert abs(t_same((mp+0)/2))>2
    assert abs(t_same((mm+.5)/2))>2
    print('epsilon=',e, 'mu_plus=',round(mp,10),'mu_minus=',round(mm,10))
print('CAT_DRIVEN_PERIOD_THREE_EXACT_CENSUS_OK')
