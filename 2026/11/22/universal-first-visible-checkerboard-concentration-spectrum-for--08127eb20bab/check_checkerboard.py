#!/usr/bin/env python3
"""Independent polynomial moment Gram test for the exact spherical checkerboard spectrum.
The test uses the quotient monomial basis rather than harmonic characters.
"""
import argparse,math,itertools
from functools import lru_cache
import numpy as np
from scipy.linalg import eigh
from fractions import Fraction

def exponents(d, q):
    def comp(total, parts):
        if parts == 1:
            yield (total,)
        else:
            for x in range(total+1):
                for rest in comp(total-x,parts-1):
                    yield (x,)+rest
    return [a for t in range(q+1) for a in comp(t,d) if a[-1]<2]

@lru_cache(None)
def even_moment(alpha,d):
    if any(a%2 for a in alpha):return 0.0
    n=sum(alpha)//2
    num=1
    for a in alpha:
        for j in range(1,a,2):num*=j
    den=1
    for j in range(n):den*=d+2*j
    return num/den

@lru_cache(None)
def signed_moment(alpha,d,q):
    if any(alpha[i]%2!=1 for i in range(2*q)) or any(alpha[i]%2 for i in range(2*q,d)):
        return 0.0
    p=(sum(alpha))//2
    ratio=math.gamma(d/2)/math.gamma(d/2+p)
    for i,a in enumerate(alpha):ratio*=math.gamma((a+1)/2)/math.sqrt(math.pi)
    return ratio

def run(q,d):
    idx=exponents(d,q)
    N=len(idx)
    M=np.zeros((N,N));B=np.zeros((N,N))
    for i,aa in enumerate(idx):
        for j,bb in enumerate(idx[:i+1]):
            gamma=tuple(a+b for a,b in zip(aa,bb))
            M[i,j]=M[j,i]=even_moment(gamma,d)
            B[i,j]=B[j,i]=signed_moment(gamma,d,q)
    assert np.linalg.eigvalsh(M)[0]>1e-9
    val=np.sort(eigh(B,M,eigvals_only=True))
    Npair=math.comb(2*q,q)//2
    c=(2/math.pi)**q
    expected=np.array([-c]*Npair+[0]*(N-2*Npair)+[c]*Npair)
    deviation=np.max(np.abs(val-expected))
    print(f'q={q}, d={d}, dimension={N}, pair_count={Npair}, predicted c={c:.12g}, spectral error={deviation:.3e}')
    assert deviation<2e-9

if __name__=='__main__':
    for q,d in [(1,2),(1,4),(2,4),(2,5),(3,6),(3,7)]:run(q,d)
    print('ALL_TESTS_PASS')
