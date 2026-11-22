"""Independent quadrature / exact endpoint checks for a Rayleigh Stein statistic.
The analytic all-sample theorem is established in RESULT.md, not by finite checks.
"""
import math
import numpy as np
from scipy.integrate import quad

def g(y,t):
    return t*(y-1/y) if t<y else y*y-2

def phi2_n2(t):
    q=min(t*t/4,1)
    points=sorted(set([0.,min(q,1.),max(0.,1-q),1.]))
    def f(u):
        u=min(max(u,1e-300),1-1e-15)
        y1=2*math.sqrt(u); y2=2*math.sqrt(1-u)
        return ((g(y1,t)+g(y2,t))/2)**2
    return sum(quad(f,lo,hi,epsabs=1e-11,epsrel=1e-10,limit=150)[0]
               for lo,hi in zip(points[:-1],points[1:]) if hi>lo)

def mean_r_n2(a):
    # s=a*t; R=2/a int E[phi^2(s/a)]e^-s ds
    return (2/a)*quad(lambda s:math.exp(-s)*phi2_n2(s/a),0,42,
                       epsabs=1e-15,epsrel=1e-8,limit=250)[0]

if __name__=='__main__':
    checks=0
    for t in [0.08,0.03,0.01,0.003,0.001]:
        val=phi2_n2(t)
        ratio=val/(t*t*math.log(1/t))
        print('small-t',t,'Ephi2',format(val,'.12g'),'normalized',format(ratio,'.8f'),'theory 0.25')
        assert 0.25<ratio<0.56
        checks+=1
    for a in [30,80,200,500]:
        val=mean_r_n2(a)
        ratio=a**3*val/math.log(a)
        print('bandwidth',a,'mean',format(val,'.12g'),'normalized',format(ratio,'.8f'),'theory 1')
        assert 0.9<ratio<1.8
        checks+=1
    # Verify pointwise limit for deterministic Y_i=sqrt(4u_i)
    us=[0.02,0.21,0.4,0.89]
    from scipy.integrate import quad
    for u in us:
        ys=[2*math.sqrt(u),2*math.sqrt(1-u)]
        z=sum(y-1/y for y in ys)**2
        for a in [50,150,600]:
            r=2*quad(lambda t: (sum(g(y,t) for y in ys)/2)**2*math.exp(-a*t),0,max(ys),
                     points=ys,epsabs=1e-14,epsrel=1e-11,limit=100)[0]
            assert 0.0<r*a**3<=z*1.3
            if a==600: assert abs(r*a**3/z-1)<.1
            checks+=1
    # Exact n=2 null tail from the uniform Dirichlet coordinate U.
    from scipy.optimize import brentq
    for z in (100.,1000.,10000.,1000000.):
        def s2(u):
            y1,y2=2*math.sqrt(u),2*math.sqrt(1-u)
            return y1-1/y1+y2-1/y2
        root=brentq(lambda u:s2(u)+math.sqrt(z),1e-14,.1,xtol=1e-15)
        tail=2*root # two symmetric endpoint intervals
        print('tail',z,'z * Pr(Z>z)',format(z*tail,'.9f'),'theory 0.5')
        assert 0.35<z*tail<.501
        checks+=1
    print('PASS',checks,'numerical checks')
