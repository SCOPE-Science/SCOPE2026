"""Reproducibility checks for a two-season recovery-hazard theorem.

Only numerical/symbolic spot checks are performed; the universal inequality is
proved analytically in RESULT.md rather than by finite enumeration.
"""
import math
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def q(a, b, h):
    return (-math.expm1(-a*h))*(-math.expm1(-b*h))/(-math.expm1(-(a+b)*h))


def a_mean(a, b, h):
    if a==b:
        return 1/a
    return .5*(1/a+1/b)-.5*(1/a-1/b)**2 *q(a,b,h)/h


def boundaries(a,b,h):
    u,v=math.exp(-a*h),math.exp(-b*h)
    x0=(1/b*(1-v)+v/a*(1-u))/(1-u*v)
    x1=1/a+(x0-1/a)*u
    return x0,x1


def solve_mean(a,b,h):
    x0,_=boundaries(a,b,h)
    def one(x,c,t):
        return 1/c + (x-1/c)*math.exp(-c*t)
    # Solve the differential equation separately over each season.
    s1=solve_ivp(lambda t,y:[1-a*y[0]],(0,h),[x0],rtol=1e-11,atol=1e-12,dense_output=True)
    s2=solve_ivp(lambda t,y:[1-b*y[0]],(h,2*h),[s1.y[0,-1]],rtol=1e-11,atol=1e-12,dense_output=True)
    t1=np.linspace(0,h,20001)
    t2=np.linspace(h,2*h,20001)
    mean=(np.trapezoid(s1.sol(t1)[0],t1)+np.trapezoid(s2.sol(t2)[0],t2))/(2*h)
    assert abs(s2.y[0,-1]-x0) < 1e-9
    return mean


def run():
    a,b,h=sp.symbols('a b h',positive=True)
    u=sp.symbols('u',positive=True)
    v=sp.symbols('v',positive=True)
    x0=(1/b*(1-v)+v/a*(1-u))/(1-u*v)
    x1=1/a+(x0-1/a)*u
    integ=h*(1/a+1/b)+(x0-1/a)*(1-u)/a+(x1-1/b)*(1-v)/b
    target=h*(1/a+1/b)-(1/a-1/b)**2*(1-u)*(1-v)/(1-u*v)
    assert sp.simplify(integ-target)==0
    assert sp.simplify(x1-(1/b+(x0-1/b)/v))==0
    print('PASS: exact periodicity and mean identity (symbolic)')
    for aa,bb,hh in [(1,4,0.13),(1,4,1.9190666745214588),(1,4,6),(2.2,0.6,0.8),(0.4,5,1.7),(3,3,1)]:
        formula=a_mean(aa,bb,hh)
        ode=solve_mean(aa,bb,hh)
        assert abs(formula-ode)<1e-8,(aa,bb,hh,formula,ode)
        assert min(1/aa,1/bb)-1e-9 <=formula <= max(1/aa,1/bb)+1e-9
    print('PASS: separate high-accuracy ODE and quadrature comparisons')
    for aa,bb in [(1,4),(0.6,2.2),(2,3),(11,0.2)]:
        hs=np.geomspace(1e-4,1e2,250)
        vals=np.array([a_mean(aa,bb,float(t)) for t in hs])
        assert min(np.diff(vals))>0,(aa,bb,min(np.diff(vals)))
        m0=2/(aa+bb)
        ml=.5*(1/aa+1/bb)
        assert abs(a_mean(aa,bb,1e-4)-m0)<1e-6
        assert abs(a_mean(aa,bb,1000)-ml)<.02
    print('PASS: monotone crossover and analytic end limits (numeric checks)')
    aa,bb,transmission=1,4,2
    hstar=brentq(lambda t: transmission*a_mean(aa,bb,t)-1,.01,10,xtol=1e-14)
    assert abs(hstar-1.91906667452146)<1e-11
    assert transmission*a_mean(aa,bb,1)<1<transmission*a_mean(aa,bb,3)
    assert transmission-(aa+bb)/2 == -.5
    print('PASS: unique crossing example: h*={:.14f}; Floquet growth = -0.5'.format(hstar))
    # Algebraic small-h coefficient; check Taylor limit at high precision via mpmath.
    import mpmath as mp
    mp.mp.dps=55
    am=mp.mpf(1);bm=mp.mpf(4)
    for hs in ['1e-3','1e-4','1e-5']:
        hh=mp.mpf(hs)
        qq=mp.expm1(-am*hh)*mp.expm1(-bm*hh)/(-mp.expm1(-(am+bm)*hh))
        # two negative factors in numerator, -expm1 in denominator
        mm=(1/am+1/bm)/2-(1/am-1/bm)**2*qq/(2*hh)
        coef=(mm-2/(am+bm))/(hh**2)
        predicted=(am-bm)**2/(24*(am+bm))
        assert abs(coef-predicted)<1e-6
    print('PASS: high-precision fast-switching second-order coefficient')
    print('All reproducibility checks completed.')

if __name__=='__main__':
    run()
