"""Independent numerical and algebraic checks for sharp critical Gabor bounds.

Uses only the Python standard library; no external files or packages.
"""
import cmath
import math
import random

TAU = 2.0 * math.pi
STAR_R = math.sqrt(2.0) - 1.0
STAR_KAPPA = 3.0 + 2.0 * math.sqrt(2.0)


def data(weights_heights, alpha=1.0):
    assert alpha > 0
    vals = [(float(weight), math.exp(-TAU * height / alpha))
            for weight, height in weights_heights]
    assert all(weight > 0 and 0.0 < r < 1.0 for weight, r in vals)
    lower_amp = sum(weight * r / (1.0 + r) for weight, r in vals)
    upper_amp = sum(weight / (1.0 - r) for weight, r in vals)
    return vals, lower_amp, upper_amp


def zak_amplitude(weights_heights, x, omega, alpha=1.0):
    """Absolute value of the Zak fiber (the phase is unimodular)."""
    vals, _, _ = data(weights_heights, alpha)
    return TAU / math.sqrt(alpha) * abs(sum(
        a * r ** omega / (1.0 - r * cmath.exp(TAU * 1j * x))
        for a, r in vals))


def exact_bounds(weights_heights, alpha=1.0):
    _, L, U = data(weights_heights, alpha)
    return (TAU * L / math.sqrt(alpha))**2, (TAU * U / math.sqrt(alpha))**2


def deficit(weights_heights, alpha=1.0):
    vals, L, U = data(weights_heights, alpha)
    return (U / L - STAR_KAPPA,
            STAR_KAPPA * sum(a * (r - STAR_R)**2 / (1.0 - r*r)
                             for a, r in vals) / L)


def direct_zak(weights_heights, x, omega, alpha=1.0, cutoff=25000):
    """Direct symmetric spatial sum at unit alpha (independent of frequency series)."""
    assert alpha == 1.0
    return sum(cmath.exp(-TAU * 1j * n * omega) *
               sum(a / (x + n + 1j * u) for a, u in weights_heights)
               for n in range(-cutoff, cutoff + 1))


def run():
    count = 0
    rnd = random.Random(260818)
    for _ in range(140):
        a = 10**rnd.uniform(-0.7, 0.6)
        mixture = [(10**rnd.uniform(-1.0, 0.5),
                    a * 10**rnd.uniform(-1.2, 0.4))
                   for _ in range(rnd.randint(1, 6))]
        A, B = exact_bounds(mixture, a)
        assert A > 0.0 and B > A
        for _ in range(18):
            x = rnd.random()
            omega = rnd.random()
            z = zak_amplitude(mixture, x, omega, a)**2
            assert A * (1.0 - 2e-13) <= z <= B * (1.0 + 2e-13)
            count += 1
        eps = 1e-8
        at_lower = zak_amplitude(mixture, 0.5, 1-eps, a)**2
        at_upper = zak_amplitude(mixture, 0.0, eps, a)**2
        assert abs(at_lower / A - 1.0) < 5e-6
        assert abs(at_upper / B - 1.0) < 5e-6
        d1, d2 = deficit(mixture, a)
        assert abs(d1-d2) < 1e-9 * (1 + abs(d1))
        assert d1 >= -3e-13
        count += 5
    for t in (0.17, 0.29, 0.54):
        for omega in (0.22, 0.41, 0.73):
            m = [(1.0, 0.27), (0.57, 0.72), (0.31, 1.4)]
            direct = direct_zak(m, t, omega, cutoff=12000)
            vals, _, _ = data(m)
            analytic = -TAU * 1j * cmath.exp(TAU*1j*omega*t) * sum(
                a * r**omega/(1-r*cmath.exp(TAU*1j*t)) for a, r in vals)
            assert abs(direct-analytic) < 2e-4
            count += 1
    optimal_u = math.log(1+math.sqrt(2.0))/TAU
    A, B = exact_bounds([(2.9, optimal_u)])
    assert abs(math.sqrt(B/A) - STAR_KAPPA) < 1e-12
    assert abs(deficit([(2.9, optimal_u)])[0]) < 1e-12
    count += 2
    print('PASS', count, 'checks; universal optimum', STAR_KAPPA,
          'and equality pole height at alpha=1', optimal_u)


if __name__ == '__main__':
    run()
