from itertools import product
from random import Random

def closed(w):
 n=len(w)
 if n==1:return True
 for t in range(1,n):
  if w[:t]==w[n-t:]:
   if sum(w[s:s+t]==w[:t] for s in range(n-t+1))==2:return True
 return False

def brute(a,n):
 w=tuple(c for c,x in enumerate(a) for _ in range(x));p=len(w)
 ext=w*(n//p+3)
 fac={ext[s:s+n] for s in range(p)}
 return sum(map(closed,fac))

def pred(a,n):
 p=sum(a)
 if n<=p:
  return sum(x>=n for x in a)+sum(1 for x in a if 2<=n-p+x<=x and (n-p+x)%2==0)
 if n<=2*p:
  h=n-p
  return sum(min(x,h-1) for x in a)+sum(x>=h and (x-h)%2==0 for x in a)
 return p

count=0
for q in range(2,6):
 for a in product(range(1,5),repeat=q):
  p=sum(a)
  for n in range(1,2*p+4):
   x,y=brute(a,n),pred(a,n)
   if x!=y:
    print('WRONG',a,n,x,y);quit()
   count+=1
 print('PASS',q)
print('checked',count)

# Extra deterministic larger-profile corroboration.
from random import Random
_rng=Random(20261105)
for _ in range(2000):
    _q=_rng.randint(3,7)
    _a=[_rng.randint(1,15) for _ in range(_q)]
    _n=_rng.randint(1,3*sum(_a)+7)
    assert brute(_a,_n)==pred(_a,_n), (_a,_n)
print('PASS seeded cases: 2000')
