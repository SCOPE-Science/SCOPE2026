#!/usr/bin/env python3
"""Standalone supplementary checks of known-pool attenuation source-distance theorem.
Run: python3 verify.py (standard library only). All checks finite and supplementary to proof.
"""
from math import exp, log, sqrt, isclose
from fractions import Fraction
from random import Random


def g(u, rates, weights):
    return sum(w * exp(-a*u) for a, w in zip(rates, weights))


def hazard(u, rates, weights):
    z = [w*exp(-a*u) for a, w in zip(rates, weights)]
    return sum(a*v for a, v in zip(rates, z))/sum(z)


def info(u,h,Q,rates,weights):
    # Stable positive pair expansion avoids subtracting almost equal hazards.
    z=[w*exp(-a*u) for a,w in zip(rates,weights)]
    g0=sum(z)
    zh=[v*exp(-a*h) for a,v in zip(rates,z)]
    g1=sum(zh)
    num=sum((rates[j]-rates[i])*z[i]*z[j]*
            (exp(-rates[i]*h)-exp(-rates[j]*h))
            for i in range(len(rates)) for j in range(i+1,len(rates)))
    return Q*num*num/(g0*g1*(g0+g1))


def info_schur(u,h,Q,rates,weights):
    g0,g1 = g(u,rates,weights),g(u+h,rates,weights)
    k0,k1 = hazard(u,rates,weights),hazard(u+h,rates,weights)
    # Schur complement of nuisance Q in Poisson information matrix
    iQQ=(g0+g1)/Q
    iQx=-(g0*k0+g1*k1)
    ixx=Q*(g0*k0*k0+g1*k1*k1)
    return ixx-iQx*iQx/iQQ


def critical(a,delta):
    def eq(h):
        # derivative of logarithm of limiting objective
        return 2*delta/(exp(delta*h)-1)-a/(1+exp(-a*h))
    lo,hi=1e-8,1.
    while eq(hi)>0: hi*=2
    for _ in range(100):
        md=(lo+hi)/2
        if eq(md)>0:lo=md
        else:hi=md
    return (lo+hi)/2


def main():
    # A two-mode, exact-rational example at x=h=log(2), Q=16.
    g0=Fraction(1,2)+Fraction(1,4)
    g1=Fraction(1,4)+Fraction(1,16)
    ratio=g1/g0
    assert (g0,g1,ratio)==(Fraction(3,4),Fraction(5,16),Fraction(5,12))
    # Recover exp(-x) from the two-point ratio at the specified rates and gap.
    t=(Fraction(1,2)-ratio)/(ratio-Fraction(1,4))
    assert t==Fraction(1,2) and 16*g0==12 and 16*g1==5
    assert (Fraction(16)*g0*g1/(g0+g1)*Fraction(2,15)**2)==Fraction(16,255)

    rng=Random(22617)
    n=0
    for _ in range(2500):
        m=rng.randint(2,6)
        rates=sorted(rng.uniform(.25,3) for __ in range(m))
        weights=[rng.uniform(.1,4) for __ in range(m)]
        x=rng.uniform(0,5)
        h=rng.uniform(.01,3)
        Q=rng.uniform(.2,20)
        r0=g(x+h,rates,weights)/g(x,rates,weights)
        r1=g(x+h+.00001,rates,weights)/g(x+.00001,rates,weights)
        assert r1>r0
        im=info(x,h,Q,rates,weights)
        assert im>0
        assert isclose(im,info_schur(x,h,Q,rates,weights),rel_tol=5e-8,abs_tol=1e-12)
        n+=1
    assert critical(1,1)>0
    hstar=critical(1,1)
    exact=log((3+sqrt(17))/2)
    assert abs(hstar-exact)<1e-12
    # Exact two-mode normalized information (a=delta=A1=A2=Q=1).
    # Compare its global maximizers across increasingly distant source sites.
    for x in (6.,10.,15.,20.):
        hs=[.001*i for i in range(1,3501)]
        best=max(hs,key=lambda h:info(x,h,1.,[1.,2.],[1.,1.]))
        assert abs(best-hstar)<.10
        f=(1-exp(-hstar))**2/(1+exp(hstar))
        rel=info(x,hstar,1.,[1.,2.],[1.,1.])*exp(3*x)/f
        assert 0.90<rel<1.01
    # Extra, faster exponential modes asymptotically do not affect the limit.
    rates=[1.,2.,3.5,5.]
    weights=[2.,3.,.7,4.]
    x=24.
    a,delta=1.,1.
    f=lambda h:(1-exp(-delta*h))**2/(1+exp(a*h))
    C=weights[1]**2/weights[0]*delta**2
    for h in (.25,.75,1.27,2.,3.):
        normalized=info(x,h,1.,rates,weights)*exp((a+2*delta)*x)/C
        assert isclose(normalized,f(h),rel_tol=2e-8)
    # In the monomodal case, an unknown amplitude leaves x nonidentifiable.
    rates=[1.5]
    for x in (0.,.5,2.,10.):
        assert isclose(g(x+1,rates,[1.])/g(x,rates,[1.]),exp(-1.5))
    print('PASS: exact inversion, Poisson efficient information, 2500 mixture challenges, long-distance asymptotics, universal gap, boundaries')
    print('example critical gap',format(hstar,'.14f'))
    print('example information',Fraction(16,255))

if __name__=='__main__':main()
