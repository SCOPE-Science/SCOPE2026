#!/usr/bin/env python3
"""Numerical checks for a Gaussian oxygen deficit with exponential depth compensation.

Standard-library-only supplementary checks. The global parameter theorem and its
fold asymptotics are proved analytically in RESULT.md; sampling is not a proof.
"""
import math
import random


def fold_location(a):
    return (math.sqrt(a*a+4.0)-a)/2.0


def critical_deficit(a):
    u = fold_location(a)
    return a*u*math.exp(u*u/2.0)


def fragmentation_deficit(a, b):
    u = fold_location(a)
    if b >= u:
        return critical_deficit(a)
    return a*math.exp(b*b/2.0)/(a+b)


def score(x, a, b, r):
    return math.exp(a*(x+b))*(1-r*math.exp(-x*x/2))


def derivative_sign_factor(x, a, r):
    return a-r*(a-x)*math.exp(-x*x/2)


def bisect_zero(fun, lo, hi):
    flo, fhi = fun(lo), fun(hi)
    assert flo * fhi < 0, (lo,hi,flo,fhi)
    for _ in range(90):
        mid=(lo+hi)/2.0
        if fun(mid)*flo>0:
            lo,flo=mid,fun(mid)
        else:
            hi,fhi=mid,fun(mid)
    return (lo+hi)/2.0


def extrema(a,r):
    u=fold_location(a)
    assert critical_deficit(a)<r<1
    f=lambda x: derivative_sign_factor(x,a,r)
    left=-max(100.0, 30.0/a)
    return bisect_zero(f,left,-u),bisect_zero(f,-u,0.0)


def check():
    checks=0
    rng=random.Random(13742024)
    # Nonlinear phase boundary and strict endpoint conditions; independent witnesses.
    for _ in range(2500):
        a=math.exp(rng.uniform(math.log(.08), math.log(5)))
        b=math.exp(rng.uniform(math.log(.02), math.log(5)))
        rc=critical_deficit(a)
        rt=fragmentation_deficit(a,b)
        u=fold_location(a)
        assert 0 < rc <= rt < 1
        assert abs(critical_deficit(a) - (1-u*u)*math.exp(u*u/2)) < 1e-12
        checks+=2
        # Deliberately sample on both sides of the exact boundary.
        for r in [rt*.8,(rt+1)*.5]:
            assert 0<r<1
            x0=-b
            predicted=r>rt
            if r<=rc:
                # No stationary points anywhere on the real line.
                assert derivative_sign_factor(-u,a,r)>=-1e-13
                assert not predicted
                checks+=2
                continue
            xleft,xright=extrema(a,r)
            assert xleft<-u<xright<0
            observed=xright>x0
            assert predicted==observed
            checks+=2
            if observed:
                m=score(xright,a,b,r)
                M=score(x0,a,b,r)
                if xleft>x0:
                    M=max(M,score(xleft,a,b,r))
                assert M>m
                theta=(M+m)/2
                # A shallow positive-length viable band and a separate deep band.
                shallow_peak_x=xleft if xleft>x0 and score(xleft,a,b,r)>=score(x0,a,b,r) else x0
                assert score(shallow_peak_x,a,b,r)>theta
                assert score(xright,a,b,r)<theta
                assert score(max(xright+30,30/a),a,b,r)>theta
                checks+=4
            else:
                # On the physical half-line the score is strictly increasing.
                for j in range(201):
                    xx=x0+j*max(8,8/a)/200
                    assert derivative_sign_factor(xx,a,r)>=-1e-12
                checks+=1
    # Verify the fold's square-root and 3/2 laws independently at several slopes.
    for a in [.12,.3,.5,.9,1.5,3.0]:
        u=fold_location(a)
        b=u+1.5
        rc=critical_deficit(a)
        A=math.sqrt(2/(1+u*u))
        for eps in [.001,.0002]:
            r=rc*(1+eps)
            assert r<1
            xleft,xright=extrema(a,r)
            gap=score(xleft,a,b,r)-score(xright,a,b,r)
            predicted=(4*a/3)*math.exp(a*(b-u))*A*eps**1.5
            assert abs(gap/predicted-1)<.02
            assert abs((xright-xleft)/(2*A*math.sqrt(eps))-1)<.02
            checks+=2
    # Exact numerical example and physically positive habitat gap.
    a,b,r=.5,2.0,.8
    xleft,xright=extrema(a,r)
    assert abs((xleft+b)-.462715876570411)<1e-10
    assert abs((xright+b)-1.86966923605016)<1e-10
    th=.7
    lower=bisect_zero(lambda x:score(x,a,b,r)-th,xleft,xright)
    upper=bisect_zero(lambda x:score(x,a,b,r)-th,xright,5)
    assert abs(lower+b-1.33340648487838)<1e-10
    assert abs(upper+b-2.25851796290664)<1e-10
    checks+=4
    # Sensitivity: deeper oxygen minimum cannot increase the threshold.
    for a in [.1,.3,.5,1,2,5]:
        bs=[.005+.01*j for j in range(401)]
        thresholds=[fragmentation_deficit(a,b) for b in bs]
        assert all(x>=y-1e-13 for x,y in zip(thresholds,thresholds[1:]))
        checks+=1
    return checks

if __name__=='__main__':
    print('SUPPLEMENTARY_ASSERTION_GROUPS_PASSED',check())
