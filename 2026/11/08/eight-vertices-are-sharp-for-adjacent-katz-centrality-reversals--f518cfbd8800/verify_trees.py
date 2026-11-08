"""Independent Prüfer-code construction of all isomorphism classes of trees through order eight."""
from itertools import product
from heapq import heapify, heappop,heappush
import networkx as nx

def key(adj):
 n=len(adj); deg=[len(x) for x in adj]
 leaves=[u for u in range(n) if deg[u]<=1]
 remaining=n
 while remaining>2:
  new=[]
  for u in leaves:
   deg[u]=0;remaining-=1
   for v in adj[u]:
    if deg[v]>0:
     deg[v]-=1
     if deg[v]==1:new.append(v)
  leaves=new
 def canon(u,p):
  return '('+''.join(sorted(canon(v,u) for v in adj[u] if v!=p))+')'
 centers=leaves
 return min(canon(c,-1) for c in centers)

def prufer_adj(n,seq):
 deg=[1]*n
 for x in seq:deg[x]+=1
 leaves=[i for i,d in enumerate(deg) if d==1];heapify(leaves)
 adj=[[] for _ in range(n)]
 for x in seq:
  leaf=heappop(leaves);adj[leaf].append(x);adj[x].append(leaf)
  deg[leaf]-=1;deg[x]-=1
  if deg[x]==1:heappush(leaves,x)
 u,v=leaves
 adj[u].append(v);adj[v].append(u)
 return adj

def run():
 for n in range(2,9):
  brute={key(prufer_adj(n,s)) for s in product(range(n),repeat=n-2)}
  nets={key([list(G.neighbors(u)) for u in range(n)]) for G in nx.nonisomorphic_trees(n)}
  assert brute==nets, (n,len(brute),len(nets),brute-nets,nets-brute)
  print('n',n,'classes',len(brute),'prufer codes',n**(n-2))
if __name__=='__main__':run()
