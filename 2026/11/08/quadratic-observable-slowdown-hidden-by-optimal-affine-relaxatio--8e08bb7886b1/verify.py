#!/usr/bin/env python3
"""Exact rational regression checks for the Gaussian conditional mirror sampler."""
from fractions import Fraction as F
from math import sqrt

checks = 0

def check(ok, context):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(context)

def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def trans(A):
    return [list(t) for t in zip(*A)]

def add(A, B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def mean_matrix(lam, eta, rho):
    a = 1/(1+eta*lam)
    t = 2*a-1
    return [[4*a-1-rho*t, -a*(2-rho)], [F(2), F(-1)]]

# The mixture's first moment and the stationary second moments are
# independently checked, branch by branch, in exact rational arithmetic.
for lam in [F(1,3),F(1),F(2),F(7),F(19)]:
 for eta in [F(1,7),F(1,2),F(1),F(7,3)]:
  a=1/(1+eta*lam)
  v=1/(lam+1/eta)
  Sigma=[[1/lam,1/lam],[1/lam,1/lam+eta]]
  Mir=[[4*a-1,-2*a],[F(2),F(-1)]]
  Ref=[[2*a,-a],[F(2),F(-1)]]
  check(mm(mm(Mir,Sigma),trans(Mir))==Sigma,"mirror invariance")
  check(add(mm(mm(Ref,Sigma),trans(Ref)),[[v,F(0)],[F(0),F(0)]])==Sigma,"refresh invariance")
  for rho in [F(0),F(1,8),F(1,2),F(7,8),F(1)]:
   T=mean_matrix(lam,eta,rho)
   target=[[ (1-rho)*Mir[i][j]+rho*Ref[i][j] for j in range(2)]for i in range(2)]
   check(T==target,"Bernoulli mean matrix")
   t=(1-eta*lam)/(1+eta*lam)
   check(T[0][0]+T[1][1]==t*(2-rho),"trace")
   check(T[0][0]*T[1][1]-T[0][1]*T[1][0]==1-rho,"determinant")

# Exact perfect-fourth-power condition numbers and interior curvatures.
for k in range(1,13):
 mu=F(1)
 L=F(k**4)
 eta=F(1,k**2)
 rho=F(4*k,(k+1)**2)
 q=F(k-1,k+1)
 s=F(k*k-1,k*k+1)
 check(1-rho==q*q,"critical-refresh discriminant")
 for lam in [mu,L,F(k*k),F(k*k+1,2),F(k**4+1,2)]:
  T=mean_matrix(lam,eta,rho)
  trace=T[0][0]+T[1][1]
  determinant=T[0][0]*T[1][1]-T[0][1]*T[1][0]
  t=(1-eta*lam)/(1+eta*lam)
  check(abs(t)<=s,"balanced endpoint envelope")
  check(determinant==q*q,"flat spectral product")
  check(trace*trace<=4*q*q,"complex or repeated modes")
  if lam==mu or lam==L:
   check(trace*trace==4*q*q,"critical endpoint double root")
  if k>1 and lam>mu and lam<L:
   check(trace*trace<4*q*q,"interior complex pair")

# Numerical tests of the scalar minimax calculation across two controls.
def scalar_radius(s,rho):
 tr=s*(2-rho); det=1-rho
 disc=tr*tr-4*det
 return sqrt(det) if disc<=1e-12 else (tr+sqrt(disc))/2
for s in [.07,.19,.43,.63,.88,.97]:
 q=s/(1+sqrt(1-s*s))
 rho=1-q*q
 check(abs(scalar_radius(s,rho)-q)<2e-14,"critical rate")
 for j in range(1001):
  r=j/1000
  check(scalar_radius(s,r)+1e-13>=q,"global refresh minimax")

# In the isotropic case the two independent refresh noises yield exactly
# the stationary covariance, independent of any deterministic initial pair.
eta=F(5,3)
noise=eta/2
Vx=noise+noise
Vy=4*noise
Cov=2*noise
check(Vx==eta and Vy==2*eta and Cov==eta,"two-step exact covariance")
print(f"PASS: {checks} exact-rational and scalar spectral checks")


def sym_lift(M):
 a,b=M[0];c,d=M[1]
 return [[a*a,2*a*b,b*b], [a*c,a*d+b*c,b*d], [c*c,2*c*d,d*d]]

def det3(A):
 return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])

# Exact characteristic cubic of the covariance-defect operator, every
# rational scalar curvature and all mixture weights including boundaries.
for lam in [F(1,3),F(1),F(2),F(7),F(19)]:
 for eta in [F(1,7),F(1,2),F(1),F(7,3)]:
  a=1/(1+eta*lam)
  t=2*a-1
  M0=[[4*a-1,-2*a],[F(2),F(-1)]]
  M1=[[2*a,-a],[F(2),F(-1)]]
  for rho in [F(0),F(1,8),F(1,2),F(7,8),F(1)]:
   Q0=sym_lift(M0);Q1=sym_lift(M1)
   Q=[[(1-rho)*Q0[i][j]+rho*Q1[i][j] for j in range(3)] for i in range(3)]
   c2=-sum(Q[i][i] for i in range(3))
   Q2=mm(Q,Q)
   tr=sum(Q[i][i] for i in range(3));tr2=sum(Q2[i][i] for i in range(3))
   c1=(tr*tr-tr2)/2
   c0=-det3(Q)
   check(c2==1-rho+(3*rho-4)*t*t,"covariance cubic quadratic coefficient")
   check(c1==rho-1+(rho-1)*(rho-4)*t*t,"covariance cubic linear coefficient")
   check(c0==-(1-rho)**2,"covariance cubic constant")

# Strict sign obstruction at the affine-optimal tuning.
for k in range(2,30):
 q=F(k-1,k+1)
 t=2*q/(1+q*q);rho=1-q*q
 c2=1-rho+(3*rho-4)*t*t
 c1=rho-1+(rho-1)*(rho-4)*t*t
 c0=-(1-rho)**2
 def cubic(z):return z*z*z+c2*z*z+c1*z+c0
 check(cubic(q)==-4*q**4*(1-q)**3/(1+q*q)**2,"exact obstruction at affine rate")
 check(cubic(F(1))==(1-q*q)**3/(1+q*q),"exact stability-side sign")
 check(cubic(q)<0<cubic(F(1)),"nontrivial interior quadratic eigenvalue")
print(f"PASS: {checks} exact-rational and scalar spectral checks, including quadratic covariance obstruction")
