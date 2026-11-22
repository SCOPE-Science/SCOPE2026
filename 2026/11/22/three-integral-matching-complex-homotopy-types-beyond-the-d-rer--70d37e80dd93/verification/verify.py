"""Exact finite verification for four generalized Petersen ordinary matching complexes.
Run with Python 3.10 or later; no third-party dependencies.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

EXPECTED = {
 6: (1038, 507, {0:1, 3:23,4:1}, {3:22}, 1),
 7: (3418,1693, {0:1, 3:2, 4:30}, {4:28}, 2),
 8: (10990,5477,{0:1, 4:11,5:25},{4:2,5:16}, 9),
 9: (34880,17404,{0:1, 5:57,6:15},{5:42}, 15)
}

def edges_gp(n):
 return sorted({tuple(sorted(e)) for i in range(n)
  for e in ((i,(i+1)%n),(i,i+n),(i+n,n+(i+2)%n))})

def face_set(edges):
 occupancy=[(1<<u)|(1<<v) for u,v in edges]
 found={0}
 def build(start,used,mask):
  for i in range(start,len(edges)):
   if used&occupancy[i]:continue
   nxt=mask|(1<<i);found.add(nxt)
   build(i+1,used|occupancy[i],nxt)
 build(0,0,0)
 return found

def faces_of(mask):
 j=0;remaining=mask
 while remaining:
  bit=remaining&-remaining
  yield (mask^bit, (-1)**j)
  j+=1;remaining^=bit

def make_matching(face_set_,edge_count,reverse=False):
 available=set(face_set_);pairs=[]
 order=range(edge_count-1,-1,-1) if reverse else range(edge_count)
 for j in order:
  bit=1<<j
  selected=[(s,s|bit) for s in available if not s&bit and (s|bit) in available]
  for lower,upper in selected:
   available.remove(lower);available.remove(upper)
  pairs.extend(selected)
 return available,pairs

def confirm_acyclic(faces,pairs):
 up=dict(pairs);indegree={s:0 for s in faces};adj=defaultdict(list);count=0
 for hi in faces:
  if hi==0:continue
  for lo,_ in faces_of(hi):
   if up.get(lo)==hi:src,dst=lo,hi
   else:src,dst=hi,lo
   adj[src].append(dst);indegree[dst]+=1;count+=1
 todo=deque(x for x in faces if indegree[x]==0)
 seen=0
 while todo:
  x=todo.popleft();seen+=1
  for y in adj[x]:
   indegree[y]-=1
   if indegree[y]==0:todo.append(y)
 assert seen==len(faces),'Directed Hasse graph contains a cycle'
 return count

def morse_matrix(unmatched,pairs,dim):
 lows=dict(pairs);uppers={b:a for a,b in pairs}
 lower=sorted(x for x in unmatched if x.bit_count()==dim)
 higher=sorted(x for x in unmatched if x.bit_count()==dim+1)
 row={x:i for i,x in enumerate(lower)}
 @lru_cache(None)
 def down(s):
  if s in uppers:return {}
  if s in unmatched:return {s:1}
  high=lows[s]
  facets=list(faces_of(high));pivot=dict(facets)[s]
  ans=defaultdict(int)
  for other,sg in facets:
   if other==s:continue
   for target,val in down(other).items():ans[target]-=pivot*sg*val
  return {x:v for x,v in ans.items() if v}
 matrix=[[0 for _ in higher] for _ in lower]
 for j,s in enumerate(higher):
  for face,sg in faces_of(s):
   for q,v in down(face).items():matrix[row[q]][j]+=sg*v
 return matrix

def unit_pivot_reduction(matrix):
 """Exact integral row and column operations, only unit pivots.
 A nonzero leftover is NOT silently accepted as free or torsion-free.
 """
 if not matrix:return 0, []
 A=[list(row) for row in matrix];m=len(A);n=len(A[0]);rank=0
 while rank<min(m,n):
  candidate=next(((i,j) for i in range(rank,m) for j in range(rank,n) if abs(A[i][j])==1),None)
  if candidate is None:break
  i,j=candidate;A[i],A[rank]=A[rank],A[i]
  for row in A:row[j],row[rank]=row[rank],row[j]
  if A[rank][rank]==-1:A[rank]=[-v for v in A[rank]]
  for i2 in range(m):
   if i2==rank:continue
   q=A[i2][rank]
   if q:A[i2]=[a-q*b for a,b in zip(A[i2],A[rank])]
  for j2 in range(n):
   if j2==rank:continue
   q=A[rank][j2]
   if q:
    for i2 in range(m):A[i2][j2]-=q*A[i2][rank]
  rank+=1
 leftover=[A[i][j] for i in range(rank,m) for j in range(rank,n) if A[i][j]]
 return rank,leftover

def gf2_ranks(faces,n):
 by=defaultdict(list)
 for s in faces:by[s.bit_count()].append(s)
 ranks={}
 for k in range(1,max(by)+1):
  rows={s:i for i,s in enumerate(by[k-1])}
  piv={};rank=0
  for cell in by[k]:
   col=0
   for face,_ in faces_of(cell):col^=1<<rows[face]
   while col:
    i=col.bit_length()-1
    if i in piv:col^=piv[i]
    else:piv[i]=col;rank+=1;break
  ranks[k]=rank
 return {k-1:len(by[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in by if k>0 and len(by[k])-ranks.get(k,0)-ranks.get(k+1,0)}

def verify(n,reverse=False,with_gf2=False):
 edges=edges_gp(n)
 assert len(edges)==3*n
 assert Counter(u for e in edges for u in e)=={u:3 for u in range(2*n)}
 faces=face_set(edges);unmatched,pairs=make_matching(faces,len(edges),reverse)
 assert len(faces)==len(unmatched)+2*len(pairs)
 assert (0 not in unmatched)
 assert sum(lo==0 for lo,_ in pairs)==1
 hasse=confirm_acyclic(faces,pairs)
 # Drop the unique empty-cell pair: it becomes one 0-cell; deleting an
 # acyclic matched pair cannot introduce a directed cycle.
 critical=Counter({0:1})
 critical.update({d:sum(x.bit_count()-1==d for x in unmatched) for d in range(2,8) if any(x.bit_count()-1==d for x in unmatched)})
 dims=sorted(k for k in critical if k>0)
 betti=dict((d,critical[d]) for d in dims)
 pivots={}
 for d in dims:
  if d-1 not in critical:continue
  M=morse_matrix(unmatched,pairs,d)
  rank,leftover=unit_pivot_reduction(M)
  assert not leftover, 'Non-unit unsolved attaching data'
  pivots[d]=rank
  betti[d]-=rank
  betti[d-1]-=rank
 betti={k:v for k,v in betti.items() if v}
 expected=EXPECTED[n]
 if not reverse:
  assert (len(faces),len(pairs),dict(critical),betti,list(pivots.values())[0])==expected
 if with_gf2:
  mod2=gf2_ranks(faces,len(edges))
  assert mod2==betti,(n,mod2,betti)
 print('n=%d order=%s faces=%d matching_pairs=%d critical=%s unit_pivots=%s homotopy=%s Hasse_edges=%d gf2=%s' %
       (n,'reverse' if reverse else 'forward',len(faces),len(pairs),dict(critical),pivots,betti,hasse,with_gf2),flush=True)

if __name__=='__main__':
 for n in (6,7,8,9):
  verify(n,reverse=False,with_gf2=True)
  verify(n,reverse=True,with_gf2=False)
 print('ALL EXACT CHECKS PASS')
