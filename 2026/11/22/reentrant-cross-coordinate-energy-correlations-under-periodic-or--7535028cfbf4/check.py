"""Exact-rational enclosure and independent phase integration for a harmonic particle with deterministic heading renewals."""
from fractions import Fraction as F
from math import factorial, exp

class Interval:
    def __init__(self, low, high=None):
        self.low = F(low)
        self.high = F(low if high is None else high)
        assert self.low <= self.high

    def __add__(self, other):
        other = as_interval(other)
        return Interval(self.low + other.low, self.high + other.high)
    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.high, -self.low)

    def __sub__(self, other):
        return self + -as_interval(other)

    def __rsub__(self, other):
        return as_interval(other) - self

    def __mul__(self, other):
        other = as_interval(other)
        values = [x*y for x in (self.low, self.high) for y in (other.low, other.high)]
        return Interval(min(values), max(values))
    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_interval(other)
        assert other.low * other.high > 0
        return self * Interval(1 / other.high, 1 / other.low)

    def __rtruediv__(self, other):
        return as_interval(other) / self

    def __pow__(self, exponent):
        assert isinstance(exponent, int) and exponent >= 0
        out = Interval(1)
        for _ in range(exponent):
            out = out * self
        return out


def as_interval(value):
    return value if isinstance(value, Interval) else Interval(value)


def exp_minus_interval(t, n=76):
    """Rational enclosures of exp(-t), using a bounded exponential Taylor tail."""
    assert isinstance(t, int) and 0 < t < n + 2
    t = F(t)
    terms = [t**k / factorial(k) for k in range(n + 2)]
    partial = sum(terms[:n + 1])
    tail_max = terms[n + 1] / (1 - t / F(n + 2))
    return Interval(1/(partial + tail_max), 1/partial)


def moments_enclosure(theta):
    """First two phase moments of square-weight sum and fourth-weight sum."""
    z = exp_minus_interval(theta)
    A = 2 / (1 + z)
    B = (1-z)**4 / (1-z**4)
    M = lambda k: (1-z**k) / F(k * theta)
    E_S = 1 - 2*M(1) + A*M(2)
    E_S2 = 1 - 4*M(1) + (4+2*A)*M(2) - 4*A*M(3) + A**2*M(4)
    E_P = 1 - 4*M(1) + 6*M(2) - 4*M(3) + (1+B)*M(4)
    var_S = E_S2 - E_S**2
    return z, E_S, var_S, E_P


def bracket_enclosure(theta, d):
    assert d >= 2
    _, _, variance, fourth = moments_enclosure(theta)
    return variance - 2*fourth / F(d+2)


def midpoint_phase_moments(theta, n=24000):
    """Independent floating-point quadrature of original geometric weights."""
    z = exp(-theta)
    ratio2 = (1-z)/(1+z)
    ratio4 = (1-z)**4 / (1-z**4)
    es = es2 = ep = 0.0
    for j in range(n):
        u = theta * (j + 0.5) / n
        y = exp(-u)
        s = (1-y)**2 + y*y*ratio2
        p = (1-y)**4 + y**4*ratio4
        es += s
        es2 += s*s
        ep += p
    es /= n
    es2 /= n
    ep /= n
    return es, es2-es*es, ep


def main():
    witnesses = [(1,-1), (3,1), (10,-1)]
    for theta, sign in witnesses:
        z, e_s, var_s, e_p = moments_enclosure(theta)
        assert e_p.low > 0, 'Positive fourth-weight moment'
        cov_bracket = bracket_enclosure(theta, 41)
        if sign > 0:
            assert cov_bracket.low > 0
        else:
            assert cov_bracket.high < 0
        # Check finite exact-rational enclosure against independently integrated weights.
        es_float, vs_float, p_float = midpoint_phase_moments(theta)
        assert abs(es_float-float(e_s.low)) < 2e-7
        assert abs(vs_float-float(var_s.low)) < 2e-7
        assert abs(p_float-float(e_p.low)) < 2e-7
        print('theta=',theta,'d=41 bracket in',float(cov_bracket.low),float(cov_bracket.high),'sign',sign)
    z, _, v, p = moments_enclosure(3)
    assert F(49787068367,10**12) < z.low <= z.high < F(49787068369,10**12)
    c = v - 2*p/F(43)
    assert F(18080676,10**11) < c.low <= c.high < F(18080678,10**11)
    # Monotonicity in dimension follows exactly from E_P>0 and 1/(d+2).
    for d in (41,42,100,1000):
        assert bracket_enclosure(3,d).low>0
    print('EXACT-RATIONAL SIGN WITNESSES AND INDEPENDENT QUADRATURE: PASS')

if __name__ == '__main__':
    main()
