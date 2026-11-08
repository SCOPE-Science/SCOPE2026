#!/usr/bin/env python3
"""Exact rational verification of cubic-harmonic latitude E-optimality.

Only Python's standard library is needed. This script checks finite-dimensional
separations, active eigenvalue branches, and high-dimensional polynomial signs.
The general theorem also uses the analytic monotonicity argument in RESULT.md.
"""
from fractions import Fraction as F


def eig(d, x):
    """Four eigenvalues at squared latitude z=x/(d+2)."""
    d, x = F(d), F(x)
    z = x / (d + 2)
    return (
        d * (d + 4) * z * ((d + 2) * z - 3) ** 2 / (6 * (d - 1)),
        d * (d + 4) * (1 - z) * ((d + 2) * z - 1) ** 2 / (2 * (d - 1) * (d + 1)),
        d * (d + 2) * (d + 4) * z * (1 - z) ** 2 / ((d - 1) * (d + 1)),
        d * (d + 2) * (d + 4) * (1 - z) ** 3 / ((d - 1) * (d + 1) * (d + 3)),
    )


class Interval:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def make(x):
        return x if isinstance(x, Interval) else Interval(x)

    def __add__(self, other):
        other = Interval.make(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-Interval.make(other))

    def __rsub__(self, other):
        return Interval.make(other) - self

    def __mul__(self, other):
        other = Interval.make(other)
        vals = (self.lo * other.lo, self.lo * other.hi,
                self.hi * other.lo, self.hi * other.hi)
        return Interval(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Interval.make(other)
        assert other.lo > 0 or other.hi < 0
        return self * Interval(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return Interval.make(other) / self

    def __pow__(self, k):
        assert k in (2, 3)
        if k == 2:
            if self.lo <= 0 <= self.hi:
                return Interval(0, max(self.lo * self.lo, self.hi * self.hi))
            return Interval(min(self.lo * self.lo, self.hi * self.hi),
                            max(self.lo * self.lo, self.hi * self.hi))
        return Interval(self.lo ** 3, self.hi ** 3)


def interval_eig(d, x):
    d, x = F(d), Interval.make(x)
    z = x / (d + 2)
    return (
        d * (d + 4) * z * ((d + 2) * z - 3) ** 2 / (6 * (d - 1)),
        d * (d + 4) * (1 - z) * ((d + 2) * z - 1) ** 2 / (2 * (d - 1) * (d + 1)),
        d * (d + 2) * (d + 4) * z * (1 - z) ** 2 / ((d - 1) * (d + 1)),
        d * (d + 2) * (d + 4) * (1 - z) ** 3 / ((d - 1) * (d + 1) * (d + 3)),
    )


def isolate_crossing(d, i, j, a, b, steps=55):
    a, b = F(a), F(b)
    va = eig(d, a)[i] - eig(d, a)[j]
    vb = eig(d, b)[i] - eig(d, b)[j]
    assert va * vb < 0, (d, i, j, a, b)
    for _ in range(steps):
        m = (a + b) / 2
        vm = eig(d, m)[i] - eig(d, m)[j]
        if vm == 0:
            a, b = m, m
            break
        if (vm > 0) == (va > 0):
            a, va = m, vm
        else:
            b, vb = m, vm
    return Interval(a, b)


# Rational data: each token represents its numerator divided by 100000.
# Entries (d, barrier, winning witness, inner split, middle split, outer split).
# Dash denotes the winning interval, for which no competitor split is needed.
FIN = [
 (3, F(61,100),  27682, None, 182085, 327884),
 (4, F(14,25),  189564, 27526, None, 338774),
 (5, F(53,100), 193236, 27416, None, 347455),
 (6, F(1,2),    192458, 27335, None, 354493),
 (7, F(12,25), 191898, 27273, None, 360299),
 (8, F(9,20),  191475, 27223, None, 365164),
 (9, F(9,20),  191144, 27183, None, 369297),
 (10,F(23,50), 190877, 27150, None, 372850),
 (11,F(47,100),190659, 27122, None, 375936),
]


def fcheck():
    count = 0
    for d, barrier, witness, inner, middle, outer in FIN:
        witness = F(witness, 100000)
        assert min(eig(d, witness)) > barrier
        count += 1
        if inner is not None:
            x = F(inner, 100000)
            assert max(eig(d,x)[1], eig(d,x)[2]) < barrier
            count += 1
        if middle is not None:
            x = F(middle, 100000)
            assert max(eig(d,x)[1], eig(d,x)[3]) < barrier
            count += 1
        if outer is not None:
            x = F(outer, 100000)
            assert max(eig(d,x)[0], eig(d,x)[3]) < barrier
            count += 1
        # Winning pair and its unique root interval. Monotonicity proves global
        # optimality within that segment once other branches clear the root.
        if d == 3:
            pair, a, b = (1, 2), 0, 1
        elif d == 4:
            pair, a, b = (1, 3), 1, 3
        else:
            pair, a, b = (0, 1), 1, 3
        root = isolate_crossing(d, *pair, a, b)
        bands = interval_eig(d, root)
        for j in range(4):
            if j not in pair:
                assert (bands[j] - bands[pair[0]]).lo > 0, (d,j)
                count += 1
        # Check the winning interval includes the crossing, whose main branch
        # is larger than the declared strict separator.
        assert bands[pair[0]].lo > barrier
        count += 1

    # Universal high-dimensional inequalities: d >= 12, y=d-12 >= 0.
    # Numerators of lambda_0(x(d))-12/25 and lambda_3(x(d))-12/25
    # after clearing positive denominators, in INCREASING powers of y.
    poly0 = [4017216,6513472,1811488,203952,10368,198]
    poly3 = [668965248,4183074336,2165026584,496258476,
             63704774,4920659,228285,5885,65]
    assert all(c > 0 for c in poly0 + poly3)
    count += len(poly0) + len(poly3)

    # Exact identities for rational functions, via polynomial identity checks:
    # each numerator has degree <= 5 / <= 8, so checking 6 / 9 distinct
    # integer values proves the identities for all d (after clearing
    # positive denominators).
    for d in range(12, 21):
        y = d - 12
        x = F(7*(3*d+2), 5*(d+2))
        l = eig(d,x)
        q0 = sum(c*y**k for k,c in enumerate(poly0))
        q3 = sum(c*y**k for k,c in enumerate(poly3))
        assert (l[0]-F(12,25))*375*(d-1)*(d+2)**4 == q0
        assert (l[3]-F(12,25))*125*(d-1)*(d+1)*(d+2)**5*(d+3) == q3
        count += 2
    # Remaining upper bounds, valid for all real d>=12, are proved by
    # monotonic rational factors and two positive shifted polynomials:
    # 12/25 - lambda_0(19/10) has numerator 581y^2+7628y+2112;
    # 12/25 - lambda_1(19/10) has numerator
    # 150y^3+3999y^2+29892y+40128.
    p_middle0 = [2112,7628,581]
    p_middle1 = [40128,29892,3999,150]
    assert all(c>0 for c in p_middle0 + p_middle1)
    count += len(p_middle0) + len(p_middle1)
    for d in range(12, 16):
        y=d-12
        l=eig(d,F(19,10))
        assert (F(12,25)-l[0])*6000*(d-1)*(d+2) == sum(c*y**k for k,c in enumerate(p_middle0))
        assert (F(12,25)-l[1])*2000*(d-1)*(d+1)*(d+2) == sum(c*y**k for k,c in enumerate(p_middle1))
        count += 2
    for d in range(12, 45):
        x=F(7*(3*d+2), 5*(d+2))
        assert min(eig(d,x)) > F(12,25)
        root=isolate_crossing(d,0,3,3,5)
        bands=interval_eig(d,root)
        assert (bands[1]-bands[0]).lo>0
        assert (bands[2]-bands[0]).lo>0
        count += 3
    return count

if __name__ == '__main__':
    n=fcheck()
    print('CUBIC_LATITUDE_RATIONAL_CERTIFICATE_PASS', n)
