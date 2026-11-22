"""Exact symbolic check of the quartic Bessel recurrence identity.

Requires sympy. This is a supplementary algebra check, not a proof of
analytic Bessel asymptotics or of uniform high-order moment bounds.
"""
import sympy as sp
r,n,y,z=sp.symbols('r n y z', real=True)
F=r**2*(y**2+z**2)**2/(4*n+2)
# The classical adjacent-order Bessel equations.
yprime=n*y/r-z
zprime=y-(n+1)*z/r
D=sp.diff(F,r)+sp.diff(F,y)*yprime+sp.diff(F,z)*zprime
assert sp.factor(D-r*(y**4-z**4)) == 0
# Leading fixed-order Hankel amplitude: r*(J_n^2+J_{n+1}^2) -> 2/pi.
leading=sp.simplify((sp.Integer(2)/sp.pi)**2/(4*n+2))
assert sp.simplify(leading-2/(sp.pi**2*(2*n+1)))==0
# Exact normalized critical stability coefficient.
t=sp.symbols('t',positive=True)
A=sp.Integer(3)/sp.pi**2
D01=sp.Integer(2)/sp.pi**2
c=sp.simplify((2*sp.pi)**2*sp.Rational(1,2)*D01/sp.sqrt(A))
assert sp.simplify(c-4*sp.pi/sp.sqrt(3))==0
# Rational upper-bound constants from the cited uniform high-mode estimates.
C=sp.Rational(3,125)+sp.Rational(13,55)+sp.Rational(4,25)
assert 0<C<1
print('Symbolic recurrence, critical coefficient, and rational bound checks passed.')
print('High-order additive bound C =',C)
