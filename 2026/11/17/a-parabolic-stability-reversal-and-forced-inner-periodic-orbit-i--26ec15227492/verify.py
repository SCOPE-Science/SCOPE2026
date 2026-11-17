"""Reproducible algebraic checks and illustrative finite numerical diagnostics.

Requires Python 3, SymPy and mpmath. Numerical diagnostics do not prove
asymptotic signs or existence of periodic orbits.
"""
import sympy as s
import mpmath as mp

x,y,t,z=s.symbols('x y t z',real=True)
p=-y
q=x+t*y*(x*x+y*y-1)*(x+y)
assert s.expand(2*x*p+2*y*q-2*t*(x*x+y*y-1)*y*y*(x+y)) == 0
th=s.symbols('th',real=True)
si,co=s.sin(th),s.cos(th)
B=si+co
H=s.Rational(2,3)*si**3+2*(-co+co**3/s.Integer(3)+s.Rational(2,3))
assert s.trigsimp(s.diff(H,th)-2*si**2*B)==0
assert s.simplify(H.subs(th,0))==0
assert s.simplify(H.subs(th,2*s.pi))==0
assert s.simplify(H.subs(th,3*s.pi/4)-(s.Rational(4,3)+s.sqrt(2)))==0
assert s.simplify(s.diff(H,th,2).subs(th,3*s.pi/4)+s.sqrt(2))==0
assert s.simplify(s.integrate(si**3*co*B**2,(th,0,2*s.pi))-s.pi/4)==0
C=1+z
numerator=2*t*z*C**s.Rational(3,2)*si**2*B
denominator=1+t*z*s.sqrt(C)*si*co*B
expansion=s.series(numerator/denominator,z,0,3).removeO().expand()
L=2*t*si**2*B
Q=3*t*si**2*B-2*t*t*si**3*co*B**2
assert s.simplify(expansion-z*L-z*z*Q)==0
phi=3*s.pi/4
A=-2*si**3*co*B**2
assert s.simplify(A.subs(th,phi))==0
assert s.simplify(s.diff(A,th).subs(th,phi))==0
assert s.simplify(s.diff(A,th,2).subs(th,phi)-2)==0
mp.mp.dps=45
hm=lambda w:mp.mpf(2)/3*mp.sin(w)**3+2*(-mp.cos(w)+mp.cos(w)**3/3+mp.mpf(2)/3)
amp=lambda w:-2*mp.sin(w)**3*mp.cos(w)*(mp.sin(w)+mp.cos(w))**2
def K(v):
    return v*v*mp.quad(lambda w:amp(w)*mp.exp(v*hm(w)),[0,mp.pi/2,3*mp.pi/4,mp.pi,3*mp.pi/2,2*mp.pi])
assert K(mp.mpf('0.2'))<0
assert K(mp.mpf('12'))>0
assert abs(K(mp.mpf('0.02'))/(-mp.pi*mp.mpf('0.02')**2/2)-1)<mp.mpf('0.04')
print('KUKLES_PARABOLIC_EXACT_IDENTITIES_AND_DIAGNOSTICS_OK')
