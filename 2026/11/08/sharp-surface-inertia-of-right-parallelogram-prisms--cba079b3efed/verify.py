"""Reproducible exact and independent face-integral checks for right parallelogram prisms."""
from fractions import Fraction as F
from math import sin, cos, sqrt, pi
import random
import sympy as sp
import numpy as np

def moments(a,b,ang,h):
    B=a*b*sin(ang)
    A=2*B+4*h*(a+b)
    JA=B*(a*a+b*b)/12
    JL=(a+b)**3/6
    J=2*JA+2*h*JL+2*B*h*h+(4/3)*(a+b)*h**3
    return A,J

def faces(a,b,ang,h):
    u=np.array([a,0.,0.]);v=np.array([b*cos(ang),b*sin(ang),0.])
    t,w=np.polynomial.legendre.leggauss(5);t=t/2;w=w/2
    A=J=0.
    for zz in [-h,h]:
        for i,wi in zip(t,w):
            for j,wj in zip(t,w):
                p=i*u+j*v+np.array([0.,0.,zz]); da=a*b*sin(ang)*wi*wj
                A+=da;J+=da*p.dot(p)
    for side in (-.5,.5):
        for k,base,jac in [('u',u,b),('v',v,a)]:
            horizontal = (side*base)
            transverse = v if k=='u' else u
            for i,wi in zip(t,w):
                for j,wj in zip(t,w):
                    p=horizontal+i*transverse+np.array([0.,0.,2*h*j]);da=2*h*jac*wi*wj
                    A+=da;J+=da*p.dot(p)
    return A,J

def symbolic():
    x,y,h=sp.symbols('x y h')
    area=2*y+4*h
    moment=y*(1-2*x)/6+h/sp.Integer(3)+2*y*h**2+4*h**3/sp.Integer(3)
    positive=(24*y*(sp.Rational(1,4)-x)+(1-4*y)*8*h*(12*h*h-10*h+3)
              +y*(4*h-1)**2*(24*h+1)+20*y*(sp.Rational(1,4)-y))
    assert sp.expand(72*moment-5*area**2-positive)==0
    assert sp.simplify((moment/area**2).subs({x:sp.Rational(1,4),y:sp.Rational(1,4),h:sp.Rational(1,4)})-sp.Rational(5,72))==0

def sample():
    rng=random.Random(7919)
    mn=1.
    for _ in range(4000):
        a=10**rng.uniform(-1,1);b=10**rng.uniform(-1,1)
        ang=rng.uniform(.06,pi-.06);h=10**rng.uniform(-1,1)
        A,J=moments(a,b,ang,h)
        A2,J2=faces(a,b,ang,h)
        assert abs(A-A2)<1e-8*max(1.,A)
        assert abs(J-J2)<1e-8*max(1.,J)
        assert J/A**2 >= 5/72-1e-12
        mn=min(mn,J/A**2)
    print('SURFACE_PRISM_CHECK_OK symbolic_identity=exact direct_face_integrals=4000 ratio_lower_bound=4000 random_min=',round(mn,10))

if __name__=='__main__':
    symbolic();sample()
