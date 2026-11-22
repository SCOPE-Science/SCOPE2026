#!/usr/bin/env python3
"""Independent direct-trace verification for the complementary prism of a 9-cycle."""
from itertools import combinations
from collections import Counter

n=9
V=2*n
adj=[set() for _ in range(V)]
def edge(a,b):
    adj[a].add(b)
    adj[b].add(a)
for i in range(n):
    edge(i,(i+1)%n)
    edge(i,i+n)
for i in range(n):
    for j in range(i+1,n):
        if j not in ((i+1)%n,(i-1)%n):
            edge(i+n,j+n)
closed=[{i}|adj[i] for i in range(V)]

# Unlike the hitting-set checker, this code constructs every entire signature
# from its chosen landmark coordinates and tests signature uniqueness.
optimal=[]
count_tests=0
for k in range(8):
    valid=[]
    for landmarks in combinations(range(V),k):
        count_tests+=1
        traces=[tuple(j for j in landmarks if j in closed[i]) for i in range(V)]
        if any(not t for t in traces) or len(set(traces))!=V:
            continue
        valid.append(sum(1<<j for j in landmarks))
    if k<7: assert not valid
    else: optimal=valid
assert count_tests==63004 and len(optimal)==90
O={v:i for i,v in enumerate(optimal)}
E={i:set() for i in range(90)}
for i in range(90):
    for j in range(i+1,90):
        if (optimal[i]^optimal[j]).bit_count()==2:
            E[i].add(j); E[j].add(i)
assert sum(map(len,E.values()))==162
components=[]; remaining=set(E)
while remaining:
    stack=[remaining.pop()]; c=[]
    while stack:
        u=stack.pop();c.append(u)
        for w in E[u]&remaining:
            remaining.remove(w);stack.append(w)
    components.append(c)
shape=Counter((len(c),sum(len(E[x]) for x in c)//2,
               tuple(sorted(len(E[x]) for x in c))) for c in components)
assert shape==Counter({(5,6,(2,2,2,2,4)):9,
                      (3,2,(1,1,2)):9,
                      (2,1,(1,1)):9})

# Dihedral symmetries preserve each of the two layers, cycle adjacency,
# and all minimum-code exchange edges.
def transform(mask,r,reflect):
    z=0
    for side in (0,1):
        for i in range(n):
            if mask>>(side*n+i)&1:
                j=(r-i if reflect else r+i)%n
                z|=1<<(side*n+j)
    return z
unseen=set(optimal); orbits=[]
while unseen:
    seed=min(unseen)
    orb={transform(seed,r,f) for r in range(n) for f in (0,1)}
    assert orb<=O.keys()
    orbits.append((seed,len(orb)))
    unseen-=orb
assert Counter(w for _,w in orbits)==Counter({18:4,9:2})
assert [s for s,w in orbits]==[3697,5858,7904,19045,19121,23201]
for i in E:
    for r in range(n):
        for f in (0,1):
            new_i=O[transform(optimal[i],r,f)]
            assert {transform(optimal[j],r,f) for j in E[i]}=={optimal[j] for j in E[new_i]}
print('PASS 63004 sets of size at most seven, 90 minima, 81 exchanges, '
      '9 bowties, 9 three-vertex paths, 9 edges, 6 dihedral orbits')
for seed,count in orbits:
    print(count, ''.join(str((seed>>i)&1) for i in range(9)),
          ''.join(str((seed>>(9+i))&1) for i in range(9)))
