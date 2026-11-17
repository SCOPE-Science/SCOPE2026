"""Exact symbolic and independent numerical checks for random ideal-tetrahedron volume tails.

Requires Python 3 with SymPy, NumPy and SciPy. No network access is used.
"""
import math
import numpy as np
import sympy as sp
from scipy.special import spence
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss

x,y,u,v=sp.symbols('x y u v', real=True)
T=sp.symbols('T',real=True)
S=sp.sqrt(3); z0=complex(.5,math.sqrt(3)/2)
x0=sp.Rational(1,2); y0=S/2
q0=x*x+y*y; q1=(1-x)**2+y*y
L=sp.log(q0)/2; M=sp.log(q1)/2
# From the differential identity dD=log|z| d arg(1-z)-log|1-z| d arg z.
Dx=-y*L/q1+y*M/q0
Dy=(x-1)*L/q1-x*M/q0
at={x:x0,y:y0}
terms={k:0 for k in (2,3,4)}
for k in terms:
    for i in range(k+1):
        j=k-i
        deriv=sp.diff(Dx,x,i-1,y,j) if i else sp.diff(Dy,y,j-1)
        terms[k]+=sp.simplify(deriv.subs(at)/(sp.factorial(i)*sp.factorial(j)))*u**i*v**j
assert sp.expand(terms[2]+S*(u*u+v*v)/4)==0
assert sp.expand(terms[3]-v*(3*u*u+7*v*v)/12)==0
assert sp.expand(terms[4]-S*(u**4+18*u*u*v*v-15*v**4)/48)==0

# Marshall--Martin closed density, including both logarithmic terms.
A=(3*x*x-3*x**3+y*y-3*x*y*y)/(2*sp.pi*y**4)
B=(-6*x*x+3*x**3-2*y*y+3*x*(1+y*y))/(2*sp.pi*y**4)
C=(3*(x-1)**2*x*x+(2*x-1)**2*y*y+y**4)/(sp.pi*y**5)
rho=A*sp.log(q0)+B*sp.log(q1)-1/(sp.pi*y*y)+C*T
rho0=sp.simplify(rho.subs(at))
rx=sp.simplify(sp.diff(rho,x).subs(at))
ry=sp.simplify(sp.diff(rho,y).subs(at))
rxx=sp.simplify(sp.diff(rho,x,2).subs(at)+C.subs(at)*(-S/2))
rxy=sp.simplify(sp.diff(rho,x,y).subs(at))
ryy=sp.simplify(sp.diff(rho,y,2).subs(at)+C.subs(at)*(-S/2))
assert sp.simplify(rho0-4*(2*S*T-3)/(9*sp.pi))==0
assert rx==0 and rxy==0
assert sp.simplify(ry-16*(-2*T+S)/(9*sp.pi))==0
assert sp.simplify(rxx-4*(8*S*T-15)/(9*sp.pi))==0
assert sp.simplify(ryy-4*(8*S*T-13)/(3*sp.pi))==0

a=S/4; b=-terms[3];c=-terms[4]
lin=rx*u+ry*v
quadr=(rxx*u*u+2*rxy*u*v+ryy*v*v)/2

def circle_integral(poly):
    result=0
    for (i,j),co in sp.Poly(sp.expand(poly),u,v).terms():
        if i%2 or j%2:continue
        p=i//2; q=j//2
        result+=co*sp.factorial(2*p)*sp.factorial(2*q)/(4**(p+q)*sp.factorial(p)*sp.factorial(q)*sp.factorial(p+q))
    return sp.simplify(2*sp.pi*result)

I=circle_integral(rho0*(3*b*b/(4*a*a)-c/(2*a))-b*lin/(2*a)+quadr/4)
C1=sp.simplify(2*sp.pi*rho0/a)
C2=sp.simplify(2*I/a**2)
assert sp.simplify(C1-(64*T/9-32*S/9))==0
assert sp.simplify(C2-32*(104*S*T-183)/243)==0

def bloch(z):
    return np.imag(spence(1-z))+np.angle(1-z)*np.log(np.abs(z))

def closed_rho(z):
    xx=np.real(z); yy=np.imag(z)
    aa=(3*xx**2-3*xx**3+yy**2-3*xx*yy**2)/(2*np.pi*yy**4)
    bb=(-6*xx**2+3*xx**3-2*yy**2+3*xx*(1+yy**2))/(2*np.pi*yy**4)
    cc=(3*(xx-1)**2*xx**2+(2*xx-1)**2*yy**2+yy**4)/(np.pi*yy**5)
    return aa*np.log(np.abs(z)**2)+bb*np.log(np.abs(1-z)**2)-1/(np.pi*yy**2)+cc*bloch(z)

# Independent numerical evaluation of the theorem's positive simplex integral.
GL=90
n,w=leggauss(GL); t=(n+1)/2; wt=w/2
alpha=t[:,None]*t[None,:]; beta=t[:,None]*(1-t[None,:]); gamma=1-t[:,None]
ws=wt[:,None]*wt[None,:]
def positive_rho(z):
    Q=alpha*beta*abs(1-z)**2+alpha*gamma*abs(z)**2+beta*gamma
    return float((2/np.pi)*np.sum(alpha*beta*gamma*t[:,None]*ws/Q**2))

for z in [z0,z0+.04+.01j,z0-.04+.025j,z0+.06-.02j]:
    assert abs(float(closed_rho(z))-positive_rho(z))<3e-8,(z,closed_rho(z),positive_rho(z))

v3=float(bloch(z0)); cc1=float(C1.subs(T,v3));cc2=float(C2.subs(T,v3))
assert abs(v3-1.0149416064096536)<1e-13
assert abs(cc1-1.05895966311264)<1e-11
assert abs(cc2+0.02307626432556)<1e-10

def exact_near_tail(epsilon, n_angles=160, n_rad=18):
    dirs=np.exp(1j*np.arange(n_angles)*2*np.pi/n_angles)
    endpoint=np.array([brentq(lambda rad: v3-bloch(z0+rad*direction)-epsilon,
                                1e-12,4*math.sqrt(epsilon),xtol=1e-13) for direction in dirs])
    t,w=leggauss(n_rad)
    radius=endpoint[:,None]*(1+t[None,:])/2
    zz=z0+radius*dirs[:,None]
    local=float(np.mean(np.sum(closed_rho(zz)*radius*w[None,:]*endpoint[:,None]/2,axis=1))*2*np.pi)
    return 2*local
for e in (0.004,0.002,0.001):
    actual=exact_near_tail(e)
    remainder=actual-cc1*e-cc2*e*e
    assert abs(remainder)<0.08*e**3,(e,actual,remainder)
    print('eps=',e,'probability=',actual,'second_coeff_est=',(actual-cc1*e)/e**2)
print('exact symbolic coefficients and positive-density cross-checks passed')
print('v3=',v3,'C1=',cc1,'C2=',cc2)
