#!/usr/bin/env python3
"""Finite checks for ordered separation of cubic Boolean functions.

Only the mathematical classification proof, not these finite tests,
establishes the dimension-four obstruction for all functions.
"""
from itertools import combinations


def monomial_masks(n, degree):
    return [sum(1 << i for i in ids) for ids in combinations(range(n), degree)]


def values(n, monomials):
    return tuple(sum((x & m) == m for m in monomials) & 1 for x in range(1 << n))


def failing_ordered_pair(n, vals):
    count = 1 << n
    supports = [sum((vals[x ^ z] ^ vals[x] ^ vals[z]) << z
                    for z in range(count)) for x in range(count)]
    for x in range(1, count):
        for y in range(1, count):
            if x != y and (supports[x] & ~supports[y]) == 0:
                return (x, y)
    return None


def exhaustive_four():
    cubics = monomial_masks(4, 3)
    quadratics = monomial_masks(4, 2)
    total = 0
    for cubic_coeff in range(1, 1 << len(cubics)):
        cm = [m for i, m in enumerate(cubics) if cubic_coeff & (1 << i)]
        for quadratic_coeff in range(1 << len(quadratics)):
            qm = [m for i, m in enumerate(quadratics) if quadratic_coeff & (1 << i)]
            assert failing_ordered_pair(4, values(4, cm + qm)) is not None
            total += 1
    assert total == 15 * 64 == 960
    return total


def check_examples():
    examples = {
        3: [0b00111],
        5: [0b00111, 0b11000],
        6: [0b000111, 0b111000],
        7: [0b0000111, 0b0011000, 0b1100000],
        8: [0b00000111, 0b00011000, 0b11100000],
    }
    for n, mons in examples.items():
        assert failing_ordered_pair(n, values(n, mons)) is None, n
    return sorted(examples)


def check_quadratic_boundary():
    # In four dimensions symplectic *quadratic* functions do separate;
    # the degree-exactly-three hypothesis is essential.
    assert failing_ordered_pair(4, values(4, [0b0011, 0b1100])) is None


def check_nested_witnesses():
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                mons = [0b0111, 0b1001]
                if a: mons.append(0b0011)
                if b: mons.append(0b0101)
                if c: mons.append(0b0110)
                vals = values(4, mons)
                r = 0b1000
                x = 0b0010 | ((a ^ c) << 3)
                def row(u):
                    return sum((vals[u ^ z] ^ vals[u] ^ vals[z]) << z
                               for z in range(16))
                sr, sx = row(r), row(x)
                assert sr.bit_count() == 8
                if c == 0:
                    assert sx.bit_count() == 4 and (sx & ~sr) == 0
                else:
                    assert sx.bit_count() == 12 and (sr & ~sx) == 0
    assert all((values(4, [0b0111])[8 ^ z] ^ values(4, [0b0111])[8] ^ values(4, [0b0111])[z]) == 0
               for z in range(16))
    return 'WITNESS_OK'


if __name__ == '__main__':
    count = exhaustive_four()
    dims = check_examples()
    check_quadratic_boundary()
    print('VERIFY_OK', count, dims, check_nested_witnesses())
