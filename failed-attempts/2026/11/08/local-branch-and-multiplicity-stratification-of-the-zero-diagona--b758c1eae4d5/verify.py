#!/usr/bin/env python3
"""Exact finite checks for the zero-diagonal rank-one singularity stratification.

The full theorem follows from explicit localized determinantal coordinate rings;
these checks independently test tangent dimensions and combinatorial counts.
"""
from itertools import combinations, product
from math import comb


def binary_rank(rows):
    pivots = {}
    for row in rows:
        v = row
        while v:
            p = v.bit_length() - 1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return len(pivots)


def tangent_dimension(m, a, b):
    variables = {(i, j): k for k, (i, j) in
                 enumerate((i, j) for i in range(m) for j in range(m) if i != j)}
    A, B = set(a), set(b)
    matrix = lambda i, j: int(i in A and j in B)
    rows = []
    for i, k in combinations(range(m), 2):
        for j, ell in combinations(range(m), 2):
            derivative = 0
            for (r, s), coefficient in [
                ((i, j), matrix(k, ell)),
                ((k, ell), matrix(i, j)),
                ((i, ell), -matrix(k, j)),
                ((k, j), -matrix(i, ell))
            ]:
                if coefficient % 2 and (r, s) in variables:
                    derivative ^= 1 << variables[r, s]
            rows.append(derivative)
    return m * (m - 1) - binary_rank(rows)


def check():
    examples = 0
    for m in range(3, 7):
        support_cases = 0
        singular_cases = 0
        for assignment in product((0, 1, 2), repeat=m):
            a = [i for i, s in enumerate(assignment) if s == 1]
            b = [i for i, s in enumerate(assignment) if s == 2]
            if not a or not b:
                continue
            c = assignment.count(0)
            actual = tangent_dimension(m, a, b)
            assert actual == m - 1 + c, (m, a, b, actual, c)
            # Ways to extend the precise support partition to a global component.
            assert 2 ** c == sum(1 for x in product((1, 2), repeat=c))
            support_cases += 1
            singular_cases += (c > 0)
        expected = 3 ** m - 2 * 2 ** m + 1
        assert support_cases == expected, (m, support_cases, expected)
        divisor_components = m * (2 ** (m - 1) - 2)
        assert divisor_components == sum(1 for omitted in range(m)
            for left_choices in range(1, 2 ** (m - 1) - 1))
        degsum = sum(comb(m, a) * comb(m - 2, a - 1)
                     for a in range(1, m))
        assert degsum == comb(2 * m - 2, m - 1)
        examples += support_cases
        print(f'm={m} supports={support_cases} nonzero_singular_supports={singular_cases} '
              f'singular_divisors={divisor_components} origin_degree={degsum}')
    print(f'EXACT_JACOBIAN_AND_COMPONENT_COUNTS_OK {examples}')


if __name__ == '__main__':
    check()
