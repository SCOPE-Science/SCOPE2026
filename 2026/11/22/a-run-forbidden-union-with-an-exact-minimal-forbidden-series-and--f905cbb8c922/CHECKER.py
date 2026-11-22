#!/usr/bin/env python3
"""Independent finite-language checks for a binary forbidden-run union."""
from itertools import product
from fractions import Fraction

def legal(word,m):
    s=''.join(map(str,word))
    return ('0'*m not in s) or ('1'*m not in s)
def coefficient(m, n):
    # Coefficients of (1 - R(z)^2)^{-1}, with R(z) = sum(z^j,j=1..m-1)
    k=n-2*m
    if k<0:return 0
    a=[0]*(k+1); a[0]=1
    for t in range(1,k+1):
        a[t]=sum(a[t-i-j] for i in range(1,m) for j in range(1,m) if t>=i+j)
    return 2*a[k]

ct=0
for m in range(2,6):
 for n in range(1,17):
    brute=0
    for w in product((0,1), repeat=n):
      if (not legal(w,m)) and legal(w[:-1],m) and legal(w[1:],m): brute+=1
    exact=coefficient(m,n)
    assert brute==exact,(m,n,brute,exact)
    ct+=1
print('PASS: ',ct,'minimal-forbidden-word coefficient comparisons')
