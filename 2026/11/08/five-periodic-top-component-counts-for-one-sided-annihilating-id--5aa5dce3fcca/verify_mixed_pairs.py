#!/usr/bin/env python3
"""Direct equation census for mixed idempotent-square-zero matrix pairs.

Run with Python 3; this script has no third-party dependencies.
The direct census enumerates full matrix spaces, not orbit representatives.
"""
from itertools import product
from math import prod

def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    return prod(q**(n-i)-1 for i in range(k)) // prod(q**(k-i)-1 for i in range(k))

def gl(k, q):
    return prod(q**k-q**i for i in range(k))

def predicted(n, q):
    return {(r, h): gaussian(n,h,q)*gaussian(n-h,h,q)*gl(h,q)*gaussian(n-h,r,q)*q**(r*(n-r))
            for h in range(n//2+1) for r in range(n-h+1)}

def matmul(a, b, p):
    n=len(a)
    return tuple(tuple(sum(a[i][t]*b[t][j] for t in range(n))%p for j in range(n)) for i in range(n))

def rank(a, p):
    w=[list(row) for row in a]
    n=len(w)
    r=0
    for c in range(n):
        pivot=next((i for i in range(r,n) if w[i][c]), None)
        if pivot is None:
            continue
        w[r],w[pivot]=w[pivot],w[r]
        inv=pow(w[r][c],-1,p)
        w[r]=[(v*inv)%p for v in w[r]]
        for i in range(n):
            if i!=r and w[i][c]:
                factor=w[i][c]
                w[i]=[(x-factor*y)%p for x,y in zip(w[i],w[r])]
        r+=1
    return r

def direct(n,p):
    mats=[tuple(tuple(a[i*n:(i+1)*n]) for i in range(n))
          for a in product(range(p),repeat=n*n)]
    z=tuple((0,)*n for _ in range(n))
    projections=[(a,rank(a,p)) for a in mats if matmul(a,a,p)==a]
    nilpotents=[(b,rank(b,p)) for b in mats if matmul(b,b,p)==z]
    got={}
    for a,r in projections:
        for b,h in nilpotents:
            if matmul(a,b,p)==z:
                got[(r,h)]=got.get((r,h),0)+1
    expected={key:value for key,value in predicted(n,p).items() if value}
    assert got==expected, (n,p,got,expected)
    print('DIRECT_OK', 'n='+str(n),'p='+str(p), 'projection_count='+str(len(projections)),
          'square_zero_count='+str(len(nilpotents)), 'pair_count='+str(sum(got.values())),
          'rank_profile='+str(sorted(got.items())))

def maximal_profiles(n):
    dims={(r,h): 2*h*(n-h)+r*(2*n-h-2*r)
          for h in range(n//2+1) for r in range(n-h+1)}
    maximum=max(dims.values())
    return maximum, sorted(key for key,v in dims.items() if v==maximum)

if __name__=='__main__':
    for case in [(1,2),(2,2),(2,3),(3,2),(3,3)]:
        direct(*case)
    for n in range(1,41):
        maximum, profiles=maximal_profiles(n)
        assert maximum == (4*n*n)//5
        k,mod=divmod(n,5)
        if mod==0: expected=[(2*k,2*k)]
        elif mod==1:
            expected=[(2*k,2*k),(2*k,2*k+1),(2*k+1,2*k)] if k else [(0,0),(1,0)]
        elif mod==2: expected=[(2*k+1,2*k+1)]
        elif mod==3: expected=[(2*k+1,2*k+1)]
        else: expected=[(2*k+1,2*k+2),(2*k+2,2*k+1),(2*k+2,2*k+2)]
        assert profiles==expected, (n,profiles,expected)
    print('MAXIMAL_STRATA_OK n=1..40')
    for n in range(1,7):
        print('EXACT_COUNTS', 'n='+str(n),
              'q2='+str(sum(predicted(n,2).values())),
              'q3='+str(sum(predicted(n,3).values())))
    print('MIXED_PAIR_DIRECT_CHECK_PASS')
