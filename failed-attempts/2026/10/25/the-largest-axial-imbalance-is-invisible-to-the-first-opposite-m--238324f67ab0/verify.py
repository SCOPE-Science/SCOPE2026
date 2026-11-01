#!/usr/bin/env python3
"""Exact finite arithmetic checks for crosspolytope mixed-volume identities."""
from fractions import Fraction as F
from itertools import product
from math import factorial, comb

def formula(ts):
    ts=sorted(ts)
    p=F(1)
    z=F(0)
    for i in range(len(ts)-1):
        p/=1+ts[i]
        z+=p*(2 if i==len(ts)-2 else 1)
    return z

def facet_ratio(ts):
    d=len(ts)
    fac=F(0)
    for signs in product((0,1),repeat=d):
        neg=[i for i in range(d) if signs[i]]
        pos=[i for i in range(d) if not signs[i]]
        weight=F(1)
        for i in neg:weight*=ts[i]
        h=max([1/ts[i] for i in neg]+[ts[i] for i in pos])
        fac+=weight*h
    den=F(1)
    for t in ts:den*=1+t
    return fac/den

def hull_2d(pts):
    pts=sorted(set(pts))
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]
    for p in pts:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0: lower.pop()
        lower.append(p)
    upper=[]
    for p in pts[::-1]:
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def area_2d(pts):
    P=hull_2d(pts)
    return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(P,P[1:]+P[:1])))/2

def planar_direct(t1,t2):
    K=[(F(1),F(0)),(-t1,F(0)),(F(0),F(1)),(F(0),-t2)]
    minus=[(-x,-y) for x,y in K]
    difference=[(x+u,y+v) for x,y in K for u,v in minus]
    area=area_2d(K)
    mixed=(area_2d(difference)-2*area)/2
    return mixed/area

n=0
for d in range(2,8):
    for vals in product((F(1,5),F(1,2),F(3,4),F(1)),repeat=d):
        if d>=6 and n>7000:break
        x=formula(vals)
        assert x==facet_ratio(vals),(d,vals,x,facet_ratio(vals))
        assert F(1)<=x<=F(d)
        n+=1
print('FACET_EXACT_OK',n)
np=0
for a in range(1,11):
 for b in range(1,11):
  for c in range(1,11):
   for e in range(1,11):
    t1,t2=F(a,b),F(c,e)
    if t1>1 or t2>1:continue
    assert planar_direct(t1,t2)==formula([t1,t2])
    np+=1
print('PLANAR_MINKOWSKI_EXACT_OK',np)
