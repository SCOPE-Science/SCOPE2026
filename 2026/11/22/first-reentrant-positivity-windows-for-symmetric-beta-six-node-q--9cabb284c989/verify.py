"""Exact coefficient and moment checks for six-node symmetric weighted quadrature.

No third-party packages required. Run: python verify.py
The sign classification for all real positive parameters is proved analytically
in RESULT.md, not inferred from finite sampling here.
"""
from fractions import Fraction as F
from math import comb


def add(p, q):
    return [((p[i] if i < len(p) else F(0)) +
             (q[i] if i < len(q) else F(0))) for i in range(max(len(p), len(q)))]


def mul(p, q):
    v = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            v[i + j] += a * b
    return v


def scale(p, c):
    return [c * i for i in p]


def lagrange(n, j):
    nodes = [F(k, n) for k in range(n + 1)]
    p, divisor = [F(1)], F(1)
    for k in range(n + 1):
        if k != j:
            p = mul(p, [-nodes[k], F(1)])
            divisor *= nodes[j] - nodes[k]
    return scale(p, F(1) / divisor)


def even_center_coeff(p):
    """Coefficients of even powers in L(1/2+z); symmetric average."""
    out = [F(0)] * (len(p) // 2 + 1)
    for k, c in enumerate(p):
        for m in range(k // 2 + 1):
            out[m] += c * comb(k, 2*m) * F(1, 2) ** (k - 2*m)
    while len(out)>1 and out[-1]==0:
        out.pop()
    return out


def evalp(p, x):
    return sum(v * x ** k for k, v in enumerate(p))


def moments_beta(a, order):
    """Raw moments E[X^k] for X ~ Beta(a,a), all exact rationals."""
    out = [F(1)]
    for k in range(1, order + 1):
        out.append(out[-1] * (a + k - 1) / (2*a + k - 1))
    return out


def weights_raw(n, a):
    mom = moments_beta(a, n)
    return [sum(c * mom[k] for k, c in enumerate(lagrange(n, j)))
            for j in range(n + 1)]


def beta_form(n, a):
    d = (2*a+1)*(2*a+3)
    if n == 1: return [F(1, 2)]*2
    if n == 2: return [1/(2*(2*a+1)), 2*a/(2*a+1), 1/(2*(2*a+1))]
    if n == 3:
        e, c = (4-a)/(8*(2*a+1)), 9*a/(8*(2*a+1))
        return [e,c,c,e]
    if n == 4:
        e, b, c = (9-2*a)/(6*d), 16*a/(3*d), 2*a*(2*a-1)/d
        return [e,b,c,b,e]
    if n == 5:
        e = (9*a*a-107*a+288)/(192*d)
        b = 25*a*(11-a)/(64*d)
        c = 25*a*(9*a+1)/(96*d)
        return [e,b,c,c,b,e]
    raise ValueError('supported panel counts 1 through 5')


# Full identities of even-centered Lagrange polynomials: no numerical fitting.
expected = [
    [F(9,768), F(-1000,768), F(10000,768)],
    [F(-25,256), F(25*104,256), F(-25*400,256)],
    [F(25*9,384), F(-25*136,384), F(25*400,384)]
]
for j in range(3):
    assert even_center_coeff(lagrange(5,j)) == expected[j]
    assert even_center_coeff(lagrange(5,5-j)) == expected[j]
assert [2*sum(expected[j][k] for j in range(3)) for k in range(3)] == [F(1), F(0), F(0)]

# Symbolic identities after clearing the common quadratic denominator.
# Polynomial coefficients indexed by powers of the Beta shape a.
D = [F(3), F(8), F(4)]       # (2a+1)(2a+3)
lin = [F(3),F(2)]          # (2a+3)
for j in range(3):
    p0,p1,p2=expected[j]
    recovered = add(add(scale(D,p0),scale(lin,p1/F(4))), [p2*F(3,16)])
    exact = [
        [F(288,192), F(-107,192), F(9,192)],
        [F(0),F(275,64),F(-25,64)],
        [F(0),F(25,96),F(225,96)]
    ][j]
    assert recovered == exact, (j,recovered,exact)

# Exact independently integrated beta moments (raw rising-factorial formula).
shapes = [F(1,10),F(1,2),F(1),F(2),F(4),F(9,2),F(5),F(6),F(8),F(9),F(11),F(12),F(30),F(100)]
count=0
for a in shapes:
    for n in range(1,6):
        w=weights_raw(n,a)
        assert w == beta_form(n,a), (n,a,w,beta_form(n,a))
        assert sum(w)==1
        # All monomials to exact interpolation degree (independent moment check)
        for k,m in enumerate(moments_beta(a,n)):
            assert sum(w[j]*F(j,n)**k for j in range(n+1))==m
            count+=1

# Rational witnesses on each side of the two distinct Beta sign changes.
for a, signs in [(F(1), (1,1,1)),(F(6),(-1,1,1)),
                 (F(9),(1,1,1)),(F(12),(1,-1,1))]:
    w=beta_form(5,a)
    got=tuple((v>0)-(v<0) for v in w[:3])
    assert got==signs, (a,got,signs)

# Exact algebra certifies the discriminant and crossing ordering.
assert 107**2 - 4*9*288 == 1081
assert 32**2 < 1081 < 33**2
# Hence the first root lies (74/18,75/18) subset (4,5),
# and the second root lies (139/18,140/18) subset (7,8).
print('PASS: six-node symmetric moment identities, Beta factorizations,')
print(f'PASS: {count} exact monomial moment checks over panel counts 1..5;')
print('PASS: rational sign witnesses and exact boundary ordering.')
