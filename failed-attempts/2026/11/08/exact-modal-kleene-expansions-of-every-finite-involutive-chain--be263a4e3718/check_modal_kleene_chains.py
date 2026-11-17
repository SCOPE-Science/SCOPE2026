#!/usr/bin/env python3
"""Independent finite check of modal Kleene operators on involutive chains.

Runs all nondecreasing unary tables on each chain, tests the three
original modal identities directly, and compares four closed formulas.
Only standard-library modules are used.
"""
from itertools import combinations_with_replacement
from math import comb


def predicted(n):
    assert n >= 2
    h = n // 2
    exceptional = comb(2 * h, h + 1)
    if n % 2 == 0:
        bulk = comb(2 * h - 1, h) ** 2
        normal = comb(2 * h - 1, h) * (comb(2 * h - 2, h - 1) + 1)
        return bulk + exceptional, normal, None, bulk, exceptional
    bulk = comb(2 * h, h) ** 2
    normal = comb(2 * h, h) * comb(2 * h - 1, h - 1) + comb(2 * h - 1, h)
    return bulk + exceptional, normal, bulk, bulk, exceptional


def valid_original_axioms(table):
    n = len(table)
    neg = lambda x: n - 1 - x
    meet = min
    join = max
    # (MK) -- meet preservation (not assumed in the test).
    for x in range(n):
        for y in range(n):
            if table[meet(x, y)] != meet(table[x], table[y]):
                return False
    # (Pos)
    for z in range(n):
        a = table[join(z, neg(z))]
        if neg(a) > a:
            return False
    # (Con)
    for x in range(n):
        for z in range(n):
            t = table[join(x, meet(z, neg(z)))]
            if t > join(table[x], neg(t)):
                return False
    return True


def structural_criterion(table):
    n = len(table)
    ell = (n - 1) // 2
    u = n - 1 - ell
    return (all(table[i] <= table[i + 1] for i in range(n - 1))
            and table[u] >= u
            and (table[ell] <= ell or all(table[x] == table[ell] for x in range(ell + 1))))


def verify(up_to=9):
    for n in range(2, up_to + 1):
        totals = [0, 0, 0, 0, 0]
        for table in combinations_with_replacement(range(n), n):
            direct = valid_original_axioms(table)
            structural = structural_criterion(table)
            assert direct == structural, (n, table, direct, structural)
            if direct:
                totals[0] += 1
                totals[1] += int(table[-1] == n - 1)
                if n % 2:
                    totals[2] += int(table[n // 2] == n // 2)
                ell = (n - 1) // 2
                is_bulk = table[ell] <= ell
                totals[3] += int(is_bulk)
                totals[4] += int(not is_bulk)
        expected = predicted(n)
        for i in (0, 1, 3, 4):
            assert totals[i] == expected[i], (n, i, totals, expected)
        if n % 2:
            assert totals[2] == expected[2], (n, totals, expected)
        print(f'n={n} all={totals[0]} normal={totals[1]} '
              f'center={totals[2] if n%2 else "not-applicable"} '
              f'bulk={totals[3]} exceptional={totals[4]} PASS')
    print('All direct-axiom / structural-normal-form / binomial-census checks PASS.')


if __name__ == '__main__':
    verify()
