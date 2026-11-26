#!/usr/bin/env python3
"""Independent direct deletion-output enumeration for a fixed scattered 01."""
from collections import Counter
from itertools import product
from fractions import Fraction

def direct(word):
    return {word[:i] + word[i+1:j] + word[j+1:]
            for i in range(len(word)) if word[i] == '0'
            for j in range(i+1, len(word)) if word[j] == '1'}

def statistic(word):
    t = sum(word[i:i+2] == '01' for i in range(len(word)-1))
    a = sum(word[i:i+4] == '0101' for i in range(len(word)-3))
    return t*(t+1)//2-a

def expected_var(n):
    if n == 0 or n == 1: return Fraction(0)
    if n == 2: return Fraction(3,16)
    if n == 3: return Fraction(1,4)
    if n == 4: return Fraction(5,16)
    if n == 5: return Fraction(143,256)
    return Fraction(2*n**3-5*n**2+45*n-60,512)

for n in range(13):
    hist = Counter()
    for x in product('01', repeat=n):
        w=''.join(x)
        y=len(direct(w))
        assert y==statistic(w), (w,y,statistic(w))
        hist[y]+=1
    assert sum(hist.values())==2**n
    e=Fraction(sum(k*v for k,v in hist.items()),2**n)
    v=Fraction(sum(k*k*v for k,v in hist.items()),2**n)-e*e
    expected_mean=Fraction(n*n+n+4,32) if n>=3 else (Fraction(1,4) if n==2 else Fraction(0))
    assert e==expected_mean,(n,e,expected_mean)
    assert v==expected_var(n),(n,v,expected_var(n))
    print(n, 'distinct values',len(hist),'mean',str(e),'variance',str(v))
print('PASS: direct output sets, run statistic, means and variances n=0..12')
