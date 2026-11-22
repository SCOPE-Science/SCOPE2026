"""Finite consistency checks for first integral path-homology formula.

The theorem itself follows from the integral cocycle proof, not from these tests.
Run with Python 3 (standard library only).
"""
from itertools import combinations
from collections import defaultdict
import random

P = 1_000_003

def rank_sparse(columns, prime=P):
    pivots = {}
    for col in columns:
        work = {k: (v % prime) for k, v in col.items() if v % prime}
        while work:
            leading = min(work)
            if leading not in pivots:
                inv = pow(work[leading], -1, prime)
                pivots[leading] = {k: (v * inv) % prime for k, v in work.items()}
                break
            mul = work[leading]
            for key, val in pivots[leading].items():
                new = (work.get(key, 0) - mul * val) % prime
                if new:
                    work[key] = new
                else:
                    work.pop(key, None)
    return len(pivots)

def build_arcs(faces):
    vertices = sorted({v for f in faces for v in f})
    edges = sorted({tuple(sorted(e)) for f in faces for e in combinations(f, 2)})
    arcs = set()
    for e in edges:
        for v in e:
            arcs.add((('v', v), ('e', e)))
    for i, facet in enumerate(faces):
        for e in combinations(facet, 2):
            arcs.add((('e', tuple(sorted(e))), ('f', i)))
        for v in vertices:
            arcs.add((('f', i), ('v', v)))
    return arcs, len(vertices)+len(edges)+len(faces)

def degree_one_rank(faces, prime=P):
    arcs, n0 = build_arcs(faces)
    adjacent = defaultdict(list)
    for u, v in arcs:
        adjacent[u].append(v)
    twopaths = [(u, v, w) for u, v in arcs for w in adjacent[v]]
    forbidden_cols = []
    for u, v, w in twopaths:
        # Endpoints cannot be joined by a direct arc in this rank-cyclic graph.
        assert (u, w) not in arcs
        forbidden_cols.append({(u, w): 1})
    # rank of the forbidden-term map from C_2 to C_1^{all}/C_1^{allowed}
    forbidden_pairs = sorted({(u, w) for u, v, w in twopaths})
    pair_index = {x: i for i, x in enumerate(forbidden_pairs)}
    # Every 2-path has -1 on exactly its endpoint pair.
    # The admissible Omega_2 consists of integral differences sharing endpoints.
    by_pair = defaultdict(list)
    for u, v, w in twopaths:
        by_pair[(u, w)].append((u, v, w))
    vertex_arcs = {a: i for i, a in enumerate(sorted(arcs))}
    boundaries = []
    for group in by_pair.values():
        ref = group[0]
        for p in group[1:]:
            col = defaultdict(int)
            for sign, path in [(1, p), (-1, ref)]:
                u, v, w = path
                col[vertex_arcs[(v, w)]] += sign
                col[vertex_arcs[(u, v)]] += sign
            boundaries.append({k: v for k, v in col.items() if v})
    rank_d2 = rank_sparse(boundaries, prime)
    # The underlying directed graph is weakly connected, so rank boundary_1 = n0-1.
    return len(arcs) - (n0 - 1) - rank_d2

def facet_component_count(faces):
    parent = list(range(len(faces)))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i, a in enumerate(faces):
        for j in range(i):
            if len(set(a) & set(faces[j])) >= 2:
                parent[root(i)] = root(j)
    return len({root(i) for i in range(len(faces))})

def main():
    examples = [
        [(0,1,2)],
        [(0,1,2),(0,2,3)],
        [(0,1,2),(0,3,4)],
        [(0,1,2),(0,3,4),(0,5,6)],
        [(0,1,2),(0,1,3),(0,2,3),(1,2,3)],
        [(0,1,2),(0,2,3),(0,3,4),(0,4,1)],
    ]
    rng = random.Random(20261120)
    for n in range(3,7):
        candidates = list(combinations(range(n),3))
        for k in range(1, min(6,len(candidates))+1):
            for _ in range(3):
                sampled = rng.sample(candidates,k)
                # Connected 1-skeleton is required for the theorem.
                all_vertices = {x for f in sampled for x in f}
                connected = set(sampled[0])
                while True:
                    nxt = connected | {x for f in sampled if set(f)&connected for x in f}
                    if nxt == connected:break
                    connected = nxt
                if connected == all_vertices:
                    examples.append(sampled)
    for i, faces in enumerate(examples):
        expected = facet_component_count(faces)
        for prime in (2, 3, 1_000_003):
            measured = degree_one_rank(faces, prime)
            assert measured == expected, (i, prime, faces, measured, expected)
    print(f'PASS: {len(examples)} connected pure two-complexes at each of three primes.')
    print('These are finite consistency checks, not a substitute for the integral proof.')

if __name__ == '__main__':
    main()
