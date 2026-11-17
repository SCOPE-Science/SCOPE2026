#!/usr/bin/env python3
"""Independent finite checks for Boolean-generator zonotope fixed-index intrinsic volumes.
Pure standard-library Python; no external files or packages.
"""
from itertools import combinations, product
from math import factorial, sqrt

def det_int(A):
    n=len(A)
    if n==0: return 1
    B=[list(map(int,row)) for row in A]
    sign=1; prev=1
    for i in range(n-1):
        if B[i][i]==0:
            for j in range(i+1,n):
                if B[j][i]:
                    B[i],B[j]=B[j],B[i]; sign=-sign; break
            else: return 0
        p=B[i][i]
        for j in range(i+1,n):
            for t in range(i+1,n):
                numerator=B[j][t]*p-B[j][i]*B[i][t]
                assert numerator % prev == 0
                B[j][t]=numerator//prev
            B[j][i]=0
        prev=p
    return sign*B[n-1][n-1]

def gram_from_vectors(cols):
    return [[sum(a*b for a,b in zip(c1,c2)) for c2 in cols] for c1 in cols]

def brute(d,k):
    cols=[tuple((i>>j)&1 for j in range(d)) for i in range(1,2**d)]
    return sum(sqrt(det_int(gram_from_vectors(C))) for C in combinations(cols,k))

def compositions(n,m):
    if m==1:
        yield (n,); return
    for i in range(n+1):
        for tail in compositions(n-i,m-1): yield (i,)+tail

def compressed(d,k):
    patterns=list(product((0,1),repeat=k))
    fac=[factorial(i) for i in range(d+1)]; total=0.0
    for counts in compositions(d,len(patterns)):
        G=[[0]*k for _ in range(k)]
        for r,p in zip(counts,patterns):
            if not r: continue
            for i in range(k):
                if p[i]:
                    for j in range(i,k):
                        if p[j]: G[i][j]+=r
        for i in range(k):
            for j in range(i): G[i][j]=G[j][i]
        determinant=det_int(G)
        if determinant<=0: continue
        mult=fac[d]//__import__('math').prod(fac[r] for r in counts)
        total+=mult*sqrt(determinant)
    return total/fac[k]

def moment_check(k):
    from math import comb
    eu=sum(comb(k,r)*4*r*(k+1-r)/(k+1) for r in range(k+1))/2**k
    eu2=sum(comb(k,r)*(4*r*(k+1-r)/(k+1))**2 for r in range(k+1))/2**k
    assert abs(eu-k)<1e-10
    assert abs(eu2-k*(k*k+k+2)/(k+1))<1e-10
    variance=eu2-eu**2
    assert abs(variance-2*k/(k+1))<1e-10
    correction=(eu2-eu**2)/8-(eu2-k)/4
    assert abs(correction+k**3/(4*(k+1)))<1e-10
    return variance,correction

if __name__=='__main__':
    comparisons=0
    for d in range(2,7):
        for k in range(1,min(3,d)+1):
            b=brute(d,k); c=compressed(d,k)
            assert abs(b-c)<1e-6*max(1,b), (d,k,b,c)
            comparisons+=1
            print('EXACT',d,k,round(b,8),round(c,8))
    d,k=4,4; b=brute(d,k); c=compressed(d,k)
    assert abs(b-c)<1e-6*b;comparisons+=1
    for k in range(1,11):moment_check(k)
    print('MOMENTS_OK k=1..10')
    for d in (8,12,20,35):
        k=2;c=compressed(d,k)
        lead=2**(d*k)*d**(k/2)*sqrt(k+1)/(2**k*factorial(k))
        scaled=d*(c/lead-1)
        print('ASYMPTOTIC',d,round(scaled,9),'target',-2/3)
        assert -.99<scaled<-.50
    print(f'BOOLEAN_INTRINSIC_PASS brute_vs_compressed={comparisons} moments=10')
