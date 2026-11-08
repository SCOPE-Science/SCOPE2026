#!/usr/bin/env python3
"""Independent finite-distance checks for stationary Pareto-reset spin correlations.

Requires scipy>=1.10. The asymptotic statements are proved analytically in RESULT.md;
finite integrals and exact transforms below do not certify an infinite limit.
"""
import math
from scipy.integrate import quad
from scipy.special import ive, gamma as gammafn

COUNT = 0

def close(actual, expected, rtol=1e-7, atol=1e-12):
    global COUNT
    assert math.isfinite(actual), actual
    assert abs(actual-expected) <= atol+rtol*abs(expected), (actual, expected)
    COUNT+=1

def survival_age(t, alpha, tau0):
    q=alpha-1
    mean=alpha*tau0/q
    return (1-t/mean) if t<tau0 else ((tau0/t)**q)/alpha

def kappa(s, gamma):
    return math.acosh(1+s/(2*gamma))

def eta(gamma):
    return (1-math.sqrt(1-gamma*gamma))/gamma

def exact_corr(n, alpha, tau0, gamma):
    # First-hitting density: n exp(-2 gamma t) I_n(2 gamma t)/t,
    # with independent bulk killing exp(-2(1-gamma)t).
    # scipy.special.ive absorbs the rapidly increasing Bessel exponential.
    scale=n*n if gamma==1.0 else n
    def integrand(u):
        if u<=0:return 0.0
        t=scale*u
        return scale*(n/t)*math.exp(-2*(1-gamma)*t)*ive(n,2*gamma*t)*survival_age(t,alpha,tau0)
    result,err=quad(integrand,0.0,math.inf,limit=350,epsabs=2e-13,epsrel=3e-9)
    assert err<max(5e-8,1e-5*abs(result)),(n,alpha,gamma,err)
    return result

def k_zero(alpha, tau0):
    q=alpha-1
    return tau0**q*4**q*gammafn(q+0.5)/(alpha*math.sqrt(math.pi))

def k_positive(alpha, tau0, gamma):
    q=alpha-1
    return tau0**q*(2*math.sqrt(1-gamma**2))**q/alpha

# Equilibrium-renewal age law and continuity at its Pareto cutoff.
for alpha in (1.1,1.25,1.5,2.0,3.5):
    for tau0 in (0.25,0.4,1.3):
        close(survival_age(0.0,alpha,tau0),1.0)
        close(survival_age(tau0,alpha,tau0),1/alpha)
        close(survival_age(tau0*(1-1e-7),alpha,tau0),
              survival_age(tau0*(1+1e-7),alpha,tau0),rtol=1e-6)
        for t in (tau0/2,tau0,2*tau0,10*tau0):
            assert 0<=survival_age(t,alpha,tau0)<=1
            COUNT+=1

# Transform e^{-n kappa(s)} equals the independent-step first-passage transform.
for g in (.3,.65,.9,1.0):
    for n in (1,2,3,5,10):
        for s in (.02,.5,1.2):
            u=math.exp(-kappa(s,g))
            close((s+2*g)*u, g*(1+u*u),rtol=1e-12)
            close(u**n, math.exp(-n*kappa(s,g)),rtol=1e-12)

# A closed inverse-moment identity at zero temperature: E[T_n^{-1}]=2/(n^2-1).
for n in (2,3,4,7,10,20):
    val,_=quad(lambda s: math.exp(-n*kappa(s,1.0)),0,math.inf,epsabs=2e-13)
    close(val,2/(n*n-1),rtol=2e-10)

# Finite-positive-temperature Laplace transform E[e^{-delta T_n}]=eta^n.
for g in (.4,.7,.9):
    delta=2*(1-g)
    for n in (1,2,5,10):
        close(math.exp(-n*kappa(delta,g)),eta(g)**n,rtol=1e-12)
        close(1/math.sqrt(delta*(delta+4*g)),1/(2*math.sqrt(1-g*g)),rtol=1e-12)

# The asymptotic prefactors are approximated by the exact Bessel hitting-time integrals.
# Normalization ratios approach one. These comparisons only corroborate convergence.
for a in (1.25,1.5,2.0):
    for n in (10,25,45):
        v=exact_corr(n,a,.4,1.0)
        predicted=k_zero(a,.4)*n**(-2*(a-1))
        assert abs(v/predicted-1)<.015,(n,a,v/predicted)
        COUNT+=1
for a in (1.25,1.5,2.0):
    for n in (10,20,30):
        v=exact_corr(n,a,.4,.9)
        predicted=k_positive(a,.4,.9)*n**(-(a-1))*eta(.9)**n
        assert abs(v/predicted-1)<.27,(n,a,v/predicted)
        COUNT+=1

# Stationary zero-field correlation signs, decay, and finite block variance identity.
for a in (1.25,1.5,2.0):
    vals=[exact_corr(n,a,.4,1.0) for n in range(1,18)]
    for i in range(len(vals)-1):
        assert 0<vals[i+1]<vals[i]<1
        COUNT+=1
    L=18
    blockvar=(L+2*sum((L-n)*v for n,v in enumerate(vals,start=1)))/L**2
    assert 0<blockvar<1
    COUNT+=1

print(f"PASS: {COUNT} finite algebraic, integral, and monotonicity assertions")
