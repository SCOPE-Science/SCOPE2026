"""Supplementary exact-rational and numerical checks of the stated runoff-memory identities.

Requires only Python 3 standard library. Finite tests supplement, not replace, the proof.
"""
from fractions import Fraction as F
from math import exp, isclose
from random import Random


def terms(a, h):
    z = exp(-h)
    u = 2*z-z*z
    v = 1-2*h*z-z*z
    w = (h-1)*z+z*z
    d = u+(1-a)/(1+a)*v
    n = (1-a)*w+a*(1-a)/(1+a)*v
    return z, u, v, w, d, n, n/d


def root(fun, lo, hi, iterations=130):
    assert fun(lo)*fun(hi)<0
    for _ in range(iterations):
        mid=(lo+hi)/2
        if fun(lo)*fun(mid)<=0:hi=mid
        else:lo=mid
    return (lo+hi)/2


def deriv_poly_identity(a, h, z):
    # Treat h,z as independent rational symbols, imposing dz/dh=-z.
    u=2*z-z*z; v=1-2*h*z-z*z; w=(h-1)*z+z*z
    ud=-2*z+2*z*z
    vd=-2*z+2*h*z+2*z*z
    wd=z*(2-h)-2*z*z
    d=u+(1-a)/(1+a)*v
    n=(1-a)*w+a*(1-a)/(1+a)*v
    dd=ud+(1-a)/(1+a)*vd
    nd=(1-a)*wd+a*(1-a)/(1+a)*vd
    return (nd*d-n*dd)*(1+a)==(1-a)*z*(2*(1-z)-(1-a)*h)


def run():
    total=0
    rng=Random(20241118)
    for i in range(1500):
        a=F(rng.randint(1,99),100)
        h=F(rng.randint(1,200),20)
        z=F(rng.randint(1,99),100)
        assert deriv_poly_identity(a,h,z)
        total+=1
    for a in (0.1,0.2,0.35,0.5,0.65,0.8):
        hc=root(lambda h:(1-a)*h+exp(-h)-(1+a), 0, 1000)
        hs=root(lambda h:2*(1-exp(-h))-(1-a)*h,1e-7,1000)
        assert 0<hc<hs
        assert terms(a,hs)[-1]>a
        for h in (0.05,0.25,0.75,1.5,2.0,hc/2,hc,hs,(hc+hs)/2,hs+1,hs+9):
            z,u,v,w,d,n,r=terms(a,h)
            assert u>0 and v>0 and w>0 and d>0
            assert isclose(r-a,z*((1-a)*h-(1+a)+z)/d,rel_tol=2e-9,abs_tol=2e-12)
            dx=1e-5
            if h>dx:
                finite=(terms(a,h+dx)[-1]-terms(a,h-dx)[-1])/(2*dx)
                exact=(1-a)*z*(2*(1-z)-(1-a)*h)/((1+a)*d*d)
                assert isclose(finite,exact,rel_tol=1e-5,abs_tol=3e-8)
            total+=3
        assert terms(a,hc*0.75)[-1]<a
        assert terms(a,(hc+hs)/2)[-1]>a
        assert terms(a,hs+0.1)[-1]<terms(a,hs)[-1]
        total+=4
    assert isclose(root(lambda h:.5*h+exp(-h)-1.5,0,100),2.8887033561931896,abs_tol=1e-10)
    assert isclose(root(lambda h:2*(1-exp(-h))-.5*h,1e-7,100),3.9206903948728877,abs_tol=1e-10)
    total+=2
    print('PASS:',total,'supplementary assertions')


if __name__=='__main__':
    run()
