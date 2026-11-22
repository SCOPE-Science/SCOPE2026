"""Standalone elementary checks of the stated ballistic threshold-reset averaging theorem.
Run: python verify.py (Python standard library only).
"""
import random
from fractions import Fraction
from math import gamma

rng = random.Random(20261115)


def Flinear(x, a):
    return x * (a - x) / 2


def Glinear(x, v, a):
    return Flinear(x, a) / v


def exact_integral_linear(a, age, v, dt):
    # X(s)=a-v*(age+s): integrate X-a/2 over one interval.
    return (a / 2 - v * age) * dt - v * dt * dt / 2


def check_coboundary():
    for n in (2, 3, 4, 6):
        for _ in range(1500):
            a = rng.uniform(0.1, 3)
            v0 = rng.uniform(0.3, 5)
            duration = a * rng.gammavariate(n - 1, 1) / v0
            v = a / duration
            age0 = duration * rng.random()
            dt = (duration - age0) * rng.random()
            x0 = a - v * age0
            x1 = x0 - v * dt
            lhs = exact_integral_linear(a, age0, v, dt)
            rhs = Glinear(x1, v, a) - Glinear(x0, v, a)
            assert abs(lhs - rhs) <= 1e-10 * max(1, abs(lhs), abs(rhs))


def stationary_endpoint(a, v0, n):
    # Stationary speed is length-biased: W=v0/V ~ Gamma(n,1)
    w = rng.gammavariate(n, 1.)
    u = rng.random()
    return a*a/(2*v0) * w * u * (1-u)


def fresh_at_time(t, a, v0, n):
    # Starts exactly at reset at time zero, then runs complete i.i.d. cycles.
    s = 0.
    while True:
        w = rng.gammavariate(n-1, 1.)
        T = a*w/v0
        if s + T > t:
            u = (t-s)/T
            return a*a/(2*v0) * w*u*(1-u)
        s += T


def stationary_at_time(t, a, v0, n):
    # Equilibrium initial cycle: size-biased duration and uniform phase.
    w = rng.gammavariate(n, 1.)
    u = rng.random()
    h0 = a*a/(2*v0) * w*u*(1-u)
    residual = a*w/v0 * (1-u)
    if residual > t:
        u1 = u + t*v0/(a*w)
        ht = a*a/(2*v0)*w*u1*(1-u1)
    else:
        ht = fresh_at_time(t-residual, a, v0, n)
    return ht-h0


def variance(xs):
    mean=sum(xs)/len(xs)
    return sum((x-mean)**2 for x in xs)/len(xs)


def check_exact_coefficients():
    # F(U)=a^2 U(1-U)/2, E U(1-U)=1/6 and E U^2(1-U)^2=1/30.
    for n in (2,3,4,7,20):
        ez=Fraction(n,12)
        ez2=Fraction(n*(n+1),120)
        var=ez2-ez**2
        assert var == Fraction(n*(n+6),720)
        assert 2*var == Fraction(n*(n+6),360)
    assert Fraction(2*3*9,720) == Fraction(3,40)


def check_simulation():
    a, v0, n = 1., 1., 3
    expect_mean=a*a*n/(12*v0)
    expect_var=a**4*n*(n+6)/(720*v0*v0)
    z=[stationary_endpoint(a,v0,n) for _ in range(50000)]
    assert abs(sum(z)/len(z)-expect_mean)<0.009
    assert abs(variance(z)-expect_var) < 0.004
    # Two different preparations. The constants are approached at long windows.
    t=75.
    stat=[stationary_at_time(t,a,v0,n) for _ in range(20000)]
    fresh=[fresh_at_time(t,a,v0,n) for _ in range(20000)]
    assert abs(variance(stat)-2*expect_var) < 0.009, (variance(stat),2*expect_var)
    assert abs(variance(fresh)-expect_var) < 0.006, (variance(fresh),expect_var)
    assert abs(sum(fresh)/len(fresh)-expect_mean) < 0.012
    print('n=3 predicted endpoint mean:',expect_mean)
    print('n=3 predicted endpoint variance:',expect_var)
    print('n=3 stationary t^2 variance estimate:',variance(stat),'theory:',2*expect_var)
    print('n=3 fresh-start t^2 variance estimate:',variance(fresh),'theory:',expect_var)

if __name__=='__main__':
    check_coboundary()
    check_exact_coefficients()
    check_simulation()
    print('PASS: 6000 pathwise identities, exact rational coefficients, stationary and fresh-start Monte Carlo.')
