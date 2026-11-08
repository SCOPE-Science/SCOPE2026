#!/usr/bin/env python3
"""Finite checks for the twin-candidate sieve Fourier theorem (standard library)."""
import cmath
import math
from itertools import product

def primes_upto(n):
    return [x for x in range(2,n+1) if x>1 and all(x%d for d in range(2,math.isqrt(x)+1))]

def mask(x, N):
    return int(math.gcd(x*(x+2),N)==1)

def rhs_abs(a, N, ps):
    v=1.0
    for p in ps:
        b=(a*pow(N//p,-1,p))%p
        if p==2:
            v*=1
        elif b==0:
            v*=p-2
        else:
            v*=abs(1+cmath.exp(4j*math.pi*b/p))
    return v

def determinant_bareiss(A):
    a=[list(row) for row in A]
    n=len(a); prev=1; sign=1
    for k in range(n-1):
        if a[k][k]==0:
            i=next(i for i in range(k+1,n) if a[i][k])
            a[k],a[i]=a[i],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=a[i][j]*pivot-a[i][k]*a[k][j]
                assert v%prev==0
                a[i][j]=v//prev
        for i in range(k+1,n): a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

if __name__=='__main__':
    tested=0
    for P in (5,7,11):
        ps=primes_upto(P)
        N=math.prod(ps)
        survivors=[x for x in range(N) if mask(x,N)]
        assert len(survivors)==math.prod(p-(1 if p==2 else 2) for p in ps)
        frequencies=range(N) if N<=210 else [0,1,2,3,4,5,7,11,19,111,321,1051,2309]
        for a in frequencies:
            dft=sum(cmath.exp(-2j*math.pi*a*x/N) for x in survivors)
            predicted=rhs_abs(a,N,ps)
            assert abs(abs(dft)-predicted)<1e-8*max(1,predicted),(N,a,abs(dft),predicted)
            tested+=1
        # Verify the exact mean/variance formulas over the entire Fourier spectrum.
        logs=[math.log(rhs_abs(a,N,ps)) for a in range(N)]
        mean=sum(logs)/N
        variance=sum((x-mean)**2 for x in logs)/N
        target_mean=sum(math.log(p-2)/p for p in ps if p>2)
        target_variance=sum((math.log(p-2)**2 + sum(math.log(2*abs(math.cos(math.pi*j/p)))**2 for j in range(1,p)))/p-(math.log(p-2)/p)**2 for p in ps if p>2)
        assert abs(mean-target_mean)<1e-10,(P,mean,target_mean)
        assert abs(variance-target_variance)<1e-10,(P,variance,target_variance)
        # Check exact nonvanishing and summation identity at every local odd prime.
        for p in ps:
            if p==2: continue
            arr=[abs(1+cmath.exp(4j*math.pi*b/p)) for b in range(1,p)]
            assert min(arr)>1e-10
            assert abs(sum(map(math.log,arr)))<1e-10
        print('FOURIER_CHECK', 'P',P,'N',N,'survivors',len(survivors),'tested_freq',len(frequencies),'full_spectral_moments=yes')
    A=[[mask((i-j)%30,30) for j in range(30)] for i in range(30)]
    det=determinant_bareiss(A)
    assert det==-3**6,(det,-3**6)
    print('DET_CHECK', 'N',30,'determinant',det,'exact_integer=yes')
    print('VERIFY_OK','frequencies',tested,'local_nonzeros=yes','local_log_product=yes','exact_determinant=yes')
