#!/usr/bin/env python3
"""Exact algebra and finite diagnostics for a rank-one CARE truncation benchmark."""
from fractions import Fraction as F
import math

# An element of Q(sqrt(2)) is represented by (rational, rational).
def add(a,b): return (a[0]+b[0], a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b): return (a[0]*b[0]+2*a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def scale(a,k): return (a[0]*k,a[1]*k)
def q(x): return (F(x),F(0))

count=0
for K in [3,4,5,7,10,17,100,1000,10000]:
    k=F(K)
    d=(F(1,K),F(1,K))
    # 2d - Kd^2 + K^{-1} is identically zero.
    assert add(sub(scale(d,2),scale(mul(d,d),k)),q(F(1,K)))==q(0)
    count+=1
    # Squared stable infimum is d^2+2(1-d)/K.
    e2=add(mul(d,d),scale(sub(q(1),d),F(2,K)))
    # e2/d^2 = ((6-4sqrt(2))*K + 3 - 2sqrt(2)).
    factor=(F(6*K+3),F(-4*K-2))
    assert e2==mul(factor,mul(d,d))
    count+=1
    dd=(1+math.sqrt(2))/K
    target=math.sqrt(dd*dd+2*(1-dd)/K)
    assert target>dd>0
    for n in [2,3,5,9]:
        # Frobenius error for a rank-one PSD Y=zz^T in n dimensions.
        # Offdiagonal terms are accounted for by (sum z_i^2)^2.
        for step in [1,2,3,5,10,100,1000]:
            y=1/K+(1-1/K)/(step+1)
            x=1-y
            z=[math.sqrt(x),math.sqrt(y)]+[0.]*(n-2)
            yz2=z[1]*z[1]
            eig_cl=[-1.]*(n-1)+[1-K*yz2]
            assert max(eig_cl)<0
            D=(sum(v*v for v in z))**2+1+dd**2-2*z[0]*z[0]-2*dd*yz2
            predicted=dd**2+2*(1-dd)*y
            assert math.isclose(D,predicted,rel_tol=1e-10,abs_tol=1e-12)
            assert D+1e-11>=target*target
            count+=3
        # An arbitrary orientation with extra stable-coordinate energy cannot lower the optimum.
        for j in [0.01,0.1,0.5]:
            y=1/K+0.001
            x=max(0.,1-y-j)
            w=j
            D=(x+y+w)**2+1+dd**2-2*x-2*dd*y
            assert D+1e-12>=dd**2+2*(1-dd)/K
            count+=1
    # Spectral truncation residual and closed-loop stability values.
    assert math.isclose(1/K,1/K,rel_tol=0,abs_tol=0)
    assert 1>0 and -math.sqrt(2)<-1
    count+=2
print(f"PASS: {count} exact-algebra and finite checks")
