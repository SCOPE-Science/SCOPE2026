"""Independent numerical checks of Gaussian line-shift information-rate formulas.

Run with standard Python 3: python verify.py
The proof of global uniqueness and limits is analytic, not based on this grid.
"""
from math import erf, exp, pi, sqrt, isclose
from random import Random

SQPI = sqrt(pi)
checks = 0

def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def E(x):
    if x < 1e-6:
        return 1.0 - 2.0*x*x/3.0 + 8.0*x**4/45.0
    return 2.0*x*exp(-x*x)/(SQPI*erf(x))

def bisect(f, lo, hi, iters=110):
    flo, fhi = f(lo), f(hi)
    require(flo > 0 and fhi < 0, 'root bracket')
    for _ in range(iters):
        mid = (lo + hi)/2.0
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi)/2

def fixed_root(d):
    return bisect(lambda x: 2*E(x)-1-x/(x+d),1e-12,3.0)

def matched_F(x):
    if x < 1e-3:
        return x-(2/3)*x**3+(8/15)*x**5
    return (SQPI/2)*erf(2*x)-(-expm1_safe(-4*x*x))/(4*x)

def expm1_safe(x):
    from math import expm1
    return expm1(x)

def matched_Fprime(x):
    return -expm1_safe(-4*x*x)/(4*x*x)

def matched_root(d):
    f=lambda x: (x+d)*matched_Fprime(x)-matched_F(x)
    hi=max(2.0,2*sqrt(d)+2)
    return bisect(f,1e-8,hi)

def fixed_rate(x,d):
    return (pi/4)*(erf(x)**2)/(x*(x+d))

def matched_rate(x,d):
    return matched_F(x)/(x+d)

def simpson(fun, hi, n=2000):
    step=hi/n
    return (step/3)*(fun(0)+fun(hi)+4*sum(fun(step*j) for j in range(1,n,2))+2*sum(fun(step*j) for j in range(2,n,2)))

x0=bisect(lambda x:2*E(x)-1,1e-10,3)
r0=SQPI*erf(x0)**2/(2*x0)
require(abs(x0-0.9899390828419045)<1e-12,'large overhead fixed root')
require(abs(r0-0.6293963793249794)<1e-12,'large overhead retention')
for d in [1e-5,1e-4,1e-3,0.01,0.1,1,3,10,100,1e3,1e5]:
    xf=fixed_root(d)
    xm=matched_root(d)
    require(0 < xf < x0, 'fixed duration bound')
    require(xm>0,'matched duration positive')
    require(abs(2*E(xf)-1-xf/(xf+d))<1e-9,'fixed stationarity')
    require(abs((xm+d)*matched_Fprime(xm)-matched_F(xm))<1e-8,'matched stationarity')
    require(fixed_rate(xf,d)<matched_rate(xm,d),'template loss')
    for s in [.1,.5,.8,1.2,2,4,7]:
        if s!=1.0:
            require(fixed_rate(s*xf,d)<=fixed_rate(xf,d)*(1+1e-12),'fixed global check')
            require(matched_rate(s*xm,d)<=matched_rate(xm,d)*(1+1e-12),'matched global check')
for d in [1e-7,1e-6,1e-5]:
    asymp=(3*d/4)**(1/3)
    require(abs(fixed_root(d)/asymp-1)<0.015,'fixed cube-root limit')
    require(abs(matched_root(d)/asymp-1)<0.015,'matched cube-root limit')
for d in [1e4,1e6,1e8]:
    xf=fixed_root(d)
    xm=matched_root(d)
    require(abs(xf/x0-1)<0.002,'fixed saturation')
    require(abs(xm/sqrt(d/(2*SQPI))-1)<0.05,'matched square-root')
    require(abs(fixed_rate(xf,d)/matched_rate(xm,d)-r0)<0.07,'efficiency-limit approach')
rng=Random(2026)
for j in range(300):
    x=10**rng.uniform(-1.4,1)
    # Direct quadrature of the integrated autocorrelation (K(u)=exp(-4u^2)).
    integral=2*simpson(lambda u:(x-u)*exp(-4*u*u),x,600)/x
    require(abs(integral-matched_F(x))<5e-7,'integrated autocorrelation')
    d=10**rng.uniform(-3,3)
    xf=fixed_root(d)
    xm=matched_root(d)
    for u in [0.2,0.5,2,4]:
        require(fixed_rate(xf*u,d)<=fixed_rate(xf,d)*(1+1e-11),'fixed peak random')
        require(matched_rate(xm*u,d)<=matched_rate(xm,d)*(1+1e-11),'matched peak random')
print('PASS',checks,'numerical assertions')
print('universal root',format(x0,'.15f'))
print('limiting fixed/full information ratio',format(r0,'.15f'))
print('illustration: beta=0.0005 s^-1; overhead=14s; fixed and full lengths',
      format(fixed_root(.0005*14)/.0005,'.7f'),
      format(matched_root(.0005*14)/.0005,'.7f'))
