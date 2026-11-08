#!/usr/bin/env python3
"""Independent exhaustive finite proof for the antipodal edge classification."""
from itertools import combinations
from collections import Counter, deque

N=20
E=set()
def add(a,b): E.add(tuple(sorted((a,b))))
for i in range(10):
    add(i,(i+1)%10)
    add(i,10+i)
    add(10+i,10+(i+2)%10)
assert len(E)==30
adj=[0]*N
for a,b in E:
    adj[a] |= 1<<b
    adj[b] |= 1<<a
assert all(x.bit_count()==3 for x in adj)
two=[]
for v in range(N):
    neighbors=set(i for i in range(N) if adj[v]>>i&1)
    twos=set(w for u in neighbors for w in range(N) if adj[u]>>w&1)
    twos-=neighbors|{v}
    assert len(twos)==6
    two.append(sum(1<<w for w in twos))

def valid(mask):
    return all((adj[v]&mask) or ((two[v]&mask).bit_count()>=2) for v in range(N))

counts=[]
for k in range(1,5):
    good=[sum(1<<v for v in S) for S in combinations(range(N),k)
          if valid(sum(1<<v for v in S))]
    counts.append(len(good))
    if k==4: states=set(good)
assert counts==[0,0,0,15], counts
T=lambda v: (v+5)%10 if v<10 else 10+(v-10+5)%10
assert all(T(T(v))==v for v in range(N))
classes={frozenset({a,b,T(a),T(b)}) for a,b in E}
assert len(classes)==15
assert states=={sum(1<<v for v in S) for S in classes}
assert all(valid(sum(1<<v for v in S)) for S in classes)
# Each quotient vertex is an antipodal pair; the 15 quotient edges form GP(5,2).
quot_edges={tuple(sorted((a%5+5*(a>=10),b%5+5*(b>=10)))) for a,b in E}
assert len(quot_edges)==15
petersen=set()
for i in range(5):
    petersen.add(tuple(sorted((i,(i+1)%5))))
    petersen.add(tuple(sorted((i,i+5))))
    petersen.add(tuple(sorted((i+5,(i+2)%5+5))))
assert quot_edges==petersen
# Reconfiguration of antipodal edge lifts: single and two-token jumping.
ordered=sorted(states)
one=0;two_move=0
A=[set() for _ in ordered]
for i,j in combinations(range(len(ordered)),2):
    intersection=(ordered[i]&ordered[j]).bit_count()
    assert intersection in (0,2)
    if intersection==3: one+=1
    if intersection==2:
        two_move+=1;A[i].add(j);A[j].add(i)
assert one==0 and two_move==30
assert all(len(x)==4 for x in A)
# Exact isomorphism to L(Petersen) through the pair of quotient endpoints.
# Equivalent direct image without assuming a coordinate labeling for quotient indices.
images={}
for s in ordered:
    labels={v%5+5*(v>=10) for v in range(N) if s>>v&1}
    assert len(labels)==2
    e=tuple(sorted(labels));assert e in petersen
    images[s]=e
assert len(set(images.values()))==15
for i,j in combinations(range(15),2):
    assert (j in A[i]) == (len(set(images[ordered[i]]) & set(images[ordered[j]]))==1)
# The line graph diameter and radius from all roots.
ecc=[]
for i in range(15):
    dist={i:0};q=deque([i])
    while q:
        v=q.popleft()
        for w in A[v]:
            if w not in dist:dist[w]=dist[v]+1;q.append(w)
    assert len(dist)==15
    ecc.append(max(dist.values()))
assert set(ecc)=={3}
print('GP_OK vertices=20 edges=30 shell2=6 counts_1_to_4='+str(counts)
      +' optima=15 antipodal_edge_pairs=15 quotient=Petersen'
      +' one_token_edges=0 two_token_edges=30 degree=4 radius=3 diameter=3')
print('GP_OPTIMA='+str([tuple(v for v in range(N) if mask>>v&1) for mask in ordered]))
