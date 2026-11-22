#!/usr/bin/env python3
"""Exact integer cellular check for a six-color cyclic graph-Hom quotient.

Standard-library Python 3. The graph-Hom cell poset is rebuilt from its
nonempty, pairwise-disjoint ordered lists; all maximal flags are subdivided
and divided by the simultaneous six-cycle on colors. The resulting oriented
orbit simplices give a genuine integral cellular chain complex.
"""
from itertools import product, combinations
from collections import defaultdict, Counter
import heapq

N = 6
ALL = (1 << N) - 1


def rotate(x, t):
    return ((x << t) & ALL) | (x >> (N - t)) if t else x


def orbit_key(flag):
    return min(tuple(tuple(rotate(x, t) for x in c) for c in flag)
               for t in range(N))


def cells():
    by_dim = [set() for _ in range(4)]
    for labels in product(range(4), repeat=N):
        if any(k not in labels for k in range(3)):
            continue
        blocks = tuple(sum(1 << i for i, a in enumerate(labels) if a == k)
                       for k in range(3))
        by_dim[sum(b.bit_count() - 1 for b in blocks)].add(blocks)
    assert [len(s) for s in by_dim] == [120, 540, 900, 540]
    return by_dim


def facets(cell):
    for i, block in enumerate(cell):
        if block.bit_count() < 2:
            continue
        for j in range(N):
            if block & (1 << j):
                b = list(cell)
                b[i] ^= (1 << j)
                yield tuple(b)


def quotient_flags(original):
    chains = [set() for _ in range(4)]
    full_count = 0

    def descend(reversed_chain):
        nonlocal full_count
        if len(reversed_chain) == 4:
            flag = tuple(reversed(reversed_chain))
            full_count += 1
            for length in range(1, 5):
                for selection in combinations(range(4), length):
                    chains[length - 1].add(
                        orbit_key(tuple(flag[i] for i in selection)))
            return
        for f in facets(reversed_chain[-1]):
            descend(reversed_chain + [f])

    for top in original[3]:
        descend([top])
    assert full_count == 19440
    assert [len(s) for s in chains] == [351, 3060, 5940, 3240]
    # Every nonmaximal cell extends to a maximal 3-cell: three disjoint
    # nonempty blocks can absorb every unused color, one at a time.
    return [sorted(s) for s in chains]


def boundaries(chains):
    indexes = [{flag: i for i, flag in enumerate(chains[k])} for k in range(4)]
    d = [None]
    for k in range(1, 4):
        entries = defaultdict(int)
        for j, flag in enumerate(chains[k]):
            for a in range(k + 1):
                face = orbit_key(flag[:a] + flag[a + 1:])
                entries[indexes[k - 1][face], j] += (-1) ** a
        entries = {key: value for key, value in entries.items() if value}
        assert all(abs(value) == 1 for value in entries.values())
        d.append(entries)
    assert [len(d[k]) for k in (1, 2, 3)] == [6120, 17820, 12960]
    for k in (1, 2):
        left = defaultdict(list)
        right = defaultdict(list)
        for (i, j), a in d[k].items():
            left[j].append((i, a))
        for (j, h), b in d[k + 1].items():
            right[h].append((j, b))
        for col, entries in right.items():
            accum = defaultdict(int)
            for intermediate, b in entries:
                for row, a in left[intermediate]:
                    accum[row] += a * b
            assert not any(accum.values()), (k, col)
    return d


