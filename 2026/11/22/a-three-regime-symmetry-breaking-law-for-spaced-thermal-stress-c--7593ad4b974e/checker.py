#!/usr/bin/env python3
"""Reproducibility checks for a two-memory, three-pulse mathematical benchmark.

The mathematical proof is analytic; finite checks below are supplemental.
Requires only the Python standard library.
"""
import math
import random


def boundaries(alpha, beta, T):
    assert 0 < alpha < beta and T > 0
    qe = (alpha / beta) * (-math.expm1(-alpha*T)) / (-math.expm1(-beta*T))
    qc = (alpha / beta)**2 * math.exp((beta-alpha)*T/2)
    return qe, qc


def variable_cost(t, T, alpha, beta, q):
    return q*(math.exp(-beta*t)+math.exp(-beta*(T-t))) - (math.exp(-alpha*t)+math.exp(-alpha*(T-t)))


def root_deviation(alpha, beta, q, T):
    qe, qc = boundaries(alpha, beta, T)
    if q <= qe: return T/2
    if q >= qc: return 0.0
    target = alpha*math.exp((beta-alpha)*T/2)/(q*beta)
    left, right = 0.0, T/2
    for _ in range(85):
        mid = (left+right)/2
        ratio = beta/alpha if mid == 0 else math.sinh(beta*mid)/math.sinh(alpha*mid)
        if ratio < target: left = mid
        else: right = mid
    return (left+right)/2


def optimal_times(alpha, beta, q, T):
    z = root_deviation(alpha, beta, q, T)
    times = sorted([T/2-z, T/2+z])
    return [times[0]] if abs(times[1]-times[0]) < 1e-13 else times


def check():
    alpha, beta, q = 1.0, 3.0, .2
    Tc = math.log(9/5)
    Te = math.log(6/(math.sqrt(33)-3))
    assert abs(boundaries(alpha,beta,Tc)[1]-q) < 1e-14
    assert abs(boundaries(alpha,beta,Te)[0]-q) < 1e-14
    assert Tc < Te
    assert len(optimal_times(alpha,beta,q,.3)) == 1
    mid = optimal_times(alpha,beta,q,.7)
    assert len(mid) == 2 and abs(mid[0]-.055825985792) < 5e-11
    assert abs(mid[1]-(.7-mid[0])) < 1e-13
    assert optimal_times(alpha,beta,q,1.0) == [0.0,1.0]
    tests = 0
    rng = random.Random(20261121)
    for i in range(7000):
        a = rng.uniform(.2,3.0)
        b = a+rng.uniform(.25,3.8)
        T = rng.uniform(.05,6.0)
        qe, qc = boundaries(a,b,T)
        q = (qe * rng.uniform(.4,.98) if i%3==0 else
             qc * rng.uniform(1.02,2.5) if i%3==1 else
             qe+(qc-qe)*rng.uniform(.01,.99))
        sol = optimal_times(a,b,q,T)
        best = variable_cost(sol[0],T,a,b,q)
        for t in sol:
            assert abs(variable_cost(t,T,a,b,q)-best) < 3e-12
        for j in range(65):
            t = T*j/64
            assert variable_cost(t,T,a,b,q) >= best-3e-10, (a,b,q,T,t,sol)
            tests += 1
        if i%3==2:
            assert 0 < sol[0] < T/2 < sol[1] < T
    # The two minima bifurcate with a universal square-root displacement.
    for dt in (1e-3,1e-4,1e-5):
        T=Tc+dt
        z = T/2 - optimal_times(alpha,beta,q=.2,T=T)[0]
        assert abs(z/math.sqrt(dt) - math.sqrt(3/(alpha+beta))) < 1e-2
    # Large-T smaller branch converges to the optimum for one lag.
    for q in (.4,.6,1.0):
        target = math.log(q*beta/alpha)/(beta-alpha)
        t=optimal_times(alpha,beta,q,40.0)[0]
        assert abs(t-target) < 1e-6
    # Baseline hazards are nonnegative even for immediate sequential pulses.
    q = .2
    for T in (.1,.7,2.0):
        for t in (0,T/2,T):
            times=(0,t,T)
            for j in range(3):
                hazard = 3.0 + sum(q*math.exp(-beta*(times[j]-times[i]))-math.exp(-alpha*(times[j]-times[i])) for i in range(j))
                assert hazard >= 1.0
    print('PASS: 7,000 parameter designs; %d grid inequalities; exact thresholds; fold and long-horizon tests'%tests)
    print('Exact witness: Tc=%.15f Te=%.15f intermediate=(%.12f, %.12f)'%(Tc,Te,mid[0],mid[1]))


if __name__ == '__main__':
    check()
