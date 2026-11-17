"""Finite illustrations for simultaneous two-dimensional condition-number cancellation.
The general proof, including arbitrary index sets, is in RESULT.md.
"""
from fractions import Fraction as F
import numpy as np

checks=0
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def affine(a,b,C):return [[(a if i==j else 0)+b*C[i][j] for j in range(2)] for i in range(2)]

# Commutative families reduce to a single nonscalar generator.
for u in (F(1),F(3,2),F(5)):
 for v in (F(1),F(4,3),F(7)):
  A=[[F(0),u],[1/u,F(0)]]
  B=[[F(0),v],[1/v,F(0)]]
  X=[[u/v,F(0)],[F(0),F(1)]]
  for a,b in ((F(0),F(1)),(F(2),F(-3)),(F(3,2),F(5,3))):
   assert mul(affine(a,b,A),X)==mul(X,affine(a,b,B))
   checks+=1
  for q in range(1,5):
   XX=np.kron(np.eye(q),np.array(X,dtype=float))
   assert abs(np.linalg.cond(XX)-float(max(u/v,v/u)))<1e-12
   checks+=1

# Noncommuting families: the commutant is scalar, so the entire amplified
# intertwiner space has the form C tensor X.
A=np.array([[0.,1.],[1.,0.]])
H=np.array([[1.,1.],[0.,2.]])
assert np.linalg.norm(A@H-H@A)>0.1
X=np.array([[3.,0.],[0.,1.]])
B=np.linalg.solve(X,A@X)
G=np.linalg.solve(X,H@X)
T=np.linalg.svd(np.vstack([np.kron(np.eye(2),A)-np.kron(A.T,np.eye(2)),np.kron(np.eye(2),H)-np.kron(H.T,np.eye(2))]))[1]
assert np.sum(T>1e-10)==3
checks+=1
rng=np.random.default_rng(44)
for q in range(1,6):
 Z=rng.normal(size=(q,q))+1j*rng.normal(size=(q,q))
 while abs(np.linalg.det(Z))<1e-5:Z+=np.eye(q)
 W=np.kron(Z,X)
 assert np.linalg.norm(np.kron(np.eye(q),A)@W-W@np.kron(np.eye(q),B))<1e-10
 assert np.linalg.norm(np.kron(np.eye(q),H)@W-W@np.kron(np.eye(q),G))<1e-10
 assert abs(np.linalg.cond(W)-np.linalg.cond(Z)*np.linalg.cond(X))<1e-10
 checks+=3
print(f'PASS: {checks} finite exact/numerical tests; universal proof is analytic')
