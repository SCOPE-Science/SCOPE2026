#!/usr/bin/env python3
"""Distinct rational algebra checks for polynomial-generator consequences.
Run: python3 verify.py (Python standard library only).
This is supplementary finite verification; asymptotic proof is in RESULT.md.
"""
from fractions import Fraction as F


def lin_diff(a, lam, gam, r):
    m = a / (r + gam + 2 * lam)
    v2 = 2 * a * m / (r + 2 * gam)
    return (v2 + a * m / (2 * lam)) / (r + gam)


def cubic_first_variation(a, lam, gam, r):
    """Exact derivative of diffusion at zero cubic-drag strength.
    Derivation: moment closure of L_0 on (v*sigma,v^2,v^3*sigma,v^4)
    and resolvent closure on (v^3,sigma*v^2,v,sigma).
    """
    m = a / (r + gam + 2 * lam)
    v2 = 2 * a * m / (r + 2 * gam)
    sv3 = 3 * a * v2 / (r + 3 * gam + 2 * lam)
    v4 = 4 * a * sv3 / (r + 4 * gam)
    h3 = 1 / (r + 3 * gam)
    hs2 = 3 * a * h3 / (r + 2 * gam + 2 * lam)
    hv = 2 * a * hs2 / (r + gam)
    hs = a * hv / (2 * lam)
    I_prime = h3*v4 + hs2*sv3 + hv*v2 + hs*m
    m_prime = -sv3 / (r + gam + 2 * lam)
    v2_prime = (2*a*m_prime - 2*v4) / (r + 2 * gam)
    return (v2_prime + a*m_prime/(2*lam) - I_prime) / (r + gam)


def checks():
    n = 0
    for a in (F(1,3), F(2,3), F(2)):
        for lam in (F(1,4), F(1), F(3)):
            for gam in (F(1,2), F(1), F(2)):
                for r in (F(1), F(4), F(16), F(64)):
                    d = lin_diff(a,lam,gam,r)
                    expected = a*a*(r+2*gam+4*lam)/(2*lam*(r+gam)*(r+2*gam)*(r+gam+2*lam))
                    assert d == expected
                    n += 1
                    assert cubic_first_variation(a,lam,gam,r) < 0
                    n += 1
    # The coefficient is a genuine limit, not a fit. Rational evaluations
    # at increasing r check its sign and convergence quantitatively.
    for a,lam,gam in [(F(2,3),F(1,2),F(1)),(F(1),F(2),F(3,4)),(F(2),F(1,3),F(2))]:
        target = -6*a**4/lam
        for r in (F(10**5),F(10**6),F(10**7)):
            ratio = cubic_first_variation(a,lam,gam,r)*r**5/target
            assert abs(ratio-F(1)) < F(1,100)
            n += 1
    print(f"PASS: {n} exact-fraction algebraic assertions")


if __name__ == '__main__':
    checks()
