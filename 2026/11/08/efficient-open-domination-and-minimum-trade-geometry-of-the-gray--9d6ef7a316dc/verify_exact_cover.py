#!/usr/bin/env python3
"""Independent exact-cover verification of efficient open domination in the Gray incidence graph.

No external packages are required. Run: python3 verify_exact_cover.py
"""
from collections import Counter, deque
from itertools import permutations, product

points = list(product(range(3), repeat=3))
pindex = {p: i for i,p in enumerate(points)}
line_points=[]
for axis in range(3):
    for other in product(range(3),repeat=2):
        cell=[]
        for t in range(3):
            p=list(other); p.insert(axis,t)
            cell.append(pindex[tuple(p)])
        line_points.append(tuple(cell))
assert len(line_points)==27 and len(set(line_points))==27
line_through=[[] for _ in range(27)]
for li,line in enumerate(line_points):
    for pi in line:line_through[pi].append(li)
assert all(len(x)==3 for x in line_through)

def exact_covers(universe, subsets):
    # Exhaustively partition universe by allowed subsets, selecting a smallest viable pivot.
    all_subsets=[frozenset(s) for s in subsets]
    through={x:[i for i,s in enumerate(all_subsets) if x in s] for x in universe}
    results=[]
    def dfs(remaining,picked):
        if not remaining:
            results.append(frozenset(picked)); return
        pivot=min(remaining,key=lambda x:sum(all_subsets[i]<=remaining for i in through[x]))
        for i in through[pivot]:
            s=all_subsets[i]
            if s<=remaining:dfs(remaining-s,picked+(i,))
    dfs(frozenset(universe),())
    return set(results)

# A point belongs to three axis lines; choose nine points to cover each line exactly once.
selected_points=exact_covers(range(27),line_through)
# A line contains three grid points; choose nine lines to cover each point exactly once.
selected_lines=exact_covers(range(27),line_points)
assert len(selected_points)==12, len(selected_points)
assert len(selected_lines)==21, len(selected_lines)

# Directly verify all 252 open-neighborhood partitions on the 54-vertex incidence graph.
for ps in selected_points:
    for ls in selected_lines:
        for i in range(27):
            assert sum(j in ls for j in line_through[i])==1
        for j in range(27):
            assert sum(i in ps for i in line_points[j])==1

pstates=sorted(selected_points,key=lambda s:tuple(sorted(s)))
lstates=sorted(selected_lines,key=lambda s:tuple(sorted(s)))
pedges={(i,j) for i in range(12) for j in range(i+1,12)
        if len(pstates[i]-pstates[j])==6}
ledges={(i,j) for i in range(21) for j in range(i+1,21)
        if len(lstates[i]-lstates[j])==3}
assert len(pedges)==54 and len(ledges)==36
pdeg=Counter(i for e in pedges for i in e)
ldeg=Counter(i for e in ledges for i in e)
assert Counter(pdeg.values())=={9:12}
assert Counter(ldeg.values())=={3:18,6:3}

states=list(product(range(12),range(21)))
lookup={st:i for i,st in enumerate(states)}
adj=[set() for _ in states]
for p in range(12):
    for i,j in ledges:
        u,v=lookup[p,i],lookup[p,j];adj[u].add(v);adj[v].add(u)
for l in range(21):
    for i,j in pedges:
        u,v=lookup[i,l],lookup[j,l];adj[u].add(v);adj[v].add(u)
assert sum(map(len,adj))//2==1566
assert Counter(map(len,adj))=={12:216,15:36}

pairs=Counter(); eccentricities=[]
for start in range(252):
    distances={start:0};queue=deque([start])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if v not in distances:
                distances[v]=distances[u]+1;queue.append(v)
    assert len(distances)==252
    eccentricities.append(max(distances.values()))
    for j in range(start+1,252):pairs[distances[j]]+=1
assert pairs=={1:1566,2:4896,3:8460,4:9180,5:6444,6:1080},pairs
assert set(eccentricities)=={6}

# The natural coordinate symmetry group acts on the two code factors.
coordinate_perms=list(permutations(range(3)))
p_to_id={x:i for i,x in enumerate(pstates)}
l_to_id={x:i for i,x in enumerate(lstates)}
line_lookup={frozenset(line):i for i,line in enumerate(line_points)}
remaining=set(states)
orbit_sizes=[]
for axis_permutation in coordinate_perms:
    for symbol_perms in product(coordinate_perms,repeat=3):
        mapped_points=[pindex[tuple(symbol_perms[k][p[axis_permutation[k]]] for k in range(3))] for p in points]
        mapped_lines=[line_lookup[frozenset(mapped_points[p] for p in line)] for line in line_points]
        pmap=[p_to_id[frozenset(mapped_points[i] for i in ps)] for ps in pstates]
        lmap=[l_to_id[frozenset(mapped_lines[i] for i in ls)] for ls in lstates]
        # Save images of every state for simultaneous group orbit enumeration.
        orbit_sizes.append((pmap,lmap))
assert len(orbit_sizes)==1296
sizes=[]
while remaining:
    seed=min(remaining)
    orbit={(pm[seed[0]],lm[seed[1]]) for pm,lm in orbit_sizes}
    sizes.append(len(orbit));remaining-=orbit
assert sorted(sizes)==[36,216],sizes
print('EXACT_COVER_GRAY_12_POINT_CODES_21_LINE_CODES_252_TOTAL_CODES_PASS')
print('TRADE_54_36_FACTOR_EDGES_PRODUCT_1566_EDGES_PASS')
print('DEGREE_216_AT_12_36_AT_15_CONNECTED_RADIUS6_DIAMETER6_PASS')
print('DISTANCE_PAIR_HISTOGRAM_1566_4896_8460_9180_6444_1080_PASS')
print('COORDINATE_AUTOMORPHISM_ORBITS_36_216_PASS')
