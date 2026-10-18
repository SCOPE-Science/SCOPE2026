"""Exact rational verification of a convex-map counterexample.

Requires Python 3 standard library only; no floating-point arithmetic.
"""
from fractions import Fraction as F


class QI:
    """Pair of rational real and imaginary parts."""
    def __init__(self, re=0, im=0):
        self.re, self.im = F(re), F(im)

    @staticmethod
    def coerce(other):
        return other if isinstance(other, QI) else QI(other)

    def __add__(self, other):
        other = self.coerce(other)
        return QI(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return QI(-self.re, -self.im)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return QI(self.re * other.re - self.im * other.im,
                  self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        d = other.re * other.re + other.im * other.im
        assert d != 0, 'division by zero'
        return QI((self.re * other.re + self.im * other.im) / d,
                  (self.im * other.re - self.re * other.im) / d)

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def __pow__(self, power):
        assert isinstance(power, int) and power >= 0
        result, base = QI(1), self
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power >>= 1
        return result

    def abs2(self):
        return self.re**2 + self.im**2

    def __eq__(self, other):
        other = self.coerce(other)
        return self.re == other.re and self.im == other.im


T = QI(F(29, 54), -F(29, 54) * F(99999, 100000))
z = (T**2 - 1) / (T**2 + 1)
assert T.re > abs(T.im)
assert z.abs2() < 1

# Branch identity: sqrt((1+z)/(1-z)) = T (positive real part).
assert (1 + z) / (1 - z) == T**2

# For f(z) = sqrt((1+z)/(1-z)) - 1, these are
# A = z*f'(z)/f(z), P = 1 + z*f''(z)/f'(z).
A = (T + 1) * (T**2 + 1) / (4*T)
P = (3*T**4 + 1) / (4*T**2)

# Independent rational identities using derivatives with respect to z.
fz = (T**2 + 1)**2 / (4*T)
assert A == z * fz / (T - 1)
assert P == 1 + z * (1 + 2*z) / (1 - z**2)
assert P.re > 0
assert (1 + A).re > 0

# h_alpha[f] at alpha=1/2, using the original definition.
alpha = F(1, 2)
h_original = (alpha * (1 - alpha) * A**2
              + (2*alpha**2 - alpha)*A
              + (1-alpha)*(alpha + P)) / (P * (1-alpha + alpha*A))
h_simplified = (A**2 + 1 + 2*P) / (2*P*(1 + A))
assert h_original == h_simplified
assert -F(1, 2) < h_original.re < -F(1, 4)
print('Exact-rational counterexample verification: PASS')
print('z =', z.re, '+ i *', z.im)
print('abs(z)^2 =', z.abs2())
print('Re h_1/2(z) =', h_original.re)
print('Rigorous interval: -1/2 < Re h_1/2(z) < -1/4')
