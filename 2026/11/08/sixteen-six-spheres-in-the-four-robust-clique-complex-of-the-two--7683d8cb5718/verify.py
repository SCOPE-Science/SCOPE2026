from itertools import combinations
from collections import Counter, defaultdict, deque
from functools import lru_cache
m=6; edges=list(combinations(range(m),2));N=len(edges)
valid=set()
for x in range(1,1<<N):
 deg=[0]*m
 for i,(a,b) in enumerate(edges):
  if x>>i&1:deg[a]+=1;deg[b]+=1
 if max(deg)<=3:valid.add(x)
rem=set(valid);lower={};upper={};pairs=[]
for i in range(N):
 bit=1<<i;curr=[]
 for x in sorted(rem):
  if not (x&bit) and (x|bit) in rem:curr.append((x,x|bit))
 for a,b in curr:
  rem.remove(a);rem.remove(b);lower[a]=b;upper[b]=a
 pairs+=curr
print('F',len(valid),'match',len(pairs),'critical',Counter(x.bit_count()-1 for x in rem),flush=True)
assert len(valid)==12067 and len(rem)==25
# acyclic directed Hasse
indeg={v:0 for v in valid};out={v:[] for v in valid}
for u in valid:
 t=u
 while t:
  v=t&-t;t-=v;l=u^v
  if not l:continue
  if upper.get(u)==l: a,b=l,u
  else:a,b=u,l
  out[a].append(b);indeg[b]+=1
q=deque(v for v in valid if indeg[v]==0);num=0
while q:
 v=q.popleft();num+=1
 for w in out[v]:
  indeg[w]-=1
  if indeg[w]==0:q.append(w)
print('DAG',num,len(valid),flush=True);assert num==len(valid)
def bd(x):
 b=x;idx=0
 while b:
  v=b&-b;b-=v
  l=x^v
  yield l,(-1)**idx
  idx+=1
@lru_cache(maxsize=None)
def reduceface(l):
 if l in rem:return {l:1}
 if l in upper:return {} # upper partner in lower dimension matching
 u=lower[l]
 sgn=dict(bd(u))[l]
 acc=defaultdict(int)
 for face,sgn_f in bd(u):
  if face==l:continue
  for k,v in reduceface(face).items():acc[k]-=sgn_f*sgn*v
 return {k:v for k,v in acc.items() if v}
crit={d:sorted([x for x in rem if x.bit_count()-1==d]) for d in [0,5,6,7]}
for d in [6,7]:
 print('Calculating differential',d,flush=True)
 mat=[]
 for c in crit[d]:
  acc=defaultdict(int)
  for l,sgn in bd(c):
   for k,v in reduceface(l).items():acc[k]+=sgn*v
  mat.append([acc.get(k,0) for k in crit[d-1]])
 print('shape',len(mat),len(mat[0]),'matrix',mat,flush=True)
print('Cache',reduceface.cache_info())
# Independent identification with four-robust clique complex of KG(6,2).
stars=[{i for i,(a,b) in enumerate(edges) if t in (a,b)} for t in range(m)]
independent_four=[]
for family in combinations(range(N),4):
    if all(len(set(edges[i])&set(edges[j]))>0 for i,j in combinations(family,2)):
        independent_four.append(frozenset(family))
star_four={frozenset(t) for star in stars for t in combinations(sorted(star),4)}
assert set(independent_four)==star_four and len(independent_four)==len(star_four)==30
for f in range(1,1<<N):
    robust=not any(all((f>>i)&1 for i in bad) for bad in independent_four)
    assert robust==(f in valid)
assert len(pairs)==6021
assert Counter(x.bit_count()-1 for x in rem)=={0:1,5:1,6:20,7:3}
D6=[];D7=[]
for d in (6,7):
    mat=[]
    for c in crit[d]:
        acc=defaultdict(int)
        for l,sgn in bd(c):
            for k,v in reduceface(l).items():acc[k]+=sgn*v
        mat.append([acc.get(k,0) for k in crit[d-1]])
    if d==6:D6=mat
    else:D7=mat
assert len(D6)==20 and all(len(r)==1 for r in D6)
assert len(D7)==3 and all(len(r)==20 for r in D7)
assert [sum(D7[i][j]*D6[j][0] for j in range(20)) for i in range(3)]==[0,0,0]
assert sorted(set(v for row in D6 for v in row))==[-1,0,1]
from itertools import permutations
selected=(0,2,4,10)
minor=[[row[j] for j in selected] for row in [[r[0] for r in D6]]+D7]
det=0
for p in permutations(range(4)):
    inversions=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    term=(-1)**inversions
    for i in range(4):term*=minor[i][p[i]]
    det+=term
assert abs(det)==1,(minor,det)
# The degree-six chain group is Z^20; the degree-five map is primitive,
# and the three degree-seven images jointly form a primitive rank-four subgroup
# with the degree-five row: hence H6=Z^16 and no other reduced homology.
print('ALL_VERIFY_OK f=12067 pairs=6021 critical=(1,1,20,3) unit_minor='+str(det)+' rank_H6=16',flush=True)
