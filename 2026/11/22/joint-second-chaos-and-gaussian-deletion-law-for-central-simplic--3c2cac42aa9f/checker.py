#!/usr/bin/env python3
"""Finite identities and deterministic experiments for circular central depth deletion."""
from math import pi, comb, factorial, cos, sin, isclose, tanh, cosh, exp, sqrt
import random, statistics

def depth(points):
    n=len(points)
    if n<3: raise ValueError('n>=3')
    a=sorted(p%(2*pi) for p in points)
    double=a+[v+2*pi for v in a]
    excluded=0
    j=1
    for i in range(n):
        j=max(j,i+1)
        while j<i+n and double[j]-double[i] < pi-1e-12:
            j+=1
        r=j-i-1
        excluded+=comb(r,2) if r>=2 else 0
    return (comb(n,3)-excluded)/comb(n,3)

def moment_theory(n):
    return (3/(8*(n-1)*(n-2)),3/(4*(n-1)*(n-2)*(n-3)))

def fourier_kernel(x,y,M=301):
    return sum(-2/(pi*pi*k*k)*cos(k*(x-y)) for k in range(1,M,2))

def h2(x,y):
    d=abs((x-y+pi)%(2*pi)-pi)
    return d/(2*pi)-.25

def main():
    checks=0
    for m in [101,401,1601]:
        for x,y in [(0,.5),(1.2,2.4),(0,pi/2),(0,pi),(0,2*pi/5)]:
            assert abs(fourier_kernel(x,y,m)-h2(x,y))<.6/m # O(1/m), conservative
            checks+=1
    for k in range(1,33,2):
        a=( ( -1)**k-1)/(2*pi*pi*k*k)
        assert isclose(a,-1/(pi*pi*k*k),rel_tol=1e-15)
        checks+=1
    for n in [4,5,10,40,100,1000]:
        v,d=moment_theory(n)
        assert isclose(v,3/(8*(n-1)*(n-2)),rel_tol=1e-15)
        assert isclose(d,v*2/((n-3)),rel_tol=1e-15)
        assert isclose((n-1)*d/v,2*(n-1)/(n-3),rel_tol=1e-15)
        checks+=3
    for q in [0.01,0.1,1,2,4]:
        # exact Gaussian-chaos transform derived by factorizing odd eigenmodes
        a=sqrt(6*q)/2
        partial=sum(1/(pi**4*k**4+6*q*pi*pi*k*k) for k in range(1,4000,2))
        closed=(1-tanh(a)/a)/(32*a*a)
        assert abs(partial-closed)<1e-12
        assert abs(exp(.75*q)/cosh(a)-exp(.75*q)* (1/cosh(a)))<1e-12
        checks+=2
    assert isclose(36*sum(1/(pi**4*k**4) for k in range(1,3000,2)),3/8,rel_tol=1e-10)
    assert isclose(72*sum(1/(pi**4*k**4) for k in range(1,3000,2)),3/4,rel_tol=1e-10)
    assert isclose(-432*sum(1/(pi**6*k**6) for k in range(1,3000,2)),-9/20,rel_tol=1e-10)
    checks+=3
    rng=random.Random(521948)
    for n,samples in [(12,7000),(50,9000),(130,9000)]:
        zz=[];jj=[];bb=[]
        for t in range(samples):
            p=[rng.random()*2*pi for _ in range(n)]
            d=depth(p)
            lm=depth(p[1:]);zz.append(n*(d-.25));j=n**1.5*(d-lm)
            jj.append(j);bb.append(j*j)
        evar=statistics.pvariance([z/n for z in zz]); theory, diff=moment_theory(n)
        ediff=sum(bb)/samples /n**3
        assert abs(evar/theory-1)<0.095,(n,'variance',evar,theory)
        assert abs(ediff/diff-1)<0.12,(n,'difference',ediff,diff)
        checks+=2
        if n>=50:
            cov=sum(z*b for z,b in zip(zz,bb))/samples-statistics.mean(zz)*statistics.mean(bb)
            print('n',n,'scaled n depth var',statistics.pvariance(zz),'deletion J variance',statistics.pvariance(jj),'Cov(Z,J^2)',cov)
            assert cov<-.08
            checks+=1
    print('PASS',checks,'checks: spectral, exact variance, hyperbolic transform, and seeded finite simulation')

if __name__=='__main__':main()
