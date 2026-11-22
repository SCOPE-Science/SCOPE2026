#!/usr/bin/env python3
"""Standalone numerical checks of the stated two-site resetting theorem.
Requires scipy>=1.11; run `python CHECK.py` in this directory.
"""
import math
from scipy import special, optimize, integrate

checks=0

def require(test, message):
    global checks
    checks += 1
    if not test: raise AssertionError(message)

def psi(alpha,x):
    return special.gamma(alpha)*math.exp(-x*x/4)*special.pbdv(-alpha,x)[0]

def H(alpha,x):
    return special.gamma(alpha)*math.exp(-x*x/4)*special.pbdv(1-alpha,x)[0]

def K(alpha,a):
    return alpha/(H(alpha,-a)+psi(alpha,-a)*H(alpha,a)/psi(alpha,a))

def f(alpha,a,p,x):
    q=1-p;c=K(alpha,a)
    if x < -a:return c*(p+q*psi(alpha,-a)/psi(alpha,a))*psi(alpha,-x)
    if x > a:return c*(q+p*psi(alpha,-a)/psi(alpha,a))*psi(alpha,x)
    return c*(p*psi(alpha,-x)+q*psi(alpha,x))

def fp(alpha,a,p,x):
    q=1-p;c=K(alpha,a)
    if x < -a:return c*(p+q*psi(alpha,-a)/psi(alpha,a))*H(alpha,-x)
    if x > a:return -c*(q+p*psi(alpha,-a)/psi(alpha,a))*H(alpha,x)
    return c*(p*H(alpha,-x)-q*H(alpha,x))

def pred(alpha,a,p):
    hneg,hpos=H(alpha,-a),H(alpha,a)
    if alpha==1:
        if p==.5:return 'plateau'
        return 'right' if p>.5 else 'left'
    if alpha>1:
        c=hneg/(hneg+hpos)
        return 'both' if 1-c<p<c else ('right' if p>=c else 'left')
    if hneg<=0:return 'interior'
    c=hneg/(hneg+hpos)
    return 'left' if p<=c else ('right' if p>=1-c else 'interior')

for alpha in [.25,.5,.9,1.,1.1,2.,4.]:
 for a in [.2,.5,1.,2.]:
  hn,hp=H(alpha,-a),H(alpha,a)
  require(hp>0,'H positive for positive arguments')
  if alpha>1: require(hn>hp,'supercritical H order')
  if alpha<1: require(hn<hp,'subcritical H order')
  for p in [.1,.35,.5,.65,.9]:
   # Independent source jump, using values from each side.
   for x,w in [(-a,1-p),(a,p)]:
    eps=2.e-7
    require(abs((fp(alpha,a,p,x+eps)-fp(alpha,a,p,x-eps))+alpha*w)<2.e-5,'source derivative jump')
   xs=[-a+2*a*j/16 for j in range(1,16)]
   ds=[fp(alpha,a,p,x) for x in xs]
   mode=pred(alpha,a,p)
   if mode=='both': require(fp(alpha,a,p,-a+1e-8)<0 and fp(alpha,a,p,a-1e-8)>0,'two peaks at sites')
   elif mode=='right':require(min(ds)>-1.e-11,'unique right mode')
   elif mode=='left':require(max(ds)<1.e-11,'unique left mode')
   elif mode=='interior':
    require(fp(alpha,a,p,-a+1e-8)>-1e-8 and fp(alpha,a,p,a-1e-8)<1e-8,'one interior mode')
   else:require(max(abs(d) for d in ds)<1.e-10,'flat plateau')
  # Stationary Fokker-Planck ODE off support, tested by finite differences.
  p=.37; x=a/3;step=1.e-3
  resid=(f(alpha,a,p,x+step)-2*f(alpha,a,p,x)+f(alpha,a,p,x-step))/step**2 + x*(f(alpha,a,p,x+step)-f(alpha,a,p,x-step))/(2*step)+(1-alpha)*f(alpha,a,p,x)
  require(abs(resid)<2.e-6,'stationary differential equation')
for alpha in [.25,.5,.9]:
 a=optimize.brentq(lambda z:H(alpha,-z),1.e-7,10,xtol=5.e-14)
 require(abs(H(alpha,-a))<1.e-9,'critical separation')
 require(H(alpha,-a*.99)>0 and H(alpha,-a*1.01)<0,'critical sign crossing')
 print('subcritical alpha',alpha,'unique separation',format(a,'.12g'))
for alpha,a,p in [(.5,1.,.2),(1.,1.2,.5),(2.,.8,.63)]:
 mass=integrate.quad(lambda x:f(alpha,a,p,x),-math.inf,-a,epsabs=1.e-10)[0]+integrate.quad(lambda x:f(alpha,a,p,x),-a,a,epsabs=1.e-10)[0]+integrate.quad(lambda x:f(alpha,a,p,x),a,math.inf,epsabs=1.e-10)[0]
 require(abs(mass-1)<1.e-8,'stationary normalization')
# Numerical check integral definition (independent of the special-function evaluation).
for alpha,z in [(.5,-1),(.75,.5),(1.,-1.3),(2.,.8),(4.,-.6)]:
 val=math.exp(-z*z/2)*integrate.quad(lambda t:t**(alpha-1)*math.exp(-t*t/2-z*t),0,math.inf,epsabs=1.e-11)[0]
 require(abs(val-psi(alpha,z))<5.e-9,'independent Green integral')
# Representative limiting sharp asymptotic at large separation.
for alpha in [1.5,2.0]:
 a=6.0;pcrit=H(alpha,-a)/(H(alpha,-a)+H(alpha,a))
 approx=1-special.gamma(alpha-1)/math.sqrt(2*math.pi)*a**(3-2*alpha)*math.exp(-a*a/2)
 require(abs(pcrit-approx)<2.e-8,'large-separation bias frontier')
print('PASS',checks,'deterministic checks')
