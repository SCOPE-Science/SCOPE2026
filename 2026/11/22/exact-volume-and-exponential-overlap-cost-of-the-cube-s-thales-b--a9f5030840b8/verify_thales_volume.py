"""Numerical checks for cube Thales-ball union volume.

Only finite checks: the all-dimensional identities and the asymptotic
statement are proved in RESULT.md.
"""
import math
import random


def half_normal_coefficient(k):
    return math.exp(0.5*k*math.log(2.0)
                    + math.lgamma((k+1)/2)
                    - 0.5*math.log(math.pi) - math.lgamma(k+1))


def volume_via_moment(n):
    a = [half_normal_coefficient(k) for k in range(n+1)]
    p = [1.0] + [0.0]*n
    for _ in range(n):
        q = [0.0]*(n+1)
        for j in range(n+1):
            if p[j]:
                for k in range(n-j+1):
                    q[j+k] += p[j]*a[k]
        p = q
    return 2.0*(math.pi/2)**(n/2)*p[n]


def normal_pdf(t):
    return math.exp(-t*t/2)/math.sqrt(2*math.pi)


def normal_cdf(t):
    return (1+math.erf(t/math.sqrt(2)))/2


def saddle():
    lo, hi = 0.0, 1.0
    for _ in range(80):
        t = (lo+hi)/2
        g = t*t + t*normal_pdf(t)/normal_cdf(t)
        if g < 1:
            lo = t
        else:
            hi = t
    z = (lo+hi)/2
    r = normal_pdf(z)/normal_cdf(z)
    variance = z*(2*z + r - z*r*(z+r))
    f = 2.0*math.exp(z*z/2)*normal_cdf(z)
    growth = math.sqrt(math.pi/8)*f/z
    return z, variance, growth


def verify():
    targets = {1: 2, 2: 2+math.pi, 3: 2+4*math.pi,
               4: 2+10*math.pi+math.pi**2,
               5: 2+20*math.pi+41*math.pi**2/6}
    for n, expected in targets.items():
        got = volume_via_moment(n)
        assert abs(got/expected-1) < 5e-13, (n, got, expected)
    z, b, growth = saddle()
    assert abs(z-0.83992367569237) < 1e-12
    assert abs(b-1.41094356197717) < 1e-11
    assert abs(growth-1.69763020222053) < 1e-11
    for n in (16, 32, 64):
        exact_ratio = volume_via_moment(n) / (2.0**n)
        estimate = 2*growth**n/math.sqrt(2*math.pi*n*b)
        assert abs(exact_ratio/estimate-1) < 0.15/n, (n,exact_ratio/estimate)
    # Independent geometric integration using random sphere directions.
    rng = random.Random(274618)
    samples = 100000
    n = 3
    total = 0.0
    for _ in range(samples):
        xs = [rng.gauss(0, 1) for j in range(n)]
        r = math.sqrt(sum(x*x for x in xs))
        total += (sum(abs(x) for x in xs)/r)**n
    estimate = math.pi**(n/2)/math.gamma(n/2+1)*total/samples
    assert abs(estimate-(2+4*math.pi)) < 0.16, estimate
    # Midpoint angular quadrature in dimension two.
    dt = math.pi/50000
    integral = 0.0
    for i in range(50000):
        t = (i+0.5)*dt
        integral += (abs(math.sin(t))+abs(math.cos(t)))**2
    integral *= dt
    assert abs(integral-(2+math.pi)) < 1e-7
    print('PASS: numerical checks of low-dimensional moments, saddle constants,')
    print('      finite-size asymptotic, independent geometric integrals')


if __name__ == '__main__':
    verify()
