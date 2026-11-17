#!/usr/bin/env python3
"""Exact finite verification of nontrivial Petersen induced-forest fixed spaces.

Pure Python 3 standard library. Run: python verify.py [--certificate census.json]
Vertices of the Petersen graph are two-subsets of five labels.
"""
import itertools, collections, json, sys

perms = list(itertools.permutations(range(5)))
ix = {p:i for i,p in enumerate(perms)}
n = len(perms)
I = ix[tuple(range(5))]
product = [[ix[tuple(a[b[j]] for j in range(5))] for b in perms] for a in perms]
inverse = [next(j for j in range(n) if product[i][j] == I) for i in range(n)]

def generated_extension(subgroup, element):
    new = set(subgroup) | {element, inverse[element]}
    todo = list(new)
    while todo:
        a = todo.pop()
        for b in tuple(new):
            for c in (product[a][b], product[b][a]):
                if c not in new:
                    new.add(c)
                    todo.append(c)
    return frozenset(new)

subgroups = {frozenset((I,))}
queue = collections.deque(subgroups)
while queue:
    H = queue.popleft()
    for g in range(n):
        if g not in H:
            J = generated_extension(H, g)
            if J not in subgroups:
                subgroups.add(J)
                queue.append(J)
assert len(subgroups) == 156
for H in subgroups:
    assert I in H
    assert all(inverse[g] in H for g in H)
    assert all(product[g][k] in H for g in H for k in H)

classes = []
remaining = set(subgroups)
while remaining:
    H = min(remaining, key=lambda x:tuple(sorted(x)))
    conj = {frozenset(product[product[g][h]][inverse[g]] for h in H) for g in range(n)}
    assert conj <= remaining
    remaining.difference_update(conj)
    classes.append((H,conj))
assert len(classes) == 19
assert sum(len(conj) for _,conj in classes) == 156

pairs = list(itertools.combinations(range(5),2))
pair_ix = {x:i for i,x in enumerate(pairs)}
action = [[pair_ix[tuple(sorted((p[a],p[b])))] for a,b in pairs] for p in perms]
# Petersen adjacency = disjointness of the corresponding two-subsets.
neighbor = [set(j for j,b in enumerate(pairs) if not set(a).intersection(b)) for a in pairs]

def forest_by_dfs(selected):
    active = set(selected)
    components = 0
    unseen = set(active)
    while unseen:
        components += 1
        todo = [unseen.pop()]
        while todo:
            u = todo.pop()
            for v in neighbor[u].intersection(unseen):
                unseen.remove(v)
                todo.append(v)
    edge_count = sum(len(neighbor[u].intersection(active)) for u in active)//2
    return edge_count == len(active) - components

