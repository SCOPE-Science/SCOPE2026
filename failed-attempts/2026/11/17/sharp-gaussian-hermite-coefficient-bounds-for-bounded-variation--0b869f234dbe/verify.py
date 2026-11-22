"""Checks for sharp Gaussian Hermite coefficients of BV functions.

Requires only Python 3 standard library. All theorem assertions are separately
proved in RESULT.md; finite calculations here are diagnostic corroboration.
"""
from math import comb, exp, factorial, isclose, log, pi, sqrt


def he_integer(n):
    a, b = [1], [0, 1]
    if n == 0:
        return a
    if n == 1:
        return b
    for k in range(2, n + 1):
        c = [0] * (k + 1)
        for i, v in enumerate(b):
            c[i + 1] += v
        for i, v in enumerate(a):
            c[i] -= (k - 1) * v
        a, b = b, c
    return b


def derivative(a):
    return [i * a[i] for i in range(1, len(a))] or [0]


def poly_add(a, b):
    z = [0] * max(len(a), len(b))
    for i, v in enumerate(a): z[i] += v
    for i, v in enumerate(b): z[i] += v
    return z


def shift(a):
    return [0] + a


def scale(a, k):
    return [k * x for x in a]


for n in range(1, 31):
    p = he_integer(n - 1)
    q = he_integer(n)
    assert poly_add(derivative(p), scale(shift(p), -1)) == scale(q, -1)
    # y=phi*p, y'=-phi*q, y''=phi*(x*q-n*p).
    assert all(v == 0 for v in poly_add(scale(p, -n), derivative(q)))
    # Hermite derivative identity: q' = n*p.
    assert derivative(q) == scale(p, n)
print('EXACT_HERMITE_DIFFERENTIATION_IDENTITIES_PASS 30')


def h(n, x):
    if n == 0: return 1.0
    a, b = 1.0, x
    if n == 1: return b
    for k in range(2, n+1):
        a, b = b, x*b/sqrt(k)-sqrt((k-1)/k)*a
    return b


def bisect_root(n, lo, hi):
    fl = h(n, lo)
    fh = h(n, hi)
    assert fl*fh < 0
    for _ in range(65):
        mid = (lo + hi)/2
        if fl * h(n, mid) <= 0: hi = mid
        else:
            lo, fl = mid, h(n, mid)
    return (lo + hi)/2


def pos_roots(n):
    xmax = 2*sqrt(n) + 1
    step = 0.005
    a = 1e-9 if n % 2 else 0.0
    last = h(n, a)
    out = []
    num = int(xmax/step) + 1
    for j in range(1, num+1):
        b = j*step
        cur = h(n, b)
        if last * cur < 0:
            out.append(bisect_root(n, a, b))
        a, last = b, cur
    return out


def amplitude(n, t):
    return exp(-t*t/2)/sqrt(2*pi*n)*abs(h(n-1,t))


for n in range(1, 31):
    rs = pos_roots(n)
    assert len(rs) == n//2, (n, len(rs))
    options = ([0.0] if n%2 else []) + rs
    values = [amplitude(n,t) for t in options]
    assert values[0] == max(values), (n, values)
    assert all(values[i] > values[i+1] for i in range(len(values)-1))
    if n%2:
        k=(n-1)//2
        exact = sqrt(comb(2*k,k)/4**k)/(sqrt(2*pi*n))
        assert isclose(exact, values[0],rel_tol=3e-12)
    else:
        first=bisect_root(n,0,2/sqrt(n))
        assert abs(first-rs[0])<1e-10
        assert abs(h(n,first))<1e-11
print('ALL_POSITIVE_HERMITE_CRITICAL_ROOTS_AND_SHARP_STEPS_PASS 30')

K=2**(-0.25)*pi**(-0.75)
for n in [40,60,80,100,160,200,300]:
    if n%2:
        raise AssertionError('chosen degrees should be even')
    t=bisect_root(n,0,2/sqrt(n))
    norm=amplitude(n,t)
    approx=K*n**(-0.75)*(1-(pi*pi-2)/(16*n))
    assert abs(norm/approx-1)<0.3/n**2
    t_asym=(pi/2)/sqrt(n)-(pi/8)/n**1.5
    assert abs(t-t_asym)<0.6/n**2.5
for n in [41,61,81,101,161,201,301]:
    k=(n-1)//2
    norm=sqrt(comb(2*k,k)/4**k)/(sqrt(2*pi*n))
    approx=K*n**(-.75)*(1+1/(8*n))
    assert abs(norm/approx-1)<0.02/n**2
print('PARITY_CORRECTIONS_AND_FIRST_POSITIVE_ZERO_ASYMPTOTICS_PASS')
print('ALL_GAUSSIAN_BV_HERMITE_COEFFICIENT_CHECKS_PASS')
