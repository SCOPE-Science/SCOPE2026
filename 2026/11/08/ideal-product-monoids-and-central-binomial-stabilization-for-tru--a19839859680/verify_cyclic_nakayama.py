#!/usr/bin/env python3
"""Finite-field direct verification of two-sided-ideal profile and product formulas.
No external dependencies.  Independent GF(2) subspace enumeration for small cases.
"""
from itertools import combinations, product
from collections import Counter
from math import comb


def profiles(n, ell):
    return [t for t in product(range(ell + 1), repeat=n)
            if all(t[(i - 1) % n] <= t[i] + 1 for i in range(n))]


def star(t, u, ell):
    n=len(t)
    return tuple(min(ell, t[i] + u[(i + t[i]) % n]) for i in range(n))


def path_set(t, ell):
    return frozenset(i * ell + d for i, x in enumerate(t) for d in range(x, ell))


def path_product(a, b, n, ell):
    i, d = divmod(a, ell)
    j, e = divmod(b, ell)
    if (i + d) % n == j and d + e < ell:
        return i * ell + d + e
    return None


def span_contains(rows, v):
    for row in rows:
        if v and (v & -v) == (row & -row):
            v ^= row
    return v == 0


def row_reduction(vectors):
    rows = {}
    for v in vectors:
        while v:
            p = (v & -v).bit_length() - 1
            if p not in rows:
                rows[p] = v
                break
            v ^= rows[p]
    return tuple(rows[p] for p in sorted(rows))


def all_rref(d):
    for rank in range(d + 1):
        for piv in combinations(range(d), rank):
            free = [[j for j in range(p + 1, d) if j not in piv] for p in piv]
            count = sum(map(len, free))
            for z in range(1 << count):
                rows=[]
                idx=0
                for p, fcols in zip(piv, free):
                    v = 1 << p
                    for j in fcols:
                        if z & (1 << idx): v |= 1 << j
                        idx += 1
                    rows.append(v)
                yield tuple(rows)


def direct_case(n, ell):
    dim = n * ell
    basis_products=[[path_product(a,b,n,ell) for b in range(dim)] for a in range(dim)]
    left_generators = [i*ell for i in range(n)] + [i*ell+1 for i in range(n) if ell>1]
    def prod(a,b):
        v=0
        for i in range(dim):
            if a >> i & 1:
                for j in range(dim):
                    if b >> j & 1:
                        k=basis_products[i][j]
                        if k is not None: v ^= (1 << k)
        return v
    subspaces=0; actual=set()
    for rows in all_rref(dim):
        subspaces += 1
        if all(span_contains(rows, prod(1<<g,row)) and span_contains(rows,prod(row,1<<g))
               for row in rows for g in left_generators):
            actual.add(rows)
    candidates=profiles(n,ell)
    expected={row_reduction(1 << b for b in path_set(t,ell)) for t in candidates}
    assert actual == expected, ('ideal-census mismatch',n,ell,len(actual),len(expected))
    # Matrix multiplication of representatives, no use of formula during calculation.
    for t in candidates:
        at=row_reduction(1 << b for b in path_set(t,ell))
        for u in candidates:
            bu=row_reduction(1 << b for b in path_set(u,ell))
            actual_product=row_reduction(prod(a,b) for a in at for b in bu)
            expected_product=row_reduction(1 << b for b in path_set(star(t,u,ell),ell))
            assert actual_product == expected_product,(n,ell,t,u)
    print('DIRECT_GF2', 'vertices=',n,'loewy=',ell,'ambient_dim=',dim,
          'subspaces=',subspaces,'ideals=',len(actual),'products=',len(candidates)**2,'PASS')


def global_combinatorics():
    for n in range(1,8):
        last=None
        for ell in range(1, max(n+2,4)):
            ps=profiles(n,ell)
            assert len(ps)==sum(1 for t in ps)
            if ell>=n-1 and last is not None:
                assert len(ps)-last==comb(2*n-1,n-1),(n,ell,len(ps)-last)
            last=len(ps)
            if n<=4 and ell<=4:
                counts=Counter(n*ell-sum(t) for t in ps)
                assert all(counts[d]==counts[n*ell-d] for d in range(n*ell+1))
                print('POLYNOMIAL',n,ell,','.join(str(counts[d]) for d in range(n*ell+1)))
    print('CENTRAL_BINOMIAL_STABILIZATION_AND_DUALITY_PASS')

if __name__=='__main__':
    for n, ell in [(1,3),(2,2),(2,3),(3,2)]:
        direct_case(n, ell)
    global_combinatorics()
    print('CYCLIC_NAKAYAMA_IDEAL_MONOID_DIRECT_CHECK_PASS')
