"""Independent algebraic and numerical checks for one-bit telegraph integral design.

Analytic sign and convexity arguments in RESULT.md establish global uniqueness;
numerical grids and simulation here are diagnostic, not uniqueness proofs.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

z, p, k = sp.symbols('z p k', positive=True)
d = 2 - (2-p)*z - p/z
s = p/z**2 - (2-p) + 2*k*(z-p)
f = d*d/(1-k*z*z)
assert sp.simplify(sp.diff(f,z) - 2*d*s/(1-k*z*z)**2) == 0
assert sp.expand(z*z*s - (2*k*z**3-(2-p+2*k*p)*z*z+p)) == 0
assert sp.factor(z*z*s.subs(k,1)) == (z-1)*(2*z*z-p*z-p)
assert sp.simplify(sp.diff(s,z,2) - 6*p/z**4) == 0
print('Exact symbolic derivative, cubic, and convexity identities: PASS')


def optimal_time(a,c):
    assert a>0 and 0<c<=1
    pp=math.exp(-a)
    def S(t):
        zz=math.exp(-a*t)
        return pp/(zz*zz)-(2-pp)+2*c*c*(zz-pp)
    return brentq(S,1e-8,1-1e-8,xtol=1e-13)


def covariance(a,t):
    pp=math.exp(-a)
    zz=math.exp(-a*t)
    return (2-(2-pp)*zz-pp/zz)/a


def risk(a,c,t):
    pp=math.exp(-a)
    v=(2*a-3+4*pp-pp*pp)/(a*a)
    zz=math.exp(-a*t)
    if c==1 and t==0:
        return v
    return v - c*c*covariance(a,t)**2/(1-c*c*zz*zz)

for a,c in [(0.02,1),(.2,.7),(.75,.8),(1,1),(5,.2),(20,1)]:
    t=optimal_time(a,c)
    vals=np.array([risk(a,c,float(x)) for x in np.linspace(0,1,3001)])
    assert risk(a,c,t)<=np.min(vals)+1e-9
    assert 0<t<1
    print('Design grid',a,c,'optimal_time',format(t,'.12g'),'risk',format(risk(a,c,t),'.12g'))

for a in [.1,.7,2.3]:
    for t in [.2,.5,.85]:
        # Independently integrate the Markov covariance instead of evaluating d.
        val=quad(lambda s: math.exp(-a*abs(s-t))-math.exp(-a*(s+t)),
                 0,1,points=[t],epsabs=3e-12)[0]
        assert abs(val-covariance(a,t))<2e-12
print('Nine direct covariance integrations: PASS')

for a in [.1,1,5]:
    for c in [.2,.5,.8,1]:
        t=optimal_time(a,c)
        r=math.exp(-a*t)
        pp=math.exp(-a)
        if c==1:
            exact=(pp+math.sqrt(pp*pp+8*pp))/4
            assert abs(r-exact)<1e-10
        assert abs(pp/r**2-(2-pp)+2*c*c*(r-pp))<5e-12
    for c1,c2 in [(.1,.4),(.4,.8),(.8,1)]:
        assert optimal_time(a,c2)<optimal_time(a,c1)
print('Root formula and strict noise ordering: PASS')

for a in [1e-3,4e-4]:
    t=optimal_time(a,1)
    assert abs(t-2/3)<.001
    for c in [.4,.8]:
        t=optimal_time(a,c)
        assert abs(t-(1-a/(2*(1-c*c))))<.002
    for kk in [0,.5,2,10]:
        c=math.sqrt(1-kk*a)
        limit=(1-kk+math.sqrt(kk*kk+4*kk+1))/3
        assert abs(optimal_time(a,c)-limit)<.005
print('Rare-switching singular boundary-layer limits: PASS')

for c in [.2,.8,1]:
    a=25
    t=optimal_time(a,c)
    assert abs(a*(t-.5)-math.log(2)/2)<.0003
print('Fast-switching universal limit: PASS')

# Independent sample-path check, using uniform Poisson event times.
rng=np.random.default_rng(19337)
a=.75;c=.8;t=optimal_time(a,c)
n=60000
counts=rng.poisson(a/2,n)
J=np.ones(n);X=np.ones(n)
for i,num in enumerate(counts):
    if num==0:continue
    jumps=np.sort(rng.random(num))
    J[i]=np.dot(np.diff(np.r_[0,jumps,1]),(-1.)**np.arange(num+1))
    X[i]=(-1.)**np.searchsorted(jumps,t,side='right')
Y=X*np.where(rng.random(n)<(1-c)/2,-1,1)
assert abs(np.mean(J)-(1-math.exp(-a))/a)<.01
assert abs(np.cov(J,Y,bias=True)[0,1]-c*covariance(a,t))<.01
print('Independent Poisson-path mean and covariance simulation: PASS')
print('All checks passed')
