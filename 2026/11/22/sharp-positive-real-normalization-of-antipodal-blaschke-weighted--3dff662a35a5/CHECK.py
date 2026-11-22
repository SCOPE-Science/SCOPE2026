"""Exact algebraic certificates for a two-zero Bergman kernel half-plane bound.

Requires Python 3 and sympy. This verifies polynomial identities only;
positivity and strictness are justified analytically in RESULT.md.
"""
import sympy as sp

z, eta, t, u, c = sp.symbols('z eta t u c', real=True)
P = (3-t*t)-t*(1+t*t)*(z*z+eta*eta)-2*(1-t*t)**2*z*eta+t*t*(3*t*t-1)*z*z*eta*eta
D = (1-t*z*z)*(1-t*eta*eta)
assert sp.expand(P-(1+t*t)*D-2*(1-t*t)*(1-z*eta)*(1+t*t*z*eta)) == 0
# A rank-two reproducing-kernel subtraction has exactly this numerator.
N = (1+t*t)*(1-t*z*z)**2*(1-t*eta*eta)**2 - (1-t*t)**2*(1-z*eta)**2*((1+t*z*z)*(1+t*eta*eta)+2*(1+t*t)*z*eta)
assert sp.expand(N-(z*z-t)*(eta*eta-t)*P) == 0
# On the torus, with u=cos(alpha+beta) and c=cos(alpha-beta),
# normalized numerator N_T/s and denominator D_T/s have real/imaginary
# parts A=(1-t^2)(u-1), -B=-(1+t^2)sin(theta),
# C=(1+t^2)u-2tc, -E=-(1-t^2)sin(theta).
A=(1-t*t)*(u-1)
B=(1+t*t)
C=(1+t*t)*u-2*t*c
E=(1-t*t)
real_num = sp.expand(A*C+B*E*(1-u*u))
assert sp.expand(real_num-(1-t*t)*(1-u)*(1+t*t+2*t*c)) == 0
assert sp.expand(1+t*t-2*t-(1-t)**2)==0
# Extremal boundary pair and exact polynomial margin.
margin=(1-t)**2*(1+t*t)
assert sp.expand(P.subs({z:1,eta:1})-margin)==0
assert sp.expand(P.subs({z:-1,eta:-1})-margin)==0
assert sp.expand(P.subs({z:1,eta:-1})-margin-4*(1-t*t)**2)==0
# The sharp margin goes quadratically to zero as t tends to one.
assert sp.limit(margin/(1-t)**2,t,1)==2
# Check centered value agrees with the deletion kernel, independently.
assert sp.expand(P.subs({z:0,eta:0})-(3-t*t))==0
print('Eight exact symbolic identities and endpoint checks passed.')
