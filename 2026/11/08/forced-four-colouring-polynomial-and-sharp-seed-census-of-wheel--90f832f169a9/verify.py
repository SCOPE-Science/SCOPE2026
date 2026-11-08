from itertools import product, combinations
from collections import Counter

def make_graph(n):
 N=n+1
 adj=[set() for _ in range(N)]
 for i in range(n):
  for j in ((i-1)%n,(i+1)%n,n):
   adj[i].add(j);adj[j].add(i)
 return adj

def forces(vals,adj):
 a=list(vals)
 if any(a[u]==a[v] and a[u]!=-1 for u in range(len(a)) for v in adj[u]): return False
 while -1 in a:
  progress=False
  for i in range(len(a)):
   if a[i]>=0:continue
   present={a[j] for j in adj[i] if a[j]>=0}
   if len(present)==3:
    a[i]=next(iter(set(range(4))-present));progress=True
    break
  if not progress:return False
 return all(a[u]!=a[v] for u in range(len(a)) for v in adj[u])

def direct(n):
 adj=make_graph(n);ctr=Counter();N=n+1
 for vals in product(range(-1,4), repeat=N):
  if forces(vals,adj):ctr[sum(x!=-1 for x in vals)]+=1
 return ctr

def from_described(n):
 ans=Counter()
 for rim in product(range(3),repeat=n):
  if any(rim[i]==rim[(i+1)%n] for i in range(n)):continue
  for Ubits in range(1<<n):
   U={i for i in range(n) if Ubits>>i&1}
   if any((i+1)%n in U for i in U):continue
   if any(rim[(i-1)%n]==rim[(i+1)%n] for i in U):continue
   ans[1+n-len(U)]+=4
   if set(rim[i] for i in range(n) if i not in U)=={0,1,2}:
    ans[n-len(U)]+=4
 return ans

# transfer exact coefficient arrays polynomial in formal variable u
STATES=[(a,b,s) for a in range(3) for b in range(3) if a!=b for s in (0,1)]

def mat(S):
 idx={x:i for i,x in enumerate(STATES)}
 M=[[None]*len(STATES) for _ in STATES]
 for i,(a,b,s) in enumerate(STATES):
  for c in range(3):
   if b==c:continue
   for t in (0,1):
    if s==1:
     if b not in S:continue
     weight=(1,)
    else:
     if a==c or t==0:continue
     weight=(0,1)
    M[i][idx[(b,c,t)]]=weight
 return M

def mult(A,B,n):
 m=len(A);out=[[None]*m for _ in range(m)]
 for i in range(m):
  for k in range(m):
   u=A[i][k]
   if u is None:continue
   for j in range(m):
    v=B[k][j]
    if v is None:continue
    if out[i][j] is None:out[i][j]=[0]*(n+1)
    z=out[i][j]
    for a,c in enumerate(u):
     if not c:continue
     for b,d in enumerate(v):
      if a+b<=n and d:z[a+b]+=c*d
 return out

def traces(n):
 F=None;G=Counter()
 for mask in range(8):
  S={i for i in range(3) if mask>>i&1}
  base=mat(S)
  idm=[[([1] if i==j else None) for j in range(12)] for i in range(12)]
  R=idm
  for i in range(n):R=mult(R,base,n)
  tr=Counter()
  for i in range(12):
   if R[i][i] is not None:
    for k,v in enumerate(R[i][i]):tr[k]+=v
  if mask==7:F=tr
  sg=(-1)**(3-len(S))
  for k,v in tr.items():G[k]+=sg*v
 return F,G

def tr_counts(n):
 F,G=traces(n); ans=Counter()
 for k,v in F.items():ans[(1+n-k,'center',k)]+=4*v
 for k,v in G.items():ans[(n-k,'blank',k)]+=4*v
 return Counter({j:sum(v for (i,_,_),v in ans.items() if i==j) for j,_,_ in ans if sum(v for (i,_,_),v in ans.items() if i==j)>0})

if __name__=='__main__':
 for n in range(4,9):
  x=direct(n) if n<=7 else from_described(n)
  y=from_described(n)
  z=tr_counts(n)
  print(n,sorted(x.items()),sorted(z.items()),x==y==z,flush=True)
  assert x==y==z,(n,x,y,z)
 for n in range(9,13):
  x=tr_counts(n)
  if n<=10:
   brute=from_described(n)
   assert x==brute,(n,x,brute)
   print('DIRECT_RIM_CLASSIFICATION_OK',n,flush=True)
  print('TRANSFER',n,'minimum',min(x),'count',x[min(x)],flush=True)
 # Minimum force-seed count from the cyclic compressed-colouring formula.
 for n in range(4,13):
  x=tr_counts(n)
  if n==4:
   minimum, multiplicity=3,144
  elif n%2:
   t=(n+1)//2
   chrom=2**t+2*(-1)**t
   multiplicity=4*n*(chrom-(6 if t%2==0 else 0))
   minimum=t
  else:
   t=n//2
   chrom=2**t+2*(-1)**t
   multiplicity=8*(chrom-(6 if t%2==0 else 0))
   minimum=t
  assert (min(x),x[min(x)])==(minimum,multiplicity),(n,x,minimum,multiplicity)
 print('MINIMUM_SEED_FORMULAS_OK n=4..12')
 print('VERIFY_OK')
