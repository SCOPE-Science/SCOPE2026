#!/usr/bin/env python3
"""Finite numerical checks for a Gaussian-cubic coupled-map theorem.
Analytic statements for all real parameters are proved in RESULT.md.
"""
import math

def rfun(s):
    return (s-1)*math.exp(-s)

def roots(a,b):
    t=(1-2*b)/a
    assert 0<t<math.exp(-2)
    lo,hi=1.0,2.0
    for _ in range(120):
        mid=(lo+hi)/2
        if rfun(mid)<t: lo=mid
        else: hi=mid
    s1=(lo+hi)/2
    lo,hi=2.0,4.0
    while rfun(hi)>t: hi*=2
    for _ in range(120):
        mid=(lo+hi)/2
        if rfun(mid)>t: lo=mid
        else: hi=mid
    return s1,(lo+hi)/2

def f(a,x):
    return a*x*(1-x*x)*math.exp(-x*x)

def T(a,b,x,y):
    return (f(a,x)+b*(y-x),f(a,y)+b*(x-y))

def mult(a,b,s):
    q=2*s*s-5*s+1
    sym=a*math.exp(-s)*q
    anti=sym-2*b
    return sym,anti

def radius_step(a,b,r):
    return abs(f(a,r)-2*b*r)

def main():
    count=0
    for a in (0.12,0.45,0.87,0.99):
        bc=(1-a*math.exp(-2))/2
        for w in (.02,.15,.40,.75,.96):
            b=bc+w*(.5-bc)
            small,large=roots(a,b)
            assert 1<small<2<large
            for s in (small,large):
                r=math.sqrt(s)
                xx,yy=T(a,b,r,-r)
                assert abs(xx+r)<3e-12 and abs(yy-r)<3e-12
                sym,anti=mult(a,b,s)
                assert abs(sym)<1
                if s<2: assert anti<-1
                else: assert -1<anti<1
                count+=1
            r1,r2=math.sqrt(small),math.sqrt(large)
            for frac,target in ((.5*r1,0),(0.97*r1,0),(1.02*r1,r2),(1.7*r2,r2)):
                r=frac
                for _ in range(35000):
                    r=radius_step(a,b,r)
                assert abs(r-target)<0.004, (a,b,w,frac,target,r)
                count+=1
            eigen_0=(a,a-2*b)
            assert all(abs(t)<1 for t in eigen_0)
            count+=1
    # Exact phase-splitting scale as detuning tends to zero.
    a=.5
    bc=(1-a*math.exp(-2))/2
    vals=[]
    for delt in (1e-5,1e-6,1e-7,1e-8):
        s1,s2=roots(a,bc+delt)
        ratio=(s2-s1)/(4*math.e/math.sqrt(a)*math.sqrt(delt))
        vals.append(ratio)
    assert max(abs(x-1) for x in vals)<0.002, vals
    print('PASS: %d cycle, stability, and basin checks; fold ratios '%count, vals)

if __name__=='__main__': main()
