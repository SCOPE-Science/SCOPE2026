"""Exact arithmetic checks for sign correlations and tightness obstruction."""
from fractions import Fraction
from math import comb, isqrt


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def corr(d, s, m):
    return Fraction(sum((-1)**j * choose(m, j) * choose(d-m, d-s-j)
                        for j in range(m+1)), choose(d, d-s))


checks = 0
for d in range(4, 201):
    for s in range(d+1):
        t = 2*s-d
        two = Fraction(t*t-d, d*(d-1))
        four = Fraction(t**4-(6*d-8)*t*t+3*d*(d-2),
                        d*(d-1)*(d-2)*(d-3))
        assert corr(d, s, 2) == two
        assert corr(d, s, 4) == four
        assert not (two == 0 and four == 0)
        if two == 0:
            assert isqrt(d)**2 == d
            assert four == Fraction(-2, (d-2)*(d-3))
        checks += 1
print('EXACT_SIGN_CORRELATION_PASS', checks)
