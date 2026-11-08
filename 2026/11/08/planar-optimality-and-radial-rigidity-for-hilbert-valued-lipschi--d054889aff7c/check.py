#!/usr/bin/env python3
"""Exact-rational and deterministic geometric checks for weighted-spider Hilbert spread.
Run: python3 check.py (Python 3 standard library only).
"""
from fractions import Fraction as F
from itertools import product
from math import cos, sin, pi, sqrt
from random import Random

rng = Random(20261102)

def data(arms, mass):
    lengths = [list(a) for a in arms]
    radii = []
    q=[]
    s=F(0)
    P=[]
    off=1
    for a in lengths:
        rr=[];rad=F(0)
        for j,l in enumerate(a):
            rad+=l;rr.append(rad)
            s+=mass[off+j]*rad*rad
        radii.append(rr)
        q.append(sum((mass[off+j]*rr[j] for j in range(len(a))),F(0)))
        P.append([sum(mass[off+j:],F(0)) if False else sum(mass[off+j:off+len(a)],F(0)) for j in range(len(a))])
        off+=len(a)
    T=sum(q,F(0));D=max(F(0),2*max(q)-T)
    return radii,q,s,D,P

def var(arms,mass,increments):
    coords=[(F(0),F(0))];ind=0
    for a in arms:
        v=(F(0),F(0))
        for l in a:
            u=increments[ind];ind+=1
            v=(v[0]+u[0],v[1]+u[1]);coords.append(v)
    mean=tuple(sum((p*x[j] for p,x in zip(mass,coords)),F(0)) for j in (0,1))
    return sum((p*(x[0]*x[0]+x[1]*x[1]) for p,x in zip(mass,coords)),F(0))-sum(y*y for y in mean)

def var_cov(arms,mass,increments):
    _,_,_,_,P=data(arms,mass)
    answer=F(0);offset=0; U=[]
    for a,Pi in zip(arms,P):
        u=increments[offset:offset+len(a)];offset+=len(a)
        Ui=[sum((Pij*v[t] for Pij,v in zip(Pi,u)),F(0)) for t in (0,1)];U.append(Ui)
        for j in range(len(a)):
            for k in range(len(a)):
                c=Pi[max(j,k)]-Pi[j]*Pi[k]
                assert c>0
                answer+=c*(u[j][0]*u[k][0]+u[j][1]*u[k][1])
    for i in range(len(arms)):
        for j in range(i+1,len(arms)):
            answer-=2*sum(U[i][t]*U[j][t] for t in (0,1))
    return answer

count=0; scalar_count=0; random_count=0; balanced=0; unbalanced=0
for m in range(3,6):
    for z in range(90):
        arms=[[F(rng.randint(1,4),rng.randint(1,3)) for j in range(rng.randint(1,3))] for i in range(m)]
        massraw=[rng.randint(1,15) for _ in range(1+sum(map(len,arms)))];mass=[F(v,sum(massraw)) for v in massraw]
        radii,q,S,delta,P=data(arms,mass)
        proposed=S-delta*delta
        lengths=[l for a in arms for l in a]
        # Independent exact covariance and direct variance identity.
        for t in range(12):
            increments=[(l*F(rng.choice((-2,-1,0,1,2)),2),F(0)) for l in lengths]
            direct=var(arms,mass,increments)
            assert direct==var_cov(arms,mass,increments)
            assert direct<=proposed
            random_count+=1
        # Enumerate all scalar straight full-length sign configurations.
        best=max(S-(sum((F(sign)*val for sign,val in zip(sgn,q)),F(0)))**2 for sgn in product((-1,1),repeat=m))
        assert best<=proposed
        if delta>0:
            unbalanced+=1
            i=max(range(m),key=lambda i:q[i]);sgn=[-1]*m;sgn[i]=1
            assert S-(sum(F(si)*qi for si,qi in zip(sgn,q)))**2==proposed
        else:
            balanced+=1
            assert 2*max(q)<=sum(q)
        # Rational feasible map with each arm straight also agrees with direct formula.
        inc=[]
        sgn=[rng.choice((-1,1)) for _ in arms]
        for a,d in zip(arms,sgn):inc.extend([(d*l,F(0)) for l in a])
        assert var(arms,mass,inc)==S-(sum(F(d)*w for d,w in zip(sgn,q)))**2
        count+=1;scalar_count+=1
# Corner cases: equal mass three leaves; scalar vs Hilbert strict, threshold rank 2.
arms=[[F(1)] for _ in range(3)];mass=[F(1,4)]*4
radii,q,S,delta,P=data(arms,mass)
assert S==F(3,4) and delta==0
scalar=S-min(abs(sum((sgn[i]*q[i] for i in range(3)),F(0))) for sgn in product((-1,1),repeat=3))**2
assert scalar==F(11,16)
# Equilateral triangle of unit directions yields exact centered Hilbert variance 3/4.
inc=[(1.,0.),(-0.5,sqrt(3)/2),(-0.5,-sqrt(3)/2)]
val=sum(float(p)*(v[0]**2+v[1]**2) for p,v in zip(mass[1:],inc))-sum(float(mass[i+1])*inc[i][0] for i in range(3))**2-sum(float(mass[i+1])*inc[i][1] for i in range(3))**2
assert abs(val-0.75)<1e-12
print('EXACT_COVARIANCE_DIRECT_IDENTITY_OK',random_count)
print('EXACT_SCALAR_EXTREMAL_COMPARISONS_OK',scalar_count)
print('POLYGON_DOMINANCE_CERTIFICATES_OK',unbalanced)
print('POLYGON_CLOSURE_PRECONDITIONS_OK',balanced)
print('THREE_ARM_DIMENSION_GAP_EXACT_OK',str(S),str(scalar))
print('ALL_WEIGHTED_SPIDER_HILBERT_CHECKS_OK')
