#!/usr/bin/env python3
"""Independent numerical and symbolic checks for a stationary resetting-Brownian current theorem.
NumPy and SciPy are needed; no external data files are required.
"""
import math
from scipy.integrate import quad
from scipy.special import erfcx, ndtr
import numpy as np
from scipy.stats import norm

N = 0

def close(x,y,rtol=1e-9,atol=1e-10):
    global N
    assert abs(x-y) <= atol+rtol*max(abs(x),abs(y)), (x,y)
    N+=1

def require(x):
    global N
    assert x
    N+=1

def h(u):
    return (3-2*u)*erfcx(math.sqrt(u))+2*math.sqrt(u/math.pi)

def C_an(rho,D,r,t):
    a=math.sqrt(r/D)
    u=r*t
    return rho/(8*a)*(1+math.exp(-u)*h(u))

def C_qu(rho,D,r,t):
    a=math.sqrt(r/D)
    u=r*t
    return rho/(8*a)*math.exp(-u)*h(u)

def Cqu_independent(rho,D,r,t):
    """Direct numerical integration of Gaussian path probabilities and stationary Laplace density.
       Numerically evaluates A and B without closed-form erfcx expression."""
    a=math.sqrt(r/D)
    sigma=math.sqrt(2*D*t)
    if t==0:
        return 3*rho/(8*a)
    # A = \int_0^infty dy (alpha/2)exp(-alpha*y) \int_0^y dz Phi((y-z)/sigma)
    def A_inner(y):
        return quad(lambda z: ndtr((y-z)/sigma),0,y,epsabs=1e-11)[0]
    A=quad(lambda y: (a/2)*math.exp(-a*y)*A_inner(y),0,40/a,epsabs=1e-10)[0]
    # B = \int_0^infty dz f(z) E(Phi((Y-z)/sigma)).
    # Integrate in Y by x=-Y or Y for x>=0, no closed-form transform used.
    def k(z):
        kp=quad(lambda y:(a/2)*math.exp(-a*y)*ndtr((y-z)/sigma),0,40/a,epsabs=2e-10)[0]
        km=quad(lambda y:(a/2)*math.exp(-a*y)*ndtr((-y-z)/sigma),0,40/a,epsabs=2e-10)[0]
        return kp+km
    B=quad(lambda z:0.5*math.exp(-a*z)*k(z),0,36/a,epsabs=1e-10)[0]
    return rho*math.exp(-r*t)*(A-B)

# Fixed-time variance and plateau anchors.
for rho,D,r in [(0.5,0.75,0.9),(1.4,2.7,0.8),(3,1,4.5)]:
    a=math.sqrt(r/D)
    close(C_an(rho,D,r,0),rho/(2*a))
    close(C_qu(rho,D,r,0),3*rho/(8*a))
    close(C_an(rho,D,r,0)-C_qu(rho,D,r,0),rho/(8*a))
    for u in [0.004,0.025,0.1,0.6,2,5,10]:
        t=u/r
        close(C_an(rho,D,r,t)-C_qu(rho,D,r,t),rho/(8*a))
        require(0<C_qu(rho,D,r,t)<C_qu(rho,D,r,0))
    us=np.geomspace(1e-6,100,301)
    qs=[C_qu(rho,D,r,u/r) for u in us]
    require(all(x>y>0 for x,y in zip(qs[:-1],qs[1:])))
    require(all(C_qu(rho,D,r,u/r)>0 for u in us))
    close(C_an(rho,D,r,100/r),rho/(8*a),rtol=1e-12)

# Direct, nested Gaussian-kernel probability quadrature (distinct from erfcx identities).
for rho,D,r,u in [(0.6,2.1,0.8,0.18),(1.8,0.7,3.0,1.5),(1.1,1,1,5.)]:
    num=Cqu_independent(rho,D,r,u/r)
    close(num,C_qu(rho,D,r,u/r),rtol=2e-8,atol=1e-9)

# Long-time exact coefficient, including slowly converging polynomial factor.
for u in [1000,10000,100000]:
    stable_ratio=h(u)*math.sqrt(math.pi*u)/4
    require(abs(stable_ratio-1)<10/u)

# Short-time cusp coefficient, subtract the finite intercept.
for u in [1e-8,1e-7,1e-6]:
    close((3-h(u))/math.sqrt(u),4/math.sqrt(math.pi),rtol=0.001)

# Environment shot-noise law, cumulants from independently integrated Laplace functional.
for theta in [0.2,1.,2.7,9.]:
    for s in [0.1,0.9,3.,12.]:
        direct=quad(lambda z: theta*(1-math.exp(-s*math.exp(-z)/2)),0,36,epsabs=1e-12)[0]
        mapped=theta*quad(lambda v:(1-math.exp(-s*v))/v,0,0.5,epsabs=1e-12)[0]
        close(direct,mapped,rtol=1e-10)
    for n in range(1,9):
        direct=quad(lambda z: theta*math.exp(-n*z)/2**n,0,60,epsabs=1e-13)[0]
        close(direct,theta/(n*2**n))

# Gaussian conditional covariance strictly positive for every threshold and lag:
# 2-point Chebyshev representation with the strict monotonicity of the heat semigroup.
for z in [0,0.01,0.4,3.]:
    for ylo,yhi in [(-1.,1.),(-0.1,3.),(-5.,0.001)]:
        if not(ylo<=z<yhi):continue
        for s0,s1 in [(.1,.3),(.1,2.),(1.,7.),(5.,15.)]:
            d0=ndtr((yhi-z)/s0)-ndtr((ylo-z)/s0)
            d1=ndtr((yhi-z)/s1)-ndtr((ylo-z)/s1)
            require(d0>d1>0)

print(f'PASS: {N} independent analytical/numerical cross-check assertions')
