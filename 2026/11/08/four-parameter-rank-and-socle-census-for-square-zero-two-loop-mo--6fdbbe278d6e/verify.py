from itertools import product
from collections import Counter
from math import prod

def gauss(n,k,q):
 if k<0 or k>n:return 0
 return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))
def surj(d,r,q):
 if d<r:return 0
 return prod(q**d-q**i for i in range(r))
def injective_pair(ell,r,s,q):
 return sum((-1)**j*q**(j*(j-1)//2)*gauss(ell,j,q)*surj(ell-j,r,q)*surj(ell-j,s,q) for j in range(ell+1))
def predicted(n,q):
 C=Counter()
 for r in range(n//2+1):
  for s in range(n//2+1):
   for w in range(max(r,s),min(r+s,n)+1):
    t=r+s-w
    x=gauss(n,w,q)*gauss(w,r,q)*gauss(r,t,q)*q**((w-r)*(w-s))
    for u in range(w,n+1):
     c=x*gauss(n-w,u-w,q)*injective_pair(n-u,r,s,q)
     if c:C[(r,s,w,u)]=c
 return C

def rank(rows,n,q):
 A=[list(row) for row in rows]; p=0
 for c in range(n):
  t=next((t for t in range(p,len(A)) if A[t][c]%q),None)
  if t is None:continue
  A[p],A[t]=A[t],A[p]
  v=pow(A[p][c],-1,q)
  A[p]=[(x*v)%q for x in A[p]]
  for t in range(len(A)):
   if t!=p and A[t][c]:
    v=A[t][c];A[t]=[(x-v*y)%q for x,y in zip(A[t],A[p])]
  p+=1
  if p==len(A):break
 return p

def mprod(A,B,q):
 n=len(A)
 return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n))%q for j in range(n)) for i in range(n))
def allzero(A):return all(not x for row in A for x in row)
def verify(n,q):
 mats=[]
 for x in product(range(q),repeat=n*n):
  A=tuple(tuple(x[i*n:(i+1)*n]) for i in range(n))
  if allzero(mprod(A,A,q)):
   r=rank(A,n,q)
   mats.append((A,r))
 obs=Counter()
 for A,r in mats:
  for B,s in mats:
   if not allzero(mprod(A,B,q)) or not allzero(mprod(B,A,q)):continue
   # row-rank of transpose concat equals sum of column spaces rank
   w=rank(tuple(tuple(A[i][j] for i in range(n)) for j in range(n))+tuple(tuple(B[i][j] for i in range(n)) for j in range(n)),n,q)
   # simultaneous map v -> (Av,Bv), rank = n-u
   stacked=A+B
   u=n-rank(stacked,n,q)
   obs[(r,s,w,u)]+=1
 exp=predicted(n,q)
 assert obs==exp,(n,q,(obs-exp),(exp-obs))
 return (n,q,len(mats),sum(obs.values()),len(obs))
def total_by_common_image(n,q):
 return sum(gauss(n,w,q)*surj(2*(n-w),w,q) for w in range(n+1))

if __name__=='__main__':
 for n,q in [(2,2),(3,2),(4,2),(2,3),(3,3)]:print('direct',verify(n,q),flush=True)
 for n,q in [(2,2),(3,2),(4,2),(5,2),(3,3)]:
  C=predicted(n,q)
  print('formula',n,q,'tuple-count',sum(C.values()),'distinct-profile-count',len(C))
  if n==3 and q==2:
   print('n3 r1s1:',sorted((w,u,c) for (r,s,w,u),c in C.items() if r==s==1))

 for n,q in [(3,4),(4,4),(5,3)]:
  ans=sum(predicted(n,q).values())
  assert ans==total_by_common_image(n,q)
  print('global-identity',n,q,ans)
 print('FOUR_PARAMETER_SQUARE_ZERO_MODULE_CENSUS_OK')
