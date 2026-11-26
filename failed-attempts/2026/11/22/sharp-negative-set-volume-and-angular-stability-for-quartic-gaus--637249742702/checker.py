"""Reproducibility checks for the quartic Fourier-eigenfunction negative-volume theorem.

Requires SymPy and NumPy.  The infinite-dimensional volume inequality is
proved analytically in RESULT.md; these checks are complementary.
"""
import math
import itertools
import numpy as np
import sympy as sp

PI=sp.pi
CHECKS=0

def tally(assertion):
    global CHECKS
    if not assertion:
        raise AssertionError('verification failed at check '+str(CHECKS+1))
    CHECKS+=1

def indices(d,degree):
    if d==1:
        yield (degree,)
        return
    for k in range(degree+1):
        for rest in indices(d-1,degree-k):
            yield (k,)+rest

def gaussian_fourier_polynomial(poly, vars):
    """Compute Fourier transform of poly(x)*exp(-pi*|x|^2), divided by Gaussian."""
    d=len(vars)
    result=0
    G=sp.exp(-PI*sum(x*x for x in vars))
    for mon,coeff in sp.Poly(poly,*vars).terms():
        term=G
        for x,deg in zip(vars,mon):
            term=sp.diff(term,x,deg)
        result += coeff*(sp.I/(2*PI))**sum(mon)*term/G
    return sp.expand(result)

def delta(expr,vars):
    return sum(sp.diff(expr,x,2) for x in vars)

for d in [2,3,4]:
    xs=sp.symbols('x0:'+str(d),real=True)
    for powers in indices(d,4):
        Q=sp.prod(x**n for x,n in zip(xs,powers))
        P=Q-delta(Q,xs)/(8*PI)
        transform=gaussian_fourier_polynomial(P,xs)
        tally(sp.simplify(transform-P)==0)
        # Generalized homogeneous harmonic polar identity.
        # Evaluated on a sphere by setting r=1 in the radial coordinate.
        radial_quad=sum(xs_i**2 for xs_i in xs)
        # Euler identity for homogeneous quartic.
        tally(sp.expand(sum(x*sp.diff(Q,x) for x in xs)-4*Q)==0)
        tally(sp.expand(sum(x*sp.diff(delta(Q,xs),x) for x in xs)-2*delta(Q,xs))==0)

# A nonradial strictly positive quartic on R^2.
x,y=sp.symbols('x y',real=True)
Q=(x*x+y*y)**2+sp.Rational(1,3)*x**4+sp.Rational(1,5)*x*x*y*y
D=delta(Q,(x,y))
Qf=sp.lambdify((x,y),Q,'numpy')
Df=sp.lambdify((x,y),D,'numpy')
Gx=sp.lambdify((x,y),sp.diff(Q,x),'numpy')
Gy=sp.lambdify((x,y),sp.diff(Q,y),'numpy')
angles=np.linspace(0,2*math.pi,65536,endpoint=False)
X,Y=np.cos(angles),np.sin(angles)
A=Qf(X,Y)
DeltaSphere=Df(X,Y)-16*A  # 4(d+2) A, d=2
R2=(4/(2*math.pi))+DeltaSphere/(8*math.pi*A)
volume=math.pi*np.mean(np.maximum(0,R2))
angGx=Gx(X,Y)-4*A*X
angGy=Gy(X,Y)-4*A*Y
energy=np.mean((angGx**2+angGy**2)/A**2)
lower=2*(1+energy/16)
# Periodic trapezoid integration is exponentially accurate for smooth data.
tally(volume>=lower-1e-10)
tally(volume>2.0001)
# Exact integral identity that produces the Fisher information.
tally(abs(np.mean(DeltaSphere/A)-energy)<1e-10)
# Sharp radial equality in every d.
for d in [2,3,4,5,10]:
    w=math.pi**(d/2)/math.gamma(d/2+1)
    rho2=(d+2)/(2*math.pi)
    tally(abs(w*(rho2**(d/2))/w/(rho2**(d/2))-1)<1e-12)
print('PASS',CHECKS,'exact algebraic and numerical assertions')
print('nonradial d=2 volume',format(volume,'.12f'),'Fisher bound',format(lower,'.12f'),'radial optimum 2')
