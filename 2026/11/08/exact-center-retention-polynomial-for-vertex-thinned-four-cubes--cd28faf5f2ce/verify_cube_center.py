#!/usr/bin/env python3
"""Exact center-containment reliability of the four-cube.

Run with Python 3 (standard library only). All linear algebra uses fractions;
all counts use finite integer enumeration. The two count routes are independent.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb


def dependence(cols):
    """Return unique nonzero rational kernel vector, or None."""
    rows = [[Q(col[i]) for col in cols] for i in range(4)]
    m = len(cols)
    pivot_cols = []
    r = 0
    for j in range(m):
        q = next((k for k in range(r, 4) if rows[k][j]), None)
        if q is None:
            continue
        rows[r], rows[q] = rows[q], rows[r]
        d = rows[r][j]
        rows[r] = [a / d for a in rows[r]]
        for k in range(4):
            if k != r:
                d = rows[k][j]
                rows[k] = [rows[k][t] - d * rows[r][t] for t in range(m)]
        pivot_cols.append(j)
        r += 1
        if r == 4:
            break
    free = [j for j in range(m) if j not in pivot_cols]
    if len(free) != 1:
        return None
    v = [Q(0) for _ in range(m)]
    v[free[0]] = Q(1)
    for k, j in enumerate(pivot_cols):
        v[j] = -rows[k][free[0]]
    assert all(sum(col[i]*v[j] for j, col in enumerate(cols)) == 0 for i in range(4))
    return v


def central_positive_circuits(vertices):
    out = set()
    for r in range(2, 6):
        for js in combinations(range(len(vertices)), r):
            v = dependence([vertices[j] for j in js])
            if v is not None and all(t != 0 for t in v) and (
                all(t > 0 for t in v) or all(t < 0 for t in v)
            ):
                out.add(sum(1 << j for j in js))
    return out


def histogram_by_minimal_circuits():
    points = list(product((-1, 1), repeat=4))
    circuits = central_positive_circuits(points)
    assert len(circuits) == 48
    assert [sum(x.bit_count() == k for x in circuits) for k in range(2, 6)] == [8, 0, 24, 16]
    inside = [0] * 17
    for mask in range(1 << 16):
        if any(mask & c == c for c in circuits):
            inside[mask.bit_count()] += 1
    return inside


def histogram_by_threshold_topes():
    # The eight antipodal-pair representatives have first coordinate +1.
    reps = [(1,) + z for z in product((-1, 1), repeat=3)]
    bad_circuits = []
    for r in range(2, 6):
        for js in combinations(range(8), r):
            coeff = dependence([reps[j] for j in js])
            if coeff is not None and all(t for t in coeff):
                signs = tuple(1 if t > 0 else -1 for t in coeff)
                bad_circuits.append((js, signs))
    assert len(bad_circuits) == 20
    assert [sum(len(js) == k for js, _ in bad_circuits) for k in range(2, 6)] == [0, 0, 12, 8]

    topes = []
    for ss in product((-1, 1), repeat=8):
        forbidden = any(
            all(ss[j] == z[k] for k, j in enumerate(js)) or
            all(ss[j] == -z[k] for k, j in enumerate(js))
            for js, z in bad_circuits
        )
        if not forbidden:
            topes.append(ss)
    assert len(topes) == 104

    # Independently show every circuit-admissible sign pattern is REALIZABLE
    # by a concrete integer normal with coordinates in [-2,2].
    normals = set()
    for a in product(range(-2, 3), repeat=4):
        values = [sum(x * y for x, y in zip(a, z)) for z in reps]
        if all(values):
            normals.add(tuple(1 if v > 0 else -1 for v in values))
    assert set(topes) == normals

    # Vertex indexing here interlaces each antipodal pair (+v_i, -v_i).
    masks = [sum(1 << (2*j + (s == 1)) for j, s in enumerate(ss))
             for ss in topes]
    outside = [0] * 17
    for mask in range(1 << 16):
        if any(mask & ~t == 0 for t in masks):
            outside[mask.bit_count()] += 1
    return [comb(16,k) - outside[k] for k in range(17)], outside


def main():
    inside_circuit = histogram_by_minimal_circuits()
    inside_tope, outside = histogram_by_threshold_topes()
    expected_outside = [1,16,112,448,1096,1584,1312,576,104] + [0] * 8
    assert outside == expected_outside
    assert inside_tope == inside_circuit
    assert sum(outside) == 5249
    assert sum(inside_circuit) == 60287
    assert inside_circuit[8] == 12766
    print('AVOIDANCE_CARDINALITY_COUNTS:', outside)
    print('CONTAINMENT_CARDINALITY_COUNTS:', inside_circuit)
    print('PROBABILITY_AT_HALF: 60287/65536')
    print('CUBE4_EXACT_RELIABILITY_TWO_CERTIFICATES_PASSED')

if __name__ == '__main__':
    main()
