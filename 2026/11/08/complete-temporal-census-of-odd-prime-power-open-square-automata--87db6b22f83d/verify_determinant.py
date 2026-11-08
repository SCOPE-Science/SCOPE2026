#!/usr/bin/env python3
"""Check exact binomial-Toeplitz determinant identity and prime-power unit property on finite examples."""
from math import comb,factorial
from fractions import Fraction

def bareiss(a):
    n=len(a);v=[row[:] for row in a]
    sign=1;d=1
    for k in range(n-1):
        if v[k][k]==0:
            j=next((j for j in range(k+1,n) if v[j][k]!=0),None)
            if j is None:return 0
            v[k],v[j]=v[j],v[k];sign=-sign
        z=v[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                t=v[i][j]*z-v[i][k]*v[k][j]
                assert t%d==0
                v[i][j]=t//d
        for i in range(k+1,n):v[i][k]=0
        d=z
    return sign*v[n-1][n-1]

checks=0
for m in range(1,19):
    for degree in range(m):
        k=m-1-degree
        matrix=[[comb(2*k,k+j-i) if 0<=k+j-i<=2*k else 0 for i in range(degree+1)] for j in range(degree+1)]
        prod=Fraction(1)
        for i in range(degree+1):prod*=Fraction(factorial(2*k+i)*factorial(i),factorial(k+i)**2)
        assert prod.denominator==1 and bareiss(matrix)==prod.numerator
        checks+=1

units=0
for p,r in [(3,1),(3,2),(3,3),(5,1),(5,2),(7,1),(7,2),(11,1)]:
    m=(p**r-1)//2
    for degree in range(m):
        k=m-1-degree
        val=0
        h=p
        while h<=2*m-2:
            for i in range(degree+1):
                val+=(2*k+i)//h+i//h-2*((k+i)//h)
            h*=p
        assert val==0,(p,r,m,degree,val)
        units+=1
print('PASS exact binomial Toeplitz determinant identities',checks)
print('PASS zero p-adic valuations of all middle determinants',units)
