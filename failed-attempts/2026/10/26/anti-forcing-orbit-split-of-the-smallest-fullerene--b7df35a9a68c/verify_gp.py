"""Exhaustive anti-forcing census for the 20-vertex dodecahedral graph.

Python >=3.9, standard library only. No external datasets.
"""
import itertools, collections, hashlib, json, functools
N=10
edges=set()
for i in range(N):
 for u,v in ((i,(i+1)%N),(i,N+i),(N+i,N+(i+2)%N)):
  edges.add(tuple(sorted((u,v))))
E=sorted(edges)
assert len(E)==30
adj=[[] for _ in range(20)]
for j,(u,v) in enumerate(E):
 adj[u].append((v,j));adj[v].append((u,j))
@functools.lru_cache(None)
def match(free):
 if free==0:return (0,)
 u=(free&-free).bit_length()-1
 return tuple((1<<e)|rest for v,e in adj[u] if free&(1<<v)
              for rest in match(free^(1<<u)^(1<<v)))
P=sorted(match((1<<20)-1));assert len(P)==36 and len(set(P))==36

def profile(m):
 a=[[] for _ in range(20)]
 for j,(u,v) in enumerate(E):
  if not(m>>j)&1:a[u].append(v);a[v].append(u)
 assert all(len(x)==2 for x in a)
 seen=set();parts=[]
 for i in range(20):
  if i in seen:continue
  st=[i];seen.add(i);sz=0
  while st:
   u=st.pop();sz+=1
   for v in a[u]:
    if v not in seen:seen.add(v);st.append(v)
  parts.append(sz)
 return tuple(sorted(parts))

byk={};first={}; exact=collections.Counter()
for k in range(6):
 count=collections.Counter();survivor_witness={}
 for ids in itertools.combinations(range(30),k):
  F=sum(1<<j for j in ids)
  survivors=[p for p in P if not (p&F)]
  if len(survivors)==1:
   p=survivors[0];count[p]+=1
   survivor_witness.setdefault(p,list(ids))
 for p in P:
  if p not in first and p in survivor_witness:first[p]=(k,survivor_witness[p])
 byk[k]=dict(count)
 exact[k]=sum(count.values())
assert len(first)==36
hist=collections.Counter((profile(p),first[p][0]) for p in P)
assert hist=={((20,),4):30,((5,5,10),5):6},hist
for p in P:
 k,w=first[p]
 assert len(w)==k and not any((p>>j)&1 for j in w)
 assert sum(not (q & sum(1<<j for j in w)) for q in P)==1
assert exact[3]==0 and exact[4]==240 and exact[5]==7272
assert {len(byk[4]) ,len(byk[5])}=={30,36}
assert all(byk[4].get(p,0)==(8 if profile(p)==(20,) else 0) for p in P)
assert all(byk[5].get(p,0)==(238 if profile(p)==(20,) else 22) for p in P)
rows=[dict(matching=m,profile=profile(m),minimum=first[m][0],num_minimal=byk[first[m][0]][m],witness_edges=[E[j] for j in first[m][1]]) for m in P]
digest=hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print(json.dumps({'graph':'GP(10,2)','vertices':20,'edges':30,'perfect_matchings':len(P),
 'profile_anti_histogram':{str(k):v for k,v in sorted(hist.items())},
 'unique_survivor_deletion_sets_k0_to_k5':{str(k):exact[k] for k in range(6)},
 'per_match_minimal_deletion_sets_by_class':{'Hamilton_complement':8,'three_cycle_complement':22},
 'rows_sha256':digest,'all_verified':True},sort_keys=True,indent=2))
