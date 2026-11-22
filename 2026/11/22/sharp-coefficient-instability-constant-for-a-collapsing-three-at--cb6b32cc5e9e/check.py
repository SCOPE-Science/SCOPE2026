#!/usr/bin/env python3
"""Standalone finite numerical consistency checks for three-atom Fourier Kaczmarz coefficients."""
import cmath
import math
import random

rng=random.Random(261103358)
checks=0

def mul(a,b):
    out=[0j]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b):out[j+k]+=x*y
    return out

def dot(x,y):
    return sum(x[j]*y[j].conjugate() for j in range(3))/3

def make(eps,f):
    nodes=[1+0j,cmath.exp(1j*eps),cmath.exp(-1j*eps)]
    a=(1+2*math.cos(eps))/3
    p=[]
    for j in range(3):
        t=[1+0j]
        for k in range(3):
            if j!=k:t=mul(t,[1,-nodes[k].conjugate()])
        p.append(t)
    N=[sum(f[j]*p[j][k] for j in range(3))/3 for k in range(3)]
    z=1j*math.sqrt((1-a)/a)
    poles=[1+z,1-z]
    vals=lambda zz:sum(N[k]*zz**k for k in range(3))
    A=[-vals(zz)/(zz*2*a*(zz-1)) for zz in poles]
    lam=[1/zz for zz in poles]
    return nodes,a,N,A,lam

for eps in [.8,.4,.2,.1,.05,.025]:
    for _ in range(8):
        f=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for k in range(3)]
        nodes,a,N,A,lam=make(eps,f)
        # Independent Gram recursion; actual auxiliary vectors, not rational coefficients.
        gs=[]
        for n in range(22):
            e=[node**n for node in nodes]
            g=[e[j]-sum(dot(e,[nodes[t]**k for t in range(3)])*gs[k][j] for k in range(n)) for j in range(3)]
            gs.append(g)
            value=dot(f,g)
            if n==0:expected=sum(f)/3
            else:expected=sum(A[k]*lam[k]**n for k in range(2))
            if abs(value-expected)>1e-7:raise AssertionError((eps,n,value,expected))
            checks+=1
        # Rational recursion checked separately.
        cs=[]
        for n in range(22):
            rhs=(N[n] if n<3 else 0)+(2*a*cs[n-1] if n>=1 else 0)-(a*cs[n-2] if n>=2 else 0)
            cs.append(rhs)
            exact=(sum(f)/3 if n==0 else sum(A[k]*lam[k]**n for k in range(2)))
            assert abs(rhs-exact)<1e-7
            checks+=1

rt=math.sqrt(3)
L1=[2/3,-1/3+1/rt,-1/3-1/rt]
L2=[2/3,-1/3-1/rt,-1/3+1/rt]
assert abs(sum(x*y for x,y in zip(L1,L2)))<1e-12
assert abs(sum(x*x for x in L1)-4/3)<1e-12
checks+=2
# Geometric tail is bounded above by (|A1|+|A2|)r^(N+1)/(1-r).
f=[x*1.5 for x in L1]  # normalized, since ||L1||_2=2/sqrt(3)
for eps in [.12,.08,.05,.035]:
    nodes,a,N,A,lam=make(eps,f)
    r=math.sqrt(a)
    K=math.ceil(35/(eps*eps))
    v=sum(abs(A[0]*lam[0]**n+A[1]*lam[1]**n) for n in range(1,K+1))+abs(sum(f)/3)
    tail=(abs(A[0])+abs(A[1]))*r**(K+1)/(1-r)
    target=2*math.sqrt(3)
    assert abs(eps*v-target)<.09 and eps*tail<.02,(eps,eps*v,eps*tail)
    checks+=2
print('THREE_ATOM_KACZMARZ_DIAGNOSTIC_OK',checks)
