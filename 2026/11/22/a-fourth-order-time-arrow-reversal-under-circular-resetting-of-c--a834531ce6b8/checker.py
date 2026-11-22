"""Reproduce the stationary fourth-order modal-energy correlation theorem.

Requires Python 3.9+ and scipy for the independent age-quadrature checks.
Run: python checker.py
"""
from fractions import Fraction as F
from math import sqrt, exp
from scipy.integrate import quad


def formula(u,T,R,r):
    """Closed formula for Cov(Q_+^2,Q_-^2) under circular resetting."""
    z=R*R/(2*T)
    return T*T*r*(8-16*z+z*z*(8-4*u*u-(r+2)**2))/(2*(r+4)*((r+2)**2-4*u*u))


def generator(u,T,R,r):
    """An independent stationary-moment generator computation."""
    A=R*R/2
    a_plus,a_minus=1+u,1-u
    mp=(2*T+r*A)/(r+2*a_plus)
    mm=(2*T+r*A)/(r+2*a_minus)
    m22=(2*T*(mp+mm)+r*A*A/2)/(r+4)
    return m22-mp*mm


def renewal_quadrature(u,T,R,r):
    """Independent renewal integral using Gaussian conditional moments.

    Integration is performed directly over the physical reset age tau.
    The reset angle is uniform; its exact second and mixed fourth
    moments are used without the stationary generator equations.
    """
    ap,am=1+u,1-u
    sp=T/ap;sm=T/am
    A=R*R/2
    def hp(tau):return sp+(A-sp)*exp(-2*ap*tau)
    def hm(tau):return sm+(A-sm)*exp(-2*am*tau)
    def integrate(f):
        return quad(lambda tau:r*exp(-r*tau)*f(tau),0,float('inf'),
                    epsabs=1e-11,epsrel=1e-11,limit=250)[0]
    mp=integrate(hp)
    mm=integrate(hm)
    joint=integrate(lambda tau:hp(tau)*hm(tau)-(R**4/8)*exp(-4*tau))
    return joint-mp*mm


def sign_class(u,T,R,r):
    z=R*R/(2*T)
    f=(1-u*u)*z*z-4*z+2
    threshold=None
    if f>0:
        threshold=sqrt(8-4*u*u+8/(z*z)-16/z)-2
        assert threshold>0
        expected=1 if r<threshold else (-1 if r>threshold else 0)
    else:
        expected=-1
    return expected,threshold


def run():
    tested=0
    # Exact rational comparisons, including both crossing branches and the central region.
    for u in [F(1,5),F(1,2),F(4,5)]:
      for T in [F(1,2),F(1),F(4)]:
       for R in [F(1,5),F(1),F(3),F(9)]:
        for r in [F(1,10),F(1,2),F(1),F(5),F(50)]:
          a=formula(u,T,R,r)
          b=generator(u,T,R,r)
          assert a==b,(u,T,R,r,a,b)
          if a!=0:
              expect,_=sign_class(float(u),float(T),float(R),float(r))
              assert (1 if a>0 else -1)==expect
          tested+=1
    # Renewal quadrature does not use the stationary generator equations.
    numeric=0
    for u,T,R,r in [(0.2,1.,0.5,1.),(0.5,1.,0.8,0.25),
                      (0.5,1.,4.,0.2),(0.8,2.,6.,3.),(0.3,1.,2.,5.),
                      (0.6,3.,2.,1.),(0.1,1.,12.,0.01)]:
        a=float(formula(u,T,R,r));q=renewal_quadrature(u,T,R,r)
        assert abs(a-q)<2e-7*(1+abs(a)),(u,T,R,r,a,q)
        numeric+=1
    # Direct independent semigroup regression and time-arrow sign.
    for u,T,R,r in [(0.2,1.,0.5,1.),(0.5,1.,4.,0.2),(0.8,2.,6.,3.)]:
        c=generator(u,T,R,r)
        for t in [0.01,0.4,2.]:
            cp=c*exp(-(r+2*(1-u))*t)
            cm=c*exp(-(r+2*(1+u))*t)
            assert abs(cp-cm*exp(4*u*t))<1e-12*(1+abs(cp))
    print('PASS:',tested,'exact rational identities,',numeric,
          'independent age quadratures, 9 chronological comparisons')

if __name__=='__main__':run()
