#!/usr/bin/env python3
"""Supplementary finite tests for sharp spectral-gap Golden--Thompson coefficients.

Only Python's standard library is needed. The analytic proof, not these finite
numerical and rational tests, establishes the all-parameter theorem.
"""
from fractions import Fraction
from math import cosh, sinh, sqrt, factorial, isclose

I=((1.0,0.0),(0.0,1.0))
Z=((1.0,0.0),(0.0,-1.0))
X=((0.0,1.0),(1.0,0.0))

def sc(a,m):return tuple(tuple(a*v for v in row) for row in m)
def add(a,b):return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))
def mul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def exp0(a,r):return add(sc(cosh(r),I),sc(sinh(r)/r,a))
def hs2(a):return sum(a[i][j]**2 for i in range(2) for j in range(2))
def f(x):return cosh(sqrt(x))
def fp(x):return sinh(sqrt(x))/(2*sqrt(x)) if x else .5

def coeff(r,s):
    low=(r-s)**2; high=(r+s)**2; span=high-low
    slope=(f(high)-f(low))/span
    return (slope-fp(low))/span,(fp(high)-slope)/span

def run():
    checks=0
    for k in range(2,25):
        ck=Fraction(1,factorial(2*k))
        assert ck > 0 and ck*factorial(2*k)==1
        checks+=2
    assert Fraction(1,factorial(4))==Fraction(1,24)
    checks+=1
    for r,s in ((.2,.2),(.4,1.1),(.75,.75),(1.0,2.0),(2.5,1.3),(3.0,3.0),(4.0,1.5),(4.5,4.5)):
        lo,hi=coeff(r,s)
        assert lo >= 1/24-1e-9 and hi>lo
        checks+=1
        ratios=[]
        for j in range(1,81):
            u=2*j/81-1
            a=sc(r,Z); b=sc(s,add(sc(u,Z),sc(sqrt(1-u*u),X)))
            ab=mul(exp0(a,r),exp0(b,s))
            x=r*r+s*s+2*r*s*u
            delta=ab[0][0]+ab[1][1]-2*f(x)
            comm=add(mul(a,b),sc(-1,mul(b,a)))
            q=delta/hs2(comm)
            x0=(r-s)**2; x1=(r+s)**2
            line=f(x0)+(f(x1)-f(x0))*(x-x0)/(x1-x0)
            q2=(line-f(x))/((x-x0)*(x1-x))
            assert isclose(q,q2,rel_tol=5e-8,abs_tol=1e-8),(r,s,u,q,q2)
            assert lo-1e-8 < q < hi+1e-8
            ratios.append(q)
            checks+=2
        assert all(x<y+1e-10 for x,y in zip(ratios,ratios[1:])),(r,s,ratios)
        checks+=1
    # Matched-gap specialization and lack of a uniform finite upper constant.
    for r in (.3,1.,2.,5.):
        lo,hi=coeff(r,r)
        lo2=(sinh(r)**2-r*r)/(8*r**4)
        hi2=(r*sinh(2*r)-2*sinh(r)**2)/(16*r**4)
        assert isclose(lo,lo2,rel_tol=1e-9,abs_tol=1e-9)
        assert isclose(hi,hi2,rel_tol=1e-9,abs_tol=1e-9)
        checks+=2
    assert coeff(8.,8.)[0] > coeff(4.,4.)[1]
    checks+=1
    print(f'PASS {checks} finite assertions')

if __name__=='__main__':run()
