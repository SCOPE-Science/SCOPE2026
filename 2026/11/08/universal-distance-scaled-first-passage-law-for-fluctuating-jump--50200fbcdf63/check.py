"""Numerical consistency checks for a stable-clock first-passage limit.

Run with Python 3, SciPy and mpmath. Tests do not prove the limit theorem.
"""
import math
from scipy.integrate import quad
from mpmath import mp


def exact_survival(n, alpha, tau, v):
    """Mittag-Leffler refresh law: exact half-line spectral survival."""
    physical_time = (n ** (2 * alpha)) * v
    blocks = int(physical_time // tau)
    rest = physical_time - blocks * tau

    def integrand(theta):
        if theta == 0:
            return 2 * n
        energy = 2 * math.sin(theta / 2) ** 2
        spectral = math.sin(n * theta) / math.tan(theta / 2)
        return spectral * math.exp(-blocks * math.log1p((tau * energy) ** alpha)) / (
                           (1 + (rest * energy) ** alpha))

    pts = [j * math.pi / n for j in range(1, n)]
    return quad(integrand, 0, math.pi, points=pts,
                epsabs=1e-9, limit=2 * n)[0] / math.pi


def limit_survival(alpha, c, v):
    """Universal absolutely convergent sine-transform survival."""
    def integrand(k):
        sinc = math.sin(k) / k if k else 1.
        return sinc * math.exp(-c * v * (k * k / 2) ** alpha)
    upper = max(40., (250. / (c * v)) ** (1 / (2 * alpha)))
    return (2 / math.pi) * quad(integrand, 0, upper,
                                epsabs=1e-10, limit=800)[0]


def gamma_moment(alpha, c, q):
    return (c ** (-q) * 2 ** (-alpha * q) *
            mp.gamma(mp.mpf('0.5') - alpha * q) / mp.sqrt(mp.pi) *
            mp.gamma(1 + q) / mp.gamma(1 + alpha * q))


def check():
    tests = 0
    mp.dps = 60
    for raw in ['0.11', '0.2', '0.35', '0.49']:
        a = mp.mpf(raw)
        got = gamma_moment(a, mp.mpf('1'), 1)
        known = 2**a * mp.gamma(1-2*a) * mp.sin(mp.pi*a) / (mp.pi*a)
        assert mp.almosteq(got, known, rel_eps=mp.mpf('1e-50'))
        tests += 1

    for a in [0.3, 0.4, 0.7]:
        tau = 1.3
        c = tau ** (a - 1)
        for v in [0.5, 2.0]:
            target = limit_survival(a, c, v)
            coarse = exact_survival(16, a, tau, v)
            fine = exact_survival(256, a, tau, v)
            assert 0 < target < 1 and 0 < coarse < 1 and 0 < fine < 1
            assert abs(fine-target) < 0.007
            tests += 4
        values = [limit_survival(a, c, v) for v in [0.2, 0.5, 1, 2, 10]]
        assert all(0 < x < 1 for x in values)
        assert all(x > y for x, y in zip(values, values[1:]))
        tests += 2

    for a in [0.3, 0.4, 0.7]:
        c = 1.3
        beta = 1 / (2 * a)
        tail_coeff = (math.sqrt(2) * float(mp.gamma(beta)) /
                      (math.pi*a)) * c ** (-beta)
        v = 30.
        ratio = limit_survival(a, c, v) / (tail_coeff * v ** (-beta))
        assert abs(ratio - 1) < 0.04, (a, ratio)
        tests += 1
    print('PASS', tests, 'deterministic numerical and special-function checks')

if __name__ == '__main__':
    check()
