"""Reproduce exact finite current/covariance identities and asymptotic constants for the squared-cycle graph."""
from fractions import Fraction as F
from itertools import combinations
from math import cos, sin, pi, sqrt


def inv(A):
 n=len(A); M=[[F(A[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
 for j in range(n):
  k=next(k for k in range(j,n) if M[k][j]); M[j],M[k]=M[k],M[j]
  t=M[j][j]; M[j]=[a/t for a in M[j]]
  for i in range(n):
   if i!=j:
    t=M[i][j]; M[i]=[M[i][h]-t*M[j][h] for h in range(2*n)]
 return [row[n:] for row in M]

def setup(n):
 edges=[(i,(i+a)%n) for a in (1,2) for i in range(n)]
 A=[[0]*(n-1) for _ in range(n-1)]
 for i,j in edges:
  if i: A[i-1][i-1]+=1
  if j: A[j-1][j-1]+=1
  if i and j:A[i-1][j-1]-=1;A[j-1][i-1]-=1
 B=inv(A)
 vectors=[[F((i==u)-(j==u)) for u in range(1,n)] for i,j in edges]
 K=[[sum(x*B[a][b]*y for a,x in enumerate(v) for b,y in enumerate(w)) for w in vectors] for v in vectors]
 return edges,K

def enumerate_trees(n,edges):
 m=len(edges); cnt=0; s=[0]*m; pairs=[[0]*m for _ in range(m)]
 for I in combinations(range(m),n-1):
  parent=list(range(n))
  def find(x):
   while parent[x]!=x:x=parent[x]
   return x
  good=True
  for a in I:
   u,v=edges[a];x,y=find(u),find(v)
   if x==y:good=False;break
   parent[x]=y
  if not good:continue
  cnt+=1
  for a in I:s[a]+=1
  for a in I:
   for b in I:pairs[a][b]+=1
 return cnt,s,pairs

def numerical(n):
 # work directly with a real current kernel built from the g-periodic identity
 t=(3-sqrt(5))/2; rho=-t
 g=[(rho**r+rho**(n-r))/(sqrt(5)*(1-rho**n)) for r in range(n)]
 def G(r):return g[r%n]
 P0=[[1/5,2/5],[2/5,4/5]]
 # K[a][b][r] with r=j-i
 K=[[[0.0]*n for b in range(2)] for a in range(2)]
 for r in range(n):
  K[0][0][r]=G(r)-1/(5*n)
  K[0][1][r]=G(r)+G(r+1)-2/(5*n)
  K[1][0][r]=G(r)+G(r-1)-2/(5*n)
  K[1][1][r]=2*G(r)+G(r-1)+G(r+1)-4/(5*n)
 p=[K[a][a][0] for a in range(2)]
 def eigen(q):
  w=2*pi*q/n
  cc=[]
  for a in range(2):
   row=[]
   for b in range(2):
    z=complex((p[a] if a==b else 0),0)-sum(K[a][b][r]**2*complex(cos(-r*w),sin(-r*w)) for r in range(n))
    row.append(z)
   cc.append(row)
  assert abs(cc[1][0]-cc[0][1].conjugate())<1e-9
  aa=cc[0][0].real;dd=cc[1][1].real
  rad=sqrt(((aa-dd)/2)**2+abs(cc[0][1])**2)
  return ((aa+dd)/2-rad,(aa+dd)/2+rad)
 return [eigen(q) for q in range(n)],p

def main():
 trials=0
 for n in (5,6,7):
  edges,K=setup(n)
  cnt,s,pairs=enumerate_trees(n,edges)
  # Independent closed-form cyclic Green function agrees with the exact grounded Laplacian inverse.
  t=(3-sqrt(5))/2; rho=-t
  def G(r):
   r=r%n
   return (rho**r+rho**(n-r))/(sqrt(5)*(1-rho**n))
  for a in range(2):
   for b in range(2):
    for i in range(n):
     for j in range(n):
      r=(j-i)%n
      if a==b==0: z=G(r)-1/(5*n)
      elif a==b==1: z=2*G(r)+G(r-1)+G(r+1)-4/(5*n)
      elif a==0: z=G(r)+G(r+1)-2/(5*n)
      else: z=G(r)+G(r-1)-2/(5*n)
      assert abs(float(K[a*n+i][b*n+j])-z)<1e-11,(n,a,b,i,j,z,K[a*n+i][b*n+j])
      trials+=1
  for a in range(2*n):
   assert F(s[a],cnt)==K[a][a];trials+=1
   for b in range(2*n):
    assert F(pairs[a][b],cnt)==K[a][a]*K[b][b]-K[a][b]**2 if a!=b else F(pairs[a][b],cnt)==K[a][a]
    trials+=1
  print('exact',n,'trees',cnt,'marginal short,long',K[0][0],K[n][n])
 for n in (8,10,16,24,40,80,160,320,640):
  spec,p=numerical(n)
  positive=[x for pair in spec for x in pair if x>1e-9]
  lo=min(positive);hi=max(positive)
  print('spectral',n,'n*lambda_min',round(n*lo,9),'lambda_max',round(hi,9),'kappa/n',round(hi/(n*lo),9),'at k=1',spec[1])
  assert abs(sum(p)-(n-1)/n)<1e-9
  assert abs(spec[0][0])<1e-9
  assert lo>0
  trials+=4
 assert abs(numerical(640)[0][1][0]*640-0.5)<0.01
 assert abs(max(x for pair in numerical(640)[0] for x in pair)-4/(5*sqrt(5)))<0.003
 print('Passed',trials,'exact and numerical assertions')
if __name__=='__main__':main()
