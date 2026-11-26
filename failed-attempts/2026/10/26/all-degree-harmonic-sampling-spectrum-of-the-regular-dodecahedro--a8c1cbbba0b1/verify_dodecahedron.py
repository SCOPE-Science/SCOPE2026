#!/usr/bin/env python3
"""Exact verification of the finite calculation in the dodecahedral harmonic theorem.
Runs under Python 3 with standard library only. There is no input dataset.
"""
from fractions import Fraction as Q
from math import pi, sqrt
from itertools import product

# Field K = Q(sqrt(5)), encoded as (rational, rational).
def C(a=0,b=0): return (Q(a),Q(b))
def plus(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def times(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def divq(x,q):return (x[0]/q,x[1]/q)
def dot(x,y):
 out=C()
 for i in range(3):out=plus(out,times(x[i],y[i]))
 return divq(out,3)

one=C(1); zero=C(); phi=C(Q(1,2),Q(1,2)); invphi=C(Q(-1,2),Q(1,2))
pts=[]
for a,b,c in product((-1,1),repeat=3):pts.append([C(a),C(b),C(c)])
for a,b in product((-1,1),repeat=2):
 pa=times(C(a),invphi);pb=times(C(b),phi)
 pts.extend([[zero,pa,pb],[pa,pb,zero],[pb,zero,pa]])
assert len(pts)==20
# The representative of each opposite pair has its first nonzero coordinate positive.
reps=[]
for p in pts:
 for x in p:
  if x!=zero:
   if x[0] > 0 or x[0]==0 and x[1]>0:reps.append(p)
   break
assert len(reps)==10

Au=[[0]*10 for _ in range(10)]; Av=[[0]*10 for _ in range(10)]
Bu=[[0]*10 for _ in range(10)]; Bv=[[0]*10 for _ in range(10)]
for i in range(10):
 for j in range(10):
  if i==j:continue
  d=dot(reps[i],reps[j]);
  if d==C(Q(1,3)):Au[i][j]=1;Bu[i][j]=1
  elif d==C(Q(-1,3)):Au[i][j]=1;Bu[i][j]=-1
  elif d==C(0,Q(1,3)):Av[i][j]=1;Bv[i][j]=1
  elif d==C(0,Q(-1,3)):Av[i][j]=1;Bv[i][j]=-1
  else:raise AssertionError(('unexpected inner product',i,j,d))

def prod(X,Y):return [[sum(X[i][k]*Y[k][j] for k in range(10)) for j in range(10)] for i in range(10)]
for i in range(10):
 assert sum(Au[i])==6 and sum(Av[i])==3
 for j in range(10):
  assert prod(Bu,Bu)[i][j]==6*(i==j)-Bu[i][j]
  assert prod(Bv,Bv)[i][j]==Bu[i][j]+3*(i==j)
  assert prod(Bu,Bv)[i][j]==2*Bv[i][j]
  assert prod(Av,Av)[i][j]==2*(i==j)-Av[i][j]+1
print('EXACT_GEOMETRIC_SCHEME_IDENTITIES_PASS')

N=186
# Recurrences in K for the Legendre polynomial at 1/3 and sqrt(5)/3.
q=[Q(1),Q(1,3)]; z=[C(1),C(0,Q(1,3))]
for ell in range(1,N):
 q.append(((2*ell+1)*q[ell]/3-ell*q[ell-1])/(ell+1))
 z.append(divq(plus(times(C((2*ell+1)), times(C(0,Q(1,3)), z[ell])),neg(times(C(ell),z[ell-1]))),ell+1))
zeros=[]; minpos=(Q(1000),None)
for ell in range(N):
 u=q[ell]
 if ell%2==0:
  assert z[ell][1]==0
  v=z[ell][0]
  eigen=[1+6*u+3*v,1+u-2*v,1-2*u+v];mult=[1,4,5]
 else:
  assert z[ell][0]==0
  w=5*z[ell][1]
  eigen=[1-3*u,1+2*u-w,1+2*u+w];mult=[4,3,3]
 assert min(eigen)>=0,(ell,eigen)
 rank=sum(m for e,m in zip(eigen,mult) if e!=0)
 if rank<10:zeros.append((ell,rank))
 for e in eigen:
  if e>0 and e<minpos[0]:minpos=(e,ell)
assert zeros==[(0,1),(1,3),(2,5),(3,7),(4,9),(5,6),(8,9),(14,9)]
# Upper bound |P_l(x)| <= sqrt(pi/(2*l*(1-x^2))) gives worst-case
# 6|P_l(1/3)|+3|P_l(sqrt(5)/3)| <= sqrt(pi/l)*(9/2+9/sqrt(8)).
# pi<22/7, sqrt(8)>707/250, yield a purely rational bound for l>=186.
assert Q(22,7)*(Q(9,2)+Q(2250,707))**2 < 186
print('EXACT_LEGENDRE_COEFFICIENT_SIGN_TESTS_PASS',N,'degrees')
print('RANK_EXCEPTIONS',zeros)
print('LOWEST_NONZERO_EIGENVALUE_OVER_0_TO_185',float(minpos[0]),'at degree',minpos[1])
print('ANALYTIC_TAIL_CERTIFICATE_PASS', 'ell>=186')
print('ALL_CHECKS_PASS')
