"""Deterministic numerical diagnostics for the exact one-window exposure theorem.

Requires only Python 3 standard library. Run: python check.py
Numerical diagnostics do not replace the analytic proof.
"""
from math import exp, expm1, log, isclose
from random import Random

def A(rate, length):
    return -expm1(-rate * length) / rate if rate > 0 else length

def B(rate, length):
    if not rate:
        return length * length / 2
    # Stable enough for moderate test domains; exact formula is (length-A)/rate.
    return (length - A(rate, length)) / rate

def exposure(tau, q, base, boost, T, h, initial):
    assert -1e-12 <= tau <= T - h + 1e-12
    tau = max(0., min(tau,T-h))
    dose = 0.0
    concentration = initial
    for rate, length in ((base,tau), (boost,h), (base,T-h-tau)):
        dose += concentration * A(rate,length) + q * B(rate,length)
        concentration = exp(-rate*length)*concentration + q*A(rate,length)
    return dose

def optimum(q, base, T, h, initial):
    slack = T-h
    if base == 0:
        return max(0.0, (slack-initial/q)/2)
    equilibrium = q/base
    if initial >= equilibrium * (-expm1(-base*slack)):
        return 0.0
    return slack/2 + log1p_safe(-base*initial/q)/(2*base)

def log1p_safe(x):
    from math import log1p
    return log1p(x)

def gradient(tau,q,base,boost,T,h,initial):
    G=(1-base/boost)*(-expm1(-boost*h))
    slack=T-h
    if base == 0:
        return G*(initial+q*(2*tau-slack))
    equilibrium=q/base
    return G*((initial-equilibrium)*exp(-base*tau)+equilibrium*exp(-base*(slack-tau)))

def predicted_regret(tau,q,base,boost,T,h,initial):
    G=(1-base/boost)*(-expm1(-boost*h))
    tstar=optimum(q,base,T,h,initial)
    if tstar > 1e-14:
        if base == 0:
            return G*q*(tau-tstar)**2
        from math import cosh
        return 2*G*(q/base)*exp(-base*(T-h-tstar))*(cosh(base*(tau-tstar))-1)/base
    if base == 0:
        return G*((initial-q*(T-h))*tau+q*tau*tau)
    E=q/base
    # Exact integral of derivative, with boundary optimum at zero.
    return G*((initial-E)*(1-exp(-base*tau))/base+E*exp(-base*(T-h))*(exp(base*tau)-1)/base)

def test():
    rng=Random(20261115)
    checks=0
    for k in range(1000):
        q=rng.uniform(0.3,3)
        base=rng.uniform(.1,2) if k%4 else 0.
        boost=base+rng.uniform(.15,4)
        T=rng.uniform(1,7)
        h=rng.uniform(.15*T,.75*T)
        slack=T-h
        initial=rng.uniform(0,2*q/max(base,.3)*max(1,slack))
        optimum_tau=optimum(q,base,T,h,initial)
        assert 0 <= optimum_tau <= slack; checks+=1
        candidates=[0,slack]+[slack*i/60 for i in range(61)]
        best=exposure(optimum_tau,q,base,boost,T,h,initial)
        for tau in candidates:
            actual=exposure(tau,q,base,boost,T,h,initial)
            assert actual + 2e-11 >= best; checks+=1
        mid=slack*.43
        step=2e-5*min(1,slack)
        num=(exposure(mid+step,q,base,boost,T,h,initial)-exposure(mid-step,q,base,boost,T,h,initial))/(2*step)
        assert isclose(num,gradient(mid,q,base,boost,T,h,initial),rel_tol=2e-6,abs_tol=2e-7), (num,gradient(mid,q,base,boost,T,h,initial)); checks+=1
        for fraction in (.1,.4,.8):
            tau=slack*fraction
            regret=exposure(tau,q,base,boost,T,h,initial)-best
            claimed=predicted_regret(tau,q,base,boost,T,h,initial)
            assert isclose(regret,claimed,rel_tol=1e-5,abs_tol=2e-9), (regret,claimed,k);checks+=1
        # The optimum is completely independent of boost strength.
        for multiplier in (1.1,2,10):
            alternative=base+(boost-base)*multiplier
            assert exposure(optimum_tau,q,base,alternative,T,h,initial)<=exposure(slack*.1,q,base,alternative,T,h,initial)+1e-10;checks+=1
    # Canonical example
    x=(1,1,3,4,1,0)
    assert isclose(optimum(1,1,4,1,0),1.5);checks+=1
    early=exposure(0,*x)
    optimal=exposure(1.5,*x)
    assert isclose(early,2.578509392222384,rel_tol=1e-11);checks+=1
    assert isclose(optimal,2.1961901118204112,rel_tol=1e-11);checks+=1
    print(f'PASS: {checks} deterministic assertions; start dose {early:.12f}; optimal dose {optimal:.12f}; improvement {(early-optimal)/early:.6%}')

if __name__=='__main__':test()
