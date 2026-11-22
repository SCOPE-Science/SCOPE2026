"""Exact finite checks for the regular-cross-polytope orthogonal-kernel theorem.

Run with Python 3: python CHECKER.py
The all-dimensional claims are proved analytically in RESULT.md; these bounded
calculations check identities and catch convention/indexing mistakes.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, factorial
from random import Random


def rank(rows, d):
    a = [[F(x) for x in row] for row in rows]
    pivot = 0
    for col in range(d):
        for i in range(pivot, len(a)):
            if a[i][col]:
                a[pivot], a[i] = a[i], a[pivot]
                break
        else:
            continue
        v = a[pivot][col]
        for j in range(col, d):
            a[pivot][j] /= v
        for i in range(pivot + 1, len(a)):
            v = a[i][col]
            if v:
                for j in range(col, d):
                    a[i][j] -= v * a[pivot][j]
        pivot += 1
        if pivot == d:
            break
    return pivot


def inequalities(d):
    a = d - 2
    return [tuple(s[i] + (a * s[j] if i == j else 0)
                  for i in range(d))
            for s in product((-1, 1), repeat=d) for j in range(d)]


def candidate_vertices(d):
    a = d - 2
    return [tuple(F(v, a + sum(t != 0 for t in s)) for v in s)
            for s in product((-1, 0, 1), repeat=d)
            if any(s)]


def projection_relints(d, b):
    """Directly check ALL nonempty proper faces via barycentric projection."""
    for m in range(1, d + 1):
        for S in combinations(range(d), m):
            for signs in product((-1, 1), repeat=m):
                t = sum(F(signs[r]) * b[S[r]] for r in range(m))
                for r, i in enumerate(S):
                    if F(signs[r]) * b[i] + (1 - t) / m <= 0:
                        return False
    return True


def main():
    vertex_cases = 0
    halfspace_checks = 0
    random_cases = 0
    inequality_count_checks = 0
    random = Random(20261117)
    for d in range(3, 7):
        hs = inequalities(d)
        candidates = candidate_vertices(d)
        assert len(candidates) == 3**d - 1
        assert len(hs) == d * 2**d
        assert len(set(hs)) == len(hs)
        for v in candidates:
            values = [sum(a*b for a, b in zip(h, v)) for h in hs]
            assert max(values) == 1
            tight = [h for h, q in zip(hs, values) if q == 1]
            assert rank(tight, d) == d
            vertex_cases += 1
            halfspace_checks += len(hs)
        a = d - 2
        v_closed = F(2**d * factorial(d-2), factorial(2*d-2))
        assert v_closed == F(2**d, 1) / F(factorial(2*d-2), factorial(d-2))
        assert v_closed / F(2**d, factorial(d)) == F(1, comb(2*d-2, d))
        inequality_count_checks += 3
        for _ in range(160):
            b = tuple(F(random.randint(-10, 10), 20) for _ in range(d))
            cond = sum(map(abs, b)) + a * max(map(abs, b)) < 1
            direct = (sum(map(abs, b)) < 1) and projection_relints(d, b)
            assert cond == direct, (d, b, cond, direct)
            random_cases += 1
        print(f'd={d}: {len(candidates)} vertices; {len(hs)} facet normals;'
              f' volume={v_closed}; ratio=1/{comb(2*d-2,d)};'
              ' projected-face test passed')
    print('PASS:', vertex_cases, 'candidate vertices', halfspace_checks,
          'halfspace evaluations,', random_cases, 'all-face projection tests,',
          inequality_count_checks, 'closed-form identities')

if __name__ == '__main__':
    main()
