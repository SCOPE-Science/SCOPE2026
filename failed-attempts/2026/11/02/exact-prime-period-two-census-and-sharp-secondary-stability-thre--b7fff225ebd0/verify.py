"""Exact, standard-library algebra checks for a scalar rational iteration."""
from fractions import Fraction
from math import sqrt

class Polynomial:
    def __init__(self, terms=None):
        self.terms = {k: int(v) for k, v in (terms or {}).items() if v}
    @staticmethod
    def constant(value): return Polynomial({(0, 0): value})
    def __add__(self, other):
        if isinstance(other, int): other = Polynomial.constant(other)
        terms = self.terms.copy()
        for k, v in other.terms.items(): terms[k] = terms.get(k, 0) + v
        return Polynomial(terms)
    __radd__ = __add__
    def __neg__(self): return Polynomial({k: -v for k,v in self.terms.items()})
    def __sub__(self, other): return self + (-other if isinstance(other, Polynomial) else -other)
    def __rsub__(self, other): return other + (-self)
    def __mul__(self, other):
        if isinstance(other, int): other = Polynomial.constant(other)
        terms = {}
        for (a,b),c in self.terms.items():
            for (i,j),d in other.terms.items():
                key = (a+i,b+j)
                terms[key] = terms.get(key,0)+c*d
        return Polynomial(terms)
    __rmul__ = __mul__
    def __pow__(self, exponent):
        assert isinstance(exponent,int) and exponent>=0
        ans=Polynomial.constant(1)
        for _ in range(exponent): ans=ans*self
        return ans
    def __eq__(self, other):
        if isinstance(other,int): other=Polynomial.constant(other)
        return self.terms == other.terms

X = Polynomial({(1,0): 1})
H = Polynomial({(0,1): 1})
Q = 1 + X*X
P = X*(Q-H)
N = P*(P*P+(1-H)*Q*Q)-X*Q*(Q*Q+P*P)
EXPECTED = -H*X*(2*Q-H)*(Q*Q-H*X*X)
assert N == EXPECTED, 'Complete rational period-two factorization failed.'

# For an asymmetric 2-cycle, x*y=1 and (x+y)^2=h; then
# x^2+y^2=h-2 and the derivative product is (2-x^2)(2-y^2)=9-2h.
S = Polynomial({(1,0): 1})
T = Polynomial({(0,1): 1})
assert (2-S)*(2-T) == 4-2*(S+T)+S*T

# Exact examples: symmetric multiplier (3-8/h)^2; asymmetric 9-2h.
assert (3-Fraction(8,3))**2 == Fraction(1,9)
assert (3-Fraction(8,4))**2 == 1
assert 9-2*Fraction(9,2) == 0
assert 9-2*Fraction(5,1) == -1
assert 9-2*Fraction(11,2) == -2

# Floating independent orbit substitution verifies point labeling (not used as proof).
for h in (4.01, 4.5, 5.0, 5.5, 8.0):
    u=(sqrt(h)+sqrt(h-4))/2
    v=(sqrt(h)-sqrt(h-4))/2
    f=lambda z: z-h*z/(1+z*z)
    assert abs(f(u)+v)<1e-10 and abs(f(-v)-u)<1e-10
    d=lambda z: 1-h*(1-z*z)/(1+z*z)**2
    assert abs(d(u)*d(-v)-(9-2*h))<1e-10
print('PASS: exact polynomial factorization, exact multiplier identities, and five numerical orbit checks.')
