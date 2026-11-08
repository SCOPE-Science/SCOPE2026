#!/usr/bin/env python3
"""Finite checks of the fifth Stirling-column residue theorem; not a proof."""
from math import factorial


def stirling_table(nmax: int, columns: int = 5):
    row = [1] + [0] * columns
    rows = []
    for n in range(nmax + 1):
        rows.append(row[:])
        row = [0] + [j * row[j] + row[j - 1] for j in range(1, columns + 1)]
    return rows


def odd_branch(n: int, k: int) -> int:
    """Integral 2-adic odd-power branch, evaluated at an ordinary exponent."""
    mod = 1 << k
    scale = 8 * mod
    numerator = (pow(5, n, scale) + 10 * pow(3, n, scale) + 5) % scale
    assert numerator % 8 == 0
    return (numerator // 8 * pow(15, -1, mod)) % mod


def main():
    levels = range(1, 13)
    max_n = max(max(5, k + 2) + 3 * (1 << (k + 1)) for k in levels)
    tab = stirling_table(max_n)
    direct_exp_checks = 0
    for n in range(5, 81):
        numerator = 5**n - 5 * 4**n + 10 * 3**n - 10 * 2**n + 5
        assert numerator % 120 == 0
        assert numerator // 120 == tab[n][5]
        direct_exp_checks += 1
    total_fibers = 0
    test_points = 0
    sharp_levels = 0
    for k in levels:
        mod, period = 1 << k, 1 << (k + 1)
        nmin = max(5, k + 2)
        for start in (nmin, nmin + 1, nmin + period):
            counts = [0] * mod
            for n in range(start, start + period):
                value = tab[n][5] % mod
                counts[value] += 1
                assert odd_branch(n, k) == value
                assert tab[n + period][5] % mod == value
                test_points += 1
            assert set(counts) == {2}, (k, start, sorted(set(counts)))
            total_fibers += len(counts)
        for parity in (0, 1):
            vals = [odd_branch(parity + 2 * t, k) for t in range(mod)]
            assert sorted(vals) == list(range(mod)), ('branch', parity, k)
        # No period smaller than 2^(k+1): binary-value pattern forbids odd periods;
        # any positive even shift < period disagrees on the corresponding parity chart.
        for d in (1, 2, period // 2, period - 1):
            if d and d < period:
                assert any(tab[n][5] % mod != tab[n + d][5] % mod
                           for n in range(nmin + period)), ('unexpected period', k, d)
        if k >= 4:
            n = k + 1
            assert n >= 5
            assert tab[n][5] % mod != tab[n + period][5] % mod
            sharp_levels += 1
    # First four fixed columns fail to have full support modulo 4 on their tails.
    for j in range(1, 5):
        vals = {tab[n][j] % 4 for n in range(20, 300)}
        assert vals != set(range(4)), (j, vals)
    print('VERIFY_OK levels=1..12 exact_fiber_counts=PASS both_parity_bijections=PASS '
          f'shift_checks={test_points} fiber_cells={total_fibers} '
          f'exponential_identity_checks={direct_exp_checks} '
          f'sharp_preperiod_checks={sharp_levels} lower_columns=PASS')


if __name__ == '__main__':
    main()
