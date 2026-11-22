#!/usr/bin/env python3
"""Exact arithmetic checks for the majority-quorum reversal theorem.

All checks use the Bernoulli generating polynomials directly; no floating-point
comparison is used. Finite checks supplement, but do not prove, the theorem.
"""
from fractions import Fraction as Q
from math import comb

def mass(probs):
    a = [Q(1)]
    for p in probs:
        b = [Q(0)] * (len(a) + 1)
        for j, value in enumerate(a):
            b[j] += value * (1 - p)
            b[j + 1] += value * p
        a = b
    return a

def success(r, k, h, l):
    n = 2*r+1
    a = mass([h]*k+[l]*(n-k))
    b = mass([l]*k+[h]*(n-k))
    return (sum(a[r+1:])+sum(b[r+1:]))/2

def count_check():
    tests=0
    for r in range(1,11):
        n=2*r+1
        for i in range(1,9):
            for j in range(i+1,10):
                l,h=Q(i,10),Q(j,10)
                vals=[success(r,k,h,l) for k in range(n+1)]
                for k in range(n+1):
                    assert vals[k]==vals[n-k]
                    tests+=1
                p=(h*(1-h))/(l*(1-l))
                for k in range(r):
                    original = mass([h]*k+[l]*(2*r-k))[r]
                    mirrored = mass([h]*(2*r-k)+[l]*k)[r]
                    assert original==mirrored*p**(k-r)
                    tests+=1
                    assert vals[k+1]-vals[k]==(h-l)*mirrored*(p**(k-r)-1)/2
                    tests+=1
                    assert ((vals[k+1]-vals[k])>0)==(h+l>1) if h+l!=1 else vals[k+1]==vals[k]
                    tests+=1
                if h+l>1:
                    assert vals[r]==max(vals)
                    assert all(vals[k]<vals[r] for k in range(r))
                    tests+=2
                elif h+l<1:
                    assert vals[0]==max(vals)
                    assert all(vals[k]<vals[0] for k in range(1,r+1))
                    tests+=2
                else:
                    assert len(set(vals))==1 and vals[0]==Q(1,2)
                    tests+=1
    assert [success(2,k,Q(3,4),Q(1,2)) for k in range(3)] == [Q(715,1024),Q(23,32),Q(187,256)]
    tests+=1
    assert [success(2,k,Q(3,4),Q(1,8)) for k in range(3)] == [Q(14951,32768),Q(6763,16384),Q(2969,8192)]
    tests+=1
    assert [success(2,k,Q(3,4),Q(1,4)) for k in range(3)] == [Q(1,2)]*3
    tests+=1
    return tests

if __name__=='__main__':
    print(f'{count_check()} exact assertions passed')
