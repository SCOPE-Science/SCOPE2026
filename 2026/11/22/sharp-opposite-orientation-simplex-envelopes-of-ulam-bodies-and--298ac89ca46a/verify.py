#!/usr/bin/env python3
"""Independent one-dimensional quadrature checks of simplex Ulam shell formulae."""
import math

def simpson(f, a, b, n=1600):
    h = (b-a)/n
    s = f(a)+f(b)
    for j in range(1,n):
        s += (4 if j % 2 else 2)*f(a+j*h)
    return s*h/3

def endpoints(d,q):
    return (1-d/(d+1)*q**(1/d),
            1-d/((d+1)*q)*(1-(1-q)**(1+1/d)))

def shells(d,q):
    return (d*(1-q)/q*(1-(1-q)**(1/d)), d*(1-q**(1/d)))

def verify():
    tested=0
    for d in (2,3,4,5,8,13,30):
        for j in range(1,20):
            q=j/20
            lo,hi=1-(1-q)**(1/d),1-q**(1/d)
            density=lambda s: d*(1-s)**(d-1)
            low_mass=simpson(density,0,lo)
            high_mass=simpson(density,hi,1)
            low_mean=simpson(lambda s:s*density(s),0,lo)/q
            high_mean=simpson(lambda s:s*density(s),hi,1)/q
            upper,lower=endpoints(d,q)
            assert abs(low_mass-q)<2e-9,(d,q,low_mass)
            assert abs(high_mass-q)<2e-9,(d,q,high_mass)
            assert abs(low_mean-lower)<2e-9,(d,q,low_mean,lower)
            assert abs(high_mean-upper)<2e-9,(d,q,high_mean,upper)
            rho,sigma=shells(d,q)
            assert abs(rho-(1-(d+1)*lower))<2e-9
            assert abs(sigma-((d+1)*upper-1))<2e-9
            H=2*q-1-q**(1+1/d)+(1-q)**(1+1/d)
            assert abs(sigma-rho -d*H/q)<2e-9
            if q<.5: assert sigma>rho
            if q==.5: assert abs(sigma-rho)<1e-11
            if q>.5: assert sigma<rho
            tested+=8
    for q in (.1,.25,.4,.6,.75,.9):
        limit_sigma=-math.log(q)
        limit_rho=-(1-q)*math.log(1-q)/q
        rho,sigma=shells(100000,q)
        assert abs(rho-limit_rho)<1e-4
        assert abs(sigma-limit_sigma)<1e-4
        tested+=2
    print(f'PASS: {tested} scalar integral, shell, transition and limit comparisons')
if __name__=='__main__': verify()
