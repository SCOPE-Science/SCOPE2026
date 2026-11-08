from oct3_sym import G,conj_table
from itertools import combinations
import json
from pathlib import Path
D=json.load(open(Path(__file__).resolve().parent / 'oct3_chars.json'))

def szpart(n):
 if n==0:return [()]
 if n==1:return [(1,)]
 if n==2:return [(2,),(1,1)]
 if n==3:return [(3,),(2,1),(1,1,1)]
 raise ValueError

def schar(sh,p,dom):
 d=len(dom)
 perm=[p[i] for i in dom]
 if sh in [(),(1,),(2,),(3,)]:return 1
 sign=(-1)**sum(perm[i]>perm[j] for i in range(d) for j in range(i+1,d))
 if sh in [(1,1),(1,1,1)]:return sign
 if sh==(2,1):return sum(p[i]==i for i in dom)-1
 raise ValueError(sh)

def bipartchar(g,pos,neg):
 p=tuple(g[2*i]//2 for i in range(3));f=tuple(g[2*i]%2 for i in range(3))
 out=0
 for S in combinations(range(3),sum(neg)):
  if set(p[i] for i in S)!=set(S):continue
  T=tuple(i for i in range(3) if i not in S)
  out+=(-1)**sum(f[i] for i in S)*schar(pos,p,T)*schar(neg,p,S)
 return out
irreps=[(a,b) for k in range(4) for a in szpart(3-k) for b in szpart(k)]
cl=conj_table(G)
print('REP DIMS',[(x,bipartchar(tuple(range(6)),*x)) for x in irreps])
assert len(irreps)==10
for x in irreps:
 vec=[bipartchar(rep,*x) for rep,orb in cl]
 mult={nam:sum(d['class_size']*d[nam]*c for d,c in zip(D,vec))//48 for nam in ['H1','H2']}
 assert all(sum(d['class_size']*d[nam]*c for d,c in zip(D,vec))%48==0 for nam in ['H1','H2'])
 print(x,'char',vec,'multiplicities',mult)
print('DONE')
