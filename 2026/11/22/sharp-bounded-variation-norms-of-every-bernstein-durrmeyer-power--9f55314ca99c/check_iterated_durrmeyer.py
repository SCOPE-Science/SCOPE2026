#!/usr/bin/env python3
"""Exact independent algebraic checks for Bernstein--Durrmeyer power variation."""
from fractions import Fraction as F
from math import comb

def matrix(n):
    return [[F((n+1)*comb(n,i)*comb(n,j),(2*n+1)*comb(2*n,i+j)) for j in range(n+1)] for i in range(n+1)]
def matvec(A,x):
    return [sum((a*b for a,b in zip(row,x)), F(0)) for row in A]
def eig(n,j):
    out=F(1)
    for t in range(j):out*=F(n-t,n+2+t)
    return out

def leg0_even(r):
    return F((-1)**r*comb(2*r,r),4**r)

def power_norm_spectral(n,k):
    return sum(((leg0_even(r)-leg0_even(r+1))*eig(n,2*r+1)**k for r in range((n+1)//2)), F(0))

def midpoint_coeff(n):
    return [F(sum(comb(n+1,j) for j in range(i+1)), 2**(n+1)) for i in range(n+1)]

def power_norm_bern(n,k):
    a=midpoint_coeff(n)
    M=matrix(n)
    for _ in range(k-1):a=matvec(M,a)
    return a[n]-a[0]

count=0
for n in range(1,13):
    M=matrix(n)
    assert all(sum(row)==1 for row in M)
    assert all(M[i][j]==M[j][i] for i in range(n+1) for j in range(n+1))
    # Bernstein coefficient matrix is strictly totally positive at the 2x2 level.
    for i in range(n):
        for j in range(n):
            assert M[i][j]*M[i+1][j+1]-M[i][j+1]*M[i+1][j] > 0
    for k in range(1,9):
        spec=power_norm_spectral(n,k)
        bern=power_norm_bern(n,k)
        assert spec==bern,(n,k,spec,bern)
        assert 0 < spec < 1
        if k==1:assert spec==F(1)-F(1,2**n)
        assert spec <= F(3,2)*eig(n,1)**k
        if n >= 3:
            assert spec>=F(3,2)*eig(n,1)**k-F(7,8)*eig(n,3)**k
        if k>1:
            assert spec < power_norm_spectral(n,k-1)*power_norm_spectral(n,1)
        count+=1
print('EXACT_SPECTRAL_VS_BERNSTEIN_COMPOSITION_PASS',count)
print('STOCHASTIC_SYMMETRIC_TP2_ADJACENT_MINORS_PASS')
print('SHARP_ONE_STEP_MIDPOINT_AND_TWO_MODE_BOUNDS_PASS')
print('STRICT_POWER_SUBMULTIPLICATIVITY_PASS')
for n in (1,2,3,4,5,6):
    print('n',n,'power_norms',*[str(power_norm_spectral(n,k)) for k in range(1,5)])
print('ALL_ITERATED_DURRMEYER_CHECKS_PASS')
