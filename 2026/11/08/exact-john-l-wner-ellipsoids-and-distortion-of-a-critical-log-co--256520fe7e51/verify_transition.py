"""Numerical supplementary checks of exact formulas for separable log-cosh bodies.
Analytic proof, not this finite testing, establishes all-dimensional statements.
"""
import math, random

def a(s):
    if s <= 0: return 0.0
    return math.acosh(math.exp(s))

def f(x):
    t=abs(x)
    return t+math.log1p(math.exp(-2*t))-math.log(2.0)

def radial(u,beta):
    hi=2.0*max(1.,beta+5)
    while sum(f(hi*t) for t in u) < beta: hi*=2
    lo=0.0
    for _ in range(72):
        m=(lo+hi)/2
        if sum(f(m*t) for t in u) < beta: lo=m
        else: hi=m
    return (lo+hi)/2

def main():
    rng=random.Random(20261008)
    checks=0
    for d in [2,3,4,6,9,16]:
        for beta in [0.05,0.2,1.,2.,8.]:
            r=(d**0.5)*a(beta/d)
            R=a(beta)
            assert abs(sum(f(a(beta/d)) for _ in range(d))-beta) < 2e-12
            assert abs(f(R)-beta) < 2e-12
            checks+=2
            for i in range(d):
                e=[0.]*d; e[i]=1.
                assert abs(radial(e,beta)-R) < 2e-10
                checks+=1
            u=[1/math.sqrt(d)]*d
            assert abs(radial(u,beta)-r)<2e-10
            checks+=1
            for j in range(240):
                u=[rng.gauss(0,1) for _ in range(d)]
                n=math.sqrt(sum(x*x for x in u)); u=[x/n for x in u]
                rho=radial(u,beta)
                assert r-1e-9 <= rho <= R+1e-9,(d,beta,rho,r,R)
                checks+=1
    # Independent finite sampling of predicted strict parameter trends.
    for d in [2,3,5,10,100]:
        last=1.
        for beta in [1.e-5,.001,.01,.05,.2,1.,4.,10.,30.]:
            D=a(beta)/(math.sqrt(d)*a(beta/d))
            assert last < D <= math.sqrt(d)+1e-10,(d,beta,last,D)
            last=D; checks+=1
    for beta in [.05,.2,1,3,10]:
        last=1.
        for d in [2,3,4,6,10,30,100,500]:
            D=a(beta)/(math.sqrt(d)*a(beta/d))
            assert last < D < a(beta)/math.sqrt(2*beta),(beta,d,last,D)
            last=D; checks+=1
    print('LOGCOSH_TRANSITION_NUMERICAL_OK',checks)

if __name__=='__main__': main()
