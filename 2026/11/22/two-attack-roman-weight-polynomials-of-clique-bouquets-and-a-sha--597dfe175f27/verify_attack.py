"""Check the weight polynomial for two-attack Roman functions on clique bouquets.
Run: python3 verify_attack.py
Uses only the Python standard library.
"""
from itertools import product
from math import comb


def plus(*terms):
    out = {}
    for term in terms:
        for e, c in term.items():
            out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}


def times(a, b):
    result = {}
    for i, u in a.items():
        for j, v in b.items():
            result[i + j] = result.get(i + j, 0) + u * v
    return {e: c for e, c in result.items() if c}


def product_polys(polys):
    out = {0: 1}
    for p in polys:
        out = times(out, p)
    return out


def power(a, n):
    return product_polys([a] * n)


def shift(p, delta):
    return {k + delta: v for k, v in p.items()}


def scale(p, factor):
    return {k: factor * v for k, v in p.items()}


def minus(p):
    return scale(p, -1)


def petal_polynomials(r):
    assert r >= 2
    all_labels = power({0: 1, 1: 1, 2: 1}, r)
    no_twos = power({0: 1, 1: 1}, r)
    # A: no zero at all, or at least one two.
    A = plus(all_labels, minus(no_twos), {r: 1})
    # D: one two, at least two zeros; the other vertices are ones.
    D = {}
    for zcount in range(2, r):
        w = 2 + r - 1 - zcount
        D[w] = D.get(w, 0) + r * comb(r - 1, zcount)
    # C: A with D excluded.
    C = plus(A, minus(D))
    B = {r - 1: r}  # one zero, all other vertices one, no two
    return A, B, C


def closed_formula(sizes):
    A, B, C = [], [], []
    for r in sizes:
        a, b, c = petal_polynomials(r)
        A.append(a)
        B.append(b)
        C.append(c)
    # Center 2; at most one weakly defended peripheral zero.
    center_two = shift(product_polys(A), 2)
    for i in range(len(sizes)):
        other = product_polys(A[:i] + A[i+1:])
        center_two = plus(center_two, shift(times(B[i], other), 2))
    # Center 1 or 0; latter excludes zero defenders and one bad pair.
    center_one = shift(product_polys(C), 1)
    center_zero = plus(product_polys(C), {
        sum(sizes): -1 - sum(r * (r - 1) for r in sizes)
    })
    return plus(center_two, center_one, center_zero)


def direct_enum(sizes):
    n = 1 + sum(sizes)
    masks = [0] * n
    offset = 1
    for r in sizes:
        for v in range(offset, offset + r):
            masks[v] |= 1
            masks[0] |= 1 << v
            for u in range(offset, offset + r):
                if u != v:
                    masks[v] |= 1 << u
        offset += r
    hist = {}
    for assignment in product(range(3), repeat=n):
        zeros = [v for v, d in enumerate(assignment) if d == 0]
        defenders = sum(1 << v for v, d in enumerate(assignment) if d == 2)
        if any(not (masks[v] & defenders) for v in zeros):
            continue
        if any(((masks[x] | masks[y]) & defenders).bit_count() < 2
               for j, x in enumerate(zeros) for y in zeros[j + 1:]):
            continue
        weight = sum(assignment)
        hist[weight] = hist.get(weight, 0) + 1
    return hist


def homogeneous_minimum(m, r):
    if r == 2:
        return 2 * m, 3**m - 2*m - 1
    if r == 3:
        return (2*m + 2, 63 if m == 2 else (m+1)*3**m)
    return 2*m+2, r**m


def main():
    cases = ((2, 2), (2, 3), (3, 3), (2, 2, 2),
             (2, 2, 3), (2, 3, 4), (3, 3, 3),
             (4, 4), (2, 5), (2, 2, 2, 3))
    total_assignments = 0
    for sizes in cases:
        actual = direct_enum(sizes)
        predicted = closed_formula(sizes)
        assert actual == predicted, (sizes, actual, predicted)
        if len(set(sizes)) == 1:
            m, r = len(sizes), sizes[0]
            weight, count = homogeneous_minimum(m, r)
            assert min(actual) == weight and actual[weight] == count
        total_assignments += 3**(1 + sum(sizes))
        print('CASE', sizes, 'MIN', min(actual),
              'MINCOUNT', actual[min(actual)],
              'TOTAL', sum(actual.values()))
    print('VERIFIED', len(cases), 'cases', total_assignments,
          'direct assignments, all polynomial coefficients')


if __name__ == '__main__':
    main()