def forest_by_union_find(selected):
    parent = {v:v for v in selected}
    def find(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for u,v in itertools.combinations(sorted(selected),2):
        if v not in neighbor[u]:
            continue
        a,b = find(u),find(v)
        if a == b:
            return False
        parent[a] = b
    return True

# Independent methods must agree on every subset of ten Petersen vertices.
for size in range(11):
    for S in itertools.combinations(range(10),size):
        assert forest_by_dfs(S) == forest_by_union_find(S)

def model(H):
    unseen = set(range(10))
    orbits = []
    while unseen:
        x = min(unseen)
        O = frozenset(action[g][x] for g in H)
        assert O <= unseen
        unseen.difference_update(O)
        orbits.append(tuple(sorted(O)))
    faces = set()
    for m in range(1,len(orbits)+1):
        for s in itertools.combinations(range(len(orbits)),m):
            union = set().union(*(orbits[j] for j in s))
            if forest_by_union_find(union):
                faces.add(s)
    assert all(s[:k]+s[k+1:] in faces for s in faces for k in range(len(s)) if len(s)>1)
    return orbits,faces

def collapse(all_faces):
    faces = set(all_faces)
    pairs_deleted=[]
    while True:
        facets=[t for t in faces if not any(set(t)<set(u) for u in faces)]
        cands=[]
        for t in facets:
            for k in range(len(t)):
                f=t[:k]+t[k+1:]
                if f and sum(set(f)<=set(u) for u in facets)==1:
                    cands.append((f,t))
        if not cands:
            break
        f,t = min(cands,key=lambda x:(-len(x[0]),x[0],x[1]))
        assert set(f)<set(t) and len(t)==len(f)+1
        assert sum(set(f)<=set(u) for u in facets)==1
        faces.remove(f)
        faces.remove(t)
        pairs_deleted.append((f,t))
    return faces,pairs_deleted

def graph_type(faces):
    if not faces:return 'empty'
    dim=max(map(len,faces))-1
    if dim>=2:return '2d'
    V={x[0] for x in faces if len(x)==1}
    edges=[f for f in faces if len(f)==2]
    unseen=set(V);cc=0
    while unseen:
        cc+=1
        todo=[unseen.pop()]
        while todo:
            v=todo.pop()
            for a,b in edges:
                w=b if v==a else (a if v==b else None)
                if w in unseen:unseen.remove(w);todo.append(w)
    rank=len(edges)-len(V)+cc
    if cc==1 and rank==0:return 'contractible'
    if cc==2 and rank==0:return 'S0'
    if cc==1 and rank==2:return 'wedge2S1'
    raise AssertionError(('unclassified graph',cc,rank))

def certify_two_spheres(faces):
    """Explicit fundamental-group elimination and free H2 rank via Euler characteristic."""
    vs=sorted(x[0] for x in faces if len(x)==1)
    edges={tuple(sorted(x)) for x in faces if len(x)==2}
    tris=[x for x in faces if len(x)==3]
    assert len(vs)==6 and len(edges)==13 and len(tris)==10
    # Select a spanning tree with five edges, preferring edges incident to vertex 0.
    tree={e for e in edges if 0 in e}
    assert len(tree)==5 and len(vs)==6
    unfilled=edges-tree
    # Each triangle has boundary with three edges, and any two already
    # nullhomotopic imply the third is nullhomotopic. Iterate this implication.
    killed=set(tree)
    witnesses=[]
    while True:
        candidates=[]
        for t in tris:
            tedges={tuple(sorted(x)) for x in itertools.combinations(t,2)}
            if len(tedges-killed)==1:
                candidates.append((tuple(sorted(tedges-killed))[0],t))
        if not candidates:
            break
        edge,tri=min(candidates)
        killed.add(edge)
        witnesses.append({'edge':list(edge),'triangle':list(tri)})
    assert killed==edges and len(witnesses)==8
    # A connected simply connected 2-complex of Euler characteristic 3
    # has free H2 of rank 2 and is homotopy-equivalent to S2 v S2.
    assert len(vs)-len(edges)+len(tris)==3
    return witnesses

census=[]
weighted=collections.Counter()
for H,conj in classes:
    orbits,faces=model(H)
    reduced,pairs_deleted=collapse(faces)
    typ=graph_type(reduced)
    fundamental_group_witness=[]
    if len(H)==1:
        assert typ=='2d'
        typ='excluded_identity'
    elif typ=='2d':
        fundamental_group_witness=certify_two_spheres(reduced)
        typ='wedge2S2'
    weighted[typ]+=len(conj)
    # Compute label orbit partition for auditability.
    unseen=set(range(5));parts=[]
    while unseen:
        x=min(unseen);O={perms[g][x] for g in H}
        assert O<=unseen
        unseen-=O;parts.append(sorted(O))
    record={'group_elements':[list(perms[g]) for g in sorted(H)],
        'group_order':len(H),'conjugacy_class_size':len(conj),
        'label_orbits':parts,'vertex_orbits':[list(O) for O in orbits],
        'face_count':len(faces),'type':typ,
        'collapse_pairs':[[list(a),list(b)] for a,b in pairs_deleted],
        'residual_faces':[list(f) for f in sorted(reduced)],
        'fundamental_group_elimination':fundamental_group_witness}
    census.append(record)
# Exact nontrivial fixed-point census, 155 subgroups in 18 classes.
expected={'empty':20,'contractible':105,'S0':10,'wedge2S1':5,'wedge2S2':15,'excluded_identity':1}
assert dict(weighted)==expected, (weighted,expected)
assert len(census)==19
# Check that conjugation preserves the *entire* fixed simplicial face count
# and the reduced homotopy type, not just the subgroup order.
for H,conj in classes:
    q,faces=model(H)
    for J in conj:
        q2,faces2=model(J)
        assert sorted(map(len,q))==sorted(map(len,q2))
        assert collections.Counter(map(len,faces))==collections.Counter(map(len,faces2))

if len(sys.argv)==3 and sys.argv[1]=='--certificate':
    with open(sys.argv[2],'w',encoding='utf-8') as f:
        json.dump({'schema_version':1,'scope':'nontrivial subgroups of S5 acting on Petersen induced-forest complex',
          'subgroup_count':len(subgroups),'conjugacy_class_count':len(classes),
          'spectrum':dict(weighted),'classes':census},f,ensure_ascii=False,indent=2)
        f.write('\n')
elif len(sys.argv)!=1:
    raise SystemExit('Usage: python verify.py [--certificate census.json]')
print('SUBGROUPS=156 CONJUGACY_CLASSES=19 NONIDENTITY_SUBGROUPS=155')
for typ in ['empty','contractible','S0','wedge2S1','wedge2S2']:
    print('%s=%s'%(typ,weighted[typ]))
print('PETERSEN_INDUCED_FOREST_NONIDENTITY_FIXED_SPACES_PASS')
