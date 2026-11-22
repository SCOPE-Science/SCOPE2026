"""Standalone exact and floating-point checks for a quadratic-source retention cascade.

Standard library only. Polynomial and rational checks are exact; numerical samples
are diagnostic and do not establish universal assertions.
"""
from fractions import Fraction as F
from math import cos, sin, pi, sqrt


def add(a, b):
    v = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a): v[i] += x
    for i, x in enumerate(b): v[i] += x
    return strip(v)


def neg(a): return [-x for x in a]


def mul(a, b):
    v = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): v[i+j] += x*y
    return strip(v)


def strip(a):
    while len(a) > 1 and not a[-1]: a.pop()
    return a


def powpoly(a, n):
    p = [F(1)]
    for _ in range(n): p = mul(p, a)
    return p


def derivative(a): return [F(i)*a[i] for i in range(1, len(a))] or [F(0)]


def evaluate(a, x):
    y = F(0)
    for c in reversed(a): y = x*y + c
    return y


ONE = [F(1)]
X = [F(0), F(1)]
P = mul([F(3), F(-1)], powpoly([F(1), F(4)], 3))
Q = mul([F(-3), F(4)], powpoly([F(1), F(1)], 3))
# G'(x) = (P'Q-PQ')/Q^2; cross-multiply the claimed formula exactly.
NUM = add(mul(derivative(P), Q), neg(mul(P, derivative(Q))))
CLAIM = mul([F(-18)], mul(powpoly([F(1), F(4)], 2), [F(5), F(-5), F(4)]))
DEN_CANCEL = mul(powpoly([F(1), F(1)], 2), ONE)
assert NUM == mul(CLAIM, DEN_CANCEL), (NUM, CLAIM)

# Quartic threshold equations, cleared of the constant 1/2 factor.
left = add(mul([F(2)], P), neg(Q))
right = add(mul([F(-2)], P), neg(Q))
assert left == [F(9), F(75), F(261), F(279), F(-132)]
# Exact independent polynomial forms (both are negative or positive scalar multiples).
assert left == mul([F(-3)], [F(-3), F(-25), F(-87), F(-93), F(44)])
assert right == [F(-3), F(-65), F(-267), F(-297), F(124)]

# Rational brackets are independently verified by sign changes; uniqueness is analytic.
la, lb = F(2873444, 1000000), F(2873445, 1000000)
ra, rb = F(3135890, 1000000), F(3135891, 1000000)
assert evaluate(left, la) * evaluate(left, lb) < 0
assert evaluate(right, ra) * evaluate(right, rb) < 0
assert F(3,4) < la < lb < 3 < ra < rb

# Directly compare transfer coefficients with the closed formulas.
def transfer(stage_rates, w):
    h = complex(1)
    for rate in stage_rates: h *= rate / complex(rate, w)
    return h

for x in (F(1,4), F(3,4), F(1), F(2), F(3), F(4), F(9)):
    w = sqrt(float(x))
    assert abs(-transfer([1.,1.,1.],w).imag - (w*(3-float(x))/(1+float(x))**3)) < 1e-13
    assert abs(-transfer([1.,1.,1.],2*w).imag - (2*w*(3-4*float(x))/(1+4*float(x))**3)) < 1e-13

# Numerical crossing signs: q=2, amplitude=1, x=3.
q, eps, w = 2., 1., sqrt(3.)
H1, H2 = transfer([1.,1.,1.], w), transfer([1.,1.,1.], 2*w)
A, B = 2*q*eps*H1.real, -2*q*eps*H1.imag
D, E = eps*eps*H2.real/2, -eps*eps*H2.imag/2
assert abs(B) < 1e-13
assert abs(E + 9*sqrt(3.)/2197) < 1e-13

def output(t): return q*q+eps*eps/2+A*cos(t)+B*sin(t)+D*cos(2*t)+E*sin(2*t)

for t in (pi/6, pi/4, pi/3):
    difference = output(t)-output(2*pi-t)
    assert abs(difference-2*sin(t)*(B+2*E*cos(t))) < 1e-12
    assert difference < 0
    t2 = pi-t
    difference2 = output(t2)-output(2*pi-t2)
    assert difference2 > 0
assert abs(output(pi/2)-output(3*pi/2)) < 1e-12
assert abs(4*eps*abs(E)/3 - 12*sqrt(3.)*eps**3/2197) < 1e-14

print('PASS: exact polynomial identities, rational root brackets, transfer phases, crossing and area diagnostics')
print('certified rational brackets:', (str(la), str(lb)), (str(ra), str(rb)))
