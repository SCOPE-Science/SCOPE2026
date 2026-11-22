#!/usr/bin/env python3
"""Numerical spot checks of cylinder products and exact branch geometry.

The infinite-scale and singularity assertions are analytical; these checks are
finite illustrations only and use Python's standard library.
"""
import math
from fractions import Fraction

def fp(x,m,sgn):
    return (x + sgn*m)/2

def logistic(v):
    return 1/(1+math.exp(-v))

def product(x,m,beta,length,positive):
    z=x
    out=1.0
    for j in range(length):
        out*=logistic(beta*z) if positive else logistic(-beta*z)
        z=fp(z,m,1 if positive else -1)
    return out

n=0
for m in [Fraction(1,3),Fraction(1,2),Fraction(1),Fraction(4,3),Fraction(2)]:
    # Every length-m word maps the entire opinion interval to its own dyadic cell.
    for depth in range(1,9):
        for word in range(1<<depth):
            lo,hi=-m,m
            for j in range(depth):
                sign=1 if (word>>j)&1 else -1
                lo=fp(lo,m,sign); hi=fp(hi,m,sign)
            assert hi-lo==2*m/Fraction(2**depth)
            n+=1
    # A sequence of all + updates gives the rightmost dyadic cell.
    for depth in range(1,20):
        lo=-m
        for _ in range(depth):lo=fp(lo,m,1)
        assert lo==m-2*m/Fraction(2**depth)
        n+=1

for m in [0.25,0.5,1.0,1.8]:
    for beta in [0.1,0.5,1.0,3.0,5.0,10.0]:
        q=logistic(beta*m)
        gamma=-math.log(q)/math.log(2)
        assert (0<gamma<1)
        for start in [-m,-m/3,0,m/3,m]:
            for positive in [False,True]:
                a=product(start,m,beta,10,positive)/(q**10)
                b=product(start,m,beta,20,positive)/(q**20)
                # Uniform tail-ratio bound from log Lipschitz beta and geometric shrink.
                assert abs(math.log(b/a)) <= 4*beta*m/(2**10)+1e-10
                n+=1
for m in [0.3,1.0,2.0]:
    for x in [-m,0,m]:
        for depth in range(1,12):
            assert abs(product(x,m,0.0,depth,True)-2.0**(-depth))<1e-14
            assert abs(product(x,m,0.0,depth,False)-2.0**(-depth))<1e-14
            n+=1
print('VERIFY_OK',n,'finite branch/product checks')
