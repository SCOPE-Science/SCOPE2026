#!/usr/bin/env python3
"""Finite, independent diagnostic for cyclic-polytope facet transversal counts.

Enumerates facets from Gale evenness, not from the matching description used in
its analytic proof. Checks all transversal sizes, plus the cyclic-gap formula.
Requires Python standard library only; does not prove infinite claims.
"""
from itertools import combinations
from math import comb


def binom(n, r):
    return comb(n, r) if n >= 0 and 0 <= r <= n else 0


def gale_facets(n, k):
    d = 2 * k
    facets = []
    for F in combinations(range(n), d):
        absent = [j for j in range(n) if j not in F]
        if all(sum(i < j < h for j in F) % 2 == 0
               for i, h in combinations(absent, 2)):
            facets.append(sum(1 << j for j in F))
    return facets


def formula(n, k, s):
    if s == 0:
        return 0
    total = sum(binom(s+a-1, a) * binom(s, n-s-2*a)
                for a in range(k))
    assert n*total % s == 0, (n,k,s,total)
    return (n*total)//s


def matching_number_of_cycle_induced(n, mask):
    # check by a general recursive matching search independent of the gap formula
    edges = [(j,(j+1)%n) for j in range(n)]
    best = 0
    def search(pos, used, count):
        nonlocal best
        if pos == n:
            best = max(best, count)
            return
        a,b = edges[pos]
        search(pos+1, used, count)
        if (mask & (1<<a)) and (mask & (1<<b)) and not ((used>>a)&1 or (used>>b)&1):
            search(pos+1, used | (1<<a) | (1<<b), count+1)
    search(0, 0, 0)
    return best


def run():
    tested = 0
    direct_matching = 0
    for n in range(3, 13):
        for k in range(1,(n-1)//2+1):
            facets = gale_facets(n,k)
            actual = [0]*(n+1)
            for mask in range(1<<n):
                s = mask.bit_count()
                hit = all(mask & f for f in facets)
                if hit:
                    actual[s] += 1
                if n<=8:
                    other = ((1<<n)-1) ^ mask
                    safe = matching_number_of_cycle_induced(n,other)<k
                    assert safe == hit, (n,k,mask)
                    direct_matching += 1
            expected = [formula(n,k,s) for s in range(n+1)]
            assert actual == expected, (n,k,actual,expected)
            tested += n+1
            assert sum(actual)<= 1<<n
            assert actual[n] == 1
            assert actual[0] == 0
            tau = (n-2*k+1)//2+1 # ceil((n-2*k)/2)+1, since n-2k integer
            assert min(i for i,v in enumerate(actual) if v) == tau,(n,k,tau)
            if n%2==0:
                predicted = 2*comb(n//2,k-1)
            else:
                predicted = n*comb((n-1)//2,k-1)
            assert actual[tau] == predicted,(n,k,tau,actual[tau],predicted)
    print('PASS: Gale-evenness facet enumeration and all transversal sizes:',tested)
    print('PASS: independent recursive induced-matching checks:',direct_matching)

if __name__ == '__main__':
    run()
