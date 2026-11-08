#!/usr/bin/env python3
"""Standalone checks for exact Nash counts on balanced complete multipartite graphs.

Uses only Python's standard library. Checks finite instances, not a substitute
for the general argument in RESULT.md.
"""
from itertools import product
from math import comb


def formula(r, n):
    total = sum(comb(r, h) for h in range(r + 1)
                if r - 1 <= 2 * h <= r + 1)
    if r % 2:
        total += r * comb(r - 1, (r - 1) // 2) * (2 ** n - 2)
    for t in range(2, r + 1):
        for h in range(r - t + 1):
            numerator = n * (r - 1 - 2 * h)
            denominator = 2 * (t - 1)
            if numerator % denominator:
                continue
            c = numerator // denominator
            if 0 < c < n:
                total += comb(r, t) * comb(r - t, h) * comb(n, c) ** t
    return total


def stable_macro(sizes, counts):
    total_one = sum(counts)
    for i, (n, x) in enumerate(zip(sizes, counts)):
        other_one = total_one - x
        degree = sum(sizes) - n
        if x > 0 and 2 * other_one > degree:
            return False
        if x < n and 2 * other_one < degree:
            return False
    return True


def cut_macro(sizes, counts):
    return sum(counts[i] * (sizes[j] - counts[j])
               + (sizes[i] - counts[i]) * counts[j]
               for i in range(len(sizes)) for j in range(i + 1, len(sizes)))


def check_macro(r, n):
    sizes = (n,) * r
    actual = 0
    welfare = {}
    for x in product(range(n + 1), repeat=r):
        if stable_macro(sizes, x):
            weight = 1
            for k in x:
                weight *= comb(n, k)
            actual += weight
            cut = cut_macro(sizes, x)
            welfare[cut] = welfare.get(cut, 0) + weight
    assert actual == formula(r, n), (r, n, actual, formula(r, n))
    if r == 3:
        b = comb(n, n // 2) ** 3 if n % 2 == 0 else 0
        assert actual == 6 * (2 ** n - 1) + b
        assert welfare.get(2 * n * n, 0) == 6 * (2 ** n - 1)
        assert (welfare.get(3 * n * n // 2, 0) if n % 2 == 0 else 0) == b
        assert len(welfare) == (2 if n % 2 == 0 else 1)
    return actual


def check_labeled(r, n):
    sizes = (n,) * r
    vertices = tuple(range(r * n))
    edges = tuple((a, b) for a in vertices for b in vertices
                  if a < b and a // n != b // n)
    actual = 0
    welfare = {}
    for bits in product((0, 1), repeat=r*n):
        stable = True
        for i in vertices:
            neighbors = [j for j in vertices if j // n != i // n]
            present = sum(bits[i] != bits[j] for j in neighbors)
            if 2 * present < len(neighbors):
                stable = False
                break
        if not stable:
            continue
        actual += 1
        cut = sum(bits[a] != bits[b] for a,b in edges)
        welfare[cut] = welfare.get(cut, 0) + 1
    assert actual == formula(r, n), (r, n, actual, formula(r, n))
    if r == 3:
        expected = {2*n*n: 6*(2**n-1)}
        if n % 2 == 0:
            expected[3*n*n//2] = comb(n,n//2)**3
        assert welfare == expected, (r,n,welfare,expected)
    return actual


def main():
    macro_tests = 0
    for r in range(2, 8):
        for n in range(1, 7):
            if (n + 1) ** r > 200000:
                continue
            check_macro(r, n)
            macro_tests += 1
    labeled_tests = 0
    for r in range(2, 7):
        for n in range(1, 7):
            if r*n > 14:
                continue
            check_labeled(r, n)
            labeled_tests += 1
    for n in range(1, 12):
        assert formula(3, n) == 6*(2**n-1)+(comb(n,n//2)**3 if n%2 == 0 else 0)
    print(f'VERIFY_OK macro_cases={macro_tests} labeled_cases={labeled_tests} tripartite_formula_cases=11')


if __name__ == '__main__':
    main()
