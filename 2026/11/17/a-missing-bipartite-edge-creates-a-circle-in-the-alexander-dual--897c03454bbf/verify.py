"""Finite incidence, Alexander-duality, and mod-prime chain checks for K_{a,b}-e.

This is a diagnostic for the universal proof in RESULT.md, not an infinite proof.
Python 3.9+; only standard library is needed.
"""
from itertools import combinations
from math import comb


def disconnected_triples(a, b):
    vertices = range(a + b)
    left = frozenset(range(a))
    missing = frozenset((0, a))
    result = []
    for triple in combinations(vertices, 3):
        edges = sum(
            (x in left) != (y in left) and frozenset((x, y)) != missing
            for x, y in combinations(triple, 2)
        )
        if edges < 2:
            result.append(frozenset(triple))
    return result


def original_and_dual(a, b):
    vertices = frozenset(range(a + b))
    bad = disconnected_triples(a, b)
    dual = {frozenset()}
    for size in range(1, 5):
        for tup in combinations(sorted(vertices), size):
            face = frozenset(tup)
            if not any(triple <= face for triple in bad):
                dual.add(face)
    cut = {frozenset()}
    for triple in bad:
        complement = sorted(vertices - triple)
        for size in range(1, len(complement) + 1):
            cut.update(frozenset(t) for t in combinations(complement, size))
    return bad, dual, cut


def pivot_rank_mod(columns, p):
    pivots = {}
    for col in columns:
        current = {r: v % p for r, v in col if v % p}
        while current:
            lead = max(current)
            if lead not in pivots:
                scale = pow(current[lead], -1, p)
                pivots[lead] = {r: (v * scale) % p for r, v in current.items()}
                break
            multiplier = current[lead]
            for r, v in pivots[lead].items():
                updated = (current.get(r, 0) - multiplier * v) % p
                if updated:
                    current[r] = updated
                else:
                    current.pop(r, None)
    return len(pivots)


def betti_mod(faces, p):
    by_size = [[frozenset()]]
    by_size.extend(
        sorted((face for face in faces if len(face) == size),
               key=lambda face: tuple(sorted(face)))
        for size in range(1, max(map(len, faces)) + 1)
    )
    ranks = []
    for size in range(1, len(by_size)):
        rows = {face: index for index, face in enumerate(by_size[size - 1])}
        columns = []
        for face in by_size[size]:
            values = sorted(face)
            columns.append([
                (rows[frozenset(values[:i] + values[i + 1:])], (-1) ** i)
                for i in range(size)
            ])
        ranks.append(pivot_rank_mod(columns, p))
    return [
        len(by_size[size]) - ranks[size - 1] - (ranks[size] if size < len(ranks) else 0)
        for size in range(1, len(by_size))
    ]


def expected_dual(a, b):
    c = comb(a - 1, 2) * comb(b - 1, 2) - (a - 2) * (b - 2)
    return {1: 1, 3: c}


def run():
    cases = [(3, 3), (3, 4), (4, 4), (4, 5), (5, 5), (5, 6)]
    for a, b in cases:
        bad, dual, cut = original_and_dual(a, b)
        n = a + b
        assert len(bad) == comb(a, 3) + comb(b, 3) + n - 2
        eleft = {frozenset(s) for size in (0, 1, 2)
                 for s in combinations(range(a), size)}
        eright = {frozenset(s) for size in (0, 1, 2)
                  for s in combinations(range(a, n), size)}
        product = {x | y for x in eleft for y in eright}
        edge = frozenset((0, a))
        expected = {face for face in product if not edge <= face} | {edge}
        assert dual == expected, 'dual subcomplex not equal to edge deletion plus isolated edge'
        assert len(dual) == len(expected)
        theory = expected_dual(a, b)
        # Two distinct prime fields check signed chain boundaries independently.
        for p in (1009, 10007):
            actual = betti_mod(dual, p)
            for dimension in range(len(actual)):
                assert actual[dimension] == theory.get(dimension, 0), (a, b, p, actual)
            if n <= 10:
                actual_cut = betti_mod(cut, p)
                for dimension in range(len(actual_cut)):
                    predicted = (
                        theory[3] if dimension == n - 6 else
                        1 if dimension == n - 4 else 0
                    )
                    assert actual_cut[dimension] == predicted, (a, b, p, actual_cut)
        print(f'a={a}, b={b}: disconnected_triples={len(bad)}, dual_faces={len(dual)}, '
              f'cut_faces={len(cut)}, dual_betti_1=1, dual_betti_3={theory[3]}: PASS')
    print('COMPLETE_BIPARTITE_EDGE_DEFECT_THREE_CUT_PASS')


if __name__ == '__main__':
    run()
