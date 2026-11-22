#!/usr/bin/env python3
"""Reproducibility checks for logistic Stein frequency-weight asymptotics."""
import numpy as np
from scipy.optimize import root
from scipy.integrate import quad
from numpy.polynomial.hermite import hermgauss
from scipy.stats import chi2
from math import pi,sqrt,exp

assertions=0
def check(cond,desc):
 global assertions
 assert bool(cond),desc
 assertions+=1

def g(x):return np.tanh(np.asarray(x)/2)
def h(x):return .5*np.asarray(x)**2*g(x)-np.asarray(x)
def logistic_density(x):return 1/(4*np.cosh(x/2)**2)

def ml_fit(x):
 m=x.mean(); s=x.std()
 def f(z):
  y=(x-z[0])/np.exp(z[1]);return [g(y).mean(),np.mean(y*g(y))-1]
 sol=root(f, [m,np.log(s*sqrt(3)/pi)],tol=1e-12)
 check(np.max(np.abs(f(sol.x)))<2e-10,'ML score equations')
 return (x-sol.x[0])/np.exp(sol.x[1])

def mo_fit(x):return (x-x.mean())/(x.std()*sqrt(3)/pi)

def T(x,a,nodes,weights):
 t=nodes/sqrt(a)
 K=((1j*t[:,None]-g(x)[None,:])*np.exp(1j*t[:,None]*x[None,:])).mean(axis=1)
 return len(x)/sqrt(a)*np.dot(weights,np.abs(K)**2)

Vmo=(pi*pi-9)/27
Vml=7*pi**4/180-(pi*pi-6)**2/108
check(Vmo>0 and Vml>0,'positive variances')

for fun,target in [
 (lambda x:g(x)**2,1/3),
 (lambda x:x*g(x),1),
 (lambda x:g(x)*(h(x)),(pi*pi-6)/18),
 (lambda x:h(x)**2,7*pi**4/180),
 (lambda x:(g(x)-x/3)**2,Vmo),
 (lambda x:(h(x)-(pi*pi-6)/6*g(x))**2,Vml),
]:
 val=quad(lambda t:fun(t)*logistic_density(t),-45,45,epsabs=2e-10,limit=300)[0]
 check(abs(val-target)<4e-8,f'integral expected {target}, saw {val}')

rng=np.random.default_rng(271828)
sample=rng.logistic(size=85)
ml=ml_fit(sample);mo=mo_fit(sample)
nodes,weights=hermgauss(100)
cm=np.mean(h(ml)); gm=np.mean(g(mo))
check(abs(cm)>1e-4 and abs(gm)>1e-4,'nondegenerate sample contrasts')
for a in [200.,600.,1800.]:
 tl=T(ml,a,nodes,weights)
 tm=T(mo,a,nodes,weights)
 lhs_l=tl*a**2.5
 rhs_l=len(ml)*3*sqrt(pi)/4*cm**2
 lhs_m=tm*a**.5
 rhs_m=len(mo)*sqrt(pi)*gm**2
 check(abs(lhs_l/rhs_l-1)<.16,'ML large-weight leading constant')
 check(abs(lhs_m/rhs_m-1)<.07,'MO large-weight leading constant')
 print('a',a,'ML normalized and target',lhs_l,rhs_l,'MO normalized and target',lhs_m,rhs_m)
print('V_MO',Vmo,'V_ML',Vml,'limit multipliers',sqrt(pi)*Vmo,3*sqrt(pi)/4*Vml)
print('Assertions passed',assertions)
