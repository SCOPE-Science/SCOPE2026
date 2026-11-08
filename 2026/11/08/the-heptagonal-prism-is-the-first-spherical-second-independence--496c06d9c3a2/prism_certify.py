from collections import Counter,deque
N=7
order=(11,4,0,8,9,1,2,7,3,12,13,6,10,5)

def graph(n):
 edges={tuple(sorted((j*n+i,j*n+(i+1)%n))) for j in range(2) for i in range(n)}
 edges.update((i,n+i) for i in range(n))
 return tuple(sorted(edges))

def facesA(n):
 N=2*n; nbr=[set() for _ in range(N)]
 for u,v in graph(n):nbr[u].add(v);nbr[v].add(u)
 forbidden=set()
 for v in range(N):
  q=sorted(nbr[v]);
  for i in range(len(q)):
   for j in range(i+1,len(q)):
    forbidden.add((1<<q[i])|(1<<v)|(1<<q[j]))
 fs={s for s in range(1,1<<N) if all(s&t!=t for t in forbidden)}
 return fs,forbidden

def facesB(n):
 N=2*n; adj=[0]*N
 for u,v in graph(n): adj[u]|=1<<v;adj[v]|=1<<u
 F=set()
 for s in range(1,1<<N):
  rem=s; good=True
  while rem:
   v=(rem&-rem).bit_length()-1
   component=1<<v; recent=component
   while recent:
    expand=0;m=recent
    while m:
     b=m&-m; m-=b; w=b.bit_length()-1
     expand|=adj[w]&s&~component
    component |= expand
    recent=expand
    if component.bit_count()>2:good=False;break
   if not good:break
   rem &= ~component
  if good:F.add(s)
 return F

def matching(F,order):
 rem=set(F);pairs=[]
 for v in order:
  b=1<<v
  for s in sorted([s for s in rem if not (s&b)]):
   t=s|b
   if t in rem:rem.remove(s);rem.remove(t);pairs.append((s,t))
 return rem,pairs

def verify_matching(F,crit,pairs,n):
 assert len(F)==2*len(pairs)+len(crit)
 md={(s,t) for s,t in pairs}
 assert len(md)==len(pairs)
 assert not set(crit)&{v for s,t in pairs for v in (s,t)}
 neighbors={s:[] for s in F};indeg={s:0 for s in F};count=0
 for high in F:
  for v in range(2*n):
   b=1<<v
   if high&b:
    low=high^b
    if low in F:
     count+=1
     start,end=(low,high) if (low,high) in md else (high,low)
     neighbors[start].append(end); indeg[end]+=1
 todo=deque([s for s in indeg if indeg[s]==0]);seen=0
 while todo:
  s=todo.popleft();seen+=1
  for t in neighbors[s]:
   indeg[t]-=1
   if indeg[t]==0:todo.append(t)
 assert seen==len(F),(seen,len(F))
 return count

for n in range(3,8):
 F,forbidden=facesA(n)
 assert F==facesB(n)
 fv=dict(sorted(Counter(s.bit_count()-1 for s in F).items()))
 redchi=sum((-1)**d*c for d,c in fv.items())-1
 if n==7:
  crit,pairs=matching(F,order)
  cnt=Counter(s.bit_count()-1 for s in crit)
  edges=verify_matching(F,crit,pairs,n)
  assert cnt=={0:1,5:1},cnt
  print('PRISM_7_CERTIFICATE:',len(graph(n)),'graph_edges',len(forbidden),'forbidden_triples',len(F),'faces',len(pairs),'matched_pairs',len(crit),'critical_cells',edges,'incidences','critical_masks',sorted(crit),'pivot_order',order)
 print('PRISM_N',n,'FV',fv,'RED_CHI',redchi)
print('ALL_CHECKS_PASS')

F,_=facesA(7)
bydim={d:sorted(s for s in F if s.bit_count()==d+1) for d in range(7)}
ranks={}
for d in range(1,7):
 lower=bydim[d-1]; rows={mask:i for i,mask in enumerate(lower)}
 pivots={}
 for s in bydim[d]:
  vec=0
  for v in range(14):
   if s&(1<<v):vec^=1<<rows[s^(1<<v)]
  while vec:
   p=vec.bit_length()-1
   if p in pivots:vec^=pivots[p]
   else:pivots[p]=vec;break
 ranks[d]=len(pivots)
betti={d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in bydim}
assert betti=={0:1,1:0,2:0,3:0,4:0,5:1,6:0},betti
print('GF2_BOUNDARY_RANKS',ranks,'BETTI',betti)
print('ALL_INTEGRAL_HOMOTOPY_AND_INDEPENDENT_MOD2_CHECKS_PASS')
