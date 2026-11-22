"""Independent numerical consistency checks for the exact two-axis reliability law.

Standard Python library only.  Monte Carlo and quadrature support, but do not
constitute, the analytic proof in RESULT.md.
"""
import math
import random
import statistics


def direct(k, u, v):
    """Original single-trait Gaussian quadratic-form covariance identity."""
    w1, w2 = math.sqrt(k)*u, v
    norm2 = w1*w1+w2*w2
    return ((k*w1*w1+w2*w2)/norm2)**2/(k*k+1)


def cdf(k, x):
    if k == 1:
        return float(x >= 0.5)
    lo, hi = 1/(k*k+1), k*k/(k*k+1)
    if x <= lo: return 0.
    if x >= hi: return 1.
    r = math.sqrt((k*k+1)*x)
    return 2/math.pi*math.atan(math.sqrt((r-1)/(k*(k-r))))


def mean(k):
    return ((k+1)**2-1.5*(k+1)*math.sqrt(k))/(k*k+1)


def median(k):
    return (k*k+1)/(k+1)**2


def simpson_integral(k, n=20000):
    """Angular integral of original coefficient, independent of CDF inversion."""
    h = (math.pi/2)/n
    ss = 0.
    for j in range(n+1):
        theta = j*h
        co, si = math.cos(theta), math.sin(theta)
        ratio = (k*k*co*co+si*si)/(k*co*co+si*si)
        f = ratio*ratio/(k*k+1)
        ss += (1 if j==0 or j==n else 4 if j%2 else 2)*f
    return (2/math.pi)*(h/3)*ss


def main():
    assert direct(1, 3, 5) == .5
    assert abs(mean(4)-10/17) < 1e-14
    assert abs(median(4)-17/25) < 1e-14
    for k in [1, 1.1, 2, 4, 11, 100]:
        assert abs(simpson_integral(k)-mean(k)) < 2e-10, k
        assert abs(cdf(k, median(k))-0.5) < 1e-10 if k > 1 else cdf(k,0.5)==1
        if k > 1:
            lo, hi = 1/(k*k+1), k*k/(k*k+1)
            assert cdf(k, lo) == 0 and cdf(k, hi) == 1
            assert 0 < cdf(k, mean(k)) < 1
            for u,v in [(1,1), (.1,1), (2,3)]:
                assert abs(direct(k,u,v)-((k*k*u*u+v*v)/(k*u*u+v*v))**2/(k*k+1)) < 1e-12
    rng = random.Random(62457)
    for k in [1.1, 4., 16.]:
        sample = [direct(k, rng.gauss(0,1), rng.gauss(0,1)) for _ in range(60000)]
        assert abs(statistics.fmean(sample)-mean(k)) < .01, ('mean',k)
        assert abs(statistics.median(sample)-median(k)) < .015, ('median',k)
        for x in [(.5 if k>1 else .5),.75]:
            empirical = sum(q<=x for q in sample)/len(sample)
            assert abs(empirical-cdf(k,x)) < .015, ('cdf',k,x,empirical,cdf(k,x))
    # Exact upper/lower endpoint interpretations, not a sampling proof.
    for k in [2.,4.,100.]:
        assert abs(direct(k,1,0)-k*k/(k*k+1))<1e-14
        assert abs(direct(k,0,1)-1/(k*k+1))<1e-14
    print('PASS: 6 angular integrations, exact cases and 3 seeded Gaussian samples.')


if __name__ == '__main__':
    main()
