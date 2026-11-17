import itertools,json,functools,os,time

def canonical(t):
 if isinstance(t,int): return t
 x,y=map(canonical,t)
 def lo(u):return u if isinstance(u,int) else min(lo(u[0]),lo(u[1]))
 return (x,y) if lo(x)<lo(y) else (y,x)

def by_splits(S):
 if len(S)==1:return [S[0]]
 low=S[0];R=S[1:];out=[]
 for bits in range(1<<len(R)):
  L=[low]+[v for k,v in enumerate(R) if bits&(1<<k)]
  M=[v for k,v in enumerate(R) if not(bits&(1<<k))]
  if not M:continue
  for a in by_splits(L):
   for b in by_splits(M):out.append(canonical((a,b)))
 return out

def by_insertion(n):
 trees=[(0,1)]
 def insertion(t,v):
  out=[canonical((t,v))]
  if isinstance(t,tuple):
   a,b=t
   out.extend([canonical((s,b)) for s in insertion(a,v)])
   out.extend([canonical((a,s)) for s in insertion(b,v)])
  return out
 for v in range(2,n):
  trees=list(itertools.chain.from_iterable(insertion(t,v) for t in trees))
  assert len(trees)==len(set(trees))
 return trees

def clades(t):
 if isinstance(t,int):return [1<<t]
 c1=clades(t[0]);c2=clades(t[1]);return c1+c2+[c1[-1]|c2[-1]]

def predicates(n):
 q=[]
 for a,b,c in itertools.combinations(range(n),3):
  q.extend([(a,b,c),(a,c,b),(b,c,a)])
 return q

def table(n):
 T=by_splits(list(range(n)))
 I=by_insertion(n)
 assert len(T)==len(I) and set(T)==set(I)
 assert len(T)==(1 if n<3 else __import__('math').prod(range(3,2*n-2,2)))
 # sorted canonical tuples, distinct
 T=sorted(T,key=str)
 q=predicates(n)
 p=[]
 for t in T:
  cc=clades(t)
  p.append(sum(1<<j for j,(a,b,c) in enumerate(q) if any((x&(1<<a)) and (x&(1<<b)) and not (x&(1<<c)) for x in cc)))
 assert len(set(p))==len(T)
 masks=[sum(1<<i for i,v in enumerate(p) if (v>>j)&1) for j in range(len(q))]
 return T,q,p,masks

def rec_maker(masks):
 @functools.lru_cache(None)
 def rec(S):
  if S.bit_count()<=1:return 0
  best=0
  for q in masks:
   yes=S&q;no=S^yes
   if not yes or not no:continue
   if min(yes.bit_count(),no.bit_count())<1<<best:continue
   v=1+min(rec(no),rec(yes))
   if v>best:best=v
  return best
 return rec

def make_strategy(q,masks,rec,allset,d):
 arr=[None]*((1<<d)-1)
 def follow(idx,cur,depth):
  if depth==0:assert cur;return
  for j,v in enumerate(masks):
   yes=cur&v;no=cur^yes
   if not yes or not no:continue
   if rec(yes)>=depth-1 and rec(no)>=depth-1:
    arr[idx]=q[j]
    follow(2*idx+1,no,depth-1)
    follow(2*idx+2,yes,depth-1)
    return
  raise RuntimeError('no strategy')
 follow(0,allset,d)
 assert all(x is not None for x in arr)
 return arr

def main():
 bundle={'schema_version':1,'query_semantics':'For a,b,c distinct, 1 iff (a,b)|c is displayed. Left branch 0, right branch 1.','strategies':{}}
 for n in range(3,7):
  T,q,p,masks=table(n)
  print('n',n,'trees',len(T),'queries',len(q),flush=True)
  allset=(1<<len(T))-1
  rec=rec_maker(masks)
  d=rec(allset)
  arr=make_strategy(q,masks,rec,allset,d)
  bundle['strategies'][str(n)]={'depth':d,'node_queries':arr}
  print('dim',d,'internal nodes',len(arr),'cache',rec.cache_info(),flush=True)
 with open('rooted_triplet_strategy.json','w',encoding='utf8') as f:json.dump(bundle,f,separators=(',',':'),sort_keys=True);f.write('\n')
if __name__=='__main__':main()
