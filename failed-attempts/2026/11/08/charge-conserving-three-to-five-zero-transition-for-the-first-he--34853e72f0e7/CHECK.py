"""Independent finite checks for the exact two-tone first-Hermite STFT theorem.

Run: python CHECK.py (Python 3 standard library only).
All-parameter completeness and critical local index rely on the analytic proof.
"""
import cmath
import math


def bisect_root(fun, lo, hi):
    flo, fhi = fun(lo), fun(hi)
    assert flo * fhi < 0, (lo, hi, flo, fhi)
    for _ in range(90):
        mid = (lo + hi) / 2
        if mid == lo or mid == hi:
            break
        fmid = fun(mid)
        if flo * fmid <= 0:
            hi = mid
        else:
            lo, flo = mid, fmid
    return (lo + hi) / 2


def locations(c):
    inner = (bisect_root(lambda u: math.atanh(u) / u - c, 1e-5, 1-1e-12)
             if c > 1 else None)
    outside = bisect_root(lambda u: math.atanh(1 / u) / u - c,
                          1 + 1e-10, 2 / math.sqrt(c) + 2)
    return inner, outside


def reduced(t, x, sigma, omega):
    a = (x - omega) * math.exp(-sigma ** 2 * (x - omega) ** 2 / 2)
    b = (x + omega) * math.exp(-sigma ** 2 * (x + omega) ** 2 / 2)
    return a * cmath.exp(2j * omega * t) + b


def exact(t, x, sigma, omega):
    prefactor = -1j * math.sqrt(2 * math.pi) * sigma ** 3
    return prefactor * cmath.exp(-1j * (x + omega) * t) * reduced(t, x, sigma, omega)


def original_integral(t, x, sigma, omega):
    # Composite Simpson quadrature over a twelve-sigma Gaussian-tail cutoff.
    n = 4800  # even
    low, high = t - 12 * sigma, t + 12 * sigma
    step = (high - low) / n

    def integrand(s):
        return (2 * math.cos(omega * s) * (s - t)
                * math.exp(-((s - t) / sigma) ** 2 / 2)
                * cmath.exp(-1j * x * s))

    acc = integrand(low) + integrand(high)
    for j in range(1, n):
        acc += (4 if j % 2 else 2) * integrand(low + j * step)
    return acc * step / 3


def winding_sign(t, x, sigma, omega):
    h = 1e-5
    d_t = (reduced(t + h, x, sigma, omega)
           - reduced(t - h, x, sigma, omega)) / (2 * h)
    d_x = (reduced(t, x + h, sigma, omega)
           - reduced(t, x - h, sigma, omega)) / (2 * h)
    det = (d_t.conjugate() * d_x).imag
    assert abs(det) > 1e-8
    return 1 if det > 0 else -1


for c in (0.25, 0.7, 0.99, 1, 1.01, 1.3, 2, 5):
    sigma, omega = math.sqrt(c), 1
    inner, outer = locations(c)
    roots = [(0, 0), (math.pi / 2, -outer), (math.pi / 2, outer)]
    if inner is not None:
        roots.extend([(0, -inner), (0, inner)])
    for t, x in roots:
        assert abs(reduced(t, x, sigma, omega)) < 2e-10, (c, t, x)
    if c != 1:
        expected = [1, -1, -1] if c < 1 else [-1, -1, -1, 1, 1]
        actual = [winding_sign(t, x, sigma, omega) for t, x in roots]
        assert actual == expected, (c, actual, expected)
    for t, x in ((0.41, 0.27), (0.1, 1.2), (0.9, -2.1)):
        a, b = exact(t, x, sigma, omega), original_integral(t, x, sigma, omega)
        assert abs(a - b) < 2e-8 * (1 + abs(a)), (c, t, x, a, b)
    print('PASS', c, 'inner', inner, 'outer', outer)

print('ALL_FIRST_HERMITE_CHECKS_PASSED')
