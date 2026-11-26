"""Exact independent arithmetic checks of the arithmetic-progression denumerant RMS identity.

Run: python3 verify.py
Only Python standard library is required.
"""
from fractions import Fraction
from math import gcd


def direct_mean_square(a: int, d: int) -> Fraction:
    b, c = a + d, a + 2 * d
    period = a * b * c
    # The coefficient of z^t in (1-z^a)^-1(1-z^b)^-1(1-z^c)^-1.
    counts = [0] * period
    counts[0] = 1
    for part in (a, b, c):
        for t in range(part, period):
            counts[t] += counts[t - part]

    scale = 12 * period
    const = a * a + b * b + c * c + 3 * (a*b + a*c + b*c)
    errors = [Fraction(scale * counts[t] - (6*t*t + 6*(a+b+c)*t + const), scale)
              for t in range(period)]
    assert sum(errors) == 0, ('nonzero mean', a, d)
    return sum((e*e for e in errors), Fraction(0)) / period


def formula(a: int, d: int) -> Fraction:
    b, c = a + d, a + 2*d
    odd_wave = lambda m: Fraction(m**4 + 70*m*m - 71, 2880*m*m)
    middle_wave = lambda m: Fraction(m**4 + 10*m*m - 11, 720*m*m)
    return odd_wave(a) + middle_wave(b) + odd_wave(c)


def main():
    count = 0
    samples = []
    for a in range(1, 17, 2):
        for d in range(1, 11):
            if gcd(a, d) != 1 or a*(a+d)*(a+2*d) > 12000:
                continue
            direct, predicted = direct_mean_square(a, d), formula(a, d)
            if direct != predicted:
                raise AssertionError((a,d,direct,predicted))
            count += 1
            if (a,d) in ((1,1),(3,1),(5,2),(7,2),(11,3)):
                samples.append((a, d, str(direct)))
    assert count >= 40, count
    print('CERTIFICATE_OK configurations=%d exact_rational_equalities=%d' % (count, count))
    for a, d, variance in samples:
        print('case a=%d d=%d variance=%s' % (a, d, variance))

if __name__ == '__main__':
    main()
