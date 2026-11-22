"""Exact finite checks for graph-state cut ranks on hypercube networks.

Run: python3 VERIFY.py (Python 3 standard library only).
The proof for all even dimensions is algebraic; these tests are finite checks.
"""
from itertools import combinations
from random import Random


def rank_binary(rows):
    basis = {}
    for value in rows:
        x = value
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                break
    return len(basis)


def cut_rows(dimension, omitted):
    even = [x for x in range(1 << dimension) if x.bit_count() % 2 == 0]
    odd = [x for x in range(1 << dimension) if x.bit_count() % 2 == 1]
    index = {x: i for i, x in enumerate(odd)}
    omit = {frozenset(edge) for edge in omitted}
    result = []
    for v in even:
        bits = 0
        for direction in range(dimension):
            w = v ^ (1 << direction)
            if frozenset((v, w)) not in omit:
                bits |= 1 << index[w]
        result.append(bits)
    return result


def omissions(dimension):
    # One edge in each two-dimensional square fiber:
    # remove the x_1-directed edge at x_2=0.
    return [(v, v ^ 1) for v in range(1 << dimension) if not (v & 1) and not (v & 2)]


def alternative_rank_mod2(rows, dimension):
    # Independent column-oriented elimination, rather than row-bitset elimination.
    m = len(rows)
    basis = [0] * m
    rank = 0
    for j in range(m):
        x = sum(((rows[i] >> j) & 1) << i for i in range(m))
        while x:
            p = (x & -x).bit_length() - 1
            if basis[p]:
                x ^= basis[p]
            else:
                basis[p] = x
                rank += 1
                break
    return rank


def check():
    trials = 0
    rng = Random(20261119)
    for d in (2, 4, 6, 8):
        target = 1 << (d - 1)
        edges = omissions(d)
        r0 = rank_binary(cut_rows(d, []))
        assert r0 == (1 << (d - 2)), (d, r0)
        assert len(edges) == (1 << (d - 2))
        used = [v for edge in edges for v in edge]
        assert len(set(used)) == len(used)
        full = rank_binary(cut_rows(d, edges))
        assert full == target, (d, full)
        assert alternative_rank_mod2(cut_rows(d, edges), d) == full
        print(f'dimension={d}, initial={r0}, final={full}, removed={len(edges)}')
        if d <= 6:
            sizes = range(len(edges) + 1)
            subsets = (c for k in sizes for c in combinations(range(len(edges)), k))
        else:
            subsets = (tuple(sorted(rng.sample(range(len(edges)), rng.randrange(len(edges) + 1)))) for _ in range(240))
        count = 0
        for subset in subsets:
            rows = cut_rows(d, [edges[i] for i in subset])
            r = rank_binary(rows)
            assert r == r0 + len(subset), (d, subset, r)
            if d <= 4 or count % 53 == 0:
                assert alternative_rank_mod2(rows, d) == r
            count += 1
        trials += count
        print(f'  subset tests={count}')
    # Odd dimensions have a pre-existing maximal parity cut.
    for d in (1, 3, 5, 7):
        r = rank_binary(cut_rows(d, []))
        assert r == (1 << (d - 1)), (d, r)
        print(f'odd dimension={d}, baseline={r}')
    print(f'PASS {trials} subset ranks, with selected independent column checks')


if __name__ == '__main__':
    check()
