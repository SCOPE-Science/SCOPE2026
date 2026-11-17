#!/usr/bin/env python3
"""Reproducible simplicial-collapse and fundamental-group certificate.

Graph vertices are grid coordinates (row, column), with C3 adjacency
between any two distinct cyclic coordinates. A face is a set of graph edges
with pairwise disjoint endpoints.
"""
import collections
import itertools
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent

def graph(kind):
    points = list(itertools.product(range(3), repeat=2))
    E = []
    for a, u in enumerate(points):
        for b in range(a + 1, len(points)):
            v = points[b]
            same_row = u[0] == v[0]
            same_col = u[1] == v[1]
            horizontal = same_row and (kind != 'rectangle' or abs(u[1]-v[1]) == 1)
            vertical = same_col and (kind == 'torus' or abs(u[0]-v[0]) == 1)
            if horizontal or vertical:
                E.append((a,b))
    return E

def enumerate_faces(E):
    F = {()}
    def rec(start,chosen,occupied):
        for i in range(start,len(E)):
            a,b=E[i]
            if not (occupied & ((1<<a)|(1<<b))):
                child=chosen+(i,)
                assert child not in F
                F.add(child)
                rec(i+1,child,occupied|(1<<a)|(1<<b))
    rec(0,(),0)
    return F

def brute_faces(E):
    F={()}
    for k in range(1,5):
        for comb in itertools.combinations(range(len(E)),k):
            endpoints=[v for j in comb for v in E[j]]
            if len(set(endpoints))==2*k:F.add(comb)
    return F

def rowvector_ranks(faces):
    layers=collections.defaultdict(list)
    for f in faces:layers[len(f)].append(f)
    maxk=max(layers)
    ranks=[0]
    for k in range(1,maxk+1):
        preceding={f:i for i,f in enumerate(sorted(layers[k-1]))}
        pivot={}
        for face in sorted(layers[k]):
            bits=0
            for j in range(k):bits^=1<<preceding[face[:j]+face[j+1:]]
            while bits:
                h=bits.bit_length()-1
                if h in pivot:bits^=pivot[h]
                else:pivot[h]=bits;break
        ranks.append(len(pivot))
    ranks.append(0)
    return ranks

def free_cofaces(live):
    co=collections.defaultdict(list)
    for upper in live:
        if len(upper)<2:continue
        for j in range(len(upper)):
            low=upper[:j]+upper[j+1:]
            if low in live:co[low].append(upper)
    return co

def make_certificate(faces):
    live={f for f in faces if f}
    collapses=[]
    while True:
        co=free_cofaces(live)
        free=[(len(low),low,parents[0]) for low,parents in co.items()
              if len(parents)==1 and low]
        if not free:break
        maxdim=max(x[0] for x in free)
        _,low,upper=min((x for x in free if x[0]==maxdim),key=lambda x:(x[1],x[2]))
        live.remove(low);live.remove(upper)
        collapses.append([list(low),list(upper)])
    # Spanning tree of collapsed one-skeleton, deterministic breadth first search.
    eds={f for f in live if len(f)==2}
    verts={f[0] for f in live if len(f)==1}
    neighbors=collections.defaultdict(set)
    for a,b in eds:neighbors[a].add(b);neighbors[b].add(a)
    root=min(verts);seen={root};queue=collections.deque([root]);tree=[]
    while queue:
        a=queue.popleft()
        for b in sorted(neighbors[a]):
            if b not in seen:
                seen.add(b);queue.append(b);tree.append([min(a,b),max(a,b)])
    assert seen==verts
    active=set(eds)-{tuple(t) for t in tree}
    triangles=sorted(f for f in live if len(f)==3)
    eliminate=[]
    while active:
        success=False
        for tri in triangles:
            e=[tuple(pair) for pair in itertools.combinations(tri,2)]
            unresolved=[x for x in e if x in active]
            if len(unresolved)==1:
                x=unresolved[0]
                eliminate.append([list(tri),list(x)])
                active.remove(x)
                success=True
                break
        if not success:break
    return {'collapses':collapses,'spanning_tree':tree,'eliminations':eliminate}

