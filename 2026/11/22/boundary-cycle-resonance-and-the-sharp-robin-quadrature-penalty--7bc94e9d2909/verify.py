"""Exact arithmetic checks for the boundary quadrature resonance theorem.
Numerical/finite checks supplement the analytic proof in RESULT.md.
"""
import sympy as S

x,y,eps,lam,t = S.symbols('x y eps lam t',real=True)
phi=S.Matrix([(1-x)*(1-y),x*(1-y),(1-x)*y,x*y])
v=S.Matrix([1,-1,-1,1]); checks=0
K=S.Matrix(4,4,lambda i,j:S.integrate(S.integrate(S.diff(phi[i],x)*S.diff(phi[j],x)+S.diff(phi[i],y)*S.diff(phi[j],y),(x,0,1)),(y,0,1)))
M=S.Matrix(4,4,lambda i,j:S.integrate(S.integrate(phi[i]*phi[j],(x,0,1)),(y,0,1)))
F=M*v
assert K*v==S.Rational(2,3)*v; checks+=1
assert F==v/36; checks+=1
C=S.Matrix.vstack(phi.subs({x:S.Rational(1,2)+eps,y:0}).T,phi.subs({x:1,y:S.Rational(1,2)}).T,phi.subs({x:S.Rational(1,2),y:1}).T,phi.subs({x:0,y:S.Rational(1,2)}).T)
assert S.factor(C.det())==eps/4;checks+=1
assert C.subs(eps,0)*v==S.zeros(4,1);checks+=1
assert (K*v).dot(v)==S.Rational(8,3);checks+=1
assert v.dot(F)==S.Rational(1,9);checks+=1
edge0=S.integrate((phi.subs(y,0)*phi.subs(y,0).T),(x,0,1))
edge1=S.integrate((phi.subs(x,1)*phi.subs(x,1).T),(y,0,1))
edge2=S.integrate((phi.subs(y,1)*phi.subs(y,1).T),(x,0,1))
edge3=S.integrate((phi.subs(x,0)*phi.subs(x,0).T),(y,0,1))
Bex=edge0+edge1+edge2+edge3
assert Bex*v==v/3;checks+=1
assert S.simplify((K+lam*Bex)*(v/(12*(2+lam)))-F)==S.zeros(4,1);checks+=1
assert (K+lam*(C.subs(eps,0).T*C.subs(eps,0)))*(v/24)==F;checks+=1
B=C.T*C
Q=K+lam*B
u=S.simplify(Q.inv()*F)
lim=S.Matrix([S.limit(ui.subs(lam,t/eps**2),eps,0,dir='+') for ui in u])
assert S.simplify(lim-v/(24+9*t))==S.zeros(4,1);checks+=1
for ei in [S.Rational(1,7),S.Rational(-2,7),S.Rational(1,12)]:
 for li in [S.Rational(1,2),2,5,29]:
  Qei=Q.subs({eps:ei,lam:li});ui=u.subs({eps:ei,lam:li})
  assert S.simplify(Qei*ui-F)==S.zeros(4,1);checks+=1
for n in range(3,17):
 for changed in [False,True]:
  ts=[S.Rational(1,2)]*n
  if changed:ts[0]=S.Rational(1,3)
  D=S.zeros(n)
  for j,a in enumerate(ts):D[j,j]=1-a;D[j,(j+1)%n]=a
  rank=n-(1 if n%2==0 and not changed else 0)
  assert D.rank()==rank;checks+=1
for n in range(3,17):
 ts=[S.Rational(1,3),S.Rational(2,3)]+[S.Rational(1,2)]*(n-2)
 D=S.zeros(n)
 for j,a in enumerate(ts):D[j,j]=1-a;D[j,(j+1)%n]=a
 # paired nonmidpoint nodes produce resonant even cycle only
 assert D.rank()==n-(1 if n%2==0 else 0);checks+=1
print('VERIFY_OK',checks)
