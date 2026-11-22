"""Exact algebraic certificate for a quartic parametric zero-trajectory theorem.

Requires Python 3.10+ and SymPy 1.12+; no network access is needed.
The script verifies symbolic identities and positive-coefficient certificates.
"""
from math import comb
import sympy as S


def main():
    a, z, t = S.symbols('a z t')
    h = S.expand(S.cancel(
        sum((-1)**j * S.binomial(4, j) * z**j/(j-a) for j in range(5))
        * S.prod(j-a for j in range(5))
    ))
    disc = 331776*a**3*(a-4)**3*(a-3)**2*(a-2)**2*(a-1)**2
    assert S.expand(S.discriminant(h, z)-disc) == 0
    p = (18*a**10-360*a**9+3114*a**8-15264*a**7
         +46647*a**6-92052*a**5+117335*a**4-93688*a**3
         +43664*a**2-10368*a+972)
    expected_res = 442368*(a**2-4*a+1)*p
    assert S.expand(S.resultant(h, S.diff(h, a), z)-expected_res) == 0
    # For each closed subinterval [l,r], a=(l+r*t)/(1+t), t>=0;
    # (1+t)^10 p(a) has strictly positive coefficients.
    for l, r in [(S.Integer(0), S.Rational(1, 3)),
                 (S.Rational(1, 3), S.Rational(2, 3)),
                 (S.Rational(2, 3), S.Integer(1))]:
        q = S.Poly(S.cancel((1+t)**10*p.subs(a, (l+r*t)/(1+t))), t)
        assert q.degree() == 10
        assert len(q.all_coeffs()) == 11
        assert all(c > 0 for c in q.all_coeffs())
    A = 2-S.sqrt(3)
    X = 2+S.sqrt(3)
    assert S.simplify(h.subs({a: A, z: X})) == 0
    assert S.simplify(S.diff(h, a).subs({a: A, z: X})) == 0
    assert S.simplify(S.diff(h, z).subs({a: A, z: X}) +24+16*S.sqrt(3)) == 0
    C = z**3 - S.sqrt(3)*z**2 + (3+2*S.sqrt(3))*z + 2+S.sqrt(3)
    assert S.simplify(S.expand(h.subs(a, A) - (6-4*S.sqrt(3))*(z-X)*C)) == 0
    J = a*(4-a)*S.diff(h, a)-4*z*S.diff(h, z)
    res_CJ = S.resultant(C, J.subs(a, A), z)
    assert S.simplify(res_CJ-(847872+494592*S.sqrt(3))) == 0
    for degree in (2, 3):
        hsmall = S.expand(S.cancel(
            sum((-1)**j*S.binomial(degree, j)*z**j/(j-a)
                for j in range(degree+1))*S.prod(j-a for j in range(degree+1))
        ))
        factor = S.factor(S.discriminant(hsmall, z))
        if degree == 2:
            assert S.expand(factor+4*a*(a-2)) == 0
        else:
            assert S.expand(factor+216*a**2*(a-3)**2*(a-2)*(a-1)) == 0
    print('PASS: quartic discriminant, stationary resultant, three exact positivity certificates,')
    print('      radical stationary point, factorization, nonstationary conjugate pair, lower orders.')


if __name__ == '__main__':
    main()
