"""Finite stress test of the nontrivial imbalance-ratio part of the theorem.
Run with Python 3 standard library: python verify_ratio.py
"""
from math import comb
from verify_counts import part_step, phi


def count_basin(n, m):
    sizes = (n, n, m)
    total = 0
    for a in range(n + 1):
        for b in range(n + 1):
            for c in range(m + 1):
                x = (a, b, c)
                y = part_step(x, sizes)
                z = part_step(y, sizes)
                w = part_step(z, sizes)
                assert part_step(w, sizes) == z
                if z != w:
                    total += comb(n, a)*comb(n, b)*comb(m, c)
    return total


if __name__ == '__main__':
    for n in (2, 4, 8, 16, 32):
        m = 2 * n
        B = count_basin(n, m)
        print(f'n={n}: m={m}, oscillation_probability={B/2**(2*n+m):.12f}, limit={phi(2):.12f}')
