#!/usr/bin/env python3
"""Exact integer verification of the equivariant rooted-forest character.

No external dependencies. The infinite-family theorem also has a symbolic
proof; finite enumeration here checks small instances and the full K_4,4
character table.
"""
from collections import Counter
from itertools import product
from math import factorial

PARTS = ((4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1))
PRESERVE_CHARACTER = (
    7, 0, 3, 3, 3,
    0, 0, 0, 0,
    63, 3, -9,
    15, -45,
    5103,
)
EXCHANGE_CHARACTER = (-1, 0, 3, -1, 27)


def rooted_forests(m):
    n = 2 * m
    arcs = [(u, v) for u in range(n) for v in range(n)
            if (u < m) != (v < m)]
    arc_index = {edge: i for i, edge in enumerate(arcs)}
    options = [[None] + [v for v in range(n)
                         if (u < m) != (v < m)] for u in range(n)]
    faces = []
    for assignment in product(*options):
        acyclic = True
        for start in range(n):
            v = start
            for _ in range(n):
                v = assignment[v]
                if v is None:
                    break
                if v == start:
                    acyclic = False
                    break
            if not acyclic:
                break
        if acyclic:
            mask = sum((1 << arc_index[(u, v)])
                       for u, v in enumerate(assignment) if v is not None)
            faces.append(mask)
    assert len(faces) == len(set(faces))
    return arcs, arc_index, faces


def cycle_representative(parts):
    p = list(range(4))
    start = 0
    for length in parts:
        for i in range(length):
            p[start+i] = start + (i+1) % length
        start += length
    assert start == 4
    return p


def trace_via_fixed_faces(arcs, arc_index, faces, perm):
    length = len(arcs)
    transformed = [arc_index[(perm[u], perm[v])] for u, v in arcs]
    seen = set()
    orbit_masks = []
    for start in range(length):
        if start in seen:
            continue
        mask = 0
        x = start
        while x not in seen:
            seen.add(x)
            mask |= 1 << x
            x = transformed[x]
        assert x == start
        orbit_masks.append(mask)
    orbit_face_count = Counter()
    for face in faces:
        used_orbits = 0
        for orbit in orbit_masks:
            intersection = face & orbit
            if intersection and intersection != orbit:
                break
            if intersection:
                used_orbits += 1
        else:
            orbit_face_count[used_orbits] += 1
    # The sign of g on a face with e edges and r complete g-orbits is (-1)^(e-r).
    # Consequently its contribution to the signed face enumerator at -1 is (-1)^r.
    # The reduced Lefschetz number is the negative of this alternating sum.
    value = -sum((-1)**r * count for r, count in orbit_face_count.items())
    return value, sum(orbit_face_count.values())


def conjugacy_class_size(part):
    multiplicity = Counter(part)
    z = 1
    for length, count in multiplicity.items():
        z *= length**count * factorial(count)
    return factorial(4)//z


def verify():
    arcs, arc_index, faces = rooted_forests(4)
    assert len(arcs) == 32 and len(faces) == 140625
    assert Counter(mask.bit_count() for mask in faces) == Counter({
        0:1, 1:32, 2:432, 3:3200, 4:14080, 5:36864, 6:53248, 7:32768,
    })

    values = []
    classes = []
    for i, a in enumerate(PARTS):
        for b in PARTS[i:]:
            p, q = cycle_representative(a), cycle_representative(b)
            g = p + [x+4 for x in q]
            value, _ = trace_via_fixed_faces(arcs, arc_index, faces, g)
            classes.append(conjugacy_class_size(a)*conjugacy_class_size(b)
                           * (1 if a==b else 2))
            values.append(value)
    assert tuple(values) == PRESERVE_CHARACTER

    for a in PARTS:
        p = cycle_representative(a)
        g = [4+p[i] for i in range(4)] + list(range(4))
        value, _ = trace_via_fixed_faces(arcs, arc_index, faces, g)
        values.append(value)
        classes.append(factorial(4)*conjugacy_class_size(a))
    assert tuple(values[15:]) == EXCHANGE_CHARACTER
    assert sum(classes) == 1152
    assert sum(s*v for s,v in zip(classes, values)) == 6912
    assert sum(s*v for s,v in zip(classes, values)) // 1152 == 6
    assert values[14] == 5103 and values[-1] == 27
    for m in (2, 3, 4):
        a, ai, fs = rooted_forests(m)
        sigma = [m+i for i in range(m)] + list(range(m))
        observed, _ = trace_via_fixed_faces(a, ai, fs, sigma)
        expected = (-1)**m * (m-1)**(m-1)
        assert observed == expected, (m, observed, expected)
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
