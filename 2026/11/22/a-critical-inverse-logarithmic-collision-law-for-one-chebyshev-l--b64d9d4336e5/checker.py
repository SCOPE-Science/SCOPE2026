"""Finite diagnostics for a one-node Chebyshev--Lobatto near-collision law.

This numerical diagnostic does not prove the infinite asymptotic theorem.
Only the Python standard library is needed.
"""
import math

PI = math.pi
checks = 0

def check(condition, detail):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(detail)

def x_of(n, j):
    return math.cos(PI * j / n)

def cardinal(n, j, theta):
    z = math.cos(theta)
    den = z - x_of(n, j)
    return -((-1)**j) * math.sin(theta) * math.sin(n * theta) / (n * (2 if j in (0, n) else 1) * den)

def new_cardinals(n, m, eps, theta):
    ytheta = (m + 1 - eps) * PI / n
    y = math.cos(ytheta)
    xm = x_of(n, m)
    z = math.cos(theta)
    Lmy = cardinal(n, m, ytheta)
    Lmz = cardinal(n, m, theta)
    out = []
    for j in range(n + 1):
        if j == m:
            out.append(Lmz / Lmy)
        else:
            Ljy = cardinal(n, j, ytheta)
            out.append(cardinal(n, j, theta) - Ljy * Lmz / Lmy)
    return out

def root_s(b):
    def derivative(s):
        return PI * (s * s + b * s) * math.cos(PI * s) - b * math.sin(PI * s)
    lo, hi = 1e-8, .5
    for _ in range(100):
        mid = (lo + hi) / 2
        if derivative(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

for n in (12, 20, 32, 48, 72):
    m = n // 2 - 1
    for eps in (.08, .3, .75):
        y = math.cos((m + 1 - eps) * PI / n)
        xm = x_of(n, m)
        for u in (-2.37, -1.43, -.75, -.23, .26, .72, 1.3, 2.41):
            theta = (m + u) * PI / n
            z = math.cos(theta)
            vals = new_cardinals(n, m, eps, theta)
            check(abs(sum(vals) - 1) < 2e-7, ("partition", n, eps, u, sum(vals)))
            for j in range(n + 1):
                if j == m:
                    continue
                alt = cardinal(n, j, theta) * (z-y)/(z-xm) * (x_of(n,j)-xm)/(x_of(n,j)-y)
                check(abs(vals[j] - alt) < 2e-6 * max(1, abs(vals[j])), ("replacement", n, eps, u, j, vals[j], alt))

for b in (1., 1.5, 2., 3., 6., 11.):
    s = root_s(b)
    check(0 < s < .5, ("s range", b, s))
    h = lambda v: math.sin(PI*v)*(1+b/v)
    check(all(h(s) + 1e-11 >= h(j/2000) for j in range(1,1001)), ("scalar global", b, s))

for n in (256, 512, 1024, 2048, 4096):
    m = n // 2
    for c in (.5, 1., 2.):
        eps = c/math.log(n)
        s = root_s(1+1/c)
        theta = (m - s) * PI/n
        lebesgue = sum(abs(v) for v in new_cardinals(n,m,eps,theta))
        target = (2/PI)*math.sin(PI*s)*(1+(1+1/c)/s)
        check(abs(lebesgue/math.log(n)-target) < 2.0, ("asymptotic gross", n, c, lebesgue/math.log(n), target))

print('NEAR_COLLISION_CHEB_DIAGNOSTIC_OK', checks)
