"""Reproduce bounded numerical identities for a resetting-rate refresh comparison.

All universal claims are established by the accompanying mathematical proof;
these numerical tests are illustrative checks, not a substitute for that proof.
Run with: python3 verify.py
"""
import math


def phi(t, rates, weights):
    return sum(p * math.exp(-rate * t) for p, rate in zip(weights, rates))


def s_two(t, mu, a, b):
    mean = (a + b) / 2.0
    gap = (b - a) / 2.0
    w = math.hypot(gap, mu / 2.0)
    # Two exponentials avoid overflow at large t.
    upper = 0.5 * (1 + mu / (2 * w))
    lower = 0.5 * (1 - mu / (2 * w))
    return upper * math.exp(-(mean + mu / 2 - w) * t) + lower * math.exp(-(mean + mu / 2 + w) * t)


def rk_survival(t, mu, rates, weights, steps=1800):
    """Numerically integrate the independent rate-refresh Feynman--Kac ODE."""
    n = len(rates)
    y = [1.] * n
    h = t / steps

    def rhs(v):
        avg = sum(p * val for p, val in zip(weights, v))
        return [-(rates[i] + mu) * v[i] + mu * avg for i in range(n)]

    for _ in range(steps):
        k1 = rhs(y)
        k2 = rhs([y[j] + h * k1[j] / 2 for j in range(n)])
        k3 = rhs([y[j] + h * k2[j] / 2 for j in range(n)])
        k4 = rhs([y[j] + h * k3[j] for j in range(n)])
        y = [y[j] + h * (k1[j] + 2*k2[j] + 2*k3[j] + k4[j]) / 6 for j in range(n)]
    return sum(p * val for p, val in zip(weights, y))


def simpson(f, a, b, n=2400):
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for j in range(1, n):
        total += (4 if j % 2 else 2) * f(a + j * h)
    return total * h / 3


def tail_two(r, mu, a, b, D=1.):
    # Integration by parts: E h(A) = integral_0^infinity S(t) dh(t)
    # h(t)=erfc(r/sqrt(4Dt)) for d=1.
    def integrand(t):
        if t == 0:
            return 0.
        return s_two(t, mu, a, b) * (r / (2*math.sqrt(math.pi * D))) * t**(-1.5) * math.exp(-r*r/(4*D*t))
    return simpson(lambda u: 2*u*integrand(u*u), 0, math.sqrt(70), 4800)


def one_split_gap(t, mu1, mu2, rates, weights):
    delta = mu2 - mu1
    return delta * math.exp(-mu2*t) * simpson(
        lambda s: phi(t,rates,weights) - phi(s,rates,weights)*phi(t-s,rates,weights), 0, t, 600)


def main():
    tests = 0
    rates = [0.7, 2.3]
    weights = [0.5, 0.5]
    mean = sum(p * r for p,r in zip(weights,rates))
    for t in [0.05,0.2,0.8,1.7,3.1]:
        arr = [s_two(t,mu,*rates) for mu in [0.,0.25,1.,4.,13.]]
        assert all(arr[j] > arr[j+1] for j in range(len(arr)-1))
        assert math.exp(-mean*t) < arr[-1] < arr[0]
        assert abs(arr[0]-phi(t,rates,weights))<1e-12
        tests+=3
        for mu in [0., 0.2, 0.8, 2., 5.]:
            assert abs(s_two(t,mu,*rates)-rk_survival(t,mu,rates,weights,steps=1300))<2e-10
            tests+=1
        for m1,m2 in [(0,0.25),(.2,1.),(1.,2.)]:
            assert s_two(t,m1,*rates)-s_two(t,m2,*rates)+1e-15>=one_split_gap(t,m1,m2,rates,weights)
            tests+=1
    # Independent three-atom check: tests full-law rather than the two-state formula.
    rates3 = [0.3,1.4,3.]
    weights3 = [0.2,0.3,0.5]
    m3 = sum(r*p for r,p in zip(rates3,weights3))
    for t in [0.1,0.5,1.6,3.]:
        values = [rk_survival(t,mu,rates3,weights3) for mu in [0,.2,.8,2.,5.]]
        assert all(values[i] > values[i+1] for i in range(4))
        assert math.exp(-m3*t)<values[-1]<phi(t,rates3,weights3)
        for j in range(4):
            assert values[j] - values[j+1]+1e-13 >=one_split_gap(t,[0,.2,.8,2.,5.][j],[0,.2,.8,2.,5.][j+1],rates3,weights3)
            tests+=1
        tests+=2
    a,b = rates
    for mu in [0.,0.3,1.,4.,12.]:
        analytic = 2.0 * (mean + mu) / (a*b + mu*mean)
        integrated = 2.0 * simpson(lambda t: s_two(t,mu,a,b),0,65,4400)
        assert abs(analytic-integrated)<2e-6
        tests+=1
    for r in [.5,1.,2.,3.]:
        tails = [tail_two(r,mu,a,b) for mu in [0.,.5,3.,10.]]
        assert all(tails[i] > tails[i+1] + 1e-6 for i in range(len(tails)-1))
        frozen = 0.5*(math.exp(-r*math.sqrt(a))+math.exp(-r*math.sqrt(b)))
        assert abs(tails[0] - frozen)<1e-5
        assert tails[-1]>math.exp(-r*math.sqrt(mean))
        tests+=3
    print('PASS', tests, 'bounded Feynman--Kac, strict ordering, partition-gap, variance and Brownian-tail checks')


if __name__ == '__main__':
    main()
