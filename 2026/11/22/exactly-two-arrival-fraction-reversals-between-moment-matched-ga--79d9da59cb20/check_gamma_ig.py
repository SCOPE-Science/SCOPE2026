"""Numerical diagnostics for the moment-matched Gamma/inverse-Gaussian CDF crossing theorem.

Requires Python 3, scipy, numpy. These checks do not replace the proof.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.stats import gamma, invgauss


def cdf_difference(v, t):
    return gamma.cdf(t, 1 / v, scale=v) - invgauss.cdf(t, mu=v, scale=1 / v)


def pdf_log_ratio(v,t):
    return gamma.logpdf(t,1/v,scale=v)-invgauss.logpdf(t,mu=v,scale=1/v)


def density_crossings(v):
    rlo=(2+v-math.sqrt(v*(v+4)))/2
    rhi=1/rlo
    # guaranteed shape from analytic derivative. root brackets search outward.
    assert pdf_log_ratio(v,rlo)<0 <pdf_log_ratio(v,rhi)
    l=rlo
    while pdf_log_ratio(v,l)<0:
        l*=0.5
    h=rhi
    while pdf_log_ratio(v,h)>0:
        h*=2
    return tuple((brentq(lambda t:pdf_log_ratio(v,t),lo,hi,xtol=1e-13)
        for lo,hi in [(l,rlo),(rlo,rhi),(rhi,h)]))


def cumulative_crossings(v):
    a,b,c=density_crossings(v)
    assert cdf_difference(v,a)>0 and cdf_difference(v,b)<0 and cdf_difference(v,c)>0
    return brentq(lambda t:cdf_difference(v,t),a,b,xtol=1e-13),\
           brentq(lambda t:cdf_difference(v,t),b,c,xtol=1e-13)


def main():
    count=0
    for v in [0.005,0.01,0.02,0.05,0.1,0.2,0.4,0.75,1.,2.,4.,8.,12.,20.,40.]:
        a,b,c=density_crossings(v)
        x,y=cumulative_crossings(v)
        checks=[0<a<x<b<y<c, cdf_difference(v,x-1e-3*min(x,1))>0,
                cdf_difference(v,(x+y)/2)<0, cdf_difference(v,y+1e-3)>0,
                math.isclose(gamma.mean(1/v,scale=v),1.,abs_tol=2e-12),
                math.isclose(gamma.var(1/v,scale=v),v,abs_tol=2e-12),
                math.isclose(invgauss.mean(v,scale=1/v),1.,abs_tol=2e-12),
                math.isclose(invgauss.var(v,scale=1/v),v,abs_tol=2e-12)]
        if not all(checks): raise AssertionError((v,checks,a,b,c,x,y))
        count += len(checks)
        print(f'v={v:8g}: density roots={a:.8g},{b:.8g},{c:.8g}; CDF roots={x:.8g},{y:.8g}')
    for v in [.005,.01,.02,.05]:
        x,y=cumulative_crossings(v)
        assert abs((x-1)/math.sqrt(v)+1)<0.30
        assert abs((y-1)/math.sqrt(v)-1)<0.30
        count+=2
    print(f'PASS {count} diagnostic assertions; exact crossing counts follow analytically, not by sampling.')


if __name__=='__main__': main()
