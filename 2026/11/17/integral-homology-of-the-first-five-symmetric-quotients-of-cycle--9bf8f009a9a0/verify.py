#!/usr/bin/env python3
"""Exact integral orbit-chain construction for symmetric quotients of path-forest complexes.
Run with Python 3.9 or later: python verify.py
"""
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from math import gcd


def cells(n, r):
    """Orbit flags with r nonempty stages; words record arc-birth stages along paths."""
    sizes = []

    def parts(seq, remaining, low):
        if seq:
            sizes.append(tuple(seq))
        for j in range(low, remaining + 1):
            parts(seq + [j], remaining - j, j)

    parts([], n, 2)
    found = set()
    for profile in sizes:
        if sum(j - 1 for j in profile) < r:
            continue
        choices = [product(range(1, r + 1), repeat=j - 1) for j in profile]
        for components in product(*choices):
            if len({t for word in components for t in word}) == r:
                found.add(tuple(sorted(components)))
    return sorted(found)


def face(flag, index, r):
    """Delete the face at the index-th place in a barycentric chain, 1-based."""
    out = []
    for word in flag:
        if index == r:
            run = []
            for t in word:
                if t == r:
                    if run:
                        out.append(tuple(run))
                        run = []
                else:
                    run.append(t)
            if run:
                out.append(tuple(run))
        else:
            out.append(tuple(t if t <= index else
                             (index if t == index + 1 else t - 1)
                             for t in word))
    return tuple(sorted(out))


def chain_complex(n):
    groups = [cells(n, r) for r in range(1, n)]
    boundaries = [None]
    for k in range(1, n - 1):
        lookup = {cell: i for i, cell in enumerate(groups[k - 1])}
        cols = {}
        for j, flag in enumerate(groups[k]):
            col = {}
            for i in range(k + 1):
                row = lookup[face(flag, i + 1, k + 1)]
                col[row] = col.get(row, 0) + (-1) ** i
            cols[j] = {row: v for row, v in col.items() if v}
        boundaries.append(cols)
    return groups, boundaries


def chain_identity(boundaries):
    for k in range(2, len(boundaries)):
        for col in boundaries[k].values():
            result = defaultdict(int)
            for middle, a in col.items():
                for row, b in boundaries[k - 1][middle].items():
                    result[row] += a * b
            assert not any(result.values()), ('boundary squared nonzero', k)


def unit_reduce(groups, boundaries):
    deleted = [set() for _ in groups]
    pairs = []
    for k in range(1, len(groups)):
        cols = boundaries[k]
        row_cols = defaultdict(set)
        for c, vec in cols.items():
            for row in vec:
                row_cols[row].add(c)
        canceled = 0
        while True:
            pivot = None
            best = 10**30
            for c, vec in cols.items():
                for row, val in vec.items():
                    if abs(val) != 1:
                        continue
                    score = (len(vec) - 1) * (len(row_cols[row]) - 1)
                    if score < best:
                        best = score
                        pivot = (c, row, val)
                        if best == 0:
                            break
                if best == 0:
                    break
            if pivot is None:
                break
            c, row, a = pivot
            pivot_col = cols[c].copy()
            for other in list(row_cols[row]):
                if other == c:
                    continue
                multiple = cols[other][row] // a
                for rr, val in pivot_col.items():
                    v = cols[other].get(rr, 0) - multiple * val
                    if v:
                        cols[other][rr] = v
                        row_cols[rr].add(other)
                    else:
                        cols[other].pop(rr, None)
                        row_cols[rr].discard(other)
            for rr in pivot_col:
                row_cols[rr].discard(c)
            cols.pop(c)
            deleted[k - 1].add(row)
            deleted[k].add(c)
            if k >= 2:
                boundaries[k - 1].pop(row)
            if k + 1 < len(groups):
                for next_col in boundaries[k + 1].values():
                    next_col.pop(c, None)
            canceled += 1
        pairs.append(canceled)
    chain_identity(boundaries)
    for k in range(1, len(groups)):
        assert set(boundaries[k]) == set(range(len(groups[k]))) - deleted[k]
        assert all(not (set(vec) & deleted[k - 1])
                   for vec in boundaries[k].values())
    return [len(g) - len(d) for g, d in zip(groups, deleted)], boundaries, pairs


