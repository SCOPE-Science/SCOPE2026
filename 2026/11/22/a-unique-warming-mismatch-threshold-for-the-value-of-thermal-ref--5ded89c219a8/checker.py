"""Reproducible numerical stress tests for the two-thermal-patch theorem.

The theorem is proved analytically; finite tests are independent diagnostics,
not a substitute for the universal proof.
"""
import math
import random


def bounds(a):
    p = math.exp(-0.5 * a * a)
    return a / 2, math.acosh(1 / p) / a


def limit_rate(a, x, R, mu, m):
    q = math.exp(-x * x / 2)
    p = math.exp(-a * a / 2)
    c, s = math.cosh(a*x), math.sinh(a*x)
    return R*q*p*c - mu - m + math.hypot(m, R*q*p*s)


def baseline(a, x, R, mu, m):
    return R * math.exp(-x*x/2) - mu


def critical_migration(a, x, R):
    p = math.exp(-a*a/2)
    z = p * math.cosh(a*x)
    return R*math.exp(-x*x/2) * (2*z - 1 - p*p)/(2*(1-z))


def critical_mismatch(a, R, m):
    lo, hi = bounds(a)
    for _ in range(110):
        mid = (lo+hi)/2
        if critical_migration(a, mid, R) < m:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def run():
    rng = random.Random(20240301)
    checks = 0
    for _ in range(4500):
        a = rng.uniform(0.15, 2.8)
        R = rng.uniform(0.3, 3)
        mu = rng.uniform(0, 1.5)
        x1, x2 = bounds(a)
        x = x1 + (x2-x1)*rng.uniform(0.05,0.95)
        M = critical_migration(a,x,R)
        assert M > 0
        vslow = limit_rate(a,x,R,mu,M*0.6)-baseline(a,x,R,mu,M*0.6)
        vfast = limit_rate(a,x,R,mu,M*1.4)-baseline(a,x,R,mu,M*1.4)
        assert vslow>1e-12 and vfast < -1e-12, (a,R,x,M,vslow,vfast)
        checks += 2
        m = rng.uniform(0.001,4)
        xcrit = critical_mismatch(a,R,m)
        assert x1 < xcrit < x2
        zlo = (x1 + xcrit)/2
        zhi = (x2 + xcrit)/2
        assert limit_rate(a,zlo,R,mu,m) < baseline(a,zlo,R,mu,m)
        assert limit_rate(a,zhi,R,mu,m) > baseline(a,zhi,R,mu,m)
        checks += 3
    for a in (0.25,0.5,1,2):
        R=1.3
        x1,x2=bounds(a)
        prev=-1
        for k in range(1,300):
            x=x1+(x2-x1)*k/300
            val=critical_migration(a,x,R)
            assert val > prev
            prev=val
            checks+=1
        for m in (1e-5, 5e-5):
            x=critical_mismatch(a,R,m)
            c0=math.exp(a*a/8)/(R*a)
            assert abs((x-x1)/m/c0-1)<0.002
            checks+=1
        p=math.exp(-a*a/2)
        c2=R*math.exp(-x2*x2/2)*math.sqrt(1-p*p)/(2*a)
        for m in (500,2000):
            x=critical_mismatch(a,R,m)
            assert abs((x2-x)*m/c2-1)<0.01
            checks+=1
    return checks

if __name__ == '__main__':
    print(f'PASS: {run()} supplementary assertions')
