"""Supplementary checks for the sharp two-tone centered energy-dilation inequality.

These finite tests do not replace the analytic all-parameter proof in RESULT.md.
"""
import cmath
import math
import random


def sinc(z):
    if abs(z) < 1e-5:
        z2 = z*z
        return 1 - z2/6 + z2*z2/120 - z2*z2*z2/5040
    return math.sin(z)/z


def energy(radius, gap, a, b):
    """Integral over [-radius,radius] of |a cos(gap*t/2)+b sin(gap*t/2)|^2."""
    s = sinc(gap*radius)
    return radius*((abs(a)**2)*(1+s)+(abs(b)**2)*(1-s))


def exact_modes(radius, gap):
    s = sinc(gap)
    outer = sinc(radius*gap)
    assert 0 < abs(gap) and radius > 1
    return radius*(1+outer)/(1+s), radius*(1-outer)/(1-s)


def check():
    rng = random.Random(713612)
    total = 0
    for gap in (0.005,0.01,0.04,0.1,0.5,1.0,2,3.14,5,10,30,100):
        for radius in (1.01,1.07,1.3,2,2.7,4,10):
            even,odd = exact_modes(radius,gap)
            assert 0 < even < radius**3
            assert 0 < odd < radius**3
            total += 2
            for _ in range(18):
                a = complex(rng.uniform(-2,2),rng.uniform(-2,2))
                b = complex(rng.uniform(-2,2),rng.uniform(-2,2))
                actual=energy(radius,gap,a,b)/energy(1,gap,a,b)
                assert actual < radius**3
                assert actual <= max(even,odd)+1e-10
                total+=2
    for radius in (1.05,1.25,2,3,10):
        for gap in (0.004,0.002,0.001):
            a,b=0,1
            actual=energy(radius,gap,a,b)/energy(1,gap,a,b)
            assert 0 < radius**3-actual < 0.0001*radius**3
            total+=1
    # A few explicit quadrature evaluations to cross-check the trigonometric integral.
    for _ in range(60):
        radius=rng.uniform(1.1,3.0)
        gap=rng.uniform(0.1,9.0)
        a=complex(rng.uniform(-1,1),rng.uniform(-1,1))
        b=complex(rng.uniform(-1,1),rng.uniform(-1,1))
        n=1200
        dt=2*radius/n
        approx=0.0
        for j in range(n):
            t=-radius+(j+0.5)*dt
            approx+=abs(a*math.cos(gap*t/2)+b*math.sin(gap*t/2))**2*dt
        exact=energy(radius,gap,a,b)
        assert abs(approx-exact) <= 3.5e-5*(1+exact)
        total+=1
    print(f"PASS {total} supplementary assertions")

if __name__ == '__main__':
    check()
