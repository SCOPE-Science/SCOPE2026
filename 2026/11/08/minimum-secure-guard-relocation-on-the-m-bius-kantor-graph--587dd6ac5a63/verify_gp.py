"""Exhaustive secure-set and relocation computation for GP(8,3). Stdlib only."""
from itertools import combinations
from collections import Counter,deque
n=16
edges=sorted({tuple(sorted((a,b))) for i in range(8) for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8))})
assert len(edges)==24
nb=[0]*n
for a,b in edges:nb[a]|=1<<b;nb[b]|=1<<a
closed=[nb[i]|(1<<i) for i in range(n)]
FULL=(1<<n)-1
dom=[False]*(1<<n)
reach=[0]*(1<<n)
for m in range(1,1<<n):
 p=m&-m;reach[m]=reach[m^p]|closed[p.bit_length()-1]
 dom[m]=(reach[m]==FULL)

def secure(m):
 if not dom[m]:return False
 outsiders=FULL^m
 while outsiders:
  p=outsiders&-outsiders;outsiders^=p;v=p.bit_length()-1
  guards=m&nb[v];good=False
  while guards:
   q=guards&-guards;guards^=q
   if dom[(m^q)|p]:good=True;break
  if not good:return False
 return True
sol=[]
for k in range(8):
 xs=[]
 for v in combinations(range(n),k):
  m=sum(1<<x for x in v)
  if secure(m):xs.append(m)
 print('size',k,'secure',len(xs))
 if xs:sol=xs;break
assert k==7 and len(sol)==336
lookup=set(sol)
graphs={label:{s:set() for s in sol} for label in ('TJ','TS')}
for s in sol:
 for a in range(n):
  if not(s>>a&1):continue
  for b in range(n):
   if s>>b&1:continue
   t=s^(1<<a)^(1<<b)
   if t in lookup:
    graphs['TJ'][s].add(t)
    if nb[a]>>b&1:graphs['TS'][s].add(t)

def report(g):
 un=set(sol); comps=[]
 while un:
  u=next(iter(un));q=[u];un.remove(u)
  for v in q:
   for w in g[v]:
    if w in un:q.append(w);un.remove(w)
  comps.append(q)
 ecc=[]
 for c in comps:
  for u in c:
   d={u:0};q=deque([u])
   while q:
    v=q.popleft()
    for w in g[v]:
     if w not in d:d[w]=d[v]+1;q.append(w)
   assert len(d)==len(c)
   ecc.append((len(c),max(d.values())))
 print('edges',sum(len(s) for s in g.values())//2,'component_sizes',sorted(Counter(map(len,comps)).items()),'degrees',sorted(Counter(len(x) for x in g.values()).items()),'component_ecc',sorted(Counter(ecc).items()))
 return comps
print('TJ'); t=report(graphs['TJ'])
print('TS'); s=report(graphs['TS'])
assert len(t)==1 and len(t[0])==336
assert sorted(map(len,s))==[2]*24+[288]
assert sum(map(len,graphs['TJ'].values()))//2==1392
assert sum(map(len,graphs['TS'].values()))//2==528
print('VERIFIED_GP')
