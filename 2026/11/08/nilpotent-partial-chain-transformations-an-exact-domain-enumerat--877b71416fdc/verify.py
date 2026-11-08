import math,itertools,collections
from math import comb

def polynomial_counts(N=8):
 A=[[0]*(n+1) for n in range(N+1)]
 B=[[0]*(n+1) for n in range(N+1)]
 C=[[0]*(n+1) for n in range(N+1)]
 for n in range(N+1):
  for d in range(n+1):
   A[n][d]=comb(n,d)*comb(n+d-1,d) if n>0 else int(d==0)
   B[n][d]=comb(n,d)*comb(n+d,d)
   C[n][d]=comb(n,d)*comb(n+d+1,d)
 def conv(a,b):
  t=[0]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
   for j,y in enumerate(b):t[i+j]+=x*y
  return t
 H=[]; out=[]
 for n in range(N+1):
  h=[0]*(n+1)
  for j in range(n+1):
   z=conv(B[j],B[n-j]);
   for k,v in enumerate(z):
    if k<=n:h[k]+=v
  for j in range(n):
   z=conv(C[j],H[n-1-j]);
   for k,v in enumerate(z):
    if k+1<=n:h[k+1]-=v
  H.append(h)
  p=A[n][:]
  if n:
   for k,v in enumerate(H[n-1]):
    p[k+1]-=v
  out.append(p)
 return out

def brute(n):
 counts=[0]*(n+1)
 for d in range(n+1):
  for dom in itertools.combinations(range(n),d):
   for img in itertools.combinations_with_replacement(range(n),d):
    f=[-1]*n
    for i,j in zip(dom,img):f[i]=j
    if all(f[i]!=i for i in range(n)):
     counts[d]+=1
 return counts

pred=polynomial_counts(9)
for n in range(9):
 got=brute(n)
 assert got==pred[n],(n,got,pred[n])
 print('n',n,'total',sum(got),'domain_counts',got)
print('VERIFY_OK')
