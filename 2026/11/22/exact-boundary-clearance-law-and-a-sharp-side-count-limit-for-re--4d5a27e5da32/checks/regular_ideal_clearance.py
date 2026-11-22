"""Independent numerical checks for the regular ideal-polygon clearance formula.

Requires Python 3, SciPy and NumPy. All tests are deterministic.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq

PI=math.pi

def inradius(n):
    return math.asinh(1/math.tan(PI/n))

def cdf(n,t):
    if t<=0: return 0.0
    if t>=inradius(n): return 1.0
    a=PI/n
    return 2*n/((n-2)*PI)*(math.atan(math.sinh(t))+
       math.sinh(t)*(math.log(math.cos(a))+log_coth(t)))

def density(n,t):
    if t<=0 or t>=inradius(n): return 0.0
    return 2*n/((n-2)*PI)*math.cosh(t)*(math.log(math.cos(PI/n))+log_coth(t))

def log_coth(t):
    return math.log1p(2/math.expm1(2*t))

def limiting_cdf(t):
    if t<=0: return 0.0
    return 2/PI*(math.atan(math.sinh(t))+
                math.sinh(t)*log_coth(t))

def limiting_density(t):
    if t<=0: return 0.0
    return 2/PI*math.cosh(t)*log_coth(t)

def tv_closed(n):
    return 4/(PI*(n-2))*math.asin(math.cos(PI/n)**(n/2))

def radial_area(n,t):
    """Integrate hyperbolic polar area, independently of the Fermi boundary formula."""
    a=PI/n; A=1/math.tan(a); C=1/math.sin(a); k=math.sinh(t)
    def integrand(ang):
        B=C*math.cos(ang)
        disc=max(0.0,k*k+B*B-A*A)
        R=math.log((A+B)/(k+math.sqrt(disc)))
        return math.cosh(R)-1
    return 2*n*quad(integrand,0,a,epsabs=4e-11,epsrel=4e-11,limit=200)[0]

def check():
    N=0
    for n in (3,4,5,6,8,12,25):
        rho=inradius(n)
        norm=quad(lambda t:density(n,t),0,rho,epsabs=5e-11,epsrel=5e-11)[0]
        assert abs(norm-1)<5e-10, (n,norm)
        N+=1
        for f in (0.07,0.2,0.49,0.76,0.93):
            t=f*rho
            polar=radial_area(n,t)/((n-2)*PI)
            assert abs(polar-(1-cdf(n,t)))<1e-9, (n,t,polar,1-cdf(n,t))
            N+=1
    for n in (3,4,8,25,80):
        t0=math.atanh(math.cos(PI/n)**(n/2))
        empirical=brentq(lambda t:density(n,t)-limiting_density(t), t0*.5, t0*1.3)
        assert abs(empirical-t0)<2e-7
        numtv=quad(lambda t:abs(density(n,t)-limiting_density(t)),0,inradius(n),points=[t0],epsabs=1e-9)[0]/2
        numtv+=(quad(limiting_density,inradius(n),18,epsabs=1e-10)[0]+(1-limiting_cdf(18)))/2
        assert abs(numtv-tv_closed(n))<2e-8,(n,numtv,tv_closed(n))
        N+=2
    for n in range(3,50):
        for t in (.01,.1,.2,.4,.6,.9,1.3,2):
            assert cdf(n,t)>=cdf(n+1,t)-1e-13,(n,t)
            assert cdf(n,t)>=limiting_cdf(t)-1e-13,(n,t)
            N+=2
    for n in (3,4,7,10):
        h=1e-4
        rho=inradius(n)
        approx=(1-cdf(n,rho-h))/(h*h)
        exact=n*math.tan(PI/n)/((n-2)*PI)
        assert abs(approx/exact-1)<2e-3,(n,approx,exact)
        N+=1
    for n in (10000,50000):
        err=abs(tv_closed(n)-(2/n-2*math.sqrt(2)/n**1.5))
        assert err<4/n**2,(n,err)
        N+=1
    print('ALL_CHECKS_PASSED',N)

if __name__=='__main__':
    check()
