#!/usr/bin/env python3
"""Independent finite checks of the crown-graph fort and forcing formulas.

Only the Python standard library is needed.  All vertices are labelled:
0,...,n-1 form one class, n,...,2n-1 the other; matching partners
have the same residue modulo n.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb


def adjacency(n):
    a = []
    for i in range(2*n):
        a.append(sum(1 << j for j in range(2*n)
                     if (i < n) != (j < n) and i % n != j % n))
    return a


def is_fort(F, adj, all_mask):
    for v in range(len(adj)):
        if not ((F >> v) & 1) and (F & adj[v]).bit_count() == 1:
            return False
    return F != 0


def forces(white, adj, all_mask):
    while white:
        changed = False
        for v in range(len(adj)):
            if not ((white >> v) & 1):
                cand = adj[v] & white
                if cand and cand & (cand - 1) == 0:
                    white ^= cand
                    changed = True
                    break
        if not changed:
            return False
    return True


def candidate_forts(n):
    for C in combinations(range(n), 3):
        amask = sum(1 << x for x in C)
        yield amask
        yield amask << n
    for C in combinations(range(n), 2):
        amask = sum(1 << x for x in C)
        yield amask | (amask << n)


def minimum_fort_packing(n, forts):
    all_mask = (1 << (2*n)) - 1
    containing = [[] for _ in range(2*n)]
    for F in forts:
        for v in range(2*n):
            if F >> v & 1:
                containing[v].append(F)
    @lru_cache(None)
    def solve(U):
        if U == 0:
            return 0
        b = U & -U
        v = b.bit_length() - 1
        best = solve(U ^ b)
        for F in containing[v]:
            if F & U == F:
                best = max(best, 1 + solve(U ^ F))
        return best
    return solve(all_mask)


def predicted_forcing(n, white):
    low = (1 << n)-1
    A = white & low
    B = (white >> n) & low
    a, b = A.bit_count(), B.bit_count()
    return a <= 2 and b <= 2 and not (a == b == 2 and A == B)


def expected_poly(n):
    F = Counter({n: 1, n-1: n, n-2: comb(n, 2)})
    P = Counter()
    for a, ca in F.items():
        for b, cb in F.items():
            P[a+b] += ca*cb
    P[2*n-4] -= comb(n, 2)
    return +P


def run():
    total_checked, total_zero, total_forts = 0, 0, 0
    for n in range(3, 9):
        all_mask = (1 << (2*n)) - 1
        adj = adjacency(n)
        candidates = tuple(candidate_forts(n))
        assert len(set(candidates)) == 2*comb(n, 3)+comb(n, 2)
        for F in candidates:
            assert is_fort(F, adj, all_mask), (n, F, 'not fort')
            sub = (F-1) & F
            while sub:
                assert not is_fort(sub, adj, all_mask), (n, F, sub, 'not minimal')
                sub = (sub-1) & F
        poly = Counter()
        zcount = fcount = 0
        for white in range(all_mask+1):
            total_checked += 1
            yes = forces(white, adj, all_mask)
            prediction = predicted_forcing(n, white)
            assert yes == prediction, (n, white, yes, prediction)
            if yes:
                zcount += 1
                poly[2*n-white.bit_count()] += 1
            if is_fort(white, adj, all_mask):
                fcount += 1
                assert any(white & F == F for F in candidates), (n, white, 'fort missing candidate')
        assert +poly == expected_poly(n), (n, poly, expected_poly(n))
        assert poly[min(poly)] == comb(n, 2)*(comb(n, 2)-1), n
        assert min(poly) == 2*n-4, n
        total_zero += zcount
        total_forts += fcount
        if n <= 7:
            packing = minimum_fort_packing(n, candidates)
            assert packing == (2*n)//3, (n, packing)
        print(f'n={n} subsets={all_mask+1} forcing={zcount} forts={fcount} '
              f'minimal_forts={len(candidates)} '
              f'ft={minimum_fort_packing(n,candidates) if n<=7 else "not brute tested"}')
    print('VERIFY_OK crown_orders=3..8 tested_subsets=', total_checked,
          'zero_forcing_sets=', total_zero, 'forts=', total_forts,
          'minimal_fort_structures=PASS poly_coefficients=PASS '
          'bruteforce_packing_n=3..7 PASS', sep='')

if __name__ == '__main__':
    run()
