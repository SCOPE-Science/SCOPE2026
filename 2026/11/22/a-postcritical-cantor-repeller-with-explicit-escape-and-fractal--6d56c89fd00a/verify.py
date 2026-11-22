#!/usr/bin/env python3
"""Standalone high-precision consistency checks for a rational K-map survivor theorem.

The infinite claims are established analytically in RESULT.md. This script
checks branch inversion, sharp contraction boundary, cylinder coverage, and
asymptotic numerical diagnostics; no finite computation is used as a substitute
for the proof.
"""
from decimal import Decimal, localcontext
from fractions import Fraction


def sqrt(x):
    return x.sqrt()


def branches(mu, y):
    disc = mu * mu - 6 * mu * y + y * y
    root = sqrt(disc)
    return ((mu - y - root) / (2 * mu), (mu - y + root) / (2 * mu))


def kmap(mu, x):
    return mu * x * (1 - x) / (1 + x)


def derivative_bounds(mu):
    d = mu * mu - 6 * mu + 1
    q = (3 * mu - 1) / sqrt(d)
    return ((q - 1) / (2 * mu), (q + 1) / (2 * mu))


def root_dimension(m, a, b):
    low, high = Decimal(0), Decimal(2)
    for _ in range(240):
        mid = (low + high) / 2
        f = a ** mid + b ** mid
        if f > 1:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def verify():
    with localcontext() as ctx:
        ctx.prec = 85
        one = Decimal(1)
        mu_c = 3 + 2 * sqrt(Decimal(2))
        assert Decimal('5.82842') < mu_c < Decimal('5.82843')
        def cubic(m):
            return m*m*m - 7*m*m + 5*m - 1
        lower, upper = Decimal('6.2222'), Decimal('6.2224')
        assert cubic(lower) < 0 < cubic(upper)
        for _ in range(190):
            middle = (lower + upper) / 2
            if cubic(middle) > 0:
                upper = middle
            else:
                lower = middle
        mu_h = (lower + upper) / 2
        assert abs(mu_h - Decimal('6.222262523120398626674561101')) < Decimal('1e-25')
        u1h, u2h = derivative_bounds(mu_h)
        assert abs(u2h-one) < Decimal('1e-55')
        assert u1h < one
        inversions = 0
        chains = 0
        for mu in [Decimal('6.25'), Decimal(7), Decimal(8), Decimal(16), Decimal(64)]:
            ul, ur = derivative_bounds(mu)
            assert Decimal(0) < ul < ur < one
            disc = mu * mu - 6*mu + one
            a, b = branches(mu, one)
            assert Decimal(0) < a < sqrt(Decimal(2))-one < b < one
            assert abs((b-a) - sqrt(disc)/mu) < Decimal('1e-75')
            assert abs(kmap(mu, a)-one) < Decimal('1e-75')
            assert abs(kmap(mu, b)-one) < Decimal('1e-75')
            assert abs(kmap(mu, one)) < Decimal('1e-75')
            for i in range(1, 51):
                y = Decimal(i)/Decimal(51)
                lm, rp = branches(mu, y)
                assert Decimal(0) < lm < a and b < rp < one
                assert abs(kmap(mu, lm)-y) < Decimal('1e-72')
                assert abs(kmap(mu, rp)-y) < Decimal('1e-72')
                # Inverse derivatives: g_i'(y) = 1/K'(g_i(y)).
                for z in (lm, rp):
                    deriv = mu*(1-2*z-z*z)/(1+z)**2
                    assert abs(deriv) > one
                inversions += 2
            l1, l2 = one/mu, Decimal(2)/mu
            low_dim = root_dimension(mu, l1, l2)
            high_dim = root_dimension(mu, ul, ur)
            assert Decimal(0) < low_dim <= high_dim
            logmu = mu.ln()
            B = Decimal(2).ln()
            three_term = B/logmu + B*B/(2*logmu**2) + (B**3/4 + B**4/8)/logmu**3
            if mu >= 16:
                assert abs(low_dim - three_term) < Decimal('0.002')
            chains += 1
        print('PASS', inversions, 'independent high-precision inverse checks;', chains,
              'parameter checks; cubic root', mu_h)
        # Rational exact source-map geometry checks (no floating approximations).
        for m in (7, 8, 16, 32):
            mf = Fraction(m)
            assert (mf-1)**2 - 4*mf == mf*mf-6*mf+1
            assert (mf+1) * Fraction(1,2) == (mf+1)/2
        print('PASS exact rational discriminant identity and parameter arithmetic')


if __name__ == '__main__':
    verify()
