#!/usr/bin/env python3
"""Independent finite Fourier checks for rank-two bilinear-form convolution.
No external data or third-party packages beyond NumPy are required.
"""
import itertools
import math
import numpy as np


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    if k == 0:
        return 1
    numerator = math.prod(q**(n-j)-1 for j in range(k))
    denominator = math.prod(q**(k-j)-1 for j in range(k))
    assert numerator % denominator == 0
    return numerator // denominator


def rank_mod_prime(values, m, n, p):
    a = [[values[i*n+j] % p for j in range(n)] for i in range(m)]
    r = 0
    for col in range(n):
        pivot = next((i for i in range(r, m) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col], -1, p)
        a[r] = [(v*inv) % p for v in a[r]]
        for i in range(r+1, m):
            if a[i][col]:
                f = a[i][col]
                a[i] = [(u-f*v) % p for u,v in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def evals(q, m, n):
    c = q * gaussian(m, 2, q)
    b = q**n * gaussian(m-1, 1, q)
    return [c-b*gaussian(k,1,q)+q**(2*n)*gaussian(k,2,q)
            for k in range(m+1)]


def expected_min_indices(q,m,n):
    if q==2 and m==n and m>=3:
        return [2]
    if q==2 and m==n==2:
        return [0,1]
    return [0]


def check_symbolic_grid():
    count=0
    for q in (2,3,4,5,7,8,9,11):
        for m in range(2,21):
            for n in range(m,m+5):
                vals=evals(q,m,n)
                minim=min(map(abs,vals))
                attained=[k for k,v in enumerate(vals) if abs(v)==minim]
                assert attained==expected_min_indices(q,m,n), (q,m,n,attained)
                valence=gaussian(m,2,q)*(q**n-1)*(q**n-q)
                assert vals[-1]==valence
                assert all(v for v in vals)
                count+=1
    return count


def check_full_fourier(q,m,n):
    shape=(q,)*(m*n)
    signal=np.zeros(shape,dtype=float)
    for x in itertools.product(range(q),repeat=m*n):
        if rank_mod_prime(x,m,n,q)==2:
            signal[x]=1
    transformed=np.fft.fftn(signal)
    checked=0
    for x in itertools.product(range(q),repeat=m*n):
        rank=rank_mod_prime(x,m,n,q)
        k=m-rank
        error=abs(transformed[x]-evals(q,m,n)[k])
        assert error < 1e-7,(q,m,n,rank,x,error)
        checked+=1
    return checked


def main():
    grid=check_symbolic_grid()
    count=0
    for q,m,n in ((2,2,2),(2,2,3),(2,3,3),(3,2,2)):
        count+=check_full_fourier(q,m,n)
    print(f'RANK_TWO_BILINEAR_FOURIER_PASS parameter_cases={grid} complete_fourier_characters={count}')

if __name__=='__main__':
    main()
