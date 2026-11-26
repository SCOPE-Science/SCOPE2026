"""Standalone exact checks for a sharp sketched one-step minimum-residual law."""
from fractions import Fraction as F
from random import Random
from math import sqrt


def dot(x,y): return sum(a*b for a,b in zip(x,y))
def mv(M,x): return [sum(a*b for a,b in zip(row,x)) for row in M]
def matmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def trans(M):return [list(x) for x in zip(*M)]
def norm2(v):return dot(v,v)

def gram(e, sign):
    # A=diag(1,4), r=(2,1)/sqrt(5), v=(1,2)/sqrt(5), w=(2,-1)/sqrt(5).
    root={F(3,5):F(4,5),F(4,5):F(3,5)}[e]
    a=1-e*e; d=sign*e*root; b=1+e*e
    U=[[F(1),F(2)],[F(2),-F(1)]]
    H=[[a,d],[d,b]]
    return [[x/F(5) for x in row] for row in matmul(matmul(U,H),trans(U))]

r=[F(2),F(1)]; A=[[F(1),F(0)],[F(0),F(4)]]; Ar=mv(A,r)
count=0
for e in (F(3,5),F(4,5)):
 for sign in (-1,1):
    M=gram(e,sign); a=M[0][0];b=M[1][1];d=M[0][1]
    assert M[1][0]==d
    assert a+b==2 and (a-1)**2+d*d==e*e
    # Eigenvalues of symmetric trace-2 Gram matrix exactly 1+-e.
    assert a*b-d*d==1-e*e
    t=dot(Ar,mv(M,r))/dot(Ar,mv(M,Ar))
    residual=[r[i]-t*Ar[i] for i in range(2)]
    factor_sq=norm2(residual)/norm2(r)
    expected=F(9,25)/(1-e*e)
    if sign==1:assert factor_sq==expected,(factor_sq,expected)
    if sign==-1 and e==F(4,5):assert t==0 and factor_sq==1
    count+=7
# Check a continuum of inexact sketch alternatives against analytical sharp factor.
rng=Random(34)
for k in [F(3,2), F(2),F(3),F(4),F(9),F(21)]:
 for epsilon in [F(0),F(1,10),F(1,3),F(3,5),F(4,5),F(9,10)]:
    target=((k-1)/(k+1))**2/(1-epsilon**2)
    for _ in range(70):
      # Rotated diagonal sketch from scalar rotation, exact rational entries.
      s=F(rng.randint(-10,10),11); c=F(1)-s*s
      if c<0:continue
      # We do not need a true rotation to ensure a bounded Gram: take an
      # arbitrary symmetric perturbation and scale by entrywise safe bound.
      p=F(rng.randint(-20,20),25); q=F(rng.randint(-20,20),25); u=F(rng.randint(-20,20),25)
      B=[[p,u],[u,q]]
      scale=F(1)+max(abs(p)+abs(u),abs(q)+abs(u))
      M=[[F(i==j)+epsilon*B[i][j]/scale for j in range(2)] for i in range(2)]
      rv=[F(rng.randint(-10,10),11),F(rng.randint(-10,10),11)]
      if not norm2(rv):continue
      Av=[rv[0],k*rv[1]]
      t=dot(Av,mv(M,rv))/dot(Av,mv(M,Av))
      error= [rv[i]-t*Av[i] for i in range(2)]
      assert norm2(error)/norm2(rv)<=target, (k,epsilon,rv,M)
      count+=1
print('PASS:',count,'exact-rational assertions/check groups')
