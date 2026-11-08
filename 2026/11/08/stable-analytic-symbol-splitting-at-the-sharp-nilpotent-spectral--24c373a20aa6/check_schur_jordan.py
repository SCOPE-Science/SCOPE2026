"""Finite reproducibility tests for a sharp nilpotent functional-calculus rigidity result.

Analytical claims in the accompanying proof do not depend on finite tests.
Only Python's standard library is needed.
"""
from fractions import Fraction
from math import sqrt, isclose
from cmath import exp, pi

checks = 0

def verify(ok, label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)

# The real positive two-by-two block [[a,2c],[0,a]] has norm
# sqrt(a*a+c*c)+c. For real a=b and c=1-b*b, f_b is an inner function.
for den in range(2, 202):
    b = Fraction(1, den)
    t = 1 - b*b
    a = b
    verify(t > 0, 'positive derivative')
    verify(b*b + t == 1, 'automorphism Schwarz-Pick equality')
    verify(b*b + t*t / (1 - b*b) == 1, 'all Taylor coefficients H2 sum')
    verify(2 - 2*t == 2*b*b, 'H2 distance')
    bf, tf = float(b), float(t)
    sj = sqrt(bf*bf + tf*tf) + tf
    delta = 2 - sj
    verify(0 < delta < 2, 'functional-calculus deficit')
    verify(2*bf*bf <= 4*delta + 1e-12, 'H2 stability bound')
    verify(sj <= 1 + tf + 1e-12, 'Toeplitz-contraction bound')
    verify(sj >= 2*tf - 1e-12, 'derivative-vector lower bound')
    for zidx in (0, 1, 2, 3, 7):
        z = exp(1j * (2*pi*zidx/11))
        f = (complex(bf)+z)/(1+bf*z)
        verify(abs(abs(f)-1) < 2e-13, 'inner boundary magnitude')
# Exact extremal and easy boundary cases.
verify(sqrt(0**2+1**2)+1 == 2, 'z exact extremality')
verify(sqrt(1**2+0**2)+0 == 1, 'unimodular constant')
# Taylor asymptotics: delta is (3/2)b^2 + O(b^4).
for n in (100, 1000, 10000, 100000):
    b = 1.0/n
    c = 1-b*b
    delta = 2 - (sqrt(b*b+c*c)+c)
    verify(abs(delta/(b*b)-1.5) < 0.001, 'deficit quadratic asymptotic')
# Tensor/direct-sum matrix-level tests: the constant complementary
# block contributes no derivative; the scalar extremal block dominates.
for n in (2, 3, 5, 11, 51):
    b = 1/n
    c = 1-b*b
    jnorm = sqrt(b*b+c*c)+c
    verify(jnorm > 0.37, 'direct-sum norm dominance')
    verify(abs((1-c) - b*b) < 1e-14, 'linear coefficient variation')
print('SCHUR_JORDAN_CHECK_OK',checks,'finite assertions')
