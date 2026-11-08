#!/usr/bin/env python3
"""Exact cyclotomic-coefficient checks for sparse indicator perturbations of prime chirps.

For a prime p, a p-th-root sum vanishes iff its p residue counts are all equal.
This verifies finite cases only; the theorem for all primes follows from the proof.
"""
from itertools import combinations
from math import comb
import random


def residues(p, a, U, u, v):
    S = set(U)
    counts = [0] * p
    for x in S:
        y = (x + u) % p
        z = (x - u) % p
        counts[(a * y*y - v*x) % p] += 1
        counts[(-a * z*z - v*z) % p] += 1
        if y in S:
            counts[(-v*x) % p] += 1
    if v == (2 * a * u) % p:
        counts[(a * u*u) % p] += p
    return counts


def iszero(cs):
    return len(set(cs)) == 1


def finite_checks():
    cases = 0
    exhaustive = [(5, 1), (7, 2), (11, 3)]
    for p, maxk in exhaustive:
        for k in range(1, maxk+1):
            for U in combinations(range(p), k):
                for a in range(1, p):
                    for u in range(p):
                        for v in range(p):
                            assert not iszero(residues(p,a,U,u,v)), (p,a,U,u,v)
                            cases += 1
    # Sample deterministic support sets at larger primes, never claimed exhaustive.
    rand = random.Random(150305800)
    for p in (13, 17, 19):
        for k in range(1, (p-1)//3+1):
            for _ in range(10):
                U = tuple(sorted(rand.sample(range(p), k)))
                a = rand.randrange(1,p)
                for u in range(p):
                    for v in range(p):
                        assert not iszero(residues(p,a,U,u,v)), (p,a,U,u,v)
                        cases += 1
    print('SPARSE_CHIRP_CYCLOTOMIC_PASS cases=',cases)
    for p,a,U,u,v in [
        (5,1,(2,3),1,3),
        (7,1,(0,3,4),1,0),
        (11,1,(4,5,6,7),1,7),
    ]:
        cs=residues(p,a,U,u,v)
        assert cs==[1]*p, (p,cs)
        assert 3*len(U) >=p
        assert v!=(2*a*u)%p
        print('BOUNDARY_VANISHING_EXAMPLE',p,'U',list(U),'u',u,'v',v)
    print('SPARSE_CHIRP_BOUNDARY_PASS examples=3')


if __name__ == '__main__':
    finite_checks()
