#!/usr/bin/env python3
"""Direct finite-field matrix checks for an odd-characteristic open-grid neighbor-sum theorem."""
import math, random
import numpy as np

def rank_mod(A,p):
    B=(np.array(A,dtype=np.int64)%p).copy();nr,nc=B.shape;r=0
    for c in range(nc):
        hits=np.nonzero(B[r:,c])[0]
        if len(hits)==0:continue
        pivot=r+int(hits[0]);B[[r,pivot],:]=B[[pivot,r],:]
        B[r,c:]=(B[r,c:]*pow(int(B[r,c]),-1,p))%p
        ids=np.nonzero(B[:,c])[0]
        for i in ids:
            if i!=r:
                fac=int(B[i,c]);B[i,c:]=(B[i,c:]-fac*B[r,c:])%p
        r+=1
        if r==nr:break
    return r

def mat(n,p):
    N=n*n; A=np.zeros((N,N),dtype=np.int64)
    for i in range(n):
        for j in range(n):
            k=i*n+j
            for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=a<n and 0<=b<n:A[k,a*n+b]=1
    return A

def jordan_dimension(m,t):return sum(min(t,2*j-1) for j in range(1,m+1))
def order(a,p):
    a%=p
    for t in range(1,p):
        if pow(a,t,p)==1:return t
    raise RuntimeError

def fixed_dim(m,p,t):
    a=t
    while a%p==0:a//=p
    power=t//a
    val=jordan_dimension(m,power)
    return val*(int(t%order(4,p)==0)+int(t%order(-4,p)==0))

def polynomial_test(p,r):
    n=p**r-1;m=n//2
    # coefficient arrays, increasing degree
    a=[1];b=[0,1]
    for k in range(2,n+1):
        x=[0]+b; y=a+[0]*(len(x)-len(a));c=[(x[i]-y[i])%p for i in range(len(x))]
        a,b=b,c
    poly=[1]
    for _ in range(m):
        x=[0]*2+[0]*len(poly)
        for i,z in enumerate(poly):x[i]=(x[i]-4*z)%p;x[i+2]=(x[i+2]+z)%p
        poly=x
    assert b==poly,(p,r,b,poly)

results=[]
for p,r in [(3,1),(3,2),(5,1),(7,1)]:
    n=p**r-1;m=n//2;N=n*n
    polynomial_test(p,r)
    A=mat(n,p);I=np.eye(N,dtype=np.int64);power=I.copy()
    assert rank_mod(A,p)==N-2*m # number of zero Jordan blocks = 2m
    for t in range(1,n):
        power=(power@A)%p
        nullity=N-rank_mod(power,p)
        assert nullity==2*jordan_dimension(m,t),(p,r,t,nullity)
    powA=I.copy()
    for t in range(1,25):
        powA=(powA@A)%p
        count=N-rank_mod((powA-I)%p,p)
        assert count==fixed_dim(m,p,t),(p,r,t,count,fixed_dim(m,p,t))
    results.append((p,r,n,N,n-1,24))

# Exhaustively check all ternary configurations of 2 by 2, including first-entry and period.
p=3;n=2;A=mat(n,p);m=1
for z in range(3**4):
    x=np.array([(z//(3**j))%3 for j in range(4)],dtype=np.int64)
    traj=[];seen={}
    while tuple(x) not in seen:
        seen[tuple(x)]=len(traj);traj.append(tuple(x));x=(A@x)%p
    T=seen[tuple(x)];period=len(traj)-T
    assert T<=n-1 and period in (1,2)

print('PASS: path characteristic polynomials, zero-primary power ranks and 24 fixed-point rank identities',results)
print('PASS: all 81 ternary configurations on the 2x2 grid classified')
