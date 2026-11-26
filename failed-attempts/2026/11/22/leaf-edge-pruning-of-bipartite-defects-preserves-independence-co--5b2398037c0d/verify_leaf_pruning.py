"""Finite independent checks of a leaf-edge collapse theorem.

Use: python verify_leaf_pruning.py
No external dependencies. This checker verifies finite instances; the uniform proof
is supplied separately.
"""
from itertools import combinations
from random import Random


def complex_faces(a, b, defect):
    """Ind(K_{a,b} minus defect), represented by all faces as frozensets."""
    V = range(a + b)
    result = {frozenset()}
    for k in range(1, a + b + 1):
        for tup in combinations(V, k):
            S = frozenset(tup)
            if all((u, v) in defect for u in S if u < a
                   for v in S if v >= a):
                result.add(S)
    return result


def neighbors(a, b, defect, v):
    return [u for u in range(a + b)
            if (min(u, v), max(u, v)) in defect]


def check_collapse(a, b, defect, v, w):
    ns = neighbors(a, b, defect, w)
    assert neighbors(a, b, defect, v) == [w]
    assert len(ns) >= 2
    ns.remove(v)
    anchor, others = ns[0], ns[1:]
    K = complex_faces(a, b, defect)
    n_pairs = 0
    for r in range(len(others), -1, -1):
        for T in combinations(others, r):
            low = frozenset((v, w, *T))
            high = low | {anchor}
            assert low in K and high in K
            # A free face must have precisely one inclusion-maximal coface.
            assert [face for face in K if low < face] == [high]
            K.remove(low)
            K.remove(high)
            n_pairs += 1
    assert n_pairs == 2 ** (len(neighbors(a, b, defect, w)) - 2)
    old_edge = (min(v, w), max(v, w))
    assert K == complex_faces(a, b, defect - {old_edge})
    return n_pairs


def forest_component_count(a, b, defect):
    parent = list(range(a + b))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in defect:
        if find(u) == find(v):
            return None
        parent[find(u)] = find(v)
    return len({find(u) for e in defect for u in e})


def rank_mod2(columns):
    pivots = {}
    for col in columns:
        while col:
            p = col.bit_length() - 1
            if p not in pivots:
                pivots[p] = col
                break
            col ^= pivots[p]
    return len(pivots)


def reduced_betti_mod2(K):
    by_dim = {}
    for S in K:
        if S:
            by_dim.setdefault(len(S) - 1, []).append(tuple(sorted(S)))
    for dim in by_dim:
        by_dim[dim].sort()
    top = max(by_dim)
    ranks = {0: 0, top + 1: 0}
    for dim in range(1, top + 1):
        rows = {face: i for i, face in enumerate(by_dim[dim - 1])}
        columns = []
        for simplex in by_dim[dim]:
            col = 0
            for j in range(len(simplex)):
                face = simplex[:j] + simplex[j+1:]
                col ^= 1 << rows[face]
            columns.append(col)
        ranks[dim] = rank_mod2(columns)
    betti = {dim: len(by_dim[dim]) - ranks[dim] - ranks[dim + 1]
             for dim in range(top + 1)}
    betti[0] -= 1
    return {d: r for d, r in betti.items() if r}


def test_instance(a, b, defect):
    count = 0
    for v in range(a + b):
        adj = neighbors(a, b, defect, v)
        if len(adj) == 1:
            w = adj[0]
            if len(neighbors(a, b, defect, w)) >= 2:
                count += check_collapse(a, b, defect, v, w)
    cc = forest_component_count(a, b, defect)
    if cc is not None:
        expected = {0: 1} if cc == 0 else ({1: cc - 1} if cc >= 2 else {})
        assert reduced_betti_mod2(complex_faces(a, b, defect)) == expected
    return count, cc is not None


def main():
    cases = 0
    pairs = 0
    forests = 0
    for a, b in ((2, 2), (2, 3), (3, 3)):
        edges = [(u, v) for u in range(a) for v in range(a, a+b)]
        for bits in range(1 << len(edges)):
            defect = {e for j, e in enumerate(edges) if bits & (1 << j)}
            p, is_forest = test_instance(a, b, defect)
            pairs += p
            forests += is_forest
            cases += 1
    rng = Random(712043)
    random_cases = 0
    for _ in range(48):
        a, b = 4, 4
        edges = [(u, v) for u in range(a) for v in range(a, a+b)]
        defect = {e for e in edges if rng.randrange(4) == 0}
        p, is_forest = test_instance(a, b, defect)
        pairs += p
        forests += is_forest
        random_cases += 1
    print('PASS: all requested free-face pairs are valid; final complex matches edge deletion')
    print(f'Exhaustive bipartite defect graphs: {cases}')
    print(f'Additional deterministic random graphs: {random_cases}')
    print(f'Forest homology cross-checks (mod 2): {forests}')
    print(f'Elementary collapse pairs individually checked: {pairs}')
    print('Scope: small finite examples only; integral and unrestricted statements require the proof')

if __name__ == '__main__':
    main()
