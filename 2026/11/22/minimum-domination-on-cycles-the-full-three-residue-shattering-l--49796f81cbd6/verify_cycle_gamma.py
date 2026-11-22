#!/usr/bin/env python3
"""Independent finite checks of optimum-cycle domination trace theorem.
Only Python's standard library is required. All graphs are simple cycles.
The infinite theorem is proved separately; finite tests are corroborative.
"""
from itertools import combinations
from math import comb


def dominating(n, vertices):
    selected = set(vertices)
    return all(any(j in selected for j in ((i - 1) % n, i, (i + 1) % n))
               for i in range(n))


def min_solutions(n):
    k = (n + 2) // 3
    return [sum(1 << i for i in V)
            for V in combinations(range(n), k) if dominating(n, V)]


def predicted(n, S):
    s = len(S)
    k, mod = divmod(n, 3)
    if s == 0:
        return True
    if s == 1:
        return True
    if mod == 0:
        return False
    if mod == 2:
        if s != 2:
            return False
        a, b = S
        return sorted(((b - a) % 3, (n - b + a) % 3)) == [0, 2]
    if s == 2:
        return True
    if s == 3:
        a, b, c = S
        return sorted(((b - a) % 3, (c - b) % 3, (n - c + a) % 3)) == [0, 2, 2]
    return False


def closed_formula(n):
    k, r = divmod(n, 3)
    if r == 0:
        return [1, n]
    if r == 2:
        return [1, n, n * k]
    return [1, n, comb(n, 2), n * comb(k, 2)]


def check_lift(n, D, edge):
    old = [(edge + j) % n for j in range(n)]
    # The new circular order is old[0], a, b, c, old[1], ..., old[n-1].
    j = 0
    while not (D >> old[-j % n]) & 1:
        j += 1
        assert j < n
    assert j <= 2
    inserted_idx = 3 - j
    new_order = [old[0], 'a', 'b', 'c'] + old[1:]
    new_selection = [q for q, x in enumerate(new_order)
                     if isinstance(x, int) and ((D >> x) & 1)]
    new_selection.append(inserted_idx)
    assert len(new_selection) == (n + 2) // 3 + 1
    assert dominating(n + 3, new_selection)


def main():
    checked_supports = checked_lifts = 0
    for n in range(3, 23):
        solutions = min_solutions(n)
        assert solutions
        counts = []
        for s in range(5):
            count = 0
            for S in combinations(range(n), s):
                smask = sum(1 << v for v in S)
                traces = {D & smask for D in solutions}
                actual = len(traces) == (1 << s)
                expect = predicted(n, S)
                assert actual == expect, (n, S, actual, expect)
                if actual:
                    count += 1
                checked_supports += 1
            counts.append(count)
        formula = closed_formula(n)
        assert counts[:len(formula)] == formula, (n, counts, formula)
        assert all(c == 0 for c in counts[len(formula):]), (n, counts)
        if n <= 15:
            for D in solutions:
                for e in range(n):
                    check_lift(n, D, e)
                    checked_lifts += 1
    print('CYCLE_GAMMA_SHATTERING_VERIFIED',
          'orders=3..22', 'supports='+str(checked_supports),
          'edge_lifts='+str(checked_lifts))


if __name__ == '__main__':
    main()
