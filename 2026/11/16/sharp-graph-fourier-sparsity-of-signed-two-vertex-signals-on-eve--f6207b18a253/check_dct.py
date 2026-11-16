"""Independent high-precision cosine-transform check; mpmath is required."""
from itertools import combinations
from mpmath import mp
from check_exact import exact_zeros


def main():
    mp.dps = 90
    cases = 0
    for n in range(2, 23):
        angles = [[mp.cos(mp.pi * k * (2 * j + 1) / (2 * n))
                   for j in range(n)] for k in range(n)]
        for u, v in combinations(range(n), 2):
            for sign in (-1, 1):
                support = sum(abs(angles[k][u] + sign * angles[k][v]) > mp.mpf('1e-65')
                              for k in range(n))
                assert support == n - exact_zeros(n, u, v, sign), (n, u, v, sign, support)
                cases += 1
    print('PASS: direct 90-digit DCT against exact congruences, n=2..22; cases=', cases)


if __name__ == '__main__':
    main()
