from itertools import product, combinations
from math import comb

def mobius(n):
 d=2; mu=1
 while d*d<=n:
  if n%d==0:
   n//=d;mu=-mu
   if n%d==0:return 0
   while n%d==0:n//=d
  d+=1
 return -mu if n>1 else mu

def primitives(q,d):
 return sum(mobius(e)*q**(d//e) for e in range(1,d+1) if d%e==0)//d

def rotations(u):
 return {u[j:]+u[:j] for j in range(len(u))}

def predicted(u,v,t):
 return any(v==u[j:]+u[:j] for j in list(range(0,min(t,len(u)-1)+1))+list(range(max(1,len(u)-t),len(u))))

def shadow(u,r,t):
 x=u*r;n=len(x)
 return {''.join(x[i] for i in range(n) if i not in idx) for idx in combinations(range(n),t)}

def cap(q,m,t):
 ans=1;size=0
 for d in range(1,m+1):
  if m%d:continue
  k=max(1,d//(t+1));c=primitives(q,d)
  size+=c*k
  ways=(d*comb(d-t*k-1,k-1))//k if d>t else d
  assert ways*k==d*comb(d-t*k-1,k-1) if d>t else True
  ans*=ways**c
 return size,ans

def test(q,m,t):
 words=[''.join(x) for x in product('0123'[:q],repeat=m)]
 r=2*t+1
 sh={u:shadow(u,r,t) for u in words}
 edges=0
 for u,v in combinations(words,2):
  exp=predicted(u,v,t);found=bool(sh[u]&sh[v]);assert found==exp,(q,m,t,u,v,found,exp)
  edges+=found
 print('verified',q,m,t,'pairs',comb(q**m,2),'edges',edges,'opt',cap(q,m,t))
 if q**m<=16:
  n=len(words); masks=[]
  for i,u in enumerate(words):
   mask=0
   for j,v in enumerate(words):
    if i!=j and predicted(u,v,t):mask|=1<<j
   masks.append(mask)
  largest=0;number=0
  for mask in range(1<<n):
   valid=all(not ((mask>>i)&1 and masks[i]&mask) for i in range(n))
   if valid:
    size=mask.bit_count()
    if size>largest: largest=size;number=0
    if size==largest:number+=1
  assert (largest,number)==cap(q,m,t),((largest,number),cap(q,m,t))

for q,m,t in [(2,1,1),(2,2,1),(2,3,1),(2,4,1),(2,5,1),(2,1,2),(2,2,2),(2,3,2),(2,4,2),(2,5,2),(3,1,1),(3,2,1),(3,3,1),(3,1,2),(3,2,2),(3,3,2)]:
 test(q,m,t)
print('VERIFY_OK')
