#!/usr/bin/env python3
"""Reproduce finite-generator identities and numeric regimes in a two-reserve model.

Run with Python 3.9+ and SymPy (tested with SymPy 1.13+).
The analytic inequalities in RESULT.md, rather than finite sweeps, establish
universality of the ordering theorem.
"""
import math
from fractions import Fraction as F
from random import Random
import sympy as sp

checks = 0

def check(cond, context=''):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(context)

e,c,z = sp.symbols('e c z', positive=True)
a,b,d = sp.symbols('a b d', positive=True)
N = c + 3*e + z
D = 2*e**2+z*N
T = N / D
G = sp.Matrix([[-2*e-z, 2*e],[c,-e-c-z]])
M = -G.inv()*sp.ones(2,1)
check(sp.factor(M[0]-T)==0,'mean from inverse generator')
check(sp.factor(sp.diff(T,c)-2*e**2/D**2)==0,'partial c')
check(sp.factor(sp.diff(T,z)-(2*e**2-N**2)/D**2)==0,'partial z')
check(sp.factor(G.det()-D)==0,'determinant')
check(sp.factor(-G.trace()-(3*e+c+2*z))==0,'trace')
Delta = sp.sqrt((c+3*e)**2-8*e**2)
lam0 = (c+3*e-Delta)/2
check(sp.simplify(lam0**2-(c+3*e)*lam0+2*e**2)==0,'eigenvalue characteristic')
check(sp.simplify(sp.diff(lam0,c)+lam0/Delta)==0,'eigenvalue derivative')

# Exact rational finite-state backward equations for every sample.
for ei in range(1,5):
  for ci in range(1,7):
    for zi in range(1,7):
      ee,cc,zz = F(ei,3), F(ci,4), F(zi,5)
      t2=(cc+3*ee+zz)/(2*ee*ee+zz*(cc+3*ee+zz))
      t1=(1+cc*t2)/(ee+cc+zz)
      check((2*ee+zz)*t2 == 1+2*ee*t1, 'backward equation 2')
      check((ee+cc+zz)*t1 == 1+cc*t2, 'backward equation 1')

def fvals(ee,cc0,zz0,aa,bb,x):
    cc=cc0*math.exp(-aa*x)
    zz=zz0*math.exp(-bb*x)
    th=cc+3*ee
    De=math.sqrt(th*th-8*ee*ee)
    l0=4*ee*ee/(th+De)  # stable rationalization
    nn=th+zz
    den=2*ee*ee+zz*nn
    mt=nn/den
    rh=zz+l0
    mder=(bb*zz*(nn*nn-2*ee*ee)-2*aa*ee*ee*cc)/(den*den)
    rder=-bb*zz+aa*cc*l0/De
    return mt,rh,mder,rder

def root(f):
    lo,hi=0.,1.
    while f(hi)>0 and hi<300:
        hi*=2.
    # only used when f starts positive and eventually negative
    check(f(lo)>0 and f(hi)<0,'root brackets')
    for _ in range(85):
       mid=(lo+hi)/2
       if f(mid)>0:lo=mid
       else:hi=mid
    return (lo+hi)/2

def optima(ee,cc0,zz0,aa,bb):
    m0,t0,md0,td0=fvals(ee,cc0,zz0,aa,bb,0.)
    dm=0 if md0<=0 else root(lambda x:fvals(ee,cc0,zz0,aa,bb,x)[2])
    dt=0 if td0>=0 else root(lambda x:-fvals(ee,cc0,zz0,aa,bb,x)[3])
    return dm,dt

examples = [(1.,1.,.03,1.,2.),(1.,1.,.08,1.,2.),(1.,1.,.3,1.,2.)]
for pars in examples:
    dm,dt=optima(*pars)
    check(dm+1e-9>=dt,'objective order')
    print('parameters',pars,'d_tail',format(dt,'.12f'),'d_mean',format(dm,'.12f'))
check(optima(*examples[0])==(0,0),'both adjacent')
check(optima(*examples[1])[1]==0 and optima(*examples[1])[0]>0,'mean only interior')
check(optima(*examples[2])[1]>0 and optima(*examples[2])[0]>optima(*examples[2])[1],'two interior')

rng=Random(1916723)
for k in range(350):
    ee=math.exp(rng.uniform(-1.5,1.5))
    cc0=math.exp(rng.uniform(-1.5,2.0))
    aa=math.exp(rng.uniform(-1.,.5))
    bb=aa*(1.05+rng.uniform(0,2.5))
    zz0=math.exp(rng.uniform(-3.5,1.))
    dm,dt=optima(ee,cc0,zz0,aa,bb)
    check(dm>=dt-1e-7,'random optimizer order')
    # Check predicted derivatives against two-sided finite differences away from boundaries.
    x=rng.uniform(.1,2.)
    mean,tail,md,td=fvals(ee,cc0,zz0,aa,bb,x)
    hh=1e-5
    pm,pt,_,_=fvals(ee,cc0,zz0,aa,bb,x+hh)
    nm,nt,_,_=fvals(ee,cc0,zz0,aa,bb,x-hh)
    check(abs(md-(pm-nm)/(2*hh))<2e-6*(1+abs(md)),'mean finite difference')
    check(abs(td-(pt-nt)/(2*hh))<2e-6*(1+abs(td)),'tail finite difference')
    # For the calculated optima, neighboring sampling cannot improve the objective.
    if dm>1e-7:
       check(fvals(ee,cc0,zz0,aa,bb,dm)[0]>= fvals(ee,cc0,zz0,aa,bb,dm+.001)[0]-1e-7,'mean optimizer sample')
    if dt>1e-7:
       check(fvals(ee,cc0,zz0,aa,bb,dt)[1]<= fvals(ee,cc0,zz0,aa,bb,dt+.001)[1]+1e-7,'tail optimizer sample')
print('PASS',checks,'assertions')
