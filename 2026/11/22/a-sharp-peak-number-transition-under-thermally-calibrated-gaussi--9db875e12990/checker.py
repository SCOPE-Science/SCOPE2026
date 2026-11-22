#!/usr/bin/env python3
"""Reproducibility checks for Gaussian-packet resetting in a harmonic trap.
Python 3 standard library only. Numerical checks corroborate, not replace, the proof.
"""
import math


def integrate_midpoint(f, n=16000):
    return sum(f((k + 0.5) / n) for k in range(n)) / n


def central_ratio(a, t):
    return (a - 1) * integrate_midpoint(lambda u: u ** (a - 1) * math.exp(t * (1-u*u)))


def root_t(a):
    assert a > 1
    lo, hi = 0.0, 1.0
    while central_ratio(a, hi) <= 1.0:
        hi *= 2.0
    for _ in range(54):
        mid = (lo + hi) * 0.5
        if central_ratio(a, mid) < 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) * 0.5


def ratio(a, t, w):
    if w < 1e-8:
        return central_ratio(a, t)
    return (a - 1) * integrate_midpoint(
        lambda u: u ** (a-2) * math.exp(t*(1-u*u)) * math.sinh(u*w) / math.sinh(w)
    )


def density(a, s, x):
    scale = 1.0 / math.sqrt(2.0 * math.pi * s)
    return a*scale*integrate_midpoint(
        lambda u: u**(a-1) * 0.5*(math.exp(-(x-u)**2/(2*s)) + math.exp(-(x+u)**2/(2*s)))
    )


def main():
    count = 0
    for a in [1.2, 1.5, 2.0, 3.0, 5.0, 12.0]:
        tc = root_t(a)
        assert abs(central_ratio(a, tc) - 1.0) < 2e-7
        count += 1
        assert central_ratio(a, 0.75*tc) < 1 < central_ratio(a, 1.25*tc)
        count += 1
        for t in [0.7*tc, tc, 1.3*tc]:
            rr = [ratio(a, t, w) for w in [0.01,0.5,1.,2.,3.,4.]]
            assert all(rr[k] > rr[k+1] for k in range(len(rr)-1)), (a,t,rr)
            count += 1
        at_low = ratio(a, 1.3*tc, 0.005)
        at_high = ratio(a, 1.3*tc, 10.0)
        assert at_low > 1 > at_high
        count += 1
    tc2 = root_t(2.0)
    assert abs(math.exp(tc2)-1-2*tc2) < 1e-7
    count += 1
    assert abs(tc2 - 1.2564312086263458) < 1e-6
    count += 1
    for a, s in [(0.5,0.35), (1.0,0.35),(1.2,1.0), (2.0,0.6), (5.0,0.9)]:
        pp = [density(a,s,x) for x in [0,0.1,0.2,0.4]]
        assert all(pp[i]>pp[i+1] for i in range(3)), (a,s,pp)
        count += 1
    for a in [1.2,2.0,3.0,5.0]:
        s = 0.8 / (2*root_t(a))
        x = math.sqrt(s)
        assert density(a,s,x) > density(a,s,0)
        count += 1
    # Moment identities: E[(X/L)^2]=s+a/(a+2), E[U^4]=a/(a+4).
    for a in [0.5,1.0,1.5,2.0,6.0]:
        E2 = integrate_midpoint(lambda u: a*u**(a-1)*u*u)
        E4 = integrate_midpoint(lambda u: a*u**(a-1)*u**4)
        assert abs(E2 - a/(a+2)) < 1e-5
        assert abs(E4 - a/(a+4)) < 1e-5
        count += 2
    # Opening law: x_mode^2 / (s_c - s) -> 3 as s increases to critical.
    a=2.0
    sc=1/(2*root_t(a))
    ratios=[]
    for eps in [0.02,0.01,0.005]:
        s=sc-eps
        t=1/(2*s)
        lo,hi=0.00001,10.0
        for _ in range(50):
            w=(lo+hi)/2
            if ratio(a,t,w)>1:lo=w
            else:hi=w
        x=s*(lo+hi)/2
        ratios.append(x*x/eps)
    assert abs(ratios[-1]-3) < 0.2, ratios
    assert abs(ratios[-1]-3) < abs(ratios[0]-3)
    count += 2
    print('PASS:', count, 'independent numerical identities and monotonicity checks')
    print('a=2 critical t=',format(tc2,'.12f'),'s_c=',format(sc,'.12f'))
    print('opening ratios=',[round(q,6) for q in ratios])

if __name__ == '__main__':
    main()
