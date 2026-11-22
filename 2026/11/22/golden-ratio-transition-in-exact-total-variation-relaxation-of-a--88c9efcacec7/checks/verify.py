"""Exact density and finite-time total-variation checks for a piecewise expanding interval map."""
import sympy as S
b=S.symbols('b', positive=True)
L=S.Matrix([[b,0,0],[b,0,1/(1+b)],[0,b,1/(1+b)]])
h=S.Matrix([0,1,1+b])/((1-b)*(1+2*b))
v=S.Matrix([(b-1)*(b+2),b*b+b-1,b*(b+1)])
w=S.Matrix([0,-1,b])
A=-1/((1-b)*(b+2)); B=1/((b+2)*(1+2*b))
assert all(S.simplify(z)==0 for z in L*h-h)
assert all(S.simplify(z)==0 for z in L*v-b*v)
assert all(S.simplify(z)==0 for z in L*w+b/(1+b)*w)
assert all(S.simplify(z)==0 for z in h+A*v+B*w-S.ones(3,1))
weights=S.Matrix([[b*b,b-b*b,1-b]])
assert S.simplify((weights*h)[0]-1)==0
assert S.simplify((weights*v)[0])==0
assert S.simplify((weights*w)[0])==0
for b0 in [S.Rational(1,4),S.Rational(1,2),S.Rational(2,3),S.Rational(7,8)]:
 P=L.subs(b,b0); steady=h.subs(b,b0)
 for n in range(17):
  v_n=P**n*S.ones(3,1); exact=steady+(A*b**n*v+B*(-b/(1+b))**n*w).subs(b,b0)
  assert all(S.simplify(z)==0 for z in v_n-exact)
  d=v_n-steady
  assert d[0]>=0 and d[2]<=0
  tv=S.simplify(S.Rational(1,2)*sum(abs(d[i])*t for i,t in enumerate([b0*b0,b0-b0*b0,1-b0])))
  d1=S.simplify((A*b**n*(b*b+b-1)-B*(-b/(1+b))**n).subs(b,b0))
  formula=b0**(n+2)+(b0-b0*b0)*max(S.S(0),d1)
  assert tv==S.simplify(formula)
 print('all n=0..16 exact rational checks passed for b=',b0)
print('symbolic diagonalization, stationary normalization and sign tests passed')
