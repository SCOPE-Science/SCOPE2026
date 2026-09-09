"""Exact rational interval arithmetic (stdlib only, outward rounding)."""
from fractions import Fraction as F


class I:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        lo = lo if isinstance(lo, F) else F(lo)
        hi = lo if hi is None else (hi if isinstance(hi, F) else F(hi))
        assert lo <= hi, (lo, hi)
        self.lo = lo
        self.hi = hi

    def __repr__(self):
        return f"[{self.lo}, {self.hi}]"

    def __add__(self, o):
        o = _c(o)
        return I(self.lo + o.lo, self.hi + o.hi)

    def __radd__(self, o):
        return self + o

    def __sub__(self, o):
        o = _c(o)
        return I(self.lo - o.hi, self.hi - o.lo)

    def __rsub__(self, o):
        return _c(o) - self

    def __mul__(self, o):
        o = _c(o)
        ps = (self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi)
        return I(min(ps), max(ps))

    def __rmul__(self, o):
        return self * o

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __truediv__(self, o):
        o = _c(o)
        assert o.lo > 0 or o.hi < 0, "division by zero-containing interval"
        return self * I(F(1, 1) / o.hi, F(1, 1) / o.lo) if o.lo > 0 else \
            self * I(F(1, 1) / o.hi, F(1, 1) / o.lo)

    def __contains__(self, v):
        v = F(v)
        return self.lo <= v <= self.hi

    def mid(self):
        return (self.lo + self.hi) / 2

    def width(self):
        return self.hi - self.lo

    def subset(self, o):
        o = _c(o)
        return o.lo <= self.lo and self.hi <= o.hi


def _c(o):
    return o if isinstance(o, I) else I(o)


def ipow(a, n):
    """a^n for integer n>=0."""
    assert isinstance(n, int) and n >= 0
    r = I(1)
    for _ in range(n):
        r = r * a
    return r


def isqrt(a, tol=F(1, 10**12)):
    """Enclosure of sqrt over interval a (a.lo >= 0)."""
    assert a.lo >= 0
    import math
    lo, hi = a.lo, a.hi
    # float guesses, then rational verify + bisect
    gl = F(math.sqrt(float(lo)) if lo > 0 else 0)
    # push gl down until gl^2 <= lo
    while gl * gl > lo:
        gl = gl - F(1, 10**9) if gl > 0 else F(0)
        if gl < 0:
            gl = F(0)
            break
    gh = F(math.sqrt(float(hi)) if hi > 0 else 0) + F(1, 10**9)
    while gh * gh < hi:
        gh = gh + F(1, 10**9)
    # bisect: shrink [gl,gh] keeping gl^2<=lo<=... and gh^2>=hi
    # want gl^2 <= lo and gh^2 >= hi; narrow gap
    while gh - gl > tol:
        m = (gl + gh) / 2
        # decide which side to keep: check m^2 vs lo and hi
        if m * m < lo:
            gl = m
        elif m * m > hi:
            gh = m
        else:
            # m^2 in [lo,hi]: keep both? narrow from the wider side
            # gl is valid lower (gl^2<=lo?), ensure invariant
            if not (gl * gl <= lo):
                gl = m  # fallback, shouldn't happen
            # shrink gh if gh^2 huge? just move gl up cautiously:
            # keep invariant gl^2<=lo, gh^2>=hi
            # try gl=m only if m^2<=lo (false here). try gh=m if m^2>=hi (false).
            break
    # final safety: enforce invariants
    while gl * gl > lo:
        gl -= tol
    while gh * gh < hi:
        gh += tol
    return I(gl, gh)


def e_const(n=12):
    """Enclosure of e = sum 1/k! with remainder <= 1/(n*n!)."""
    from math import factorial
    s = sum(F(1, factorial(k)) for k in range(n + 1))
    r = F(1, n * factorial(n))
    return I(s, s + r)


def exp_lower(t, n=40, etop=None):
    """Lower bound of e^t for rational t>=0: partial Taylor sum (all terms >=0)."""
    assert t >= 0
    s = F(0)
    term = F(1)
    for k in range(n + 1):
        if k > 0:
            term = term * t / k
        s += term
    return s


def exp_upper(t, n=40, etop=None):
    """Upper bound of e^t for rational t>=0 via Taylor + Lagrange remainder."""
    assert t >= 0
    from math import factorial
    s = exp_lower(t, n)
    if etop is None:
        etop = e_const().hi ** 8  # valid only if t <= 8
        assert t <= 8
    r = etop * (t ** (n + 1)) / F(factorial(n + 1))
    return s + r


def exp_interval(y, n=40):
    """Enclosure of e^y over interval y (requires y.hi <= 8)."""
    assert y.hi <= 8
    e8 = e_const().hi ** 8
    if y.lo >= 0:
        return I(exp_lower(y.lo, n, e8), exp_upper(y.hi, n, e8))
    elif y.hi <= 0:
        # e^y = 1/e^{-y}
        en = I(exp_lower(-y.hi, n, e8), exp_upper(-y.lo, n, e8))
        return I(F(1) / en.hi, F(1) / en.lo)
    else:
        lo = I(exp_lower(-y.lo, n, e8), exp_upper(-y.lo, n, e8))
        return I(F(1) / lo.hi, exp_upper(y.hi, n, e8))


def atan_interval(b, K=10):
    """Enclosure of arctan(b) for rational 0<b<1 via alternating series, error<=first omitted."""
    assert F(0) < b < 1
    s = F(0)
    for k in range(K + 1):
        s += ((-1) ** k) * (b ** (2 * k + 1)) / (2 * k + 1)
    e = (b ** (2 * (K + 1) + 1)) / (2 * (K + 1) + 1)
    return I(s - e, s + e)


def pi_interval(K=10):
    """Machin: pi = 16 arctan(1/5) - 4 arctan(1/239)."""
    a = atan_interval(F(1, 5), K)
    b = atan_interval(F(1, 239), K)
    return I(16) * a - I(4) * b
