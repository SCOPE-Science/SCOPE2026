"""Numerical consistency tests for finite-N first-passage resetting stationary escape tails.

Uses Python's standard library only. These tests are bounded checks, not the proof
of any limit or moment-existence claim.
"""
import math


def simpson(fn, end, panels=20000):
    assert panels % 2 == 0
    h = end / panels
    s = fn(0.0) + fn(end)
    for i in range(1, panels):
        s += (4 if i % 2 else 2) * fn(i * h)
    return s * h / 3


def tau(n):
    # Integration by parts of (1/2)int erf(u)^n/u^3 du.
    def density(u):
        if u == 0.0:
            return 6 / math.pi**1.5 if n == 3 else 0.0
        return n / (2*math.sqrt(math.pi)) * math.erf(u)**(n - 1) * math.exp(-u*u) / (u*u)
    return simpson(density, 8, 30000)


def tail_constant(n):
    return 2**(n-2) * math.gamma((n-2)/2) / (math.pi**(n/2)*tau(n))


def event_integral(n, thresholds, R, panels=16000):
    epsilon = 1 / R
    k = len(thresholds)
    def integrand(w):
        if w == 0.0:
            return (2*epsilon/math.sqrt(math.pi))**n if n == 3 else 0.0
        product = math.erf(epsilon*w)**(n-k)
        for a in thresholds:
            h = (math.erf((a+epsilon)*w)-math.erf((a-epsilon)*w))/2
            product *= h
        return product/(w*w*w)
    return simpson(integrand, 12, panels)


def exact_event_probability(n, thresholds, R):
    return R*R/(2*tau(n))*event_integral(n,thresholds,R)


def rayleigh_moment(p, t):
    delta = 1/math.sqrt(4*t)
    def fn(z):
        return z**p * (math.exp(-(z-delta)**2)-math.exp(-(z+delta)**2)) / (math.sqrt(math.pi)*math.erf(delta))
    return simpson(fn, 9, 18000)


def run():
    checks = 0
    # Scaling integral and integration-by-parts normalization are independent.
    for n in (3,4,5,7):
        got=tau(n)
        assert got > 0
        # The u>14 remainder of direct integral is 1/(4*14^2) to machine precision.
        eps=1e-5
        def direct(u):
            if u==0: return (2/math.sqrt(math.pi))**3/2 if n==3 else 0.0
            return .5 * math.erf(u)**n/u**3
        direct_val=simpson(lambda x:direct(x+eps),14-eps,36000)+1/(4*14**2)
        assert abs(got-direct_val)<3e-5, (n,got,direct_val)
        checks+=2

    for n in (3,4,5,7):
        for a in ((1.0,), (1.0,1.0), (1.0,2.0,3.0)):
            if len(a)>n:continue
            for R in (20.0,50.0):
                actual=exact_event_probability(n,a,R)
                alpha=(n-2)/2
                asymptotic=tail_constant(n)*(sum(v*v for v in a))**(-alpha)*R**(-(n-2))
                assert abs(actual/asymptotic-1)<0.002, (n,a,R,actual/asymptotic)
                checks+=1

    for p in (0.,0.5,1.,2.,4.):
        val=rayleigh_moment(p,10000)
        assert abs(val/math.gamma(1+p/2)-1)<0.0008,(p,val)
        checks+=1

    for n in (3,5,7):
        for k in (1,2,3):
            a=(1.,)*k
            raw=tail_constant(n)*k**(-(n-2)/2)
            assert abs(raw/tail_constant(n)-k**(-(n-2)/2))<1e-12
            checks+=1
    print('PASS:',checks,'bounded numerical/integral checks')
    print('normalizers:',', '.join('N=%d: %.12f'%(n,tau(n)) for n in (3,4,5,7)))
    print('C_3:', format(tail_constant(3),'.12f'))


if __name__ == '__main__':
    run()
