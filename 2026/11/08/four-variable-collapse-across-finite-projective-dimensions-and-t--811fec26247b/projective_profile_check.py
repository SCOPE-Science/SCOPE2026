"""Finite checks for elementary point-collinearity extension profiles.

All computations are independent finite corroboration, not substitutes for the
projective-geometric argument used in the accompanying proof.
"""
from itertools import product, combinations


def projective_points(d, q):
    assert q in (2, 3, 5, 7), 'Prime-field computation only'
    points = set()
    for vector in product(range(q), repeat=d + 1):
        if not any(vector):
            continue
        leading = next(v for v in vector if v)
        factor = pow(leading, -1, q)
        points.add(tuple((factor * v) % q for v in vector))
    return sorted(points)


def collinear(a, b, c, q):
    # All three repeated-point configurations are declared collinear.
    if a == b or a == c or b == c:
        return True
    first = next(i for i, (u, v) in enumerate(zip(a, b)) if u != v)
    # Since a,b are independent normalized projective vectors, find a nonzero 2x2 minor.
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            det = (a[i] * b[j] - a[j] * b[i]) % q
            if det:
                r = ((c[i] * b[j] - c[j] * b[i]) * pow(det, -1, q)) % q
                s = ((a[i] * c[j] - a[j] * c[i]) * pow(det, -1, q)) % q
                return all((r * x + s * y - z) % q == 0 for x, y, z in zip(a, b, c))
    raise AssertionError('Distinct projective points must be independent')


def extension_profiles(points, q, anchors):
    # Includes equality and all atomic C-relations involving the new point.
    # C on solely anchored triples already belongs to the stationary type.
    n = len(anchors)
    signatures = set()
    for x in points:
        eq = tuple(x == a for a in anchors)
        lines = tuple(collinear(anchors[i], anchors[j], x, q)
                      for i, j in combinations(range(n), 2))
        signatures.add((eq, lines))
    return signatures


def witness_counts(points, q, anchors):
    n = len(anchors)
    counts = {}
    for x in points:
        eq = tuple(x == a for a in anchors)
        lines = tuple(collinear(anchors[i], anchors[j], x, q)
                      for i, j in combinations(range(n), 2))
        key = (eq, lines)
        counts[key] = counts.get(key, 0) + 1
    return counts


def standard_representatives(d):
    e = [tuple(int(i == j) for i in range(d + 1)) for j in range(d + 1)]
    return {
        'empty': (),
        'singleton': (e[0],),
        'pair': (e[0], e[1]),
        'collinear_triple': (e[0], e[1], tuple(a + b for a, b in zip(e[0], e[1]))),
        'noncollinear_triple': (e[0], e[1], e[2]),
    }


def main():
    profiles_by_class = {}
    tested = []
    for q, d in ((2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4), (5, 2), (5, 3)):
        points = projective_points(d, q)
        assert len(points) == (q ** (d + 1) - 1) // (q - 1)
        reps = standard_representatives(d)
        for pattern, anchors in reps.items():
            prof = extension_profiles(points, q, anchors)
            key = ('line_3' if q == 2 else 'line_ge4', pattern)
            if key in profiles_by_class:
                assert prof == profiles_by_class[key], (key, q, d, prof ^ profiles_by_class[key])
            else:
                profiles_by_class[key] = prof
        cc = witness_counts(points, q, reps['collinear_triple'])
        nc = witness_counts(points, q, reps['noncollinear_triple'])
        counts = [len(extension_profiles(points, q, reps[x])) for x in reps]
        assert len(cc) == (4 if q == 2 else 5), (q,d,cc)
        assert len(nc) == 7, (q,d,nc)
        # Four-pebble collinearity cutoffs, and the two-line skew witness.
        e = [tuple(int(i == j) for i in range(d + 1)) for j in range(d + 1)]
        if d >= 3:
            assert all(not (collinear(e[0], e[1], z, q) and collinear(e[2], e[3], z, q)) for z in points)
        else:
            # By dimension, line spans from arbitrary distinct points must intersect.
            for a,b in combinations(points,2):
                for c,f in combinations(points,2):
                    if not any(collinear(a,b,z,q) and collinear(c,f,z,q) for z in points):
                        raise AssertionError(('unexpected skew lines in plane',q,a,b,c,f))
        tested.append((q,d,len(points),counts,len(cc),len(nc)))
    for row in tested:
        print('q=%d d=%d vertices=%d extension-types=%s collinear=%d noncollinear=%d' % row)
    print('PASS: eight projective geometries, all five stationary classes, F04 profiles, skew-line boundary')


if __name__ == '__main__':
    main()
