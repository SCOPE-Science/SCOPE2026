#!/usr/bin/env python3
"""Exact-rational checks for a boundary fixed-point theorem; proof in RESULT.md."""
from fractions import Fraction as F
from math import ceil

def frac(x):
    return x - (x.numerator // x.denominator)

def map3(k,u,v,w):
    a = frac(k*v*(1-u)+w)
    b = frac(k*v+w*(1+a*a))
    c = frac((k/F(64))*(F(64)+a+b)*(w-w**3/F(6)))
    return a,b,c

def nodes(k):
    if k <= 1:
        return [(F(0),F(0),F(0))] if k < 1 else None
    n = (k-1).numerator // (k-1).denominator
    # j<k-1; if k-1 integer, omit last j.
    if k-1 == n:
        n -= 1
    result=[]
    for j in range(n+1):
        v=F(j)/(k-1)
        y=k*v
        for m in range(j+1):
            u=(y-m)/(1+y)
            result.append((u,v,F(0)))
    return result

def count(k):
    if k < 1: return 1
    if k == 1: return None
    c = (k.numerator + k.denominator - 1)//k.denominator
    return c*(c-1)//2

def test():
    params = [F(1,4),F(1,2),F(999,1000),F(1),F(1001,1000),
      F(5,4),F(1999,1000),F(2),F(2001,1000),F(9,4),F(3),
      F(17,4),F(6),F(63,1),F(64),F(65),F(255),F(511,2)]
    tests=0; total=0
    for k in params:
        pts=nodes(k)
        if k==1:
            for v in [F(0),F(1,9),F(1,2),F(9,10),F(999,1000)]:
                p=(v/(1+v),v,F(0))
                assert map3(k,*p)==p
                tests+=1
            continue
        assert len(pts)==count(k),(k,len(pts),count(k))
        assert len(set(pts))==len(pts)
        for u,v,w in pts:
            assert 0<=u<1 and 0<=v<1 and w==0
            assert map3(k,u,v,w)==(u,v,w),(k,u,v,w)
            if v:
                assert abs(-k*v)>1 and k>1 and k*(1+(u+v)/64)>1
            tests+=1
        total+=len(pts)
    for k in range(2,40):
        n=count(F(k))
        assert n==k*(k-1)//2
        # On K integer, direct row weights differ from bins of density 2v by <= h^2.
        h=F(1,k-1)
        for j in range(k-1):
            w=F(j+1,n)
            truebin=F(2*j+1,(k-1)**2)
            assert abs(w-truebin) <= h*h
            tests+=1
    print(f'PASS: {len(params)} rational parameters; {total} finite fixed states; {tests} exact comparisons; continuum resonance and density bin checks.')

if __name__=='__main__':test()
