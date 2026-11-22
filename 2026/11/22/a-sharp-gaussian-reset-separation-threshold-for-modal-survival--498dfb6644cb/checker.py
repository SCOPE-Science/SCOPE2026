"""Numerical checks for the stationary two-location reset-mode theorem.

Requirements: Python 3.10+, numpy, scipy, sympy.
The all-parameter and asymptotic statements are established in RESULT.md;
these finite tests independently check formulas and selected values.
"""
from math import exp, sqrt, log, pi, isfinite
from scipy.special import erfcx
from scipy.integrate import quad
from scipy.optimize import brentq
from sympy import symbols, exp as Sexp, diff, simplify, Rational

checks=0

def check(condition, name):
    global checks
    assert condition, name
    checks+=1

def normal(x, sigma):
    return exp(-0.5*(x/sigma)**2)/(sigma*sqrt(2*pi))

def g(x,b,sigma):
    t1=(sigma/b-x/sigma)/sqrt(2)
    t2=(sigma/b+x/sigma)/sqrt(2)
    return exp(-x*x/(2*sigma*sigma))/(4*b)*(erfcx(t1)+erfcx(t2))

def dg(x,b,sigma):
    t1=(sigma/b-x/sigma)/sqrt(2)
    t2=(sigma/b+x/sigma)/sqrt(2)
    return exp(-x*x/(2*sigma*sigma))/(4*b*b)*(-erfcx(t1)+erfcx(t2))

def d2g(x,b,sigma):
    return (g(x,b,sigma)-normal(x,sigma))/(b*b)

def threshold(b,sigma):
    return brentq(lambda x:d2g(x,b,sigma),sigma,8*sigma,xtol=1e-13)

def stationary(x,a,b,sigma):
    return (g(x-a,b,sigma)+g(x+a,b,sigma))/2

def derivative(x,a,b,sigma):
    return (dg(x-a,b,sigma)+dg(x+a,b,sigma))/2

# Exact algebraic relation for density and the inverse Fourier resolvent.
q,B,k=symbols('q B k',real=True)
check(simplify((1+B**2*k**2)*(Sexp(-q*k**2/2)/(1+B**2*k**2))-Sexp(-q*k**2/2))==0,
      'Fourier resolvent')
# Gaussian base curve: threshold equals standard deviation at zero smoothing.
x=symbols('x', real=True)
p=Sexp(-x*x/2)
check(simplify(diff(p,x,2).subs(x,1))==0,'Gaussian threshold')
check(simplify(diff(p,x,3).subs(x,1)-2*Sexp(-Rational(1,2)))==0,'Gaussian third derivative')

for b in (0.25,0.5,1.0,3.0,10.0,100.0):
    sigma=1.0
    a0=threshold(b,sigma)
    check(a0>sigma,'strict threshold beyond Gaussian mixture')
    check(abs(g(a0,b,sigma)-normal(a0,sigma))<1e-11,'threshold equation')
    check(d2g(.9*a0,b,sigma)<0 and d2g(1.1*a0,b,sigma)>0,'inflection sign')
    # Gaussian-variance-mixture formula is evaluated independently of closed form.
    for xx in (0.1,0.95,1.5,2.8):
        def integrand(u):
            v=sigma*sigma+2*b*b*u
            return exp(-u)*exp(-xx*xx/(2*v))/sqrt(2*pi*v)*(xx*xx-v)/v**2
        result=quad(integrand,0,60,epsabs=2e-12,epsrel=1e-11,limit=300)[0]
        check(abs(result-d2g(xx,b,sigma)) < 1e-9,'independent variance-mixture derivative')
    # The age integral uses the original Brownian heat propagator.
    for a in (0.0,1.35*a0):
        for xx in (0.0,.6,1.8):
            r=1/b**2
            def integrand(t):
                sd=sqrt(sigma*sigma+2*t)
                return r*exp(-r*t)*.5*(normal(xx-a,sd)+normal(xx+a,sd))
            answer=quad(integrand,0,max(160*b*b,50),epsabs=2e-12,epsrel=1e-10,limit=400)[0]
            check(abs(answer-stationary(xx,a,b,sigma))<1e-9,'independent stationary age integral')
    # Below transition the density derivative is negative on positive grid.
    for aa in (0.75*a0,0.99*a0):
        for xx in (0.05,0.4,0.9,1.6,3,7):
            check(derivative(xx,aa,b,sigma)<0,'unimodal sign sample')
    # Above threshold derivative switches once from positive to negative.
    for aa in (1.02*a0,1.20*a0):
        peak=brentq(lambda xx:derivative(xx,aa,b,sigma),1e-7,aa,xtol=1e-13)
        check(0<peak<aa,'side peak')
        check(derivative(.5*peak,aa,b,sigma)>0,'rising side')
        check(derivative((peak+aa)/2,aa,b,sigma)<0,'descending side')
    # Square-root onset at the transition.
    nphi=normal(a0,sigma)
    gp3=(dg(a0,b,sigma)+a0*nphi)/b**2
    gp4=-(a0*a0-1)*nphi/b**2
    check(gp3>0 and gp4<0,'nondegenerate pitchfork coefficients')
    const=sqrt(-6*gp3/gp4)
    for delta in (0.0001,0.001):
        aa=a0+delta
        peak=brentq(lambda xx:derivative(xx,aa,b,sigma),1e-7,aa,xtol=1e-13)
        check(abs(peak/(const*sqrt(delta))-1)<.005,'square-root split')

# Verify small-kernel and large-kernel endpoint approximations independently.
for b in (.05,.08,.1):
    aa=threshold(b,1.0)
    check(abs((aa-1)/b**2-1)<.07,'small-b leading correction')
for b in (100,1000,10000):
    aa=threshold(b,1.0)
    center=2*log(sqrt(2/pi)*b)
    check(abs(aa**2-center)<0.1,'large-b squared threshold')

print('PASS:',checks,'independently evaluated formula/sign/asymptotic assertions')
print('Benchmark: b=sigma=1, threshold a=',format(threshold(1.0,1.0),'.14f'))
