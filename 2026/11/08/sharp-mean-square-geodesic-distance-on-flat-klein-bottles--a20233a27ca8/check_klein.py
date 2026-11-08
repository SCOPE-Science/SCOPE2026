"""Numerical, independent consistency checks for the flat Klein bottle distance law.

Only the Python standard library is needed. These checks do not replace the proof.
"""
import math
import random

SEED = 3528511
rng = random.Random(SEED)


def cdistance(v, a):
    q = v % a
    return min(q, a-q)


def reduced_distance_squared(p, q, a, b):
    x, y = p
    xp, yp = q
    u = abs(y-yp)
    xeven = cdistance(x-xp, a)
    xodd = cdistance(x+xp, a)
    return min(xeven*xeven+u*u, xodd*xodd+(b-u)**2)


def raw_deck_distance_squared(p, q, a, b):
    x, y = p
    xp, yp = q
    best = math.inf
    for k in range(-2, 3):
        for m in range(-2, 3):
            best = min(best,
                       (xp+k*a-x)**2 + (yp+2*m*b-y)**2,
                       (-xp+k*a-x)**2 + (yp+(2*m+1)*b-y)**2)
    return best


def h(v):
    if v <= 1:
        return (1 + v*v) / 2
    return v


def formula_energy(t, subdivisions=70000):
    if t <= 2:
        return (t+1/t)/12-t**3/360
    # Independent midpoint quadrature using the exact density of |S^2-T^2|.
    # f_|Z|(z) = asinh(sqrt((1-z)/z)) on (0,1).
    acc = 0.0
    for i in range(subdivisions):
        z = (i+0.5) / subdivisions
        density = math.asinh(math.sqrt((1-z)/z))
        acc += h(t*t*z/4)*density
    return t/12+1/(3*t)-acc/(2*t*subdivisions)


def cdf_integral(a, b, r, subdivisions=12000):
    survive = 0.0
    for i in range(subdivisions):
        u = b * (i + 0.5) / subdivisions
        w = b-u
        def q(z):
            return min(1.0, (2/a)*math.sqrt(max(0.0, r*r-z*z)))
        survive += (1-q(u))*(1-q(w))
    return 1-survive/subdivisions


def sample_stats(a, b, count=125000):
    vals = []
    for i in range(count):
        p = (a*rng.random(), b*rng.random())
        q = (a*rng.random(), b*rng.random())
        sq = reduced_distance_squared(p, q, a, b)
        if i < 1800:
            deck = raw_deck_distance_squared(p, q, a, b)
            assert abs(deck-sq) < 1e-10 * (1+a*a+b*b)
        vals.append(sq/(a*b))
    mean = sum(vals)/count
    second = sum(z*z for z in vals)/count
    stderr = math.sqrt(max(0.0, second-mean*mean)/count)
    return mean, stderr


def check():
    tstar = math.sqrt(5-math.sqrt(15))
    vstar = (10+math.sqrt(15))*tstar/90
    assert abs(tstar-1.061610405842267) < 1e-13
    assert abs(formula_energy(tstar)-vstar) < 1e-13
    assert formula_energy(1) > vstar and formula_energy(2) > vstar
    for a, b in [(0.35, 2.0), (0.6, 1.0), (1.0, 1.0),
                 (tstar, 1.0), (2.0, 1.0), (3.0, 1.0), (6.0, 1.0)]:
        mean, stderr = sample_stats(a, b)
        reference = formula_energy(a/b)
        assert abs(mean-reference) <= 6*stderr+0.0008, (
            a, b, mean, reference, stderr)
        print('MOMENT_OK', 'a=', a, 'b=', b, 'sample=', round(mean, 8),
              'integral=', round(reference, 8), 'std_error=', round(stderr, 8))
    print('DIRECT_DECK_ORBIT_OK', 'count=', 7*1800)

    # A second, genuinely different check of the all-radius law: direct
    # random samples and deterministic quadrature of the closed CDF kernel.
    for a, b in [(0.7, 1.0), (2.7, 1.0)]:
        vals = []
        for _ in range(90000):
            p = (a*rng.random(), b*rng.random())
            q = (a*rng.random(), b*rng.random())
            vals.append(math.sqrt(reduced_distance_squared(p, q, a, b)))
        diameter = math.hypot(a,b)/2
        for frac in (0.16,0.31,0.47,0.62,0.78,0.93):
            r = frac*diameter
            empirical = sum(z <= r for z in vals)/len(vals)
            exact = cdf_integral(a,b,r)
            assert abs(empirical-exact) < 0.011, (a,b,frac,empirical,exact)
        assert abs(cdf_integral(a,b,diameter) - 1) < 1e-10
    print('FULL_CDF_QUADRATURE_OK', 'geometries=2 radii=12')

    # Strict analytic derivative lower bounds (tested numerically at samples).
    def gp(t):
        return 1/12-1/(12*t*t)-t*t/120
    for t in (tstar+0.0001,1.5,2,2.2,2.6,math.sqrt(8)):
        assert gp(t) > 0
    for t in (math.sqrt(8)+0.0001,3,4,8,20):
        assert t*t/24-1/3 > 0
    print('GLOBAL_OPTIMIZER_BOUND_CONSISTENCY_OK', 'tstar=',tstar,
          'normalized_minimum=',vstar)


if __name__ == '__main__':
    check()
