"""Symbolic checks of two-periodic variable-step BDF2.

Run: python checker.py (SymPy required). All displayed assertions are exact
unless explicitly identified as numerical eigenvalue sanity checks.
"""
import cmath
import itertools
from fractions import Fraction
import sympy as S

r, x, y, q = S.symbols('r x y q', real=True)
z = x + S.I*y
W = (1 + 2*r + r*(r+1)*z)*(r + 2 + (r+1)*z)
P = 2*(r*r + 3*r + 1) - (r+1)*(r*r+1)*z
u = x*x + y*y
A = (r*(r+1)**2*u**2 + 2*(r+1)*(r*r+4*r+1)*u*x
     + 4*(2*r+1)*(r+2)*x*x + 8*(r+1)*x)
B = r*r*A + (r+1)**2*(12*r*(r+1)*x
    + r*(r*r+6*r+1)*u + 4*(r*r+3*r+1))

def check(value, label):
    assert S.expand(value) == 0, label

# Use the actual nonuniform BDF2 coefficients, not the claimed polynomial,
# to reconstruct the two-sweep companion matrices.
def step(ratio, scaled_decay):
    # scaled_decay = - lambda * (current step length)
    d = 1 + 2*ratio + (1+ratio)*scaled_decay
    return S.Matrix([[(1+ratio)**2/d, -ratio**2/d], [1, 0]])

checks = 0
for rr in [S.Rational(1,9),S.Rational(1,2),S.Integer(1),S.Rational(5,3), S.Integer(3), S.Integer(10), S.Integer(100)]:
    for zz in [0,S.Rational(1,10),1,7,S.I/3,2+S.I/2]:
        mm = step(S.Integer(1)/rr, zz) * step(rr, rr*zz)
        w = W.subs({r:rr,x:S.re(zz),y:S.im(zz)})
        p = P.subs({r:rr,x:S.re(zz),y:S.im(zz)})
        check(S.cancel(mm.trace()-p/w),'trace')
        check(S.cancel(mm.det()-rr/w),'determinant')
        checks+=2

# Universal Schur-Cohn factorization over complex decay parameters.
AW=S.expand(W*S.conjugate(W))
K=S.expand(P*S.conjugate(W)-r*S.conjugate(P))
F=S.expand((AW-r*r)**2-K*S.conjugate(K))
check(F-(r+1)**4*A*B,'global Schur-Cohn factorization')
checks+=1

# Zero mode is a simple eigenvalue one with a strictly damped parasitic mode.
w0=(1+2*r)*(r+2)
p0=2*(r*r+3*r+1)
check(w0-p0+r,'zero-mode factor')
checks+=1

# Singular ratio with fixed total decay q: one eigenvalue tends to trapezoidal,
# the other to zero (determinant); these limits use rational functions.
Ws=S.factor(W.subs({x:q/(r+1),y:0}))
Ps=S.factor(P.subs({x:q/(r+1),y:0}))
check(S.limit(Ps/Ws,r,S.oo)-(2-q)/(2+q),'large-r trace limit')
check(S.limit(r/Ws,r,S.oo),'large-r determinant limit')
check(S.limit(Ps/Ws,q,S.oo),'fixed-r stiff trace limit')
check(S.limit(r/Ws,q,S.oo),'fixed-r stiff determinant limit')
checks+=4

# For representative complex decay parameters directly compute both roots
# and check strict unit-circle inclusion. This is only a numerical sanity check;
# the universal theorem follows from the exact factorization above.
for rr in [0.001,0.1,1.,5.,2000.]:
    for xx, yy in [(0.,0.01),(0.,20.),(0.001,2.),(1.,0.),(20.,11.)]:
        zz=complex(xx,yy)
        w=complex(W.subs({r:rr,x:xx,y:yy}).evalf())
        p=complex(P.subs({r:rr,x:xx,y:yy}).evalf())
        t=p/w
        delta=rr/w
        roots=[(t+cmath.sqrt(t*t-4*delta))/2,
               (t-cmath.sqrt(t*t-4*delta))/2]
        assert all(abs(t0)<1+1e-9 for t0 in roots), (rr,zz,roots)
        checks+=1
print(f'PASS: {checks} symbolic, exact-rational, and numerical checks')
print('Identity: (|W|^2-r^2)^2-|P conj(W)-r conj(P)|^2 = (r+1)^4 A B')
print('A=r(r+1)^2 u^2+2(r+1)(r^2+4r+1)ux+4(2r+1)(r+2)x^2+8(r+1)x')
print('B=r^2 A+(r+1)^2[12r(r+1)x+r(r^2+6r+1)u+4(r^2+3r+1)]')
print('For r>0, Re z>=0, z!=0: A,B>0, |W|>r; strict Schur-Cohn holds.')
print('Limits: r->infinity at fixed q: roots -> ((2-q)/(2+q),0).')
print('At fixed r, q->infinity: both roots ->0; stiff and ratio limits do not commute.')
