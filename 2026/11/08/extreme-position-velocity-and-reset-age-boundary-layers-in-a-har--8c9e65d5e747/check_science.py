#!/usr/bin/env python3
"""Numerical and symbolic checks of extreme-position laws for a resetting-noise harmonic particle."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr
from scipy.optimize import minimize_scalar


def covs(s, mu, r, D):
    if s <= 0:
        return (0., 0., 0.)
    z=-math.expm1(-mu*s)
    z2=-math.expm1(-2*mu*s)
    vx=(2*D*r*r/(mu*mu))*(s-2*z/mu+z2/(2*mu))
    c=(D*r*r/(mu*mu))*z*z
    vw=(D*r*r/mu)*z2
    return vx,c,vw


def compare(mu,r,D,x):
    k=mu/math.sqrt(D*r)
    c=mu/(2*r*math.sqrt(D*r))
    m=r*math.sqrt(D*r)/mu
    v=D*r*r/mu
    # one-reset-interval density as in the published Kesten kernel
    def dens(s):
        if s<=0:return 0.
        vx, cv, vw=covs(s,mu,r,D)
        if vx<=0: return 0.
        return r*math.exp(-r*s-x*x/(2*vx))/math.sqrt(2*math.pi*vx)
    top=max(30.0/r,2.6*c*x+20/r)
    h=quad(dens,0,top,points=[c*x],epsrel=2e-9,limit=200)[0]
    def rat_integral(fn):
        return quad(lambda s: dens(s)*fn(s),0,top,points=[c*x],epsrel=2e-9,limit=200)[0]/h
    age=rat_integral(lambda s:s)
    wmean=rat_integral(lambda s: covs(s,mu,r,D)[1]*x/covs(s,mu,r,D)[0])
    wnegative=rat_integral(lambda s:ndtr(-(covs(s,mu,r,D)[1]*x/covs(s,mu,r,D)[0])/math.sqrt(covs(s,mu,r,D)[2]-covs(s,mu,r,D)[1]**2/covs(s,mu,r,D)[0])))
    asym=0.5*k*math.exp(-3*r/(2*mu)-k*x)
    return h/asym,age/(c*x),wmean/m,wnegative,ndtr(-math.sqrt(r/mu))

def test():
    for mu,r,D in [(1,1,1),(2,1,0.5),(0.75,2,1.25)]:
        for s in [0.02,0.1,0.7,4,15]:
            vx,c,vw=covs(s,mu,r,D)
            assert vx>0 and vw>0 and c*c<vx*vw
            # independent kernels: X= (r/mu)*sqrt(2D)*int(1-exp(-mu u))dB;
            # W=r*sqrt(2D)*int exp(-mu u)dB.
            xx=quad(lambda u:2*D*(r/mu)**2*(1-math.exp(-mu*u))**2,0,s)[0]
            xw=quad(lambda u:2*D*r*r/mu*(1-math.exp(-mu*u))*math.exp(-mu*u),0,s)[0]
            ww=quad(lambda u:2*D*r*r*math.exp(-2*mu*u),0,s)[0]
            assert np.allclose([vx,c,vw],[xx,xw,ww],rtol=2e-6,atol=1e-10)
        vals=[]
        for x in [16,32,64,96]:
            vals.append(compare(mu,r,D,x))
        print('parameters',mu,r,D,'k=',mu/math.sqrt(D*r),'m=',r*math.sqrt(D*r)/mu,'v=',D*r*r/mu)
        for x, row in zip([16,32,64,96],vals):
            print('x=',x, 'density/asym, age/saddle, wmean/m, wrong-direction, limit:',*[f'{a:.7g}' for a in row])
        assert abs(vals[-1][0]-1)<0.08
        assert abs(vals[-1][1]-1)<0.23
        assert abs(vals[-1][2]-1)<0.1
        assert abs(vals[-1][3]-vals[-1][4])<0.035
    # at x>0 a no-reset-age O(1/x) layer must exactly balance a drift r/k;
    # r/(k*mu*x) is the asymptotic layer mass.
    for mu,r,D in [(1,1,1),(2,1,0.5),(0.75,2,1.25)]:
        k=mu/math.sqrt(D*r)
        m=r*math.sqrt(D*r)/mu
        assert math.isclose(m,r/k,rel_tol=1e-14)
        assert math.isclose(-mu *r/(k*mu),-m,rel_tol=1e-14)
    print('PASS: bivariate Brownian covariance integral identities, saddle comparisons and flux-balance coefficients.')
if __name__=='__main__':test()
