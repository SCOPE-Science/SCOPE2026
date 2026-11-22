"""Direct exact tests of rectangular-band derivation normal forms. Standard library only."""
from itertools import product

def coordinates(m,n):
 b=n-1;c=m-1
 # canonical e, row B, column C, W with C tensor B
 return 1+b+c+b*c

def mult(x,y,m,n,p):
 b=n-1;c=m-1
 z=[0]*(m*n);z[0]=x[0]*y[0]%p
 for j in range(b):z[1+j]=x[0]*y[1+j]%p
 for i in range(c):z[1+b+i]=x[1+b+i]*y[0]%p
 off=1+b+c
 for i in range(c):
  for j in range(b):z[off+i*b+j]=x[1+b+i]*y[1+j]%p
 return tuple(z)

def normal_D(m,n,p,b0,c0,S,T):
 b=n-1;c=m-1;N=m*n;W=1+b+c
 cols=[]
 # e
 cols.append([0]+list(b0)+list(c0)+[0]*(b*c))
 # B basis vectors
 for j in range(b):
  v=[0]*N
  for i in range(b):v[1+i]=S[i*b+j]%p
  for i in range(c):v[W+i*b+j]=c0[i]%p
  cols.append(v)
 # C basis vectors
 for j in range(c):
  v=[0]*N
  for i in range(c):v[1+b+i]=T[i*c+j]%p
  for h in range(b):v[W+j*b+h]=b0[h]%p
  cols.append(v)
 # W basis vectors
 for i in range(c):
  for j in range(b):
   v=[0]*N
   for h in range(c):v[W+h*b+j]=T[h*c+i]%p
   for h in range(b):v[W+i*b+h]=(v[W+i*b+h]+S[h*b+j])%p
   cols.append(v)
 return tuple(tuple(v) for v in cols)

def apply(cols,v,p):
 N=len(cols);return tuple(sum(v[j]*cols[j][i] for j in range(N))%p for i in range(N))

def rank(cols,p):
 a=[[cols[j][i]%p for j in range(len(cols))] for i in range(len(cols))]
 rr=0
 for cc in range(len(cols)):
  k=next((k for k in range(rr,len(cols)) if a[k][cc]),None)
  if k is None:continue
  a[rr],a[k]=a[k],a[rr];f=pow(a[rr][cc],-1,p)
  a[rr]=[(v*f)%p for v in a[rr]]
  for k in range(len(cols)):
   if k!=rr and a[k][cc]:
    f=a[k][cc];a[k]=[(u-f*v)%p for u,v in zip(a[k],a[rr])]
  rr+=1
 return rr

def check_derivation(cols,m,n,p):
 N=m*n;basis=[tuple(int(i==j) for i in range(N)) for j in range(N)]
 for i in range(N):
  for j in range(N):
   xy=mult(basis[i],basis[j],m,n,p)
   left=apply(cols,xy,p)
   right=tuple((u+v)%p for u,v in zip(mult(cols[i],basis[j],m,n,p),mult(basis[i],cols[j],m,n,p)))
   if left!=right:return False
 return True

def is_idempotent(cols,p):return all(apply(cols,v,p)==v for v in cols)

def test(m,n,p):
 b=n-1;c=m-1
 observed={};all_deriv=0;all_idemp=0
 for nums in product(range(p),repeat=b+c+b*b+c*c):
  b0=nums[:b];c0=nums[b:b+c];S=nums[b+c:b+c+b*b];T=nums[b+c+b*b:]
  cols=normal_D(m,n,p,b0,c0,S,T)
  assert check_derivation(cols,m,n,p)
  all_deriv+=1
  if is_idempotent(cols,p):
   all_idemp+=1
   r=rank(cols,p);observed[r]=observed.get(r,0)+1
 # Independently enumerate idempotent S,T and eigenvectors
 predicted={}
 for s in product(range(p),repeat=b*b):
  Scols=[tuple(s[i*b+j] for i in range(b)) for j in range(b)]
  if any(apply(Scols,v,p)!=v for v in Scols):continue
  sr=rank(Scols,p)
  for t in product(range(p),repeat=c*c):
   Tcols=[tuple(t[i*c+j] for i in range(c)) for j in range(c)]
   if any(apply(Tcols,v,p)!=v for v in Tcols):continue
   tr=rank(Tcols,p)
   if p!=2 and sr and tr:continue
   r=sr*m+tr*n-(2*sr*tr if p==2 else 0)
   predicted[r]=predicted.get(r,0)+p**(sr+tr)
 assert observed==predicted,(observed,predicted)
 print(f'PASS m={m} n={n} p={p} all_deriv={all_deriv} idempotent={all_idemp} rank_counts={dict(sorted(observed.items()))}')
if __name__=='__main__':
 for args in [(2,2,2),(2,2,3),(2,2,5),(2,3,2),(3,2,2)]:test(*args)

def exhaustive_all_linear_binary_2by2():
 p=2;m=n=2;N=4
 def bit2tuple(x):return tuple((x>>i)&1 for i in range(N))
 def tup2bit(t):return sum(x<<i for i,x in enumerate(t))
 prod=[[tup2bit(mult(bit2tuple(x),bit2tuple(y),m,n,2)) for y in range(16)] for x in range(16)]
 def out(cols,x):
  v=0
  for i in range(N):
   if x>>i &1:v^=cols[i]
  return v
 found=set();idf={}
 for cols in product(range(16),repeat=4):
  ok=True
  for i in range(N):
   if not ok:break
   for j in range(N):
    l=out(cols,prod[1<<i][1<<j]);r=prod[cols[i]][1<<j]^prod[1<<i][cols[j]]
    if l!=r:ok=False;break
  if ok:
   found.add(cols)
   if all(out(cols,c)==c for c in cols):idf[cols]=True
 assert len(found)==16,(len(found),len(idf))
 assert len(idf)==9
 print('PASS exhaustive all 65536 binary 4x4 linear maps: exactly 16 derivations, 9 idempotent')
if __name__=='__main__':exhaustive_all_linear_binary_2by2()
