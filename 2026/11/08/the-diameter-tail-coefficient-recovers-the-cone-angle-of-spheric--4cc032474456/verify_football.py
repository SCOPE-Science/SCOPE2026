#!/usr/bin/env python3
"""Deterministic quadrature checks for the diameter-tail law on spherical footballs.

Only Python's standard library is required. Numerical checks corroborate, rather
than replace, the analytical derivation in RESULT.md.
"""
from math import acos, atan2, cos, hypot, pi, sin, tan, sqrt


def simpson(f, lo, hi, n):
    assert n >= 2 and n % 2 == 0
    h = (hi - lo) / n
    v = f(lo) + f(hi)
    for i in range(1, n):
        v += (4 if i % 2 else 2) * f(lo + i * h)
    return v * h / 3


def angular_integral(delta):
    if abs(delta) < 0.004:
        q = delta * delta
        return 1 / 24 + q / 60 + q * q / 252 + q**3 / 1350
    return (sin(delta) - delta * cos(delta)) / (8 * sin(delta)**3)


def tail_coefficient(alpha):
    a = pi * alpha
    return (1 / sin(a)**2 - cos(a) / (a * sin(a))) / 32


def radial_integral(delta):
    c = cos(delta)
    return simpson(lambda t: sin(2*t) / (8*(1+c*sin(2*t))**2), 0, pi/2, 1000)


def local_exact_tail(alpha, eps):
    """Geodesic probability, evaluated near the opposite poles.

    For these alpha and eps, every pair with d>pi-eps is in one of the
    two opposite-pole coordinate patches. For a fixed longitude gap and
    north-pole colatitude u, solve the cosine inequality for the
    south-pole colatitude v without asymptotic approximation.
    """
    a = pi * alpha
    ulim = min(pi/2, (2.5 + 4 / max(.25, sin(a))) * eps)
    def one_longitude(delta):
        c = cos(delta)
        def one_colatitude(u):
            R = hypot(cos(u), sin(u) * c)
            if R <= cos(eps):
                return 0.
            phase = atan2(sin(u) * c, cos(u))
            t = acos(min(1., cos(eps)/R))
            low = max(0., -phase - t)
            high = max(0., -phase + t)
            if low >= high:
                return 0.
            return sin(u) * (cos(low) - cos(high))
        return simpson(one_colatitude, 0, ulim, 840)
    return simpson(one_longitude, 0, a, 440) / (2 * a)


def main():
    alphas = (0.25, 0.5, 0.75, 0.9)
    for alpha in alphas:
        a = pi * alpha
        target = tail_coefficient(alpha)
        angle_average = simpson(angular_integral, 0, a, 1000) / (2*a)
        assert abs(angle_average / target - 1) < 2e-7, (alpha,angle_average,target)
        for delta in (0, a/2, a):
            r1 = radial_integral(delta)
            r2 = angular_integral(delta)
            assert abs(r1/r2 - 1) < 1e-8, (alpha,delta,r1,r2)
        values = []
        for eps in (0.05, 0.025):
            observed = local_exact_tail(alpha, eps) / eps**4
            values.append(observed)
        # The normalized finite-epsilon tail approaches the exact coefficient.
        assert abs(values[-1] / target - 1) < 0.006, (alpha,values,target)
        assert abs(values[-1]-target) < abs(values[0]-target), (alpha,values)
        print(f'alpha={alpha:.2f} coefficient={target:.12f} '
              f'tail-ratios={values[0]:.12f},{values[1]:.12f}')
    assert abs(tail_coefficient(.5)-1/32)<1e-14
    assert tail_coefficient(.25)<tail_coefficient(.5)<tail_coefficient(.75)<tail_coefficient(.9)
    assert abs((tail_coefficient(0.01)-1/48)/(pi*.01)**2 - 1/360)<1e-5
    print('SPHERICAL_FOOTBALL_DIAMETER_TAIL_OK')

if __name__=='__main__':
    main()
