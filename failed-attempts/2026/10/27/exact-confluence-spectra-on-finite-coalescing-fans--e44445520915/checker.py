"""Exact finite test of bilateral modal confluence on an antichain with a top.

Run: python3 checker.py
Requires only the Python standard library.
The finite census is a check, not a proof of formulas for unbounded size.
"""
from itertools import product
from math import comb


def confluence(rows, m):
    """Literal existential checks of (40) and (41), order a_i<t."""
    n = m + 1
    t = m

    def leq(x, y):
        return x == y or (x < m and y == t)

    for x in range(n):
        for y in range(n):
            if not leq(x, y):
                continue
            for z in range(n):
                if rows[y] & (1 << z):
                    if not any((rows[x] & (1 << w)) and leq(w, z)
                               for w in range(n)):
                        return False
                if rows[x] & (1 << z):
                    if not any((rows[y] & (1 << w)) and leq(z, w)
                               for w in range(n)):
                        return False
    return True


def normal_form(rows, m):
    """Independent bitmask implementation of the claimed classification."""
    t_bit = 1 << m
    upper = rows[m]
    leaves = upper & (t_bit - 1)
    if not upper & t_bit:
        return all(row == leaves for row in rows[:m])
    if leaves:
        return all(row & leaves == leaves for row in rows[:m])
    return all(row != 0 for row in rows[:m])


def is_reflexive(rows):
    return all(row & (1 << i) for i, row in enumerate(rows))


def all_count(m):
    u = 1 << (m + 1)
    return 2**m + (u - 1)**m + (u + 2)**m - u**m


def refined_count(m):
    """Independent finite sum over the top row; also checks closed form."""
    u = 1 << (m + 1)
    total = 1 << m  # all top-free rows, including the all-empty relation
    for k in range(m + 1):
        rows = (u - 1) if k == 0 else (1 << (m + 1 - k))
        total += comb(m, k) * rows**m
    return total


def reflexive_count(m):
    return (2**m + 2)**m


def check_small(m):
    n = m + 1
    options = 1 << n
    counts_by_top = [0] * options
    total = 0
    reflexive = 0
    predicates_tested = 0
    for rows in product(range(options), repeat=n):
        literal = confluence(rows, m)
        predicted = normal_form(rows, m)
        predicates_tested += 1
        if literal != predicted:
            raise AssertionError(('normal-form mismatch', m, rows))
        if literal:
            total += 1
            reflexive += bool(is_reflexive(rows))
            counts_by_top[rows[m]] += 1
    assert total == all_count(m) == refined_count(m)
    assert reflexive == reflexive_count(m)
    top_bit = 1 << m
    assert counts_by_top[top_bit] == (options - 1)**m
    for top_row, observed in enumerate(counts_by_top):
        k = (top_row & (top_bit - 1)).bit_count()
        if not (top_row & top_bit):
            expected = 1
        else:
            expected = ((options - 1) if k == 0 else (1 << (m + 1 - k)))**m
        assert observed == expected, (m, top_row, observed, expected)
    print(f'm={m}: checked={predicates_tested}, all={total}, reflexive={reflexive}')


if __name__ == '__main__':
    for m in range(1, 4):
        check_small(m)
    for m in range(1, 31):
        assert all_count(m) == refined_count(m)
    print('VERIFY_OK')
