#!/usr/bin/env python3
"""Independent numeric checks for the two-site fixed-release model.
Usage: python3 checker.py
No external packages required. Numerical checks supplement the analytic proof.
"""
import math
import random

def exp_integral(rate, t):
    if abs(rate*t)<1e-7:
        z=rate*t
        return t*(1-z/2+z*z/6-z*z*z/24+z*z*z*z/120)
    return -math.expm1(-rate*t)/rate

def j_integral(u, k, h, d):
    return exp_integral(k+d,u)-math.exp(-h*u)*exp_integral(k+d-h,u)

def probability(t,T,a,b,c,d):
    k=a+b;h=c+d;u=T-t
    return a*c/h*(exp_integral(k,t)*(-math.expm1(-h*u))+math.exp(-k*t)*j_integral(u,k,h,d))

def derivative_scaled(t,T,a,b,c,d):
    k=a+b;h=c+d;u=T-t
    return d*math.exp(h*u)*j_integral(u,k,h,d) - (h/k)*math.expm1(k*t)

def optimizer(T,a,b,c,d):
    lo,hi=0.,T
    for _ in range(95):
        mid=(lo+hi)/2
        if derivative_scaled(mid,T,a,b,c,d)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def simpson(f,lo,hi,n=800):
    if hi<=lo: return 0.
    step=(hi-lo)/n
    return step/3*(f(lo)+f(hi)+4*sum(f(lo+(2*i+1)*step) for i in range(n//2))+2*sum(f(lo+2*i*step) for i in range(1,n//2)))

def direct_integral(t,T,a,b,c,d):
    k=a+b;h=c+d
    part1=simpson(lambda s:a*math.exp(-k*s)*c/h*(-math.expm1(-h*(T-t))),0,t)
    part2=simpson(lambda s:a*math.exp(-k*s)*math.exp(-d*(s-t))*c/h*(-math.expm1(-h*(T-s))),t,T)
    return part1+part2

def run():
    rng=random.Random(441126)
    n=0
    for _ in range(1600):
        a,b,c,d=[math.exp(rng.uniform(-2,1.2)) for _ in range(4)]
        T=rng.uniform(.12,4.4)
        t=rng.random()*T
        P=probability(t,T,a,b,c,d)
        Pd=direct_integral(t,T,a,b,c,d)
        assert abs(P-Pd)<1.5e-9*(1+P),('integral',a,b,c,d,T,t,P,Pd)
        h=max(1e-6,1e-5*T)
        if h<t<T-h:
            deriv=(probability(t+h,T,a,b,c,d)-probability(t-h,T,a,b,c,d))/(2*h)
            k=a+b;hh=c+d
            analytic=a*c/hh*math.exp(-k*t-hh*(T-t))*derivative_scaled(t,T,a,b,c,d)
            assert abs(deriv-analytic)<1e-7*(1+abs(analytic)),('derivative',deriv,analytic)
        opt=optimizer(T,a,b,c,d)
        assert 0<opt<T
        assert derivative_scaled(0,T,a,b,c,d)>0
        assert derivative_scaled(T,T,a,b,c,d)<0
        v=probability(opt,T,a,b,c,d)
        for q in range(26):
            p=probability(T*q/25,T,a,b,c,d)
            assert v+2e-10>=p,('grid',T,opt,q,v,p)
        if T>=.4:
            opt2=optimizer(.999*T,a,b,c,d)
            assert opt>opt2
            assert T-opt>.999*T-opt2
        n+=1
    for a,b,c,d in [(2,1,3,1),(1,3,.5,2),(.2,.3,.1,.05)]:
        k=a+b;h=c+d
        for T in [.001,.002,.004]:
            opt=optimizer(T,a,b,c,d)
            assert abs(opt/T**2-d/2)<.03*d
        for T in [18.,35.]:
            # moderate rates only; asymptotic error exponentially small
            if max(k,h)*T>160: continue
            opt=optimizer(T,a,b,c,d)
            prediction=h/(k+h)*T - math.log(h*(k+d)/(k*d))/(k+h)
            if min(k,h)*T>12:
                assert abs(opt-prediction)<.015,(T,opt,prediction)
    print('PASS 1600 independent integral checks, 1600 grid global checks, finite differences, horizon monotonicity, short/long limits')

if __name__=='__main__': run()
