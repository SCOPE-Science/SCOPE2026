#!/usr/bin/env python3
"""Exact-arithmetic checks for squared balancing and Lucas-balancing windows.
Run with python3 verify.py. Finite tests corroborate, but do not replace, proofs.
"""
from math import gcd

def seq(a0, a1, A, n):
    s = [a0, a1]
    for _ in range(2,n+1):
        s.append(A*s[-1]-s[-2])
    return s

def v2(a):
    assert a
    a = abs(a)
    return (a & -a).bit_length()-1

K = 180
P = [0,1]
for _ in range(2,4*K+20):
    P.append(2*P[-1]+P[-2])
B = seq(0,1,6,2*K+15)
C = seq(1,3,6,2*K+15)
assert all(B[i]*B[i]*8+1==C[i]*C[i] for i in range(2*K+10))
assert all(B[2*k+1]-1==P[2*k]*C[k+1] for k in range(1,K+1))
for k in range(1,K+1):
    sb = sum(B[i]*B[i] for i in range(1,k+1))
    sc = sum(C[i]*C[i] for i in range(1,k+1))
    assert sb == (B[2*k+1]-1-2*k)//32
    assert sc == 8*sb+k
    assert v2(sb) == v2(k*(k+1))-1
    assert v2(sc) == v2(k)
    predicted_C = gcd(k,P[2*k])
    predicted_B = predicted_C // (2 if k%2==0 else 1)
    actual_B=actual_C=0
    for n in range(3):
        actual_B=gcd(actual_B,sum(B[n+i]**2 for i in range(1,k+1)))
        actual_C=gcd(actual_C,sum(C[n+i]**2 for i in range(1,k+1)))
    assert actual_B==predicted_B,(k,actual_B,predicted_B)
    assert actual_C==predicted_C,(k,actual_C,predicted_C)
    # Explicitly test window-difference gcd via pairs of neighboring Pell terms.
    D_B=gcd(abs(B[k+1]**2-B[1]**2),abs(B[k+2]**2-B[2]**2))
    D_C=gcd(abs(C[k+1]**2-C[1]**2),abs(C[k+2]**2-C[2]**2))
    assert D_B==(3*P[2*k] if k%2==0 else P[2*k]//2),(k,D_B)
    assert D_C==(24*P[2*k] if k%2==0 else 4*P[2*k]),(k,D_C)
for t in range(3,2*K+3,2):
    assert v2(B[t]-t)==v2(t*t-1)+2
print('PASS 180 window lengths: first-three-window GCDs agree with both formulas')
print('PASS 180 exact square-sum identities and 2-adic valuations')
print('PASS 180 independent consecutive-difference GCD comparisons')
print('PASS 180 odd-index Chebyshev valuation tests')
