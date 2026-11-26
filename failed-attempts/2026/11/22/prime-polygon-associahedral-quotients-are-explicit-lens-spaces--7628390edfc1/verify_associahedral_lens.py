#!/usr/bin/env python3
"""Independent finite sanity checks for cyclic polygon diagonal-complex lens identification.
Uses the standard-library only. General proof is mathematical, not exhaustive computation.
"""
from functools import lru_cache
from math import comb, gcd


def canonical_edge(a,b):
    return tuple(sorted((a,b)))


def triangulations(n):
    def diagonal(a,b):
        a,b=canonical_edge(a,b)
        return b-a!=1 and (a,b)!=(0,n-1)

    @lru_cache(None)
    def intervals(a,b):
        if b-a<=1:
            return (frozenset(),)
        possibilities=[]
        for k in range(a+1,b):
            for left in intervals(a,k):
                for right in intervals(k,b):
                    s=set(left)|set(right)
                    if diagonal(a,k):s.add(canonical_edge(a,k))
                    if diagonal(k,b):s.add(canonical_edge(k,b))
                    possibilities.append(frozenset(s))
        return tuple(possibilities)
    return set(intervals(0,n-1))


def rotate_face(face,n,k):
    return frozenset(canonical_edge((a+k)%n,(b+k)%n) for a,b in face)


def catalan(k):
    return comb(2*k,k)//(k+1)


def cyclic_weight_representatives(n):
    # Real Fourier character decomposition of W={sum x=sum x cos=sum x sin=0}.
    return list(range(2,(n//2)+1))


def fixed_real_dimension(n,rotation_exponent):
    # Normal-mode coefficient j contributes 2 real dimensions except j=n/2.
    total=0
    for j in cyclic_weight_representatives(n):
        if (j*rotation_exponent)%n==0:
            total+=1 if 2*j==n else 2
    return total


def verify():
    for n in (5,7,11):
        faces=triangulations(n)
        assert len(faces)==catalan(n-2),(n,len(faces))
        assert all(len(f)==n-3 for f in faces)
        for f in faces:
            for k in range(1,n):
                assert rotate_face(f,n,k)!=f,(n,k,f)
        assert len(cyclic_weight_representatives(n))==(n-3)//2
        assert all(fixed_real_dimension(n,k)==0 for k in range(1,n))
        # S^(n-4) has all nonzero weights j=2,...,(n-1)/2.
        assert all(gcd(j,n)==1 for j in cyclic_weight_representatives(n))
        print(f'prime {n}: {len(faces)} triangulations; free orbit size {n}; Fourier weights {cyclic_weight_representatives(n)}; all nonidentity fixed dimensions 0')
    for n in (4,6,8,9,10,12,15):
        fixed=[(k,fixed_real_dimension(n,k)) for k in range(1,n) if fixed_real_dimension(n,k)>0]
        assert fixed,(n,'no proper fixed mode')
        assert sum(1 if 2*j==n else 2 for j in cyclic_weight_representatives(n))==n-3
        print(f'composite {n}: fixed modes for rotations {fixed}; sharp free-action criterion verified')
    print('ASSOCIAHEDRAL_LENS_FINITE_CHECKS_OK')

if __name__=='__main__':verify()
