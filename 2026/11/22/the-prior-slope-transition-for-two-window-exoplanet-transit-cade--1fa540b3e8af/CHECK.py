"""Reproduce numerical examples and diagnostic checks for ideal two-window transit timing.

Python 3 standard library only. Numerical integration and grids are finite diagnostics;
the accompanying mathematical proof, not this checker, proves uniqueness.
"""
from math import sqrt, log, isclose


def prior_weight(p, beta):
    return p**(beta-1)


def integral_weight(lo, hi, beta):
    if hi <= lo:
        return 0.0
    if beta == 0:
        return log(hi/lo)
    return (hi**beta-lo**beta)/beta


def derivative(lag, a, b, width, beta):
    plus_lo, plus_hi = max(a, lag), min(b, lag+width)
    minus_lo, minus_hi = max(a, lag-width), min(b, lag)
    return (integral_weight(plus_lo, plus_hi, beta)
            - integral_weight(minus_lo, minus_hi, beta))


def score(lag, a, b, width, beta):
    # unnormalized expected probability; normalization independent of lag
    # integrate triangular overlap / P, splitting at lag
    x0, x1 = max(a, lag-width), min(b,lag)
    y0, y1 = max(a,lag),min(b,lag+width)
    def moment(lo, hi, powr):
        if hi<=lo: return 0.
        k=powr+1
        if k==0: return log(hi/lo)
        return (hi**k-lo**k)/k
    left = (width-lag)*moment(x0,x1,beta-1)+moment(x0,x1,beta)
    right = (width+lag)*moment(y0,y1,beta-1)-moment(y0,y1,beta)
    return left+right


def bisect(f, lo, hi):
    assert f(lo)>0 and f(hi)<0
    for _ in range(90):
        mid=(lo+hi)/2
        if f(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def theorem_lag(a,b,w,beta):
    assert 0<w and a+2*w<=b and b+2*w<2*a
    if beta<1:
        return bisect(lambda l:derivative(l,a,b,w,beta),a,a+w)
    if beta>1:
        return bisect(lambda l:derivative(l,a,b,w,beta),b-w,b)
    return None


def run():
    count=0
    for a in (2.,3.,5.,7.,11.):
        for w in (.08,.12,.2,.3):
            if 6*w>=a: continue
            for span in (2.01*w,2.5*w,3*w):
                b=a+span
                if b+2*w>=2*a:continue
                for beta in (-3.,-2.,-1.,0.,.3,.75,1.,1.25,2.,3.):
                    star=theorem_lag(a,b,w,beta)
                    if beta==1:
                        base=score(a+w,a,b,w,beta)
                        for frac in (0,.2,.5,.8,1):
                            t=a+w+frac*(b-a-2*w)
                            assert abs(score(t,a,b,w,beta)-base)<2e-10
                            count+=1
                    else:
                        assert a<=star<=b
                        assert abs(derivative(star,a,b,w,beta))<1e-8
                        count+=2
                        best=score(star,a,b,w,beta)
                        for i in range(101):
                            t=a-w+(b-a+2*w)*i/100
                            assert score(t,a,b,w,beta)<=best+1e-9
                            count+=1
    a,b,w=3.,4.,.2
    lo=theorem_lag(a,b,w,0.)
    hi=theorem_lag(a,b,w,2.)
    assert abs(lo-(a+sqrt(a*a+4*a*w))/2)<1e-12
    assert abs(hi-(-w+sqrt(b*b+2*w*w)))<1e-12
    print('uniform-period optimum',format(lo,'.12f'))
    print('quadratically weighted-period optimum',format(hi,'.12f'))
    print('linear-period prior plateau',a+w,b-w)
    print('diagnostic assertions:',count+2)


if __name__=='__main__':run()
