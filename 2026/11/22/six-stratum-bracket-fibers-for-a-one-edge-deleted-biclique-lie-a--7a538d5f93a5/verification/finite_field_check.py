from collections import Counter
from itertools import product

def rank(M,p):
 a=[[(int(x)%p) for x in row] for row in M]
 r=0
 for c in range(len(a[0])):
  k=next((j for j in range(r,len(a)) if a[j][c]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r]
  v=pow(a[r][c],-1,p)
  a[r]=[(x*v)%p for x in a[r]]
  for j in range(len(a)):
   if j!=r and a[j][c]:
    v=a[j][c];a[j]=[(x-v*y)%p for x,y in zip(a[j],a[r])]
  r+=1
 return r

def image_rank_target(t,p):
 A=[list(t[:2]),list(t[3:5])]
 b=[t[2],t[5]]; d=[t[6],t[7]]
 ra=rank(A,p)
 if ra==2:return 2
 if ra==1:
  cr=rank([[A[0][0],A[0][1],b[0]],[A[1][0],A[1][1],b[1]]],p)>1
  rr=rank([A[0],A[1],d],p)>1
  if cr and rr:return -1
  if cr or rr:return 20
  return 12
 if any(b) and any(d):return 20
 if any(b) or any(d):return 11
 return 10

def nr(p):
 gl=(p*p-1)*(p*p-p)
 n2=gl
 n1=(p*p-1)*p**3+(p+1)*gl
 n0=p**6+((p**3-1)*(p*p-1)//(p-1))*p**3+(p*p+p+1)*gl
 return n0,n1,n2

def pred(t,p):
 n0,n1,n2=nr(p)
 k=image_rank_target(t,p)
 return {-1:0,2:n2,20:p*n2,12:n1+(p-1)*n2,11:p*n1,10:n0+(p-1)*n1}[k]

def brute(p):
 vec=list(product(range(p),repeat=3));out=Counter()
 # choose u,u',v,v' and aggregate matrix images, no 14D central coords
 for u in vec:
  for up in vec:
   for v in vec:
    for vp in vec:
     t=tuple((u[i]*vp[j]-up[i]*v[j])%p for i in range(3) for j in range(3) if (i,j)!=(2,2))
     out[t]+=1
 assert sum(out.values())==p**12
 for t in product(range(p),repeat=8):
  a=out[t];b=pred(t,p)
  assert a==b,(p,t,a,b)
 unreachable=p*p*(p-1)**3*(p+1)**2
 assert p**8-len(out)==unreachable,(p,len(out),unreachable)
 strata=Counter(image_rank_target(t,p) for t in product(range(p),repeat=8))
 print('q',p,'total_targets',p**8,'attainable',len(out),'unattainable',unreachable,'bracket_pairs',sum(out.values()),'strata',sorted(strata.items()),'N',nr(p))
for p in [2,3]:brute(p)
