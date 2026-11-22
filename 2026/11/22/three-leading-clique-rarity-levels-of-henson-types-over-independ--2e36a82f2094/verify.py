#!/usr/bin/env python3
"""Finite extension cross-checks for independent-base Henson type spectra.

Usage: python3 verify.py. Standard library only. Tests are corroborative;
the general statements require the written combinatorial proof.
"""
from collections import Counter
from itertools import combinations
from math import comb


def edges(r):
    return tuple(combinations(range(r), 2))


def q_cliques(r, q, graph):
    e = edges(r)
    adjacent = set(pair for i, pair in enumerate(e) if (graph >> i) & 1)
    return tuple(sum(1 << v for v in Q) for Q in combinations(range(r), q)
                 if all(pair in adjacent for pair in combinations(Q, 2)))


def base_direct(r, q, cliques):
    return sum(1 for neighbors in range(1 << r)
               if not any((neighbors & C) == C for C in cliques))


def is_clique_free(r, q, graph):
    return not q_cliques(r, q, graph)


def direct_old_new_adjacencies(r, q, cliques, m):
    # This separately enumerates each adjacency bit in the old-new incidence.
    # The named old graph is empty, so a forbidden (q+1)-clique uses <=1 old vertex.
    good = 0
    for pattern in range(1 << (r*m)):
        valid = True
        for old in range(m):
            old_neighborhood = (pattern >> (old*r)) & ((1 << r)-1)
            for C in cliques:
                if old_neighborhood & C == C:
                    valid = False
                    break
            if not valid:
                break
        good += valid
    return good


def exact_at_critical_arity(q, m):
    r = q+1
    n2 = comb(r, 2)
    n1 = r * (2**q-q-1)
    n0 = 2**comb(r, 2) - 1 - n1 - n2
    return n0*(2**r)**m + n1*(2**r-2)**m + n2*(2**r-3)**m


def check(q, r, m_values):
    numbers = Counter()
    total_by_m = {m: 0 for m in m_values}
    terms = 0
    critical_B = {0: 1 << r, 1: (1 << r)-(1 << (r-q)),
                  2: (1 << r)-3*(1 << (r-q-1))} if r >= q+1 else {}
    for graph in range(1 << comb(r, 2)):
        if not is_clique_free(r, q+1, graph):
            continue
        C = q_cliques(r, q, graph)
        b = base_direct(r, q, C)
        numbers[(len(C),b)] += 1
        terms += 1
        if len(C)==0:
            assert b == (1 << r)
        elif len(C)==1:
            assert b == (1 << r)-(1 << (r-q))
        else:
            b2 = (1 << r)-3*(1 << (r-q-1))
            assert b <= b2
            if b==b2:
                assert len(C)==2 and C[0].bit_count()==q and C[1].bit_count()==q
                assert (C[0]&C[1]).bit_count()==q-1
            elif len(C)==2 and (C[0]&C[1]).bit_count()==q-1:
                raise AssertionError('missed equality')
        for m in m_values:
            total_by_m[m] += b**m
            if m and r*m <= 10:
                assert direct_old_new_adjacencies(r, q, C, m)==b**m
    if r == q+1:
        for m in m_values:
            assert total_by_m[m]==exact_at_critical_arity(q,m), (q,m,total_by_m[m])
        assert numbers[(0,2**r)]==2**comb(r,2)-1-(r*(2**q-q-1))-comb(r,2)
        assert numbers[(1,2**r-2)]==r*(2**q-q-1)
        assert numbers[(2,2**r-3)]==comb(r,2)
    return terms, total_by_m, numbers


def main():
    for q,r,mvals in [(3,4,(0,1,2)),(3,5,(0,1)),(3,6,(0,1)),(4,5,(0,1,2)),(5,6,(0,1))]:
        n, totals, groups=check(q,r,mvals)
        print('PASS',f'q={q} r={r}',f'K_(q+1)-free internal diagrams={n}',
              'type totals '+str(totals))
        if r==q+1:
            print('CRITICAL_COUNTS',q,
                  (groups[(0,2**r)],groups[(1,2**r-2)],groups[(2,2**r-3)]))
    print('ALL_FINITE_DIAGRAM_TESTS_PASS')


if __name__=='__main__':
    main()
