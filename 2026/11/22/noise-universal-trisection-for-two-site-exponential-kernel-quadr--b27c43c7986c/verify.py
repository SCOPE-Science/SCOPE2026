"""Independent checks for two-observation stationary exponential-kernel quadrature.
No proof step relies on these finite numerical checks.
"""
import math, random
from statistics import fmean


def kernel_mean(t, lam):
    return (2-math.exp(-lam*t)-math.exp(-lam*(1-t)))/lam


def capture_direct(x, y, lam, eta):
    r=math.exp(-lam*abs(y-x))
    a=1+eta
    u=kernel_mean(x,lam);v=kernel_mean(y,lam)
    return (a*(u*u+v*v)-2*r*u*v)/(a*a-r*r)


def root_s(lam, eta):
    L=lam/2; a=1+eta
    def g(s):
        return math.exp(s)+a*math.exp(2*s)*math.sinh(s)-math.exp(L)
    lo=0.;hi=L
    assert g(lo)<0<g(hi)
    for _ in range(95):
        md=(lo+hi)/2
        if g(md)<0: lo=md
        else:hi=md
    return (lo+hi)/2


def optimum(lam, eta):
    s=root_s(lam,eta)
    x=.5-s/lam; y=.5+s/lam
    q=math.exp(-lam/2)
    m=2*(1-q*math.cosh(s))/lam
    gain=2*m*m/(1+eta+math.exp(-2*s))
    variance=2*(lam-1+math.exp(-lam))/(lam*lam)-gain
    return x,y,gain,variance


def run():
    rng=random.Random(20261116)
    ct=0
    for lam in (.05,.1,.3,1.,2.,5.,10.):
      for eta in (.001,.01,.1,1.,10.,100.):
        x0,y0,g,v=optimum(lam,eta)
        assert 0 < x0 < .5 < y0 < 1
        assert math.isclose(x0+y0,1,rel_tol=0,abs_tol=3e-15)
        assert math.isclose(capture_direct(x0,y0,lam,eta),g,rel_tol=2e-13,abs_tol=1e-13)
        assert capture_direct(.5,.5,lam,eta)<g
        for _ in range(100):
            x=rng.random();y=rng.random()
            f=capture_direct(x,y,lam,eta)
            if f>g+1e-12:
                raise AssertionError((lam,eta,x,y,f,g))
            ct+=1
    # For fixed separation, reflected centering is never worse than any translation.
    cd=0
    for lam in (.1,.5,2.,6.,10.):
      for eta in (.00001,.1,10.):
        for _ in range(200):
            sep=rng.random()
            x=rng.random()*(1-sep)
            y=x+sep
            a=(1-sep)/2
            f=capture_direct(x,y,lam,eta)
            fc=capture_direct(a,1-a,lam,eta)
            if f>fc+2e-12:raise AssertionError((lam,eta,x,y,f,fc))
            cd+=1
    # Independent one-dimensional direct optimization via a dense grid.
    for lam in (.1,1.,5.,10.):
        for eta in (.01,.3,5.):
            _,_,best,_=optimum(lam,eta)
            for j in range(501):
                d=j/1000
                f=capture_direct(.5-d,.5+d,lam,eta)
                assert f<=best+2e-12
    # At noise variance equal to marginal process variance, all decay rates
    # have optimal trisection nodes and simple equal weights.
    for lam in (.01,.1,.5,1.,2.,5.,15.):
        x,y,_,var=optimum(lam,1.)
        assert abs(x-1/3)<1e-13 and abs(y-2/3)<1e-13
        assert math.isclose(var,2*(lam-3+3*math.exp(-lam/3))/(lam*lam),rel_tol=4e-10,abs_tol=1e-11)
        a=1+1.; r=math.exp(-lam/3)
        w=kernel_mean(1/3,lam)/(a+r)
        assert math.isclose(w,-math.expm1(-lam/3)/lam,rel_tol=1e-12,abs_tol=1e-12)
    # High-noise asymptotic of the unique positive root.
    for lam in (.1,1.,3.):
        for eta in (1e5,1e6):
            s=root_s(lam,eta)
            ratio=s*(eta+2)/(math.expm1(lam/2))
            assert abs(ratio-1)<1e-4, (lam,eta,ratio)
    # Weak-correlation kernel limit for sampling positions.
    for eta in (.0,.5,5.):
        x,_,_,_=optimum(1e-5,eta)
        assert abs(x-(1+eta)/(2*(2+eta)))<5e-6
    print('PASS: 4200 unconstrained pairs, 3000 translations, 6012 symmetric-grid checks, high-noise and small-decay limits')

if __name__=='__main__':run()
