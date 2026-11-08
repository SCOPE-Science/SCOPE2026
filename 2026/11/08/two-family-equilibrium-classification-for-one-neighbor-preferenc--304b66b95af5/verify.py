#!/usr/bin/env python3
"""Reproduce the cyclic anonymous-neighborhood game equilibrium census.

Run: python3 verify.py (Python standard library only).
"""
from collections import Counter
from math import comb, factorial
import random


def jump_stable(bits):
    """Independent definition: test every occupied-to-vacant jump."""
    n = len(bits)
    for src in range(n):
        if bits[src] == 0:
            continue
        present = bits[(src-1)%n] + bits[(src+1)%n]
        for dst in range(n):
            if bits[dst]:
                continue
            nxt = list(bits)
            nxt[src] = 0
            nxt[dst] = 1
            after = nxt[(dst-1)%n] + nxt[(dst+1)%n]
            if (after == 1) > (present == 1):
                return False
    return True


def classified(bits):
    n = len(bits)
    k = sum(bits)
    if k in (0, 1, n):
        return True
    # Family D: every occupied vertex has exactly one occupied neighbor.
    dimers = all(bits[(i-1)%n]+bits[(i+1)%n] == 1
                 for i in range(n) if bits[i])
    # Family H: all vacancies are isolated; every occupied run has >=2 sites.
    holes = all(bits[(i-1)%n] == bits[(i+1)%n] == 1
                for i in range(n) if not bits[i])
    no_ones_singleton = all(bits[(i-1)%n]+bits[(i+1)%n]>=1
                            for i in range(n) if bits[i])
    return dimers or (holes and no_ones_singleton)


def exact_count(n,k):
    if not 0<=k<=n or n<3:
        raise ValueError('n>=3 and 0<=k<=n required')
    if k in (0,n):return 1
    if k==1:return n
    z=n-k
    d=0
    if k%2==0:
        r=k//2
        if z>=r:
            d=n*comb(z-1,r-1)//r
    h=0
    if k>=2*z:
        h=n*comb(k-z-1,z-1)//z
    overlap=3 if n==3*z and k==2*z else 0
    return d+h-overlap


def main():
    total=0
    n_max=16
    for n in range(3,n_max+1):
        c=Counter()
        for mask in range(1<<n):
            bits=tuple((mask>>i)&1 for i in range(n))
            actual=jump_stable(bits)
            predicted=classified(bits)
            assert actual==predicted, ('classification',n,mask,bits,actual,predicted)
            if actual:c[sum(bits)]+=1
            total+=1
        for k in range(n+1):
            assert c[k]==exact_count(n,k), ('count',n,k,c[k],exact_count(n,k))
            if k>=2 and k<n:
                expected=((k%2==0 and 3*k<=2*n) or 3*k>=2*n)
                assert (c[k]>0)==expected, ('existence',n,k)
    print(f'PASS: {total} independently enumerated binary cycle placements, n=3..{n_max}')
    print('PASS: unrestricted-jump classification, exact count, and sharp existence regime')
    for n in (19,23,31,57):
        r=random.Random(7263+n)
        for _ in range(150):
            bits=[0]*n
            for i in r.sample(range(n),r.randint(0,n)):
                bits[i]=1
            assert jump_stable(bits)==classified(bits), ('random',n,bits)
    print('PASS: 600 independent larger-cycle random placement checks')
    print('Examples:')
    for n in range(5,12):
        print(n, ' '.join(f'{k}:{exact_count(n,k)}' for k in range(n+1)))

if __name__=='__main__':main()
