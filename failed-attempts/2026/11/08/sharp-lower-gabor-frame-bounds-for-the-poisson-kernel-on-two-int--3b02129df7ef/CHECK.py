"""Standalone numerical and symbolic verification of the Poisson-kernel Gabor lower bound.

No finite numerical check replaces the analytic proof in RESULT.md.
Requires numpy, scipy, sympy.
"""
import math
import numpy as np
from scipy.optimize import differential_evolution
import sympy as sp

checks = 0

def check(ok, reason):
    global checks
    if not bool(ok):
        raise AssertionError(reason)
    checks += 1

def zak_closed(x, nu, w):
    r = math.exp(-2*math.pi*w)
    z = np.exp(2j*math.pi*x)
    a = r**nu
    b = r**(1-nu)
    return math.pi/w*np.exp(2j*math.pi*nu*x)*(a/(1-r*z)+b/(z-r))

def zak_direct(x, nu, w, N=4000):
    k = np.arange(-N,N+1,dtype=np.float64)
    return np.sum(np.exp(-2j*np.pi*k*nu)/((x+k)**2+w*w))

def lower(w, theta):
    d = min(theta % 1.0,(-theta) % 1.0)
    return (8*math.pi**2/w**2 * math.sinh(math.pi*w)**2 *
            math.sin(math.pi*d/2)**2 / (math.cosh(2*math.pi*w)+math.cos(math.pi*d))**2)

# Symbolic identity for the numerator of |Zak|^2, with ab=r.
a,b,r,c = sp.symbols('a b r c',positive=True,real=True)
P=a-r*b
Q=b-r*a
numer=sp.expand(P*P+Q*Q+2*c*P*Q)
target=(1+r*r-2*r*c)*(a*a+b*b)+(-4*r*r+2*r*(1+r*r)*c)
check(sp.simplify((numer-target).subs(a*b,r))==0, 'Zak algebra identity')
t, beta = sp.symbols('t beta',real=True,positive=True)
f=t/(beta+1-2*t)**2
check(sp.simplify(sp.diff(f,t)-(beta+1+2*t)/(beta+1-2*t)**3)==0,'positive first derivative')
check(sp.simplify(sp.diff(f,t,2)-8*(beta+1+t)/(beta+1-2*t)**4)==0,'positive second derivative')

for w in [0.2,0.45,1.0,1.8]:
    for x in [0.05,0.22,0.49,0.69,0.96]:
        for nu in [0.1,0.35,0.5,0.77]:
            v1=zak_closed(x,nu,w)
            v2=zak_direct(x,nu,w)
            check(abs(v1-v2)<1e-6,'Poisson summation real-space cross-check')
    for theta in [0.037,0.13,0.29,0.5,0.73,0.98]:
        A=lower(w,theta)
        for x in np.arange(0.0,1.0,0.023):
            for nu in [0,0.09,0.27,0.5,0.71,0.91]:
                measured=abs(zak_closed(x,nu,w))**2+abs(zak_closed(x-theta,nu,w))**2
                check(measured>=A-2e-9,'global candidate lower bound')
        d=min(theta,1-theta)
        center=.5+ (theta/2 if theta<=.5 else (theta-1)/2)
        measured=abs(zak_closed(center,.5,w))**2+abs(zak_closed(center-theta,.5,w))**2
        check(abs(measured-A)<1e-9,'exact minimizer equality')
        if theta in [.037,.29,.5]:
            res=differential_evolution(lambda q: abs(zak_closed(q[0],q[1],w))**2+
                abs(zak_closed(q[0]-theta,q[1],w))**2,[(0,1),(0,1)],
                seed=43,popsize=12,tol=1e-9,polish=True,maxiter=600)
            check(abs(res.fun-A)<1e-8,'global numerical minimizer')
    for h in [1e-2,3e-3,1e-3]:
        c=(math.pi**4/(2*w*w))*math.tanh(math.pi*w)**2/math.cosh(math.pi*w)**2
        check(abs(lower(w,h)/h**2/c-1)<2e-3,'quadratic collision asymptotic')
print('POISSON_TWO_COSET_CHECKS_PASSED',checks)
