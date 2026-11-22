#!/usr/bin/env python3
"""Independent all-pairs certificate via pair-separation masks and Floyd-Warshall."""
from itertools import combinations
from collections import Counter
import json

EDGES=((0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),
       (2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),
       (5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11))
N=12; INF=10**5; V=(1<<N)-1
adjbits=[0]*N
for a,b in EDGES:adjbits[a]|=1<<b;adjbits[b]|=1<<a
assert all(z.bit_count()==4 for z in adjbits)

# Floyd-Warshall on the original labelled twelve-vertex graph.
D=[[0 if u==v else 1 if (adjbits[u]>>v)&1 else INF for v in range(N)] for u in range(N)]
for k in range(N):
 for i in range(N):
  dik=D[i][k]
  for j in range(N):
   D[i][j]=min(D[i][j],dik+D[k][j])
assert all(max(row)==2 for row in D)

# For each pair of distinct targets, a bitmask of possible distinguishing landmarks.
separators=[sum(1<<w for w in range(N) if D[u][w]!=D[v][w])
            for u in range(N) for v in range(u+1,N)]

def acceptable(m):return all(m&s for s in separators)
for k in range(4):
 for S in combinations(range(N),k):
  assert not acceptable(sum(1<<x for x in S))
B=[sum(1<<x for x in S) for S in combinations(range(N),4)
   if acceptable(sum(1<<x for x in S))]
assert len(B)==146


def measure(slide):
 m=len(B);mat=[[0 if i==j else INF for j in range(m)] for i in range(m)]
 edges=0
 for i in range(m):
  for j in range(i+1,m):
   x=B[i]^B[j]
   if x.bit_count()!=2:continue
   if slide:
    a=(x & B[i]).bit_length()-1
    b=(x & B[j]).bit_length()-1
    if not ((adjbits[a]>>b)&1):continue
   mat[i][j]=mat[j][i]=1;edges+=1
 # Floyd-Warshall on all configurations, deliberately unlike the BFS verifier.
 for k in range(m):
  rowk=mat[k]
  for i in range(m):
   ik=mat[i][k]
   if ik==INF:continue
   rowi=mat[i]
   for j in range(m):
    possible=ik+rowk[j]
    if possible<rowi[j]:rowi[j]=possible
 assert max(max(row) for row in mat)<INF
 ecc=Counter(max(row) for row in mat)
 dist=Counter();extra=Counter()
 for i in range(m):
  for j in range(i+1,m):
   z=mat[i][j]
   dist[z]+=1
   minimum=(B[i]^B[j]).bit_count()//2
   extra[z-minimum]+=1
 centers=[tuple(v for v in range(N) if B[i]>>v&1) for i in range(m)
           if max(mat[i])==min(ecc)]
 return {'edges':edges,'eccentricities':dict(sorted(ecc.items())),
         'distances':dict(sorted(dist.items())), 'detours':dict(sorted(extra.items())),
         'centers':centers if slide else 'all 146 states', 'radius':min(ecc),'diameter':max(ecc)}

TJ=measure(False);TS=measure(True)
assert TJ['edges']==928 and TJ['eccentricities']=={4:146}
assert TJ['detours']=={0:10367,1:218}
assert TS['edges']==452 and TS['eccentricities']=={4:2,5:104,6:40}
assert TS['centers']==[(2,8,9,11),(3,6,7,10)]
assert TS['distances']=={1:452,2:1700,3:3444,4:3577,5:1344,6:68}
assert TS['detours']=={0:4463,1:4944,2:1070,3:92,4:16}
print(json.dumps({'basis_size':4,'basis_count':len(B),'TJ':TJ,'TS':TS},sort_keys=True))
