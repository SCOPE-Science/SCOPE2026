"""Deterministic checks for the circle positive-weight quadrature theorem.

Only Python standard library is required. This script checks finite-dimensional
geometry and numerical integral identities; asymptotic proofs are analytical.
"""
import math
import random

PI = math.pi
TAU = 2 * PI


def density(theta, a):
    assert -1 < a < 1
    return (1 + a * math.cos(2 * theta)) / TAU


def circle_error_gap(angles):
    ordered = sorted(x % TAU for x in angles)
    gaps = [ordered[(j+1) % len(ordered)] - ordered[j]
            if j + 1 < len(ordered)
            else TAU + ordered[0] - ordered[-1]
            for j in range(len(ordered))]
    gap = max(gaps)
    return math.sin((gap - PI) / 2) if gap > PI else 0.0


def point_segment_distance(a, b):
    x, y = math.cos(a), math.sin(a)
    u, v = math.cos(b), math.sin(b)
    dx, dy = u - x, v - y
    t = -(x*dx + y*dy) / (dx*dx + dy*dy)
    t = min(1.0, max(0.0, t))
    return math.hypot(x + t*dx, y + t*dy)


def circle_error_polygon(angles):
    ordered = sorted(x % TAU for x in angles)
    gaps = [(ordered[(j+1) % len(ordered)] - ordered[j]) % TAU
            for j in range(len(ordered))]
    if max(gaps) <= PI:
        return 0.0  # center lies in polygon
    return min(point_segment_distance(ordered[j], ordered[(j+1) % len(ordered)])
               for j in range(len(ordered)))


def angular_arc_mass(theta, width, a):
    return (width + (a / 2) * (math.sin(2 * (theta + width))
                               - math.sin(2 * theta))) / TAU


def periodic_midpoint_integral(func, count=512):
    return TAU / count * sum(func(TAU * (j + .5) / count)
                             for j in range(count))


def exact_tail(N, z, a=0.0):
    if z < 0:
        return 1.0
    if z >= 1:
        return 0.0
    w = 2 * math.asin(z)
    return N * periodic_midpoint_integral(
        lambda theta: density(theta, a)
        * max(0.0, .5 - angular_arc_mass(theta, w, a)) ** (N - 1))


def conditional_tail_rescaled(N, t, a):
    if t >= N:
        return 0.0
    return exact_tail(N, t / N, a) / (N * 2 ** (1 - N))


def limit_conditional_tail(t, a):
    return periodic_midpoint_integral(
        lambda theta: density(theta, a)
        * math.exp(-4 * t * density(theta, a)))


def midpoint_integral(func, lo, hi, count=1400):
    step = (hi - lo) / count
    return step * sum(func(lo + (j + .5) * step)
                      for j in range(count))


def verify():
    rng = random.Random(236273)
    total = 0
    for N in (2, 3, 4, 5, 7, 10, 16):
        for _ in range(72):
            angles = [rng.random() * TAU for _ in range(N)]
            a, b = circle_error_gap(angles), circle_error_polygon(angles)
            assert math.isclose(a, b, rel_tol=1e-10, abs_tol=1e-10), (a,b)
            total += 1
    for N in (2,3,4,7,12):
        for z in (.001,.05,.1,.25,.49,.75,.95):
            lhs = exact_tail(N, z)
            rhs = N * (.5 - math.asin(z) / PI) ** (N-1)
            assert math.isclose(lhs,rhs,rel_tol=2e-12,abs_tol=1e-13)
            total += 1
    for a in (-.85,-.5,.0,.4,.9):
        for N in (2,3,7,21):
            assert math.isclose(exact_tail(N,0.0,a), N*2**(1-N),rel_tol=2e-12)
            total += 1
    for a in (-.5,0,.6):
        for t in (.1,.6,1.7,3.,6.):
            approx = conditional_tail_rescaled(800,t,a)
            limit = limit_conditional_tail(t,a)
            assert abs(approx - limit) < .004, (a,t,approx,limit)
            total += 1
    for a in (0.0,.7):
        # Numerically integrate the limiting p=1,2 moments;
        # compare with analytically integrated angular-density powers.
        for p in (1.0, 2.0):
            mean_p = p * midpoint_integral(lambda t: t**(p-1)*limit_conditional_tail(t,a),
                                             0.,80.,count=1200)
            if p == 1:
                expected = PI/2
            else:
                expected = PI*PI/(2*math.sqrt(1-a*a))
            assert math.isclose(mean_p,expected,rel_tol=.0002), (a,p,mean_p,expected)
            total += 1
    print(f'PASS: {total} geometric, finite-tail and asymptotic-coefficient assertions')


if __name__ == '__main__':
    verify()
