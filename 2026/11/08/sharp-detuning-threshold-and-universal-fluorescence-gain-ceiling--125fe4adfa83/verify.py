"""Standalone exact checks of the stationary fluorescence reset-rate phase theorem."""
import sympy as sp
r,g,O,D = sp.symbols('r g O D', positive=True, real=True)
B = g**3 + 2*g*O**2 + 4*g*D**2 + (5*g**2+4*O**2+4*D**2)*r + 8*g*r**2+4*r**3
J = g*O**2*(g+2*r)/B
J0 = g*O**2/(g**2+2*O**2+4*D**2)
poly = 16*r**3+28*g*r**2+16*g**2*r+3*g**3-4*g*D**2
checks=0

def assert_equal(a,b):
    global checks
    assert sp.cancel(a-b)==0, f'Identity failed: {sp.factor(a-b)}'
    checks+=1

# Direct independent stationary Bloch balance equations, not renewal theory.
h = g/2+r
p,u,v = sp.symbols('p u v')
sol=sp.solve([O*v-(g+r)*p, -h*u-D*v, D*u-h*v+O*(1-2*p)/2], [p,u,v])
assert_equal(g*sol[p],J)
assert_equal(J.subs(r,0),J0)
assert_equal(sp.diff(J,r),-g*O**2*poly/B**2)
assert_equal(J-J0, -g*O**2*r*(3*g**2+8*g*r+4*r**2-4*D**2)/((g**2+2*O**2+4*D**2)*B))
assert_equal(2*J0-J,g*O**2*(g**3+2*g*O**2+4*g*D**2+(8*g**2+4*O**2)*r+16*g*r**2+8*r**3)/((g**2+2*O**2+4*D**2)*B))

# Completely different derivation: invert the no-photon 4x4 real-density generator,
# then evaluate the renewal Laplace transform and flux from per-window counts.
L = sp.Matrix([[0,0,0,-O],[0,-g,0,O],[0,0,-g/2,-D],[O/2,-O/2,D,-g/2]])
q = sp.factor(g*((r*sp.eye(4)-L).inv()*sp.Matrix([1,0,0,0]))[1])
assert_equal(r*q/(1-q),J)
assert_equal(-sp.diff(q,r).subs(r,0),(g*g+2*O*O+4*D*D)/(g*O*O))

# Reconstruct the complete Lindbladian (including trace-preserving spontaneous
# emission and state reset) from 2x2 matrices independently for exact samples.
for gg,oo,dd,rr in [(1,1,0,sp.Rational(1,2)),(1,1,2,sp.Rational(1,3)),
                     (2,3,4,sp.Rational(5,7)),(1,sp.Rational(1,2),1,2),
                     (3,2,1,sp.Rational(9,4)),(2,1,sp.Rational(9,5),1),
                     (4,5,6,3),(1,3,4,sp.Rational(7,3))]:
    hh = sp.Rational(gg,2)+rr
    mat = sp.Matrix([[-(gg+rr),0,oo], [0,-hh,-dd],[-oo,dd,-hh]])
    vec = sp.Matrix([0,0,-oo/2])
    puv=mat.inv()*vec
    jj=sp.factor(gg*puv[0]); expected=J.subs({g:gg,O:oo,D:dd,r:rr})
    assert_equal(jj,expected)
    # Direct integral of quantum no-jump density evolution for this parameter set.
    ll=L.subs({g:gg,O:oo,D:dd}); z=(rr*sp.eye(4)-ll).inv()*sp.Matrix([1,0,0,0]);
    qq=gg*z[1]
    assert_equal(rr*qq/(1-qq),expected)

# Sign classification via exact roots for rational examples.
for gg,oo,dd in [(1,1,0),(1,1,1),(1,1,2),(2,3,2),(2,3,4),(1,2,3), (3,1,sp.Rational(8,3))]:
    P=sp.Poly(poly.subs({g:gg,D:dd}),r)
    n= len([x for x in sp.nroots(P,maxsteps=100) if abs(float(sp.im(x)))<1e-9 and float(sp.re(x))>1e-10])
    assert n==int(bool(4*dd**2>3*gg**2))
    checks+=1
print('PASS: exact symbolic identities, independent resolvents, stationary matrix systems, and root counts. Checks:',checks)
