"""Independent finite cross-check of total two-rainbow domination on clique bouquets.

Run: python verify_total_rainbow_windmills.py
Requires only Python's standard library. Colors are bitmasks 0, 1, 2, 3.
"""
from collections import Counter
from itertools import product


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a): c[i] += v
    for i, v in enumerate(b): c[i] += v
    return c


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return c


def power(a, k):
    c = [1]
    for _ in range(k): c = multiply(c, a)
    return c


def monomial(coef, degree): return [0]*degree + [coef]


def local_B(m):
    return add(add(power([1, 2, 1], m), [-x for x in power([1, 1], m)]), monomial(1, m))


def local_D(m):
    if m == 1: return [0]
    c = add(power([1, 2, 1], m), [-2*x for x in power([1, 1], m)])
    c = add(c, [1])
    c = add(c, monomial(-m, 2))
    return add(c, monomial(2, m))


def derived_coefficients(blades):
    total = sum(blades)
    dual_center = [0, 0] + add(power([1, 1], 2*total), [-1])
    b = [1]; d = [1]
    for size in blades:
        b = multiply(b, local_B(size))
        d = multiply(d, local_D(size))
    single_center = [0] + [2*x for x in b]
    empty_center = add(d, monomial(-2, total)) if min(blades) >= 2 else [0]
    return add(add(dual_center, single_center), empty_center)


def direct_counts(blades):
    vertices = sum(blades) + 1
    adjacency = [set() for _ in range(vertices)]
    p = 1
    for size in blades:
        group = range(p, p+size)
        for v in group:
            adjacency[0].add(v)
            adjacency[v].add(0)
            for w in group:
                if v != w: adjacency[v].add(w)
        p += size
    result = Counter()
    for assignment in product((0, 1, 2, 3), repeat=vertices):
        for v in range(vertices):
            neighborhood_colors = 0
            for u in adjacency[v]:
                neighborhood_colors |= assignment[u]
            if assignment[v] == 0:
                if neighborhood_colors != 3: break
            elif neighborhood_colors == 0:
                break
        else:
            weight = sum(x.bit_count() for x in assignment)
            result[weight] += 1
    return [result[k] for k in range(2*vertices + 1)]


def compositions(n):
    if n == 0:
        yield ()
    for first in range(1, n+1):
        for rest in compositions(n-first):
            yield (first,) + rest


def main():
    cases = []
    for size in range(2, 8):
        cases += [c for c in compositions(size) if len(c) >= 2]
    cases += [(2,2,2), (3,3), (2,3,2), (1,2,2,2), (1,1,1,1,1,1,1,1), (3,2,2)]
    nassign = 0
    nvalid = 0
    for blades in cases:
        pred = derived_coefficients(blades)
        actual = direct_counts(blades)
        assert pred == actual, (blades, pred, actual)
        assert pred[0:3] == [0, 0, 0]
        n = sum(blades)
        b = lambda m: 2 if m == 1 else m
        expected_min = 2*n + (2*b(blades[0])*b(blades[1]) if len(blades) == 2 else 0)
        assert pred[3] == expected_min, (blades, pred[3], expected_min)
        assert all(x >= 0 for x in pred)
        nassign += 4**(n+1)
        nvalid += sum(actual)
    print(f'VERIFY_OK clique_bouquets={len(cases)} labelings_examined={nassign} '
          f'feasible_labelings={nvalid} full_polynomials=PASS minimum_multiplicities=PASS')


if __name__ == '__main__':
    main()
