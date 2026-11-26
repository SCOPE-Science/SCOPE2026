#!/usr/bin/env python3
"""Independent algebraic, numerical, and conditional Monte Carlo checks of
Poisson resetting of squared-Brownian diffusivity without position resetting.
Run: python3 verify.py
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import erfcx

A, L, t = sp.symbols('A L t', positive=True)
z=A*t
V = 4*L**2*t/A
kappa4=480*L**4/A**4*(z-1+sp.exp(-z))
B = 8*L**4*t/A**2+40*L**4/A**3*(1-sp.exp(-z))
M4=3*V**2+kappa4
assert sp.simplify(sp.diff(V,t)-4*L**2/A)==0
assert sp.simplify(sp.diff(B,t)+A*B-48*L**4/A**2-2*L**2*V)==0
assert sp.simplify(sp.diff(M4,t)-12*B)==0
assert sp.simplify(kappa4/(3*V**2)-10*(z-1+sp.exp(-z))/z**2)==0

r, u, k = sp.symbols('r u k', real=True, positive=True)
ho = (sp.cosh(2*L*k*u))**sp.Rational(-1,2)*sp.exp(-k*r*r*sp.tanh(2*L*k*u)/(2*L))
pde = sp.diff(ho,u)-L**2*sp.diff(ho,r,2)+k**2*r*r*ho
assert sp.simplify(pde/ho)==0


def f(ka, tm, lam):
    return 1/math.sqrt(math.cosh(2*lam*abs(ka)*tm))

def g(ka, tm, alpha, lam):
    if ka==0 or tm==0: return 1.
    beta=abs(ka)/(2*lam)*math.tanh(2*lam*abs(ka)*tm)
    c=math.sqrt(alpha)/lam
    return f(ka,tm,lam)*c*math.sqrt(math.pi)/(2*math.sqrt(beta))*erfcx(c/(2*math.sqrt(beta)))

def FT(ka, s, alpha, lam):
    ff=quad(lambda x: math.exp(-(s+alpha)*x)*f(ka,x,lam),0,60,epsabs=1e-11)[0]
    gg=quad(lambda x: math.exp(-(s+alpha)*x)*g(ka,x,alpha,lam),0,60,epsabs=1e-11)[0]
    return gg/(1-alpha*ff)

for alpha,lam,kk,ss in [(1.3,0.7,0.5,1.1),(.7,1.1,1.,1.7),(2.,.3,.9,.8)]:
    assert abs(FT(0.,ss,alpha,lam)-1/ss)<1e-10
    # time-domain first-reset renewal convolution, trapezoidal quadrature.
    dt=.01; N=1600; times=np.arange(N+1)*dt
    fgrid=np.array([f(kk,v,lam) for v in times])
    ggrid=np.array([g(kk,v,alpha,lam) for v in times])
    ef=alpha*np.exp(-alpha*times)*fgrid
    eg=alpha*np.exp(-alpha*times)*ggrid
    pf=np.zeros(N+1);pg=np.zeros(N+1);pf[0]=pg[0]=1
    for j in range(1,N+1):
        # trapezoidal quadrature: includes term at u=0 dependent on current value.
        pf[j]=(math.exp(-alpha*times[j])*fgrid[j]+dt*(np.dot(ef[1:j],pf[j-1:0:-1])+0.5*ef[j]))/(1-0.5*dt*ef[0])
        pg[j]=math.exp(-alpha*times[j])*ggrid[j]+dt*(0.5*eg[0]*pf[j]+np.dot(eg[1:j],pf[j-1:0:-1])+0.5*eg[j])
    integrate=np.trapezoid(np.exp(-ss*times)*pg,times)
    assert abs(integrate-FT(kk,ss,alpha,lam))<0.0015,(integrate,FT(kk,ss,alpha,lam))

# Different numerical check: stationary diffusivity is a Gaussian mixed over exponential age;
# use a direct conditional Gaussian simulation of the stochastic integral.
alpha,lam,k0=1.3,.7,.6
rng=np.random.default_rng(831726)
ns=30000; dt=.004; T=2.0; steps=round(T/dt)
ages=rng.exponential(1/alpha,size=ns)
w0=rng.normal(size=ns)*np.sqrt(2*lam**2*ages)
w=w0.copy();v=np.zeros(ns)
for j in range(steps):
    v+=2*w**2*dt
    w+=math.sqrt(2*lam**2*dt)*rng.normal(size=ns)
    w[rng.random(ns)<alpha*dt]=0.
mc=np.exp(-k0**2*v/2).mean() # E(e^{ikX}|w)=exp(-k² V/2)
# Difference in units: expected characteristic from F-K uses k² * integral ω².
# Note V=2 int ω², so exponent indeed -k²V/2.
fgrid=np.array([f(k0,j*dt,lam) for j in range(steps+1)])
ggrid=np.array([g(k0,j*dt,alpha,lam) for j in range(steps+1)])
ef=alpha*np.exp(-alpha*dt*np.arange(steps+1))*fgrid
eg=alpha*np.exp(-alpha*dt*np.arange(steps+1))*ggrid
pf=np.zeros(steps+1);pg=np.zeros(steps+1);pf[0]=pg[0]=1
for j in range(1,steps+1):
    pf[j]=(math.exp(-alpha*j*dt)*fgrid[j]+dt*(np.dot(ef[1:j],pf[j-1:0:-1])+0.5*ef[j]))/(1-0.5*dt*ef[0])
    pg[j]=math.exp(-alpha*j*dt)*ggrid[j]+dt*(0.5*eg[0]*pf[j]+np.dot(eg[1:j],pf[j-1:0:-1])+0.5*eg[j])
assert abs(mc-pg[-1])<0.015,(mc,pg[-1])

for z0 in np.geomspace(1e-4,1e3,45):
    h=10*math.expm1(-z0)/z0**2+10/z0 # same universal expression; stable enough for z>1e-4
    assert 0<h<5.00001
    # exact derivative is negative, using exp(z)>1+z.
    assert 2-z0-(z0+2)*math.exp(-z0)<1e-12

# Squared-increment nonoverlap correlation, direct double integral of D covariance.
for alpha,lam,h,lag in [(1.3,.7,.5,1.3),(.5,2.,1.,2.3),(1.,1.,.1,.25)]:
    direct=quad(lambda v:quad(lambda u:20*lam**4/alpha**2*math.exp(-alpha*(u-v)),lag,lag+h)[0],0,h)[0]*4
    exact=80*lam**4/alpha**4*math.exp(-alpha*(lag-h))*(1-math.exp(-alpha*h))**2
    assert abs(direct/exact-1)<2e-11

print('PASS: harmonic-oscillator Feynman–Kac PDE, two independent fourth-moment generator equations, 3 renewal-transform tests, Monte Carlo conditional characteristic, 45 monotonicity/boundary checks, 3 volatility-correlation integrations.')
print(f'Independent time-domain vs conditional simulation: {pg[-1]:.8f} vs {mc:.8f} at T={T}, alpha=1.3, Lambda=0.7, k={k0}')
