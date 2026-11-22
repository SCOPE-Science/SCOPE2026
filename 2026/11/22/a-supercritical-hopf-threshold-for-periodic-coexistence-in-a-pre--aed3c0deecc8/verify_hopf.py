"""Exact symbolic check for a positive-payoff three-population Hopf bifurcation.
Requires Python 3 and SymPy; no external data.
"""
import sympy as S
I=S.I
x,P,Y,k=S.symbols('x P Y k',real=True)
MR=S.Matrix([[S.Rational(13,8),S.Rational(9,8)],[S.Rational(9,8),S.Rational(5,8)]])
MP=S.Matrix([[1,S.Rational(3,2)],[S.Rational(1,2),1]])
fA=MR[0,0]*x+MR[0,1]*(1-x)
fB=MR[1,0]*x+MR[1,1]*(1-x)
gA=MP[0,0]*x+MP[0,1]*(1-x)
gB=MP[1,0]*x+MP[1,1]*(1-x)
r=S.expand(x*fA+(1-x)*fB)
delta=S.expand(x*gA+(1-x)*gB)
assert S.simplify(r-(S.Rational(5,8)+x))==0
assert delta==1
assert S.simplify(fA-fB-S.Rational(1,2))==0
assert S.simplify(gA-gB-S.Rational(1,2))==0
flow=S.Matrix([x*(1-x)*((fA-fB)-(gA-gB)*Y),
               P*(r-k*P-delta*Y),Y*(delta*P-1)])
assert S.simplify(flow-S.Matrix([x*(1-x)*(1-Y)/2,
 P*(S.Rational(5,8)+x-k*P-Y),Y*(P-1)]))==S.zeros(3,1)
xe=S.Rational(3,8)+k
assert flow.subs({x:xe,P:1,Y:1}).applyfunc(S.simplify)==S.zeros(3,1)
J=flow.jacobian([x,P,Y]).subs({x:xe,P:1,Y:1}).applyfunc(S.simplify)
lam=S.symbols('lam')
expected=lam**3+k*lam**2+lam+xe*(1-xe)/2
assert S.expand(J.charpoly(lam).as_expr()-expected)==0
kh=S.Rational(1,8)
assert S.expand(expected.subs(k,kh)-(lam+kh)*(lam**2+1))==0
assert S.simplify(k-xe*(1-xe)/2-(k-kh)-(k-kh)**2/2)==0
# Derivative of the complex eigenvalue at k = 1/8.
char=expected
lamprime=S.simplify(-S.diff(char,k).subs({k:kh,lam:I})/
                      S.diff(char,lam).subs({k:kh,lam:I}))
assert lamprime==-S.Rational(32,65)-S.Rational(4,65)*I
# Exact multilinear forms at critical equilibrium in centered coordinates.
X,U,V=S.symbols('X U V',real=True)
Z=S.Matrix([X,U,V]); F=flow.subs({x:X+S.Rational(1,2),P:U+1,Y:V+1,k:kh}).expand()
J0=F.jacobian(Z).subs({X:0,U:0,V:0})
assert J0==S.Matrix([[0,0,-S.Rational(1,8)],[1,-S.Rational(1,8),-1],[0,1,0]])
q=S.Matrix([I/8,I,1]); left=S.Matrix([(-32-4*I)/65,(4-32*I)/65,S.Rational(1,2)])
assert J0*q==I*q
assert (left.T*J0-I*left.T).applyfunc(S.simplify)==S.zeros(1,3)
assert S.simplify((left.T*q)[0])==1
zero={X:0,U:0,V:0}
def B(a,b):
 return S.Matrix([sum(S.diff(F[ii],Z[j],Z[l]).subs(zero)*a[j]*b[l]
  for j in range(3) for l in range(3)) for ii in range(3)])
def C(a,b,c):
 return S.Matrix([sum(S.diff(F[ii],Z[j],Z[l],Z[m]).subs(zero)*a[j]*b[l]*c[m]
  for j in range(3) for l in range(3) for m in range(3)) for ii in range(3)])
qb=S.conjugate(q)
assert B(q,qb)==S.zeros(3,1)
G=S.simplify((left.T*(C(q,q,qb)-2*B(q,J0.inv()*B(q,qb))+
 B(qb,(2*I*S.eye(3)-J0).inv()*B(q,q))))[0])
assert G==-S.Rational(369,33410)-S.Rational(521107,801840)*I
l1=S.simplify(S.re(G)/2)
assert l1==-S.Rational(369,66820)<0
print('PASS: payoff derivation, equilibrium for all nearby k, exact cubic, transversal Hopf, normalized eigenvectors, multilinear Lyapunov coefficient')
print('G =',G,'l1 =',l1,'d(lambda)/dk =',lamprime)
