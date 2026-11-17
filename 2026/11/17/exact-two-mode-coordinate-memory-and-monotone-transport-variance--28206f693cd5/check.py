#!/usr/bin/env python3
"""Symbolic consistency checks for quadratic-base coordinate covariances.
Requires SymPy; no external data or network calls.
"""
import sympy as s
b, t = s.symbols('b t', positive=True); z=s.Symbol('z')
m = b-1/b
M=s.Matrix([[m/b,1/b,m*(m-1)/(2*b**2),0],[1/b,0,m/b**2,0],[0,0,m/b**2,1/b**2],[0,0,1/b**2,0]])
k=b**2/(b**2+1)
h=s.Matrix([k,k/b,0,0])
q=s.Matrix([0,0,k,k/b])
L0=s.Matrix([[1,1/b,s.Rational(1,2),1/(2*b**2)]])
L1=s.Matrix([[s.Rational(1,2),1/(2*b**2),s.Rational(1,3),1/(3*b**3)]])
zero=lambda x: s.cancel(x)==0
assert all(zero(x) for x in M*h-h)
assert zero((L0*h)[0]-1)
mean=s.factor((L0*q)[0]);assert zero(mean-(b+1)*(b**2-b+1)/(2*b*(b**2+1)))
assert zero(M.charpoly(z).as_expr()-(z-1)*(z-1/b)*(z+1/b**2)*(z+1/b**3))
C=[s.factor((L1*M**n*q)[0]-mean**2) for n in range(4)]
A=(b**4-3*b**3+6*b**2-3*b+1)/(12*b**2*(b**2+1))
B=(b-1)**2*(b**2+b+1)/(4*b*(b**2+1)**2)
for n in range(4):assert zero(C[n]-(A*b**(-n)+B*(-b**(-2))**n))
assert zero(C[2]-(1/b-1/b**2)*C[1]-C[0]/b**3)
assert zero(C[3]-(1/b-1/b**2)*C[2]-C[1]/b**3)
V=s.factor(A*(b+1)/(b-1)+B*(b*b-1)/(b*b+1))
Vformula=(b+1)*(b**8-b**6+8*b**4-b**2+1)/(12*b**2*(b-1)*(b**2+1)**3)
assert zero(V-Vformula)
Q=b**11-4*b**10+22*b**8+7*b**7-29*b**6+7*b**5+15*b**4-3*b**2+b-1
assert zero(s.diff(V,b)+Q/(6*b**3*(b-1)**2*(b*b+1)**4))
Qshift=t**11+7*t**10+15*t**9+7*t**8+33*t**7+258*t**6+666*t**5+890*t**4+712*t**3+360*t**2+112*t+16
assert zero(Q.subs(b,t+1)-Qshift)
assert zero((b**4-3*b**3+6*b**2-3*b+1).subs(b,t+1)-(t**4+t**3+3*t**2+4*t+2))
assert zero((b**6-3*b**5+4*b**4-3*b**3+7*b**2-2).subs(b,t+1)-(t**6+3*t**5+4*t**4+3*t**3+7*t**2+12*t+4))
assert s.limit(V,b,s.oo)==s.Rational(1,12)
print('PASS: exact invariant density, all-mode transfer matrix, covariance cancellation, variance, positivity and derivative algebra')
