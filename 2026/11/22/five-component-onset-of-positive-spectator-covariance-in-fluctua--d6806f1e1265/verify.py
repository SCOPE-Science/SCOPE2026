"""Exact rational enclosures for Gaussian minimum-covariance constants.

This independently checks the orthant-integral signs in the theorem.
Uses only the Python standard library; no floating point is used in the certificate.
"""
from fractions import Fraction as F
from math import comb


def plus(a, b):
    return (a[0] + b[0], a[1] + b[1])

def minus(a, b):
    return (a[0] - b[1], a[1] - b[0])

def times(a, b):
    vals = [x*y for x in a for y in b]
    return (min(vals), max(vals))

def inv(a):
    assert a[0] > 0
    return (1/a[1], 1/a[0])

def divide(a, b):
    return times(a, inv(b))

def const(x):
    return (F(x), F(x))

def arctan_interval(x, n=18):
    assert 0 < x < 1
    s = sum(((-1)**j) * x**(2*j+1) / (2*j+1) for j in range(n))
    next_term = x**(2*n+1)/F(2*n+1)
    return (s, s+next_term) if n%2 == 0 else (s-next_term, s)


def arcsin_interval(x, n=16):
    assert 0 < x <= F(1, 3)
    terms = [F(comb(2*k,k), 4**k*(2*k+1))*x**(2*k+1) for k in range(n+1)]
    s = sum(terms[:-1]); remainder = terms[-1]/(1-x*x)
    return (s, s+remainder)

p1 = arctan_interval(F(1,5)); p2 = arctan_interval(F(1,239))
PI = minus(times(const(16),p1), times(const(4),p2))
ROOT_PI = (F(1772453850905, 10**12), F(1772453850907, 10**12))
ROOT_3 = (F(1732050807568, 10**12), F(1732050807570, 10**12))
assert ROOT_PI[0]**2 < PI[0] < PI[1] < ROOT_PI[1]**2
assert ROOT_3[0]**2 < 3 < ROOT_3[1]**2
A = arcsin_interval(F(1,3)); B = arcsin_interval(F(1,4))


def ortho(k, arcs):
    if k == 0: return const(1)
    if k == 1: return const(F(1,2))
    if k == 2: return plus(const(F(1,4)),divide(arcs, times(const(2),PI)))
    if k == 3: return plus(const(F(1,8)),divide(times(const(3),arcs), times(const(4),PI)))
    raise ValueError(k)


def bound_c(m):
    # E min(Z_1,...,Z_m)=-m(m-1)/(2 sqrt(pi))*P_{m-2}(rho=1/3).
    mu_abs = divide(times(const(F(m*(m-1),2)), ortho(m-2,A)),ROOT_PI)
    # E min^2 =1 + m(m-1)(m-2)/(4 pi sqrt(3))*P_{m-3}(rho=1/4)
    if m == 2: nu=const(1)
    else:
        coeff=divide(const(F(m*(m-1)*(m-2),4)),times(PI,ROOT_3))
        nu=plus(const(1),times(coeff,ortho(m-3,B)))
    return minus(minus(nu,times(mu_abs,mu_abs)), const(F(2,m)))

for m in (2,3,4,5):
    bounds=bound_c(m)
    label='POSITIVE' if bounds[0] > 0 else ('NEGATIVE' if bounds[1] < 0 else 'INCONCLUSIVE')
    assert label != 'INCONCLUSIVE'
    print(f'm={m} Gaussian scaled residual covariance {label}; '
          f'certified interval [{float(bounds[0]):.12f}, {float(bounds[1]):.12f}]')
assert bound_c(4)[1] < 0 < bound_c(5)[0]
print('All rational interval signs proved, including sharp high-loading 4-to-5 crossover.')
