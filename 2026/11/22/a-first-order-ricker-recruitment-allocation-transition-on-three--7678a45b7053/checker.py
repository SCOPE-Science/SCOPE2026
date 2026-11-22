"""Deterministic numerical diagnostics for fixed-sum identical Ricker recruitment.

The theorem is established analytically; these tests exercise numeric evaluations
and challenge the claimed global selection against random feasible allocations.
No experimental sampling is presented as a proof of global optimality.
"""
from math import exp, expm1, isfinite
import random


def response(x):
    return x * exp(-x)


def u(d):
    if abs(d) < 1.0e-5:
        return 1 - d/2 + d*d/12 - d**4/720 + d**6/30240
    return d/expm1(d)


def sprime(m,d):
    if d < 1.0e-4:
        return 1 + m*(-0.5+d/6 - d**3/180+d**5/5040)
    E = expm1(d)
    return 1 + m*(E-d*exp(d))/(E*E)


def total(m,d):
    return m+d+m*u(d)


def densities(m,d):
    return 1+u(d), 1+u(d)+d


def advantage(m,d):
    a,b = densities(m,d)
    return (m-1)*response(a)+response(b)-m*response(total(m,d)/m)


def bisect(fun,low,high,n=85):
    fl,fh = fun(low),fun(high)
    assert fl*fh < 0, (low,high,fl,fh)
    for _ in range(n):
        mid=(low+high)/2
        if fun(mid)*fl > 0:
            low=mid
            fl=fun(mid)
        else:
            high=mid
    return (low+high)/2


def thresholds(m):
    if m==2:
        return 4.0,None,None,None
    ds=bisect(lambda d:sprime(m,d),.001,m+4)
    d2=bisect(lambda d:total(m,d)-2*m,ds+1e-5,m+4)
    dc=bisect(lambda d:advantage(m,d),ds+1e-4,d2-1e-5)
    return total(m,dc),ds,dc,d2


def optimum(m,S):
    sc,ds,dc,d2=thresholds(m)
    if S < sc-1e-10 or abs(S-sc)<=1e-10:
        return tuple([S/m]*m),m*response(S/m)
    if m==2:
        d=bisect(lambda t:total(m,t)-S,1e-8,max(S,6.0))
    else:
        d=bisect(lambda t:total(m,t)-S,ds+1e-9,max(S,m+5))
    a,b=densities(m,d)
    return tuple([a]*(m-1)+[b]),(m-1)*response(a)+response(b)


def run():
    rng=random.Random(20261119)
    checks=0
    for m in range(2,11):
        sc,ds,dc,d2=thresholds(m)
        if m==2:
            assert sc==4.0; checks+=1
        else:
            assert m < sc < 2*m and total(m,ds) < sc
            assert 0 < ds < dc < d2
            assert advantage(m,ds)<0 and abs(advantage(m,dc))<1e-12
            checks+=3
        for S in [0.2*m, 0.75*m, 1.2*m, sc*0.997, sc-0.0001, sc, sc+0.0001, sc*1.003, 2*m, 3*m, 6*m]:
            opt,F=optimum(m,S)
            assert isfinite(F) and abs(sum(opt)-S) < 1e-9*max(S,1)
            assert abs(sum(response(x) for x in opt)-F)<1e-10
            assert F + 1e-8 >= m*response(S/m)
            checks+=3
            if max(opt)-min(opt)>1e-7:
                a,b=min(opt),max(opt)
                assert 1-1e-12<=a<2<b and abs((1-a)*exp(-a)-(1-b)*exp(-b))<2e-10,(m,S,sc,a,b,opt)
                checks+=1
            for _ in range(350):
                yy=[rng.expovariate(1) for j in range(m)]
                scale=S/sum(yy)
                test=sum(response(v*scale) for v in yy)
                assert test<=F+2e-8,(m,S,F,test)
                checks+=1
        if m>=3:
            # At equality of the two globally best regimes, both give the same reward.
            a,b=densities(m,dc)
            assert abs((m-1)*response(a)+response(b)-m*response(sc/m))<1e-11
            checks+=1
    # Numeric example for three identical spawning patches.
    sc,ds,dc,d2=thresholds(3)
    assert abs(sc-5.774313471725135)<1e-10
    assert abs(ds-1.0356584794018933)<1e-10
    assert abs(dc-1.3974995195939495)<1e-10
    assert abs(d2-2.1491257999069706)<1e-10
    checks+=4
    print('All',checks,'supplementary assertions passed.')
    print('Three-patch transition S_c=%.12f, density jump=%.12f' %(sc,dc))
    return checks


if __name__=='__main__':
    run()
