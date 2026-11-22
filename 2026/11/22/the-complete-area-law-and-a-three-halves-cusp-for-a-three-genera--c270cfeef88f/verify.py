"""Standalone numerical checks for the three-unit-segment random zonogon area law."""
import math
import random

PI = math.pi
AMAX = 1.5 * math.sqrt(3.0)

def area_from_gaps(x, y):
    return math.sin(x) + math.sin(y) + math.sin(PI - x - y)

def strip_length(t, x):
    lo = 2.0 * math.sin(x)
    hi = math.sin(x) + 2.0 * math.cos(x / 2.0)
    if t <= lo:
        return PI - x
    if t >= hi:
        return 0.0
    q = (t - math.sin(x)) / (2.0 * math.cos(x / 2.0))
    return PI - 2.0 * math.asin(max(-1.0, min(1.0, q)))

def tail(t, n=60000):
    if t <= 0.0:
        return 1.0
    if t >= AMAX:
        return 0.0
    step = PI / n
    return 2.0 / (PI * PI) * step * sum(
        strip_length(t, (i + .5) * step) for i in range(n))


def main():
    random.seed(713691)
    n = 300000
    levels = (0.2, 0.5, 1.0, 1.8, 2.0, 2.3, 2.5)
    counts = [0] * len(levels)
    total = 0.0
    for _ in range(n):
        # Fix the first (labelled) projective direction at zero by rotation.
        u, v = sorted((PI * random.random(), PI * random.random()))
        a = area_from_gaps(u, v-u)
        total += a
        for j, t in enumerate(levels):
            if a >= t:
                counts[j] += 1
    assert abs(total/n - 6.0/PI) < .006, (total/n, 6.0/PI)
    for t, k in zip(levels, counts):
        exact = tail(t)
        empirical = k/n
        assert abs(empirical-exact) < .006, (t, exact, empirical)
        print('CDF survival at',t,'analytic',round(exact,9),'sample',round(empirical,9))
    for i in range(400):
        t1, t2, t3 = (PI * random.random() for _ in range(3))
        direct = sum(abs(math.sin(u-v)) for u,v in ((t1,t2),(t1,t3),(t2,t3)))
        angles = sorted((t1,t2,t3))
        x,y,z = angles[1]-angles[0],angles[2]-angles[1],PI-angles[2]+angles[0]
        assert abs(direct - (math.sin(x)+math.sin(y)+math.sin(z))) < 1e-12
    for e in (0.1, 0.05, 0.02):
        low=(1-tail(e))/e**2
        high=tail(AMAX-e)/e
        assert abs(low-3/(4*PI**2)) < .004, (e,low)
        assert abs(high-8/(3*PI)) < .025, (e,high)
        print('endpoint epsilon',e,'low/e^2',round(low,8),'high/e',round(high,8))
    for h in (.05,.02,.01):
        cusp=(tail(2-h)+tail(2+h)-2*tail(2))/h**1.5
        assert abs(cusp+8/PI**2)<.08,(h,cusp)
        print('interior cusp h',h,'symmetric difference / h^1.5',round(cusp,8))
    print('PASS: exact planar determinant equivalence, numerical CDF, mean, endpoint and interior cusp checks')

if __name__ == '__main__': main()
