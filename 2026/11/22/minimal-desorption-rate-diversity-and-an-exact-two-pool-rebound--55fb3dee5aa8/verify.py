#!/usr/bin/env python3
"""Exact arithmetic checks for a source-free reversible sorption benchmark.

No third-party Python packages are required. Finite checks supplement
but do not replace the analytic eigenvalue and zero-count arguments.
"""
from fractions import Fraction as F
from math import factorial

ZERO=F(0)
ONE=F(1)
M=((F(-3,10),F(1,10),ONE),
   (F(1,10),F(-1,10),ZERO),
   (F(1,10),ZERO,-ONE))
x0=(F(2),F(5),ZERO)

def mv(A,x):
    return tuple(sum((a*b for a,b in zip(row,x)),ZERO) for row in A)

def polydot(t,N):
    # sum_{k=0}^N (t M)^k/k! applied to x0, then e_1^T M.
    term=x0
    acc=x0
    for k in range(1,N+1):
        term=tuple(F(t,k)*v for v in mv(M,term))
        acc=tuple(a+b for a,b in zip(acc,term))
    return mv(M,acc)[0]

def geotail_exp(x,start):
    # For exp(x), the k-th term ratio <= x/(start+1) for k>=start.
    assert x>=0 and F(x,start+1)<1
    return x**start/F(factorial(start))/(1-F(x,start+1))

assert mv(M,x0)[0]==F(-1,10)
assert M[0][0]==-(F(1,10)+F(1,10)+F(1,10))
assert max(sum(abs(v) for v in row) for row in M)==F(7,5)
assert max(map(abs,x0))==5
# Finite polynomial plus rigorous positive tail shows exp(7/5)<5.
x=F(7,5)
upper_exp=sum((x**k/F(factorial(k)) for k in range(6)),ZERO)+geotail_exp(x,6)
assert upper_exp<5
P10=polydot(1,10)
assert P10==F(138133084986931,22680000000000000)
err1=35*x**11/F(factorial(11))
assert P10>err1
# Additional independent sign at 5: exp(7)<1200, checked exactly.
y=F(7)
upper_exp7=sum((y**k/F(factorial(k)) for k in range(20)),ZERO)+geotail_exp(y,20)
assert upper_exp7<1200
P75=polydot(5,75)
err5=F(7)*1200*y**76/F(factorial(76))
assert P75 < -err5
print('Exact checks passed: Cprime(0)<0, Cprime(1)>0, Cprime(5)<0.')
print('Taylor-10 derivative at 1:',P10)
print('Certified abs error bound at 1:',err1)
print('Taylor-75 derivative at 5:',float(P75))
print('Certified abs error bound at 5:',float(err5))
print('Analytical spectral theorem supplies the global two-zero maximum.')
