"""Exact algebraic verification for a ratio-dependent intraguild predation theorem.
Requires Python 3 and SymPy; no external data or network calls.
"""
import sympy as S
x,y,z,v,w=S.symbols('x y z v w',positive=True)
c,a,m,E,c3,a3,e3,d1,d2=S.symbols('c a m E c3 a3 e3 d1 d2',positive=True)
D=m+(a3-m)*v
L=d1+c3*m*(1-v)/D
G=(m+(e3-m)*v)/D
A=1-x-c*w/(a+w)
B=E*c/(a+w)-L
C=E*c/(a+w)+e3*c3*v/D-d2
F=[x*(1-x)-c*x*(m*y+z)/(a*x+m*y+z),
   y*(E*c*x/(a*x+m*y+z)-c3*z/(a3*y+z)-d1),
   z*(E*c*x/(a*x+m*y+z)+e3*c3*y/(a3*y+z)-d2)]
vals={y:v*w*x/m,z:(1-v)*w*x}
assert all(S.cancel((F[i]/[x,y,z][i]).subs(vals)-[A,B,C][i])==0 for i in range(3))
assert S.factor(S.diff(G,v)-m*(e3-a3)/D**2)==0
assert S.factor(B-C-c3*((d2-d1)/c3-G))==0
vc=S.solve(S.Eq(d2-d1,c3*G),v)[0]
assert S.factor(vc-m*((d2-d1)/c3-1)/(e3-m-((d2-d1)/c3)*(a3-m)))==0
vector=[x*A,v*(1-v)*(B-C),w*(v*B+(1-v)*C-A)]
J=S.Matrix(vector).jacobian((x,v,w))
assert S.factor(J[0,1])==0 and S.factor(J[1,0])==0 and S.factor(J[1,2])==0
assert S.factor(J[1,1].subs({d2:d1+c3*G})-c3*m*v*(1-v)*(a3-e3)/D**2)==0
assert S.factor(J[2,2].subs({x:1-c*w/(a+w),d1:E*c/(a+w)-c3*m*(1-v)/D,d2:E*c/(a+w)+e3*c3*v/D}) + w*c*(E-a)/(a+w)**2)==0
p=S.symbols('lambda')
for aa,ee,dd1,dd2,lead in [(S.Integer(1),S.Integer(2),S.Rational(1,2),S.Integer(2),S.Rational(-1,4)),(S.Integer(2),S.Integer(1),S.Rational(2,3),S.Rational(4,3),S.Rational(1,9))]:
 par={c:S.Rational(1,2),a:S.Rational(1,2),m:1,E:2,c3:1,a3:aa,e3:ee,d1:dd1,d2:dd2}
 pt={x:S.Rational(3,4),y:S.Rational(3,16),z:S.Rational(3,16)}
 assert all(S.cancel(fi.subs(par).subs(pt))==0 for fi in F)
 poly=S.Matrix(F).jacobian((x,y,z)).subs(par).subs(pt).charpoly(p).as_expr()
 assert S.factor(poly-(p-lead)*(p*p+S.Rational(9,8)*p+S.Rational(3,8)))==0
# A completely neutral composition with a positive equilibrium for each 0<v<1.
par={c:S.Rational(1,2),a:S.Rational(1,2),m:1,E:2,c3:1,a3:1,e3:1,d1:S.Rational(1,2),d2:S.Rational(3,2)}
vv=S.symbols('vv',positive=True)
ll=S.factor(L.subs(par).subs(v,vv)); ww=S.factor(S.Rational(1,1)/ll-S.Rational(1,2)); xx=S.factor(1-S.Rational(1,2)*ww/(S.Rational(1,2)+ww))
assert S.factor(ll-(S.Rational(3,2)-vv))==0
assert S.factor(B.subs(par).subs(v,vv).subs(w,ww))==0
assert S.factor(C.subs(par).subs(v,vv).subs(w,ww))==0
assert S.factor(A.subs(par).subs(v,vv).subs({x:xx,w:ww}))==0
print('PASS: exact transformation, frequency law, eigenvalue factorization, two hyperbolic witnesses and neutral continuum')
