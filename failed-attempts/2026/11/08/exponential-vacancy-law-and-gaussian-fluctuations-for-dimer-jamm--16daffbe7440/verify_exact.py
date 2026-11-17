#!/usr/bin/env python3
"""Exact finite-state checks for edge-uniform dimer adsorption on complete split graphs."""
from fractions import Fraction
from functools import lru_cache


def add_scaled(out, inp, multiplier):
    for k, v in inp.items():
        out[k] = out.get(k, Fraction(0)) + multiplier * v


@lru_cache(None)
def reduced_distribution(a, b):
    if a == 0:
        return {b: Fraction(1)}
    if a == 1:
        return {b - 1 if b else 0: Fraction(1)}
    denom = a - 1 + 2 * b
    out = {}
    add_scaled(out, reduced_distribution(a - 2, b), Fraction(a - 1, denom))
    if b:
        add_scaled(out, reduced_distribution(a - 1, b - 1), Fraction(2 * b, denom))
    return out


def labelled_distribution(a, b):
    edges = [(i, j) for i in range(a) for j in range(i + 1, a)]
    edges += [(i, j) for i in range(a) for j in range(a, a + b)]
    edge_masks = [(1 << i) | (1 << j) for i, j in edges]
    initial = (1 << (a + b)) - 1
    independent_mask = ((1 << b) - 1) << a

    @lru_cache(None)
    def walk(mask):
        available = [edge for edge in edge_masks if mask & edge == edge]
        if not available:
            return {(mask & independent_mask).bit_count(): Fraction(1)}
        out = {}
        for edge in available:
            add_scaled(out, walk(mask ^ edge), Fraction(1, len(available)))
        return out

    return walk(initial)


def main():
    checks = 0
    for a in range(7):
        for b in range(7):
            r = reduced_distribution(a, b)
            assert sum(r.values()) == 1 and all(v > 0 for v in r.values())
            assert r == labelled_distribution(a, b), (a, b, r, labelled_distribution(a, b))
            checks += 1
    assert reduced_distribution(4, 4) == {
        0: Fraction(24, 55), 2: Fraction(8, 15), 4: Fraction(1, 33)
    }
    for n in range(1, 8):
        P = reduced_distribution(n, n)
        mean = sum(k * v for k, v in P.items())
        print(f'n={n}: exact mean vacancies={mean}, perfect probability={P.get(0, Fraction(0))}')
    print(f'PASS: {checks} separate exact finite distributions compared against labeled-state recursion')


if __name__ == '__main__':
    main()
