#!/usr/bin/env python3
"""Numerical cross-checks for the cusp and jump of logistic-induced proximal maps.

The analytic proof in RESULT.md establishes the infinite-parameter statements.
This script uses only the Python standard library; numeric tests are supplementary.
"""
import math


def bisect(fn, lo, hi, iterations=85):
    flo, fhi = fn(lo), fn(hi)
    assert flo * fhi <= 0, (lo, hi, flo, fhi)
    for _ in range(iterations):
        mid = (lo + hi) / 2
        fm = fn(mid)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def gate(a, t):
    z = a * (t - 1)
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    e = math.exp(z)
    return e / (1.0 + e)


def h(a, t):
    return t * gate(a, t)


def hp(a, t):
    q = gate(a, t)
    return q + a*t*q*(1-q)


def maximum(a):
    t0 = bisect(lambda t: a*t*math.tanh(a*(t-1)/2)-2, 1, max(4, 3+4/a))
    q = gate(a, t0)
    L = hp(a, t0)
    # h''' at the unique maximum of h'
    h3 = a*q*(1-q)*(a*(1-2*q)-2*a*a*t0*q*(1-q))
    assert t0 > 1 and L > 1 and h3 < 0
    return t0, L, h3


def simpson(fn, low, high, n=4096):
    assert n % 2 == 0
    dh=(high-low)/n
    z=fn(low)+fn(high)
    for j in range(1, n):
        z += (4 if j % 2 else 2)*fn(low+j*dh)
    return z*dh/3


def check(a=4, lam=1):
    t0, L, h3 = maximum(a)
    rho = 1 - 1/L
    bc = 1/rho
    D = -h3/(lam*lam*L**4)
    assert rho > 0 and D > 0
    ua = lam*h(a,t0)
    def T(t,b):
        return lam*(b*t+(1-b)*h(a,t))
    for eps in (0.001, 0.005, 0.02):
        b=bc*(1+eps)
        cutoff=b/(b-1)
        ta=bisect(lambda t:hp(a,t)-cutoff,0,t0)
        tb=bisect(lambda t:hp(a,t)-cutoff,t0,20)
        slo,shi=T(tb,b),T(ta,b)
        assert 0<slo<shi
        def minimizers(s):
            l=bisect(lambda t:T(t,b)-s,0,ta)
            r=bisect(lambda t:T(t,b)-s,tb,max(10, s/lam+10))
            return l,r
        def area(s):
            l,r=minimizers(s)
            return simpson(lambda t:(T(t,b)-s)*lam*hp(a,t), l,r)
        assert area(slo)>0 and area(shi)<0
        sm=bisect(area,slo,shi,70)
        tl,tr=minimizers(sm)
        ul,ur=lam*h(a,tl),lam*h(a,tr)
        jump=ur-ul
        predicted_jump=2*math.sqrt(6/(bc*D))*math.sqrt(eps)
        predicted_width=(4/3)*math.sqrt(2/(bc*D))*eps**1.5
        assert abs(area(sm)) < 3e-10
        assert 0<ul<ua<ur
        assert abs(jump/predicted_jump-1) < 0.11
        assert abs((shi-slo)/predicted_width-1)<0.08
        print('delta=',eps,'fold_width=',round(shi-slo,12),
              'Maxwell_input=',round(sm,12),'jump=',round(jump,12),
              'jump/scaling=',round(jump/predicted_jump,8),
              'fold/scaling=',round((shi-slo)/predicted_width,8))
    sc=T(t0,bc)
    coeff=(6/(bc*D))**(1/3)
    for sign in (-1,1):
        ds=sign*1e-6
        if sign<0:
            root=bisect(lambda t:T(t,bc)-(sc+ds),0,t0)
        else:
            root=bisect(lambda t:T(t,bc)-(sc+ds),t0,10)
        du=lam*h(a,root)-ua
        assert du*sign>0
        ratio=abs(du)/(coeff*(abs(ds)**(1/3)))
        assert abs(ratio-1)<0.02
        print('critical_input_shift=',ds,'cubic_ratio=',round(ratio,8))
    print('OK', 'L=',round(L,12),'beta_critical=',round(bc,12),
          'critical_u=',round(ua,12),'D=',round(D,12))

if __name__=='__main__':
    check()
