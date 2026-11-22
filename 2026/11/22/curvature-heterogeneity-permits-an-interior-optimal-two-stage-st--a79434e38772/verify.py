"""Exact symbolic checks for the two-component affine extragradient coupling example.
Run with: python verify.py (requires SymPy)."""
import sympy as s
u = s.symbols('u', real=True)
eta = s.Rational(3,10)
a=(s.Integer(1),s.Integer(3))
b=(-s.Integer(3),s.Integer(3)) # F_i(x) = a_i*x+b_i
A=s.Matrix(2,2,lambda i,j: 1-eta*a[j]+eta**2*a[i]*a[j])
B=s.Matrix(2,2,lambda i,j: eta**2*a[j]*b[i]-eta*b[j])
assert A == s.Matrix([[s.Rational(79,100),s.Rational(37,100)],[s.Rational(97,100),s.Rational(91,100)]])
assert B == s.Matrix([[s.Rational(63,100),s.Rational(-171,100)],[s.Rational(117,100),s.Rational(-9,100)]])
p=s.Matrix([[u/2,(1-u)/2],[(1-u)/2,u/2]])
def moment(expr):
    return s.factor(sum(p[i,j]*expr(A[i,j],B[i,j]) for i in range(2) for j in range(2)))
EA=moment(lambda a,b:a)
EB=moment(lambda a,b:b)
EA2=moment(lambda a,b:a*a)
EAB=moment(lambda a,b:a*b)
EB2=moment(lambda a,b:b*b)
assert s.simplify(EA-(67+18*u)/100)==0
assert s.simplify(EB-s.Rational(27,100)*(2*u-1))==0
assert s.simplify(EA2-(5389+1872*u)/10000)==0
assert s.simplify(EAB-s.Rational(27,10000)*(93-16*u))==0
assert s.simplify(EB2-s.Rational(81,2000)*(53-48*u))==0
mu=s.factor(EB/(1-EA))
risk=s.factor((2*EAB*mu+EB2)/(1-EA2))
assert s.simplify(mu-9*(2*u-1)/(11-6*u))==0
assert s.factor(risk-27*(1248*u*u-3018*u+2357)/((11-6*u)*(1537-624*u)))==0
D=s.factor(s.diff(risk,u))
assert s.factor(D+2592*(91416*u*u-255736*u+136569)/((11-6*u)**2*(1537-624*u)**2))==0
p0=91416*u*u-255736*u+136569
assert p0.subs(u,0)>0 and p0.subs(u,1)<0
assert s.diff(p0,u).subs(u,1)<0
roots=s.solve(p0,u)
root=[r for r in roots if 0<float(r)<1][0]
assert s.simplify(root - (s.Rational(2459,1758)-s.sqrt(966408430)/45708))==0
assert s.simplify(risk.subs(u,root)-(-941795+32*s.sqrt(966408430))/17161)==0
assert s.simplify(risk.subs(u,0)-s.Rational(63639,16907))==0
assert s.simplify(risk.subs(u,s.Rational(1,2))-s.Rational(783,245))==0
assert s.simplify(risk.subs(u,1)-s.Rational(15849,4565))==0
assert all(0<a<1 for a in A)
assert risk.subs(u,root).evalf()<min(float(risk.subs(u,x)) for x in [0,s.Rational(1,2),1])
# Equal slopes: with c1=m+d and c2=m-d, step t = eta*a
# stochastic sign noise t*d*(S_J-t*S_I), with E[S_IS_J]=2u-1.
t,d=s.symbols('t d',positive=True)
variance=s.expand(t*t*d*d*(1+t*t-2*t*(2*u-1)))
assert s.diff(variance,u)==-4*t**3*d**2
print('PASS exact affine map, coupled moments, stationary risk, derivative, unique interior minimizer, comparison, equal-slope rigidity')
print('u_star=',s.N(root,15),'risk_star=',s.N(risk.subs(u,root),15))
print('risk endpoints=',[(str(x),s.N(risk.subs(u,x),12)) for x in [0,s.Rational(1,2),1]])
