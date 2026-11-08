#!/usr/bin/env python3
from itertools import product

def mm(A,B,p):
 d=len(A)
 return [[sum(A[i][k]*B[k][j] for k in range(d))%p for j in range(d)] for i in range(d)]
def add(A,B,p):return [[(x+y)%p for x,y in zip(a,b)] for a,b in zip(A,B)]
def sub(A,B,p):return [[(x-y)%p for x,y in zip(a,b)] for a,b in zip(A,B)]
def rank(M,p):
 A=[[x%p for x in row] for row in M]
 h=len(A); w=len(A[0]) if h else 0; t=0
 for j in range(w):
  i=next((i for i in range(t,h) if A[i][j]),None)
  if i is None:continue
  A[i],A[t]=A[t],A[i]; c=pow(A[t][j],-1,p); A[t]=[c*x%p for x in A[t]]
  for v in range(h):
   if v!=t and A[v][j]:
    c=A[v][j]; A[v]=[(a-c*b)%p for a,b in zip(A[v],A[t])]
  t+=1
  if t==h:break
 return t

def Jv(v,n,p):return [(-v[i+n])%p if i<n else v[i-n] for i in range(2*n)]
def outer(u,v,p):return [[a*b%p for b in v] for a in u]
def X(u,n,p):return outer(u,Jv(u,n,p),p)
def basisT(u,n,p):
 d=2*n
 if not any(u):
  b=[]
  for i in range(d):
   e=[0]*d;e[i]=1;b.append(X(e,n,p))
  for i in range(d):
   for j in range(i+1,d):
    e=[0]*d;e[i]=1;f=[0]*d;f[j]=1
    b.append(add(outer(e,Jv(f,n,p),p),outer(f,Jv(e,n,p),p),p))
  return b
 b=[]
 for j in range(d):
  e=[0]*d;e[j]=1
  b.append(add(outer(u,Jv(e,n,p),p),outer(e,Jv(u,n,p),p),p))
 return b

def test(n, vecs, p=3):
 r=len(vecs); d=2*n
 Xs=[X(u,n,p) for u in vecs]
 for i in range(r):
  for j in range(i+1,r):
   assert mm(Xs[i],Xs[j],p)==mm(Xs[j],Xs[i],p)
 bs=[basisT(u,n,p) for u in vecs]
 unknown=sum(map(len,bs)); cols=[]
 for i in range(r):
  for B in bs[i]:
   eq=[]
   for a in range(r):
    for b in range(a+1,r):
     v=[[0]*d for _ in range(d)]
     if a==i:v=add(v,sub(mm(B,Xs[b],p),mm(Xs[b],B,p),p),p)
     if b==i:v=add(v,sub(mm(Xs[a],B,p),mm(B,Xs[a],p),p),p)
     eq.extend(sum(v,[]))
   cols.append(eq)
 constraints=list(zip(*cols)) if cols else []
 tangent_dim=unknown-rank(constraints,p)
 active=[u for u in vecs if any(u)]
 s=rank(list(zip(*active)),p) if active else 0
 t=len(active);z=r-t
 predicted=t*(2*n-s)+s*(s+1)//2+z*(2*n-s)*(2*n-s+1)//2
 assert tangent_dim==predicted,(tangent_dim,predicted)
 if r<=n: ambient=2*n*r-r*(r-1)//2
 else:ambient=n*r+n*(n+1)//2
 print('PASS',f'n={n},r={r},t={t},s={s},tangent={tangent_dim},variety_dim={ambient},smooth={tangent_dim==ambient}')

if __name__=='__main__':
 z2=[0]*4;e1=[1,0,0,0];e2=[0,1,0,0];f1=[0,0,1,0]
 for sample in [[e1],[z2],[e1,e1],[e1,e2],[e1,z2],[e1,e2,z2],[e1,e1,e2],[e1,e1,e1],[e1,e1,z2],[z2,z2,z2],[e1,e2,e1,e2],[e1,e2,e1,z2]]:test(2,sample)
 z3=[0]*6;g1=[1,0,0,0,0,0];g2=[0,1,0,0,0,0];g3=[0,0,1,0,0,0]
 for sample in [[g1,g1],[g1,g2],[g1,z3],[g1,g1,g1],[g1,g2,g3],[g1,g1,g2],[g1,g2,g3,z3],[g1,g2,g3,g2]]:test(3,sample)
 print('ALL_SP_RANK_ONE_TANGENTS_PASS')
