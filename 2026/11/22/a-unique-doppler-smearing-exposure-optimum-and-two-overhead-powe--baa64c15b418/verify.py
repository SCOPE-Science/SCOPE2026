#!/usr/bin/env python3
"""Reproducibility checks for an ideal Gaussian Doppler-smearing cadence law.
Requires Python 3 standard library only. The proof is analytic; tests are auxiliary.
"""
from math import erf, exp, pi, sqrt, isclose


def gaussian_F(t, c=1.0):
    return sqrt(pi)*erf(c*t)/c - (-__import__('math').expm1(-c*c*t*t))/(c*c*t)

def gaussian_Fprime(t, c=1.0):
    return (-__import__('math').expm1(-c*c*t*t))/(c*c*t*t)

def optimal_t(h, c=1.0):
    assert h > 0 and c > 0
    def condition(t):
        return (t+h)*gaussian_Fprime(t,c)-gaussian_F(t,c)
    lo, hi = 1e-12/c, max(h,1/c)
    while condition(hi)>0:
        hi *= 2
    for _ in range(120):
        mid=(lo+hi)/2
        if condition(mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

def simpson(f,a,b,n=1000):
    assert n%2==0
    step=(b-a)/n
    return step/3*(f(a)+f(b)+4*sum(f(a+j*step) for j in range(1,n,2))+2*sum(f(a+j*step) for j in range(2,n,2)))

def main():
    checks=0
    # Independent numerical reconstruction of the autocorrelation integral.
    for c in (0.3,1.0,2.3):
        for t in (0.15,0.7,1.0,2.0,4.0):
            integral=(2/t)*simpson(lambda u:(t-u)*exp(-(c*u)**2),0,t)
            assert isclose(integral,gaussian_F(t,c),rel_tol=3e-10,abs_tol=3e-10)
            checks+=1
            derivative=(2/t**2)*simpson(lambda u:u*exp(-(c*u)**2),0,t)
            assert isclose(derivative,gaussian_Fprime(t,c),rel_tol=3e-10,abs_tol=3e-10)
            checks+=1
    # Sign change and strict global optimality over a geometric grid.
    for c in (0.3,1.0,2.3):
        for h in (0.05,0.3,1.0,7.0,25.0):
            t=optimal_t(h,c)
            sn=lambda x:gaussian_F(x,c)/(x+h)
            for factor in (0.1,0.25,0.5,0.75,0.9,1.1,1.3,2.0,4.0,10.0):
                assert sn(t)>sn(factor*t)
                checks+=1
    # Comparative statics in overhead and analytic limiting laws.
    for c in (0.5,1,2.0):
        ts=[optimal_t(h,c) for h in (0.01,0.1,1,10,100)]
        assert all(ts[i]<ts[i+1] for i in range(4));checks+=4
        for h in (1e-7,1e-6,1e-5):
            ratio=optimal_t(h,c)/(3*h/c**2)**(1/3)
            assert abs(ratio-1)<0.04
            checks+=1
        for h in (1e6,1e7):
            ratio=optimal_t(h,c)/sqrt(h/(c*sqrt(pi)))
            assert abs(ratio-1)<0.03
            checks+=1
    # Check finite exponential autocorrelation as a second shape.
    for b in (0.2,1.0,3.0):
        # K(u)=exp(-bu): F=2/b-2(1-exp(-bt))/(b**2*t)
        def F(t):return 2/b - 2*(-__import__('math').expm1(-b*t))/(b*b*t)
        def Fp(t):return 2*((1-__import__('math').exp(-b*t))/(b*b*t*t)-__import__('math').exp(-b*t)/(b*t))
        for t in (0.2,1,5):
            assert isclose(F(t),2/t*simpson(lambda u:(t-u)*exp(-b*u),0,t),rel_tol=3e-9)
            assert isclose(Fp(t),2/t**2*simpson(lambda u:u*exp(-b*u),0,t),rel_tol=3e-9)
            checks+=2
    print('PASS',checks,'auxiliary checks')
    for h in (0.01,0.1,1,10,100):
        print('Gaussian c=1, h=',h,'T*=',f'{optimal_t(h):.12f}')

if __name__=='__main__': main()
