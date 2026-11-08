#!/usr/bin/env python3
"""Finite checks for a capped rank-metric Fourier theorem; standard Python and NumPy."""
from math import log
import numpy as np


def rank_f2(v, rows, cols):
    a = [(v >> (r*cols)) & ((1<<cols)-1) for r in range(rows)]
    piv = 0
    for bit in range(cols):
        hit = next((i for i in range(piv, rows) if (a[i] >> bit)&1), None)
        if hit is None:
            continue
        a[piv], a[hit] = a[hit], a[piv]
        for i in range(rows):
            if i != piv and ((a[i] >> bit)&1):
                a[i] ^= a[piv]
        piv += 1
        if piv == rows:
            break
    return piv


def spectral_data(q,m,n,s):
    M=q**m;N=q**n; U=(M-1)//(q-1)
    degree1=(M-1)*(N-1)//(q-1)
    k1=(q**(m+n-s)-N-M+1)//(q-1)
    numerator=k1*k1-(M+N-q-2)*k1-degree1
    assert numerator%(q*(q+1))==0
    return k1,numerator//(q*(q+1))


def fwht(x):
    a=x.copy().astype(np.int64)
    k=1
    while k<len(a):
        r=a.reshape(-1,2,k)
        x=r[:,0,:].copy(); y=r[:,1,:].copy()
        r[:,0,:]=x+y
        r[:,1,:]=x-y
        k*=2
    return a


def verify_full_binary(m,n):
    N=2**(m*n)
    ranks=np.fromiter((rank_f2(i,m,n) for i in range(N)),np.int8,count=N)
    # Recover rank-one and rank-two Fourier multipliers independently by transforms.
    one=fwht((ranks==1).astype(np.int64))
    two=fwht((ranks==2).astype(np.int64))
    for s in range(m+1):
        mask=(ranks==s)
        expected=spectral_data(2,m,n,s)
        assert np.all(one[mask]==expected[0]),(m,n,s,'rank-one')
        assert np.all(two[mask]==expected[1]),(m,n,s,'rank-two')
    print('FULL_BINARY_FOURIER_PASS', 'rows',m,'cols',n,'characters',N)


def root_and_max(q,m,n):
    M=q**m; N=q**n; U=(M-1)//(q-1)
    A=N-U; B=-spectral_data(q,m,n,m-1)[1]
    assert A>0 and B>2*A+3
    def f(b,s):
        x,y=spectral_data(q,m,n,s)
        return (1-3**b)*x + (2**b-3**b)*y-3**b
    lo=0.0;hi=1.0
    for _ in range(70):
        md=(lo+hi)/2
        if f(md,m-1)>0:hi=md
        else:lo=md
    b=(lo+hi)/2
    for p in [0.00001,b/2,b, min(1,2*b),1,4]:
        vals=[f(p,s) for s in range(1,m+1)]
        assert max(range(m),key=lambda i:vals[i])==m-2,(q,m,n,p,vals)
    assert abs(f(b,m-1))<1e-8 * max(1,A,B)
    print('ROOT_AND_CRITICAL_SHELL_PASS',q,m,n,format(b,'.12g'))


def verify_two_walks_binary(m,n):
    # Independent check of the rank-one adjacency-square intersection numbers.
    one=[x for x in range(2**(m*n)) if rank_f2(x,m,n)==1]
    freq={}
    for a in one:
        for b in one:
            k=a^b
            freq[k]=freq.get(k,0)+1
    c0=len(one);c1=2**m+2**n-4; c2=6
    for t in range(2**(m*n)):
        r=rank_f2(t,m,n)
        expected=(c0 if r==0 else c1 if r==1 else c2 if r==2 else 0)
        assert freq.get(t,0)==expected,(t,r,expected,freq.get(t,0))
    print('TWO_STEP_INTERSECTION_PASS',m,n,c0,c1,c2)

if __name__=='__main__':
    verify_two_walks_binary(4,4)
    verify_full_binary(4,4)
    for q in [2,3,4,5]:
        for m in [4,5,6]:
            for n in [m,m+1,m+3]:root_and_max(q,m,n)
    print('CAPPED_RANK_THREE_VERIFY_PASS')
