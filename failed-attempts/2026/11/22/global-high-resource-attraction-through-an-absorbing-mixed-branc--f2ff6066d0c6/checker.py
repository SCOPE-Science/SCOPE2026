#!/usr/bin/env python3
"""Exact-rational checks of an invariant high-resource phase of a two-maxima map."""
from fractions import Fraction as Q
import random

def original_step(x,y,a):
    u=a*x*(1-y)
    v=a*y*(1-x)
    return max(u,1-x)/(u+1-x),max(v,1-y)/(v+1-y)

def coordinates(x,y):
    u=(1-x)/x
    v=(1-y)/y
    return u/v,v

def mixed_step(r,b,a):
    return (1+r*b)*(1+b)/(a*a),a*r/(1+r*b)

def unmodified_step(r,b,a):
    x=Q(1,1)/(1+r*b)
    y=Q(1,1)/(1+b)
    xx,yy=original_step(x,y,a)
    return coordinates(xx,yy)

random.seed(20261117)
count=0
for a in [Q(4),Q(5),Q(6),Q(10),Q(100)]:
    for i in range(140):
        den=1000
        nums=sorted(random.sample(range(1,den),2))
        # sample rational odds 0 < u < v < 1
        u,v=Q(nums[0],den),Q(nums[1],den)
        r,b=u/v,v
        switched=False
        for t in range(12000):
            nr,nb=unmodified_step(r,b,a)
            if (1+r*b)>a*r:  # mixed
                er,eb=mixed_step(r,b,a)
                assert (nr,nb)==(er,eb),(a,r,b,nr,nb,er,eb)
                switched=True
                assert nr<Q(4,1)/(a*a) and nb<=1
                for j in range(4):
                    assert (1+nr*nb)>a*nr or (a==4 and nr==Q(1,4) and nb==0)
                    nrr,nbb=unmodified_step(nr,nb,a)
                    frr,fbb=mixed_step(nr,nb,a)
                    assert (nrr,nbb)==(frr,fbb)
                    nr,nb=nrr,nbb
                break
            else:
                assert nr<r
                r,b=nr,nb
        assert switched,(a,nums)
        count+=1
print(f'PASS: {count} exact initial trajectories enter permanently mixed regime; repeated map identities exact.')
# Float convergence to the predicted asymptotic fixed point
import math
float_count=0
for a in (4.,4.25,5.,8.,16.,100.):
    rstar=(a-1)/(a*(a-1)**2-1)
    bstar=1/(a-1)
    for seed in range(250):
        u,v=sorted([random.random(),random.random()])
        r,b=u/v,v
        for t in range(4000):
            # original odds branch, preserving winner order
            A=r*(1+b)/a
            B=(1+r*b)/(a*r)
            new_u=A
            new_v=min(B,1/B)
            r,b=new_u/new_v,new_v
            if abs(r-rstar)+abs(b-bstar)<1e-11:break
        assert abs(r-rstar)+abs(b-bstar)<1e-9,(a,seed,r,b,rstar,bstar)
        float_count+=1
print(f'PASS: {float_count} float initial trajectories converged to exact high-resource limit.')
# Symbolic identities linking the original branch, the planar mixed map, and fixed point.
import sympy as S
rr,bb,aa=S.symbols('r b alpha',positive=True)
F1=(1+bb)*(1+rr*bb)/aa**2
F2=aa*rr/(1+rr*bb)
D=S.Matrix([F1,F2]).jacobian([rr,bb])
assert S.simplify(D[0,0]-bb*(1+bb)/aa**2)==0
assert S.simplify(D[0,1]-(1+rr+2*rr*bb)/aa**2)==0
assert S.simplify(D[1,0]-aa/(1+rr*bb)**2)==0
assert S.simplify(D[1,1]+aa*rr**2/(1+rr*bb)**2)==0
bstar=1/(aa-1)
rstar=(aa-1)/(aa*(aa-1)**2-1)
assert S.simplify(F1.subs({rr:rstar,bb:bstar})-rstar)==0
assert S.simplify(F2.subs({rr:rstar,bb:bstar})-bstar)==0
xstar=S.factor(1/(1+rstar*bstar))
ystar=S.factor(1/(1+bstar))
assert S.simplify(xstar-(1-1/(aa*(aa-1)**2)))==0
assert S.simplify(ystar-(1-1/aa))==0
print('PASS: symbolic Jacobian, positive fixed point and physical-coordinate formulas.')
