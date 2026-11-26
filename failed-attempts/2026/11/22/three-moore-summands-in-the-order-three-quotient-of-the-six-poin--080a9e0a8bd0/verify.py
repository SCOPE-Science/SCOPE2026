import itertools,collections,sys,math

n=6
def part_recur(seq):
 if len(seq)==n:
  blocks=[]
  for j in range(max(seq)+1): blocks.append(tuple(i for i,v in enumerate(seq) if v==j))
  return [tuple(blocks)]
 out=[]
 for j in range(max(seq)+2):out+=part_recur(seq+[j])
 return out
parts=sorted([p for p in part_recur([0]) if 1<len(p)<n],key=lambda x:(n-len(x),x));P={p:i for i,p in enumerate(parts)}
def is_refine(a,b):
 return all(any(set(u)<=set(v) for v in b) for u in a)
upper={i: [j for j in range(len(parts)) if n-len(parts[j])>n-len(p) and is_refine(p,parts[j])] for i,p in enumerate(parts)}
byrank=collections.defaultdict(list)
for i,p in enumerate(parts):byrank[n-len(p)].append(i)
flags=set()
for i in range(len(parts)):
 flags.add((i,));work=[(i,)]
 while work:
  seq=work.pop()
  for j in upper[seq[-1]]:
   nxt=seq+(j,)
   flags.add(nxt);work.append(nxt)
perms=[tuple((i+k)%n for i in range(n)) for k in range(0,n,2)]
act=[]
for perm in perms:
 act.append([P[tuple(sorted(tuple(sorted(perm[v] for v in block)) for block in p))] for p in parts])
assert len(perms)==3
visited=set();cells=[]; orbit_of={}
for d in range(n-2):
 for f in sorted(x for x in flags if len(x)==d+1):
  if f in visited:continue
  orbit={tuple(a[i] for i in f) for a in act}
  visited.update(orbit)
  idx=len(cells)
  cells.append(f)
  for g in orbit:orbit_of[g]=idx
assert len(visited)==len(flags)
bd=[{} for _ in cells]
for j,f in enumerate(cells):
 if len(f)==1:continue
 for k in range(len(f)):
  i=orbit_of[f[:k]+f[k+1:]]
  bd[j][i]=bd[j].get(i,0)+(-1)**k
 bd[j]={i:v for i,v in bd[j].items() if v}
for j,f in enumerate(cells):
 if len(f)<3:continue
 assert not any(sum(u*bd[i].get(v,0) for i,u in bd[j].items()) for v in set().union(*(bd[i] for i in bd[j])))
cof=collections.defaultdict(set)
for i,ds in enumerate(bd):
 for j in ds:cof[j].add(i)
active=set(range(len(cells)));t=0;sch=[]
while True:
 pivot=None;best=10**18
 for u in active:
  for v,c in bd[u].items():
   if abs(c)!=1:continue
   cost=(len(bd[u])-1)*(len(cof[v])-1)
   if cost<best: pivot=(u,v);best=cost
   if best==0:break
  if best==0:break
 if pivot is None:break
 u,v=pivot;sg=bd[u][v]
 sch.append((u,v,sg))
 for uu in list(cof[v]):
  if uu==u:continue
  q=bd[uu][v]
  for w,c in bd[u].items():
   r=bd[uu].get(w,0)-q*sg*c
   if r:bd[uu][w]=r;cof[w].add(uu)
   else:bd[uu].pop(w,None);cof[w].discard(uu)
 for uu in list(cof[u]):
  if uu!=u: bd[uu].pop(u,None)
 for w in list(bd[u]):cof[w].discard(u)
 active.remove(u);active.remove(v);cof.pop(v,None);cof.pop(u,None)
 t+=1
assert len(parts)==201 and len(flags)==9011 and len(cells)==3009
assert tuple(sum(len(c)==d+1 for c in cells) for d in range(4))==(71,623,1415,900)
assert t==1482 and tuple(sum(len(cells[i])==d+1 for i in active) for d in range(4))==(1,0,3,41)
left=sorted(i for i in active if len(cells[i])==3)
right=sorted(i for i in active if len(cells[i])==4)
m=[[bd[j].get(i,0) for j in right] for i in left]
g1=math.gcd(*(v for row in m for v in row))
g2=0
g3=0
for a in range(len(right)):
 for b in range(a+1,len(right)):
  for i in range(3):
   for j in range(i+1,3):g2=math.gcd(g2,m[i][a]*m[j][b]-m[i][b]*m[j][a])
  for c in range(b+1,len(right)):
   v=(m[0][a]*(m[1][b]*m[2][c]-m[1][c]*m[2][b])
      -m[0][b]*(m[1][a]*m[2][c]-m[1][c]*m[2][a])
      +m[0][c]*(m[1][a]*m[2][b]-m[1][b]*m[2][a]))
   g3=math.gcd(g3,v)
assert (g1,g2,g3)==(3,9,27),(g1,g2,g3)
assert len([i for i in active if len(cells[i])==1])==1
print('PASS_PARTITION_LATTICE_SIX_ORDER_THREE_QUOTIENT_H2_Z3_CUBED_H3_Z38')
