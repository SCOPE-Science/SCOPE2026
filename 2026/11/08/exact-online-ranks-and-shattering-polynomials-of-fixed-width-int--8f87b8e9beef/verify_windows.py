from functools import lru_cache
from itertools import combinations

def rank(codes,n):
 masks=[sum(1<<j for j,c in enumerate(codes) if c>>i&1) for i in range(n)]
 @lru_cache(None)
 def rec(sub):
  if sub&(sub-1)==0:return 0
  bound=sub.bit_count().bit_length()-1
  best=0
  for cm in masks:
   a=sub&cm;b=sub^a
   if a and b:
    best=max(best,1+min(rec(a),rec(b)))
    if best==bound:break
  return best
 return rec((1<<len(codes))-1)

def poly_actual(codes,n):
 res=[1,0,0,0]
 for j in range(1,4):
  for S in combinations(range(n),j):
   tr={sum((1<<k) for k,x in enumerate(S) if c>>x&1) for c in codes}
   if len(tr)==(1<<j):res[j]+=1
 return res

def poly_pred(n,r,zero):
 m=n-r+1
 if zero:
  return [1,n,sum(min(k,r-1) for k in range(1,m-1)),0]
 k=max(0,m-r-1)
 q=min(r-1,k-1)
 return [1,n-max(0,r-m+1),2*k*(r-1)-sum(k-d for d in range(1,q+1)),0]

def expected_rank(m,r,zero):return min((m+int(zero)).bit_length()-1,1+(r.bit_length()-1))

if __name__=='__main__':
 nr=0;cs=0
 for n in range(1,17):
  for r in range(1,n+1):
   m=n-r+1
   wins=[sum(1<<i for i in range(a,a+r)) for a in range(m)]
   for zero in [False,True]:
    codes=[0]+wins if zero else wins
    actual=rank(codes,n)
    exp=expected_rank(m,r,zero)
    assert actual==exp,(n,r,zero,actual,exp)
    p=poly_actual(codes,n) if n<=14 else None
    if p is not None: assert p==poly_pred(n,r,zero),(n,r,zero,p,poly_pred(n,r,zero))
    cs+=1
   nr+=1
 print('WINDOW_RANK_AND_TRACE_PASS',nr,'n_r_pairs',cs,'rank_classes','n_max',n,'polynomial_n_max',14)
