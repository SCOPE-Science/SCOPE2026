#!/usr/bin/env python3
"""Exact rational tests for quadrature-rank formulas in a nilpotent Lyapunov flow."""
from fractions import Fraction as F
from math import factorial
def zeros(n,m): return [[F(0) for _ in range(m)] for _ in range(n)]
def transpose(M): return list(map(list,zip(*M)))
def add(A,B): return [[a+b for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]
def scale(c,A): return [[c*a for a in row] for row in A]
def mul(A,B):
    Bt=transpose(B)
    return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in Bt] for row in A]
def rank(A):
    a=[row[:] for row in A]
    n=len(a); m=len(a[0]); k=0
    for j in range(m):
        i=next((i for i in range(k,n) if a[i][j]),None)
        if i is None: continue
        a[k],a[i]=a[i],a[k]; t=a[k][j]
        a[k]=[v/t for v in a[k]]
        for i in range(k+1,n):
            q=a[i][j]
            if q: a[i]=[v-q*w for v,w in zip(a[i],a[k])]
        k+=1
        if k==n: break
    return k
def determinant(M):
    a=[row[:] for row in M]
    n=len(a); z=F(1)
    for j in range(n):
        i=next((i for i in range(j,n) if a[i][j]),None)
        if i is None: return F(0)
        if i!=j: a[j],a[i]=a[i],a[j];z=-z
        v=a[j][j]; z*=v
        for i in range(j+1,n):
            t=a[i][j]/v
            if t:
                for k in range(j+1,n): a[i][k]-=t*a[j][k]
                a[i][j]=F(0)
    return z
def v(n,t): return [(-t)**k/F(factorial(k)) for k in range(n)]
def outer(a): return [[x*y for y in a] for x in a]
def N(n,t): return outer(v(n,t))
def quadrature(n,h,m,order):
    Z=zeros(n,n)
    for j in range(m):
        t=j*h
        if order==2:
            Z=add(Z,scale(h/2,add(N(n,t),N(n,t+h))))
        else:
            Z=add(Z,scale(h/6,add(add(N(n,t),scale(4,N(n,t+h/2))),N(n,t+h))))
    return Z
def stages(n,h,m,order):
    W=zeros(n,n)
    for j in range(m):
        t=j*h
        W1=add(W,scale(h,N(n,t)))
        W2=add(W1,scale(h,N(n,t+h)))
        if order==2: W=scale(F(1,2),add(W,W2))
        else:
            Wh=add(scale(F(3,4),W),scale(F(1,4),W2))
            Wh3=add(Wh,scale(h,N(n,t+h/2)))
            W=add(scale(F(1,3),W),scale(F(2,3),Wh3))
    return W
def det_square_nodes(n,times,weights):
    result=F(1)
    for w in weights: result*=w
    for i in range(n):
        result/=F(factorial(i)**2)
        for j in range(i+1,n):
            result*=(times[j]-times[i])**2
    return result
count=0
for n in range(2,8):
    for h in [F(1,3),F(2,3),F(5,4)]:
        for m in range(1,6):
            for order in (2,3):
                W=quadrature(n,h,m,order)
                assert stages(n,h,m,order)==W,(n,h,m,order)
                expected=min(n,m+1 if order==2 else 2*m+1)
                assert rank(W)==expected, (n,h,m,order,rank(W),expected)
                count+=1
# Dimension 3 explicit strictness contrast from zero.
h=F(1)
assert rank(quadrature(3,h,1,2))==2
assert rank(quadrature(3,h,1,3))==3
assert determinant(quadrature(3,h,1,3))==h**9/F(3456)
assert determinant(quadrature(3,h,2,2))==h**9/F(4)
# General Vandermonde weighted Gram determinant where exactly n nodes are used
for n in range(2,8):
    times=[F(j,3) for j in range(n)]
    weights=[F(j+1,7) for j in range(n)]
    Z=zeros(n,n)
    for t,w in zip(times,weights): Z=add(Z,scale(w,N(n,t)))
    assert determinant(Z)==det_square_nodes(n,times,weights)
    count+=1
# For a stable diagonal real-spectrum controllable pair, h=2 log(2) gives
# exponential sample vectors with exact rational entries 2^(-a*j).
for n in range(2,8):
    for m in range(1,6):
        for order in (2,3):
            Z=zeros(n,n)
            samples=list(range(0,2*m+1,2)) if order==2 else list(range(2*m+1))
            for j in samples:
                if order==2:
                    w=1 if j in (0,2*m) else 2
                else:
                    w=1 if j in (0,2*m) else (4 if j%2 else 2)
                vj=[F(1,2**((i+1)*j)) for i in range(n)]
                Z=add(Z,scale(F(w),outer(vj)))
            assert rank(Z)==min(n,len(samples))
            count+=1
# Continuous moment Gramian in three dimensions; no stage approximation.
n=3
exact=[[(-1)**(i+j)*F(1,i+j+1)/F(factorial(i)*factorial(j))
        for j in range(n)] for i in range(n)]
assert determinant(exact)==F(1,8640)
assert determinant(quadrature(3,F(1),1,3))/determinant(exact)==F(5,2)
count+=2
print("VERIFY_OK",count,"exact stage/composite/rank/determinant cases; rank3 witness det=1/3456")
