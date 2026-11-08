#!/usr/bin/env python3
"""Independent Pappus Levi-incidence exhaustive certificate; no third-party modules."""
import json
from collections import Counter, deque
from itertools import combinations

N = 18
edges = set()
# Affine plane over F_3 with one entire parallel class deleted:
# points (x,y) with index 3*x+y; nine lines x=c, y=c, x+y=c.
for x in range(3):
    for y in range(3):
        point = 3*x + y
        for direction, intercept in enumerate((x, y, (x + y) % 3)):
            line = 9 + 3*direction + intercept
            edges.add((point, line))
assert len(edges) == 27
neighbors = [set() for _ in range(N)]
for a,b in edges:
    neighbors[a].add(b)
    neighbors[b].add(a)
assert all(len(x) == 3 for x in neighbors)
closed = [set([v]) | neighbors[v] for v in range(N)]
# Separating-witness dual: every vertex must be hit, and each symmetric difference
# of two closed neighborhoods must be hit. This is not the signature-based test.
witness_constraints = [sum(1 << i for i in c) for c in closed]
for a in range(N):
    for b in range(a+1, N):
        witness_constraints.append(sum(1 << v for v in (closed[a] ^ closed[b])))
assert len(witness_constraints) == 171

def admissible(mask):
    return all(mask & witness for witness in witness_constraints)

best = None
codes = set()
number_examined = 0
for k in range(N+1):
    batch = []
    for c in combinations(range(N),k):
        number_examined += 1
        mask = sum(1 << j for j in c)
        if admissible(mask):
            batch.append(mask)
    if batch:
        best = k
        codes = set(batch)
        break
assert best == 9 and len(codes) == 1028

slide = {s:set() for s in codes}
jump = {s:set() for s in codes}
for s in codes:
    selected = [j for j in range(N) if s & (1<<j)]
    for u in selected:
        for v in range(N):
            if s & (1<<v): continue
            t = s - (1<<u) + (1<<v)
            if t not in codes: continue
            jump[s].add(t)
            if v in neighbors[u]: slide[s].add(t)

def record(links):
    unvisited = set(codes)
    components=[]
    degrees = Counter(len(links[s]) for s in codes)
    while unvisited:
        seed = min(unvisited)
        cc={seed}
        frontier=[seed]
        for u in frontier:
            for v in links[u]:
                if v not in cc:
                    cc.add(v);frontier.append(v)
        unvisited -= cc
        edges_number=sum(len(links[u]) for u in cc)//2
        if len(cc)>1:
            ecc=[]
            for root in cc:
                D={root:0}
                Q=deque([root])
                while Q:
                    v=Q.popleft()
                    for w in links[v]:
                        if w not in D:
                            D[w]=D[v]+1;Q.append(w)
                assert len(D)==len(cc)
                ecc.append(max(D.values()))
            components.append({'size':len(cc),'edges':edges_number,'radius':min(ecc),
                               'diameter':max(ecc),'eccentricities':dict(sorted(Counter(ecc).items()))})
        else:
            components.append({'size':1,'edges':0})
    comps=Counter(x['size'] for x in components)
    return {'edges':sum(map(len,links.values()))//2,
            'components':dict(sorted(comps.items())),
            'degrees':dict(sorted(degrees.items())),
            'nontrivial':sorted([x for x in components if x['size']>1],key=lambda x:x['size'])}

# A concrete graph isomorphism from affine labels to the LCF labels.
map_to_lcf = (0,2,8,12,10,6,16,4,14,1,11,15,17,3,7,5,13,9)
offsets = (5,7,-7,7,-7,-5)*3
lcf_edges = set()
for i, delta in enumerate(offsets):
    for j in ((i+1)%N,(i+delta)%N):
        lcf_edges.add(tuple(sorted((i,j))))
assert {tuple(sorted((map_to_lcf[u], map_to_lcf[v]))) for u,v in edges} == lcf_edges

# Points/lines are the bipartition sides here (not the even/odd LCF indices).
by_points = Counter(sum(bool(m & (1<<j)) for j in range(9)) for m in codes)
result = {'graph':'AG(2,3) incidence with x-y parallel class omitted',
          'independent_graph_isomorphism_to_lcf':True,
          'subsets_tested_through_optimal_cardinality':number_examined,
          'optimal_cardinality':best,'optimal_codes':len(codes),
          'codes_by_point_count':dict(sorted(by_points.items())),
          'slide':record(slide), 'jump':record(jump)}
assert by_points == Counter({0:1,1:27,2:81,3:243,4:162,5:162,6:243,7:81,8:27,9:1})
assert result['slide']['edges']==1404 and result['slide']['components']=={1:108,460:2}
assert result['jump']['edges']==3780 and result['jump']['components']=={514:2}
assert all(x['radius']==4 and x['diameter']==8 for x in result['slide']['nontrivial'])
assert all(x['radius']==4 and x['diameter']==8 for x in result['jump']['nontrivial'])
print(json.dumps(result,sort_keys=True,indent=2))
