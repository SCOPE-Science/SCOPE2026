#!/usr/bin/env python3
"""Finite tests for cyclically primitive fixed-density Boolean traces.
Scientific tests only; exhaustive within explicit finite bounds, not an all-n proof.
Run: python checker.py
"""
from itertools import combinations
from math import comb, gcd


def mobius(n):
    p = 2
    sign = 1
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            sign = -sign
        p += 1
    return -sign if n > 1 else sign


def primitive(mask, n):
    for d in range(1, n):
        if n % d == 0 and all((mask >> i) & 1 == (mask >> (i % d)) & 1 for i in range(n)):
            return False
    return True


def bits(n, k):
    for tup in combinations(range(n), k):
        yield sum(1 << i for i in tup)


def a_count(n, k):
    return sum(mobius(d) * comb(n//d, k//d) for d in range(1,gcd(n,k)+1) if gcd(n,k)%d == 0)


def direct_is_shattered(fam, support):
    s = support.bit_count()
    traces = set()
    for a in fam:
        traces.add(a & support)
        if len(traces) == 1 << s:
            return True
    return False


def gf2_rank(vectors):
    pivots = {}
    for vector in vectors:
        while vector:
            p = vector.bit_length()-1
            if p not in pivots:
                pivots[p] = vector
                break
            vector ^= pivots[p]
    return len(pivots)


def boundary_rank(n, r, faces):
    if r == 1:
        # Reduced boundary maps singleton vertices to the single empty face.
        return int(bool(faces))
    rows = {face:i for i,face in enumerate(bits(n, r-1))}
    columns = []
    for F in faces:
        col = 0
        for i in range(n):
            if (F>>i)&1:
                col ^= (1<<rows[F^(1<<i)])
        columns.append(col)
    return gf2_rank(columns)


comparison_count = 0
rank_tests = 0
periodic_exchange_tests = 0
record=[]
for n in range(2, 13):
    for k in range(1, n):
        r = min(k, n-k)
        all_k = list(bits(n,k))
        family = [x for x in all_k if primitive(x,n)]
        assert len(family) == a_count(n,k), (n,k,'Mobius')
        # For n<=12, test all candidate support sizes, including those >r.
        observed = []
        for s in range(n+1):
            successes = 0
            for S in bits(n,s):
                actual = direct_is_shattered(family,S)
                predicted = s<r or (s==r and primitive(S,n))
                assert actual == predicted, (n,k,S,s,'trace discrepancy')
                successes += actual
                comparison_count += 1
            observed.append(successes)
        wanted = [comb(n,s) for s in range(r)] + [a_count(n,r)] + [0]*(n-r)
        assert observed == wanted, (n,k,observed,wanted)
        missing = [S for S in bits(n,r) if not primitive(S,n)]
        for i,a in enumerate(missing):
            for b in missing[i+1:]:
                assert (a^b).bit_count()!=2, (n,k,a,b,'periodic adjacent')
                periodic_exchange_tests += 1
        if n<=10:
            facets = [S for S in bits(n,r) if primitive(S,n)]
            rank = boundary_rank(n,r,facets)
            expected_rank = comb(n-1,r-1)
            assert rank == expected_rank, (n,k,'rank',rank,expected_rank)
            beta = len(facets)-rank
            assert beta == a_count(n,r)-comb(n-1,r-1)
            rank_tests += 1
        if k==n//2 or (n==12 and k==5):
            record.append((n,k,r,observed[r],a_count(n,r)-comb(n-1,r-1)))
print('PASS: all fixed-weight trace profiles for 2<=n<=12, 1<=k<n.')
print(f'PASS: {comparison_count} (n,k,S) shattered-support decisions; {periodic_exchange_tests} forbidden periodic Johnson adjacency pairs.')
print(f'PASS: {rank_tests} independent GF(2) top-boundary rank calculations, for n<=10.')
print('Selected n,k,VCdim,top_faces,top_betti:')
for x in record:
    print('  ',*x)
