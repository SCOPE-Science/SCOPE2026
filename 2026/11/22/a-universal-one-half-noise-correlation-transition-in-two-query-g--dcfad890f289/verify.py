"""Reproducible algebra and finite checks for two-site correlated-noise quadrature."""
from fractions import Fraction as F
from random import Random
from math import isfinite
import sympy as s

def k(u,v):
    return min(u,v)-u*v

def m(u):
    return u*(1-u)/2

def gain(u,v,eta,rho):
    a=k(u,u)+eta
    d=k(v,v)+eta
    b=k(u,v)+eta*rho
    det=a*d-b*b
    if det.is_number if hasattr(det,"is_number") else True:
        assert det>0
    return (d*m(u)**2 - 2*b*m(u)*m(v)+a*m(v)**2)/det

d,eta,rho=s.symbols('d eta rho', real=True)
u=(1-d)/2;v=(1+d)/2
# For ordered u <= v the bridge covariance is u(1-v).
a=u*(1-u)+eta
b=u*(1-v)+eta*rho
D=v*(1-v)+eta
mu=u*(1-u)/2
mv=v*(1-v)/2
symgain=s.factor((D*mu**2-2*b*mu*mv+a*mv**2)/(a*D-b*b))
sym_expected=(1-d*d)**2/(16*(1-d+2*eta*(1+rho)))
assert s.simplify(symgain-sym_expected)==0
endpoint= s.factor(gain(s.Integer(0),s.Rational(1,2),eta,rho))
endpoint_expected=1/(16*(1+4*eta*(1-rho**2)))
assert s.simplify(endpoint-endpoint_expected)==0
center=s.factor(gain(s.Rational(1,2),s.Rational(1,2),eta,rho))
center_expected=1/(16*(1+2*eta*(1+rho)))
assert s.simplify(center-center_expected)==0
cross=s.factor(endpoint-center)
assert s.simplify(cross.subs(rho,s.Rational(1,2)))==0
assert s.factor(cross).has(2*rho-1)
assert gain(F(0),F(1,2),F(1),F(3,4))==F(1,44)
assert F(1,44)>F(1,56)
assert F(1,44)-F(1,56)==F(3,616)
assert F(1,12)-F(1,44)==F(2,33)
# Corner values of strictly convex leading objective with m_max = M.
M=s.symbols('M',positive=True)
Q=lambda p,q:s.factor((p*p-2*rho*p*q+q*q)/(1-rho*rho))
assert s.simplify(Q(M,M)-2*M*M/(1+rho))==0
assert s.simplify(Q(M,0)-M*M/(1-rho*rho))==0
assert s.simplify(Q(M,0)-Q(M,M)-M*M*(2*rho-1)/(1-rho*rho))==0
x,y=s.symbols('x y',real=True)
hess=s.hessian(Q(x,y),(x,y))
assert s.simplify(hess.det()-4/(1-rho*rho))==0
# Exact rational test of the bound on every reflected design in a dense grid.
for j in range(0,501):
    dd=F(j,500)
    G=gain((1-dd)/2,(1+dd)/2,F(1),F(3,4))
    assert G<=F(1,56) and G<F(1,44)
# Uniform high-noise error bound checked for rational sample locations and correlations.
rng=Random(3507)
for _ in range(1200):
    u0=F(rng.randrange(101),100)
    v0=F(rng.randrange(101),100)
    e0=F(rng.randrange(1,101),3)
    r0=F(rng.randrange(-90,91),100)
    g0=gain(u0,v0,e0,r0)
    q0=Q(m(u0),m(v0)).subs(rho,r0)
    lead=q0/e0
    err=lead-g0
    # ||k_2||_op <= 1/2, ||m||^2 <= 1/32
    bd=F(1,64)/(e0*e0*(1-abs(r0))**2)
    assert err>=0 and err<=bd
assert isfinite(float(gain(F(0),F(1,2),F(1),F(3,4))))
print('PASS: 6 exact symbolic identities, 4 exact witness identities, 501 symmetric-grid checks, 1200 resolvent-error checks')
