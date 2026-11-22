#!/usr/bin/env python3
"""Standalone symbolic and numerical checks for the stated invariant-diagonal formulas."""
import math
import cmath
import sympy as sp
import mpmath as mp

x, y, z, alpha, beta = sp.symbols('x y z alpha beta', real=True)
s = alpha + beta
F = sp.Matrix([
    x + 3*x*(1-x-alpha*y-beta*z),
    y + 3*y*(1-beta*x-y-alpha*z),
    z + 3*z*(1-alpha*x-beta*y-z),
])
q, w = sp.symbols('q w', real=True)
D = sp.simplify(F.jacobian([x,y,z]).subs({x:q,y:q,z:q}))
assert sp.simplify(F[0].subs({x:q,y:q,z:q}) - (4*q-3*(1+s)*q**2)) == 0
assert sp.simplify(((3*(1+s)/4)*(4*q-3*(1+s)*q**2) - 4*w*(1-w)).subs(q,4*w/(3*(1+s)))) == 0
assert all(sp.simplify(D[0,j]-D[1,(j+1)%3])==0 for j in range(3))
assert all(sp.simplify(D[0,j]-D[2,(j+2)%3])==0 for j in range(3))
assert sp.simplify(sum(D[0,j] for j in range(3))-(4-6*(1+s)*q)) == 0
omega = sp.Rational(-1,2)-sp.sqrt(3)*sp.I/2
eta = D[0,0]+D[0,1]*omega+D[0,2]*omega**2
B = 2*(s-2+sp.I*sp.sqrt(3)*(alpha-beta))/(1+s)
assert sp.simplify(sp.expand_complex(eta.subs(q,4*w/(3*(1+s)))-(4*(1-w)+B*w)))==0

mp.mp.dps = 50

def closed(a,b):
    B = mp.mpc(2*(a+b-2)/(1+a+b), 2*mp.sqrt(3)*(a-b)/(1+a+b))
    return 2*mp.log(abs(1+mp.sqrt(B)/2))

def radical(a,b):
    u=2*(a+b-2)/(1+a+b)
    v=2*mp.sqrt(3)*(a-b)/(1+a+b)
    h=mp.sqrt(u*u+v*v)
    return mp.log(1+mp.sqrt((h+u)/2)+h/4)

def quadrature(a,b):
    # theta representation removes arcsine endpoint weights
    B=mp.mpc(2*(a+b-2)/(1+a+b),2*mp.sqrt(3)*(a-b)/(1+a+b))
    f=lambda theta: mp.log(abs(4*mp.cos(theta)**2 + B*mp.sin(theta)**2))
    if abs(a-b)<mp.mpf('1e-30') and a+b<2:
        # split at exact interior zero to avoid automatic-integration failure
        theta0=mp.atan(2/mp.sqrt(-mp.re(B)))
        eps=mp.mpf('1e-22')
        val=mp.quad(f,[0,theta0-eps])+mp.quad(f,[theta0+eps,mp.pi/2])
        assert abs(2*val/mp.pi-closed(a,b)) < mp.mpf('1e-18')
        return
    val=mp.quad(f,[0,mp.pi/2])
    assert abs(2*val/mp.pi-closed(a,b)) < mp.mpf('1e-25')

for a,b in [(mp.mpf('0.4'),mp.mpf('0.4')), (mp.mpf('2'),mp.mpf('2')),
            (mp.mpf('1.5'),mp.mpf('0.5')), (mp.mpf('0.3'),mp.mpf('1.4')),
            (mp.mpf('1'),mp.mpf('1')), (mp.mpf('2.3'),mp.mpf('0.6'))]:
    assert abs(closed(a,b)-radical(a,b))<mp.mpf('1e-42')
    assert abs(closed(a,b)-closed(b,a))<mp.mpf('1e-42')
    quadrature(a,b)
for delta in map(mp.mpf,['0.002','0.01','0.2','1.0','1.8']):
    a,b=1+delta/2,1-delta/2
    special=mp.log(1+mp.sqrt(delta/mp.sqrt(3))+delta/(2*mp.sqrt(3)))
    assert abs(closed(a,b)-special)<mp.mpf('1e-42')
assert closed(mp.mpf(1),mp.mpf(1)) == 0
assert abs(closed(mp.mpf('1.000000005'),mp.mpf('0.999999995'))/mp.sqrt(mp.mpf('1e-8'))-3**(-mp.mpf(1)/4))<mp.mpf('0.0001')
print('VERIFY_OK')
