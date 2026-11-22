#!/usr/bin/env python3
"""Standalone finite-field checks for square-zero products. Only prime fields are enumerated."""
import itertools
from collections import Counter
from math import prod

def gaussian(n,k,q):
    if k<0 or k>n: return 0
    # exact independent Gaussian recursion
    row=[0]*(k+1);row[0]=1
    for t in range(1,n+1):
        for j in range(min(t,k),0,-1):
            row[j]=row[j]+q**(t-j)*row[j-1]
    return row[k]

def gl(r,q):
    return prod(q**r-q**j for j in range(r))

def stratum(n,q,r,s):
    return (gaussian(n,r,q)**2*gl(r,q)*q**(n*(n-r))
            *gaussian(r,s,q)*gaussian(r-s,s,q)*gl(s,q)
            *q**((r-s)*(n-r)))

def matmul(A,B,n,q):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%q
                 for i in range(n) for j in range(n))

def rank(M,n,q):
    m=[list(M[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for j in range(n):
        p=next((i for i in range(r,n) if m[i][j]%q),None)
        if p is None: continue
        m[p],m[r]=m[r],m[p]
        inv=pow(m[r][j],-1,q)
        m[r]=[(v*inv)%q for v in m[r]]
        for i in range(n):
            if i != r:
                d=m[i][j]
                if d: m[i]=[(u-d*v)%q for u,v in zip(m[i],m[r])]
        r+=1
        if r==n:break
    return r

def exhaustive(n,q):
    mats=list(itertools.product(range(q),repeat=n*n))
    ranks=[rank(M,n,q) for M in mats]
    zero=(0,)*(n*n)
    observed=Counter()
    for ai,A in enumerate(mats):
        r=ranks[ai]
        for B in mats:
            C=matmul(A,B,n,q)
            if matmul(C,C,n,q)!=zero:continue
            s=rank(matmul(C,A,n,q),n,q)
            observed[r,s]+=1
    predicted={(r,s):stratum(n,q,r,s) for r in range(n+1) for s in range(r//2+1)}
    predicted={k:v for k,v in predicted.items() if v}
    assert observed==predicted,(n,q,observed,predicted)
    total=sum(observed.values())
    print(f'q={q} n={n}: {total}/{len(mats)**2} successful pairs; strata={dict(sorted(observed.items()))}')

def asymptotic_terms(q,n):
    numerator=sum(stratum(n,q,r,s) for r in range(n+1) for s in range(r//2+1))
    # Return normalized log in floating-point only for presentation; the exact number is certified by integer arithmetic.
    from math import log
    logprob=(len(str(numerator))-1)*log(10)+log(numerator/10**(len(str(numerator))-1))-2*n*n*log(q)
    scaled=logprob/log(q)+3*n*n/7
    print(f'q={q} n={n}: log_q P + 3n^2/7 = {scaled:.8f}')

if __name__=='__main__':
    for n,q in [(1,2),(2,2),(2,3),(3,2)]:exhaustive(n,q)
    for n in [5,10,20,35]:asymptotic_terms(2,n)
    print('VERIFY_OK')
