"""Independent cut-side face and mod-two chain calculation, not used by main verifier."""
from itertools import combinations
from collections import defaultdict
from verify import graph,connected
_,pe,adj = graph(); n=len(adj); allmask=(1<<n)-1

def rank2(columns):
 piv={}
 for col in columns:
  while col:
   top=col.bit_length()-1
   if top in piv: col ^= piv[top]
   else: piv[top]=col;break
 return len(piv)

for k in (4,5):
 bad=[]
 for c in combinations(range(n),k):
  s=sum(1<<i for i in c)
  if not connected(s,adj):bad.append(s)
 fac=[allmask ^ b for b in bad]
 bydim=defaultdict(list)
 for face in range(1,1<<n):
  if any(face&f==face for f in fac):bydim[face.bit_count()-1].append(face)
 ranks={0:0}
 for d in range(1,max(bydim)+1):
  ix={f:i for i,f in enumerate(bydim[d-1])}
  def boundary():
   for f in bydim[d]:
    yield sum(1<<ix[f^(1<<i)] for i in range(n) if f>>i&1)
  ranks[d]=rank2(boundary())
 betti={d:len(bydim[d])-ranks[d]-ranks.get(d+1,0)-(d==0) for d in bydim}
 print('k=',k,'number of disconnected facets=',len(bad),'cut faces=',sum(map(len,bydim.values())),'cut nonzero mod2 Betti=',{d:b for d,b in betti.items() if b},flush=True)
 assert {d:b for d,b in betti.items() if b} == {15-k-1:{4:196,5:624}[k]}
