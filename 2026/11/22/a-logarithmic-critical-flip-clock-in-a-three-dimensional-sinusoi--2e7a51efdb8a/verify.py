"""Exact symbolic check of the five-jet of a critical sine recurrence.

Requires sympy; numerical values are independent diagnostics only.
"""
import math
import sympy as S
b,u=S.symbols('b u',real=True)
a,d=S.symbols('a d')
cs=S.symbols('c0:3')
ds=S.symbols('d0:3')
e=S.Matrix([1,-1,1]);ell=S.Matrix([[-b,0,1]])/(1-b)
J=S.Matrix([[0,1,0],[0,0,1],[b,b,-1]])
H=e*u+S.Matrix(cs)*u**3+S.Matrix(ds)*u**5
f=-u+a*u**3+d*u**5
Hof=S.Matrix([S.series(H[i].subs(u,f),u,0,7).removeO().expand() for i in range(3)])
F=J*H+S.Matrix([0,-H[2]**3/6+H[2]**5/120,H[2]**3/6-H[2]**5/120])
F=S.Matrix([S.series(F[i],u,0,7).removeO().expand() for i in range(3)])
eq3=[S.expand(Hof[i]-F[i]).coeff(u,3) for i in range(3)]+[(ell*S.Matrix(cs))[0]]
s3=S.solve(eq3,[*cs,a],dict=True)
assert len(s3)==1
s3=s3[0]
assert S.simplify(s3[a]-1/(6*(1-b)))==0
eq5=[S.simplify(S.expand(Hof[i]-F[i]).coeff(u,5).subs(s3)) for i in range(3)]+[(ell*S.Matrix(ds))[0]]
s5=S.solve(eq5,[*ds,d],dict=True)
assert len(s5)==1
s5=s5[0]
assert S.simplify(s5[d]-(9*b*b+12*b-1)/(120*(1-b)**3))==0
assert S.simplify((3*s3[a]**2+2*s5[d])/(2*s3[a])-(9*b*b+7*b+4)/(20*(1-b)**2))==0
assert S.simplify((ell*e)[0]-1)==0
assert S.factor(J.charpoly().as_expr()-(S.Symbol('lambda')+1)*(S.Symbol('lambda')**2-b))==0
print('Exact center invariance and reciprocal-clock identities: PASS')
for bv in [S.Rational(1,10), S.Rational(1,4), S.Rational(1,2)]:
 bb=float(bv); x,y,z=.015,-.015,.015
 A=1/(3*(1-bb)); B=(9*bb*bb+7*bb+4)/(20*(1-bb)**2)
 records=[]
 for n in range(1,160001):
  x,y,z=y,math.sin(z),bb*(x+y)-math.sin(z)
  if n in (40000,80000,160000):
   amp=(z-bb*x)/(1-bb)
   records.append((n,round(n*amp*amp,7),round(1/(amp*amp)-A*n-B*math.log(n),5)))
 assert records[-1][1] >0
 print('Finite trajectory diagnostic b=',bb,'n, nU², centered clock:',records)
print('Checker finished; finite trajectory diagnostics are not infinite proofs.')
