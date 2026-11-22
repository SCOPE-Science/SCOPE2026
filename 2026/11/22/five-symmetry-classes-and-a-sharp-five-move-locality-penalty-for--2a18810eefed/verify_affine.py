"""Exact power-domination and one-token relocation check, affine-incidence model.
Standard library only. Run with python3 verify_affine.py.
"""
from itertools import combinations
from collections import Counter, deque
N=18
neighbors=[0]*N
for x in range(3):
 for y in range(3):
  p=3*x+y
  for c in range(3):
   for ell,flag in ((9+c,x==c),(12+c,y==c),(15+c,(y-x)%3==c)):
    if flag:
     neighbors[p]|=1<<ell
     neighbors[ell]|=1<<p
assert all(t.bit_count()==3 for t in neighbors)
def works(mask):
 observed=mask
 for v in range(N):
  if mask>>v&1:observed|=neighbors[v]
 while True:
  expanded=observed
  for v in range(N):
   if observed>>v&1:
    missing=neighbors[v]&~observed
    if missing and not missing&(missing-1):expanded|=missing
  if expanded==observed:return observed==(1<<N)-1
  observed=expanded
counts=[]
for k in range(1,4):
 a=[sum(1<<i for i in s) for s in combinations(range(N),k) if works(sum(1<<i for i in s))]
 counts.append(len(a))
assert counts==[0,0,486], counts
states=a;index={s:i for i,s in enumerate(states)}
jump=[set() for _ in states];slide=[set() for _ in states]
for i,s in enumerate(states):
 for x in range(N):
  if not (s>>x&1):continue
  for y in range(N):
   if s>>y&1:continue
   t=s^(1<<x)^(1<<y)
   if t in index:
    j=index[t];jump[i].add(j)
    if neighbors[x]>>y&1:slide[i].add(j)
def distances(graph,start):
 d={start:0};q=deque([start])
 while q:
  i=q.popleft()
  for j in graph[i]:
   if j not in d:d[j]=d[i]+1;q.append(j)
 assert len(d)==len(states)
 return d
jump_dist=Counter();slide_dist=Counter();penalty=Counter();center=Counter();degree=Counter()
exception=0;maxpairs=0
for i in range(len(states)):
 dj=distances(jump,i);ds=distances(slide,i)
 center[max(ds.values())]+=1
 degree[(len(jump[i]),len(slide[i]),max(ds.values()))]+=1
 for j in range(i+1,len(states)):
  jdist,sdist=dj[j],ds[j]
  jump_dist[jdist]+=1;slide_dist[sdist]+=1;penalty[sdist-jdist]+=1
  ambient=3-(states[i]&states[j]).bit_count()
  assert jdist>=ambient
  if jdist>ambient:exception+=1
  if sdist-jdist==5:maxpairs+=1
assert sum(map(len,jump))//2==7128
assert sum(map(len,slide))//2==1620
assert jump_dist=={1:7128,2:43902,3:66825},jump_dist
assert slide_dist=={1:1620,2:6480,3:18063,4:31644,5:33912,6:20358,7:5454,8:324},slide_dist
assert penalty=={0:9423,1:29808,2:42174,3:28026,4:7938,5:486},penalty
assert center=={7:54,8:432},center
assert exception==162 and maxpairs==486
assert degree=={(28,7,8):108,(29,8,8):108,(29,6,8):108,(28,5,8):108,(36,8,7):54},degree
# Full symmetry group of the Pappus incidence graph, provided as checkable generators.
generators=[
(3,4,5,6,7,8,0,1,2,10,11,9,12,13,14,17,15,16),
(1,2,0,4,5,3,7,8,6,9,10,11,13,14,12,16,17,15),
(0,3,6,1,4,7,2,5,8,12,13,14,9,10,11,15,17,16),
(0,4,8,6,1,5,3,7,2,15,16,17,12,13,14,9,10,11),
(9,12,15,13,17,11,16,10,14,0,7,5,1,3,8,2,6,4),
]
for g in generators:
 assert sorted(g)==list(range(N))
 assert all(((neighbors[i]>>j)&1)==((neighbors[g[i]]>>g[j])&1) for i in range(N) for j in range(N))
identity=tuple(range(N));seen={identity};queue=[identity]
for p in queue:
 for g in generators:
  q=tuple(g[p[i]] for i in range(N))
  if q not in seen:seen.add(q);queue.append(q)
assert len(seen)==216
unused=set(states);orbits=[]
while unused:
 s=next(iter(unused));orb=set()
 for g in seen:
  t=sum(1<<g[i] for i in range(N) if s>>i&1)
  orb.add(t)
 assert orb<=unused
 unused-=orb
 orbits.append((len(orb),len(jump[index[s]]),len(slide[index[s]]),max(distances(slide,index[s]).values())))
assert Counter(orbits)=={(108,28,7,8):1,(108,29,8,8):1,(108,29,6,8):1,(108,28,5,8):1,(54,36,8,7):1},orbits
print('PASS affine; min=(0,0,486), edges=(7128,1620), all pairs=117855')
print('jump',sorted(jump_dist.items()),'slide',sorted(slide_dist.items()))
print('penalty',sorted(penalty.items()),'orbit sizes',sorted(orbits))
