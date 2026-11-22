#!/usr/bin/env python3
"""Exact arithmetic checks for adjacent little-Schroeder gaps."""
from math import comb

def v2(a):
    assert a
    return (abs(a) & -abs(a)).bit_length()-1

def little_schroeder(N):
    seq=[1, 1]
    for n in range(2,N+1):
        numerator=(6*n-3)*seq[n-1]-(n-2)*seq[n-2]
        assert numerator % (n+1) == 0
        seq.append(numerator//(n+1))
    return seq

N=1100
s=little_schroeder(N+2)
assert s[:9]==[1,1,3,11,45,197,903,4279,20793]
checks=0
for n in range(1,N+1):
    d=s[n+1]-s[n]
    expected=1 if n&1 else v2(n*(n+2))
    assert v2(d)==expected,(n,d,v2(d),expected)
    checks+=1

# The hypergeometric finite sum is independently evaluated.
for n in range(0,101):
    # Evaluate the finite hypergeometric polynomial with rational arithmetic.
    from fractions import Fraction
    f=sum((Fraction(2**j*comb(n,j)*comb(n+2,j),j+1)
           for j in range(n+1)),Fraction(0))
    assert f.denominator==1 and f.numerator*2==s[n+2]-s[n+1],n
    checks+=1

# Directly test 2-adic isometry on odd input classes at many shifts.
f=[(s[n+2]-s[n+1])//2 for n in range(N+1)]
for h in [4,8,12,16,24,32,48,64,96,128,192,256]:
    for n in range(1,N-h,2):
        assert v2(f[n+h]-f[n])==v2(h),(n,h)
        checks+=1

# Finite residue zero-loci test and limiting density-count identities.
for k in range(3,12):
    mod=2**k
    for n in range(1,N+1):
        assert ((s[n+1]-s[n])%mod==0)==(n%2==0 and n%(2**(k-1)) in (0,2**(k-1)-2)),(k,n)
        checks+=1

print('CHECK_OK',checks,'exact assertions; n<=',N)
