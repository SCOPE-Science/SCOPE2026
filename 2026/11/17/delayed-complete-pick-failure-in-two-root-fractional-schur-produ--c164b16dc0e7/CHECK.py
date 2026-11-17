"""Independent finite arithmetic checks for a two-root fractional kernel.

Only standard-library Fraction is used. These tests do not prove asymptotics.
"""
from fractions import Fraction as F
from math import gamma


def binom_power_coeff(exponent, n):
    """Exact [z^n](1-z)^exponent for a rational exponent."""
    p = F(1)
    for k in range(1, n + 1):
        p *= F(k - 1) - exponent
        p /= k
    return p


def recurrence_coeffs(a, b, nmax):
    """Coefficient array of (1-t)^a (1-t^2)^b."""
    f = [F(1), -a]
    for n in range(1, nmax):
        f.append((-a * f[n] + (n - 1 - a - 2 * b) * f[n - 1]) / (n + 1))
    return f[:nmax + 1]


def convolution_coeffs(a, b, nmax):
    p = [binom_power_coeff(a, k) for k in range(nmax + 1)]
    q = [binom_power_coeff(b, k) for k in range(nmax // 2 + 1)]
    return [sum((p[n - 2 * j] * q[j] for j in range(n // 2 + 1)), F(0))
            for n in range(nmax + 1)]


def first_negative(a, b, limit):
    f = recurrence_coeffs(a, b, limit)
    bad = [n for n in range(1, limit + 1) if f[n] > 0]
    return (bad[0] if bad else None), f


def main():
    checks = 0
    test_params = [(F(1, 2), F(1, 100)), (F(1, 2), F(1, 200)),
                   (F(7, 10), F(1, 200)), (F(3, 10), F(1, 20)),
                   (F(1, 1), F(1, 10))]
    for a, b in test_params:
        f = recurrence_coeffs(a, b, 80)
        g = convolution_coeffs(a, b, 80)
        assert f == g
        checks += len(f)
        assert f[0] == 1 and f[1] == -a
        checks += 2

    expected = [
        (F(1, 2), F(1, 100), 403, 410),
        (F(1, 2), F(1, 200), 1603, 1610),
        (F(7, 10), F(1, 200), 121, 150),
        (F(1, 1), F(1, 10), 3, 8),
    ]
    for a, b, want, limit in expected:
        observed, coefficients = first_negative(a, b, limit)
        assert observed == want, (a, b, observed, want)
        assert all(coefficients[n] <= 0 for n in range(1, want))
        assert coefficients[want] > 0
        checks += want + 1

    a = 0.5
    leading = lambda b: (a / (2 ** a * gamma(1 - a) * b)) ** (1 / a)
    assert abs(403 / leading(.01) - 1) < .025
    assert abs(1603 / leading(.005) - 1) < .01
    checks += 2
    print(f"PASS: {checks} exact coefficient/sign and scalar asymptotic checks")
    print("Checked first negative coefficients: (a,b,N)=(1/2,1/100,403),"
          " (1/2,1/200,1603), (7/10,1/200,121), (1,1/10,3)")
    print("Finite computation is not a proof of the infinite theorem.")

if __name__ == '__main__':
    main()
