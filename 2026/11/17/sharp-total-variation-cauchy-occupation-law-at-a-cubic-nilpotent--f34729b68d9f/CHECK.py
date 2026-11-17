"""Supplementary numerical diagnostics for the stated cubic nilpotent center.

Uses only the Python standard library. All universal statements are proved
analytically in RESULT.md; these computations do not certify a limit.
"""
import math


def potential(x):
    root = math.sqrt(3.0)
    return x*x/2 - x + 2/root * (
        math.atan((2*x+1)/root) - math.atan(1/root)
    )


def p(x):
    return 1+x+x*x


def bisect_root(energy, side):
    b = max(10.0, 8*math.sqrt(energy))
    lo, hi = (-b, 0.0) if side < 0 else (0.0, b)
    assert (potential(lo)-energy)*(potential(hi)-energy) < 0
    for _ in range(100):
        mid = (lo+hi)/2
        if (potential(lo)-energy)*(potential(mid)-energy) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def composite_midpoint(func, lo, hi, n):
    h = (hi-lo)/n
    return h*sum(func(lo + (k+0.5)*h) for k in range(n))


def check():
    for x in [-11.4, -2.0, -0.2, 0.0, 0.5, 2.3, 23.0]:
        assert abs((x-1+1/p(x)) - x**3/p(x)) < 1e-11 * max(1,abs(x))
    c = 2*math.pi/math.sqrt(3)
    assert abs((2/math.sqrt(3))*(math.pi) - c) < 1e-14
    coeff = math.sqrt(3)/(math.sqrt(2)*math.pi)
    previous = None
    for energy in [100.0, 500.0, 3000.0]:
        left = bisect_root(energy, -1)
        right = bisect_root(energy, +1)
        # Smooth out both square-root turning-point singularities.
        def j_integrand(t):
            s = math.sin(t)
            x = left + (right-left)*s*s
            dxdt = (right-left)*math.sin(2*t)
            return dxdt/p(x)/math.sqrt(max(1e-300, 1-potential(x)/energy))
        j = composite_midpoint(j_integrand, 0.0, math.pi/2, 16000)
        assert math.isfinite(j)
        # Exact Cauchy mass outside the finite-energy turning points.
        cdf_gap = (2/math.sqrt(3))*(
            math.atan((2*right+1)/math.sqrt(3))
            - math.atan((2*left+1)/math.sqrt(3))
        )
        tail_prob = (c-cdf_gap)/c
        leading = tail_prob*math.sqrt(energy)
        assert abs(leading-coeff) < 0.02
        assert abs(j-c) < 0.05
        if previous is not None:
            assert abs(leading-coeff) < abs(previous-coeff)
        previous = leading
        print(f'E={energy:.0f}, sqrt(E) * Cauchy outside mass={leading:.10f}, J-C={j-c:.10f}')
    print('NILPOTENT_CAUCHY_TV_DIAGNOSTICS_OK')


if __name__ == '__main__':
    check()
