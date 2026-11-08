import itertools
from collections import Counter
from functools import lru_cache

def field(r):
 p=5; mod= [3,0] if r==2 else [1,1,0]
 Q=p**r
 def digits(x):return [(x//p**i)%p for i in range(r)]
 dig=[digits(x) for x in range(Q)]
 @lru_cache(None)
 def mul(x,y):
  x=dig[x];y=dig[y];c=[0]*(2*r-1)
  for i in range(r):
   for j in range(r):c[i+j]+=x[i]*y[j]
  for k in range(2*r-2,r-1,-1):
   t=c[k]%p
   for j in range(r):c[k-r+j]-=t*mod[j]
  return sum((c[i]%p)*p**i for i in range(r))
 def power(x,n):
  a=1
  while n:
   if n&1:a=mul(a,x)
   x=mul(x,x);n//=2
  return a
 inv=[None]+[power(x,Q-2) for x in range(1,Q)]
 frob=[power(x,5) for x in range(Q)]
 neg=[sum(((-v)%5)*5**i for i,v in enumerate(dig[x])) for x in range(Q)]
 return Q,mul,inv,frob,neg

def pm(a):
 if not a:yield ()
 else:
  a0=a[0]
  for v in a[1:]:
   for rest in pm([w for w in a[1:] if w!=v]):yield tuple(sorted(((a0,v),)+rest))
ms=sorted(set(pm(list(range(6)))))

def run(r,ps):
 Q,mul,inv,frob,neg=field(r)
 def norm(z):
  t=next(x for x in z if x)
  return tuple(mul(y,inv[t]) for y in z)
 B=set()
 for m in ms:
  for c in itertools.chain(((1,a,b) for a in range(Q) for b in range(Q)),((0,1,a) for a in range(Q)),[(0,0,1)]):
   z=[0]*6
   for (i,j),a in zip(m,c):z[i]=a;z[j]=neg[a]
   B.add(norm(z))
 print('field F_5^',r,'geometric points in union over field',len(B))
 for p in ps:
  perm=list(range(6));i=0
  for size in p:
   for j in range(size):perm[i+j]=i+(j+1)%size
   i+=size
  cnt=Counter()
  for z in B:
   zz=[0]*6
   for i in range(6):zz[perm[i]]=frob[z[i]]
   if norm(zz)==z:
    m=sum(all(z[i]==neg[z[j]] for i,j in match) for match in ms)
    cnt[m]+=1
  assert dict(cnt) == {
   (2,2,2):{1:126,2:33,3:3,6:4},
   (2,2,1,1):{1:58,2:23,3:3,6:2},
   (2,1,1,1,1):{1:54,2:33,3:7,6:4},
   (3,3):{1:90,6:1},
   (3,1,1,1):{3:3,6:1},
  }[p], (p, cnt)
  print(p, dict(cnt),'total',sum(cnt.values()))
run(2,[(2,2,2),(2,2,1,1),(2,1,1,1,1)])
run(3,[(3,3),(3,1,1,1)])

print("VERIFY_SEGRE_DIRECT_OK F25_F125")
