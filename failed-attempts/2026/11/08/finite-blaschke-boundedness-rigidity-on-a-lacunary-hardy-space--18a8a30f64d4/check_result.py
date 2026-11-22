"""Finite numerical diagnostics for the lacunary Hardy/Blaschke classification.

Requires Python 3 and NumPy. These diagnostics do not prove the
infinite-dimensional coefficient-decay or operator statements.
"""
import math
import numpy as np


def beta(n, q, gamma):
    if n == 0:
        return 1.0
    k = round(math.log(n, q))
    return (k + 1) ** (-gamma) if k >= 1 and q ** k == n else 1.0


def blaschke_on_circle(z, a, zeros_at_zero=0):
    return z ** zeros_at_zero * (z - a) / (1 - a * z)


def run():
    checks = 0
    for q in (3, 4, 5):
        for gamma in (0.75, 1.3):
            for j in range(4):
                d = q ** j
                for n in range(1, 600):
                    ratio = beta(d * n, q, gamma) / beta(n, q, gamma)
                    assert ratio <= 1 + 1e-11
                    checks += 1
            for d in (2, 6, 7, 10):
                if d in [q ** j for j in range(6)]:
                    continue
                for k in range(1, 7):
                    n = q ** k
                    ratio = beta(d * n, q, gamma) / beta(n, q, gamma)
                    assert abs(ratio - (k + 1) ** gamma) < 1e-9
                    checks += 1
    grid = 65536
    z = np.exp(2j * np.pi * np.arange(grid) / grid)
    for a in (0.23, 0.37):
        for p in (0, 1, 2):
            B = blaschke_on_circle(z, a, p)
            assert np.max(np.abs(np.abs(B) - 1)) < 5e-14
            checks += 1
            lacunary_masses = []
            for k in (2, 3, 4, 5):
                n = 3 ** k
                coeff = np.fft.fft(B ** n) / grid
                parseval = np.sum(np.abs(coeff) ** 2)
                assert abs(parseval - 1) < 5e-11
                indices = []
                m = 3
                while m < grid // 2:
                    indices.append(m)
                    m *= 3
                mass = float(np.sum(np.abs(coeff[indices]) ** 2))
                weighted_loss = sum((1 - (j + 1) ** (-1.3)) * abs(coeff[3 ** j]) ** 2
                                    for j in range(1, len(indices) + 1))
                assert 0 <= weighted_loss < 1 and 0 <= mass < 1
                normalized = math.sqrt(1 - weighted_loss)
                assert normalized <= 1 + 1e-12
                lacunary_masses.append(mass)
                checks += 5
            assert lacunary_masses[-1] < lacunary_masses[0]
            checks += 1
    print('PASS', checks, 'finite checks: exact monomial ratios and finite FFT diagnostics')


if __name__ == '__main__':
    run()
