"""Deterministic checks for Thomas–Fermi reset-age density fluctuation minimization.
Usage: python check.py. Requires SciPy and SymPy.
All quantities use dimensionless omega=x0=1 unless specified.
"""
import math
from scipy.integrate import quad
import sympy as sp


def moments(r, exponents=(1, 2, 3, 4, 6)):
    # Independent change of variables lambda=1+s**2 in the normalized
    # exponential-reset-age integral from the exact expansion clock.
    def one(k):
        def integrand(s):
            lam=1+s*s
            clock=(s*math.sqrt(lam)+math.asinh(s))/math.sqrt(2)
            return math.sqrt(2)*r*math.exp(-r*clock)*lam**(0.5-k)
        return quad(integrand,0,math.inf,epsabs=3e-12,epsrel=3e-12,limit=400)[0]
    return {k:one(k) for k in exponents}


def direct_variance(r, y):
    # Separate stable quadrature using individual profile and its mean.
    def integration(func):
        def integrand(s):
            lam=1+s*s
            t=(s*math.sqrt(lam)+math.asinh(s))/math.sqrt(2)
            u=1/lam
            return math.sqrt(2)*r*math.exp(-r*t)*math.sqrt(lam)*func(u)
        return quad(integrand,0,math.inf,epsabs=8e-12,epsrel=5e-12,limit=400)[0]
    mean=integration(lambda u: u-y*u**3)
    return integration(lambda u:(u-y*u**3-mean)**2)


def main():
    assert sp.simplify((sp.beta(3,sp.Rational(1,2))/sp.beta(5,sp.Rational(1,2))-sp.Rational(21,16)).rewrite(sp.gamma))==0
    assert sp.simplify((sp.beta(1,sp.Rational(1,2))-2*sp.beta(3,sp.Rational(1,2))+sp.beta(5,sp.Rational(1,2))-sp.Rational(214,315)).rewrite(sp.gamma))==0
    EA2=sp.factorial(2); EA4=sp.factorial(4); EA6=sp.factorial(6); EA8=sp.factorial(8)
    V2=EA4-EA2**2; V4=EA8-EA4**2; C24=EA6-EA2*EA4
    delta=C24/(6*V2)
    coefficient=sp.Rational(9,16)*(V4-C24**2/V2)/16
    assert delta==sp.Rational(28,5),delta
    assert coefficient==sp.Rational(12069,20),coefficient
    expected_zero=sp.Rational(107,280)/sp.sqrt(2)
    for r in (0.007,0.025,0.08,0.4,1,3,10,35,80):
        m=moments(r)
        c=m[4]-m[1]*m[3]
        v=m[6]-m[3]**2
        assert c>0 and v>0,(r,c,v)
        y=min(1,c/v)
        assert 0<y<=1
        vv=(m[2]-m[1]**2)-2*y*c+y*y*v
        direct=direct_variance(r,y)
        if abs(vv)>1e-11: assert abs(vv-direct) < 2e-8*(1+direct), (r,vv,direct)
        for test in (0,0.3,0.7,1):
            testvar=direct_variance(r,test)
            assert direct <= testvar+2e-11,(r,y,test,direct,testvar)
        if r < 0.08:
            assert y==1,(r,y)
        if r >= 35:
            assert abs(y-1/3)<0.01,(r,y)
    # Asymptotic small reset-time coefficient at edge is checked independently.
    for r in (0.00005, 0.00002):
        v=direct_variance(r,1)
        exactlimit=214/315/math.sqrt(2)
        assert abs(v/r/exactlimit-1)<0.025, (r,v/r,exactlimit)
    import mpmath as mp
    mp.mp.dps=42
    for rr in (80,160):
        rat=mp.mpf(rr)
        def Mm(k):
            return mp.quad(lambda u: mp.sqrt(2)*rat*mp.exp(-rat*(u*mp.sqrt(1+u*u)+mp.asinh(u))/mp.sqrt(2))*(1+u*u)**(mp.mpf('0.5')-k), [0,mp.mpf('.2'),1,mp.inf])
        ms={k:Mm(k) for k in (1,2,3,4,6)}
        cov=ms[4]-ms[1]*ms[3]
        v3=ms[6]-ms[3]**2
        y=cov/v3
        vmin=mp.mpf(9)/16*(ms[2]-ms[1]**2-2*y*cov+y*y*v3)
        assert abs(vmin*rat**8 / (mp.mpf(12069)/20)-1) < mp.mpf('.052')
        assert abs((y-mp.mpf(1)/3)*rat**2/(mp.mpf(28)/5)-1)<mp.mpf('.06')
    print('PASS: beta/Gamma constants, exact exponential moment coefficients, optimization for 9 reset rates, spatial direct variance comparisons, slow-rate edge law and 80/160 high-precision rapid-rate coefficients')

if __name__=='__main__':
    main()
