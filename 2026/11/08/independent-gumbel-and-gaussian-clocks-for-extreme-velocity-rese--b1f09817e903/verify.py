#!/usr/bin/env python3
"""Reproduce algebraic and quadrature checks for the velocity-reset cycle theorem.

The rigorous limit arguments are in RESULT.md; the finite checks are diagnostics only.
"""
import math
import sympy as s
from scipy.integrate import quad
from scipy.special import erfc, ndtr

checks = 0

def require(condition, explanation):
    global checks
    if not condition:
        raise AssertionError(explanation)
    checks += 1

r, D, x, ell = s.symbols('r D x ell', positive=True)
k = (s.Rational(9,4)/(D*r))**s.Rational(1,4)
c = s.Rational(4,3)*r*k
lx = k*s.sqrt(x)
f = r*ell + 3*x**2/(4*D*ell**3)
require(s.simplify(s.diff(f,ell).subs(ell,lx))==0,'saddle derivative')
require(s.simplify(s.diff(f,ell,2).subs(ell,lx)-4*r/lx)==0,'saddle curvature')
require(s.simplify(f.subs(ell,lx)-c*s.sqrt(x))==0,'saddle rate')
pref = r * s.sqrt(4*D/(3*s.pi))*lx**s.Rational(3,2)/x * s.sqrt(2*s.pi*lx/(4*r))
require(s.simplify(pref-s.sqrt(s.Rational(3,2)))==0,'tail constant')
require(s.simplify(k/c-3/(4*r))==0,'record length center')
require(s.simplify(s.sqrt(lx/(4*r)).subs(x, (s.symbols('b',positive=True)/c)**2)-s.sqrt(3*s.symbols('b',positive=True))/(4*r))==0, 'mark variance scale')


def tail_and_conditional(xval, rval=1., dval=1., z=None):
    lopt = (9*xval*xval/(4*dval*rval))**0.25
    width = math.sqrt(lopt/(4*rval))
    def integrand(length):
        if length <= 0: return 0.
        return rval * math.exp(-rval*length)*erfc(xval/math.sqrt(4*dval*length**3/3))
    total = quad(integrand,0,float('inf'),epsabs=1e-150,epsrel=1e-11,limit=300)[0]
    if z is None:
        return total
    border = lopt+z*width
    joint = quad(integrand,0,max(0,border),epsabs=1e-150,epsrel=1e-11,limit=300)[0]
    return total, joint / total

for rval,dval in ((1.,1.),(2.,3.),(0.8,2.4)):
    kv=(9/(4*dval*rval))**.25
    cv=4*rval*kv/3
    for xv in (40.,100.,300.,1000.):
        tv=tail_and_conditional(xv,rval,dval)
        a=math.sqrt(1.5)*math.exp(-cv*math.sqrt(xv))
        require(abs(tv/a-1)<.04, f'tail asymptotic at {rval,dval,xv}: {tv/a}')
for xv in (2000.,4000.,8000.):
    for z in (-1.,0.,1.):
        _,p=tail_and_conditional(xv,1,1,z)
        require(abs(p-ndtr(z))<.09, f'conditional Gaussian at {xv},{z}: {p}')

for nv in (1000,10000,100000):
    rv,dv=1.,1.
    cv=4*rv/3*(9/(4*dv*rv))**.25
    bv=math.log(math.sqrt(1.5)*nv)
    for y in (-1.,0.,1.):
        xv=((bv+y)/cv)**2
        p=tail_and_conditional(xv,rv,dv)
        require(abs(nv*p-math.exp(-y))/math.exp(-y)<.06, f'Gumbel threshold at n={nv},y={y}')

print('PASS', checks,'symbolic and numerical assertions')
