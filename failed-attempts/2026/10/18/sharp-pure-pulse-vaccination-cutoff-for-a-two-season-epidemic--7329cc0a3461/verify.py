"""Finite independent checks of a two-season pure-pulse optimality theorem.

Analytical arguments, not the finite tests, establish the all-measure theorem.
Run with: python3 verify.py
"""
import math
import random


def transmission(s, high, low, change):
    return high if s < change else low


def annual_cost(pulses, delta, period, change, high, low):
    """Exact affine period map and elementary exponential integrals.

    Pulses are within [0, period); each (time,mass) is a removal impulse.
    """
    events = sorted(pulses)
    assert all(0 <= s < period and mass >= 0 for s, mass in events)

    def pass_once(x, measure_cost):
        current = 0.0
        objective = 0.0
        for t, mass in events + [(period, 0.0)]:
            assert t >= current
            for left, right in [(current, min(t, change)), (max(current, change), t)]:
                if right <= left:
                    continue
                dt = right-left
                if measure_cost:
                    beta = transmission((right+left)/2, high, low, change)
                    objective += beta*(dt+(x-1)*(-math.expm1(-delta*dt))/delta)
                x = 1.0+(x-1)*math.exp(-delta*dt)
            if t != period:
                x *= math.exp(-mass)
            current = t
        return x, objective

    f0,_ = pass_once(0.0, False)
    f1,_ = pass_once(1.0, False)
    s0 = f0/(1-(f1-f0))
    end, cost = pass_once(s0, True)
    assert abs(s0-end) < 1e-12
    return cost


def threshold(delta, period, high_start, high, low):
    E = math.exp(-delta*period)
    F = (high*(-math.expm1(-delta*high_start))
         +low*(math.exp(-delta*high_start)-E))/delta
    alpha = delta*F/(1-E)
    return math.log(min(high/alpha,alpha/low)), alpha


def H(s, budget, delta, period, change, high, low):
    E=math.exp(-delta*period)
    q=math.exp(-budget)
    F=(high*(1-math.exp(-delta*change))
       +low*(math.exp(-delta*change)-E))/delta
    A=(1-q)/(1-q*E)
    if s < change:
        G=(high*(math.exp(-delta*s)-math.exp(-delta*change))
           +low*(math.exp(-delta*change)-E))/delta
    else:
        G=low*(math.exp(-delta*s)-E)/delta
    return (math.exp(delta*s)-A)*(G+q*E*F/(1-q*E))


def test():
    delta, period, change=1.,1.,.5
    high, low=1.75,.25
    cutoff, alpha=threshold(delta,period,change,high,low)
    assert abs(cutoff-0.3909799575971128)<1e-13
    assert low < alpha < high
    assert abs(H(0,.25,delta,period,change,high,low)-
               H(period,.25,delta,period,change,high,low))<1e-12
    tested=0
    for budget in [.05,.25,cutoff,cutoff+.02,.8,2.]:
        pure=annual_cost([(0.,budget)],delta,period,change,high,low)
        h0=H(0.,budget,delta,period,change,high,low)
        for s in [.0005,.1,.25,.49,.5,.65,.8,.99,.9995]:
            hs=H(s,budget,delta,period,change,high,low)
            eps=1e-6
            shifted=annual_cost([(0.,budget-eps),(s,eps)],delta,period,change,high,low)
            numeric=(shifted-pure)/eps
            assert abs(numeric-(h0-hs))<4e-6, (budget,s,numeric,h0-hs)
            if budget < cutoff-1e-5:
                assert hs < h0-1e-12, (budget,s,hs,h0)
            tested += 1
    # Exact optimizer/nonoptimizer is a consequence of the inequalities,
    # whereas this finite grid only tests illustrative schedules.
    rng = random.Random(8262026)
    schedule_checks=0
    for _ in range(150):
        d=rng.uniform(.2,3.0)
        T=rng.uniform(.6,2.)
        a=rng.uniform(.1*T,.9*T)
        L=rng.uniform(.1,1.8)
        HH=L*rng.uniform(1.1,8.)
        bc,_=threshold(d,T,a,HH,L)
        b=bc*rng.uniform(.02,.98)
        pulse_value=annual_cost([(0.,b)],d,T,a,HH,L)
        weights=[rng.random() for _ in range(3)]
        times=[rng.uniform(0,T) for _ in range(3)]
        sw=sum(weights)
        trial=annual_cost([(t,b*w/sw) for t,w in zip(times,weights)],d,T,a,HH,L)
        assert trial+2e-11>=pulse_value, (d,T,a,HH,L,b,trial,pulse_value)
        # Find an improving local direction immediately above the cutoff.
        b2=bc+.12
        pure2=annual_cost([(0.,b2)],d,T,a,HH,L)
        E=math.exp(-d*T)
        weighted=(HH*(1-math.exp(-d*a))+L*(math.exp(-d*a)-E))/(1-E)
        trialtime=min(1e-3*T, a/100) if math.exp(-b2)*HH<weighted else T-min(1e-3*T,(T-a)/100)
        assert H(trialtime,b2,d,T,a,HH,L)>H(0,b2,d,T,a,HH,L), ('local',d,T,a,HH,L,b2)
        eps=1e-6
        improved=annual_cost([(0.,b2-eps),(trialtime,eps)],d,T,a,HH,L)
        assert improved < pure2+1e-13, (d,T,a,HH,L,b2,trialtime)
        schedule_checks += 1
    print(f'VERIFY_OK: {tested} directional derivatives, {schedule_checks} random parameter families, sharp cutoff {cutoff:.12f}; all checks passed')

if __name__=='__main__':
    test()
