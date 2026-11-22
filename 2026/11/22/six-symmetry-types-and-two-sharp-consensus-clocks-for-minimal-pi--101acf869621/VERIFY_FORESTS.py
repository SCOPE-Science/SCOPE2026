"""Exact forest and graph-symmetry certificate for optimal Franklin forcing sets.
Usage: python3 VERIFY_FORESTS.py [min_forcing_sets.csv]
Pure Python standard library; no external dependencies.
"""
from itertools import combinations
from collections import Counter
import csv
import sys

N=12
E=set()
for i in range(N):
    for j in ((i+1)%N,(i+(5 if i%2==0 else -5))%N):
        E.add(tuple(sorted((i,j))))
assert len(E)==18
adj=[set() for _ in range(N)]
for i,j in E: adj[i].add(j);adj[j].add(i)
assert all(len(s)==3 for s in adj)

def induced_forest(P):
    """Return whether an induced vertex set P is a forest, by DFS cycle test."""
    vertices=set(P)
    visited=set()
    for root in vertices:
        if root in visited: continue
        stack=[(root,-1)]
        while stack:
            u,parent=stack.pop()
            if u in visited: return False
            visited.add(u)
            stack.extend((v,u) for v in adj[u] if v in vertices and v!=parent)
    return True

def leaf_stripping_time(P):
    left=set(P)
    t=0
    while left:
        leaves={u for u in left if len(adj[u]&left)<=1}
        if not leaves: return None
        left-=leaves
        t+=1
    return t

# Backtracking graph-isomorphisms: images of adjacent vertices remain adjacent,
# and images of nonadjacent vertices remain nonadjacent.
def all_automorphisms():
    mappings=[]
    def rec(mapping,unused):
        if len(mapping)==N:
            mappings.append(tuple(mapping[i] for i in range(N)))
            return
        u=max((v for v in range(N) if v not in mapping),
              key=lambda v:(len(adj[v]&mapping.keys()),-v))
        for w in sorted(unused):
            if all(((v in adj[u])==(mapping[v] in adj[w])) for v in mapping):
                mapping[u]=w
                rec(mapping,unused-{w})
                del mapping[u]
    rec({},set(range(N)))
    return mappings

autos=all_automorphisms()
assert len(autos)==48

def orbit_of(seed):
    return {frozenset(a[v] for v in seed) for a in autos}

allfour=list(combinations(range(N),4))
valid={frozenset(s) for s in allfour if induced_forest(set(range(N))-set(s))}
assert len(valid)==144
assert not any(induced_forest(set(range(N))-set(s)) for s in combinations(range(N),3))
assert sum(induced_forest(set(range(N))-set(s)) for s in allfour)==144
edge_counts=Counter(sum(1 for u,v in E if u in s and v in s) for s in valid)
assert edge_counts==Counter({0:36,1:108})
times={s:leaf_stripping_time(set(range(N))-s) for s in valid}
assert Counter(times.values())==Counter({3:72,4:72})

classes=[]
unseen=set(valid)
while unseen:
    s=min(unseen,key=lambda t:tuple(sorted(t)))
    orbit=orbit_of(s)
    assert orbit<=valid
    assert len({times[v] for v in orbit})==1
    unseen-=orbit
    classes.append((tuple(sorted(s)),len(orbit),times[s],sum(1 for u,v in E if u in s and v in s)))
classes.sort(key=lambda x:(x[2],x[3],x[0]))
assert Counter(size for _,size,_,_ in classes)==Counter({12:2,24:3,48:1})
assert len(classes)==6
assert sum(size for _,size,_,_ in classes)==144
assert Counter((tm,edges) for _,size,tm,edges in classes for _ in range(size)) == Counter({(3,0):36,(3,1):36,(4,1):72})

if len(sys.argv)>1:
    with open(sys.argv[1],'w',newline='',encoding='utf-8') as out:
        writer=csv.writer(out)
        writer.writerow(['pinned_vertices_zero_based','forcing_steps','seed_internal_edges'])
        for s in sorted(valid,key=lambda x:tuple(sorted(x))):
            writer.writerow([' '.join(map(str,sorted(s))),times[s],sum(1 for u,v in E if u in s and v in s)])
print('ALL FOREST AND SYMMETRY CHECKS PASSED')
print('graph vertices',N,'edges',len(E),'automorphisms',len(autos))
print('minimum forcing size',4,'optimal placements',len(valid))
print('forcing time population',sorted(Counter(times.values()).items()))
print('seed edge counts', sorted(edge_counts.items()))
print('symmetry orbits, representative/size/rounds/seed-edges', classes)
