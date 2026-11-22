"""Reproducible finite checks of the simple two-letter de Bruijn flag complex.

Uses only the Python 3 standard library. The all-q homotopy statement is
proved separately; finite ranks here are corroboration, not that proof.
"""
from itertools import combinations
from math import comb


def rank_binary(columns):
    pivots = {}
    for vector in columns:
        while vector:
            p = vector.bit_length() - 1
            if p in pivots:
                vector ^= pivots[p]
            else:
                pivots[p] = vector
                break
    return len(pivots)


def check(q):
    vertices = [(a, b) for a in range(q) for b in range(q)]
    edges = [tuple(pair) for pair in combinations(vertices, 2)
             if pair[0][1] == pair[1][0] or pair[1][1] == pair[0][0]]
    edge_set = {frozenset(e) for e in edges}
    triangles = [t for t in combinations(vertices, 3)
                 if all(frozenset(e) in edge_set for e in combinations(t, 2))]
    assert not any(all(frozenset(e) in edge_set for e in combinations(c, 2))
                   for c in combinations(vertices, 4)), 'Unexpected 4-clique'
    # Independent triangle census, by the two theoretically specified types.
    cone = set()
    for b in range(q):
        for a in range(q):
            if a == b:
                continue
            for c in range(q):
                if c == b:
                    continue
                cone.add(tuple(sorted(((b, b), (a, b), (b, c)))))
    cycle = set()
    for a,b,c in combinations(range(q),3):
        cycle.add(tuple(sorted(((a,b),(b,c),(c,a)))))
        cycle.add(tuple(sorted(((a,c),(c,b),(b,a)))))
    assert set(triangles) == cone | cycle
    assert not (cone & cycle)
    assert len(cone) == q*(q-1)**2
    assert len(cycle) == 2*comb(q,3)
    assert len(edges) == q*(q-1)*(2*q+1)//2
    index_v = {v: i for i,v in enumerate(vertices)}
    index_e = {frozenset(e): i for i,e in enumerate(edges)}
    d1 = [(1 << index_v[a]) ^ (1 << index_v[b]) for a,b in edges]
    d2 = []
    for triangle in triangles:
        d2.append(sum(1 << index_e[frozenset(e)]
                      for e in combinations(triangle, 2)))
    rank1, rank2 = rank_binary(d1), rank_binary(d2)
    # The binary boundary condition is checked independently for each face.
    # XOR check without relying on the redundant arithmetic expression.
    assert all((d1[index_e[frozenset((a,b))]] ^
                d1[index_e[frozenset((a,c))]] ^
                d1[index_e[frozenset((b,c))]]) == 0
               for a,b,c in triangles)
    betti = (len(vertices)-rank1, len(edges)-rank1-rank2,
             len(triangles)-rank2)
    expected = (1, 0, (q-1)*(q-2)*(2*q-3)//6)
    assert betti == expected, (q, betti, expected)
    print(f'q={q}: f={len(vertices)},{len(edges)},{len(triangles)}; '
          f'ranks(d1,d2)={rank1},{rank2}; mod-2 Betti={betti}; PASS')

if __name__ == '__main__':
    for q in range(2, 9):
        check(q)
    print('All finite checks passed; the all-q integral homotopy proof is in RESULT.md.')
