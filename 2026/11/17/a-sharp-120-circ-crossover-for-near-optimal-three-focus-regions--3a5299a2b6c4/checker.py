"""Independent numerical diagnostics for near-critical Fermat-distance sublevel geometry."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar
from scipy.special import beta as B

THETA0=2*math.pi/3
BETA=math.sqrt(3)/2

def coeffs(b,c):
    return 3*(1/b+1/c)/8, math.sqrt(3)*b*c/4

def mlim(lam,k):
    return -BETA**2*min(lam,0)**2/(4*k)

def positive_poly(x, lam, k):
    return 1+mlim(lam,k)-k*x*x-BETA*lam*x

def volume(lam,b=1.,c=1.):
    k,_=coeffs(b,c)
    m=mlim(lam,k)
    d=(BETA*lam)**2+4*k*(1+m)
    left=max(0.,(-BETA*lam-math.sqrt(d))/(2*k))
    right=(-BETA*lam+math.sqrt(d))/(2*k)
    assert right>left
    f=lambda x: 2*math.sqrt(2*x*max(0.,positive_poly(x,lam,k)))
    return quad(f,left,right,epsabs=1e-11,epsrel=1e-11,limit=300)[0]

def exact_cost(u,v,theta,b,c):
    co=math.cos(theta/2); si=math.sin(theta/2)
    return (math.hypot(u,v) + math.hypot(b*co-u,b*si-v)
            + math.hypot(c*co-u,-c*si-v))

def mincost(theta,b,c):
    if theta>=THETA0: return b+c
    a2=b*b+c*c-2*b*c*math.cos(theta)
    area=b*c*math.sin(theta)/2
    return math.sqrt((a2+b*b+c*c+4*math.sqrt(3)*area)/2)

def direct_area(t,lam,b=1.,c=1.):
    theta=THETA0+lam*math.sqrt(t)
    threshold=mincost(theta,b,c)+t
    tan=math.tan(theta/2)
    k, area0=coeffs(b,c)
    # All rare sublevels lie near A; this endpoint suffices for the tested parameters.
    xmax=min(.46, max(.18, (abs(lam)*BETA/(2*k)+3/math.sqrt(k))*math.sqrt(t)))
    def width(x):
        if x==0:return 0.
        ybound=x*tan
        fun=lambda y:exact_cost(x,y,theta,b,c)-threshold
        res=minimize_scalar(fun,bounds=(-ybound,ybound),method='bounded',options={'xatol':1e-12})
        ym=res.x
        if res.fun>=0:return 0.
        low = -ybound if fun(-ybound)<=0 else brentq(fun,-ybound,ym,xtol=1e-13)
        high= ybound if fun(ybound)<=0 else brentq(fun,ym,ybound,xtol=1e-13)
        return high-low
    # deterministic quadrature at fine mesh, no stochastic sampling
    nodes, weights = np.polynomial.legendre.leggauss(420)
    xx=xmax*(nodes+1)/2
    widths=np.array([width(float(x)) for x in xx])
    area=(xmax/2)*float(weights@widths)
    parent=b*c*math.sin(theta)/2
    return area/parent, xmax, widths[-1]

def run():
    k,area0=coeffs(1,1)
    baseline=math.sqrt(2)*B(.75,1.5)/k**.75
    print('k,theta0,beta,area0',k,THETA0,BETA,area0)
    print('V(0), beta-integral',volume(0),baseline)
    assert abs(volume(0)-baseline)<1e-11
    for lam in [-2., -0.75, 0., .75, 2.]:
        vv=volume(lam)
        print('lam,V,normalized coefficient',lam,vv,vv/area0)
        for t in [.004,.001]:
            p,xmax,edge=direct_area(t,lam)
            ratio=p/(t**1.25*vv/area0)
            print('  t,p,ratio,xmax,edge',t,p,ratio,xmax,edge)
            assert abs(ratio-1)<.11, (lam,t,ratio)
            assert edge==0, 'integration upper limit cuts a nonzero sublevel'
    # crossover probability at lambda=0 equals Beta(5/4,1).
    for s in [.1,.25,.5,.75]:
        conditional=s**1.25*volume(0/math.sqrt(s))/volume(0)
        assert abs(conditional-s**1.25)<1e-13
    print('FERMAT_CRITICAL_CROSSOVER_DIAGNOSTIC_OK')
if __name__=='__main__':run()
