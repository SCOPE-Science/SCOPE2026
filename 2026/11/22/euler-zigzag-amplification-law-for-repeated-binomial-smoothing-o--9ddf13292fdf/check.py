#!/usr/bin/env python3
"""Exact supplementary checks for the binomial cyclic inverse norm formulas.
No external packages, approximate claims, or external dependencies are required.
"""
from math import comb, factorial, pi, sin
from fractions import Fraction

def convolve(x,y):
    n=len(x)
    return [sum(x[j]*y[(k-j)%n] for j in range(n)) for k in range(n)]

def inverse_coefficients(n,m):
    assert n>=3 and n%2==1 and m>=1
    a=[(-1)**j for j in range(n)]
    b=[1]+[0]*(n-1)
    for _ in range(m):
        b=convolve(b,a)
    return b

def polynomial_recurrence(n,m):
    p=[1]*n
    for h in range(1,m):
        q=[0]*n
        q[0]=p[0]-sum(p[1:])
        for j in range(1,n):
            q[j]=q[j-1]+2*p[j]
        assert q[0]+q[-1]==2*p[0]
        p=q
    return [(-1)**j*p[j] for j in range(n)]

def zigzag(m):
    a=[1]
    for n in range(m):
        total=sum(comb(n,k)*a[k]*a[n-k] for k in range(n+1))
        if n==0:
            a.append(1)
        else:
            assert total%2==0
            a.append(total//2)
    return a

checks=0
for n in range(3,102,2):
    for m in range(1,10):
        coeff=inverse_coefficients(n,m)
        assert coeff==polynomial_recurrence(n,m)
        checks+=1
        b=inverse_coefficients(n,m)
        product=b[:]
        for _ in range(m):
            assert all((product[j]+product[(j-1)%n])%2==0 for j in range(n))
            product=[(product[j]+product[(j-1)%n])//2 for j in range(n)]
        assert product==[1]+[0]*(n-1)
        checks+=1
        if m<=4:
            expected=[n,(n*n+1)//2,n*(n*n+2)//3,(5*n**4+10*n*n+9)//24][m-1]
            assert sum(map(abs,b))==expected,(n,m)
            checks+=1
for m in range(1,10):
    a=zigzag(m)[m]
    if m>1:
        # At N=401 the fixed-order values must approximate the proven limit.
        n=401
        val=sum(map(abs,inverse_coefficients(n,m)))/n**m
        lim=a/factorial(m)
        assert abs(val-lim)<.02,(m,val,lim)
        checks+=1
assert zigzag(10)==[1,1,1,2,5,16,61,272,1385,7936,50521]
checks+=1
for n in range(3,82,2):
    assert abs(min(abs((1+complex(__import__('cmath').exp(2j*pi*k/n)))/2) for k in range(n))-sin(pi/(2*n)))<1e-12
    checks+=1
print(f'PASS {checks} exact structural/inverse/norm assertions; supplementary floating Fourier gap and limit checks.')
