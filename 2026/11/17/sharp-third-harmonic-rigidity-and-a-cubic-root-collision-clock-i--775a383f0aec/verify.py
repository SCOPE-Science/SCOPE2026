"""Exact identities and finite phase-portrait checks for the even triadic phase model."""
import sympy as s
from math import pi, cos, sin, sqrt
import numpy as np
from scipy.integrate import solve_ivp
x,y,r,u=s.symbols('x y r u',real=True)
G=lambda z: -s.cos(z)+r*s.cos(3*z)
Q=lambda z: -s.sin(z)+r*s.sin(3*z)/3
H=Q(y-x)-Q(y)+Q(x)
f=s.simplify(G(y-x)-G(y));h=s.simplify(G(y-x)-G(x))
assert s.trigsimp(s.diff(H,y)-f)==0
assert s.trigsimp(-s.diff(H,x)-h)==0
F=4*r*u**3-(1+3*r)*u
assert s.expand(F-(F.subs(u,1)))==s.expand((u-1)*(4*r*(u*u+u)+(r-1)))
assert s.factor((F-F.subs(u,1)).subs(r,s.Rational(1,9)))==s.Rational(4,9)*(u-1)**2*(u+2)
assert s.series(G(y)-G(0),y,0,7).expand().coeff(y,2)==(1-9*r)/2
assert s.series((G(y)-G(0)).subs(r,s.Rational(1,9)),y,0,6).expand().coeff(y,4)==s.Rational(1,3)
J=s.Matrix([f,h]).jacobian(s.Matrix([x,y]))
Js=s.simplify(s.trigsimp(J.subs({x:2*s.pi/3,y:4*s.pi/3})))
assert s.simplify(Js.trace())==0
assert s.simplify(Js.det()-s.Rational(9,4))==0
assert s.simplify(s.trigsimp(H.subs({x:2*s.pi/3,y:4*s.pi/3})+3*s.sqrt(3)/2))==0
assert s.simplify(H.subs(x,0))==0
assert s.simplify(H.subs(y,0))==0
assert s.simplify(H.subs(y,x))==0
# Compare numerically the Hamiltonian on representative regular solutions and the center locations.
for rv in [-1/3,-1/10,0,1/12,1/9]:
    def ff(t,z):
        xx,yy=z
        gg=lambda v:-cos(v)+rv*cos(3*v)
        return [gg(yy-xx)-gg(yy),gg(yy-xx)-gg(xx)]
    hlambda=s.lambdify((x,y,r),H,'numpy')
    for z0 in [[0.4,2.3],[2.1,4.4]]:
        sol=solve_ivp(ff,(0,15),z0,rtol=2e-10,atol=2e-12)
        hh=hlambda(sol.y[0,:],sol.y[1,:],rv)
        assert np.max(abs(hh-hh[0]))<2e-8,(rv,z0)
# Numerical critical laws along collision invariant set, using separation quadrature.
from scipy.integrate import quad
# For y=-eps and y0=-1, time tau(eps)=int_eps^1 du/[G(u)-G(0)], then tau*eps^p -> constants.
for rv,p,expected in [(0,1,2),(-1/3,1,0.5),(1/18,1,4),(1/9,3,1)]:
    def diff(t): return 1-cos(t)+rv*(cos(3*t)-1)
    for eps in [0.035,0.02]:
        # avoid extreme rounding; direct quadrature, positive interval.
        tm=quad(lambda z:1/diff(z),eps,1,epsabs=1e-7,limit=500)[0]
        assert abs(tm*eps**p-expected)<expected*0.15,(rv,tm*eps**p,expected)
print('VERIFY_OK symbolic_hamiltonian=3 polynomial_factors=2 local_series=2 splay_spectrum=3 collision_boundaries=3 numerical_energy=10 critical_clocks=8')
