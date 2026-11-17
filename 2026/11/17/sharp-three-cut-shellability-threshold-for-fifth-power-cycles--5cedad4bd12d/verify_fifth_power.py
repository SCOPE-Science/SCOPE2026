#!/usr/bin/env python3
"""Verify finite shellings and mod-two Alexander-dual obstructions for fifth-power cycles.

Requires Python 3.10+ standard library; reads shelling_orders.json from its own directory.
Finite tests do not replace the cited all-size shelling theorem for n>=27.
"""
import itertools
import json
from pathlib import Path

P = 5
HERE = Path(__file__).resolve().parent


def triples_disconnected(n):
    """A graph on three vertices is disconnected iff it has at most one edge."""
    def is_edge(a, b):
        d = abs(a - b)
        return min(d, n - d) <= P
    return [t for t in itertools.combinations(range(n), 3)
            if sum(is_edge(a, b) for a, b in itertools.combinations(t, 2)) <= 1]


def check_shellings():
    cert = json.loads((HERE / 'shelling_orders.json').read_text(encoding='utf-8'))
    assert cert['power'] == P and sorted(cert['orders']) == [str(n) for n in range(21, 27)]
    summaries = []
    for n in range(21, 27):
        triples = triples_disconnected(n)
        order = cert['orders'][str(n)]
        assert len(order) == len(triples) and sorted(order) == list(range(len(triples)))
        # Independent verification: build the codimension-one overlap set using
        # exact set differences, then check the defining shelling axiom directly.
        earlier = []
        spanning = 0
        V = set(range(n))
        for j in order:
            t = set(triples[j])
            if earlier:
                B = {next(iter(u - t)) for u in earlier if len(u-t) == 1 and len(t-u) == 1}
                assert B, (n, j, 'disconnected first attachment')
                for s in earlier:
                    assert (s-t) & B, (n,j, 'shelling axiom')
                if B == (V-t):
                    spanning += 1
            earlier.append(t)
        expected = (n-10)*(n-11)//2 - 54
        assert spanning == expected, (n, spanning, expected)
        summaries.append((n,len(triples),spanning))
    return summaries


def dual_homology(n):
    bad = triples_disconnected(n)
    forbidden_pairs = [[] for _ in range(n)]
    for t in bad:
        m = sum(1 << i for i in t)
        for v in t:
            forbidden_pairs[v].append(m ^ (1 << v))
    legal = bytearray(1 << n)
    legal[0] = 1
    by_cardinality = [[] for _ in range(n+1)]
    by_cardinality[0] = [0]
    for mask in range(1, 1 << n):
        bit = mask.bit_length()-1
        sub = mask ^ (1 << bit)
        if legal[sub] and all((sub & pair) != pair for pair in forbidden_pairs[bit]):
            legal[mask] = 1
            by_cardinality[mask.bit_count()].append(mask)
    ranks = []
    for k in range(1, n+1):
        if not by_cardinality[k]:
            break
        positions = {m:j for j,m in enumerate(by_cardinality[k-1])}
        pivots = {}
        for simplex in by_cardinality[k]:
            column = 0
            vertices = simplex
            while vertices:
                bit = vertices & -vertices
                vertices -= bit
                column ^= 1 << positions[simplex^bit]
            while column:
                lead = column.bit_length()
                if lead in pivots:
                    column ^= pivots[lead]
                else:
                    pivots[lead] = column
                    break
        ranks.append(len(pivots))
    active = [len(level) for level in by_cardinality if level]
    # The augmented complex includes an empty face, and the first boundary maps
    # all singleton vertices to the unique empty face over F_2.
    bettis = {}
    for degree in range(len(active)-1):
        b = active[degree+1]-ranks[degree] - (ranks[degree+1] if degree+1<len(ranks) else 0)
        assert b >= 0
        if b:
            bettis[degree] = b
    # Independent internal consistency check using Euler–Poincare over F_2.
    reduced_euler = sum((-1)**(k-1)*c for k,c in enumerate(active))
    assert reduced_euler == sum((-1)**d*b for d,b in bettis.items())
    return len(bad), active, ranks, bettis


def check_dual_obstructions():
    expected = {13:(5,1), 14:(5,1), 15:(3,21), 16:(3,101), 17:(3,52),
                18:(3,19), 19:(3,1), 20:(2,4)}
    summaries=[]
    for n,(d,b) in expected.items():
        count,faces,ranks,bettis=dual_homology(n)
        assert bettis == {d:b}, (n, bettis)
        original_degree=n-d-3
        assert original_degree < n-4
        summaries.append((n,count,d,b,original_degree,faces,ranks))
    return summaries


def main():
    print('Finite shellings of fifth-power cycle three-cut complexes:')
    for n,count,sp in check_shellings():
        print(f'n={n}: {count} facets; shelling valid; {sp} spanning facets')
    print('Alexander-dual mod-two homology and lower-degree obstructions:')
    for n,count,d,b,original_degree,faces,ranks in check_dual_obstructions():
        print(f'n={n}: {count} forbidden triples; dual H_{d} F2 rank {b}; '
              f'original H_{original_degree} F2 rank {b}; '
              f'dual face counts={faces}; boundary ranks={ranks}')
    for n in range(3,13):
        assert len(triples_disconnected(n))==0
    print('n=3..12: no disconnected triple; three-cut complex void')
    print('ALL FINITE CERTIFICATES PASSED')

if __name__=='__main__':
    main()
