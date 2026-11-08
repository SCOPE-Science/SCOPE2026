"""Reproducible exact algebra checks for two-agent quadratic gradient tracking."""
import sympy as S
from fractions import Fraction

v,e,b,d,k=S.symbols('v e b d k', real=True)
z=S.symbols('z')
W=S.Matrix([[(1+v)/2,(1-v)/2],[(1-v)/2,(1+v)/2]])
H=S.diag(1+e,1-e)
M=W.row_join(-b*W).col_join((H*(W-S.eye(2))).row_join(W-b*H*W))
Q=z**3+(b*(1+v)-1-2*v)*z**2+(v*v+2*v-4*b*v+b*b*v*(1-e*e))*z+(-v*v+b*v*(v+1)-b*b*v*(1-e*e))
assert S.simplify(M.charpoly(z).as_expr()-(z-1)*Q)==0
ac=S.Poly(Q,z).all_coeffs()
a,B,c=ac[1:]
F=S.expand(1-B+a*c-c*c)
G=S.expand(1-a+B-c)
P=S.expand(1+a+B+c)
assert S.simplify(P-b*(1-v)**2)==0
assert S.expand(Q.subs(v,1)-(z-1)*(z+b*(1-e)-1)*(z+b*(1+e)-1))==0
for vv,expected,cert in [
 (S.Rational(1,2), z**3-z**2/S.Integer(5)-S.Rational(61,100)*z+S.Rational(11,100), [S.Rational(3,10),S.Rational(12,25),S.Rational(15759,10000),S.Rational(111,100),S.Rational(89,100)]),
 (-S.Rational(1,2),z**3+S.Rational(3,5)*z**2+S.Rational(111,100)*z-S.Rational(1,100),[S.Rational(27,10),S.Rational(38,25),-S.Rational(1161,10000),S.Rational(99,100),S.Rational(101,100)])]:
 sub={v:vv,e:S.Rational(1,2),b:S.Rational(6,5)}
 assert S.simplify(Q.subs(sub)-expected)==0
 vals=[P,G,F,1+c,1-c]
 assert [S.factor(i.subs(sub)) for i in vals]==cert
assert [S.simplify(S.diff(i.subs({v:-1+d,b:k*d}),d).subs(d,0)) for i in [F,G,1+c]]==[8-4*k,4*k,2]
assert S.simplify(F.subs(v,-1)+b*((1-e*e)**2*b**3-4*(1-e*e)*b+4))==0
assert S.factor(Q.subs({v:-S.Rational(1,2),e:S.Rational(1,2),b:S.Rational(6,5)}).as_poly(z).clear_denoms()[1].as_expr())==100*z**3+60*z**2+111*z-1
assert all((100*t**3+60*t**2+111*t-1)%7!=0 for t in range(7))
# Supplemental grid: each predicted stable point satisfies all four exact strict inequalities.
checks=0
for ee in [S.Rational(1,5),S.Rational(1,2),S.Rational(4,5)]:
 for t in [S.Rational(1,4), S.Rational(1,10), S.Rational(1,20)]:
  for rr in [S.Rational(1,2),S.Rational(3,4),S.Rational(9,10)]:
   vv=-rr
   bb=S.Rational(1,2)*(1-rr)
   sub={e:ee,v:vv,b:bb}
   assert all(x.subs(sub)>0 for x in [P,G,F,1+c,1-c])
   checks+=1
print('PASS: exact characteristic polynomial, Schur factors, asymptotic coefficients, finite sign-separated witness, modular irreducibility,',checks,'supplemental Schur checks')
