#!/usr/bin/env python3
"""Reproduce the finite-cycle lifting Pareto theorem: exact threshold and direct checks.
Python 3 standard library only. Numerical tests are supplementary to the proof.
"""
from fractions import Fraction as Q
import math, random, cmath

def harmonic_columns(q):
    return [[Q(q+1-t,q+1),Q(t,q+1)] for t in range(1,q+1)]

def thomas(q, rhs, lam):
    d=[2.+lam]*q; r=list(rhs)
    for i in range(1,q):
        c=-1/d[i-1]
        d[i]+=c
        r[i]-=c*r[i-1]
    v=[0.]*q
    v[-1]=r[-1]/d[-1]
    for i in range(q-2,-1,-1):
        v[i]=(r[i]+v[i+1])/d[i]
    return v

def ndot(a,b):return sum(x*y for x,y in zip(a,b))

def modes(q, beta):
    bp=([1/math.sqrt(2)]+[0.]*(q-2)+[1/math.sqrt(2)],
        [1/math.sqrt(2)]+[0.]*(q-2)+[-1/math.sqrt(2)])
    out=[]
    for h in bp:
        raw=thomas(q,h,0.)
        s=ndot(raw,raw)
        if beta>=s: v,lam=raw,0.
        elif beta==0: v,lam=[0.]*q,float('inf')
        else:
            lo,hi=0.,1.
            while ndot(thomas(q,h,hi),thomas(q,h,hi))>beta: hi*=2
            for _ in range(90):
                md=(lo+hi)/2;vv=thomas(q,h,md)
                if ndot(vv,vv)>beta: lo=md
                else: hi=md
            lam=(lo+hi)/2
            v=thomas(q,h,lam)
        out.append((v,lam,s))
    plus,minus=out
    t=[[ (plus[0][i]+minus[0][i])/math.sqrt(2), (plus[0][i]-minus[0][i])/math.sqrt(2)] for i in range(q)]
    return t,out

def arc_energy(cols,q):
    e=0.
    for j in range(len(cols[0])):
        a=float(j==0); b=float(j==1)
        vals=[a]+[row[j] for row in cols]+[b]
        e+=sum((vals[i+1]-vals[i])**2 for i in range(q+1))
    return e

def frob(cols):return math.sqrt(sum(float(z*z) for row in cols for z in row))

checks=0
for q in range(2,31):
    h=harmonic_columns(q)
    p=[(row[0]+row[1])/Q(2**0,1) for row in h]
    m=[(row[0]-row[1]) for row in h]
    sp=sum(x*x for x in p)/2
    sm=sum(x*x for x in m)/2
    assert sp==Q(q,2)
    assert sm==Q(q*(q-1),6*(q+1))
    assert sum((h[i][0]-h[i][1])**2 for i in range(q))==2*sm
    assert sum((h[i][0]+h[i][1])**2 for i in range(q))==2*sp
    # Harmonic trace energy, exact rational.
    def arc_exact(j):
        vv=[Q(1 if j==0 else 0)]+[row[j] for row in h]+[Q(1 if j==1 else 0)]
        return sum((vv[i+1]-vv[i])**2 for i in range(q+1))
    assert arc_exact(0)+arc_exact(1)==Q(2,q+1)
    checks+=6
    for beta in [0., float(sm)*0.04,float(sm)*0.40,float(sm), float((sp+sm)/2),float(sp),float(sp)*1.4]:
        T,info=modes(q,beta)
        bp, bm=info
        assert abs(bp[2]-float(sp))<1e-8 and abs(bm[2]-float(sm))<1e-8
        # Reflection and modal orthogonality are exact up to roundoff.
        for i in range(q):
            assert abs(T[i][0]-T[q-1-i][1])<1e-8
        s1=ndot(bp[0],bp[0]);s2=ndot(bm[0],bm[0])
        assert abs(max(s1,s2)-min(beta,float(sp)))<1e-8
        e=arc_energy(T,q)
        assert e>=float(Q(2,q+1))-1e-8 and e<=2+1e-8
        if beta==0: assert abs(e-2)<1e-9
        if beta>=float(sp): assert abs(e-float(Q(2,q+1)))<1e-8
        # Independent eigen-sine formula for constrained norms.
        for parity,(v,lam,s) in enumerate(info):
            if math.isfinite(lam):
                val=4/(q+1)*sum(math.sin(math.pi*k/(q+1))**2/(
                    2-2*math.cos(math.pi*k/(q+1))+lam)**2
                    for k in range(1,q+1) if k%2==(1 if parity==0 else 0))
                assert abs(val-ndot(v,v))<1e-7
        checks+=7
        # Stress test arbitrary COMPLEX-linear completion coefficients represented by real matrices.
        if 0<beta<float(sp):
            rng=random.Random(71*q+round(beta*1e7))
            for _ in range(40):
                cols=[[rng.uniform(-1,1) for _ in range(3)] for j in range(q)]
                # Interior input is zero at both endpoints; its Dirichlet contribution is >=0.
                scale=math.sqrt(beta)/max(frob(cols),1e-20)
                cols=[[scale*z for z in row] for row in cols]
                assert arc_energy(cols,q) >=e-1e-7
                checks+=1

# DFT Parseval checks for the host lift (one frequency channel already a Parseval bank).
for q in range(2,9):
    m=3;N=m+q
    T,_=modes(q,float(Q(q,2))/3)
    f=[complex(1.,0.3),complex(-.5,.8),complex(.1,-.7)]
    w=f+[T[i][0]*f[0]+T[i][1]*f[-1] for i in range(q)]
    c=[sum(w[n]*cmath.exp(-2j*math.pi*k*n/N) for n in range(N))/math.sqrt(N) for k in range(N)]
    assert abs(sum(abs(x)**2 for x in w)-sum(abs(z)**2 for z in c))<1e-9
    checks+=1
print('PASS:',checks,'exact-identity, spectral, numerical and feasible-competitor checks')
