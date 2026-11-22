#!/usr/bin/env python3
"""Exact finite water-filling and sampled directional consistency checks.
The proof for arbitrary real weights and dimensions is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt
from random import Random

def fill(weights, target):
    """Unique minimum-square vector with x >= weights and sum x=target."""
    a=sorted(weights)
    assert target >= sum(a)
    if target == sum(a):
        return list(weights)
    k=len(a)
    for j in range(1,k+1):
        level=(target-sum(a[j:]))/j
        if level>=a[j-1] and (j==k or level<=a[j]):
            ans=[max(x,level) for x in weights]
            assert sum(ans)==target
            return ans
    raise AssertionError('Water-filling level not located')

def candidate(b, mask):
    N=len(b); S=[i for i in range(N) if mask>>i&1]; T=[i for i in range(N) if not (mask>>i&1)]
    assert S and T
    z=[F(0)]*N
    BS=sum(b[i] for i in S); BT=sum(b[j] for j in T)
    if BS >= BT:
        for i in S: z[i]=b[i]
        vals=fill([b[i] for i in T],BS)
        for i,x in zip(T,vals):z[i]=x
    else:
        for i in T:z[i]=b[i]
        vals=fill([b[i] for i in S],BT)
        for i,x in zip(S,vals):z[i]=x
    assert all(z[i]>=b[i] for i in range(N))
    assert sum(z[i] for i in S)==sum(z[i] for i in T)
    return sum(x*x for x in z),z

def solve(b):
    N=len(b)
    profile=[(candidate(b,mask)[0],mask,candidate(b,mask)[1]) for mask in range(1,(1<<N)-1)]
    best=min(v[0] for v in profile)
    return best,[(m,z) for E,m,z in profile if E==best]

def check():
    tests=0; rng=Random(482)
    vectors=[(F(1),)*N for N in range(3,9)]
    vectors += [(F(1),F(1),F(1),F(2)),(F(1),F(3),F(2)),(F(4),F(1),F(1),F(2),F(3)),
                (F(1),F(2),F(3),F(4)),(F(1,2),F(3,2),F(5,3),F(2,3))]
    for N in range(3,9):
        for _ in range(18): vectors.append(tuple(F(rng.randint(1,7),rng.randint(1,5)) for _ in range(N)))
    for b in vectors:
        N=len(b);d=N-1
        best,ans=solve(b)
        for mask,z in ans:
            E,z1=candidate(b,mask)
            assert E==best and z1==z
            E2,z2=candidate(b,((1<<N)-1)^mask)
            assert E2==E and z2==z
            sign=[1 if mask>>i&1 else -1 for i in range(N)]
            assert sum(s*x for s,x in zip(sign,z))==0
            assert sum(x*x for x in z)==best
            assert min(z[i]/b[i] for i in range(N))==1
            # The normal projection a_i is sqrt(N/(d*best))*sign_i*z_i.
            assert sum((sign[i]*z[i])**2 for i in range(N))==best
        if len(set(b))==1:
            q=N//2;p=N-q
            assert best==b[0]**2*F(p*N,q)
        for _ in range(40):
            v=[rng.gauss(0,1) for i in range(N)];avg=sum(v)/N;v=[x-avg for x in v]
            norm=sqrt(sum(x*x for x in v));
            # For simplex unit vertices w_i, a_i=sqrt(N/d)*v_i/||v||.
            gain=min(abs(x)/float(bb) for x,bb in zip(v,b))*sqrt(N/d)/norm
            assert gain<=sqrt(N/d/float(best))+1e-10
            tests+=1
    assert solve((F(1),F(1),F(1),F(2)))[0]==F(19,2)
    print(f'PASS: {len(vectors)} weighted profiles, {tests} sampled directions, exact water-filling and complement identities')
if __name__=='__main__':check()
