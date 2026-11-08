"""Complete exact edge-metric Chvatal-graph basis/mobility census, bitmask method."""
from itertools import combinations
from collections import deque,Counter
EDGES=[(0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11)]
n=12
adj=[set() for _ in range(n)]
for a,b in EDGES: adj[a].add(b);adj[b].add(a)
assert Counter(map(len,adj))=={4:12}
D=[]
for s in range(n):
 d={s:0};q=deque([s])
 while q:
  u=q.popleft()
  for v in adj[u]:
   if v not in d:d[v]=d[u]+1;q.append(v)
 assert len(d)==n
 D.append([min(d[a],d[b]) for a,b in EDGES])
P=list(combinations(range(len(EDGES)),2));m=[]
for v in range(n):m.append(sum(1<<i for i,(a,b) in enumerate(P) if D[v][a]!=D[v][b]))
allmask=(1<<len(P))-1
C={}
for k in range(6):
 C[k]=[s for s in combinations(range(n),k) if __import__('functools').reduce(int.__or__,(m[x] for x in s),0)==allmask]
assert [len(C[k]) for k in range(6)]==[0,0,0,0,0,192]
B=C[5];idx={t:i for i,t in enumerate(B)}
J=[set() for _ in B];S=[set() for _ in B]
for i,t in enumerate(B):
 st=set(t)
 for v in t:
  for w in range(n):
   if w in st:continue
   z=tuple(sorted((st-{v})|{w}));j=idx.get(z)
   if j is not None:
    J[i].add(j)
    if w in adj[v]:S[i].add(j)
def groups(A):
 unseen=set(range(len(A)));out=[]
 while unseen:
  v=unseen.pop();q=[v];c=0
  for u in q:
   c+=1
   for w in A[u]:
    if w in unseen:unseen.remove(w);q.append(w)
  out.append(c)
 return Counter(out)
def ecc(A):
 out=[]
 for u in range(len(A)):
  d={u:0};q=deque([u])
  while q:
   v=q.popleft()
   for w in A[v]:
    if w not in d:d[w]=d[v]+1;q.append(w)
  out.append(max(d.values()))
 return Counter(out)
assert sum(map(len,J))//2==1152 and sum(map(len,S))//2==428
assert groups(J)==groups(S)=={192:1}
assert ecc(J)=={5:192} and ecc(S)=={6:120,7:72}
assert Counter(map(len,S))=={2:28,3:32,4:48,5:32,6:32,7:8,8:8,10:4}
print('basis_counts_by_size',[len(C[k]) for k in range(6)])
print('jump_edges=1152 jump_components=1 jump_ecc={5:192}')
print('slide_edges=428 slide_components=1 slide_degree='+str(dict(sorted(Counter(map(len,S)).items()))))
print('slide_ecc={6:120,7:72} slide_radius=6 slide_diameter=7')
print('PASS')
