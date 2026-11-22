"""Independent numerical diagnostics for the thin spatial-tube Crofton theorem.
Usage: python verify_line_tubes.py (requires NumPy and SciPy)."""
import numpy as np
from math import pi
from scipy.integrate import quad
from scipy.special import ellipe

def verify_ellipses():
    for a,b in [(1.,1.),(2.,1.),(3.,0.7)]:
        def bphi(phi): return np.hypot(a*np.sin(phi),b*np.cos(phi))
        j=quad(lambda phi: pi*bphi(phi)**2/(a*b),0,pi,epsabs=1e-12)[0]/pi
        expected=pi*(a*a+b*b)/(2*a*b)
        assert abs(j-expected)<1.e-11,(a,b,j,expected)
        integral=quad(lambda phi: 2*bphi(phi)**2/(pi*(a*a+b*b)),0,pi,epsabs=1e-12)[0]
        assert abs(integral-1)<1e-12
        print('ellipse',a,b,'reciprocal-chord functional',j,'azimuth normalization',integral)

def verify_circle_lines():
    # Uniform (mu,phi) directional law and rectangular orthogonal offsets.
    rng=np.random.default_rng(20261120)
    for r in (.2,.5):
        n=80000
        mu=rng.uniform(0,1,n)
        s=rng.uniform(-1,1,n)*(mu+r)
        t=rng.uniform(-1,1,n)*(1+r)
        weight=4*(mu+r)*(1+r)
        aa=s*s+t*t+1-r*r
        bcoef=2*aa-4*(1-mu*mu)
        ccoef=-8*mu*s*np.sqrt(1-mu*mu)
        dcoef=aa*aa-4*(mu*mu*s*s+t*t)
        counts=np.empty(n,dtype=np.int8)
        for k in range(n):
            roots=np.roots([1,0,bcoef[k],ccoef[k],dcoef[k]])
            counts[k]=np.sum(np.abs(roots.imag)<1.e-6)//2
        denominator=np.mean(weight*(counts>0))
        numerator=np.mean(weight*(counts>1))
        estimate=numerator/denominator
        benchmark={.2:.0414384,.5:.0647318}[r]
        assert abs(estimate-benchmark)<.006,(r,estimate,benchmark)
        print('circle',r,'Monte Carlo double-hit ratio',estimate,'independent quadrature',benchmark)
    print('small-radius circle coefficient',1/pi)

if __name__=='__main__':
    verify_ellipses()
    verify_circle_lines()
    print('all numerical diagnostics passed')