def homology_of_small_residual(dims, boundaries):
    # The reduced matrices in this range have at most one nonzero map,
    # which has rank one and a single Smith invariant equal to the gcd.
    active = []
    for k in range(1, len(dims)):
        vals = [v for vec in boundaries[k].values() for v in vec.values() if v]
        if vals:
            active.append((k, vals))
    assert len(active) <= 1, active
    ranks = [0] * len(dims)
    torsion = {}
    if active:
        k, vals = active[0]
        # In this range each nonzero reduced matrix has just one row or column.
        assert min(dims[k - 1], dims[k]) == 1
        ranks[k] = 1
        invariant = 0
        for val in vals:
            invariant = gcd(invariant, abs(val))
        if invariant > 1:
            torsion[k - 1] = invariant
    result = []
    for i, count in enumerate(dims):
        free_rank = count - ranks[i] - (ranks[i + 1] if i + 1 < len(dims) else 0)
        assert free_rank >= 0
        result.append((free_rank, torsion.get(i)))
    return result


def brute_orbit_counts(n):
    """Independent labeled-flag orbit enumeration for n=4,5."""
    ps = list(permutations(range(n)))
    arcs = [(i, j) for i in range(n) for j in range(n) if i != j]
    a_index = {a: i for i, a in enumerate(arcs)}
    maps = [[a_index[(p[i], p[j])] for i, j in arcs] for p in ps]

    def act(mask, perm):
        return sum(1 << perm[i] for i in range(len(arcs)) if mask & (1 << i))

    seen_faces = set()
    for p in ps:
        edges = [a_index[(p[i], p[i + 1])] for i in range(n - 1)]
        for m in range(1, 1 << (n - 1)):
            seen_faces.add(sum(1 << edges[j] for j in range(n - 1) if m & (1 << j)))

    flags = [set() for _ in range(n - 1)]
    def visit(stages, top):
        ordered = tuple(reversed(stages))
        flags[len(stages) - 1].add(min(tuple(act(x, mp) for x in ordered) for mp in maps))
        bits = [j for j in range(len(arcs)) if top & (1 << j)]
        for size in range(1, len(bits)):
            for sub in combinations(bits, size):
                next_mask = sum(1 << j for j in sub)
                visit(stages + [next_mask], next_mask)
    for top in seen_faces:
        visit([top], top)
    return [len(x) for x in flags]


def main():
    expected = {
        3: ([2, 2], [1, 1], [(1, None), (1, None)]),
        4: ([4, 9, 6], [1, 1, 1], [(1, None), (0, 2), (0, None)]),
        5: ([6, 29, 48, 24], [1, 0, 1, 1], [(1, None), (0, None), (1, None), (1, None)]),
        6: ([10, 83, 253, 300, 120], [1, 0, 0, 2, 1],
            [(1, None), (0, None), (0, None), (1, 2), (0, None)]),
        7: ([14, 215, 1114, 2352, 2160, 720], [1, 0, 0, 1, 2, 1],
            [(1, None), (0, None), (0, None), (0, 2), (1, None), (1, None)]),
    }
    for n, (counts, reduced, groups_expected) in expected.items():
        groups, ds = chain_complex(n)
        assert [len(x) for x in groups] == counts
        chain_identity(ds)
        survivors, ds, pairs = unit_reduce(groups, ds)
        result = homology_of_small_residual(survivors, ds)
        assert survivors == reduced, (n, survivors)
        assert result == groups_expected, (n, result)
        assert len(pairs) == n - 2
        print('n={} orbit_cells={} reduced_cells={} H={} unit_pairs={}'.format(
            n, counts, survivors, result, pairs))
    for n in (4, 5):
        assert brute_orbit_counts(n) == expected[n][0]
        print('n={} independent_labeled_flag_enumeration=PASS'.format(n))
    print('CYCLE_FREE_CHESSBOARD_SYMMETRIC_ORBIT_INTEGRAL_PASS n=3..7')


if __name__ == '__main__':
    main()
