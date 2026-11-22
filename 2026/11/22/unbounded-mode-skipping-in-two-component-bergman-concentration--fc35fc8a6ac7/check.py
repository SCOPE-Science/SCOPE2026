"""Standalone supplementary exact and high-precision checks for two-shell Bergman localization."""
from fractions import Fraction as F
from decimal import Decimal, localcontext

b, c = F(3, 4), F(7, 8)
mu = lambda n: c ** (n + 1) - b ** (n + 1)
d = mu(4) - mu(0)
assert mu(4) == F(9031, 32768)
assert mu(0) == F(1, 8)
assert d == F(4935, 32768)
lo, hi = F(3, 20), F(151, 1000)
H = lambda a: a - a ** 5
assert H(lo) < d < H(hi)
for n in range(1, 4):
    assert lo - lo ** (n + 1) > mu(n) - mu(0)
    assert mu(n) < mu(4)
    assert (n + 1) * hi ** n - 5 * hi ** 4 > 0
for n in range(0, 4):
    assert mu(n + 1) > mu(n)
for n in range(4, 200):
    assert mu(n + 1) < mu(n)
for n in range(5, 200):
    assert mu(n) < mu(4)
assert H(F(3, 4)) > d

with localcontext() as ctx:
    ctx.prec = 65
    one = Decimal(1)
    logtwo = Decimal(2).ln()
    for M in (10, 20, 40, 80, 160):
        R = (logtwo / (Decimal(M) + Decimal('0.5'))).exp()
        h = (R - one) / (2 * R - one)
        bout, cout = one - 2 * h, one - h
        m = lambda n: cout ** (n + 1) - bout ** (n + 1)
        target = m(M) - h
        low, high = Decimal(0), one / 3
        for _ in range(230):
            mid = (low + high) / 2
            if mid - mid ** (M + 1) < target:
                low = mid
            else:
                high = mid
        a = (low + high) / 2
        val = lambda n: a ** (n + 1) + m(n)
        assert abs(val(0) - val(M)) < Decimal('1e-60')
        assert val(M) > max(val(n) for n in range(1, 5 * M) if n != M)
        assert m(M) > m(M - 1) and m(M) > m(M + 1)
print('PASS: rational exact certificate and five high-precision illustrative cases')
