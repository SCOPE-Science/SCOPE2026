#!/usr/bin/env python3
"""Independent finite diagnostics for a spectral-memory time-average theorem.

Standard library only; repeatability seed fixed.  The exact claims and all-t
limits require the written proof, not these finite checks.
"""
from decimal import Decimal, localcontext
from math import exp, sqrt, gamma
from random import Random


def exact_variance(lam, rate, stationary_variance, time):
    """Independent hypergeometric power-series evaluation of the exact formula."""
    with localcontext() as ctx:
        ctx.prec = 70
        la, rr, vv, tt = map(lambda x: Decimal(str(x)),
                              (lam, rate, stationary_variance, time))
        aa = la + rr
        pp = 2 * rr / aa
        z = -aa * tt
        term = Decimal(1)
        accum = term
        for n in range(1, 400):
            term *= z * (Decimal(n+1)-pp) / (Decimal(n+1)*Decimal(n+2))
            accum += term
            if abs(term) < Decimal('1e-57'):
                break
        else:
            raise AssertionError('series failed to converge')
        return float(vv * accum)


def integrate_moment_ode(lam, rate, v, T, steps=25000):
    """Integrate directly the martingale-moment ODE (not the series)."""
    eps = 1e-5
    h = (T-eps)/steps
    s, c, t = v*eps*eps, v*eps, eps

    def rhs(tt, ss, cc):
        return 2*cc, v-(lam+rate)*cc + rate*ss/tt

    for _ in range(steps):
        a1,b1=rhs(t,s,c)
        a2,b2=rhs(t+h/2,s+h*a1/2,c+h*b1/2)
        a3,b3=rhs(t+h/2,s+h*a2/2,c+h*b2/2)
        a4,b4=rhs(t+h,s+h*a3,c+h*b3)
        s += h*(a1+2*a2+2*a3+a4)/6
        c += h*(b1+2*b2+2*b3+b4)/6
        t += h
    return s/T**2


def simulate_ou(lam, rate, diffusion, T=6.0, step=0.02,
                paths=3500, seed=74125):
    """Independent discretization of path-history relocations; finite grid only."""
    rng=Random(seed)
    n=round(T/step)
    v=diffusion/lam
    q=exp(-lam*step)
    noise=sqrt(v*(1-q*q))
    p_reset=1-exp(-rate*step)
    sq=0.0
    for _ in range(paths):
        x=rng.gauss(0,sqrt(v))
        hist=[x]
        integral=0.0
        for _ in range(n):
            drifted=q*x+noise*rng.gauss(0,1)
            integral += step*(x+drifted)/2
            if rng.random()<p_reset:
                x=hist[rng.randrange(len(hist))]
            else:
                x=drifted
            hist.append(x)
        sq+=(integral/T)**2
    return sq/paths


def main():
    checks=0
    for lam,rate,v,T in [
        (1.0,0,2.0,2.5),(1.0,0.25,1.0,6),
        (1.0,1.0,1.0,6),(1.0,2.0,1.0,6),
        (0.7,1.1,0.9,4), (1.8,0.4,1.3,3)]:
        exact=exact_variance(lam,rate,v,T)
        ode=integrate_moment_ode(lam,rate,v,T)
        assert abs(exact-ode)<1e-7,(lam,rate,exact,ode)
        assert 0 < exact < v+1e-10
        checks+=2
        print('ODE/series',lam,rate,T,'variance',round(exact,9),'error',round(exact-ode,11))
    # Markovian calibration at zero reset rate.
    lam, v, T=1.3,1.7,5.0
    expected=2*v*(T/lam-(1-exp(-lam*T))/lam**2)/T**2
    assert abs(expected-exact_variance(lam,0,v,T))<1e-12
    checks+=1
    for rate in (0.25,1.0,2.0):
        theo=exact_variance(1,rate,1,6)
        emp=simulate_ou(1,rate,1)
        rel=abs(theo-emp)/theo
        assert rel<0.14,(rate,theo,emp,rel)
        checks+=1
        print('Path-history simulation: r=',rate,'theoretical=',round(theo,6),
              'empirical=',round(emp,6),'relative=',round(rel,4))
    print('PASS: %d comparison assertions (ODE, series, Markov and histories)'%checks)

if __name__=='__main__':
    main()
