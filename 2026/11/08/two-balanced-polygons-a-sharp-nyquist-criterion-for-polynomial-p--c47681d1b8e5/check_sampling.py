"""Numerical corroboration for balanced two-orbit polynomial phase retrieval.

Runs without external dependencies. The all-degree proof is analytical;
these finite tests check the Fourier recovery identity and sharp aliases.
"""
import cmath
import math
import random


def power_sum(coefficients, z):
    out = 0j
    for c in reversed(coefficients):
        out = out * z + c
    return out


def recover_profile(samples, rho, phi, d):
    """Return Fourier coefficients c_0,...,c_{d-1}, Nyquist real datum."""
    mcount = 2 * d
    theta = [phi + math.pi * k / d for k in range(mcount)]
    lower = [sum(samples[k] * cmath.exp(-1j * m * theta[k])
                 for k in range(mcount)) / mcount for m in range(d)]
    top = sum(((-1) ** k) * samples[k] for k in range(mcount)) / mcount
    return lower, top


def coeff_at_circle(a, rho, m):
    d = len(a) - 1
    return sum(a[j + m] * a[j].conjugate() * rho ** (2 * j + m)
               for j in range(d - m + 1))


def main():
    rng = random.Random(9185)
    checks = 0
    for d in range(1, 14):
        r, R = 0.7, 1.1
        phi = math.pi / (2 * d)
        for _ in range(16):
            a = [complex(rng.uniform(-0.4, 0.4), rng.uniform(-0.4, 0.4))
                 for _ in range(d + 1)]
            ys = []
            low = []
            tops = []
            for rad, offset in [(r, 0.0), (R, phi)]:
                y = [abs(power_sum(a, rad * cmath.exp(1j * (offset + math.pi * k / d)))) ** 2
                     for k in range(2 * d)]
                ys.append(y)
                c, nyq = recover_profile(y, rad, offset, d)
                low.append(c)
                tops.append(nyq)
                for m in range(d):
                    expected = coeff_at_circle(a, rad, m)
                    assert abs(c[m] - expected) < 3e-9 * (1 + abs(expected))
                    checks += 1
            C = complex(tops[0] / (2 * r ** d),
                        -tops[1] / (2 * R ** d))
            expectedC = a[d] * a[0].conjugate()
            assert abs(C - expectedC) < 3e-9 * (1 + abs(expectedC))
            checks += 1
            for rad, c in [(r, low[0]), (R, low[1])]:
                for th in [0.12, 0.57, 1.31, 2.2]:
                    reconstructed = c[0].real + 2 * sum(
                        (c[m] * cmath.exp(1j * m * th)).real for m in range(1, d))
                    reconstructed += 2 * (rad ** d * C * cmath.exp(1j * d * th)).real
                    exact = abs(power_sum(a, rad * cmath.exp(1j * th))) ** 2
                    assert abs(reconstructed - exact) < 3e-8 * (1 + exact)
                    checks += 1
        # Angular resonance: both orbits give purely real powers z^d.
        for k in range(2 * d):
            for rad, offset in [(r, 0.0), (R, math.pi / d)]:
                z = rad * cmath.exp(1j * (offset + math.pi * k / d))
                assert abs(abs(1 + 1j * z ** d) ** 2 -
                           abs(1 - 1j * z ** d) ** 2) < 2e-7
                checks += 1
    print('BALANCED_POLYGON_PHASE_CHECKS_PASS', checks)


if __name__ == '__main__':
    main()
