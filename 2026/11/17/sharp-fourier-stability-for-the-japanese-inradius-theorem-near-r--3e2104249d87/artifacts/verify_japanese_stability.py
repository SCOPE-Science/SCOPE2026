"""Reproducible exact and floating-point checks for a polygonal inradius-flip linearization.

Requires Python, sympy and numpy. Does not certify an asymptotic theorem by testing.
"""
import sympy as sp
import numpy as np

t = sp.symbols('t', real=True)

def half_sine(k):
    # h=4 arctan(t), so this is sin(k*h/2).
    z = sp.expand((1 + sp.I*t)**(2*k))
    return sp.expand(sp.im(z)) / (1+t*t)**k

def radial_inradius_derivative(b, c):
    # Triangle vertices at anomalies 0,b*h,c*h; move the first radially.
    A = 2*half_sine(b)*half_sine(c-b)*half_sine(c)
    P = 2*(half_sine(b)+half_sine(c-b)+half_sine(c))
    r = sp.cancel(2*A/P)
    return sp.cancel((half_sine(2*b)-half_sine(2*c)
                      -r*(half_sine(b)+half_sine(c)))/P)

f0 = sp.factor(radial_inradius_derivative(1,2)
               +radial_inradius_derivative(2,3)
               -radial_inradius_derivative(1,3))
assert sp.simplify(f0+(1+t*t)**3/(4*(1-t*t)*(3-t*t))) == 0


def radius(a, b, c):
    lengths=[np.linalg.norm(a-b),np.linalg.norm(b-c),np.linalg.norm(c-a)]
    signed_area2=np.linalg.det(np.vstack((b-a,c-a)))
    return abs(signed_area2)/sum(lengths)

def flips(u):
    n=len(u)
    angles=2*np.pi*np.arange(n)/n
    p=np.column_stack(((1+u)*np.cos(angles),(1+u)*np.sin(angles)))
    out=np.zeros(n)
    for j in range(n):
        a,b,c,d=(p[(j+k)%n] for k in range(4))
        out[j]=radius(a,b,c)+radius(a,c,d)-radius(a,b,d)-radius(b,c,d)
    return out

for n in (4,5,6,7,11,30):
    x=np.pi/n
    kappa=1/(2*np.cos(x)*(1+np.cos(x))*(1+2*np.cos(x)))
    co=1+2*np.cos(2*x)
    coeff=np.array([-1,co,-co,1])*kappa
    e=1e-6
    zero=np.zeros(n)
    for j in range(n):
        u=zero.copy();u[j]=e
        actual=(flips(u)[0]-flips(zero)[0])/e
        target=coeff[j] if j<4 else 0
        assert abs(actual-target)<1e-5,(n,j,actual,target)
    symbols=np.exp(2j*np.pi*np.arange(n)/n)
    all_singular=np.abs((symbols-1)*(symbols-np.exp(2j*x))*(symbols-np.exp(-2j*x)))
    sigma=8*np.sin(x)*np.sin(2*x)*np.sin(3*x)
    assert abs(min(all_singular[2:n-1])-sigma)<1e-9
    mode=np.cos(4*np.pi*np.arange(n)/n)
    mode=mode/np.linalg.norm(mode)
    for e in (1e-3,1e-4):
        ratio=np.linalg.norm(flips(e*mode))/e
        assert abs(ratio-kappa*sigma)<0.05,(n,e,ratio,kappa*sigma)
    # Nearby circle of center c and radius R, intersected with each radial ray.
    theta=2*np.pi*np.arange(n)/n
    center=np.array([0.02,-0.01]);R=1.05
    dots=center[0]*np.cos(theta)+center[1]*np.sin(theta)
    radii=dots+np.sqrt(R*R-(center@center)+dots*dots)
    assert np.linalg.norm(flips(radii-1))<1e-10
print('JAPANESE_INRADIUS_FOURIER_CHECKS_OK')
