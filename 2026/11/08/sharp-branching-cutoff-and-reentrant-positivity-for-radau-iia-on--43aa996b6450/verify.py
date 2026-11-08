#!/usr/bin/env python3
"""Exact, independently runnable algebra check for Radau IIA on equal-armed double stars.
Requires SymPy. Run: python verify.py
"""
import sympy as s

h,m=s.symbols('h m', positive=True)
Q=s.Matrix([[m+1,-1,-m,0],[-1,m+1,0,-m],[-1,0,1,0],[0,-1,0,1]])
R=lambda M:(6*s.eye(M.rows)-2*h*M)*(h*h*M*M+4*h*M+6*s.eye(M.rows)).inv()
T=R(Q)
r=(6-2*h)/(h*h+4*h+6)
classes={
 'hub_diag':T[0,0],
 'hub_hub':T[0,1],
 'hub_own_leaf':T[0,2]/m,
 'hub_other_leaf':T[0,3]/m,
 'leaf_diag':T[2,2]/m+(1-1/m)*r,
 'leaf_same_offdiag':(T[2,2]-r)/m,
 'leaf_opposite':T[2,3]/m,
}
classes={k:s.factor(v) for k,v in classes.items()}
assert s.simplify((6-2*h)/(h*h+4*h+6)-(1-h/3)/(1+2*h/3+h*h/6))==0
# Sturm's theorem counts all positive real roots, without numerical root approximations.
checks=0
for M in range(2,6):
 for label,formula in classes.items():
  expr=s.factor(formula.subs(m,M))
  numerator,denominator=s.fraction(expr)
  p=s.Poly(numerator,h)
  # All rational denominators here have strictly positive coefficients and factors.
  den_factors=s.factor_list(denominator)[1]
  for f,exp in den_factors:
   coeffs=s.Poly(f,h).all_coeffs()
   assert all(v>0 for v in coeffs), (M,label,'bad denominator',f)
  if p.eval(0)==0:
   p=s.Poly(s.cancel(p.as_expr()/h**p.terms()[-1][0][0]),h)
  assert p.eval(0)>0,(M,label,'nonpositive first coefficient')
  assert p.LC()>0,(M,label,'nonpositive leading coefficient')
  nroots=p.count_roots(0,s.oo)
  assert nroots==0,(M,label,'positive root count',nroots)
  checks+=1
 print('m =',M,'all seven orbit-entry numerators positive for h>0; Sturm certificates passed')
# Universal counter-witness h=10, all integer m>=6.
f=s.factor(classes['leaf_diag'])
num,den=s.fraction(f)
t=s.symbols('t',nonnegative=True)
shift=s.Poly(s.expand(num.subs({h:10,m:t+6})),t)
assert shift.all_coeffs()==[-420000,-14576000,-183761600,-764053760,-221329592],shift
print('h=10, m=t+6 numerator:',shift.as_expr())
# Direct full-matrix checks, not relying on the equitable 4x4 quotient.
for M in range(2,7):
 n=2*M+2
 L=s.zeros(n)
 edges=[(0,1)]+[(0,2+i) for i in range(M)]+[(1,2+M+i) for i in range(M)]
 for i,j in edges:
  L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
 for step in [s.Rational(1,4),s.Rational(3,2),s.Rational(10)]:
  physical=(6*s.eye(n)-2*step*L)*(step**2*L**2+4*step*L+6*s.eye(n)).inv()
  substitutions={m:M,h:step}
  wanted={'hub_diag':physical[0,0], 'hub_hub':physical[0,1],
          'hub_own_leaf':physical[0,2], 'hub_other_leaf':physical[0,2+M],
          'leaf_diag':physical[2,2], 'leaf_same_offdiag':physical[2,3],
          'leaf_opposite':physical[2,2+M]}
  for label,actual in wanted.items():
   assert s.cancel(classes[label].subs(substitutions)-actual)==0,(M,step,label)
  assert physical*s.ones(n,1)==s.ones(n,1)
print('PASS: 28 exact Sturm root counts, symbolic infinite-family witness, 105 full-matrix comparisons.')
