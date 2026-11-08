"""Exact-rational checks of two exponential-step curvature-transport kernels.

Uses only Python's standard library. This verifies polynomial instances;
continuous-function generality follows from the proof in RESULT.md.
"""
from fractions import Fraction as F
from math import factorial
from itertools import product


def moments(coeffs, eta):
    # E[p(S)] where S has exponential mean eta.
    return sum((c * factorial(k) * eta**k for k, c in enumerate(coeffs)), F(0))


def square(p):
    a = [F(0)] * (2 * len(p) - 1)
    for i, c in enumerate(p):
        for j, d in enumerate(p):
            a[i + j] += c*d
    return a


def error_coeffs(h, eta):
    # delta=eta*h(S)+(S-eta)*h(0); D=int_0^S h(t)dt.
    e = [F(0)] * (len(h) + 1)
    for j in range(1, len(h)):
        e[j] += eta*h[j]
        e[j + 1] -= h[j] / (j + 1)
    return e


def endpoint_kernel(h, eta):
    # E error^2 = eta^2 int int e^{-max(u,v)/eta} h'(u) h'(v) du dv.
    deriv = [(i + 1) * h[i+1] for i in range(len(h) - 1)]
    return eta**2 * sum(
        deriv[i]*deriv[j]*factorial(i+j+1)*eta**(i+j+2)
        *(F(1, i+1) + F(1, j+1))
        for i in range(len(deriv)) for j in range(len(deriv))
    )


def uniform_kernel(h, eta):
    # E error^2 = eta int int min(u,v)e^{-max(u,v)/eta} h'(u)h'(v) du dv.
    # For u>=v: int_0^u v^{j+1}dv = u^{j+2}/(j+2).
    deriv = [(i + 1) * h[i+1] for i in range(len(h) - 1)]
    return eta * sum(
        deriv[i]*deriv[j]*factorial(i+j+2)*eta**(i+j+3)
        *(F(1, i+2) + F(1, j+2))
        for i in range(len(deriv)) for j in range(len(deriv))
    )


def uniform_direct(h, eta):
    # E[S^2 h(US)^2] - E[(int_0^S h)^2].
    # Conditional on S, U uniform, E_U[S^2 h(US)^2]=S int_0^S h(t)^2 dt.
    sq = square(h)
    term1 = [F(0)]*(len(sq)+2)
    for k,c in enumerate(sq):term1[k+2] += c/(k+1)
    D = [F(0)]*(len(h)+1)
    for k,c in enumerate(h):D[k+1]=c/(k+1)
    return moments(term1,eta)-moments(square(D),eta)

n = 0
for eta in [F(1,5),F(1,2),F(1),F(3,2),F(3)]:
  for degree in range(0,5):
   for coeffs in product([F(-2),F(-1,3),F(0),F(1,2),F(2)], repeat=degree+1):
    h = list(coeffs)
    ep = error_coeffs(h,eta)
    assert moments(ep,eta) == 0
    direct = moments(square(ep),eta)
    kern = endpoint_kernel(h,eta)
    assert direct == kern, (eta,h,direct,kern)
    uq = uniform_kernel(h,eta)
    ud = uniform_direct(h,eta)
    assert uq == ud, (eta,h,uq,ud)
    assert direct >= 0 and uq >= 0
    if len(h)==1:
     # The endpoint-corrected estimator and uniform path rule are quadratic exact.
     assert direct==uq==0
    if len(h)==2:
     # Sharp coincidence on affine Hessian paths: both MSEs 2*L^2*eta^4.
     assert direct==uq==2*h[1]**2*eta**4
    n += 1
print(f'PASS: {n} exact-rational polynomial configurations (five exponential means; all degrees 0..4).')
