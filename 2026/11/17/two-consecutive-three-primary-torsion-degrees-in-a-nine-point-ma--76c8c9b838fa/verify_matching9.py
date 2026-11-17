#!/usr/bin/env python3
"""Exact integral orbit-chain certificate for the nine-point matching complex.

Uses only the Python standard library; integer unit elimination is accompanied
by a rank-one residual certificate (cross products plus gcd).
"""
from collections import defaultdict
from itertools import combinations
from math import gcd

N = 9
EDGES = tuple(combinations(range(N), 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}


def all_matching_faces():
    out = set()
    for size in range(1, 5):
        for inds in combinations(range(len(EDGES)), size):
            if len({v for i in inds for v in EDGES[i]}) == 2 * size:
                out.add(inds)
    return out


def flags(faces):
    by_size = defaultdict(set)
    for face in faces:
        def visit(chain, current):
            by_size[len(chain)].add(tuple(reversed(chain)))
            for size in range(1, len(current)):
                for subface in combinations(current, size):
                    visit(chain + (subface,), subface)
        visit((face,), face)
    return by_size


def orbit_complex():
    faces = all_matching_faces()
    assert len(faces) == 2619
    flags_by_size = flags(faces)
    assert tuple(len(flags_by_size[k]) for k in range(1, 5)) == (2619, 21546, 41580, 22680)
    edge_actions = [tuple(EDGE_INDEX[tuple(sorted(((u + t) % N, (v + t) % N)))]
                          for u, v in EDGES) for t in range(N)]
    face_actions = [{f: tuple(sorted(a[i] for i in f)) for f in faces}
                    for a in edge_actions]
    orbit_ids, orbit_reps = {}, {}
    for k in range(1, 5):
        lookup, reps = {}, []
        for flag in sorted(flags_by_size[k]):
            if flag in lookup:
                continue
            j = len(reps)
            reps.append(flag)
            for a in face_actions:
                transformed = tuple(a[f] for f in flag)
                if transformed in lookup:
                    assert lookup[transformed] == j
                lookup[transformed] = j
        assert len(lookup) == len(flags_by_size[k])
        orbit_ids[k], orbit_reps[k] = lookup, reps
    counts = tuple(len(orbit_reps[k]) for k in range(1, 5))
    assert counts == (293, 2394, 4620, 2520), counts
    boundaries = {}
    for k in range(2, 5):
        cols = []
        for flag in orbit_reps[k]:
            entries = defaultdict(int)
            for i in range(k):
                face = flag[:i] + flag[i+1:]
                entries[orbit_ids[k-1][face]] += (-1)**i
            cols.append({r: a for r, a in entries.items() if a != 0})
        boundaries[k] = cols
    for k in range(3, 5):
        for col in boundaries[k]:
            composed = defaultdict(int)
            for j, coefficient in col.items():
                for r, v in boundaries[k-1][j].items():
                    composed[r] += coefficient * v
            assert not any(composed.values()), (k, composed)
    return boundaries, counts, faces


def integral_smith_certificate(columns):
    """Exact unimodular unit-pivot elimination and rank-one residual.

    Each pivot subtracts integer multiples of its column from other columns,
    then splits off a unit diagonal summand. These are integral unimodular
    operations. After all pivots, check that residual rank <=1 over Q via
    every 2x2 minor and that its unique SNF factor is the entries' gcd.
    """
    cols = {j: dict(x) for j, x in enumerate(columns)}
    rows = defaultdict(set)
    for j, col in cols.items():
        for r in col:
            rows[r].add(j)
    pivots = 0
    while True:
        choice = None
        best = float('inf')
        for j, col in cols.items():
            for r, a in col.items():
                if a not in (-1, 1):
                    continue
                weight = len(col) * len(rows[r])
                if weight < best:
                    best, choice = weight, (r, j, a)
                if best == 1:
                    break
            if best == 1:
                break
        if choice is None:
            break
        r, j, pivot_value = choice
        pivot_col = dict(cols[j])
        for other in list(rows[r] - {j}):
            col = cols[other]
            multiple = col[r] // pivot_value
            assert multiple * pivot_value == col[r]
            for rr, a in pivot_col.items():
                old = col.get(rr, 0)
                new = old - multiple*a
                if new:
                    col[rr] = new
                    rows[rr].add(other)
                elif old:
                    del col[rr]
                    rows[rr].discard(other)
        for rr in pivot_col:
            rows[rr].discard(j)
        del cols[j]
        pivots += 1
    remaining = [c for c in cols.values() if c]
    rr = sorted(set(r for col in remaining for r in col))
    if remaining:
        pivot = remaining[0]
        first_r = next(iter(pivot))
        first_a = pivot[first_r]
        for col in remaining:
            for r in rr:
                assert col.get(r, 0)*first_a == col.get(first_r, 0)*pivot.get(r, 0)
    divisor = 0
    for col in remaining:
        for a in col.values():
            divisor = gcd(divisor, abs(a))
    assert divisor in (0, 3), divisor
    # Rank-one nonzero residual contributes one nonunit elementary divisor.
    rank = pivots + int(divisor != 0)
    return pivots, divisor, rank, len(rr), len(remaining)


def fixed_points(faces):
    for shift, expected in [(1, 0), (2, 0), (3, 9), (4, 0), (6, 9)]:
        invariant = 0
        for f in faces:
            mapped = tuple(sorted(EDGE_INDEX[tuple(sorted(((EDGES[i][0]+shift)%N,
                    (EDGES[i][1]+shift)%N)))] for i in f))
            invariant += (mapped == f)
        assert invariant == expected, (shift, invariant)


def main():
    boundaries, counts, faces = orbit_complex()
    fixed_points(faces)
    certificate = [integral_smith_certificate(boundaries[k]) for k in (2, 3, 4)]
    assert certificate == [(292,0,292,0,0), (2101,3,2102,2,442),
                           (2511,3,2512,84,4)], certificate
    r1,r2,r3 = (c[2] for c in certificate)
    assert counts[1]-r1-r2 == 0
    assert counts[2]-r2-r3 == 6
    assert counts[3]-r3 == 8
    assert counts[0]-r1 == 1
    assert counts[0]-counts[1]+counts[2]-counts[3] == -1
    print('MATCHING_9_C9_INTEGRAL_ORBIT_HOMOLOGY_PASS')
    print('flags_0_1_2_3=2619,21546,41580,22680')
    print('orbit_cells_0_1_2_3=293,2394,4620,2520')
    print('smith_d1_d2_d3=1^292;1^2101,3;1^2511,3')
    print('H0=Z;H1=Z/3;H2=Z^6+Z/3;H3=Z^8')
    print('fixed_matching_counts_shift1_shift2_shift3_shift4_shift6=0,0,9,0,9')

if __name__ == '__main__':
    main()