def verify_certificate(faces, cert, expected):
    live={f for f in faces if f}
    for low,upper in cert['collapses']:
        low=tuple(low);upper=tuple(upper)
        assert low in live and upper in live and len(upper)==len(low)+1
        assert set(low).issubset(upper)
        assert free_cofaces(live)[low]==[upper], (low,upper)
        live.remove(low);live.remove(upper)
    assert max(map(len,live))==3
    counts=collections.Counter(map(len,live))
    assert [counts[k] for k in range(1,4)]==expected['collapsed_faces'],counts
    verts={f[0] for f in live if len(f)==1}
    eds={f for f in live if len(f)==2}
    tree={tuple(x) for x in cert['spanning_tree']}
    assert len(tree)==len(verts)-1 and tree.issubset(eds)
    neighbors=collections.defaultdict(set)
    for a,b in tree:neighbors[a].add(b);neighbors[b].add(a)
    seen={min(verts)};queue=collections.deque(seen)
    while queue:
        a=queue.popleft()
        for b in neighbors[a]:
            if b not in seen:seen.add(b);queue.append(b)
    assert seen==verts
    active=eds-tree
    tri={f for f in live if len(f)==3}
    for t,e in cert['eliminations']:
        t=tuple(t);e=tuple(e)
        assert t in tri and e in active
        boundary=set(tuple(pair) for pair in itertools.combinations(t,2))
        assert boundary & active=={e}
        active.remove(e)
    assert not active
    assert len(cert['collapses'])==expected['collapses']
    assert len(cert['eliminations'])==expected['eliminations']
    assert len(verts)-len(eds)+len(tri)==expected['spheres']+1
    return counts

EXPECTED={
 'rectangle':{'edges':12,'faces':[1,12,44,56,18], 'ranks':[0,1,11,33,18,0],
              'collapsed_faces':[12,37,31], 'collapses':25,'eliminations':26,'spheres':5},
 'cylinder': {'edges':15,'faces':[1,15,69,107,36], 'ranks':[0,1,14,55,36,0],
              'collapsed_faces':[15,62,64], 'collapses':43,'eliminations':48,'spheres':16},
 'torus':    {'edges':18,'faces':[1,18,99,180,72], 'ranks':[0,1,17,82,72,0],
              'collapsed_faces':[18,91,100],'collapses':80,'eliminations':74,'spheres':26}
}

def run():
    data={}
    results={}
    for typ in ('rectangle','cylinder','torus'):
        exp=EXPECTED[typ]
        E=graph(typ)
        assert len(E)==exp['edges']
        faces=enumerate_faces(E)
        # Independent test: combination enumeration, without the recursive algorithm.
        assert faces==brute_faces(E)
        counts=[sum(len(f)==k for f in faces) for k in range(5)]
        assert counts==exp['faces'],(typ,counts)
        ranks=rowvector_ranks(faces)
        assert ranks==exp['ranks'],(typ,ranks)
        beta=[counts[k]-ranks[k]-ranks[k+1] for k in range(5)]
        assert beta==[0,0,0,exp['spheres'],0],(typ,beta)
        if sys.argv[1:]==['--create-certificate']:
            data[typ]=make_certificate(faces)
        else:
            cert=json.loads((HERE/'CERTIFICATE.json').read_text())
            collapsed=verify_certificate(faces,cert[typ],exp)
            results[typ]={'graph_vertices':9,'graph_edges':len(E),
             'simplices_by_cardinality':counts,
             'reduced_mod2_betti_by_cardinality':beta,
             'mod2_boundary_ranks':ranks,
             'elementary_collapse_pairs':len(cert[typ]['collapses']),
             'collapsing_core_faces_by_cardinality':{str(k):collapsed[k] for k in range(1,4)},
             'spanning_tree_edges':len(cert[typ]['spanning_tree']),
             'fundamental_group_generators_killed':len(cert[typ]['eliminations']),
             'integral_wedge_2_spheres':exp['spheres']}
    if sys.argv[1:]==['--create-certificate']:
        (HERE/'CERTIFICATE.json').write_text(json.dumps(data,separators=(',',':'),ensure_ascii=False)+'\n')
        return
    print(json.dumps(results,sort_keys=True,indent=2))
    print('THREE_BOUNDARY_MATCHING_COMPLEX_CERTIFICATE_PASS')

if __name__=='__main__':run()
