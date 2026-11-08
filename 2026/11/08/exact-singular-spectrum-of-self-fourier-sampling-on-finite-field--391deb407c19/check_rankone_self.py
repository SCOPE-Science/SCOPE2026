#!/usr/bin/env python3
"""Independent numerical comparisons for a finite-field rank-one Fourier sampling theorem.
Requires Python 3 and NumPy. This checker asserts numerical singular values
against closed-form multiplicities, without using the proof's character blocks.
"""
import itertools
import numpy as np

def field(q):
    if q in (2,3,5):
        def mul(a,b):return (a*b)%q
        def add(a,b):return (a+b)%q
        def char(a):return np.exp(2j*np.pi*a/q)
    elif q == 4:
        def add(a,b):return a^b
        def mul(a,b):
            z=0
            while b:
                if b&1:z^=a
                b>>=1;a<<=1
                if a&4:a^=7
            return z
        def char(a):return 1 if a in (0,1) else -1
    else:raise ValueError(q)
    return add,mul,char

def theoretical(q,m,n):
    P=lambda k:(q**k-1)//(q-1)
    a=P(m);b=P(n)
    d={}
    def add(x,mult):d[round(float(x),10)]=d.get(round(float(x),10),0)+mult
    add((q**(m+n-1))**0.5,(q-2)*a*b)
    add((q-1)*a*b-q**(m+n-1),1)
    add(q**(m+(n-2)/2),b-1)
    add(q**(n+(m-2)/2),a-1)
    add(q**((m+n-2)/2),(a-1)*(b-1))
    return sorted((x,y) for x,y in d.items() if y)

def check(q,m,n):
    add,mul,chi=field(q)
    vec=lambda k: list(itertools.product(range(q),repeat=k))
    mats=set()
    for u in vec(m):
        if not any(u): continue
        for v in vec(n):
            if not any(v): continue
            mats.add(tuple(mul(a,b) for a in u for b in v))
    M=sorted(mats);N=len(M)
    K=np.empty((N,N),dtype=complex)
    for i,x in enumerate(M):
        for j,y in enumerate(M):
            a=0
            for a1,b1 in zip(x,y):a=add(a,mul(a1,b1))
            K[i,j]=chi(a)
    vals=np.linalg.svd(K,compute_uv=False)
    actual=[]
    for x in sorted(vals):
        x=round(float(x),10)
        if actual and abs(actual[-1][0]-x)<1e-7:actual[-1][1]+=1
        else:actual.append([x,1])
    expected=theoretical(q,m,n)
    assert sum(j for _,j in expected)==N,(q,m,n,N,expected)
    assert len(actual)==len(expected) and all(abs(x-y)<1e-6 and j==k for (x,j),(y,k) in zip(actual,expected)),(q,m,n,actual,expected)
    print('PASS',q,m,n,'N',N,'spec',expected)
for t in [(2,2,2),(2,2,3),(2,3,3),(3,2,2),(3,2,3),(4,2,2),(5,2,2)]:check(*t)
print('RANK_ONE_SELF_FOURIER_PASS')
