"""Finite diagnostic checks for a dimerized boundary-weight spectral formula.

These checks corroborate algebra and finite-section behavior; they do not certify
infinite-dimensional spectral conclusions or publication originality.
"""
from math import sqrt, isclose
from random import Random

checks = 0


def verify(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1


def gfun(lam, a, b):
    upper = a + b
    return ((lam * lam + b * b - a * a) -
            sqrt((lam * lam - upper * upper) *
                 (lam * lam - (a - b) ** 2))) / (2 * b * b * lam)


def ffun(lam, a, b, c, d):
    return lam - c * c / lam - d * d * gfun(lam, a, b)


def surface_energy(a, b, c, d):
    upper = a + b
    if c * c + upper / b * d * d <= upper * upper:
        return upper
    lo, hi = upper, upper + a + b + c + d + 1
    verify(ffun(hi, a, b, c, d) > 0, 'positive far residual')
    for _ in range(75):
        mid = (lo + hi) / 2
        if ffun(mid, a, b, c, d) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def finite_top(n, a, b, c, d):
    """Largest eigenvalue of a real tridiagonal principal section via inertia."""
    edge = [c, d] + [a if i % 2 == 0 else b for i in range(n - 3)]
    assert len(edge) == n - 1

    def neg_count(lam):
        p = -lam
        count = int(p < 0)
        for x in edge:
            if abs(p) < 1e-14:
                p = -1e-14
            p = -lam - x * x / p
            count += int(p < 0)
        return count

    lo = 0.0
    hi = 2 * max(a, b, c, d) + a + b + 2
    verify(neg_count(hi) == n, 'finite upper inertia')
    for _ in range(65):
        mid = (lo + hi) / 2
        if neg_count(mid) < n:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


samples = [
    (1.0, 2.0, 1.0, 2.0),
    (1.0, 2.0, 2.2, 2.2),
    (1.0, 2.0, 2.2, 0.5),
    (2.0, 1.0, 1.0, 1.0),
    (0.6, 1.7, 1.5, 2.0),
    (1.0, 1.0, 0.4, 1.6),  # constant-tail consistency case, not novelty
    (2.0, 1.0, 2.5, 0.7),
]
rng = Random(451)
for _ in range(28):
    a = rng.uniform(0.6, 2.4)
    b = rng.uniform(0.6, 2.4)
    c = rng.uniform(0.25, 3.1)
    d = rng.uniform(0.25, 3.1)
    samples.append((a, b, c, d))

for a, b, c, d in samples:
    L = a + b
    h = c * c + (L / b) * d * d
    verify(isclose(gfun(L, a, b), 1 / b, rel_tol=1e-11, abs_tol=1e-11),
           'boundary resolvent')
    for k in range(1, 10):
        lam = L + 0.15 * k
        g = gfun(lam, a, b)
        verify(g > 1 / lam, 'strict positivity of tail correction')
        quad = b*b*lam*g*g-(lam*lam+b*b-a*a)*g+lam
        verify(abs(quad) < 1e-9, 'Schur quadratic')
    candidate = surface_energy(a, b, c, d)
    if h > L * L:
        verify(candidate > L, 'surface binding')
        verify(abs(ffun(candidate, a, b, c, d)) < 1e-8,
               'exact root residual')
    else:
        verify(candidate == L, 'no surface binding')
    top = finite_top(280, a, b, c, d)
    verify(top <= candidate + 4e-7,
           'finite-section variational upper bound')
    verify(candidate - top < 0.018,
           'finite-section convergence diagnostic')

for a, b, d in [(1.0, 2.0, 1.5), (1.0, 1.0, 1.3), (2.0, 1.0, 1.6)]:
    L = a + b
    cstar2 = L*L-L/b*d*d
    verify(cstar2 > 0, 'positive critical first bond')
    coeff = b**3/(2*a*L*d**4)
    for eps in (0.025, 0.012):
        E = surface_energy(a, b, sqrt(cstar2 + eps), d)
        observed = (E - L) / eps**2
        verify(abs(observed - coeff) / coeff < 0.08, 'quadratic onset')

for a, b, S in [(1.1, 2.0, 6.0), (1.7, 0.8, 4.0), (0.5, 1.3, 3.5)]:
    prev = None
    for k in range(1, 25):
        d2 = S * k / 25
        c2 = S - d2
        x = surface_energy(a, b, sqrt(c2), sqrt(d2))
        if prev is not None:
            verify(x >= prev - 1e-10, 'fixed-budget monotonicity')
        prev = x

print('PASS: %d finite diagnostic assertions' % checks)
