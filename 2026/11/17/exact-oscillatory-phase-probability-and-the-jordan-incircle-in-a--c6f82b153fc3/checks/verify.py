from fractions import Fraction as F
from itertools import product
from math import pi,sqrt

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,v):return [sum(A[i][j]*v[j] for j in range(3)) for i in range(3)]
def add(A,B):return [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)]
def mul(t,A):return [[t*A[i][j] for j in range(3)] for i in range(3)]
def eq(A,B):return A==B
I=[[F(i==j) for j in range(3)] for i in range(3)]
for den in range(3,14):
 for p in range(1,den-1):
  for q in range(1,den-p):
   c=[F(p,den),F(q,den),F(den-p-q,den)]
   x,y,z=c
   B=[[1-y,x,F(0)],[F(0),1-z,y],[z,F(0),1-x]]
   s=x*y+y*z+z*x
   w=[z/s,x/s,y/s]
   P=[[c[i]*w[j] for j in range(3)] for i in range(3)]
   E=add(I,mul(-1,P))
   Q=add(B,mul(-1,P))
   assert mv(B,c)==c
   assert [sum(w[i]*B[i][j] for i in range(3)) for j in range(3)]==w
   assert eq(mm(P,P),P)
   assert eq(mm(B,P),P) and eq(mm(P,B),P)
   assert eq(add(mm(Q,Q),add(mul(-1,Q),mul(s,E))), [[0]*3 for _ in range(3)])
   if s==F(1,4):
    N=add(Q,mul(-F(1,2),E))
    assert eq(mm(N,N),[[0]*3 for _ in range(3)])
    assert N!=[[0]*3 for _ in range(3)]
    for n in range(1,11):
     lhs=I
     for j in range(n):lhs=mm(lhs,B)
     rhs=add(P,add(mul(F(1,2**n),E),mul(F(n,2**(n-1)),N)))
     assert eq(lhs,rhs)
print('FIBER_SPECTRUM_EXACT_OK 3<=den<=13')
R2=F(1,6)
# Polar disk integral: pi*(R^2/27 - R^4/12), times (120/sqrt(3)).
coefficient=F(120)*(R2/F(27)-R2*R2/F(12))
assert coefficient==F(25,54)
print('DIRICHLET_DISK_INTEGRAL_OK',f'{coefficient} * pi/sqrt(3)',float(coefficient)*pi/sqrt(3))
# Direct original QSO at rational c and arbitrary fiber u
c=[F(1,6),F(1,6),F(2,3)]
u=[F(1,12),F(1,18),F(1,2)]
x=sum(([u[i],c[i]-u[i]] for i in range(3)),[])
assert sum(x)==1 and all(t>=0 for t in x)
for n in range(1,11):
 xnew=x[:]
 for i in range(3):
  j=(i+1)%3
  change=x[2*i+1]*x[2*j]-x[2*i]*x[2*j+1]
  xnew[2*i]+=change; xnew[2*i+1]-=change
 x=xnew
 u=[x[0],x[2],x[4]]
 # exact Jordan formula from initial u
 x0=[F(1,12),F(1,18),F(1,2)]
 z,y,t=c
 s=z*y+y*t+t*z
 B=[[1-y,z,F(0)],[F(0),1-t,y],[t,F(0),1-z]]
 w=[t/s,z/s,y/s]
 P=[[c[i]*w[j] for j in range(3)] for i in range(3)]
 E=add(I,mul(-1,P));Q=add(B,mul(-1,P));N=add(Q,mul(-F(1,2),E))
 rhs=mv(add(P,add(mul(F(1,2**n),E),mul(F(n,2**(n-1)),N))),x0)
 assert u==rhs,(n,u,rhs)
print('ORIGINAL_QSO_JORDAN_EXACT_OK steps=10')
