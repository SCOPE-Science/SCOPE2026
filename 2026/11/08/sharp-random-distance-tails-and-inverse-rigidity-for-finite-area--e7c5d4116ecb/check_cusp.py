#!/usr/bin/env python3
"""Independent numerical checks for the random-distance law on a truncated hyperbolic cusp.
The analytical theorem stands on the proof, not these finite checks.
Requires only the Python standard library.
"""
import math
import random


def tail_integral(width, radius, panels=4096):
    assert width > 0 and radius >= 2 * math.asinh(width / 4)
    b = width / 2
    H = math.sinh(radius)
    C = math.cosh(radius)
    step = b / panels
    def f(z):
        return (2 / b) * (1 - z / b) / (C + math.sqrt(H * H - z * z))
    value = f(0) + f(b)
    for j in range(1, panels):
        value += (4 if j % 2 else 2) * f(j * step)
    return value * step / 3


def asymptotic(width, radius):
    e = math.exp(-radius)
    return e + width**2 / 24 * e**3 + (width**2 / 24 + width**4 / 120) * e**5


def direct_hyperbolic_distance(x1, y1, x2, y2, width):
    dx = abs(x1 - x2)
    dx = min(dx, width - dx)
    return math.acosh(1 + ((y1 - y2)**2 + dx**2)/(2*y1*y2))


def run():
    rng = random.Random(672904)
    # The direct simulator uses hyperbolic plane coordinates; the quadrature
    # uses independent Exp/Beta coordinates obtained by a separate derivation.
    for width, radius in [(0.75, 2), (1.0, 2), (3, 2), (3, 3), (6, 4)]:
        theory = tail_integral(width, radius)
        assert abs(theory - asymptotic(width, radius)) < max(3e-5, theory * 0.003)
        successes = 0
        count = 220000
        for _ in range(count):
            x1, x2 = width*rng.random(), width*rng.random()
            y1, y2 = 1/(1-rng.random()), 1/(1-rng.random())
            d = direct_hyperbolic_distance(x1,y1,x2,y2,width)
            successes += (d > radius)
            delta = min(abs(x1-x2), width-abs(x1-x2))
            s = abs(math.log(y1) - math.log(y2))
            m = min(math.log(y1),math.log(y2))
            z = delta*math.exp(-m)
            reconstructed = math.acosh(math.cosh(s) + z*z*math.exp(-s)/2)
            assert abs(d - reconstructed) < 1e-7
        empirical = successes / count
        # Conservative fixed-binomial test with an independent geometric derivation.
        std = math.sqrt(theory * (1-theory)/count)
        assert abs(empirical-theory) < 6*std+0.0002, (width,radius,empirical,theory,std)
    # Check exact second/third tail coefficients using high-resolution Simpson quadrature.
    for width in [0.5,1.0,3.0,8.0]:
        for radius in [4.0,5.0,6.0]:
            if radius < 2*math.asinh(width/4):
                continue
            exact=tail_integral(width,radius)
            formula=asymptotic(width,radius)
            # Analytic remainder is O_width(e^{-7R}). At these values
            # this is directly observable without severe cancellation.
            assert abs(exact-formula) < 3e-14 + (1+width**6)*math.exp(-7*radius), (width,radius,exact,formula)
    print('TRUNCATED_HYPERBOLIC_CUSP_TAIL_AND_MC_OK 1100000')

if __name__=='__main__':
    run()
