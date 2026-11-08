from itertools import product
from math import comb

# Values 0,1,2 denote 0, 1/2, 1.
def transitive(n, v):
  for a in range(n):
    if v[a*n+a]!=2:return False
  for a,b,c in product(range(n),repeat=3):
    if v[a*n+c] < max(0,v[a*n+b]+v[b*n+c]-2):return False
  return True

def normal(n,v):
  P={(a,b) for a,b in product(range(n),repeat=2) if v[a*n+b]==2}
  H={(a,b) for a,b in product(range(n),repeat=2) if v[a*n+b]>=1}
  condP=all((a,c) in P for a,b,c in product(range(n),repeat=3) if (a,b) in P and (b,c) in P)
  condH=all((a,c) in H for a,b,c in product(range(n),repeat=3) if ((a,b) in P and (b,c) in H) or ((a,b) in H and (b,c) in P))
  return condP and condH

for n in range(1,5):
  count=0
  for off in product(range(3),repeat=n*(n-1)):
    x=iter(off)
    v=tuple(2 if i==j else next(x) for i in range(n) for j in range(n))
    a=transitive(n,v); b=normal(n,v)
    assert a==b,(n,v)
    count+=a
  print('DIRECT',n,count,flush=True)
from itertools import combinations
from math import factorial

def all_posets(k):
  q=[(i,j) for i in range(k) for j in range(k) if i!=j]
  for bits in product((0,1),repeat=len(q)):
    P={(i,i) for i in range(k)}|{q[t] for t,b in enumerate(bits) if b}
    if all((a,c) in P for a,b,c in product(range(k),repeat=3) if (a,b) in P and (b,c) in P) and all((a,b) not in P or (b,a) not in P for a,b in q):yield P

def ideals(k,P):
 D=[(a,b) for a,b in product(range(k),repeat=2) if (a,b) not in P]
 # each outside pair in H forces others outside (a',b') with a'<=a, b<=b'
 up=[sum(1<<j for j,(aa,bb) in enumerate(D) if (aa,a) in P and (b,bb) in P) for a,b in D]
 count=0
 for mask in range(1<<len(D)):
   if all(mask&up[i]==up[i] for i in range(len(D)) if mask>>i&1):count+=1
 return count

T={}
for k in range(1,5):
 P=list(all_posets(k)); sm=sum(ideals(k,p) for p in P)
 T[k]=sm
 print('POSET',k,len(P),'T',sm)
for n in range(1,5):
 from functools import lru_cache
 @lru_cache(None)
 def S(n,k):return 1 if n==k or k==1 else S(n-1,k-1)+k*S(n-1,k)
 print('SUM',n,sum(S(n,k)*T[k] for k in range(1,n+1)))
for k in range(1,8):
 P={(a,b) for a in range(k) for b in range(k) if a<=b}
 res=ideals(k,P)
 catalan=comb(2*k,k)//(k+1)
 print('CHAIN',k,res,catalan)
 assert res==catalan
