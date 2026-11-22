"""Independent checks of the degree-two/degree-three polar-cap coupling formulas.

Requires Python 3 and SciPy. Finite tests are not a proof of all dimensions.
"""
from math import sqrt, gamma, pi
from scipy.integrate import quad
from numpy import linspace
import sympy as sp

d, s, r = sp.symbols('d s r', positive=True, real=True)
P = d * (d+2) * s**2 - 6*s + 3
Q = (1-s) * (1+(d+2)*s)
Z2 = P**2 / 12
V2 = d * Q**2 / (2*(d+1))
T2 = d*(d+2)*(1-s)**4 / (d+1)**2
checks = 0
# The reduced branches all carry the common positive factor
# J1 * sqrt(d*(d+2)*(d+4))/(d+3).
assert sp.simplify(P.subs(s,1/(d+2))-4*d/(d+2)) == 0; checks += 1
assert sp.simplify(Q.subs(s,1/(d+2))-2*(d+1)/(d+2)) == 0; checks += 1
h = sp.sqrt(6*d/(d+1))
poly = sp.expand(P - h*Q)
assert sp.simplify(poly-(d+2)*(d+h)*s**2+(6+h*(d+1))*s-(3-h)) == 0; checks+=1
# At the T/V crossing, C^2 - A^2 factors strictly positively.
rr = sp.sqrt(2*(d+2)/(d+1))
sc = (rr-1)/(rr+d+2)
d_of_r = 2/(r**2-2)-1
sc_of_r = sp.factor(sc.subs(d,d_of_r).subs(sp.sqrt(2*(d_of_r+2)/(d_of_r+1)),r))
assert sp.simplify(sc_of_r-(r**2-2)/(r*(r+2))) == 0; checks+=1
D = sp.factor((12*T2-P**2).subs(s,sc_of_r).subs(d,d_of_r))
# Replacing the positive radical before simplification is unnecessary here:
assert sp.factor(D+64*(r-1)*(r+1)**2*(r**2-3)/(r**2*(r+2)**3))==0; checks+=1

for dim in (3,4,5,6,8,12,20,50,100):
    root = sqrt(2*(dim+2)/(dim+1))
    cut = (root-1)/(root+dim+2)
    hh = sqrt(6*dim/(dim+1))
    A = (dim+2)*(dim+hh)
    B = 6+hh*(dim+1)
    C = 3-hh
    disc = B*B-4*A*C
    lo, hi = (B-sqrt(disc))/(2*A),(B+sqrt(disc))/(2*A)
    assert 0<lo<cut<1/(dim+2)<hi<1;checks+=1
    def branches(x):
        p=dim*(dim+2)*x*x-6*x+3
        q=(1-x)*(1+(dim+2)*x)
        return p/sqrt(12),sqrt(dim/(2*(dim+1)))*q,sqrt(dim*(dim+2))/(dim+1)*(1-x)**2
    for x in (0,lo/2, (lo+cut)/2,cut,(cut+1/(dim+2))/2, 1/(dim+2), (1/(dim+2)+hi)/2,hi,(hi+1)/2,0.999):
        z,v,t=branches(x)
        target = 2 if x<cut-1e-11 else 1 if cut+1e-11<x<hi-1e-11 else 0 if x>hi+1e-11 else None
        assert target is None or (z,v,t)[target]>=max(z,v,t)-1e-10,(dim,x,z,v,t)
        checks+=1
    # Full polar-integration computation, not the truncated-moment recurrence.
    c = gamma(dim/2)/(sqrt(pi)*gamma((dim-1)/2))
    def density(u): return c*(1-u*u)**((dim-3)/2)
    n2z = 2*(dim-1)/(dim**2*(dim+2))
    n3z = 6*(dim-1)/(dim*(dim+2)**2*(dim+4))
    n2v = 1/(dim*(dim+2))
    n3v = 2*(dim+1)/(dim*(dim+4))
    n2t = 4/(dim*(dim+2))
    n3t = 4/(dim*(dim+2)*(dim+4))
    for x in (0, .01, cut, .23, hi, .70, .95):
        a=sqrt(x)
        j1 = quad(lambda u:u*density(u),a,1,epsabs=2e-12)[0]
        rawz = quad(lambda u:(u*u-1/dim)*(u**3-3*u/(dim+2))*density(u),a,1,epsabs=2e-12)[0]
        rawv = quad(lambda u:u*((dim+2)*u*u-1)*(1-u*u)/(dim-1)*density(u),a,1,epsabs=2e-12)[0]
        rawt = quad(lambda u:u*4*(1-u*u)**2/((dim-1)*(dim+1))*density(u),a,1,epsabs=2e-12)[0]
        numeric=(rawz/sqrt(n2z*n3z),rawv/sqrt(n2v*n3v),rawt/sqrt(n2t*n3t))
        p,q,tt = branches(x)
        predicted=tuple(j1*sqrt(dim*(dim+2)*(dim+4))/(dim+3)*v for v in (p,q,tt))
        for z,pred in zip(numeric,predicted):
            assert abs(z-pred)<4e-10,(dim,x,z,pred)
            checks+=1
# Independently check the entire 3D azimuthal cross-block against
# associated-Legendre functions, without invoking the polynomial moment formulas.
from scipy.special import lpmv
from math import factorial
for x in (0, .02, .10, .50, .80):
    a=sqrt(x)
    J1=(1-x)/4
    common=J1*sqrt(3*5*7)/6
    analytic=(common*(15*x*x-6*x+3)/sqrt(12),
              common*sqrt(3/8)*(1-x)*(1+5*x),
              common*sqrt(15)/4*(1-x)**2)
    for m in range(3):
        norm=lambda ell:sqrt((2*ell+1)/(4*pi)*factorial(ell-m)/factorial(ell+m))
        integral=quad(lambda u:lpmv(m,2,u)*lpmv(m,3,u),a,1,epsabs=1e-13)[0]
        direct=abs(2*pi*norm(2)*norm(3)*integral)
        assert abs(direct-analytic[m])<4e-12,(x,m,direct,analytic[m]);checks+=1
print(f'PASS: {checks} independent exact/inequality/quadrature assertions')
