"""Independent dodecahedral anti-forcing census using a 20-cycle LCF encoding.

Python >=3.9, standard library only; matching search and deletion search
are independent of the generalized-Petersen verifier.
"""
import itertools, collections, json, hashlib
shifts=[10,7,4,-4,-7,10,-4,7,-7,4]*2
H=sorted({tuple(sorted((i,(i+1)%20))) for i in range(20)}|
         {tuple(sorted((i,(i+shifts[i])%20))) for i in range(20)})
assert len(H)==30
A=[set() for _ in range(20)]
for i,j in H:A[i].add(j);A[j].add(i)
assert all(len(t)==3 for t in A)
# Independent explicit isomorphism from GP(10,2) index to LCF index.
phi=[0,1,8,7,14,15,16,17,18,19,10,2,9,6,13,5,12,4,11,3]
assert len(set(phi))==20
GP=set()
for i in range(10):
 for x,y in [(i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10)]:GP.add(tuple(sorted((x,y))))
assert {tuple(sorted((phi[x],phi[y]))) for x,y in GP}==set(H)

P=[]
def dfs(rest,selected):
 if not rest:
  P.append(tuple(sorted(selected)));return
 i=min(rest)
 for j in sorted(A[i]&rest):
  dfs(rest-{i,j},selected+[(i,j)])
dfs(set(range(20)),[])
assert len(P)==36 and len(set(P))==36
pbits=[]
for p in P:pbits.append(frozenset(tuple(sorted(e)) for e in p))

def cycles(m):
 remaining={v:set(A[v]) for v in range(20)}
 for u,v in m:remaining[u].remove(v);remaining[v].remove(u)
 seen=set();profile=[]
 for s in range(20):
  if s in seen:continue
  todo=[s];seen.add(s);ct=0
  while todo:
   u=todo.pop();ct+=1
   for v in remaining[u]:
    if v not in seen:seen.add(v);todo.append(v)
  profile.append(ct)
 return tuple(sorted(profile))

hist=collections.Counter();min_count=collections.Counter(); witness_classes={}
for M in pbits:
 available=[e for e in H if e not in M]
 assert len(available)==20
 best=None;number=0;sample=None
 for k in range(4,6):
  for F in itertools.combinations(available,k):
   deletions=frozenset(F)
   if sum(q.isdisjoint(deletions) for q in pbits)==1:
    if best is None:best=k
    number+=1; sample=sample or F
  if best is not None:break
 assert best in (4,5) and sample is not None
 tup=cycles(M)
 hist[tup,best]+=1
 min_count[tup,best,number]+=1
 witness_classes.setdefault(str((tup,best)),[list(x) for x in sample])
assert hist=={((20,),4):30,((5,5,10),5):6},hist
assert min_count=={((20,),4,8):30,((5,5,10),5,22):6},min_count
print(json.dumps({'graph':'LCF [10,7,4,-4,-7,10,-4,7,-7,4]^2',
 'vertices':20,'edges':len(H),'isomorphic_to_GP10_2':True,
 'perfect_matchings':len(pbits),'profile_anti_histogram':{str(k):v for k,v in sorted(hist.items())},
 'minimum_deletion_count_by_class':{str(k):v for k,v in sorted(min_count.items())},
 'sample_minimum_sets':witness_classes,'all_verified':True},sort_keys=True,indent=2))