def integer_unit_reduction(entries, target_rank, nonunit):
    # Each unit pivot is an integer basis change in adjacent chain groups.
    # The Schur-complement formula maintains the exact remainder.
    rows = defaultdict(dict)
    cols = defaultdict(dict)
    for (r, c), value in entries.items():
        rows[r][c] = value
        cols[c][r] = value
    heap = []
    for r, terms in rows.items():
        for c, value in terms.items():
            if abs(value) == 1:
                heapq.heappush(heap, ((len(terms) - 1) * (len(cols[c]) - 1), r, c))
    pivots = 0
    while heap:
        old_cost, r, c = heapq.heappop(heap)
        if r not in rows or c not in rows[r] or abs(rows[r][c]) != 1:
            continue
        actual_cost = (len(rows[r]) - 1) * (len(cols[c]) - 1)
        if old_cost != actual_cost:
            heapq.heappush(heap, (actual_cost, r, c))
            continue
        unit = rows[r][c]
        pivot_row = rows[r].copy()
        pivot_col = cols[c].copy()
        for rr, x in pivot_col.items():
            if rr == r:
                continue
            for cc, y in pivot_row.items():
                if cc == c:
                    continue
                value = rows[rr].get(cc, 0) - x * y * unit
                if value:
                    rows[rr][cc] = value
                    cols[cc][rr] = value
                    if abs(value) == 1:
                        heapq.heappush(heap, (
                            (len(rows[rr]) - 1) * (len(cols[cc]) - 1), rr, cc))
                elif cc in rows[rr]:
                    del rows[rr][cc]
                    del cols[cc][rr]
        for cc in pivot_row:
            if cc != c:
                del cols[cc][r]
        for rr in pivot_col:
            if rr != r:
                del rows[rr][c]
        del rows[r]
        del cols[c]
        pivots += 1
    assert pivots == target_rank
    all_entries = [(r, c, v) for r, terms in rows.items() for c, v in terms.items()]
    if nonunit is None:
        assert not all_entries
        return pivots, None
    assert all_entries
    assert all(abs(value) == nonunit for _, _, value in all_entries)
    rr, cc, pivot = all_entries[0]
    # This is an exact rank-one test, INCLUDING possible zero positions.
    assert all(rows[r].get(c, 0) * pivot == rows[r].get(cc, 0) * rows[rr].get(c, 0)
               for r in rows for c in cols)
    # Rank one plus an entry of exact absolute size nonunit proves the
    # sole remaining nonzero Smith invariant is exactly nonunit.
    return pivots, nonunit


def fixed_points(original):
    # Invariant original cells under each nonidentity rotation. For the
    # half-turn, six invariant 3-cubes each have a single fixed center.
    counts = []
    for t in range(1, N):
        stable = [c for dim_cells in original for c in dim_cells
                  if tuple(rotate(b, t) for b in c) == c]
        counts.append((t, len(stable), Counter(sum(b.bit_count()-1 for b in c)
                                                   for c in stable)))
    assert [(t, count) for t, count, _ in counts] == [
        (1, 0), (2, 0), (3, 6), (4, 0), (5, 0)]
    assert counts[2][2] == Counter({3: 6})


def main():
    original = cells()
    fixed_points(original)
    orbit = quotient_flags(original)
    assert sum((-1) ** k * len(orbit[k]) for k in range(4)) == -9
    ds = boundaries(orbit)
    proofs = [integer_unit_reduction(ds[1], 350, None),
              integer_unit_reduction(ds[2], 2709, 3),
              integer_unit_reduction(ds[3], 3229, 2)]
    assert proofs == [(350, None), (2709, 3), (3229, 2)]
    # Ranks are 350,2710,3230; all invariant factors determined exactly.
    ranks = [350, 2710, 3230]
    free = [len(orbit[0]) - ranks[0],
            len(orbit[1]) - ranks[0] - ranks[1],
            len(orbit[2]) - ranks[1] - ranks[2],
            len(orbit[3]) - ranks[2]]
    assert free == [1, 0, 0, 10]
    print('HOM_K3_K6_C6_INTEGRAL_HOMOLOGY_OK')
    print('orbit_cells', [len(x) for x in orbit])
    print('smith_d1', '1x350')
    print('smith_d2', '1x2709,3x1')
    print('smith_d3', '1x3229,2x1')
    print('integral_homology', 'H0=Z H1=Z/3 H2=Z/2 H3=Z^10')


if __name__ == '__main__':
    main()
