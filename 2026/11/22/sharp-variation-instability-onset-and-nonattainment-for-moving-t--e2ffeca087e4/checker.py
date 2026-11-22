#!/usr/bin/env python3
"""Finite numerical corroboration for local standard-deviation variation stability."""
import math
import random

c=math.sqrt(2)/3
rr=random.Random(9245)

def profile(d):
    return [c*math.sqrt(a*a+a*b+b*b) for a,b in zip(d,d[1:])]

def var(y):
    return sum(abs(b-a) for a,b in zip(y,y[1:]))

def jac_norm(d):
    n=len(d)+1
    al=[];be=[]
    for a,b in zip(d,d[1:]):
        q=math.sqrt(a*a+a*b+b*b)
        assert q>0
        al.append(c*(a+2*b)/(2*q))
        be.append(c*(2*a+b)/(2*q))
    J=[[0.0]*(n-1) for _ in range(max(n-3,0))]
    for k in range(n-2):
        if k>0:
            J[k-1][k-1]+=be[k]
            J[k-1][k]+=al[k]
        if k<n-3:
            J[k][k-1]-=be[k]
            J[k][k]-=al[k]
    return max([sum(abs(row[j]) for row in J) for j in range(n-1)]+[0.0])

lims={3:0,4:math.sqrt(2)/2,5:5*math.sqrt(2)/6,6:math.sqrt(2),7:math.sqrt(2),9:math.sqrt(2)}
for n,K in lims.items():
    for _ in range(1000):
        d=[(1 if rr.random()<.5 else -1)*math.exp(rr.gauss(0,2)) for j in range(n-1)]
        h=[v+rr.gauss(0,.4) for v in d]
        assert jac_norm(d)<=K+1e-10
        assert var([a-b for a,b in zip(profile(d),profile(h))])<=K*sum(abs(a-b) for a,b in zip(d,h))+1e-9
print('RANDOM_TWO_INPUT_AND_JACOBIAN_BV_UPPER_BOUNDS_PASS 6000')
for n,K in lims.items():
    if n==3:continue
    j=1 if n in (4,5) else 2
    d=[.37]*(n-1)
    d[j]=1
    if n==5:
        d[j-1]=-1.e6;d[j+1]=0
    else:
        d[j-1]=0;d[j+1]=-1.e6
    other=d[:];other[j]+=1e-5
    ratio=var([a-b for a,b in zip(profile(other),profile(d))])/1e-5
    assert abs(K-ratio)<1e-4,(n,K,ratio)
    print('STEP_CONTRAST_SHARPNESS_PASS',n,round(ratio,9))
print('THREE_WINDOW_STDDEV_VARIATION_ALL_FINITE_CHECKS_PASS')
