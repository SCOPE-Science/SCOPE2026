"""Exact checks of a two-community predator–prey Turing pitchfork theorem.
Requires sympy. Run: python verify.py
This checks algebraic certificates; local bifurcation implications follow from
analytic center-manifold and implicit-function theorems.
"""
import sympy as S

R=S.Rational
u,v,z=S.symbols('u v z')
xx=(u,v)
U,V=R(1,5),R(14,25)
F=S.Matrix([
 R(1,5)*u*u*(1-u)/(u+R(1,5))-R(1,5)*u*v/(1+2*u),
 2*u*v/(1+2*u)-R(4,7)*v*v/(R(14,25)+v)
])
P={u:U,v:V}
assert F.subs(P)==S.zeros(2,1)
J=F.jacobian(xx).subs(P)
assert J==S.Matrix([[R(3,70),-R(1,35)],[R(4,7),-R(1,7)]])
assert S.trace(J)==-R(1,10) and J.det()==R(1,98)
D0=S.diag(R(151,47880),R(151,1680))
tau=S.symbols('tau')
q=S.symbols('q')
pol=S.factor((J-q*tau*D0).det())
assert S.simplify(pol-D0.det()*(q*tau-R(900,151))*(q*tau-R(912,151)))==0

# Graph K_{3,3}: negative graph Laplacian has eigenvalues 0,3,6.
L=S.zeros(6)
for i in range(3):
 for j in range(3,6):
  L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
assert L.eigenvals()=={S.Integer(0):1,S.Integer(3):4,S.Integer(6):1}

# Derivative tensors, independently compared with directly expanded rational reactions.
def B(a,b):
 return S.Matrix([sum(S.diff(F[k],xx[i],xx[j]).subs(P)*a[i]*b[j]
 for i in range(2) for j in range(2)) for k in range(2)])
def C(a,b,c):
 return S.Matrix([sum(S.diff(F[k],xx[i],xx[j],xx[h]).subs(P)*a[i]*b[j]*c[h]
 for i in range(2) for j in range(2) for h in range(2)) for k in range(2)])

cases=[
 (R(150,151),S.Matrix([R(19,16),1]),S.Matrix([-R(95,4),1]),
  S.Matrix([-R(15849,17920),-R(17949,4480)]),R(151,731220),R(97752677,6114949120)),
 (R(152,151),S.Matrix([R(6,5),1]),S.Matrix([-24,1]),
  S.Matrix([-R(1499,1750),-R(13917,3500)]),-R(151,739480),-R(1844319,476770000))]
checks=0
for t,r,l,m,slope,cubic in cases:
 M=J-6*t*D0
 assert M*r==S.zeros(2,1);checks+=1
 assert (l.T*M)==S.zeros(1,2);checks+=1
 assert S.simplify(J*m+B(r,r)/2)==S.zeros(2,1);checks+=1
 assert S.simplify((l.T*(-6*D0)*r)[0]/(l.T*r)[0]-slope)==0;checks+=1
 assert S.simplify((l.T*(C(r,r,r)/6+B(r,m)))[0]/(l.T*r)[0]-cubic)==0;checks+=1
 assert S.trace(M)<0 and M.det()==0;checks+=1
 # The other 10 eigenvalues are strictly in the left half-plane.
 M3=J-3*t*D0
 assert S.trace(M3)<0 and M3.det()>0;checks+=1
 # A second exact check: extract cubic coefficients directly from F(z+a r+a^2 m).
 plus={u:U+z*r[0]+z*z*m[0],v:V+z*r[1]+z*z*m[1]}
 minus={u:U-z*r[0]+z*z*m[0],v:V-z*r[1]+z*z*m[1]}
 diff=(F.subs(plus)-F.subs(minus))/2
 cubic_direct=S.Matrix([S.expand(S.series(w,z,0,4).removeO()).coeff(z,3) for w in diff])
 assert S.simplify((l.T*cubic_direct)[0]/(l.T*r)[0]-cubic)==0;checks+=1
assert cases[0][4]>0 and cases[0][5]>0
assert cases[1][4]<0 and cases[1][5]<0
print('VERIFY_OK',checks,'exact identities; signs and full graph spectrum confirmed')
