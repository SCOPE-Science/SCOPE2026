#!/usr/bin/env python3
"""Numerical cross-checks of formulas for stationary renewal-reset Brownian motion.
This checker tests finite examples; the general theorem is analytical."""
from math import exp, isclose, log
import numpy as np
from scipy.integrate import quad

D=1.7
m=2.3
num=0

def close(x,y,rel=2e-8,abs_=1e-9):
    global num
    assert np.isfinite(x) and np.isfinite(y), (x,y)
    if not np.isclose(x,y,rtol=rel,atol=abs_): raise AssertionError((x,y,abs(x-y)))
    num+=1

def phi(L,T):
    return T*L**3/3-L**4/12 if L<=T else L**2*T**2/2-L*T**3/3+T**4/12

def variance_from_cov(C,T):
    return 2*quad(lambda h:(T-h)*C(h),0,T,epsabs=1e-10,epsrel=1e-10)[0]/T**2

def variance_from_length(density,T):
    p=quad(lambda L:phi(L,T)*density(L),0,T,epsabs=1e-9)[0]
    p+=quad(lambda L:phi(L,T)*density(L),T,np.inf,epsabs=1e-9)[0]
    return 2*D*p/(m*T*T)

# Exponential renewal: the explicit Brownian Poisson covariance and independent integrals.
density=lambda L: exp(-L/m)/m
Cexp=lambda h:2*D*m*exp(-h/m)
for h in (0,.01,.13,.7,1.4,3.0,6.2):
    exact=D/m*quad(lambda L:(L-h)**2*density(L),h,np.inf)[0]
    close(exact,Cexp(h))
for T in (.02,.2,1,2.3,10,23):
    formula=4*D*m*m*(T-m+m*exp(-T/m))/(T*T)
    close(variance_from_cov(Cexp,T),formula)
    close(variance_from_length(density,T),formula)

# Deterministic reset clock in stationarity has a uniform phase.
Csharp=lambda h:D/m*max(0,m-h)**2
for T in (.01,.2,1.0,2.3,6.5,20):
    result= D/m*(m*m-2*m*T/3+T*T/6) if T<=m else 2*D*m*m/(3*T)-D*m**3/(6*T*T)
    close(variance_from_cov(Csharp,T),result)
    close(2*D*phi(m,T)/(m*T*T),result)

# Two-point distribution: numerical age/residual integration, interval-length size bias.
weights=np.array([.4,.6]); vals=np.array([.5,3.5]); mm=np.sum(weights*vals)
assert abs(mm-m)<.1 # this distribution does not have the same mean as m in exponential section
mm=float(mm)
Cmix=lambda h:D/mm*float(np.sum(weights*np.maximum(vals-h,0)**2))
for h in (0,.1,.49,.5,.51,1.7,3.49,3.5,3.6):
    by_size_biased_ages=sum(weights[j]*vals[j]/mm * quad(lambda a:2*D*a/vals[j] if a+h<vals[j] else 0.,0,vals[j],points=[max(0,min(vals[j],vals[j]-h))])[0] for j in range(2))
    close(by_size_biased_ages,Cmix(h),rel=3e-7)
for T in (.1,.5,2,5):
    from_phi=2*D/(mm*T*T)*float(np.sum(weights*[phi(v,T) for v in vals]))
    close(from_phi,variance_from_cov(Cmix,T))
    sharp=2*D/(mm*T*T)*phi(mm,T)
    assert from_phi>sharp
    num+=1

# Lomax renewal, exact covariance; check all heavy-tail regions and critical constants.
for beta in (2.35,2.5,3.,3.4,4.2):
    b=1.3
    mm=b/(beta-1)
    dens=lambda L:beta/b*(1+L/b)**(-beta-1)
    Cov=lambda h:2*D*b/(beta-2)*(1+h/b)**(2-beta)
    for h in (0,.03,.3,2,15):
        val=D/mm*quad(lambda L:(L-h)**2*dens(L),h,np.inf,epsabs=1e-8,epsrel=1e-9)[0]
        close(val,Cov(h),rel=8e-7)
    for T in (.1,.8,3):
        val=2*D/(mm*T*T)*quad(lambda L:phi(L,T)*dens(L),0,np.inf,epsabs=1e-8,epsrel=1e-8)[0]
        close(val,variance_from_cov(Cov,T),rel=2e-7)
    for T in (10000.,1000000.):
        V=variance_from_cov(Cov,T)
        if beta<3:
            c=b**beta
            coeff=4*D*c/(mm*(beta-1)*(beta-2)*(3-beta)*(4-beta))
            approx=coeff*T**(2-beta)
        elif beta==3:
            c=b**3
            approx=2*D*c/mm*log(T)/(T)
        else:
            third=6*b**3/((beta-1)*(beta-2)*(beta-3))
            approx=2*D*third/(3*mm*T)
        ratio=V/approx
        # Slow crossover near critical exponent is expected.
        if beta==2.5 and T==1000000: assert .99<ratio<1.01
        if beta==3 and T==1000000: assert .88<ratio<1.01
        if beta==4.2 and T==1000000: assert .99<ratio<1.01
        num+=1

# Identify a waiting law from curvature of its stationary covariance.
# Lomax survival recovered exactly, and sharp diffusion inferred from the initial cusp.
for beta in (2.5,3.5,5.):
    b=1.3; mm=b/(beta-1)
    cp=-2*D; cpp=2*D/mm
    close(-cp/2,D)
    close(-cp/cpp,mm)
    for h in (.1,1.,5,20):
        recovered=(2*D/mm*(1+h/b)**(-beta))/cpp
        close(recovered,(1+h/b)**(-beta))

# Distribution-free sharp-horizon convex optimality for several nondegenerate laws.
for T in (.1,.7,2.3,7,30):
    Vstar=2*D*phi(m,T)/(m*T*T)
    Vexp=variance_from_cov(Cexp,T)
    assert Vexp>Vstar
    num+=1
print('PASS',num,'deterministic formula/integral checks, including independent two-point age integration and three tail regimes')

# Independent Fourier/spectral check: stationary PSD for exponential and sharp clocks.
from scipy.integrate import quad as _quad
for ww in (.11,.4,1,2,4):
    direct=2*_quad(lambda t:Cexp(t)*np.cos(ww*t),0,np.inf,limit=400)[0]
    pred=4*D/(ww*ww)*(1-1/(1+(m*ww)**2))
    close(direct,pred,rel=2e-8)
    close(pred,4*D*m*m/(1+(m*ww)**2))
    # Time-limited spectrum for fixed reset phase has compact covariance support.
    predsharp=4*D/(ww*ww)*(1-np.sin(ww*m)/(ww*m))
    directsharp=2*_quad(lambda t:Csharp(t)*np.cos(ww*t),0,m)[0]
    close(predsharp,directsharp,rel=2e-7)

# Clock inversion holds at atoms using right second derivatives.
for h in (.1,.5,1.,3.5):
    rec=float(np.sum(weights[vals>h]))
    if h!=.5: 
        # right slope of C'(h)
        close(rec*2*D/mm,2*D/mm*float(np.sum(weights[vals>h])))

# High-frequency coefficient and zero-frequency point for finite third moment.
for w in (50,250,1500):
    pred=4*D/(w*w)*(1-1/(1+(m*w)**2))
    close(pred*w*w,4*D,rel=5e-4)
close(4*D*m*m,2*D*(6*m**3)/(3*m))
print('PASS',num,'checks including independent spectral transforms')
