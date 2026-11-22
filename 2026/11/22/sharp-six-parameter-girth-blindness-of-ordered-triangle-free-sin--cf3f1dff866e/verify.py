#!/usr/bin/env python3
"""Exact finite checks for ordered triangle-free graph extension profiles.

Uses only the Python standard library; arithmetic is integer-exact.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb


def pairs(n):
    return list(combinations(range(n), 2))


def edgelist(n, mask):
    return tuple(e for k, e in enumerate(pairs(n)) if (mask >> k) & 1)


def triangle_free(n, edges):
    E = set(edges)
    return all(not ((a, b) in E and (a, c) in E and (b, c) in E)
               for a, b, c in combinations(range(n), 3))


def profile(n, edges):
    """Direct full finite one-point extensions by gap and neighborhood."""
    C = Counter()
    for gap in range(n + 1):
        for s in range(1 << n):
            if any((s >> a) & 1 and (s >> b) & 1 for a, b in edges):
                continue
            left = sum((s >> a) & 1 for a in range(gap))
            right = sum((s >> a) & 1 for a in range(gap, n))
            C[(left, right)] += 1
    return tuple(C[(left, right)] for left in range(n + 1)
                 for right in range(n + 1 - left))


def canon(n, edges):
    """Exact unordered isomorphism test via all vertex permutations."""
    E = tuple(sorted(tuple(sorted(e)) for e in edges))
    return min(tuple(sorted(tuple(sorted((p[a], p[b]))) for a, b in E))
               for p in permutations(range(n)))


def four_cycles(n, edges):
    E = set(tuple(sorted(e)) for e in edges)
    adj = [set() for _ in range(n)]
    for a, b in E:
        adj[a].add(b)
        adj[b].add(a)
    # Each simple 4-cycle is counted twice by opposite-vertex pairs.
    return sum(comb(len(adj[a] & adj[b]), 2)
               for a, b in combinations(range(n), 2)) // 2


def poly_as_counter(n, edges):
    x = profile(n, edges)
    return {(a,b):x[sum(n+1-j for j in range(a))+b]
            for a in range(n+1) for b in range(n+1-a)
            if x[sum(n+1-j for j in range(a))+b]}


def cut_polynomials(n, edges):
    out = []
    for gap in range(n + 1):
        C = Counter()
        for s in range(1 << n):
            if any((s >> a) & 1 and (s >> b) & 1 for a, b in edges):
                continue
            a = (s & ((1 << gap) - 1)).bit_count()
            b = s.bit_count() - a
            C[(a,b)] += 1
        out.append(C)
    return out


def independent_polynomial(n, edges):
    E = [sum(1<<u for u in e) for e in edges]
    C = Counter()
    for s in range(1<<n):
        if all((s & e) != e for e in E):
            C[s.bit_count()] += 1
    return C


def cutoff():
    rows = []
    for n in range(1, 6):
        spectra = defaultdict(set)
        count = 0
        for mask in range(1 << len(pairs(n))):
            E = edgelist(n, mask)
            if not triangle_free(n, E):
                continue
            count += 1
            spectra[profile(n, E)].add(canon(n, E))
        bad = sum(len(classes)-1 for classes in spectra.values())
        assert bad == 0, (n, bad)
        rows.append((n, count, len(spectra)))
    return rows


def main():
    rows = cutoff()
    print('TRIANGLE_FREE_CUTOFF_TABLE n labelled_graphs distinct_profiles')
    for n,c,d in rows:
        print(n,c,d)
    print('CUTOFF_NONISOMORPHIC_COLLISIONS_ZERO PASS')

    n = 6
    A = ((0,4),(0,5),(1,2),(1,4),(1,5),(2,3))
    B = ((0,4),(0,5),(1,2),(1,3),(1,5),(2,4))
    assert triangle_free(n,A) and triangle_free(n,B)
    assert canon(n,A) != canon(n,B)
    pa = profile(n,A);pb=profile(n,B)
    assert pa == pb
    expected = {(0,0):7,(1,0):21,(0,1):21,
                (2,0):22,(1,1):17,(0,2):24,
                (3,0):5,(2,1):4,(1,2):4,(0,3):8}
    assert poly_as_counter(n,A) == expected
    assert independent_polynomial(n,A)==independent_polynomial(n,B)==Counter({0:1,1:6,2:9,3:3})
    cutsA= cut_polynomials(n,A)
    cutsB= cut_polynomials(n,B)
    expected_gap2=Counter({(2,1):1,(1,2):-1})
    for j in range(n+1):
        d=cutsA[j].copy();d.subtract(cutsB[j]);
        d=Counter({k:v for k,v in d.items() if v})
        assert d == (expected_gap2 if j==2 else
                     Counter({k:-v for k,v in expected_gap2.items()}) if j==4 else Counter()), (j,d)
    print('EXPLICIT_SIX_VERTEX_POLYNOMIAL_AND_CUT_CANCELLATION PASS')
    assert four_cycles(n,A)==1 and four_cycles(n,B)==0
    for t in range(7):
        n=6+t
        At=A+tuple((v,i) for i in range(6,n) for v in (3,4))
        Bt=B+tuple((v,i) for i in range(6,n) for v in (3,4))
        assert triangle_free(n,At) and triangle_free(n,Bt)
        assert profile(n,At)==profile(n,Bt)
        assert four_cycles(n,At)==comb(t,2)+1
        assert four_cycles(n,Bt)==comb(t,2)
    print('TWIN_EXTENSIONS t=0..6 PROFILE_EQUAL_FOUR_CYCLES_DIFFER PASS')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
