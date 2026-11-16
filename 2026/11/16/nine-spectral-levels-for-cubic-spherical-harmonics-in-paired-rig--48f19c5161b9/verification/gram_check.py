#!/usr/bin/env python3
"""Direct monomial-projection quadrature for cubic harmonic concentration on opposite spherical quadrants."""
import math
from itertools import combinations_with_replacement
import numpy as np
from scipy.special import betainc, poch

def projection_monomial(exp,d):
    # Harmonic projection x^exp - |x|^2 (Delta x^exp)/(2(d+2)).
    p={tuple(exp):1.0}
    for j in range(d):
        if exp[j]<2:continue
        delta=list(exp);delta[j]-=2
        for k in range(d):
            new=list(delta);new[k]+=2;new=tuple(new)
            p[new]=p.get(new,0.0)-exp[j]*(exp[j]-1)/(2*(d+2))
    return {k:v for k,v in p.items() if abs(v)>1e-14}

def moment(e,mask,d):
    if any(x%2 for x in e):return 0.0
    n=sum(e)//2
    v=1.0
    for x in e:v*=float(poch(.5,x//2))
    v/=float(poch(d/2,n))
    if mask:
        a=(e[0]+1)/2;b=(e[1]+1)/2
        v*=float(betainc(b,a,.5))
    return v

def gram(d):
    exps=[]
    for ids in combinations_with_replacement(range(d),3):
        e=[0]*d
        for i in ids:e[i]+=1
        exps.append(tuple(e))
    P=[projection_monomial(e,d) for e in exps]
    n=len(P)
    full=np.zeros((n,n)); obs=np.zeros((n,n))
    cache={}
    for i,p in enumerate(P):
        for j in range(i+1):
            q=P[j]
            total=observed=0.0
            for a,x in p.items():
                for b,y in q.items():
                    e=tuple(u+v for u,v in zip(a,b))
                    if e not in cache: cache[e]=(moment(e,False,d),moment(e,True,d))
                    f,o=cache[e]
                    total+=x*y*f; observed+=x*y*o
            full[i,j]=full[j,i]=total;obs[i,j]=obs[j,i]=observed
    vals, U=np.linalg.eigh(full)
    positive=vals>1e-10
    Q=U[:,positive]/np.sqrt(vals[positive])
    assert int(positive.sum())==d*(d-1)*(d+4)//6,(d,positive.sum())
    actual=np.linalg.eigvalsh(Q.T@obs@Q)
    m=d-2
    dim2=(m+2)*(m-1)//2
    dim3=m*(m+4)*(m-1)//6
    R=math.sqrt((7*d+2)/(d+2))
    a=(R+1)/(3*math.pi);b=(R-1)/(3*math.pi)
    c=math.sqrt(d/(d+2))/math.pi
    spectrum=[]
    for shift,mult in ((a,1),(b,1),(c,m),(1/math.pi,dim2)):
        spectrum +=[.5-shift]*mult+[.5+shift]*mult
    spectrum +=[.5]*(m+dim3)
    expected=np.sort(spectrum)
    assert len(actual)==len(expected)
    err=np.max(np.abs(actual-expected))
    print(f'd={d}: rank={positive.sum()}, max_err={err:.3g}; extremes=({actual[0]:.12f},{actual[-1]:.12f})')
    assert err < 3e-11

for d in range(3,9):gram(d)
print('All direct projected-monomial Gram checks passed.')
