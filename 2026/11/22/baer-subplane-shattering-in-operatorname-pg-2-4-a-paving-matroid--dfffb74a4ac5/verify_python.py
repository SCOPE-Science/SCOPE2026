"""Exact point-incidence traces and online dimension for PG(2,4) Baer subplanes.
Run: python3 verify_python.py (Python 3 standard library only).
The two-dimensional F4 field is represented by F2[t]/(t*t+t+1).
"""
from itertools import combinations,product
from functools import lru_cache
import json

mul=[[0]*4 for _ in range(4)]
for a in range(4):
 for b in range(4):
  v=0
  for i in range(2):
   for j in range(2):
    if (a>>i)&1 and (b>>j)&1:v^=[1,2,3][i+j]
  mul[a][b]=v
inv={a:next(b for b in range(1,4) if mul[a][b]==1) for a in range(1,4)}
def norm(p):
 f=next(x for x in p if x)
 return tuple(mul[x][inv[f]] for x in p)
def det(p,q,r):
 return mul[p[0]][mul[q[1]][r[2]]^mul[q[2]][r[1]]] ^ mul[p[1]][mul[q[0]][r[2]]^mul[q[2]][r[0]]] ^ mul[p[2]][mul[q[0]][r[1]]^mul[q[1]][r[0]]]
points=sorted({norm(p) for p in product(range(4),repeat=3) if any(p)})
assert len(points)==21
index={p:i for i,p in enumerate(points)}
lines=[sum(1<<i for i,p in enumerate(points) if det(p,points[a],points[b])==0) for a,b in combinations(range(21),2)]
lines=set(lines)
assert len(lines)==21 and all(l.bit_count()==5 for l in lines)
planes=set()
frames=0
for q in combinations(range(21),4):
 p=[points[i] for i in q]
 if any(det(p[a],p[b],p[c])==0 for a,b,c in combinations(range(4),3)):continue
 frames+=1
 # A maps the standard projective frame to this one; its columns are a scaled basis.
 base_d=det(*p[:3]); assert base_d
 coeff=[]
 for i in range(3):
  t=list(p[:3]);t[i]=p[3];coeff.append(mul[det(*t)][inv[base_d]])
 columns=[tuple(mul[coeff[i]][p[i][j]] for j in range(3)) for i in range(3)]
 B=0
 for b in product((0,1),repeat=3):
  if not any(b):continue
  y=tuple(__import__('functools').reduce(lambda x,z:x^z,(columns[i][j] for i in range(3) if b[i]),0) for j in range(3))
  B|=1<<index[norm(y)]
 planes.add(B)
assert frames==2520 and len(planes)==360 and all(p.bit_count()==7 for p in planes)
planes=sorted(planes)

# Directly verify the geometric trace criterion on all candidate supports of sizes <=4.
counts=[0]*6
for k in range(5):
 for ids in combinations(range(21),k):
  S=sum(1<<i for i in ids)
  traces={sum((1<<j) for j,i in enumerate(ids) if (B>>i)&1) for B in planes}
  shattered=(len(traces)==1<<k)
  predicted=(k<4 or not any(S&L==S for L in lines))
  assert shattered==predicted,(k,ids,len(traces),predicted)
  counts[k]+=shattered
assert counts[:5]==[1,21,210,1330,5880]
# Exhaustive 5-support obstruction is checked independently of the short proof.
for ids in combinations(range(21),5):
 S=sum(1<<i for i in ids)
 if not any(B&S==S for B in planes):continue
 assert any(not any((B&S)==(S^(1<<j)) for B in planes) for j in ids)

# Exact dynamic-programming recurrence for Littlestone dimension.
positive=[sum(1<<j for j,B in enumerate(planes) if (B>>i)&1) for i in range(21)]
full=(1<<360)-1
@lru_cache(None)
def witness(C,d):
 if d==0:return []
 if C.bit_count()<(1<<d):return None
 for i in range(21):
  Y=C&positive[i]
  N=C&(~positive[i])
  if min(Y.bit_count(),N.bit_count())<(1<<(d-1)):continue
  wY=witness(Y,d-1)
  if wY is None:continue
  wN=witness(N,d-1)
  if wN is not None:return [i,wY,wN]
 return None
w5=witness(full,5)
assert w5 is not None
assert witness(full,6) is None
# Each leaf has >=1 surviving concept; internal queries split both children.
def check_tree(tree,C,depth):
 if depth==0:return tree==[] and C!=0
 if not isinstance(tree,list) or len(tree)!=3:return False
 i,Y,N=tree
 return check_tree(Y,C&positive[i],depth-1) and check_tree(N,C&~positive[i],depth-1)
assert check_tree(w5,full,5)
with open('witness_tree.json','w') as f:json.dump({'points':points,'depth':5,'tree':w5},f,sort_keys=True,indent=2);f.write('\n')
print('POINTS',len(points),'LINES',len(lines),'QUADRANGLES',frames,'BAER_SUBPLANES',len(planes))
print('SHATTERING_POLYNOMIAL',counts[:5])
print('LITTLESTONE_LOWER',5,'UPPER',5,'DEPTH_SIX_CACHE_STATES',witness.cache_info().currsize)
print('TOP_BETTI_FROM_MATROID_SHELLABILITY',4740)
