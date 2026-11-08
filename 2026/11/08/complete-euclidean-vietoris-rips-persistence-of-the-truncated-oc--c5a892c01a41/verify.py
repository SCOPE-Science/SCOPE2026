#!/usr/bin/env python3
"""Reproducible exact combinatorial checks for Euclidean Rips complexes.
No downloaded packages or external data are needed; Python 3 standard library only.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, product

V = sorted(set(tuple(s[i]*p[i] for i in range(3))
    for p in permutations((0,1,2)) for s in product((-1,1),repeat=3)))
assert len(V) == 24
D2 = {(i,j):sum((V[i][k]-V[j][k])**2 for k in range(3))
      for i,j in combinations(range(24),2)}
shells = Counter(D2.values())
assert dict(sorted(shells.items())) == {2:36,4:12,6:48,8:24,10:24,
                                       12:24,14:48,16:12,18:36,20:12}

# Intrinsic edge metric, tested rather than identified with chord lengths.
neighbors = [[] for _ in V]
for (i,j),d in D2.items():
    if d==2: neighbors[i].append(j);neighbors[j].append(i)
assert all(len(n)==3 for n in neighbors)
dist = {}
for i in range(24):
    ds = {i:0};q=deque([i])
    while q:
        a=q.popleft()
        for b in neighbors[a]:
            if b not in ds:ds[b]=ds[a]+1;q.append(b)
    assert len(ds)==24
    for j in range(i+1,24):dist[i,j]=ds[j]
metric_shells=defaultdict(Counter)
for edge,d in D2.items():metric_shells[dist[edge]][d]+=1
assert {k:dict(v) for k,v in metric_shells.items()} == {
 1:{2:36},2:{4:12,6:48},3:{8:24,10:24,12:24},
 4:{14:48,16:12},5:{18:36},6:{20:12}}

def faces_at(threshold):
    adj=[0]*24
    for (i,j),d in D2.items():
        if d<=threshold:adj[i]|=1<<j;adj[j]|=1<<i
    faces_by_dimension=defaultdict(list)
    def extend(face,options):
        if face:faces_by_dimension[face.bit_count()-1].append(face)
        while options:
            bit=options&-options;options-=bit
            extend(face|bit,options&adj[bit.bit_length()-1])
    extend(0,(1<<24)-1)
    return dict(faces_by_dimension)

F={t:faces_at(t) for t in (2,4,6,8,10,12,14,16)}
expected={
 2:[24,36],4:[24,48,24,6],6:[24,96,112,30],
 8:[24,120,208,150,48,8],
 10:[24,144,328,342,168,32],
 12:[24,168,472,618,384,92],
 14:[24,216,944,2250,3216,2860,1560,480,64],
 16:[24,228,1112,3042,4848,4592,2592,822,112]}
for t,vec in expected.items():
    assert [len(F[t][d]) for d in sorted(F[t])] == vec,(t,F[t])

# Boundary triangles of the fourteen geometric faces (6 squares, 8 hexagons).
planes=[]
for axis in range(3):
    for sg in (-1,1):
        planes.append(tuple(i for i,v in enumerate(V) if v[axis]==2*sg))
for signs in product((-1,1),repeat=3):
    planes.append(tuple(i for i,v in enumerate(V)
              if sum(signs[k]*v[k] for k in range(3))==3))
assert Counter(map(len,planes))==Counter({4:6,6:8})
surface=set();all_triangles=[];square_edge_cycles=[]
for face in planes:
    links={i:[j for j in face if j!=i and D2[min(i,j),max(i,j)]==2]
           for i in face}
    assert all(len(x)==2 for x in links.values())
    start=min(face);cycle=[start,min(links[start])]
    while True:
        options=[k for k in links[cycle[-1]] if k!=cycle[-2]]
        assert len(options)==1
        nxt=options[0]
        if nxt==start:break
        assert nxt not in cycle
        cycle.append(nxt)
    assert len(cycle)==len(face)
    if len(face)==4:
        square_edge_cycles.append(tuple(cycle))
        triangles=[(cycle[0],cycle[k],cycle[k+1])
                   for k in (1,2)]
    else:
        triangles=[(cycle[0],cycle[1],cycle[2]),
                   (cycle[2],cycle[3],cycle[4]),
                   (cycle[4],cycle[5],cycle[0]),
                   (cycle[0],cycle[2],cycle[4])]
    for tri in triangles:
        all_triangles.append(tri)
        for size in range(1,4):
            for sub in combinations(tri,size):
                surface.add(sum(1<<i for i in sub))
assert len(all_triangles)==44
assert Counter(s.bit_count() for s in surface)==Counter({1:24,2:66,3:44})
# Each edge belongs to two distinct surface triangles; polygonal boundary sphere.
edge_mult=Counter()
for tri in all_triangles:
    for a,b in combinations(tri,2):edge_mult[sum(1<<i for i in (a,b))]+=1
assert len(edge_mult)==66 and set(edge_mult.values())=={2}
assert surface <= {s for seq in F[6].values() for s in seq}

# A graph retract: delete one boundary edge in each square from the original graph.
target_graph={1<<v for v in range(24)}
for (i,j),d in D2.items():
    if d==2:target_graph.add((1<<i)|(1<<j))
for face in square_edge_cycles:
    mask=sum(1<<i for i in face)
    edges=sorted(s for s in target_graph if s.bit_count()==2 and (s&mask)==s)
    assert len(edges)==4
    target_graph.remove(edges[-1])
assert Counter(s.bit_count() for s in target_graph)==Counter({1:24,2:30})
# Connectedness of the retained graph, not inferred from Euler characteristic.
visited={0};stack=[0]
while stack:
    v=stack.pop()
    for edge in target_graph:
        if edge.bit_count()!=2 or not ((edge>>v)&1):continue
        w=(edge ^ (1<<v)).bit_length()-1
        if w not in visited:visited.add(w);stack.append(w)
assert len(visited)==24

# Fully checked elementary collapse from K to specified target subcomplex.
def collapse(phase,target):
    faces={s for items in F[phase].values() for s in items}
    assert target <= faces
    cofaces=defaultdict(set)
    for cell in faces:
        leftover=cell
        while leftover:
            bit=leftover&-leftover;leftover-=bit
            lower=cell^bit
            if lower:cofaces[lower].add(cell)
    queue=deque(sorted((s for s in faces if s not in target and
                         len(cofaces[s])==1),key=lambda x:(x.bit_count(),x)))
    pairs=[]
    while queue:
        lo=queue.popleft()
        if lo not in faces or lo in target or len(cofaces[lo])!=1:continue
        up=next(iter(cofaces[lo]))
        if up not in faces or up in target:continue
        assert up.bit_count()==lo.bit_count()+1 and not cofaces[up]
        pairs.append((lo,up))
        for cell in (lo,up):
            faces.remove(cell)
            leftover=cell
            while leftover:
                bit=leftover&-leftover;leftover-=bit
                down=cell^bit
                if down:
                    cofaces[down].discard(cell)
                    if down not in target and len(cofaces[down])==1:
                        queue.append(down)
    assert faces==target,(phase,len(faces),len(target),len(faces-target))
    return pairs

counts={4:24,8:212,10:452,12:812,14:5740}
collapses={}
for t,n in counts.items():
    pairs=collapse(t,target_graph if t==4 else surface)
    assert len(pairs)==n,(t,len(pairs))
    collapses[t]=pairs

# Replay the packaged explicit collapse certificate, not just the counts.
from pathlib import Path
import json
certificate_path=Path(__file__).with_name('collapse_pairs.json')
assert certificate_path.is_file(), 'The packaged collapse certificate is required.'
certificate=json.loads(certificate_path.read_text(encoding='utf-8'))
assert certificate['schema_version']==1
for t,computed in collapses.items():
    stored=certificate['squared_thresholds'][str(t)]
    assert stored==[[lo,up] for lo,up in computed],(t,'certificate mismatch')

# Separate exact mod-two boundary-rank checks (corroboration, not an integral proof).
def betti_mod2(phase):
    faces=F[phase]
    ranks={}
    for d in range(1,max(faces)+1):
        index={s:i for i,s in enumerate(faces[d-1])}
        piv={}
        for cell in faces[d]:
            z=0;bits=cell
            while bits:
                b=bits&-bits;bits-=b
                z^=1<<index[cell^b]
            while z:
                k=z.bit_length()-1
                if k in piv:z^=piv[k]
                else:piv[k]=z;break
        ranks[d]=len(piv)
    return {d:len(v)-ranks.get(d,0)-ranks.get(d+1,0)
            for d,v in faces.items()}
expected_betti={2:{0:1,1:13},4:{0:1,1:7},6:{0:1,2:9},
                 8:{0:1,2:1},10:{0:1,2:1},12:{0:1,2:1},
                 14:{0:1,2:1},16:{0:1,4:5,5:2}}
for phase in F:
    positive={d:b for d,b in betti_mod2(phase).items() if b}
    assert positive==expected_betti[phase],(phase,positive)

# At squared distance 18, complement graph consists of twelve disjoint pairs.
missing18=[edge for edge,d in D2.items() if d>18]
assert len(missing18)==12
assert all(V[j]==tuple(-x for x in V[i]) for i,j in missing18)
assert len(set(sum(([i,j] for i,j in missing18),[])))==24
assert max(D2.values())==20

print('SQUARED_SHELLS',dict(sorted(shells.items())))
print('GRAPH_CHORD_SHELL_MAP',dict(sorted((k,dict(sorted(v.items())))
                                       for k,v in metric_shells.items())))
print('FACE_VECTORS',expected)
print('SURFACE_F_VECTOR',[24,66,44], 'SURFACE_IN_SCALE6',True)
print('COLLAPSES',counts,'TARGET_GRAPH_V_E',[24,30])
print('BETTI_MOD2_NONZERO',expected_betti)
print('FINAL_MISSING_ANTIPODAL_PAIRS',len(missing18))
print('VERIFY_OK')
