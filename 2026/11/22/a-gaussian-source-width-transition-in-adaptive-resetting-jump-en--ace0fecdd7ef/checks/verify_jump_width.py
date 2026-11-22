"""Deterministic checks for an adaptive Gaussian-reset entropy-width theorem.
Requires Python 3 and scipy; numerical tests do not prove the asymptotic statements.
"""
from math import sqrt, exp, log, pi, sin
from scipy.integrate import quad
from scipy.special import gamma
from scipy.optimize import minimize_scalar

def min_rate(z,a=1.0):
    if not 0.0 < z < 1.0:
        raise ValueError('width fraction outside (0,1)')
    if z < 1./3.:
        return a*2*z**1.5/(1-z)*exp((1-3*z)/(2*z))
    return a*sqrt(z)

def dimensionless_f(y,z):
    return sqrt(z)*(2*z*y-1)*exp((1-z)*y)

def second_moment(z):
    return z*(3*z*z-2*z+1)/(2*z-1)**2.5

def integrate_gamma(fun,split=()):
    # y=t^2 removes the integrable gamma density singularity at zero.
    cuts=[0.] + sorted(sqrt(v) for v in split if 0<v<400) + [20.]
    return sum(quad(lambda t:2/sqrt(pi)*exp(-t*t)*fun(t*t),lo,hi,epsabs=1e-13,epsrel=5e-12,limit=200)[0]
               for lo,hi in zip(cuts,cuts[1:]))

def jump_entropy(R,z):
    if R<=min_rate(z):raise ValueError('hazard nonpositive')
    ystar=1/(2*z)
    yR=log(R)/(1-z)
    return integrate_gamma(lambda y:dimensionless_f(y,z)*__import__('math').log1p(dimensionless_f(y,z)/R),(ystar,yR))

def low_asymptotic(z,R):
    p=1/(1-z);theta=1-z;B=2*z**1.5
    K=B**p/(sqrt(pi)*theta**(p-.5))
    return K*p*pi/((p-1)*sin(pi*(p-1)))*R**(1-p)*log(R)**(p-.5)

def critical_profile(lam):
    return quad(lambda t:t**1.5*exp(-2*lam*t)/(2*sqrt(pi)),0.,2.,epsabs=1e-13)[0]

def check_close(x,y,tol=1e-8):
    if abs(x-y)>tol*max(1.,abs(x),abs(y)):
        raise AssertionError(f'not close: {x} vs {y}; tolerance {tol}')

checks=0
for z in (.1,.2,.3,.3333333333333333,.4,.49,.5,.6,.8,.9):
    y_max=max(2.,2./z)
    opt=minimize_scalar(lambda y: dimensionless_f(y,z),bounds=(0.,y_max),method='bounded',options={'xatol':1e-12})
    actual=-min(0.,opt.fun,dimensionless_f(0,z))
    check_close(actual,min_rate(z),3e-7);checks+=1
    ef=integrate_gamma(lambda y: dimensionless_f(y,z),(1/(2*z),))
    check_close(ef,0.,5e-8);checks+=1
for z in (.54,.6,.67,.8,.9):
    ef2=integrate_gamma(lambda y:dimensionless_f(y,z)**2,(1/(2*z),))
    check_close(ef2,second_moment(z),4e-7);checks+=1
for z in (.2,.4,.5,.6,.8):
    rates=[max(2*min_rate(z),2),max(20*min_rate(z),20),max(200*min_rate(z),200)]
    vals=[jump_entropy(R,z) for R in rates]
    if not (vals[0]>vals[1]>vals[2]>0):raise AssertionError((z,vals))
    checks+=3
for z in (.32,.4,.7,.85):
    R=1e9
    j=jump_entropy(R,z)
    if z<.5: a=low_asymptotic(z,R)
    else:a=second_moment(z)/R
    if not .5<j/a<1.6:raise AssertionError((z,j/a))
    checks+=1
for lam in (-1.,0.,1.):
    R=1e12;L=log(R);z=.5+lam/L
    j=jump_entropy(R,z)
    pred=L**2.5/R*critical_profile(lam)
    if not .25<j/pred<1.4:raise AssertionError((lam,j/pred))
    checks+=1
print(f'PASS: {checks} numerical/structural checks; asymptotic tolerance is deliberately broad')
