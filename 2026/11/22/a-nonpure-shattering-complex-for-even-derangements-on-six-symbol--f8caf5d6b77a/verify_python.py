from itertools import permutations,combinations
from collections import Counter
from math import comb
n=6

def parity(p):return sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))%2
cl=[p for p in permutations(range(n)) if parity(p)==0 and all(i!=p[i] for i in range(n))]
edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
shat=[set() for _ in range(7)]
for k in range(6):
 for cols in combinations(range(n),k):
  for rows in combinations(range(n),k):
   for image in permutations(cols):
    pairs=tuple(zip(rows,image))
    if any(i==j for i,j in pairs):continue
    S=sum(1<<edges.index(pair) for pair in pairs)
    if len({sum(1<<j for j,(i,v) in enumerate(pairs) if p[i]==v) for p in cl})==1<<k:shat[k].add(S)
 print(k,len(shat[k]),flush=True)
assert len(cl)==130
assert [len(shat[k]) for k in range(6)]==[1,30,315,1420,1140,0]
facets=[]
allf=set.union(*shat)
for s in allf:
 if not any((s|(1<<i)) in allf for i in range(len(edges)) if not s>>i&1):facets.append(s)
print('facets sizes',Counter(s.bit_count() for s in facets))
assert Counter(s.bit_count() for s in facets)=={3:360,4:1140}
ranks=[]
for k in range(1,6):
 if not shat[k]: continue
 ids={x:i for i,x in enumerate(shat[k-1])}
 basis={};r=0
 for s in shat[k]:
  b=0
  for i in range(30):
   if s>>i&1:b^=1<<ids[s^(1<<i)]
  while b:
   m=b.bit_length()-1
   if m not in basis:basis[m]=b;r+=1;break
   b^=basis[m]
 print('boundary rank k',k,r)
 ranks.append(r)
assert ranks==[1,29,286,750]
group=list(permutations(range(n)))
sets_by_k={k:set(s for s in facets if s.bit_count()==k) for k in (3,4)}
for k in [3,4]:
 rest=sets_by_k[k].copy();sizes=[];examples=[]
 while rest:
  s=min(rest); pairs=[edges[i] for i in range(len(edges)) if s>>i&1]
  orbit=set()
  for perm in group:
   m=0
   for (a,b) in pairs:m|=1<<edges.index((perm[a],perm[b]))
   orbit.add(m)
  assert orbit<=sets_by_k[k]
  sizes.append(len(orbit));examples.append(pairs);rest-=orbit
 print('facets k',k,'orbit sizes',sizes, 'representatives',examples)
 assert sorted(sizes)==([360] if k==3 else [180,240,360,360])

assert len(shat[5])==0
print("EVEN_DERANGEMENT_PYTHON_PASS")
