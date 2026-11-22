from functools import lru_cache
from collections import Counter, deque, defaultdict
from functools import reduce
from operator import or_
import json

@lru_cache(None)
def trees(h):
 if h==0:return (None,)
 prev=trees(h-1)
 return (None,)+tuple((a,b) for a in prev for b in prev)

def decoder(t):
 nodes=[]
 def traverse(x,path):
  if x is None:return
  nodes.append(path)
  traverse(x[0],path+'0');traverse(x[1],path+'1')
 traverse(t,'')
 ids={p:i for i,p in enumerate(nodes)}
 edges=[]
 for p in nodes:
  edges.append(tuple(ids.get(p+c,0) for c in '01'))
 return nodes,edges

def dist(t):
 nodes,edges=decoder(t)
 n=len(nodes)
 allmask=(1<<n)-1
 if n==1:return 0, '', n
 trans=[]
 for c in range(2):trans.append([reduce(or_,(1<<edges[i][c] for i in range(n) if (m>>i)&1),0) for m in range(1<<n)])
 seen={allmask:0}
 q=deque([allmask]);pre={}
 while q:
  m=q.popleft();d=seen[m]
  if m.bit_count()==1:
   word='';x=m
   while x!=allmask:
    pm,c=pre[x];word=str(c)+word;x=pm
   return d,word,n
  for c in range(2):
   nxt=trans[c][m]
   if nxt not in seen:
    seen[nxt]=d+1;pre[nxt]=(m,c);q.append(nxt)
 return None,None,n

def lengths(t):
 out=[]
 def walk(x,k):
  if x is None:out.append(k)
  else:
   walk(x[0],k+1);walk(x[1],k+1)
 walk(t,0);return tuple(sorted(out))

if __name__ == '__main__':
    expected = {None:19,1:2,2:20,3:44,4:92,5:96,6:56,7:50,8:144,9:118,10:4,11:2,12:2,17:2}
    measured = Counter()
    all_heights = Counter()
    maxima = []
    for tree in trees(4)[1:]:
        height = max(lengths(tree))
        d, word, n = dist(tree)
        all_heights[height] += 1
        if height == 4:
            measured[d] += 1
            if d == 17:
                maxima.append((tree,word,n))
    assert len(trees(4)) == 677
    assert all_heights == {1:1,2:3,3:21,4:651}
    assert measured == expected, (measured, expected)
    assert len(maxima)==2
    print('verified:', sum(measured.values()), 'depth-four codes; synchronized:', 651-measured[None])
    print('exact histogram:', sorted(measured.items(),key=lambda x: (-1 if x[0] is None else x[0])))
    print('extremal shortest witnesses:',[(w,n) for _,w,n in maxima])
