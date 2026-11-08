"""Standalone exact integer-normal checks for a family of expanded cubes.

Run: python verify.py
All scientific comparisons here are exact integer comparisons.
"""
from itertools import permutations, product


def vertices():
    return tuple(sorted({tuple(sign[j] * (2 if j == i else 1) for j in range(3))
                         for i in range(3) for sign in product((-1, 1), repeat=3)}))


def normals_at(v):
    """The four outward facet normals at a vertex of P_a, a>1."""
    i = next(j for j, x in enumerate(v) if abs(x) == 2)
    s = tuple(1 if x > 0 else -1 for x in v)
    out = []
    n = [0, 0, 0]
    n[i] = s[i]
    out.append(tuple(n))
    for j in range(3):
        if j != i:
            n = [0, 0, 0]
            n[i], n[j] = s[i], s[j]
            out.append(tuple(n))
    out.append(s)
    return tuple(out)


def dot(n, d):
    return sum(x*y for x, y in zip(n, d))


def illuminated(v, d):
    return all(dot(n, d) < 0 for n in normals_at(v))


def predicted_count(d):
    A = list(map(abs, d))
    assert all(A) and len(set(A)) == 3 and all(A[i] != A[j]+A[k]
        for i in range(3) for j, k in [tuple(x for x in range(3) if x != i)])
    return sum(1 + (A[i]>A[j]) + (A[i]>A[k]) + (A[i]>A[j]+A[k])
               for i in range(3) for j, k in [tuple(x for x in range(3) if x != i)])


def all_facets_at(v):
    """All active normals from the 26-inequality description at a=2."""
    norms = []
    for i in range(3):
        for s in (-1, 1):
            n = [0]*3
            n[i] = s
            if dot(n, v) == 2:
                norms.append(tuple(n))
    for i, j in ((0,1),(0,2),(1,2)):
        for si, sj in product((-1,1),repeat=2):
            n = [0]*3
            n[i], n[j] = si, sj
            if dot(n, v) == 3:
                norms.append(tuple(n))
    for n in product((-1,1),repeat=3):
        if dot(n,v) == 4:
            norms.append(n)
    return set(norms)


def main():
    V = vertices()
    assert len(V) == 24
    for v in V:
        assert all_facets_at(v) == set(normals_at(v)), (v, all_facets_at(v), normals_at(v))

    full = tuple(sorted({tuple(s[j]*p[j] for j in range(3))
            for p in set(permutations((4,2,1)))
            for s in product((-1,1), repeat=3)}))
    assert len(full) == 48
    counts = [sum(illuminated(v,d) for v in V) for d in full]
    assert set(counts) == {7}
    frequency = [sum(illuminated(v,d) for d in full) for v in V]
    assert set(frequency) == {14}

    cover = ((-4,-2,1), (-1,4,2), (2,1,-4), (4,-2,1))
    assert len(set(cover)) == 4
    assert all(d in full for d in cover)
    assert all(any(illuminated(v,d) for d in cover) for v in V)
    assert [sum(illuminated(v,d) for v in V) for d in cover] == [7]*4

    comparisons = 0
    for d in product(range(-5,6), repeat=3):
        if 0 in d or len(set(map(abs,d))) != 3:
            continue
        a = list(map(abs,d))
        if any(a[i] == sum(a[j] for j in range(3) if j != i) for i in range(3)):
            continue
        counted = sum(illuminated(v,d) for v in V)
        assert counted == predicted_count(d) and counted in (6,7), (d,counted)
        comparisons += 1
    print('EXACT_OK', 'vertices', len(V), 'orbit', len(full),
          'fractional_weight_aggregate', '48/14=24/7',
          'ordinary_cover', len(cover), 'generic_checks',comparisons)

if __name__ == '__main__':
    main()
