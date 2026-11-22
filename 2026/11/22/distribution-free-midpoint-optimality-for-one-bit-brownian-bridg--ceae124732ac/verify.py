"""Supplementary numerical checks for one-bit Brownian bridge occupation design.

This checker tests formulas and finite parameter grids. The infinite and
all-noise-design claims are justified by the analytic proof, not by this code.
"""
import math
from scipy.integrate import quad
from scipy.special import ndtr

PI = math.pi
SQRT2 = math.sqrt(2.0)

def rho(s,t):
    if s <= t:
        return math.sqrt(s*(1.0-t)/(t*(1.0-s))) if s else 0.0
    return math.sqrt(t*(1.0-s)/(s*(1.0-t))) if s < 1 else 0.0

def c_noiseless(t):
    return (math.sqrt(t)+math.sqrt(1.0-t)-1.0)/2.0

def c_gauss_integral(t,a):
    fun=lambda s:math.asin(min(1.0,a*rho(s,t)))/PI
    return quad(fun,0.0,t,epsabs=3e-12)[0]+quad(fun,t,1.0,epsabs=3e-12)[0]

def c_gauss_mid_formula(a):
    theta=PI/2 if a == 1 else math.atan(math.sqrt((1+a*a)/(1-a*a)))
    return (-math.asin(a)+2*a/math.sqrt(1+a*a)*theta)/PI

def corr_rademacher(rho_val,noise_magnitude):
    if rho_val <= 0: return 0.0
    if rho_val >= 1:
        return 2*(1-ndtr(noise_magnitude))
    a=rho_val/math.sqrt(1-rho_val*rho_val)
    fun=lambda y: math.exp(-y*y/2)/math.sqrt(2*PI)*(2*ndtr(a*y)-1)
    return 2*quad(fun,noise_magnitude,math.inf,epsabs=1e-10)[0]

def c_rademacher(t,r):
    fun=lambda s:.5*corr_rademacher(rho(s,t),r)
    return quad(fun,0.0,t,epsabs=2e-8)[0]+quad(fun,t,1.0,epsabs=2e-8)[0]

def check():
    checks=0
    for t in [.03,.1,.2,.35,.5,.65,.8,.9,.97]:
        got=c_gauss_integral(t,1.0)
        assert abs(got-c_noiseless(t))<1.0e-9,(t,got,c_noiseless(t))
        checks+=1
    for a in [.01,.10,.35,.70,.90,.99,1.0]:
        got=c_gauss_integral(.5,a)
        assert abs(got-c_gauss_mid_formula(a))<1e-9,(a,got,c_gauss_mid_formula(a))
        checks+=1
        for t in [.06,.17,.3,.42,.58,.7,.83,.94]:
            got=c_gauss_integral(t,a)
            assert got < c_gauss_mid_formula(a)-1e-8,(a,t,got)
            checks+=1
    for sd in [.15,.8,2.0]:
        central=c_gauss_mid_formula(1.0/math.sqrt(1+4*sd*sd))
        for t in [.08,.2,.35,.45,.55,.65,.8,.92]:
            a=1/math.sqrt(1+sd*sd/(t*(1-t)))
            assert c_gauss_integral(t,a)<central-1e-9
            checks+=1
    for r in [0.0,.4,1.2]:
        mid=c_rademacher(.5,r)
        for t in [.1,.25,.4,.6,.75,.9]:
            assert c_rademacher(t,r)<mid-1e-7,(r,t,c_rademacher(t,r),mid)
            checks+=1
    assert abs(1/12-c_noiseless(.5)**2-(3*SQRT2-4)/6)<1e-14
    checks+=1
    assert abs(12*c_noiseless(.5)**2-(9-6*SQRT2))<1e-14
    checks+=1
    print(f'PASS: {checks} deterministic formula and strict-grid checks')
    print('Noiseless optimal MSE:',(3*SQRT2-4)/6)
    print('Noiseless fraction explained:',9-6*SQRT2)

if __name__=='__main__':
    check()
