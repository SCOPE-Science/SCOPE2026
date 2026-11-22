"""Reproducible diagnostic computations for a rhombic-dodecahedron shadow law.

Requires only Python 3 standard library. This checks numerical and finite
identities, not the infinite analytic claims, which are proved in RESULT.md.
"""
import itertools
import math
import random

VERTICES = list(itertools.product((-1., 1.), repeat=3))
VERTICES += [tuple(2. * s if k == j else 0. for j in range(3))
             for k in range(3) for s in (-1, 1)]
CENTERS = sorted(set(itertools.permutations((2, 1, 0))) |
                 set(itertools.permutations((2, -1, 0))) |
                 set(itertools.permutations((-2, 1, 0))) |
                 set(itertools.permutations((-2, -1, 0))))
assert len(CENTERS) == 24


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def norm(a):
    return math.sqrt(dot(a, a))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def brightness(u):
    a, b, _ = sorted((abs(x) for x in u), reverse=True)
    return 4*(2*a+b)


def projected_area(u):
    seed = (1., 0., 0.) if abs(u[0]) < 0.8 else (0., 1., 0.)
    q = dot(seed, u)
    v = tuple((seed[i]-q*u[i]) for i in range(3))
    t = norm(v)
    v = tuple(x/t for x in v)
    w = cross(u, v)
    pts = sorted({(dot(p, v), dot(p, w)) for p in VERTICES})

    def cr(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

    lower = []
    for p in pts:
        while len(lower) >= 2 and cr(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cr(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    hull = lower[:-1]+upper[:-1]
    return abs(sum(cr((0, 0), hull[i], hull[(i+1) % len(hull)])
                   for i in range(len(hull))))/2


def cdf(b, n=24000):
    if b <= 4*math.sqrt(3): return 0.
    if b >= 4*math.sqrt(5): return 1.

    def integrand(s):
        A = 1+s*s
        if s == 0: return 0.
        z = (16*(2+s)**2/b**2-A)/s**2
        T = 0. if z <= 0. else (1. if z >= 1. else math.sqrt(z))
        return s/A*(1/math.sqrt(1+2*s*s)-T/math.sqrt(A+s*s*T*T))

    # Uniform midpoint sum gives a stable, deterministic cross-check.
    return 12/math.pi*sum(integrand((j+.5)/n) for j in range(n))/n


def main():
    rng = random.Random(20261118)
    for _ in range(500):
        v = [rng.gauss(0, 1) for k in range(3)]
        v = tuple(x/norm(v) for x in v)
        assert abs(projected_area(v)-brightness(v)) < 1e-10
        assert abs(brightness(v)-4*max(dot(c, v) for c in CENTERS)) < 1e-10
    print('1000 independent convex-hull/support tests passed')

    nearest = [(a, b) for i, a in enumerate(CENTERS) for b in CENTERS[i+1:]
               if dot(a, b) == 4]
    assert len(nearest) == 36
    assert max(dot(a, b) for i, a in enumerate(CENTERS)
               for b in CENTERS[i+1:]) == 4
    print('36 first-neighbor pairs verified')

    hi = 4*math.sqrt(5)
    threshold = 6*math.sqrt(2)
    for b in (threshold+.03, threshold+.1, 8.6, 8.8, hi-.015):
        exact = 1-12*(1-b/hi)
        assert abs(cdf(b)-exact) < 7e-6, (b, cdf(b), exact)
    print('Five exact-terminal-tail CDF comparisons passed')

    lo = 4*math.sqrt(3)
    lo_constant = math.sqrt(3)/(8*math.pi)
    ratios = [cdf(lo+e)/e**2 for e in (.06, .03, .015)]
    assert abs(ratios[-1]/lo_constant-1) < .011, ratios
    assert ratios[0] > ratios[1] > ratios[2] > lo_constant
    print('Quadratic lower-tail scaling confirmed', ratios)

    critical_coefficient = math.sqrt(3)*2**(5/4)/math.pi
    ratios = []
    for e in (.05, .025, .0125):
        b = threshold-e
        no_overlap = 12*(1-b/hi)
        exact = 1-cdf(b)
        ratios.append((no_overlap-exact)/e**1.5)
    assert abs(ratios[-1]/critical_coefficient-1) < .015, ratios
    assert ratios[0] < ratios[1] < ratios[2] < critical_coefficient
    print('First-overlap three-halves scaling confirmed', ratios)
    print('Median by one-dimensional quadrature is approximately 8.5716')


if __name__ == '__main__':
    main()
