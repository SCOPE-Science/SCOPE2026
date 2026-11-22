from collections import Counter
import itertools

def rank(a,m,n,q):
 a=[list(a[i*n:i*n+n]) for i in range(m)];r=0
 for j in range(n):
  k=next((t for t in range(r,m) if a[t][j]%q),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r]
  for t in range(m):
   if t!=r and a[t][j]:
    v=a[t][j]*pow(a[r][j],-1,q)%q
    for l in range(j,n):a[t][l]=(a[t][l]-v*a[r][l])%q
  r+=1
  if r==m:break
 return r

def key(z,m,n,q):
 if all(v==0 for v in z):return 'zero'
 if sum(z)%q:return 'total_nonzero'
 R=rank(z,m,n,q)
 row=[sum(z[i*n:(i+1)*n])%q for i in range(m)]
 col=[sum(z[i*n+j] for i in range(m))%q for j in range(n)]
 a=int(any(row));b=int(any(col))
 return str(R)+':'+str(a)+str(b)

def expected(z,m,n,q):
 h=(m-1)*(n-1)
 K=(q**(m+n-1)+(q**(n-1)-1)*q**(n-1)+(q**(m-1)-1)*q**(m-1)+(q**(m+n-1)-q**(n-1)-q**(m-1)+1)*q)
 typ=key(z,m,n,q)
 if typ=='zero':return q**(2*h)*K
 if typ=='1:01':return (q*q-1)*q**(2*h+n-1)
 if typ=='1:10':return (q*q-1)*q**(2*h+m-1)
 if typ=='1:00':return (q*q-1)*q**(2*h)*(q**(m-1)+q**(n-1)-q)
 if typ=='2:11':return q**(2*h)*q*(q*q-1)
 if typ=='2:00':return q**(2*h)*(q*q-1)*(q*q-q)
 return 0

def prod(x,y,m,n,q):
 r=[sum(x[i*n:(i+1)*n])%q for i in range(m)]
 c=[sum(y[i*n+j] for i in range(m))%q for j in range(n)]
 return [r[i]*c[j]%q for i in range(m) for j in range(n)]
for m,n,q in [(2,2,2),(2,3,2),(3,2,2),(2,2,3),(3,3,2)]:
 aa=list(itertools.product(range(q),repeat=m*n));h=Counter()
 for x in aa:
  for y in aa:
   p=prod(x,y,m,n,q);s=prod(y,x,m,n,q)
   h[tuple((a-b)%q for a,b in zip(p,s))]+=1
 err=[];ct=Counter()
 for z in itertools.product(range(q),repeat=m*n):
  typ=key(z,m,n,q);ct[typ]+=1
  if h[z]!=expected(z,m,n,q):err.append((z,typ,h[z],expected(z,m,n,q)))
 print(m,n,q,'types',sorted(ct.items()),'errors',len(err),err[:3])
 assert not err
