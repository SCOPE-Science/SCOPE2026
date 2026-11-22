"""Finite numerical consistency tests for a two-state adaptive-feedback theorem.

These computations are illustrative; the global and asymptotic assertions
are established by the analytic proof in RESULT.md.
"""
import math


def step(x, theta, c, k, delta):
    return 0.5 + c * math.tanh(theta), (1-delta)*theta + delta*k*(x-0.5)


def cycle_amplitude(a, delta):
    assert 0 < a < 1 and 2/(1+a) < delta < 2
    lo, hi = 0.0, 1.0
    while (2-delta)*hi < delta*a*math.tanh(hi):
        hi *= 2
    for _ in range(80):
        r = (lo+hi)/2
        if (2-delta)*r < delta*a*math.tanh(r):
            lo = r
        else:
            hi = r
    return (lo+hi)/2


cases = 0
for a in (0.12, 0.37, 0.79):
    c = 0.2
    k = a/c
    critical = 2/(1+a)
    for delta in (0.5*critical, 0.98*critical, critical, (critical+2)/2):
        x, theta = 0.5, 0.5
        yprev = theta
        ycurr = -((1-delta)*theta + delta*k*(x-0.5))
        seq = [theta]
        for n in range(10000):
            x, theta = step(x, theta, c, k, delta)
            assert 0 <= x <= 1
            seq.append(theta)
            if n >= 1:
                prior = seq[-3]
                predicted = (1-delta)*seq[-2]+delta*a*math.tanh(prior)
                assert abs(seq[-1]-predicted) < 1e-10
                cases += 1
        if delta < critical-1e-10:
            assert abs(theta) < 1e-7
        elif delta > critical+1e-10:
            r = cycle_amplitude(a,delta)
            assert abs(abs(theta)-r)<1e-7
            jac_feedback = delta*a/(math.cosh(r)**2)
            assert jac_feedback < 2-delta
        else:
            b=delta*a
            target=3*(1+b)/(2*b)
            estimate=10000*theta**2
            assert abs(estimate/target-1)<0.01
            print('critical a=',a,'n*theta^2=',round(estimate,8),'theory=',round(target,8))
print('PASS physical-map/delayed-recurrence, convergence, cycle, critical-law:',cases,'recurrence comparisons')
