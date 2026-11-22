from itertools import combinations
from random import Random

def arcs(n,mask):
 a=[[False]*n for _ in range(n)]; k=0
 for i in range(n):
  for j in range(i+1,n):
   a[i][j]=bool(mask&(1<<k));a[j][i]=not a[i][j];k+=1
 return a

def rec_rank3(n,mask):
 a=arcs(n,mask)
 def rank_ge(F,k):
  if k==0:return True
  rest=set(range(n))-set(F)
  for t in range(1<<len(F)):
   viable=False
   for w in rest:
    if tuple(a[w][u] for u in F)==tuple(bool((t>>j)&1) for j in range(len(F))):
     if rank_ge(tuple(F)+(w,),k-1):viable=True;break
   if not viable:return False
  return True
 return rank_ge((),3)

def fast_pred(n,mask):
 a=arcs(n,mask)
 return any(all(any(a[a0][b]==side and len({(a[w][a0],a[w][b]) for w in range(n) if w!=a0 and w!=b})==4 for b in range(n) if b!=a0) for side in (True,False)) for a0 in range(n))
R=Random(771)
for n in range(1,8):
 maxmask=1<<(n*(n-1)//2)
 sample=range(maxmask) if n<=5 else [R.randrange(maxmask) for _ in range(1000)]
 for m in sample:
  x=rec_rank3(n,m);y=fast_pred(n,m)
  assert x==y,(n,m,x,y)
 print(n,'independent recursion checks',len(sample))
print('INDEPENDENT_RECURSION_OK')
