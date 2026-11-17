#!/usr/bin/env python3
"""Finite independent checks for open-neighborhood complexes of vertex-punctured cubes.

No external dependencies. Python >=3.9. Uses exact GF(2) row elimination.
"""
from itertools import combinations
from math import comb


def parity(x):
    return x.bit_count() & 1


def all_faces_from_facets(facets):
    faces = set()
    for facet in facets:
        for k in range(1, len(facet) + 1):
            faces.update(combinations(facet, k))
    return faces


def mod2_rank(columns):
    pivots = {}
    for col in columns:
        while col:
            p = col.bit_length() - 1
            if p in pivots:
                col ^= pivots[p]
            else:
                pivots[p] = col
                break
    return len(pivots)


def profile(n, shore):
    vertices = [x for x in range(1 << n) if parity(x) == shore and x != 0]
    centers = [x for x in range(1 << n) if parity(x) != shore and x != 0]
    by_center = {
        x: tuple(sorted(y for y in vertices if (x ^ y).bit_count() == 1))
        for x in centers
    }
    facets = sorted(set(by_center.values()))
    assert len(facets) == len(centers) and all(len(f) >= 2 for f in facets)
    assert all(all(y != 0 and parity(y) == shore and (x ^ y).bit_count() == 1
                   for y in f) for x, f in by_center.items())
    faces = all_faces_from_facets(facets)
    counts = {k: sum(len(f) == k for f in faces) for k in range(1, n + 1)}
    edge_id = {f: i for i, f in enumerate(sorted(f for f in faces if len(f) == 2))}
    seen = {vertices[0]}
    changed = True
    while changed:
        old = len(seen)
        for u, v in edge_id:
            if u in seen or v in seen:
                seen.update((u, v))
        changed = len(seen) != old
    assert seen == set(vertices), (n, shore, "disconnected")
    triangles = [f for f in faces if len(f) == 3]
    rows = []
    for t in triangles:
        row = 0
        for e in combinations(t, 2):
            row ^= (1 << edge_id[e])
        rows.append(row)
    rank2 = mod2_rank(rows)
    betti1 = len(edge_id) - len(vertices) + 1 - rank2
    euler = sum((-1) ** (k - 1) * counts[k] for k in counts)
    betti2 = euler - 1 + betti1
    return facets, faces, counts, betti1, betti2


def verify_explicit_collapse(n, shore, facets, original_faces):
    # Pair each non-apex face of size at least 3 to its cone with that apex,
    # processing larger lower faces first; check elementary freeness at each step.
    faces = set(original_faces)
    pairs = 0
    for facet in facets:
        apex = min(facet)
        rest = tuple(x for x in facet if x != apex)
        for r in range(len(rest), 2, -1):
            for sub in combinations(rest, r):
                low = tuple(sorted(sub))
                top = tuple(sorted(sub + (apex,)))
                assert low in faces and top in faces
                for other in faces:
                    if len(other) > len(low) and set(low).issubset(other):
                        assert other == top, (n, shore, low, other, top)
                faces.remove(low)
                faces.remove(top)
                pairs += 1
    assert all(len(f) <= 3 for f in faces)
    assert 2 * pairs + len(faces) == len(original_faces)
    return pairs


def main():
    for n in range(3, 8):
        expected = (1 << (n - 3)) * (n*n - 5*n + 8) - 1 - comb(n - 1, 2)
        assert expected >= 0
        outputs = []
        for shore in (0, 1):
            facets, faces, counts, b1, b2 = profile(n, shore)
            assert b1 == 0 and b2 == expected, (n, shore, b1, b2, expected)
            pairs = verify_explicit_collapse(n, shore, facets, faces) if n <= 6 else None
            outputs.append((shore, len(faces), b1, b2, pairs))
        assert outputs[0][3] == outputs[1][3]
        print(f'n={n} expected_beta2={expected} shore_profiles={outputs}', flush=True)
    print('PUNCTURED_CUBE_NEIGHBORHOOD_INTEGRAL_PROOF_MOD2_CHECK_PASS')


if __name__ == '__main__':
    main()
