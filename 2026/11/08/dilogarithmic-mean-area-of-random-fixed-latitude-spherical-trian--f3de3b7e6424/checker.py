"""Reproducible numerical checks for the fixed-latitude spherical triangle area law.

Requires Python 3 standard library only. Monte Carlo is corroboration, not proof.
"""
import math
import random


def li2_negative(r):
    """Return Li_2(-r) by its convergent power series, for 0 <= r < 1."""
    if not 0 <= r < 1:
        raise ValueError('domain')
    result = 0.0
    power = -r
    for k in range(1, 10000):
        term = power / (k * k)
        result += term
        if abs(term) < 2e-16:
            return result
        power *= -r
    raise RuntimeError('insufficient series convergence')


def mean_area(theta):
    c = abs(math.cos(theta))
    r = (1-c)/(1+c)
    return -6 / math.pi * li2_negative(r)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def area_both(theta, az):
    c, s = math.cos(theta), math.sin(theta)
    vertices = [(s*math.cos(u), s*math.sin(u), c) for u in az]
    a, b, d = vertices
    scalar = dot(a, cross(b, d))
    den = 1 + dot(a, b) + dot(b, d) + dot(d, a)
    solid = 2*math.atan2(abs(scalar), den)

    pole_cos = abs(c)
    angles = []
    for i in range(3):
        u = (az[(i+1)%3]-az[i]) % (2*math.pi)
        v = (az[(i+2)%3]-az[i]) % (2*math.pi)
        bu = math.atan2(math.sin(u), pole_cos*(1-math.cos(u)))
        bv = math.atan2(math.sin(v), pole_cos*(1-math.cos(v)))
        angles.append(abs(bu-bv))
    girard = sum(angles)-math.pi
    return solid, girard


def check():
    rng = random.Random(20261104)
    n = 85000
    for theta in (0.20, 0.65, 1.10, 1.47):
        total, total2, worst = 0., 0., 0.
        for _ in range(n):
            u = [rng.random()*2*math.pi for i in range(3)]
            solid, girard = area_both(theta, u)
            worst = max(worst, abs(solid-girard))
            total += solid
            total2 += solid*solid
        assert worst < 2e-9, (theta, worst)
        avg = total/n
        stderr = math.sqrt(max(0., total2/n-avg*avg)/n)
        predicted = mean_area(theta)
        assert abs(avg-predicted)<5*stderr+0.001, (theta, predicted, avg, stderr)
        print(f'colatitude={theta:.2f}: theory={predicted:.9f}, sample={avg:.9f}, stderr={stderr:.6f}')
    assert abs(-6/math.pi*(-math.pi**2/12) - math.pi/2)<1e-13
    print('LATITUDE_SPHERICAL_AREA_DILOG_CHECK_OK', n, 'samples each')


if __name__ == '__main__':
    check()
