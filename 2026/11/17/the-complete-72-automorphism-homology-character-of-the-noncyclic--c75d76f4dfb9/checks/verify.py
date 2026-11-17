import networkx as nx
from itertools import combinations
from collections import defaultdict, Counter
L=[[0,1,2,3,4],[1,0,3,4,2],[2,3,4,0,1],[3,4,1,2,0],[4,2,0,1,3]]
G=nx.Graph();G.add_nodes_from(range(25))
for a in range(25):
 for b in range(a+1,25):
  i,j=divmod(a,5);k,l=divmod(b,5)
  if i==k or j==l or L[i][j]==L[k][l]:G.add_edge(a,b)
F={k:[] for k in range(1,6)}
for c in nx.enumerate_all_cliques(G):
 F[len(c)].append(tuple(sorted(c)))
print('f', {k:len(v) for k,v in F.items()})
fs=[set(map(frozenset,F[k])) for k in range(1,6)]
d=defaultdict(list)
for p in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter():
 cyc=[];vis=set()
 for v in range(25):
  if v in vis:continue
  u=v;n=0
  while u not in vis:vis.add(u);n+=1;u=p[u]
  cyc.append(n)
 traces=[]
 for k in range(1,6):
  s=0
  for f in F[k]:
   perm=[p[a] for a in f]
   if set(perm)!=set(f):continue
   inversions=sum(perm[i]>perm[j] for i in range(k) for j in range(i+1,k))
   s+=(-1)**inversions
  traces.append(s)
 chi=sum((-1)**j*x for j,x in enumerate(traces))-1
 d[tuple(sorted(cyc))].append(chi)
print('aut count',sum(len(v) for v in d.values()))
for c,v in sorted(d.items(),key=lambda x:(len(x[0]),x[0])):print(c,len(v),Counter(v))
print('invariant rank',sum(sum(v) for v in d.values())//72,'char total',sum(sum(v) for v in d.values()))
def r2(cols):
 b={}
 for x in cols:
  while x:
   i=x.bit_length()-1
   if i not in b:b[i]=x;break
   x^=b[i]
 return len(b)
ranks=[]
for k in range(2,6):
 index={f:i for i,f in enumerate(F[k-1])};cols=[]
 for f in F[k]:
  z=0
  for v in f:z^=1<<index[tuple(u for u in f if u!=v)]
  cols.append(z)
 ranks.append(r2(cols))
print('boundary ranks mod2',ranks)
print('betti reduced mod2',(len(F[1])-1-ranks[0],len(F[2])-ranks[0]-ranks[1],len(F[3])-ranks[1]-ranks[2],len(F[4])-ranks[2]-ranks[3],len(F[5])-ranks[3]))

assert len(F[1])==25 and len(F[2])==150 and len(F[3])==250 and len(F[4])==79 and len(F[5])==15
assert ranks==[24,126,64,15]
assert sum(len(v) for v in d.values())==72
assert sum(sum(v) for v in d.values())==0
assert d[tuple([1]*25)]==[60]
print("LATIN5_NONCYCLIC_EQUIVARIANT_PASS")
