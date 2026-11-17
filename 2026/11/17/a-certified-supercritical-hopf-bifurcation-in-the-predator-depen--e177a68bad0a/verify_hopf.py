#!/usr/bin/env python3
"""Exact Sturm and interval-normal-form certificate for the predator-dependent replicator Hopf point."""
import sympy as s
from mpmath import iv
x,p,y,k=s.symbols('x p y k'); beta=2
# Positive payoffs of Cruz and Neves's scenario 8.
a,b,c,d=s.Rational(16,5),s.Rational(3,4),s.Integer(3),s.Rational(4,5)
A,B,C,D=s.Rational(1,2),s.Rational(3,5),s.Rational(7,20),s.Rational(3,10)
fa=a*x+b*(1-x);fb=c*x+d*(1-x)
ga=A*x+B*(1-x);gb=C*x+D*(1-x)
u=s.factor(fa-fb);v=s.factor(ga-gb)
r=s.factor(x*fa+(1-x)*fb);delta=s.factor(x*ga+(1-x)*gb)
m=s.factor(u/v);F=s.factor(r-delta*m);K=s.factor(1/(delta*F))
field=s.Matrix([x*(1-x)*(u-v*y),p*(r-p/k-delta*y),beta*y*(-1+delta*p)])
state=(x,p,y)
JJ=field.jacobian(state)
beq={p:1/delta,y:m,k:K}
J=JJ.subs(beq).applyfunc(s.factor)
D2=[[[s.factor(s.diff(field[i],state[j],state[k]).subs(beq)) for k in range(3)]for j in range(3)]for i in range(3)]
D3=[[[[s.factor(s.diff(field[i],state[j],state[k],state[l]).subs(beq)) for l in range(3)]for k in range(3)]for j in range(3)]for i in range(3)]
A1=s.factor(-s.trace(J))
A2=s.factor(sum(J.extract(I,I).det() for I in [(0,1),(0,2),(1,2)]))
A3=s.factor(-J.det())
H=s.factor(A1*A2-A3)
N=s.Poly(s.together(H).as_numer_denom()[0],x)
low=s.Rational(3381326771974,10**13)
high=s.Rational(3381326771975,10**13)
assert N.eval(low)*N.eval(high)<0
assert s.polys.polytools.count_roots(N,s.Rational(1,5),1)==1
assert s.polys.polytools.count_roots(N,low,high)==1
# Positivity on the entire tiny rational root bracket is checked below by interval arithmetic.
print('EXACT_STURM_OK isolating_interval',low,high)
print('root_count_(1/5,1)',s.polys.polytools.count_roots(N,s.Rational(1,5),1))
# Rational-function interval evaluation, rational coefficients are injected exactly.
iv.dps=45
xlo=iv.mpf(int(low.p))/iv.mpf(int(low.q))
xhi=iv.mpf(int(high.p))/iv.mpf(int(high.q))
X=iv.mpf([xlo.a,xhi.b]);II=iv.mpc(0,1)
def coef_iv(q):
 q=s.Rational(q)
 return iv.mpf(int(q.p))/iv.mpf(int(q.q))
def poly_iv(P):
 out=iv.mpf(0)
 for v in s.Poly(P,x).all_coeffs():out=out*X+coef_iv(v)
 return out
def evaluate(expr):
 num,den=s.fraction(s.cancel(expr))
 return poly_iv(num)/poly_iv(den)
for name,expr in [('a1',A1),('a2',A2),('a3',A3),('Hprime',s.diff(H,x)),('minus_Kprime',-s.diff(K,x)),('positive_y',m),('positive_F',F),('positive_delta',delta),('positive_K',K)]:
 val=evaluate(expr)
 assert val.a > 0,(name,val)
 print('RIGOROUS_POSITIVE',name,val)
def mtxmul(U,V):return [[sum((U[i][k]*V[k][j] for k in range(3)),iv.mpc(0)) for j in range(3)] for i in range(3)]
def mtxvec(U,V):return [sum((U[i][k]*V[k] for k in range(3)),iv.mpc(0)) for i in range(3)]
def solve(U,v):
 # Cramer's rule, with exact outward-rounded interval operations.
 def det(A):return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
 den=det(U)
 return [det([[v[i] if j==k else U[i][j] for j in range(3)] for i in range(3)])/den for k in range(3)]
Jv=[[iv.mpc(evaluate(J[i,j])) for j in range(3)]for i in range(3)]
Bb=[[[evaluate(D2[i][j][k]) for k in range(3)] for j in range(3)] for i in range(3)]
Cc=[[[[evaluate(D3[i][j][k][l]) for l in range(3)] for k in range(3)] for j in range(3)]for i in range(3)]
alpha=evaluate(A1); omega=iv.sqrt(evaluate(A2));
qq=[iv.mpc(1),iv.mpc(0),iv.mpc(0)]
qq[2]=(II*omega-Jv[0][0])/Jv[0][2]
qq[1]=(Jv[1][0]-qq[2])/(-Jv[1][1]+II*omega)
conj=lambda z:iv.mpc(z.real, -z.imag)
qc=[conj(z)for z in qq]
def bil(v,w):return [sum((Bb[i][j][k]*v[j]*w[k] for j in range(3) for k in range(3)),iv.mpc(0))for i in range(3)]
def tri(u,v,w):return [sum((Cc[i][j][k][l]*u[j]*v[k]*w[l] for j in range(3) for k in range(3) for l in range(3)),iv.mpc(0))for i in range(3)]
b1=bil(qq,qc);b2=bil(qq,qq)
aux1=solve(Jv,b1)
aux2=solve([[ (2*II*omega if i==j else iv.mpc(0))-Jv[i][j] for j in range(3)]for i in range(3)],b2)
T=[tri(qq,qq,qc)[i]-2*bil(qq,aux1)[i]+bil(qc,aux2)[i]for i in range(3)]
identity=[[iv.mpc(int(i==j))for j in range(3)]for i in range(3)]
proj=mtxmul([[Jv[i][j]+alpha*identity[i][j] for j in range(3)]for i in range(3)],[[Jv[i][j]+II*omega*identity[i][j] for j in range(3)]for i in range(3)])
cv=mtxvec(proj,T)[0]/((alpha+II*omega)*(2*II*omega))
l1=cv.real/(2*omega)
print('l1 enclosure',l1)
assert l1.b < 0
print('INTERVAL_LYAP_OK negative')
# Exact algebraic data for the scientific statement.
print('H_numerator',s.factor(H))
print('K_of_x',K)
print('J11',s.factor(J[0,0]))
print('K_bracket',s.N(K.subs(x,high),25),s.N(K.subs(x,low),25))
print('VERIFY_OK')
