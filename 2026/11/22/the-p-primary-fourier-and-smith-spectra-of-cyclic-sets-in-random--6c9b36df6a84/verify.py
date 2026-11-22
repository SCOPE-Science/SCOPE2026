#!/usr/bin/env python3
"""Exact arithmetic verification of cyclic-vertex Fourier congruences.

Reproducible with Python 3 (standard library only). The mathematical
proof is independent of these finite tests; no finite cutoff certifies
all primes.
"""
from itertools import product
from math import comb, factorial

CHECKS = 0

def check(ok, explanation):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(explanation)


def cyclic_mask(mapping):
    n = len(mapping)
    mask = 0
    for x in range(n):
        history = {}
        v = x
        while v not in history:
            history[v] = len(history)
            v = mapping[v]
        if x in tuple(list(history)[history[v]:]):
            mask |= (1 << x)
    return mask


def mask_profile_direct(n):
    counts = [0] * (1 << n)
    for mapping in product(range(n), repeat=n):
        counts[cyclic_mask(mapping)] += 1
    return counts


def profile_coefficient(n, size):
    if size == 0:
        return 0
    # r! permutations on the cyclic vertices; r*n^(n-r-1)
    # rooted forests. At r=n, the latter factor equals one.
    if size == n:
        return factorial(n)
    return factorial(size) * size * n ** (n - size - 1)


def hamming_spectrum(n):
    coeff = [profile_coefficient(n, r) for r in range(n + 1)]
    out = []
    for k in range(n + 1):
        lam = 0
        for r in range(n + 1):
            K = sum((-1)**a * comb(k, a) * comb(n-k, r-a)
                    for a in range(max(0, r-n+k), min(k, r)+1))
            lam += coeff[r] * K
        out.append(lam)
    return out


def walsh_direct(counts):
    vals = counts[:]
    m = len(vals)
    stride = 1
    while stride < m:
        for i in range(0, m, 2*stride):
            for j in range(stride):
                a, b = vals[i+j], vals[i+j+stride]
                vals[i+j], vals[i+j+stride] = a+b, a-b
        stride *= 2
    return vals


def isprime(x):
    return x>=2 and all(x%d for d in range(2,int(x**0.5)+1))


def vp(x, p):
    if not x:
        return float('inf')
    i=0
    while x%p==0:
        x//=p;i+=1
    return i


def modular_rank(matrix, prime):
    a=[list(map(lambda x: x%prime, row)) for row in matrix]
    m=len(a); n=len(a[0]); rank=0
    for j in range(n):
        pivot=next((i for i in range(rank,m) if a[i][j]),None)
        if pivot is None: continue
        a[rank], a[pivot]=a[pivot], a[rank]
        inv=pow(a[rank][j], -1, prime)
        for k in range(j,n):a[rank][k]=a[rank][k]*inv%prime
        for i in range(rank+1,m):
            mul=a[i][j]
            if mul:
                for k in range(j,n): a[i][k]=(a[i][k]-mul*a[rank][k])%prime
        rank+=1
    return rank


def run():
    # This tests an entirely independent direct enumeration of self-maps.
    for n in range(1,7):
        tab=mask_profile_direct(n)
        check(sum(tab)==n**n, ('total',n))
        for mask,frequency in enumerate(tab):
            check(frequency == profile_coefficient(n,mask.bit_count()),('profile',n,mask))
        transform=walsh_direct(tab)
        spectral=hamming_spectrum(n)
        for mask,frequency in enumerate(transform):
            check(frequency==spectral[mask.bit_count()],('direct Fourier',n,mask))
    print('Direct enumeration and independent Walsh transform: all n <= 6 passed')

    # All odd prime powers through dimension 169; all characters, all valuations.
    tested=0
    for p in range(3,170):
        if not isprime(p): continue
        n=p
        a=1
        while n<=169:
            tested+=1
            b=vp(factorial(n-1),p)
            spectrum=hamming_spectrum(n)
            check(spectrum[0]==n**n, ('trivial multiplier',n))
            check(vp(spectrum[0],p)==a*n,('trivial valuation',n))
            unit_factor=factorial(n-1)//(p**b)
            for k in range(1,n):
                check(vp(spectrum[k],p)==b+vp(k,p),('interior valuation',n,k))
                residue=(unit_factor*(n-1)*((-1)**k)*(n-2*k))%(p**a)
                check((spectrum[k]//(p**b))%(p**a)==residue,
                      ('interior normalized residue',n,k))
            check(vp(spectrum[n],p)==b+a,('all-ones valuation',n))
            check((spectrum[n]//(p**b))%(p**(2*a)) ==
                  unit_factor*n*(n-2)%(p**(2*a)),
                  ('all-ones normalized residue',n))
            check(all(x!=0 for x in spectrum),('rational invertibility',n))
            n*=p; a+=1
    print('Complete prime-power Fourier valuations and residues:',tested,
          'odd prime-power dimensions <= 169 passed')

    # Completely separate small integral matrix elimination modulo p.
    for p in [3,5,7]:
        freq=[profile_coefficient(p,mask.bit_count()) for mask in range(1<<p)]
        mat=[[freq[i^j] for j in range(1<<p)] for i in range(1<<p)]
        rank=modular_rank(mat,p)
        check(rank==(1<<p)-2,('modular rank',p,rank))
    print('Direct convolution-matrix modular ranks for p=3,5,7 passed')
    print('TOTAL exact assertions:',CHECKS)

if __name__ == '__main__':
    run()
