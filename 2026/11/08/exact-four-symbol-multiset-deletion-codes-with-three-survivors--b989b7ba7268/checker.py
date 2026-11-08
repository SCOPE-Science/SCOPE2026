"""Self-contained exact checker for four-symbol, three-survivor multiset codes.

Requires Python 3.8+; uses integer arithmetic and the standard library only.
"""
from itertools import combinations
from math import comb


def compositions(n, q=4):
    def rec(k, r, prefix):
        if k == 1:
            yield tuple(prefix + (r,))
        else:
            for a in range(r + 1):
                yield from rec(k - 1, r - a, prefix + (a,))
    return list(rec(q, n, ()))


def overlap(a, b):
    return sum(min(x, y) for x, y in zip(a, b))


def descendants(a):
    """Independent direct enumeration of exactly-three-symbol submultisets."""
    return {u for u in compositions(3) if all(x <= y for x, y in zip(u, a))}


def compatibility_graph(vectors):
    adj = [0] * len(vectors)
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            if overlap(vectors[i], vectors[j]) <= 2:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return adj


def exists_compatible_subset(adj, target):
    """Exact finite recursion over all ordered selections, with safe cardinality pruning.

    A set of candidate indices is a bit mask. At each level its least index is
    either selected (and future candidates restricted to its graph neighbors)
    or skipped. Every sorted clique of target size occurs on exactly one path.
    """
    visited = 0
    witness = None

    def search(selected, candidates):
        nonlocal visited, witness
        visited += 1
        if len(selected) == target:
            witness = tuple(selected)
            return True
        remaining = target - len(selected)
        if candidates.bit_count() < remaining:
            return False
        while candidates:
            if candidates.bit_count() < remaining:
                break
            bit = candidates & -candidates
            v = bit.bit_length() - 1
            candidates ^= bit
            if search(selected + [v], candidates & adj[v]):
                return True
        return False

    exists = search([], (1 << len(adj)) - 1)
    return exists, visited, witness


def pure(n):
    return [tuple(n if i == j else 0 for i in range(4)) for j in range(4)]


def proposed_witness(n):
    if n == 3:
        return compositions(n)
    if n == 4:
        return pure(4) + [tuple(2 if j in pair else 0 for j in range(4))
                          for pair in combinations(range(4), 2)] + [(1, 1, 1, 1)]
    if n == 5:
        return pure(n) + [(0, 2, 2, 1), (2, 0, 1, 2)]
    if n in (6, 7, 8):
        return pure(n) + [(2, 2, 2, n - 6)]
    return pure(n)


def main():
    expected = {3: 20, 4: 11, 5: 6, 6: 5, 7: 5, 8: 5}
    absent_target = {4: 12, 5: 7, 6: 6, 7: 6, 8: 6}
    for n in range(3, 13):
        vertices = compositions(n)
        assert len(vertices) == comb(n + 3, 3)
        W = proposed_witness(n)
        assert len(W) == (expected[n] if n in expected else 4)
        assert len(set(W)) == len(W)
        assert all(sum(v) == n and min(v) >= 0 for v in W)
        for a, b in combinations(W, 2):
            assert overlap(a, b) <= 2
            assert descendants(a).isdisjoint(descendants(b))
        if n in absent_target:
            feasible, nodes, _ = exists_compatible_subset(compatibility_graph(vertices), absent_target[n])
            assert not feasible, (n, absent_target[n])
            print(f'n={n}: |simplex|={len(vertices)}; forbidden_size={absent_target[n]}; '
                  f'exhaustive_nodes={nodes}; no such code; lower_bound={len(W)}')
        else:
            print(f'n={n}: |simplex|={len(vertices)}; witness_size={len(W)}')
    # The n>=9 argument is the separate infinite combinatorial proof in RESULT.md.
    # Check the exact boundary and a sample of each subsequent length.
    for n in range(9, 13):
        assert all(max(v) >= 3 for v in compositions(n))
    print('PASS: all finite exhaustive upper bounds and witnesses verified')


if __name__ == '__main__':
    main()
