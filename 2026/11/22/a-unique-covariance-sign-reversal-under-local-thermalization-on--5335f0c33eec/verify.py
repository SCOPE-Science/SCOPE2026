#!/usr/bin/env python3
"""Exact generator-moment identities for KMP exchange with local baths."""
import sympy as s
n,g,t,d=s.symbols('n g t d', positive=True)
h,c,p,q=s.symbols('H2 C2 HC CC')
mH=t+(1+2*g)*d/(n+2*g)
mC=t+d/(n+2*g)
eqs=[
(n-1)*((h+c+2*p)/3-h)+g*(2*(t+d)**2-h),
((c+h+2*p)/3-c)+(n-2)*((2*c+2*q)/3-c)+g*(2*t**2-c),
(h+c)/6-s.Rational(2,3)*p+(n-2)*(q-p)/2+g*((t+d)*mC+t*mH-2*p),
c/3-s.Rational(2,3)*q+(p-q)+g*(2*t*mC-2*q)]
M,b=s.linear_eq_to_matrix(eqs,[h,c,p,q]); solution=M.inv()*b
P=12*g**4+(4*n+2)*g**3+(-6*n**2-2*n+4)*g**2+(-2*n**3-7*n**2+5*n+2)*g-2*n**3+n**2+n
Q=10*g**3+(18*n-4)*g**2+(11*n**2-5*n-2)*g+2*n**3-n**2-n
D=(n+2*g)**2*(n+3*g)*(12*g**2+11*n*g+2*n**2+n)
assert s.factor(M.det())==g*(n+3*g)*(12*g**2+11*n*g+2*n**2+n)/9
assert s.cancel(solution[2]-mH*mC+d*d*P/D)==0
assert s.cancel(solution[3]-mC*mC-d*d*Q/D)==0
for nn in range(3,8):
 for gg in [s.Rational(1,2),s.Rational(3,2),s.Integer(6)]:
  vals={n:nn,g:gg,t:s.Integer(1),d:s.Integer(3)}
  moments=[s.cancel(v.subs(vals)) for v in solution]
  for eq in eqs:
   assert s.cancel(eq.subs(vals).subs(dict(zip([h,c,p,q], moments))))==0
  assert s.cancel((solution[2]-mH*mC).subs(vals)+s.Integer(9)*P.subs(vals)/D.subs(vals))==0
  assert s.cancel((solution[3]-mC*mC).subs(vals)-s.Integer(9)*Q.subs(vals)/D.subs(vals))==0
print('SYMBOLIC_AND_RATIONAL_MOMENT_IDENTITIES_PASS')
