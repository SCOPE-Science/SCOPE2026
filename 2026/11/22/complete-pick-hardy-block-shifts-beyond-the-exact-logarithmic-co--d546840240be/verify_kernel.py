#!/usr/bin/env python3
"""Exact symbolic checks for a two-site analytic reproducing kernel.

Requires Python 3 and SymPy. This tests algebraic identities; the general
positive-kernel and complete-Pick arguments are proved in RESULT.md.
"""
import sympy as s

a, c, b, z, w = s.symbols('a c b z w', real=True)
t = z*w
q = a*c+b*z
qw = a*c+b*w
K = 1 + (c**2*t+t**2/(1-t))/(q*qw)
R = s.expand(q*qw-c**2+(c**2-1)*t)
Q = s.cancel(1-(1-t)*K)
H = s.expand(c**2*R-(c**2-1)*q*qw)
F = s.cancel(1-1/K)
F_certificate = c**2*t/(q*qw)+t**2*H/(q**2*qw**2*(1-Q))
assert s.factor(Q-t*R/(q*qw)) == 0
assert s.factor(F-F_certificate) == 0
R_matrix = s.Matrix([[c**2*(a**2-1),a*c*b],[a*c*b,b**2+c**2-1]])
H_matrix = s.Matrix([[c**2*(a**2-c**2),a*c*b],[a*c*b,b**2+c**2*(c**2-1)]])
D = s.Matrix([[c**2-1,c*b],[c*b,a**2+b**2-1]])
A = s.Matrix([[0,a],[0,0]])
P = s.expand(D+D*D-A.T*D*A)
assert s.factor(R_matrix.det()-c**2*((a**2-1)*(c**2-1)-b**2)) == 0
assert s.factor(H_matrix.det()-c**4*((a**2-c**2)*(c**2-1)-b**2)) == 0
assert s.factor(D.det()-((a**2-1)*(c**2-1)-b**2)) == 0
assert s.factor(P[0,0]-c**2*(b**2+c**2-1)) == 0
assert s.factor(P.det()-a**2*c**2*((a**2-c**2)*(c**2-1)-b**2*c**2)) == 0
point = {a:3,c:2,b:2}
assert D.subs(point) == s.Matrix([[3,4],[4,12]])
assert P.subs(point) == s.Matrix([[28,64],[64,145]])
assert H_matrix.subs(point) == s.Matrix([[20,12],[12,16]])
assert D.subs(point).det() == 20
assert P.subs(point).det() == -36
assert H_matrix.subs(point).det() == 176
print('EXACT_KERNEL_CERTIFICATE_OK: 12 symbolic and rational identities')
