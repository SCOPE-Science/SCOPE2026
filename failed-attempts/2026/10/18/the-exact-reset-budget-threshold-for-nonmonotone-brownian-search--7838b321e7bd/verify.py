"""Exact rational certificate for the finite-reset Brownian threshold theorem.

Requires Python >=3.10 and SymPy >=1.10. Run: python verify.py
"""
from fractions import Fraction as Fr
from math import comb, exp, log
import sympy as sp

x = sp.Symbol('x')
t = sp.Symbol('t')


def weighted_polynomials(n):
    Q = sp.Poly(0, x, domain=sp.QQ)
    M = sp.Poly(0, x, domain=sp.QQ)
    for j in range(1, n+1):
        Q += sp.Poly((2*x)**j * (1+x)**(n-j), x)
        M += sp.Poly(j * (2*x)**(j-1) * (1+x)**(n-j), x)
    return Q, M


def rational_log_upper_polynomial(n=21, terms=4):
    Q, M = weighted_polynomials(n)
    B = sp.Poly(sum(sp.Rational(1, 2*j+1)*x**(2*j+1)
                    for j in range(terms)), x)
    P = (sp.Poly(1-x*x, x) *
         (Q-sp.Poly(1-x, x)*M*B)
         - sp.Poly(1-x, x)*M*
         sp.Poly(x**(2*terms+1) / sp.Integer(2*terms+1), x))
    divisor = sp.Poly(x*(1-x), x)
    F, remainder = sp.div(P, divisor)
    assert remainder.is_zero
    assert F.degree() == 28
    assert F.eval(0) == 1
    assert F.eval(1) == sp.Rational(183500800, 3)
    return F


def to_fraction(z):
    q = sp.Rational(z)
    return Fr(int(q.p), int(q.q))


def bernstein_coefficients_on_interval(F, a, b):
    degree = F.degree()
    polynomial = sp.Poly(F.as_expr().subs(
        x, sp.Rational(a.numerator, a.denominator)
        + sp.Rational((b-a).numerator, (b-a).denominator)*t), t)
    power_coefficients = [to_fraction(c) for c in reversed(polynomial.all_coeffs())]
    assert len(power_coefficients) == degree+1
    return [sum((power_coefficients[k]*Fr(comb(j,k), comb(degree,k))
                 for k in range(j+1)), Fr(0))
            for j in range(degree+1)]


def certify_positive_polynomial():
    F = rational_log_upper_polynomial()
    expected_minima = [
        Fr(1),
        Fr(98838903696272268379, 756604737398243328),
        Fr(286415793320830451119, 630503947831869440),
        Fr(231505758399776864059, 180143985094819840),
    ]
    for k in range(4):
        coeff = bernstein_coefficients_on_interval(
            F, Fr(k,4), Fr(k+1,4))
        assert len(coeff) == 29
        assert all(v > 0 for v in coeff)
        assert min(coeff) == expected_minima[k]
    # An independent exact Sturm check, not needed for the Bernstein proof.
    assert F.count_roots(0, 1) == 0
    return expected_minima


def certify_lower_counterexample():
    q = Fr(6, 7)
    y = Fr(3, 4)
    n = 22
    S = sum((q**j for j in range(1, n+1)), Fr(0))
    S_prime = sum((j*q**(j-1) for j in range(1, n+1)), Fr(0))
    lower_log7 = 2*sum((y**(2*j+1) / Fr(2*j+1)
                        for j in range(5)), Fr(0))
    assert lower_log7 == Fr(8858481, 4587520)
    strict_margin = lower_log7*(1-q)*S_prime - 2*S
    assert strict_margin == Fr(641665092531749639153799,
                               17936382256795429334548480)
    assert strict_margin > 0
    return strict_margin


def independent_numeric_cross_checks():
    # Derivative computed independently from the dimensionless mean formula.
    def T(n, z):
        q = -__import__('math').expm1(-z)
        return sum(q**j for j in range(1,n+1))/z**2
    def H(n, z):
        q = -__import__('math').expm1(-z)
        S = sum(q**j for j in range(1,n+1))
        Sp = sum(j*q**(j-1) for j in range(1,n+1))
        return z*exp(-z)*Sp/S
    for n in (1, 2, 10, 20, 21, 22, 40):
        for z in (0.35, 0.8, 1.2, log(7), 3.0, 7.0):
            h = 1e-5
            derivative = (T(n,z+h)-T(n,z-h))/(2*h)
            formula = T(n,z)*(H(n,z)-2)/z
            assert abs(derivative-formula) < 1e-6*max(1, abs(formula))
    assert H(21, log(7)) < 2 < H(22, log(7))
    assert T(22,1.8) < T(22,2.0)
    assert T(22,2.0) > T(22,2.3)


if __name__ == '__main__':
    values = certify_positive_polynomial()
    margin = certify_lower_counterexample()
    independent_numeric_cross_checks()
    print('Exact Bernstein certificate: four strictly positive 29-coefficient lists.')
    print('Minimum Bernstein coefficients:', ', '.join(str(v) for v in values))
    print('Exact strict 22-attempt witness margin:', str(margin))
    print('Independent finite numerical consistency checks: passed.')
