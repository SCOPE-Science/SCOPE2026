"""No-jump dynamics checks on hypercubes with unequal positive shell rates.

Run: python verify_dynamics.py
Requires numpy, scipy. Matrix exponentials are sampled, never used as proof
of an infinite-time limit. The analytic semigroup argument proves the limit.
"""
import math
import numpy as np
from scipy.linalg import expm


def shell2_expected(n):
    s = math.isqrt(n)
    if s*s != n:
        return 0.0
    return 2 * math.comb(n, (n-s)//2) / (2**n)


def main():
    checked = 0
    for n in range(2, 7):
        N = 1 << n
        A = np.zeros((N, N), dtype=complex)
        for x in range(N):
            for bit in range(n):
                A[x, x ^ (1 << bit)] = 1.0
        assert np.array_equal(A, A.conj().T)
        start = np.zeros(N, dtype=complex)
        start[0] = 1
        for trial in range(3):
            random = np.random.default_rng(9000 + 10*n + trial)
            gamma = np.zeros(N, dtype=float)
            for x in range(N):
                if x.bit_count() == 2:
                    gamma[x] = 0.5 + 0.5*random.random()
            J = (-1 if trial % 2 else 1) * (0.7 + trial * 0.2)
            generator = -1j * J * A - np.diag(gamma)/2
            short = float(np.linalg.norm(expm(50 * generator) @ start)**2)
            long = float(np.linalg.norm(expm(3000 * generator) @ start)**2)
            expected = shell2_expected(n)
            assert short + 1e-8 >= long, (n, trial, short, long)
            assert expected - 1e-7 <= long < expected + 1e-6, (n,trial,expected,long)
            checked += 1
    print(f'PASS: {checked} nonuniform-loss dynamics checks; near-limit norms '
          'agree with the exact square-dimensional prediction')


if __name__ == '__main__':
    main()
