from fractions import Fraction


def cov_closed(m, t):
    return -Fraction(1, m) * (
        Fraction(t.numerator, t.denominator)
        * (m - 1)
        * (1 - t) ** (m - 1)
        * ((m + 2) * t - 2)
        / (m + 1)
    )


def eg_indicator_integral(m, t):
    # Independent exact computation of E[G * 1{D1>t}] by one-dimensional integration.
    q = 1 - t
    # Integral over d=D1 with density (m-1)(1-d)^(m-2):
    # d^2 plus the conditional mean sum of squares of the remaining simplex.
    # Substitution u=1-d gives exact beta-polynomial terms.
    a = (m - 1) * (
        q ** (m - 1) / (m - 1)
        - 2 * q ** m / m
        + q ** (m + 1) / (m + 1)
    )
    b = Fraction(2 * (m - 1), m) * q ** (m + 1) / (m + 1)
    return a + b


def cov_from_integral(m, t):
    p = (1 - t) ** (m - 1)
    eg = Fraction(2, m + 1)
    en = m * p
    egn = m * eg_indicator_integral(m, t)
    cov_g_n = egn - eg * en
    return -cov_g_n / m


def var_fhat(m, t):
    p = (1 - t) ** (m - 1)
    q = (1 - 2*t) ** (m - 1) if 2*t <= 1 else Fraction(0)
    var_n = m * p * (1-p) + m * (m-1) * (q-p*p)
    return var_n / (m*m)


def integral_cov(m):
    # Integrate over x=m t. Closed beta integrals.
    i1 = Fraction(1, m*(m+1))
    i2 = Fraction(2, m*(m+1)*(m+2))
    return Fraction(m-1, m+1) * (2*i1 - (m+2)*i2)


def run(max_m=80):
    assertions = 0
    thresholds = 0
    for m in range(2, max_m+1):
        # Endpoints plus a dense rational t-grid adapted to m.
        den = 4*m + 3
        ts = {Fraction(0), Fraction(1)}
        for j in range(1, den):
            ts.add(Fraction(j, den))
        # Include the exact sign-change threshold t*=2/(m+2).
        ts.add(Fraction(2, m+2))
        for t in sorted(ts):
            thresholds += 1
            c1 = cov_closed(m, t)
            c2 = cov_from_integral(m, t)
            assert c1 == c2
            assertions += 1

            v = var_fhat(m, t)
            assert v >= 0
            assertions += 1

            if 0 < t < 1:
                root = Fraction(2, m+2)
                if t < root:
                    assert c1 > 0
                elif t == root:
                    assert c1 == 0
                else:
                    assert c1 < 0
                assertions += 1

        assert integral_cov(m) == 0
        assertions += 1

        # Check Greenwood variance from Dirichlet fourth moments.
        e_g = Fraction(2, m+1)
        e_g2 = (
            m * Fraction(24, m*(m+1)*(m+2)*(m+3))
            + m*(m-1) * Fraction(4, m*(m+1)*(m+2)*(m+3))
        )
        var_g = e_g2 - e_g*e_g
        target = Fraction(4*(m-1), (m+1)*(m+1)*(m+2)*(m+3))
        assert var_g == target
        assertions += 1

    print('VERIFY_OK')
    print(f'max_m={max_m}')
    print(f'thresholds_checked={thresholds}')
    print(f'exact_assertions={assertions}')


if __name__ == '__main__':
    run()
