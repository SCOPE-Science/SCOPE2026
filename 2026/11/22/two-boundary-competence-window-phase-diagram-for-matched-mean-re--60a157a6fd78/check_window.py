"""Diagnostics for the two-residence-law finite-competence-window theorem.

Requires scipy and numpy. This finite checker supplements, but does not replace,
its analytic proof. The code compares two probability models; it contains no
field calibration.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.stats import gamma, norm

N = 0

def insist(condition, desc):
    global N
    N += 1
    if not condition:
        raise AssertionError(desc)


def data(k):
    assert k > 1
    def g(t):
        return math.exp(k*math.log(k) - math.lgamma(k) + (k-1)*math.log(t) - k*t) - math.exp(-t)
    def h(t):
        return gamma.cdf(t, a=k, scale=1/k) + math.expm1(-t)
    def df_ratio_log(t):
        return k*math.log(k)-math.lgamma(k)+(k-1)*math.log(t)-(k-1)*t
    lo = brentq(df_ratio_log, 1e-9, 1.0, xtol=1e-14)
    hi_end = max(10, k + 20)
    hi = brentq(df_ratio_log, 1.0, hi_end, xtol=1e-13)
    ell = brentq(h, lo, hi, xtol=1e-13)
    return lo, ell, hi, g, h


def roots(k, L, a, ell, b, h):
    d = lambda c: h(c+L) - h(c)
    cl = None
    if L < ell - 1e-12:
        cl = brentq(d, 0.0, a, xtol=1e-13)
    cu = brentq(d, ell+1e-12, b, xtol=1e-13)
    return cl, cu, d


def close(a, b, atol=1e-8, rtol=1e-8):
    insist(abs(a-b) <= atol+rtol*max(abs(a),abs(b)), f'not close: {a} {b}')


shapes = [1.05, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 10.0, 15.0, 30.0, 100.0]
for k in shapes:
    a,ell,b,g,h=data(k)
    insist(0<a<ell<b and a<1<b, (k,'density and CDF order'))
    insist(h(a)<0<h(b), (k,'extremal CDF signs'))
    insist(g(.5*a)<0 and g(.5*(a+b))>0 and g(1.2*b)<0, (k,'density signs'))
    close(h(ell),0,atol=5e-12)
    for j in range(1,301):
        t = .01*j*b
        want = (t<ell)
        insist((h(t)<0)==want if abs(t-ell)>1e-6 else True, (k,t,'H sign'))
    widths = [0.1*ell, 0.3*ell, 0.6*ell, 0.9*ell, ell, 1.1*ell, 1.5*ell, 3*ell, 10*ell]
    old_lower, old_upper = math.inf, math.inf
    for L in widths:
        cl,cu,d=roots(k,L,a,ell,b,h)
        insist(ell<cu<b and abs(d(cu))<5e-10, (k,L,'upper root'))
        insist(cu<old_upper, (k,L,'upper root monotonic'))
        old_upper=cu
        if L<ell:
            insist(0<cl<a, (k,L,'lower root'))
            insist(cl<old_lower, (k,L,'lower root monotonic'))
            insist(abs(d(cl))<5e-10, (k,L,'lower root exact'))
            old_lower=cl
            for x in [0.0,0.25*cl,0.75*cl]:
                insist(d(x)<0, (k,L,x,'lower sign'))
            for x in [cl+0.1*(cu-cl),.5*(cl+cu),cu-.1*(cu-cl)]:
                insist(d(x)>0,(k,L,x,'middle sign'))
        else:
            insist(cl is None, (k,L,'lower root absent'))
            for x in [0.0,0.25*cu,0.5*cu]:
                if L>ell:
                    insist(d(x)>0,(k,L,x,'left sign'))
                elif x>0:
                    insist(d(x)>0,(k,L,x,'boundary left sign'))
        for x in [cu+(b-cu)*.5,b,b+1,b+10]:
            insist(d(x)<0, (k,L,x,'upper negative sign'))
        for x in np.linspace(0, min(b+5,max(10,3*b)), 501):
            if cl is None:
                expected = (x<cu)
            else:
                expected = (cl<x<cu)
            if min(abs(x-cu),abs(x-(cl if cl is not None else 0))) > 1e-6:
                insist((d(x)>0)==expected,(k,L,x,'global sign'))
    print(f'k={k:g} alpha={a:.10f} ell={ell:.10f} beta={b:.10f}')

constant=norm.ppf(1-math.exp(-1))
for k in [100,1000,10000]:
    _,ell,_,_,h=data(k)
    insist(abs(math.sqrt(k)*(ell-1)-constant)<1.0/math.sqrt(k), (k,'asymptotic'))
    print(f'asymptotic k={k}: normalized offset {math.sqrt(k)*(ell-1):.10f}; target={constant:.10f}')
print(f'PASS: {N} diagnostic assertions')
