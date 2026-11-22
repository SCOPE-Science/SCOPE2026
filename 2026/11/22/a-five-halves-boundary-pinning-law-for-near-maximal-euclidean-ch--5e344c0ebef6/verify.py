"""Deterministic algebraic and numerical checks for a random hemisphere chord-triangle endpoint law.
Scientific claims rely on the accompanying proof, not on finite sampling.
Run: python verify.py
"""
import math
import numpy as np
import sympy as sp
from scipy.stats import qmc, beta

M=3*math.sqrt(3)/4
ka=math.sqrt(3)/4
kz=math.sqrt(3)/12
C=32*3**(.75)/(45*math.pi)


def area(q,r,z):
    """Unsigned Euclidean area of three unit sphere vertices, one azimuth pinned at zero."""
    theta=np.stack([np.zeros_like(q),2*math.pi/3+q,4*math.pi/3+r],axis=-1)
    xy=np.sqrt(np.maximum(0,1-z*z))
    p=np.stack([xy*np.cos(theta),xy*np.sin(theta),z],axis=-1)
    return .5*np.linalg.norm(np.cross(p[...,1,:]-p[...,0,:],p[...,2,:]-p[...,0,:]),axis=-1)


def check_quadratic():
    q,r,z1,z2,z3=sp.symbols('q r z1 z2 z3',real=True)
    u=[q,r,z1,z2,z3]
    d={v:0 for v in u}
    A=-sp.Rational(1,2)-sp.sqrt(3)*q/2+q*q/4+(z1*z1+z2*z2)/4+z1*z2
    B=-sp.Rational(1,2)+sp.sqrt(3)*r/2+r*r/4+(z1*z1+z3*z3)/4+z1*z3
    D=-sp.Rational(1,2)-sp.sqrt(3)*(r-q)/2+(r-q)**2/4+(z2*z2+z3*z3)/4+z2*z3
    four_area2=4*(1-A)*(1-B)-(1+D-A-B)**2
    H=sp.Matrix([[sp.diff(four_area2,x,y).subs(d) for y in u] for x in u])
    quadratic=sp.expand(-sp.Rational(1,16)/(3*sp.sqrt(3)/4)*(sp.Matrix(u).T*H*sp.Matrix(u))[0])
    expected=sp.sqrt(3)/4*(q*q-q*r+r*r)+sp.sqrt(3)/12*(z1+z2+z3)**2
    assert sp.simplify(quadratic-expected)==0
    V=sp.Rational(64,45)*sp.pi*3**sp.Rational(3,4)
    Csym=sp.simplify(V/(2*sp.pi**2))
    assert sp.simplify(Csym-32*3**sp.Rational(3,4)/(45*sp.pi))==0
    print('EXACT_QUADRATIC_AND_COEFFICIENT_OK',C)


def check_pointwise():
    u=np.array([.28,-.39,.14,.23,.34])
    Q=ka*(u[0]**2-u[0]*u[1]+u[1]**2)+kz*sum(u[2:])**2
    for t in [.1,.05,.025,.0125]:
        z=np.broadcast_to(t*u[2:],(1,3))
        a=float(area(np.array([t*u[0]]),np.array([t*u[1]]),z)[0])
        err=abs((M-a)/t**2-Q)
        print('HESSIAN_RESIDUAL',t,err)
        assert err < .3*t


def check_integral():
    # Sobol quadrature on a cap of quadratic radius 1.2; normalise by exact cap volume.
    N=2**16
    pts=qmc.Sobol(5,scramble=False).random_base2(16)
    T=beta.ppf(pts[:,0],1.5,2)
    rho=np.sqrt(pts[:,1]); phi=2*np.pi*pts[:,2]
    x=np.sqrt((1-T)/ka)*rho*np.cos(phi)
    y=np.sqrt((1-T)/ka)*rho*np.sin(phi)
    q=x+y/np.sqrt(3); r=2*y/np.sqrt(3)
    # Uniform 2-simplex fractions, from square-to-triangle barycentric map.
    sq=np.sqrt(pts[:,3]); v=pts[:,4]
    props=np.column_stack((1-sq,sq*(1-v),sq*v))
    z=np.sqrt(T/kz)[:,None]*props
    predicted=np.mean((ka*(q*q-q*r+r*r)+kz*np.sum(z,axis=1)**2)<=1+1e-10)
    assert predicted > .9999
    for e in (.02,.005,.001,.0002):
        scale=math.sqrt(1.2*e)
        tri=area(scale*q,scale*r,scale*z)
        factor=1.2**(2.5)*np.mean((M-tri)<e)
        print('ENDPOINT_COEFFICIENT_RATIO',e,factor)
        assert .9<factor<1.1
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    check_quadratic()
    check_pointwise()
    check_integral()
