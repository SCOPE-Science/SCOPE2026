#!/usr/bin/env python3
"""Independent geometric construction and exchange-graph census for AG(2,3).

Uses no external libraries or external data. All incidence lines are generated
from the four directions in F_3^2. Every optimum is constructed from an omitted
point pair; each residual incidence graph is checked for its two matchings.
"""
from collections import Counter, deque
from itertools import combinations

points = tuple((x,y) for x in range(3) for y in range(3))
lines = tuple(frozenset((x,y) for y in range(3)) for x in range(3)) + tuple(
    frozenset((x,(m*x+b)%3) for x in range(3))
    for m in range(3) for b in range(3))
assert len(points)==9 and len(lines)==len(set(lines))==12
incidence={(i,j) for i,p in enumerate(points) for j,line in enumerate(lines) if p in line}
assert len(incidence)==36


def bijections(remaining_lines, available_points, chosen=()):
    if not remaining_lines:
        yield frozenset(chosen)
        return
    line = remaining_lines[0]
    for p in available_points:
        if points[p] in lines[line]:
            yield from bijections(remaining_lines[1:], tuple(x for x in available_points if x!=p), chosen+((p,line),))

optima=[]
for missing in combinations(range(9),2):
    covered_lines=tuple(j for j,ell in enumerate(lines) if any(points[p] in ell for p in missing))
    assert len(covered_lines)==7
    remaining_points=tuple(i for i in range(9) if i not in missing)
    candidates=list(bijections(covered_lines,remaining_points))
    assert len(candidates)==2
    for m in candidates:
        assert len(m)==7 and all(p not in missing for p,_ in m)
        covered_points={p for p,_ in m}
        covered_blocks={j for _,j in m}
        assert all(p in covered_points or j in covered_blocks for p,j in incidence)
        optima.append(m)
assert len(optima)==72 and len(set(optima))==72

# Distance in a fixed-size batch-exchange graph is defined using one move
# replacing up to d of the seven edges while remaining an optimum.
N=len(optima)
intersection=Counter()
for i,j in combinations(range(N),2):
    intersection[len(optima[i] & optima[j])] += 1
assert intersection == {0:612,1:900,2:756,3:288}, intersection
adj=[[] for _ in range(N)]
for i,j in combinations(range(N),2):
    if len(optima[i] & optima[j])==3:
        adj[i].append(j); adj[j].append(i)
assert all(len(v)==8 for v in adj)
assert sum(map(len,adj))//2==288
profiles=Counter()
for root in range(N):
    dist=[-1]*N;dist[root]=0
    queue=deque([root])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if dist[v]<0:
                dist[v]=dist[u]+1;queue.append(v)
    assert min(dist)==0 and max(dist)==4
    profiles[tuple(Counter(dist)[k] for k in range(5))]+=1
assert profiles=={(1,8,32,28,3):72},profiles
print('INCIDENCE_9_12_36')
print('PAIR_CLASSES_36_MATCHINGS_EACH_2_OPTIMA_72')
print('SHARED_EDGE_PAIRS',sorted(intersection.items()))
print('EXCHANGE_THRESHOLD_4_DEGREE_8_EDGES_288')
print('DISTANCE_PROFILE_1_8_32_28_3_FOR_ALL_72')
print('GEOMETRY_CERTIFICATE_OK')
