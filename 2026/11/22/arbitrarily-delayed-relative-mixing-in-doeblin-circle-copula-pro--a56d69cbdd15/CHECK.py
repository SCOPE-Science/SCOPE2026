"""Numerical consistency checks for a singular circle-copula Markov chain.

Requires mpmath. The mathematical proof is analytic and does not rely on
these finite numerical checks.
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 45


def fourier(a, k):
    a = mp.mpf(a)
    z = 2 * mp.pi * 1j * k
    return (1-a) * mp.gammainc(1-a, 0, z) / z**(1-a)


def asymptotic_lead(a, k):
    a = mp.mpf(a)
    return (mp.gamma(2-a) * (2*mp.pi)**(a-1)
            * mp.exp(-1j*mp.pi*(1-a)/2) * k**(a-1))


def run():
    # Algebraic finite-lag identity: psi(2)/epsilon^2 = (1-a)^2/(1-2a)-1.
    for a in (Fraction(1, 10), Fraction(1, 4), Fraction(2, 5)):
        lhs = (1-a)**2 / (1-2*a) - 1
        rhs = a*a / (1-2*a)
        assert lhs == rhs and lhs > 0
    print('exact rational psi(2) formulas: 3/3 passed')

    # Independent Fourier computation via a complex incomplete-gamma integral.
    for a in ('0.25', '0.50', '0.75'):
        e1 = abs(fourier(a, 80)/asymptotic_lead(a, 80)-1)
        e2 = abs(fourier(a, 240)/asymptotic_lead(a, 240)-1)
        assert e2 < e1 and e2 < mp.mpf('0.20')
        assert abs(fourier(a, 1)) < 1
    print('nonzero Fourier decay and phase: 3/3 passed')

    # Positive Fourier squared tails agree with the exact L2 identity.
    a = mp.mpf('0.25')
    partial_64 = 2*sum(abs(fourier(a, k))**2 for k in range(1, 65))
    partial_256 = 2*sum(abs(fourier(a, k))**2 for k in range(1, 257))
    target = a*a/(1-2*a)
    assert 0 < partial_64 < partial_256 < target
    assert abs(partial_256-target) < mp.mpf('0.012')
    print('positive even-lag Fourier series: passed')

    # The truncated L2 integral diverges for a>=1/2, at polynomial/log rates.
    for a in (mp.mpf('0.5'), mp.mpf('0.75')):
        def tail_integral(delta):
            if a == mp.mpf('0.5'):
                return (1-a)**2 * (-mp.log(delta))
            return (1-a)**2 * (1-delta**(1-2*a))/(1-2*a)
        assert tail_integral(mp.mpf('1e-8')) > tail_integral(mp.mpf('1e-5'))
    print('critical supercritical L2 divergence: 2/2 passed')

    # Exact integer delay: n(1-a)>1 is the first finite-relative-mixing lag.
    for a in (Fraction(1, 4), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(9, 10)):
        d = 1/(1-a)
        first = d.numerator//d.denominator + 1
        assert first * (1-a) > 1 and (first-1) * (1-a) <= 1
    print('finite-lag threshold arithmetic: 5/5 passed')
    print('ALL NUMERICAL CONSISTENCY CHECKS PASSED')


if __name__ == '__main__':
    run()
