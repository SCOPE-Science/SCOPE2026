"""Reproduce orbit counts for balanced Johnson-graph vertices.

Only integer arithmetic and the Python standard library are used.
"""
from math import comb, factorial
from itertools import combinations, permutations
from collections import defaultdict


def pointset_signature(sets, ground):
    r = len(sets)
    code = [0] * ground
    for pos, subset in enumerate(sets):
        for elem in subset:
            code[elem] |= 1 << pos
    hist = [0] * (1 << r)
    for mask in code:
        hist[mask] += 1
    return tuple(hist)


def all_distinct_signatures(k, r):
    sets = list(map(frozenset, combinations(range(2 * k), k)))
    return {pointset_signature(tup, 2 * k)
            for tup in permutations(sets, r)}


def complement_signature(a):
    return tuple(a[(1 << (len(a).bit_length() - 1)) - 1 - i]
                 for i in range(len(a)))


def signature_census(k, r):
    raw = all_distinct_signatures(k, r)
    paired = {min(a, complement_signature(a)) for a in raw}
    fixed = {a for a in raw if a == complement_signature(a)}
    return len(raw), len(paired), len(fixed)


def H3_via_intersections(k):
    h = g = f = 0
    for p in range(k):
        for q in range(k):
            for r in range(k):
                lo = max(0, p + q - k, p + r - k, q + r - k)
                hi = min(p, q, r, p + q + r - k)
                if lo > hi:
                    continue
                assert lo + hi == p + q + r - k
                n = hi - lo + 1
                h += n
                g += (n + 1) // 2
                f += n % 2
    return h, g, f


def H3_via_pair_stabilizer(k):
    total = 0
    for t in range(k):
        for x in range(t + 1):
            for y in range(k - t + 1):
                for z in range(k - t + 1):
                    w = k - x - y - z
                    total += 0 <= w <= t
    return total - 2 * k


def closed_H3(k):
    if k % 2 == 0:
        return k * (k**3 + 8*k*k + 26*k - 32) // 24
    return (k - 1) * (k**3 + 9*k*k + 35*k + 3) // 24


def closed_G3(k):
    if k % 2 == 0:
        return k * (k**3 + 12*k*k + 50*k - 60) // 48
    return (k - 1) * (k**3 + 13*k*k + 63*k + 3) // 48


def no_repetition_orbits_formula(k, r):
    # S(n,m) signed Stirling numbers of the first kind, built recursively.
    s = [[0] * (r + 1) for _ in range(r + 1)]
    s[0][0] = 1
    for n in range(1, r + 1):
        for m in range(1, n + 1):
            s[n][m] = s[n-1][m-1] - (n-1) * s[n-1][m]
    def venntypes(m):
        # enumerate all 2^m-cell histograms of 2k ground elements
        all_s = {pointset_signature(tup, 2*k)
                 for tup in __import__('itertools').product(
                     list(map(frozenset, combinations(range(2*k),k))), repeat=m)}
        return len(all_s)
    H = sum(s[r][m] * venntypes(m) for m in range(1, r+1))
    F = sum(s[r][m] * comb(k + 2**(m-1) - 1, 2**(m-1) - 1) for m in range(1,r+1))
    return H,(H+F)//2,F


def check():
    for k in range(2, 26):
        H,G,F = H3_via_intersections(k)
        assert H == H3_via_pair_stabilizer(k)
        assert H == closed_H3(k)
        assert G == closed_G3(k)
        assert F == k * (k-1)*(k+7)//6
        assert 2*G == H+F
    for k,r in [(2,1),(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4)]:
        H,G,F = signature_census(k,r)
        hf,gf,ff = no_repetition_orbits_formula(k,r)
        assert (H,G,F)==(hf,gf,ff),(k,r,(H,G,F),(hf,gf,ff))
        if r == 3:
            assert (H,G,F)==H3_via_intersections(k)
        print(f'k={k}, r={r}: H_orbits={H}, full_aut_orbits={G}, fixed={F}')
    # Brute graph + automorphism group at J(4,2): all induced permutations are graph automorphisms,
    # and the orbit on triples is exactly the signature criterion.
    k=2
    vertices=list(map(frozenset,combinations(range(4),2)))
    edges={(a,b) for a in vertices for b in vertices if len(a&b)==1}
    automorphisms=[]
    for perm in permutations(range(len(vertices))):
        if all(((vertices[i],vertices[j]) in edges) == ((vertices[perm[i]],vertices[perm[j]]) in edges)
               for i in range(len(vertices)) for j in range(len(vertices))):
            automorphisms.append(perm)
    assert len(automorphisms)==48
    remaining=set(permutations(range(len(vertices)),3)); orbit_n=0
    while remaining:
        tup=next(iter(remaining)); remaining.difference_update(tuple(g[i] for i in tup) for g in automorphisms); orbit_n+=1
    assert orbit_n==closed_G3(2)==4
    print('BRUTE_AUT_J4_2=48; DISTINCT_TRIPLE_ORBITS=4')
    print('ALL_CHECKS_OK')


if __name__=='__main__': check()
