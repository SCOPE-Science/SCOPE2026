#!/usr/bin/env python3
"""Finite checks for prime-power-index multinomial Catalan integrality laws."""
from math import comb


def digit_sum(n, p):
    s = 0
    while n:
        s += n % p
        n //= p
    return s


def fact_valuation(n, p):
    v = 0
    while n:
        n //= p
        v += n
    return v


def digit_column_sums(n, p, r):
    sums = [0] * r
    i = 0
    while n:
        sums[i % r] += n % p
        n //= p
        i += 1
    return sums


def check(p, r, H):
    M = p**r - 1
    bound = p**H
    predicted = (comb(H // r + p - 2, p - 1)**(r - H % r)
                 * comb((H + r - 1) // r + p - 2, p - 1)**(H % r)) - 1
    count = 0
    for L in range(2, (bound - 1) // M + 1):
        K = M*L
        if not K < bound:
            continue
        v_actual = fact_valuation(K, p) - L * fact_valuation(M, p) - (L-1)*r
        v_digit = r - digit_sum(K, p)//(p-1)
        assert v_actual == v_digit and digit_sum(K, p) % (p-1) == 0
        col = digit_column_sums(K, p, r)
        accepted = v_actual >= 0
        assert accepted == (col == [p-1]*r), (p, r, H, L, v_actual, col)
        if accepted:
            assert v_actual == 0
            count += 1
    assert count == predicted, (p, r, H, count, predicted)
    return count


def main():
    cases = [(2,1,13), (2,2,12), (2,3,12), (2,4,12),
             (3,1,9), (3,2,9), (3,3,9),
             (5,1,6), (5,2,6), (7,1,5)]
    for p, r, H in cases:
        count = check(p, r, H)
        print(f'p={p}, r={r}, H={H}: {count} integral parameters; exact count confirmed')
    print('ALL TESTS PASSED')

if __name__ == '__main__':
    main()
