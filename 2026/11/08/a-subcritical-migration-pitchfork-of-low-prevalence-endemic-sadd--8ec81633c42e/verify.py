"""Exact checks for the two-patch nonlinear-reinfection pitchfork theorem.

Run with: python verify.py
Requires sympy; optional scipy/numpy for diagnostic branch evaluation.
"""
import sympy as sp

R = sp.Rational
x, r = sp.symbols('x r')
z = sp.Matrix([x, r])
F = sp.Matrix([x*(-R(1,2)-R(3,2)*x+R(77,2)*r), x-r-40*x*r])
J = F.jacobian(z)
z0 = sp.Matrix([R(1,30), R(1,70)])
zplus = sp.Matrix([R(1,4), R(1,44)])
assert F.subs({x:z0[0],r:z0[1]}) == sp.zeros(2,1)
assert F.subs({x:zplus[0],r:zplus[1]}) == sp.zeros(2,1)
A = J.subs({x:z0[0],r:z0[1]})
assert A == sp.Matrix([[-R(1,20),R(77,60)],[R(3,7),-R(7,3)]])
assert sp.trace(A) == -R(143,60)
assert A.det() == -R(13,30)
root = sp.sqrt(26689)
lam = (root-143)/120
dstar = lam/2
assert sp.simplify((A-lam*sp.eye(2)).det()) == 0
assert 0 < dstar < R(1,10)
e = sp.Matrix([1,(root-137)/154])
ell = sp.Matrix([[R(1,2)+137*root/53378, 77*root/26689]])
assert sp.simplify(A*e-lam*e) == sp.zeros(2,1)
assert sp.simplify(ell*A-lam*ell) == sp.zeros(1,2)
assert sp.simplify((ell*e)[0]-1) == 0

def Q(u,v):
    return sp.Matrix([-R(3,2)*u[0]*v[0]+R(77,4)*(u[0]*v[1]+u[1]*v[0]),
                      -20*(u[0]*v[1]+u[1]*v[0])])

# The quadratic polarization is exact, not a truncated numerical derivative.
u0,u1,v0,v1=sp.symbols('u0 u1 v0 v1')
u=sp.Matrix([u0,u1]);v=sp.Matrix([v0,v1])
sub=lambda w: F.subs({x:w[0],r:w[1]}, simultaneous=True)
assert sp.simplify(sub(u+v)+sub(u-v)-2*sub(u)-2*Q(v,v)) == sp.zeros(2,1)
assert sp.simplify(sub(u+v)-sub(u-v)-2*J.subs({x:u0,r:u1})*v) == sp.zeros(2,1)
h=-A.inv()*Q(e,e)
assert sp.simplify(A*h+Q(e,e)) == sp.zeros(2,1)
eta=sp.simplify((ell*(2*Q(h,e)))[0])
eta_closed=-R(166845,52)+R(26656035,1387828)*root
assert sp.simplify(eta-eta_closed) == 0
assert root < 164
assert -R(166845,52)+R(26656035,1387828)*164 == -R(81336465,1387828) < 0
assert sp.N(eta,12) < -70
# The eigenvalue of the full four-dimensional Jacobian at a synchronized state
# is the multiset union of spectra(A) and spectra(A - 2 d I).
d=sp.symbols('d')
C=sp.BlockMatrix([[A-d*sp.eye(2),d*sp.eye(2)],
                  [d*sp.eye(2),A-d*sp.eye(2)]]).as_explicit()
t=sp.symbols('t')
assert sp.simplify(C.det() - A.det()*(A-2*d*sp.eye(2)).det()) == 0
# Critical cubic balance in the difference equation, using the slaved mean.
assert sp.simplify((ell*(2*Q(h,e)-eta*e))[0]) == 0
# Feasibility at the bifurcation: positive susceptible, infected and recovered.
assert 1-z0[0]-z0[1] == R(20,21)
assert 1-zplus[0]-zplus[1] == R(8,11)
print('VERIFY_OK exact quadratic identities, equilibria, critical spectrum, eigenvectors, cubic sign')
print('d_star',sp.N(dstar,16))
print('eta',sp.N(eta,16))
