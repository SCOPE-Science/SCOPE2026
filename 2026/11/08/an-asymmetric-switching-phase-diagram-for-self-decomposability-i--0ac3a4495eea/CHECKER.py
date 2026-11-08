"""Finite independent arithmetic checks for explicit switch-modulated trap laws.
Requires Python 3 and SciPy (scipy.special.kv, scipy.integrate.quad).
These are diagnostics only; the proof of the phase diagram is analytic.
"""
from math import exp, sqrt, log, pi, isclose
from scipy.special import kv, gamma
from scipy.integrate import quad

COUNT=0

def check(value, message, atol=1.e-8, rtol=1.e-7):
    global COUNT
    assert abs(value-message[0]) <= atol+rtol*abs(message[0]), (message[1],value,message[0])
    COUNT+=1

def f(d,c,r):
    nu=d/2
    return 2/(2*pi)**nu * (sqrt(c)/r)**nu*kv(nu,sqrt(c)*r)

def canonical(d,u,v,r):
    return r**d*((1+u/2)*f(d,v,r)-f(d,u+v,r))

def deriv(d,u,v,r):
    nu=d/2
    C=2/(2*pi)**nu
    return -C*r**(nu)*((1+u/2)*(sqrt(v))**(nu+1)*kv(nu-1,sqrt(v)*r)
        -(sqrt(u+v))**(nu+1)*kv(nu-1,sqrt(u+v)*r))

def cf(u,v,q):
    return exp(-q*q/2)*(1+q*q/(u+v))*(1+q*q/v)**(-1-u/2)

for u in [.2,.9,2,6]:
    for v in [.4,1.,1.8,2.,3.2]:
        for q in [.15,.7,1.9]:
            # characteristic exponent and Fourier integral of 1D Levy measure
            A=1+u/2
            exponent=q*q/2+A*log(1+q*q/v)-log(1+q*q/(u+v))
            integral=quad(lambda x: (1-__import__('math').cos(q*x))*(A*exp(-sqrt(v)*x)-exp(-sqrt(u+v)*x))/x,
                          0,180/sqrt(v),epsabs=3.e-9)[0]
            check(2*integral+q*q/2,(exponent,'Levy transform'),2.e-7)
            check(exp(-exponent),(cf(u,v,q),'CF inversion'))
        for d in (1,2,3,4):
            for r in (.08,.4,1.1,3.):
                h=1.e-5*min(1.,r)
                numerical=(canonical(d,u,v,r+h)-canonical(d,u,v,r-h))/(2*h)
                check(numerical,(deriv(d,u,v,r),'Bessel derivative'),4.e-6,2.e-5)
                assert canonical(d,u,v,r)>0
                COUNT+=1
                threshold=(4/(u+4)) if d==1 else 2.
                if v>=threshold+1.e-8:
                    assert deriv(d,u,v,r)<=1.e-8, (d,u,v,r)
                    COUNT+=1
        # stationary variance from characteristic function
        eps=1.e-4
        numeric=2*(1-cf(u,v,eps))/(eps*eps)
        expected=1-2/(u+v)+(u+2)/v
        check(numeric,(expected,'variance'),3.e-7)

# At the low-rate non-SD threshold the signed BDLP jump density is negative near origin.
for u in (.2,.9,2,6):
    for d in (1,2,3,4):
        v=(4/(u+4))*.75 if d==1 else 1.5
        signs=[deriv(d,u,v,r) for r in (1.e-7,1.e-5,1.e-3,.01,.04)]
        assert any(x>0 for x in signs), ('positive-derivative witness',d,u,v,signs)
        COUNT+=1

# Conditional generator-moment identity for d=1.
for u in (.2,1.,3.):
    for v in (.6,1.5,2.5):
        m1=(v/(u+v))*(1+u/v) # not used: check exact fixed-state second moments
        on_var=1+u/v
        off_var=on_var+2/v
        stat=(v*on_var+u*off_var)/(u+v)
        expected=1-2/(u+v)+(u+2)/v
        check(stat,(expected,'moment generator'),1.e-10)
print(f'CHECKER PASSED: {COUNT} finite numerical / arithmetic assertions')
