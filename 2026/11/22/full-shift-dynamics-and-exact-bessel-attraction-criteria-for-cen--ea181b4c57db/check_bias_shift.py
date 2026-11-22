"""Finite reproducibility checks for the centered quadratic-bias conjugacy.

This program checks illustrative identities and truncation-sensitive numerical
examples; the general infinite-dimensional result is established by proof.
"""
from fractions import Fraction
from math import factorial
from decimal import Decimal, localcontext


def tail_ratio_pmf(r, k, count):
    """First count weights of Phi(r), normalized on the finite window."""
    w = [Fraction(1, factorial(k))]
    for n in range(count - 1):
        w.append(w[-1] * r[n] / ((n+1)*(n+k+1)))
    z = sum(w)
    return [v/z for v in w]


def recovered_ratio(p, k, n):
    return Fraction((n+1)*(n+k+1)) * p[n+1] / p[n]


def local_unscaled_weights(r, k, count):
    w = [Fraction(1, factorial(k))]
    for n in range(count-1):
        w.append(w[-1] * r[n] / ((n+1)*(n+k+1)))
    return w


def checks():
    assertions=0
    # Check the exact algebra of shifted weighted ratios for several periods.
    for k in [0, 1, 4]:
        for m in [1, 2, 3, 5, 7]:
            period = [Fraction(j+2, j+1) for j in range(m)]
            # For m>1, all ratios differ; for m=1 they are constant.
            r = [period[n%m] for n in range(80)]
            p = tail_ratio_pmf(r, k, 75)
            for n in range(60):
                assert recovered_ratio(p, k, n) == period[n%m]
                assertions += 1
            # A centered bias has tail ratios shifted by exactly one.
            q = [Fraction((n+1)*(n+k+1))*p[n+1] for n in range(72)]
            q = [x/sum(q) for x in q]
            for n in range(60):
                assert recovered_ratio(q, k, n) == period[(n+1)%m]
                assertions += 1
            # Shift by m restores exactly the original ratios.
            for n in range(20):
                assert r[n+m] == r[n]
                assertions += 1
    # Explicit positive two-cycle at k=0: weights 1,2,1,2,... .
    r = [Fraction(2) if n%2 == 0 else Fraction(1, 2) for n in range(90)]
    p = tail_ratio_pmf(r, 0, 75)
    q = tail_ratio_pmf(r[1:], 0, 75)
    for n in range(50):
        assert recovered_ratio(q, 0, n) == r[n+1]
        assert r[n+2] == r[n]
        assertions += 2
    assert p[1]/p[0] != q[1]/q[0]
    assertions += 1
    # Exact finite-prefix convergence of a ratio sequence to a 2-periodic one.
    a = [Fraction(3, 2), Fraction(2, 3)]
    for t in [12, 35, 80, 160, 400]:
        r_t = [a[(t+j)%2] * (1 + Fraction(1, t+j+2)) for j in range(32)]
        expected = [a[(t+j)%2] for j in range(32)]
        actual = tail_ratio_pmf(r_t, 2, 30)
        limit = tail_ratio_pmf(expected, 2, 30)
        # Explicit bound via the finite window plus a very small tail.
        eps = Fraction(1, t+2)
        z0 = local_unscaled_weights(expected, 2, 30)
        zplus = sum(v * (1+eps)**n for n,v in enumerate(z0))
        zminus = sum(v * (1-eps)**n for n,v in enumerate(z0))
        z = sum(z0)
        d = sum(abs(x-y) for x,y in zip(actual,limit))/2
        assert d <= (zplus-z)/zminus
        assertions += 1
    # Direct half-line point probability shows finite total mass and positivity.
    with localcontext() as ctx:
        ctx.prec=65
        for k in [0, 2, 7]:
            mass=Decimal(0)
            w=Decimal(1)/Decimal(factorial(k))
            for n in range(85):
                mass += w
                w *= Decimal(2)/Decimal((n+1)*(n+k+1))
            assert mass>0 and w<Decimal('1e-110')
            assertions += 1
    print(f'PASS {assertions} exact/finite diagnostic assertions')


if __name__=='__main__':
    checks()
