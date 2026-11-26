"""Exact rational verification for fixed-degree cubic spherical cap concentration."""
from fractions import Fraction as F
from math import isclose


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def plus(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def neg(a):
    return [-x for x in a]


def times(a, b):
    r = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return trim(r)


def product(*parts):
    p = [F(1)]
    for x in parts:
        p = times(p, x)
    return p


def scale(a, c):
    return trim([x * c for x in a])


def derivative(a):
    return trim([i * a[i] for i in range(1, len(a))] or [F(0)])


def antiderivative(a):
    return [F(0)] + [a[i] / F(i + 1) for i in range(len(a))]


def at(a, x):
    r = 0
    for c in reversed(a):
        r = r * x + c
    return r


def restrict_at_square(a, c):
    # Image under Q[t]/(t^2-c), represented as constant + coefficient*t.
    b = [F(0), F(0)]
    for i, v in enumerate(a):
        b[i % 2] += v * c ** (i // 2)
    return b


x = [F(0), F(1)]
u = [F(1), F(0), F(-1)]
a = [F(-1), F(0), F(5)]
b = [F(-3), F(0), F(5)]
c = [F(1), F(0), F(5)]
d = [F(5), F(0), F(-12), F(0), F(15)]
P3 = [F(0), F(-3, 2), F(0), F(5, 2)]
expected = [
    [F(1),0,0,F(-21,4),0,F(21,2),0,F(-25,4)],
    [F(1),F(-21,16),0,F(77,16),0,F(-147,16),0,F(75,16)],
    [F(1),0,0,F(-35,8),0,F(21,4),0,F(-15,8)],
    [F(1),F(-35,16),0,F(35,16),0,F(-21,16),0,F(5,16)],
]

lambdas = []
for m in range(4):
    deriv = P3
    for i in range(m):
        deriv = derivative(deriv)
    density = product(*([u] * m + [deriv, deriv]))
    integ = antiderivative(density)
    z = at(integ, F(1))
    assert z > 0
    lam = scale(plus([z], neg(integ)), F(1) / z)
    assert lam == trim(expected[m]), (m, lam)
    lambdas.append(lam)
print('ALL_FOUR_EXACT_LEGENDRE_CAP_EIGENPOLYNOMIALS_OK')

factors = {
    (0,1): scale(product(x,u,a,b), F(7,16)),
    (0,2): scale(product(x,x,x,u,a), F(7,8)),
    (0,3): scale(product(x,u,d), F(7,16)),
    (1,2): scale(product(x,u,u,a), F(21,16)),
    (1,3): scale(product(x,u,u,c), F(7,8)),
    (2,3): scale(product(x,u,u,u), F(35,16)),
}
for (i,j), fac in factors.items():
    assert trim(plus(lambdas[i], neg(lambdas[j]))) == trim(fac), (i,j)
assert plus(lambdas[0], scale(plus(plus(lambdas[1],lambdas[2]),lambdas[3]),2)) == [F(7),F(-7)]
print('SIX_GAP_FACTORIZATIONS_AND_SEVEN_DIMENSIONAL_TRACE_OK')

root1 = F(1,5)
root2 = F(3,5)
red1 = [restrict_at_square(p,root1) for p in lambdas]
red2 = [restrict_at_square(p,root2) for p in lambdas]
assert red1[0] == red1[1] == red1[2] == [F(1),F(-17,25)]
assert red1[3] == [F(1),F(-9,5)]
assert red2[0] == red2[1] == [F(1),F(-18,25)]
assert red2[2] == [F(1),F(-57,50)]
assert red2[3] == [F(1),F(-32,25)]
print('EXACT_FIVE_DIMENSIONAL_AND_THREE_DIMENSIONAL_RESONANCES_OK')

# Exact sign testing at rational sample points in the open phases;
# the factorizations above prove the sign patterns throughout those phases.
for t, ordering in [
    (F(1,4), (2,0,1,3)),
    (F(1,2), (1,0,2,3)),
    (F(9,10), (0,1,2,3)),
]:
    v = [at(p,t) for p in lambdas]
    assert all(v[ordering[k]] > v[ordering[k+1]] for k in range(3))
    assert all(0 < v[k] < 1 for k in range(4))
print('THREE_STRICT_ORDERING_PHASES_AND_UNIVERSAL_MINIMUM_OK')

# Independent midpoint quadrature of the associated Legendre densities.
for t in (0.2,0.5,0.86):
    for m in range(4):
        deriv = P3
        for _ in range(m):
            deriv = derivative(deriv)
        def density(z):
            return (1-z*z)**m * at(deriv,z)**2
        steps=4000
        total0=sum(density((k+0.5)/steps) for k in range(steps))/steps
        total1=(1-t)*sum(density(t+(1-t)*(k+0.5)/steps) for k in range(steps))/steps
        assert isclose(total1/total0,float(at(lambdas[m],t)),abs_tol=3e-7), (m,t)
print('INDEPENDENT_NUMERIC_LEGENDRE_INTEGRATION_OK_12')
print('ALL_CUBIC_TWO_CAP_SPECTRAL_CHECKS_OK')
