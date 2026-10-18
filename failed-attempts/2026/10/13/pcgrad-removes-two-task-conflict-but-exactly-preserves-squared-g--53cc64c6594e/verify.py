import math
import random


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def norm(x):
    return math.sqrt(dot(x, x))


def add(x, y):
    return [a+b for a, b in zip(x, y)]


def scale(c, x):
    return [c*a for a in x]


def sub(x, y):
    return [a-b for a, b in zip(x, y)]


def pcgrad(g1, g2):
    c = dot(g1, g2)
    a2 = dot(g1, g1)
    b2 = dot(g2, g2)
    p1 = sub(g1, scale(c/b2, g2))
    p2 = sub(g2, scale(c/a2, g1))
    return add(p1, p2)


def prescribed(a, b, rho):
    return [a, 0.0], [b*rho, b*math.sqrt(max(0.0, 1.0-rho*rho))]


random.seed(350069)

# Random conflicting vector pairs.
for _ in range(4000):
    d = random.randint(2, 10)
    g1 = [random.gauss(0.0, 1.0) for _ in range(d)]
    g2 = [random.gauss(0.0, 1.0) for _ in range(d)]
    if dot(g1, g2) >= -1e-8:
        g2 = scale(-1.0, g2)
    a = norm(g1)
    b = norm(g2)
    rho = dot(g1, g2)/(a*b)
    if not (-0.999999 < rho < -1e-8):
        continue
    dpc = pcgrad(g1, g2)
    lhs1 = dot(g1, dpc)
    lhs2 = dot(g2, dpc)
    rhs1 = a*a*(1.0-rho*rho)
    rhs2 = b*b*(1.0-rho*rho)
    assert abs(lhs1-rhs1) <= 2e-10*max(1.0, rhs1)
    assert abs(lhs2-rhs2) <= 2e-10*max(1.0, rhs2)
    assert lhs1 > 0.0 and lhs2 > 0.0
    n2 = dot(dpc, dpc)
    n2_exact = (1.0-rho*rho)*(a*a+b*b-2.0*a*b*rho)
    assert abs(n2-n2_exact) <= 4e-10*max(1.0, n2_exact)
    assert abs((lhs1/(a*a))-(lhs2/(b*b))) <= 2e-10
    assert abs((lhs1/lhs2)-(a*a/(b*b))) <= 2e-9*max(1.0, a*a/(b*b))

# Raw-sum strict common-descent window and boundaries.
for rho in (-0.05, -0.2, -0.5, -0.9, -0.99):
    lo = -rho
    hi = -1.0/rho
    for r in (lo*0.5, lo*1.0001, 1.0, hi*0.9999, hi*1.5):
        g1, g2 = prescribed(r, 1.0, rho)
        dsum = add(g1, g2)
        good = dot(g1, dsum) > 0.0 and dot(g2, dsum) > 0.0
        expected = (lo < r < hi)
        assert good == expected

    # Exact lower boundary: task 1 has zero progress.
    g1, g2 = prescribed(lo, 1.0, rho)
    dsum = add(g1, g2)
    assert abs(dot(g1, dsum)) < 2e-13
    assert dot(g2, dsum) > 0.0

    # Exact upper boundary: task 2 has zero progress.
    g1, g2 = prescribed(hi, 1.0, rho)
    dsum = add(g1, g2)
    assert dot(g1, dsum) > 0.0
    assert abs(dot(g2, dsum)) < 2e-12*max(1.0, hi*hi)

# Exact antiparallel null update for arbitrary norm ratio.
for r in (0.01, 0.2, 1.0, 5.0, 100.0):
    g1 = [r, 0.0]
    g2 = [-1.0, 0.0]
    dpc = pcgrad(g1, g2)
    assert norm(dpc) < 2e-12*max(1.0, r)

# Near-antiparallel normalized progress is sin^2(epsilon) ~ epsilon^2.
for eps in (1e-2, 3e-3, 1e-3, 3e-4):
    rho = -math.cos(eps)
    g1, g2 = prescribed(3.0, 0.7, rho)
    dpc = pcgrad(g1, g2)
    normalized = dot(g1, dpc)/dot(g1, g1)
    exact = math.sin(eps)**2
    assert abs(normalized-exact) < 2e-12
    assert abs(normalized/(eps*eps)-1.0) < 5e-5

print('verification passed')
