"""Reproduce general-position polynomial coefficients for triangular graphs.

Run: python3 verify_triangle_gp.py
Uses only the Python standard library.
"""
from collections import defaultdict
from itertools import combinations
from math import comb, factorial


def from_assembly(n):
    polynomials = [{0: 1}]
    for m in range(1, n + 1):
        result = defaultdict(int)
        for k in range(1, m + 1):
            if k == 1:
                blocks = {0: 1}
            elif k == 2:
                blocks = {1: 1}
            elif k == 3:
                blocks = {2: 3, 3: 1}
            else:
                blocks = {k - 1: k}
            for a, count in polynomials[m - k].items():
                for b, multiplicity in blocks.items():
                    result[a + b] += comb(m - 1, k - 1) * count * multiplicity
        polynomials.append(dict(result))
    return polynomials[n]


def from_geodesics(n):
    vertices = list(combinations(range(n), 2))
    size = len(vertices)
    distances = [[0 if i == j else 1 if set(u) & set(v) else 2
                  for j, v in enumerate(vertices)] for i, u in enumerate(vertices)]
    triples = [(i, j, k) for i, j, k in combinations(range(size), 3)
               if distances[i][k] == distances[i][j] + distances[j][k]
               or distances[i][j] == distances[i][k] + distances[k][j]
               or distances[j][k] == distances[j][i] + distances[i][k]]
    forbidden = [(1 << i) | (1 << j) | (1 << k) for i, j, k in triples]
    output = defaultdict(int)
    for subset in range(1 << size):
        if not any((subset & t) == t for t in forbidden):
            output[subset.bit_count()] += 1
    return dict(output)


def max_count(n):
    if n % 3 == 0:
        return factorial(n) // (6 ** (n // 3) * factorial(n // 3))
    total = 0
    for k in range(1, n + 1):
        if (n - k) % 3:
            continue
        r = (n - k) // 3
        a = 1 if k <= 2 else k
        total += factorial(n) * a // (factorial(k) * 6 ** r * factorial(r))
    return total



def maximal_from_assembly(n):
    polynomials = [{0: 1}]
    for m in range(1, n + 1):
        result = defaultdict(int)
        for k in range(2, m + 1):
            blocks = {1: 1} if k == 2 else {3: 1} if k == 3 else {k - 1: k}
            for a, count in polynomials[m - k].items():
                for b, multiplicity in blocks.items():
                    result[a + b] += comb(m - 1, k - 1) * count * multiplicity
        polynomials.append(dict(result))
    output = defaultdict(int, polynomials[n])
    if n % 3 == 1:
        r = (n - 1) // 3
        output[3 * r] += factorial(n) // (6 ** r * factorial(r))
    return dict(output)


def from_geodesics_maximal(n):
    vertices = list(combinations(range(n), 2))
    size = len(vertices)
    distances = [[0 if i == j else 1 if set(u) & set(v) else 2
                  for j, v in enumerate(vertices)] for i, u in enumerate(vertices)]
    forbidden = [(1 << i) | (1 << j) | (1 << k) for i, j, k in combinations(range(size), 3)
                 if distances[i][k] == distances[i][j] + distances[j][k]
                 or distances[i][j] == distances[i][k] + distances[k][j]
                 or distances[j][k] == distances[j][i] + distances[i][k]]
    valid = [not any((mask & triplet) == triplet for triplet in forbidden)
             for mask in range(1 << size)]
    output = defaultdict(int)
    for mask, ok in enumerate(valid):
        if ok and not any(valid[mask | (1 << i)] for i in range(size)
                          if not (mask & (1 << i))):
            output[mask.bit_count()] += 1
    return dict(output)


def lower_count(n):
    if n % 2 == 0:
        r = n // 2
        return factorial(n) // (2 ** r * factorial(r))
    r = (n - 3) // 2
    triangles = comb(n, 3) * factorial(n - 3) // (2 ** r * factorial(r))
    stars = 0
    if n >= 5:
        r = (n - 5) // 2
        stars = 5 * comb(n, 5) * factorial(n - 5) // (2 ** r * factorial(r))
    return triangles + stars


def main():
    for n in range(2, 7):
        a = from_assembly(n)
        b = from_geodesics(n)
        assert a == b, (n, a, b)
        print('geodesic-exhaustive', n, sorted(a.items()))
        c = maximal_from_assembly(n)
        d = from_geodesics_maximal(n)
        assert c == d, (n, c, d)
        print('maximal-geodesic-exhaustive', n, sorted(c.items()))
    for n in range(3, 16):
        a = from_assembly(n)
        d = n if n % 3 == 0 else n - 1
        assert max(a) == d
        assert a[d] == max_count(n)
        print('extremal-formula', n, d, max_count(n))
        maximal = maximal_from_assembly(n)
        lower = n // 2 if n % 2 == 0 else (n + 3) // 2
        assert min(maximal) == lower, (n, maximal)
        assert maximal[lower] == lower_count(n), (n, maximal, lower_count(n))
        print('lower-extremal-formula', n, lower, lower_count(n))
    print('PYTHON_VERIFICATION_OK')


if __name__ == '__main__':
    main()
