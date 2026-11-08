#!/usr/bin/env python3
"""Exact finite checks for dihedral characters of squared-cycle 3-cut homology.

Usage: python3 verify.py.  Python standard library only.
Finite tests corroborate, but do not replace, the parameter-uniform proof.
"""
from itertools import combinations
from math import comb, gcd


def graph_connected_triple(t, n):
    t = tuple(t)
    edges = [(a, b) for a, b in combinations(t, 2)
             if (a-b) % n in (1, 2, n-1, n-2)]
    seen = {t[0]}
    for _ in range(3):
        for a, b in edges:
            if a in seen:
                seen.add(b)
            if b in seen:
                seen.add(a)
    return len(seen) == 3


def parity(vals):
    return -1 if sum(vals[i] > vals[j]
                     for i in range(len(vals)) for j in range(i+1, len(vals))) % 2 else 1


def sign_subset(g, subset):
    return parity([g[i] for i in subset])


def expected(n, a, reflection):
    rank = comb(n-4, 2) - 9
    if reflection:
        if n % 2:
            return (-1)**((n-1)//2) * ((7-n)//2)
        if a % 2 == 0:
            return (-1)**((n-2)//2) * (5-n//2)
        return (-1)**(n//2) * (3-n//2)
    if a == 0:
        return rank
    return (-1)**(n-gcd(n, a)) * (1-n//2 if n % 2 == 0 and a == n//2 else 1)


def check_n(n, test_cut=False):
    T3 = [t for t in combinations(range(n), 3) if graph_connected_triple(t, n)]
    good3 = [t for t in combinations(range(n), 3) if not graph_connected_triple(t, n)]
    B4 = [t for t in combinations(range(n), 4)
          if all(graph_connected_triple(u, n) for u in combinations(t, 3))]
    blocks = {tuple(sorted((i+j) % n for j in range(4))) for i in range(n)}
    assert len(T3) == 4*n
    assert set(B4) == blocks
    assert len(B4) == n
    if n <= 14:
        assert not any(all(graph_connected_triple(u, n) for u in combinations(t, 3))
                       for t in combinations(range(n), 5))
    set2 = list(combinations(range(n), 2))
    for refl in (False, True):
        for a in range(n):
            g = [(a-i) % n if refl else (a+i) % n for i in range(n)]
            sg = parity(g)
            # The relative chain formula is evaluated from independent
            # enumeration of its fixed oriented complement sets.
            traces = [1]
            for sets in ([tuple([i]) for i in range(n)], set2, T3, B4):
                traces.append(sum(sign_subset(g, s) for s in sets
                                  if {g[v] for v in s} == set(s)))
            actual = sg*sum((-1)**q * x for q, x in enumerate(traces))
            assert actual == expected(n, a, refl), (n, a, refl, actual)
    character_sum = sum(expected(n, a, False) + expected(n, a, True)
                        for a in range(n))
    assert character_sum % (2*n) == 0
    expected_fixed = ((n-7)*(1-(-1)**((n-1)//2))//4 if n % 2
                      else (n-9-3*(-1)**(n//2))//4)
    assert character_sum//(2*n) == expected_fixed, (n, character_sum)
    assert expected_fixed >= 0
    if test_cut:
        allmask = (1 << n)-1
        badmasks = [sum(1 << x for x in t) for t in good3]
        faces = [s for s in range(1 << n)
                 if any((s & b)==0 for b in badmasks)]
        # Calculate alternating fixed oriented face counts in the actual
        # cut complex, not in its Alexander-dual or relative complex.
        for refl in (False, True):
            for a in range(n):
                g = [(a-i) % n if refl else (a+i) % n for i in range(n)]
                lef = 0
                for mask in faces:
                    vs = [i for i in range(n) if mask & (1 << i)]
                    if {g[i] for i in vs} == set(vs):
                        lef += (-1)**(len(vs)-1) * sign_subset(g, vs)
                assert (-1)**(n-4)*lef == expected(n, a, refl), (n, a, refl, lef)
        # independent mod-2 simplicial homology rank verification
        bydim = {}
        for m in faces:
            bydim.setdefault(m.bit_count()-1, []).append(m)
        assert len(bydim[n-4]) == len(good3)
        boundary_ranks = {}
        for d in range(1, n-3):
            index = {m:i for i,m in enumerate(bydim[d-1])}
            basis = {}
            for m in bydim[d]:
                col = 0
                x = m
                while x:
                    bit = x & -x
                    col ^= 1 << index[m ^ bit]
                    x -= bit
                while col:
                    pivot = col.bit_length()-1
                    if pivot in basis:
                        col ^= basis[pivot]
                    else:
                        basis[pivot] = col
                        break
            boundary_ranks[d] = len(basis)
        # reduced H0=0 for connected complex; ordinary H0 rank1
        assert len(bydim[0])-boundary_ranks.get(1, 0) == 1
        for d in range(1,n-3):
            b = len(bydim[d])-boundary_ranks.get(d, 0)-boundary_ranks.get(d+1, 0)
            assert b == (comb(n-4,2)-9 if d == n-4 else 0), (n,d,b)
        print(f'n={n} direct_complex={len(faces)} f_top={len(good3)} top_beta={comb(n-4,2)-9} actions={2*n}')
    return 2*n


def main():
    actions = 0
    for n in range(9, 23):
        actions += check_n(n, test_cut=(n <= 12))
    print(f'VERIFY_OK n_range=9..22 actions={actions} direct_cut_n=9..12 mod2_betti_n=9..12')

if __name__=='__main__':
    main()
