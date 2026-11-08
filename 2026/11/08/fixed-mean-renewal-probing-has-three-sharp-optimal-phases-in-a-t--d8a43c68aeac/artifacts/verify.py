#!/usr/bin/env python3
"""Independent finite checks of the stated two-level mean-budget theorem.

These checks corroborate formulas and sample inequalities; the global
optimization and uniqueness assertions are proved analytically in RESULT.md.
"""
import math
import random


def bisect_root():
    lo, hi = math.pi / 4, math.pi / 2
    for _ in range(130):
        mid = (lo + hi) / 2
        if math.tan(mid) > 2 * mid:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


XC = bisect_root()
SLOPE = math.sin(XC) ** 2 / XC


def envelope(x):
    assert x >= 0
    if x <= XC:
        return SLOPE * x
    if x < math.pi / 2:
        return math.sin(x) ** 2
    return 1.0


def success(x):
    return math.sin(x) ** 2


def optimal_law(m):
    """Return support-probability pairs; includes zero if m<XC."""
    assert m > 0
    if m < XC:
        return [(0.0, 1 - m / XC), (XC, m / XC)]
    if m <= math.pi / 2:
        return [(m, 1.0)]
    k = math.floor((m - math.pi / 2) / math.pi)
    left = math.pi / 2 + k * math.pi
    w = (m - left) / math.pi
    return [(left, 1 - w), (left + math.pi, w)]


def qavg(law):
    return sum(p * success(x) for x, p in law)


def mean(law):
    return sum(x * p for x, p in law)


def check(cond, message):
    if not cond:
        raise AssertionError(message)


def run():
    count = 0
    def test(ok, msg):
        nonlocal count
        check(ok, msg)
        count += 1
    test(math.pi / 4 < XC < math.pi / 2, "critical root location")
    test(abs(math.tan(XC) - 2 * XC) < 1e-13, "critical tangent")
    test(abs(2 * math.sin(XC) * math.cos(XC) - SLOPE) < 1e-13, "slope matching")
    test(abs(XC - 1.1655611852072303) < 1e-13, "critical root numeric")
    test(abs(XC / math.sin(XC)**2 - 1.380050139689301) < 1e-13, "unconstrained time constant")

    for m in (0.03, 0.15, 0.52, XC, 1.30, math.pi/2, 1.9, 2.8, 4.9, 10.2):
        law = optimal_law(m)
        test(abs(mean(law) - m) < 2e-14, "optimizer mean")
        test(abs(qavg(law) - envelope(m)) < 2e-14, "optimizer success envelope")
        test(abs(sum(w for _, w in law) - 1) < 2e-14, "optimizer probabilities")
        test(all(-1e-14 <= w <= 1+1e-14 for _, w in law), "admissible weights")

    rng = random.Random(4137)
    for _ in range(1600):
        x = rng.uniform(0, 30)
        test(success(x) <= envelope(x) + 3e-14, "pointwise supporting majorant")
    for _ in range(600):
        a,b,c = sorted(rng.uniform(0, 30) for _ in range(3))
        w = rng.random()
        test(envelope((1-w)*a+w*c) >= (1-w)*envelope(a)+w*envelope(c)-3e-14, "concavity witness")
    for _ in range(800):
        m = rng.uniform(0.02, 18)
        a = rng.uniform(0, m)
        b = m+rng.uniform(0,18)
        w = (b-m)/(b-a)
        law = [(a,w),(b,1-w)]
        test(qavg(law) <= envelope(m)+3e-14, "fixed-mean two-point upper bound")

    # Direct two-state unitary/projection identities, including nonzero detuning.
    for d,re,im,t in ((0.,1.,0.,0.4), (0.6,1.2,0.4,0.8),
                      (2.4,0.7,-0.2,3.2),(-1.1,0.7,0.6,1.2)):
        om=math.sqrt(d*d+re*re+im*im)
        v=complex(re,im)
        u00=math.cos(om*t)-1j*math.sin(om*t)*d/om
        u10=-1j*math.sin(om*t)*v.conjugate()/om
        a=(re*re+im*im)/(om*om)
        test(abs(abs(u10)**2-a*math.sin(om*t)**2)<2e-14,"direct quantum transfer")
        test(abs(abs(u00)**2+abs(u10)**2-1)<2e-14,"failed-projection norm")
        test(abs(abs(u00)**2-(1-a*math.sin(om*t)**2))<2e-14,"renewal failure probability")

    # Two admissible finite-support protocols with the same mean,
    # checking the expected elapsed time from the attempt-wise geometric sum.
    for m in (0.35, 1.37, 2.31, 6.2):
        law = optimal_law(m)
        p = 0.75*qavg(law)
        exact = m/p
        partial = sum(m*(1-p)**j for j in range(2500))
        test(abs(exact-partial) < 5e-11,"geometric renewal sum")
    print('PASS',count,'diagnostic assertions')
    print('x_c = %.17f' % XC)
    print('sin^2(x_c)/x_c = %.17f' % SLOPE)
    print('unconstrained infimum in units 1/(A Omega) = %.17f' % (1/SLOPE))

if __name__ == '__main__':
    run()
