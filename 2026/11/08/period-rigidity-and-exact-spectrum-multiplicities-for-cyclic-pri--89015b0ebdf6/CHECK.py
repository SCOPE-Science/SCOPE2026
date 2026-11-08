#!/usr/bin/env python3
"""Exact, finite checks of spectrum-count/period theorem for cyclic CRT graphs.

No numerical complex arithmetic; cyclotomic Fourier zeros are reduced in Z[X]/Phi_N.
The exhaustive tests include ALL frequency sets, not merely frequency graphs.
"""
from itertools import product,combinations
from functools import lru_cache
from math import gcd, comb


def divisors(n):return [d for d in range(1,n+1) if n%d==0]
def mu(n):
    out=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;out=-out
            if n%p==0:return 0
        p+=1
    if n>1:out=-out
    return out

def polydiv(num,den):
    r=num[:];q=[0]*max(1,len(num)-len(den)+1)
    while len(r)>=len(den):
        c=r[-1];j=len(r)-len(den);q[j]=c
        for i,v in enumerate(den):r[i+j]-=c*v
        while r and r[-1]==0:r.pop()
    return q,r

@lru_cache(None)
def phi(n):
    x=[-1]+[0]*(n-1)+[1]
    for d in divisors(n):
        if d<n:
            x,r=polydiv(x,phi(d));assert not any(r)
    return x
@lru_cache(None)
def powers(n):
    P=phi(n);k=len(P)-1;R=[]
    for e in range(n):
        _,rem=polydiv([0]*e+[1],P)
        R.append(tuple((rem+[0]*k)[:k]))
    return R


def crt(x,m,y,q):return next(z for z in range(m*q) if z%m==x and z%q==y)
def graph(m,q,f):return tuple(crt(x,m,f[x],q) for x in range(m))
def period_size(f):
    m=len(f)
    return sum(all(f[(x+t)%m]==f[x] for x in range(m)) for t in range(m))
def spectrum_predicate(n,A,R):
    zero=set()
    for k in range(1,n):
        vec=[0]*len(R[0])
        for a in A:
            for j,v in enumerate(R[(a*k)%n]):vec[j]+=v
        if not any(vec):zero.add(k)
    return lambda B:all((b-a)%n in zero for a,b in combinations(B,2))

def test(m,q,independent=True):
    n=m*q;R=powers(n)
    H={d:0 for d in divisors(m)};representatives={}
    for f in product(range(q),repeat=m):
        d=period_size(f);H[d]+=1;representatives.setdefault(d,f)
    for d,c in H.items():
        exp=sum(mu(e//d)*q**(m//e) for e in divisors(m) if e%d==0)
        assert c==exp,(m,q,d,c,exp)
    assert sum(H.values())==q**m
    if independent:
        tests=list(product(range(q),repeat=m)) if n<=15 else list(representatives.values())
        F=list(combinations(range(n),m)) if n<=30 else None
        for f in tests:
            A=graph(m,q,f); P=spectrum_predicate(n,A,R)
            if F is not None:
                found=sum(P(B) for B in F)
            else:
                found=sum(P(graph(m,q,g)) for g in product(range(q),repeat=m))
            assert found==q**period_size(f),(m,q,f,found,q**period_size(f))
        print('CHECK',n,'m',m,'q',q,'graphs',q**m,'independent_A_tested',len(tests),
              'tested_B_per_A',len(F) if F else q**m,
              'spectrum_multiplicities',sorted((q**d,num) for d,num in H.items() if num),
              'ordered_pairs',sum(q**d*c for d,c in H.items()))
    else:
        print('CHECK_HISTOGRAM',n,'m',m,'q',q,'graphs',q**m,
              'spectrum_multiplicities', sorted((q**d,c) for d,c in H.items() if c),
              'ordered_pairs',sum(q**d*c for d,c in H.items()))

if __name__=='__main__':
    for m,q in [(3,2),(2,3),(5,2),(2,5),(7,2),(3,5),(5,3),(4,3),(6,5),(9,2)]:test(m,q)
    test(10,3,independent=False)
    print('CHECK_OK')
