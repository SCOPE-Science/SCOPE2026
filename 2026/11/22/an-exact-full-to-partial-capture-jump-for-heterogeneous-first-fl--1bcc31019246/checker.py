#!/usr/bin/env python3
"""Standalone scientific diagnostics for a heterogeneous first-flush capture model.

Uses only Python's standard library.  Diagnostics do not replace the
analytic argument about arbitrary probability laws in RESULT.md.
"""
from math import exp, log, sqrt, isclose
from random import Random


def benchmark(rate, weight, gamma=1.0):
    mean = sum(k * w for k, w in zip(rate, weight))
    assert min(rate) < gamma < mean

    def H(t):
        return sum(w * exp((gamma-k)*t) for k, w in zip(rate, weight))

    def Hprime(t):
        return sum(w*(gamma-k)*exp((gamma-k)*t) for k, w in zip(rate, weight))

    def slope(t):
        return sum(w*k/gamma*exp((gamma-k)*t) for k, w in zip(rate, weight))

    lo, hi = 0.0, 1.0
    while Hprime(hi) <= 0:
        hi *= 2
        assert hi < 1024
    for _ in range(75):
        mid=(lo+hi)/2
        if Hprime(mid)<0: lo=mid
        else: hi=mid
    tstar=(lo+hi)/2
    cstar=H(tstar)
    vstar=1-exp(-gamma*tstar)
    assert 0 < cstar < 1 and 0 < vstar < 1
    assert abs(slope(tstar)-cstar)<1e-9

    def captured(v):
        if v >= 1: return 1.0
        if v <= 0: return 0.0
        t=-log(1-v)/gamma
        return 1-sum(w*exp(-k*t) for k,w in zip(rate,weight))

    def opt(c):
        if c < cstar: return 1.0
        if c == cstar: return vstar
        if c >= mean/gamma: return 0.0
        a,b=0.0,tstar
        for _ in range(75):
            m=(a+b)/2
            if slope(m)>c: a=m
            else: b=m
        return 1-exp(-gamma*(a+b)/2)

    return mean, cstar, vstar, captured, opt, H


def run():
    assertions=0
    rate=(0.5,1.5)
    weight=(0.25,0.75)
    mu, cstar, vstar, F, opt, H = benchmark(rate,weight)
    assert abs(mu-1.25)<1e-13; assertions+=1
    assert abs(cstar-sqrt(3)/2)<1e-12; assertions+=1
    assert abs(vstar-2/3)<1e-12; assertions+=1
    assert abs(H(2*log(3))-1)<1e-12; assertions+=1
    assert abs(F(vstar)- (1-cstar*(1-vstar)))<1e-12; assertions+=1
    assert abs(F(vstar)-cstar*vstar - (F(1)-cstar))<1e-12; assertions+=1
    for c in [0,0.6,0.8,0.9,1,1.1,1.24,1.25,1.8]:
        v=opt(c)
        for i in range(1201):
            u=i/1200
            assert F(v)-c*v >= F(u)-c*u-2e-11, (c,v,u)
            assertions+=1
    rng=Random(8675309)
    for _ in range(110):
        slow=rng.uniform(.12,.81)
        fast=[rng.uniform(1.65,4.7) for _j in range(rng.randint(1,3))]
        ws=rng.uniform(.025,.20)
        remaining=[rng.uniform(.05,2) for _j in fast]
        total=sum(remaining)
        weights=[ws]+[(1-ws)*x/total for x in remaining]
        rates=[slow]+fast
        m,cs,vs,FF,OPT,HH=benchmark(rates,weights)
        assertions+=6
        assert 0<cs<1<m
        assert FF(vs)-cs*vs > 0
        assert abs(FF(vs)-cs*vs-(1-cs))<1e-9
        assertions+=3
        for cc in [cs*.7, cs, (cs+m)/2, m, m*1.2]:
            vv=OPT(cc)
            for j in range(181):
                u=j/180
                assert FF(vv)-cc*vv >= FF(u)-cc*u-1e-9, (rates,weights,cc,vv,u)
                assertions+=1
    return assertions

if __name__ == '__main__':
    total=run()
    print(f'PASS: {total} deterministic assertions')
