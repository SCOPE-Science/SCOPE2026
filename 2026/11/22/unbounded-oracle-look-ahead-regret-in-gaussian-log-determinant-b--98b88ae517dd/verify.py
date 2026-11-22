"""Standalone finite checks of two-plateau log-determinant budget laws.

Run: python3 verify.py. The finite checks supplement, not replace,
the theorem's algebraic and Gaussian moment proof.
"""
from fractions import Fraction
from math import gcd, log1p, sqrt


def verify_family():
    checks = 0
    for q in range(2, 9):
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            beta = Fraction(p, q)
            for m in range(2, 9):
                for j in (1, 2, 3, 5, 12, 32):
                    ell = m*q*q*j
                    top = beta*ell
                    early = beta*beta*ell
                    assert top.denominator == early.denominator == 1
                    top, early = int(top), int(early)
                    delta = top - early
                    assert delta > 0
                    tail = ell*ell
                    n = top + tail
                    assert ell < n
                    k = Fraction(ell+m-top, m)
                    assert k.denominator == 1 and k > 1
                    qlook = Fraction(m, delta+m)
                    for a in (Fraction(1, 4), Fraction(1, 10), Fraction(1, 100)):
                        # The weak eigenvalue b satisfies N*b*b=(m/2)*a*a.
                        weak_mass = Fraction(m, 2)*a*a
                        f0 = delta*a*a + weak_mass
                        f1 = weak_mass
                        assert qlook*f0 > f1
                        b = float(a)*sqrt(m/2)/ell
                        h = log1p(float(a))
                        t = log1p(b)
                        assert b < float(a)
                        assert qlook*(delta*h*h + tail*t*t) > tail*t*t
                        n_extra = ell-top
                        assert tail-n_extra > 0
                        risk_one = 2*(tail-n_extra)*t*t
                        risk_many = 2*tail*t*t/int(k)
                        exact_regret = k*(1-Fraction(n_extra,tail))
                        assert abs(risk_one/risk_many-float(exact_regret)) < 1e-9
                        assert risk_one > risk_many
                        checks += 10
    return checks


def verify_recommended_parameters():
    checks = 0
    prev = Fraction(0)
    for j in range(1, 101):
        ell = 32*j
        n = 24*j + ell**2
        assert n > ell
        K = 4*j+1
        ratio = Fraction(K*(ell*ell-8*j),ell*ell)
        assert ratio == Fraction(K)*(1-Fraction(1,128*j))
        assert ratio > prev
        prev=ratio
        for a in (Fraction(1,4),Fraction(1,1000)):
            b = float(a)/ell
            f0 = (6*j+1)*a*a
            f1 = a*a
            qlook = Fraction(1,3*j+1)
            assert qlook*f0 > f1
            h,t = log1p(float(a)),log1p(b)
            assert qlook*(6*j*h*h+ell*ell*t*t) > ell*ell*t*t
            assert (1+float(a))/(1+b) < 1+float(a)
            assert abs((2*(ell*ell-8*j)*t*t)/(2*ell*ell*t*t/K)-float(ratio)) < 1e-10
            checks += 7
    return checks


if __name__ == '__main__':
    general = verify_family()
    recommended = verify_recommended_parameters()
    print(f'VERIFY_OK general_inequality_checks={general} recommended_checks={recommended}')
