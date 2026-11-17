#!/usr/bin/env python3
"""Exact finite orbit-cell, collapse, and integer-chain verification.

Run with Python 3.10+ and SymPy: python verify_dihedral_cycle.py
No external data or network access is used.
"""
from collections import defaultdict
from functools import lru_cache
from sympy import ZZ, Matrix
from sympy.matrices.normalforms import smith_normal_form



def fixed_face_lefschetz(n, eps, shift):
    """Independent signed orbit-face formula for fixed-point Euler data."""
    perm = lambda x: (eps * x + shift) % n
    unseen = set(range(n))
    orbital_parts = []
    while unseen:
        start = min(unseen)
        orbit = set()
        cur = start
        while cur not in orbit:
            orbit.add(cur)
            unseen.remove(cur)
            cur = perm(cur)
        orbital_parts.append(orbit)
    valid = [a for a in orbital_parts
             if all((v + 1) % n not in a for v in a)]
    adj = [0] * len(valid)
    for i, a in enumerate(valid):
        for j in range(i):
            if any((v - 1) % n in valid[j] or
                   (v + 1) % n in valid[j] for v in a):
                adj[i] |= 1 << j
                adj[j] |= 1 << i

    @lru_cache(maxsize=None)
    def independent_minus_one(mask):
        if mask == 0:
            return 1
        bit = mask & -mask
        i = bit.bit_length() - 1
        return (independent_minus_one(mask ^ bit) -
                independent_minus_one(mask & ~(bit | adj[i])))

    # Reduced Lefschetz number for the action on Ind(C_n) is -I(-1),
    # where the allowed vertex-orbits are the vertices of the orbit graph.
    return -independent_minus_one((1 << len(valid)) - 1)


def burnside_euler(n):
    reduced = sum(fixed_face_lefschetz(n, eps, shift)
                  for eps in (1, -1) for shift in range(n))
    assert reduced % (2 * n) == 0
    return 1 + reduced // (2 * n)


def model(n):
    """Generate the barycentric orbit-CW complex and collapse free pairs."""
    perms = [[(eps * i + k) % n for i in range(n)]
             for eps in (1, -1) for k in range(n)]

    @lru_cache(maxsize=None)
    def transform(mask, permutation_id):
        mapping = perms[permutation_id]
        result = 0
        while mask:
            lowest = mask & -mask
            result |= 1 << mapping[lowest.bit_length() - 1]
            mask -= lowest
        return result

    @lru_cache(maxsize=None)
    def canonical(chain):
        return min(tuple(transform(face, j) for face in chain)
                   for j in range(2 * n))

    # Bit-mask faces, exactly those subsets with no two cyclic neighbors.
    faces = sorted((s for s in range(1, 1 << n)
                    if all(not (s & (1 << i) and
                                s & (1 << ((i + 1) % n)))
                           for i in range(n))),
                   key=lambda s: (s.bit_count(), s))
    by_top = {}
    cells = defaultdict(set)
    for idx, face in enumerate(faces):
        chains = [(face,)]
        for small in faces[:idx]:
            if small & face == small:
                chains.extend(chain + (face,) for chain in by_top[small])
        by_top[face] = chains
        for chain in chains:
            cells[len(chain) - 1].add(canonical(chain))
    raw_counts = tuple(len(cells[d]) for d in range(max(cells) + 1))

    def facets(chain):
        return [(canonical(chain[:j] + chain[j + 1:]), (-1) ** j)
                for j in range(len(chain))]

    # The action on a flag has no inversions: distinct ranks cannot be
    # interchanged. Thus every flag orbit is a regular quotient cell, with
    # signed facets obtained simply by deleting one level of the flag.
    live = {d: set(entries) for d, entries in cells.items()}
    removed = {}
    for d in range(max(cells), 0, -1):
        reverse = defaultdict(set)
        for upper in live[d]:
            for lower, _ in facets(upper):
                reverse[lower].add(upper)
        count = 0
        while True:
            pair = None
            for lower in sorted(live[d - 1]):
                surviving = reverse.get(lower, set()) & live[d]
                if len(surviving) == 1:
                    pair = (lower, next(iter(surviving)))
                    break
            if pair is None:
                break
            lower, upper = pair
            assert upper in live[d] and lower in live[d-1]
            live[d].remove(upper)
            live[d - 1].remove(lower)
            count += 1
        removed[d] = count
    dimensions = sorted(live)
    boundary = {}
    counts = tuple(len(live[d]) for d in dimensions)
    smith = {}
    for d in dimensions[1:]:
        lower = sorted(live[d - 1])
        upper = sorted(live[d])
        index = {a: i for i, a in enumerate(lower)}
        matrix = [[0] * len(upper) for _ in lower]
        for j, simplex in enumerate(upper):
            for facet, orientation in facets(simplex):
                assert facet in index, (n, d, simplex, facet)
                matrix[index[facet]][j] += orientation
        boundary[d] = Matrix(matrix)
        diagonal = smith_normal_form(boundary[d], domain=ZZ)
        smith[d] = tuple(abs(int(diagonal[j, j]))
                         for j in range(min(diagonal.shape))
                         if diagonal[j, j] != 0)
        assert all(t == 1 for t in smith[d]), (n, d, smith[d])
    for d in dimensions[2:]:
        assert boundary[d-1] * boundary[d] == Matrix.zeros(
            boundary[d-1].rows, boundary[d].cols)
    homology_ranks = {}
    for d in dimensions:
        r_prev = len(smith[d]) if d in smith else 0
        r_next = len(smith[d + 1]) if d + 1 in smith else 0
        homology_ranks[d] = len(live[d]) - r_prev - r_next
    # Independent alternating-cell-count check: collapse preserves Euler char.
    assert sum((-1) ** d * v for d, v in enumerate(raw_counts)) == \
           sum((-1) ** d * len(live[d]) for d in dimensions)
    assert sum((-1) ** d * raw_counts[d] for d in range(len(raw_counts))) == burnside_euler(n)
    assert homology_ranks.get(0) == 1
    return raw_counts, removed, counts, smith, homology_ranks


def main():
    for n in range(3, 14):
        raw, removed, counts, snf, ranks = model(n)
        higher = {d: r for d, r in ranks.items() if d > 0 and r}
        expected = {3: 1} if n in (11, 13) else {}
        assert higher == expected, (n, higher, expected)
        print(f"n={n}; raw_cells={raw}; collapse_pairs={removed}; "
              f"remaining_cells={counts}; integral_smith="
              f"{ {d: (len(snf[d]), sorted(set(snf[d]))) for d in snf} }; "
              f"homology_free_ranks={higher}; torsion=none; "
              f"Burnside_Euler={burnside_euler(n)}")
    print("EXACT_DIHEDRAL_CYCLE_QUOTIENT_CHECK_PASS_n=3..13")


if __name__ == '__main__':
    main()
