from itertools import combinations,product
from math import prod

def rref(A,q):
 A=[list(v) for v in A if any(v)]
 if not A:return []
 n=len(A[0]); k=0
 for c in range(n):
  z=next((i for i in range(k,len(A)) if A[i][c]%q),None)
  if z is None:continue
  A[k],A[z]=A[z],A[k]
  inv=pow(A[k][c],-1,q)
  A[k]=[(v*inv)%q for v in A[k]]
  for i in range(len(A)):
   if i!=k and A[i][c]:
    a=A[i][c]; A[i]=[(u-a*v)%q for u,v in zip(A[i],A[k])]
  k+=1
  if k==len(A):break
 return [tuple(v) for v in A[:k]]

def spaces(d,q):
 for k in range(d+1):
  for pivots in combinations(range(d),k):
   free=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,d) if j not in pivots]
   for coeffs in product(range(q),repeat=len(free)):
    A=[[0]*d for _ in range(k)]
    for i,p in enumerate(pivots):A[i][p]=1
    for (i,j),c in zip(free,coeffs):A[i][j]=c
    yield tuple(map(tuple,A))

def w(u,v,q):
 r=len(u)//2
 return sum(u[i]*v[r+i]-u[r+i]*v[i] for i in range(r))%q

def form_vertices(r,q):
 d=2*r; ans=[]
 for U in spaces(d,q):
  k=len(U)
  if k==d:continue
  ans.append((U,tuple(tuple(v)+(0,) for v in U)+(tuple([0]*d+[1]),)))
  if k and all(w(u,v,q)==0 for u,v in combinations(U,2)):
   for f in product(range(q), repeat=k):
    ans.append((U,tuple(tuple(v)+(c,) for v,c in zip(U,f))))
 return ans

def bracket(a,b,q):
 d=len(a)-1
 return tuple([0]*d + [w(a[:d],b[:d],q)])

def generated_full(A,B,d,q):
 Z=list(rref(tuple(A)+tuple(B),q))
 while True:
  br=[bracket(u,v,q) for u,v in combinations(Z,2)]
  Y=rref(Z+br,q)
  if len(Y)==len(Z):return len(Y)==d+1
  Z=Y

def numerical(r,q):
 d=2*r
 V=form_vertices(r,q)
 print('vertices',r,q,len(V),flush=True)
 E=0
 for i,(U,A) in enumerate(V):
  for W,B in V[i+1:]:
   E+=generated_full(A,B,d,q)
 print('edges',r,q,E,flush=True)
 return len(V),E

def qbinom(n,k,q):
 if not 0<=k<=n:return 0
 return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))

def isotropic_count(r,k,q):
 if not 0<=k<=r:return 0
 return prod(q**(2*r-i)-q**i for i in range(k))//prod(q**k-q**i for i in range(k))

def completions(d,k,q):
 return sum(qbinom(k,s,q)*q**((d-k)*s) for s in range(1,k+1))

def formula(r,q):
 d=2*r
 N=sum(qbinom(d,k,q) for k in range(d))+sum(isotropic_count(r,k,q)*q**k for k in range(1,r+1))
 E0=sum(qbinom(d,k,q)*completions(d,k,q) for k in range(1,d))//2
 E1=sum(isotropic_count(r,k,q)*q**k*completions(d,k,q) for k in range(1,r+1))
 E2=isotropic_count(r,r,q)*q**(r*(r+1)//2+2*r)//2
 return N,E0+E1+E2,(E0,E1,E2)

def check_hyperplanes(r,q):
 d=2*r
 U=list(spaces(d,q)); hs=[v for v in U if len(v)==d-1]
 graph=form_vertices(r,q)
 # Every proper projected subspace admits a hyperplane color. Distinct hyperplanes are adjacent.
 H={v: i for i,v in enumerate(hs)}
 colors=[]
 for v,A in graph:
  opts=[i for i,h in enumerate(hs) if len(rref(list(h)+list(v),q))==d-1]
  assert opts
  colors.append(opts[0])
 assert len(H)==(q**d-1)//(q-1)
 # The whole set of distinct hyperplane vertices is a clique.
 ph=[(v,A) for v,A in graph if len(v)==d-1]
 assert len(ph)==len(H) if r>=2 else len(H)*(q+1)
 for i,(_,A) in enumerate(graph):
  for j in range(i+1,len(graph)):
   if generated_full(A,graph[j][1],d,q):assert colors[i]!=colors[j]
 return len(H)

if __name__=='__main__':
 for r,q in ((1,2),(1,3),(1,5),(2,2),(2,3)):
  expected=formula(r,q)
  actual=numerical(r,q)
  assert actual==expected[:2],(r,q,expected,actual)
  H=check_hyperplanes(r,q)
  print('MATCH',r,q,actual, 'omega=chi',H,'pieces',expected[2],flush=True)
 for r,q in ((3,2),(3,3),(4,2)):
  n,e,c=formula(r,q)
  assert n>0 and 0<=e<=n*(n-1)//2
  print('EXACT_INTEGER',r,q,n,e,c,flush=True)
 print('VERIFY_OK')
