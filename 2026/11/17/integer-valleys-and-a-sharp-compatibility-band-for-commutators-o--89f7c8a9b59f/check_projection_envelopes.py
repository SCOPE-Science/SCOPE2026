"""Arithmetic stress tests for a rank-k projection angle envelope.
Each test is finite, and the analytical argument is the proof.
"""
from math import floor, sqrt
from random import Random

def bounds(k, d):
    assert k >= 1 and 0 <= d <= k
    if d == k:
        return 0.0, 0.0
    m=floor(d); f=d-m
    if f == 0: a=0.0
    else: a=min(f/(k-m), (1-f)/(m+1))
    lo=sqrt(a*(1-a))
    left=max(0.,d-k+1.); right=min(1.,d)
    t=max(left,min(0.5,right))
    hi=sqrt(t*(1-t))
    return lo, hi

def blocks(k,d):
    if d==k: return [[1.0]*k]
    m=floor(d); f=d-m
    return [[1.0]*m + [f/(k-m)]*(k-m),
            [0.0]*(k-m-1) + [1.0-(1.0-f)/(m+1)]*(m+1)]

def max_builder(k,d):
    if d<=0.5: return [d]+[0.]*(k-1)
    if d>=k-0.5: return [1.0]*(k-1)+[d-k+1]
    # put one angle at 1/2, fill remainder greedily
    rem=d-0.5
    t=[0.5]
    for i in range(k-1):
        v=min(1.0,rem); t.append(v); rem-=v
    return t

rng=Random(1442001)
n=0
for k in range(1,11):
    for j in range(1001):
        d=k*j/1000
        lo,hi=bounds(k,d)
        assert lo <= hi + 1e-10, (k,d,lo,hi)
        for t in blocks(k,d)+[max_builder(k,d)]:
            assert len(t)==k
            assert all(-1e-12<=z<=1+1e-12 for z in t)
            assert abs(sum(t)-d)<1e-10,(k,d,t)
            comm=max(sqrt(max(0,z*(1-z))) for z in t)
            assert lo-1e-10 <= comm <= hi+1e-10
        assert min(max(sqrt(max(0,z*(1-z))) for z in t) for t in blocks(k,d))<=lo+1e-10
        assert max(sqrt(max(0,z*(1-z))) for z in max_builder(k,d))>=hi-1e-10
        n+=1
    for j in range(10000):
        v=[rng.random() for _ in range(k)]
        d=sum(v)
        lo,hi=bounds(k,d)
        c=max(sqrt(x*(1-x)) for x in v)
        assert lo-1e-10<=c<=hi+1e-10,(k,v,c,lo,hi)
        n+=1
for k in range(1,11):
    for m in range(k):
        d=m+(k-m)/(k+1)
        lo,hi=bounds(k,d)
        assert abs(lo-sqrt(k)/(k+1))<1e-12
        n+=1
print('PASS',n,'finite construction, random envelope, and integer-cell peak checks')
try:
    import numpy as np
    for k in range(1,7):
        for _ in range(300):
            ts=np.asarray([rng.random() for j in range(k)])
            s=np.sqrt(ts); c=np.sqrt(1-ts)
            P=np.zeros((2*k,2*k)); Q=P.copy()
            for j in range(k):
                P[2*j,2*j]=1
                Q[2*j,2*j]=c[j]*c[j]
                Q[2*j,2*j+1]=Q[2*j+1,2*j]=c[j]*s[j]
                Q[2*j+1,2*j+1]=s[j]*s[j]
            assert np.max(np.abs(P@P-P)) < 2e-15
            assert np.max(np.abs(Q@Q-Q)) < 2e-15
            d=np.linalg.norm(P-Q,'fro')**2/2
            z=np.linalg.norm(P@Q-Q@P,2)
            lo,hi=bounds(k,d)
            assert lo-1e-9<=z<=hi+1e-9
            assert abs(z-max(c*s)) < 2e-12
            n+=1
    print('PASS',n,'including direct matrix orthoprojection checks')
except ImportError:
    print('numpy absent; scalar tests above completed')
