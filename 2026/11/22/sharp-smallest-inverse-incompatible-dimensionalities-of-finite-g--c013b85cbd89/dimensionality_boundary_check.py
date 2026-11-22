"""Exhaustive finite certificate for the minimal inverse-unstable group dimensionalities.

Public mathematical code: standard Python 3, no external modules. Run:
    python3 dimensionality_boundary_check.py
"""
from itertools import permutations
from math import prod


def partitions_with_identity_singleton(n):
    """Each partition with {0} a block, exactly once, as restricted-growth labels."""
    if n == 1:
        yield (0,)
        return
    labels = [0, 1] + [0] * (n - 2)

    def rec(i, top):
        if i == n:
            yield tuple(labels)
            return
        for c in range(1, top + 2):
            labels[i] = c
            yield from rec(i + 1, max(top, c))

    yield from rec(2, 1)


def cyclic_table(n):
    return [[(a + b) % n for b in range(n)] for a in range(n)]


def product_table(factors):
    elems = list(__import__('itertools').product(*(range(d) for d in factors)))
    idx = {x: i for i, x in enumerate(elems)}
    return [[idx[tuple((a[k]+b[k]) % factors[k] for k in range(len(factors)))]
             for b in elems] for a in elems]


def symmetric_three_table():
    elements = list(permutations(range(3)))
    identity = (0, 1, 2)
    elements.remove(identity)
    elements.insert(0, identity)
    idx = {p: i for i, p in enumerate(elements)}
    return [[idx[tuple(a[b[k]] for k in range(3))] for b in elements]
            for a in elements], elements


def inverse_table(mul):
    n = len(mul)
    return [next(j for j in range(n) if mul[i][j] == 0 and mul[j][i] == 0)
            for i in range(n)]


def classes_of(labels):
    classes = [[] for _ in range(max(labels) + 1)]
    for elem, col in enumerate(labels):
        classes[col].append(elem)
    return classes


def is_dimensionality(labels, mul):
    """Setwise block products are unions of whole blocks (Jenča's D2)."""
    classes = classes_of(labels)
    for A in classes:
        for B in classes:
            products = {mul[a][b] for a in A for b in B}
            for x in products:
                if any(y not in products for y in classes[labels[x]]):
                    return False
    return True


def direct_D2_check(labels, mul):
    """Independent quantifier check: for ab in [c], find a'~a,b'~b,a'b'=c."""
    classes = classes_of(labels)
    for a in range(len(labels)):
        for b in range(len(labels)):
            col = labels[mul[a][b]]
            for c in classes[col]:
                if not any(mul[x][y] == c
                           for x in classes[labels[a]]
                           for y in classes[labels[b]]):
                    return False
    return True


def inverse_stable(labels, inv):
    return all(labels[inv[a]] == labels[inv[b]]
               for a in range(len(inv)) for b in range(len(inv))
               if labels[a] == labels[b])


def census(label, mul, check_direct=True):
    n = len(mul)
    assert all(mul[0][j] == j and mul[j][0] == j for j in range(n))
    inv = inverse_table(mul)
    count = 0
    failures = []
    for p in partitions_with_identity_singleton(n):
        if is_dimensionality(p, mul):
            if check_direct:
                assert direct_D2_check(p, mul), (label, p)
            count += 1
            if not inverse_stable(p, inv):
                failures.append(p)
    print(f'{label}: dimensionalities={count}, inverse-unstable={len(failures)}', flush=True)
    return count, failures


def block_sets(p):
    return tuple(tuple(i for i, c in enumerate(p) if c == color)
                 for color in range(max(p) + 1))


def hyperproducts(mul, p):
    C = block_sets(p)
    return [[tuple(sorted({p[mul[a][b]] for a in A for b in B}))
             for B in C] for A in C]


def main():
    # Every finite abelian group of order < 12 belongs to this list,
    # except elementary 2-groups, whose inverses are all themselves.
    for n in range(1, 12):
        count, failures = census(f'C{n}', cyclic_table(n), check_direct=(n >= 9))
        assert not failures
    for F in [(2, 2), (4, 2), (2, 2, 2), (3, 3)]:
        _, failures = census('x'.join(f'C{d}' for d in F), product_table(F))
        assert not failures

    S3, elts = symmetric_three_table()
    count6, bad6 = census('S3', S3)
    assert (count6, len(bad6)) == (22, 12)
    # The following 3-block example is explicit and its full class table is checked.
    pS3 = (0, 1, 1, 1, 2, 2)
    assert pS3 in bad6
    print('S3 witness classes:', block_sets(pS3))
    print('S3 quotient hyperproduct:', hyperproducts(S3, pS3))
    assert hyperproducts(S3, pS3) == [
        [(0,), (1,), (2,)],
        [(1,), (0, 1, 2), (0, 1, 2)],
        [(2,), (0, 1, 2), (0, 1)]
    ]

    count12, bad12 = census('C12', cyclic_table(12))
    assert (count12, len(bad12)) == (44, 4)
    pC12 = (0, 1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2)
    assert pC12 in bad12
    print('C12 witness classes:', block_sets(pC12))
    print('C12 quotient hyperproduct:', hyperproducts(cyclic_table(12), pC12))
    assert hyperproducts(cyclic_table(12), pC12) == [
        [(0,), (1,), (2,)],
        [(1,), (0, 1, 2), (0, 1, 2)],
        [(2,), (0, 1, 2), (1, 2)]
    ]
    # Four defective partitions: one orbit under multiplication by units mod 12.
    units = (1, 5, 7, 11)
    C = [frozenset(x) for x in block_sets(pC12)]
    images = {
        frozenset(frozenset((u * x) % 12 for x in block) for block in C)
        for u in units
    }
    expected = {
        frozenset(frozenset(x) for x in block_sets(p)) for p in bad12
    }
    assert images == expected
    print('C12 exceptional partitions: 4, one Aut(C12)-orbit')
    # In each witness the class 1 has two distinct inverse candidates,
    # because the identity is in both products (1,1) and (1,2).
    for p, table in [(pS3, S3), (pC12, cyclic_table(12))]:
        h = hyperproducts(table, p)
        assert 0 in h[1][1] and 0 in h[1][2]
    print('DIMENSIONALITY_BOUNDARY_OK')


if __name__ == '__main__':
    main()
