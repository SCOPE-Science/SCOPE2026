"""Reproduce the suspension/double opposition-graph theorem on triangulated surfaces.
Requires Python 3.9+ and networkx for the icosahedron case only.
Scientific outputs are constructed from the face lists, with a direct tetrahedron-based double.
"""
from collections import defaultdict, Counter
from itertools import combinations
from random import Random


def comps(vset, edges):
    adj={v:set() for v in vset}
    for x,y in edges:
        adj[x].add(y);adj[y].add(x)
    found=set();groups=[]
    for v in sorted(vset):
        if v in found:continue
        stack=[v];found.add(v);group=set()
        while stack:
            u=stack.pop();group.add(u)
            for w in adj[u]:
                if w not in found:found.add(w);stack.append(w)
        groups.append(group)
    return groups


def faces_ok(tris):
    tris=set(tuple(sorted(t)) for t in tris)
    assert all(len(set(t))==3 for t in tris)
    verts=set().union(*map(set,tris))
    adj=defaultdict(list)
    for tri in tris:
        for e in combinations(tri,2): adj[e].append(tri)
    assert all(len(f)==2 for f in adj.values())
    for v in verts:
        lk_edges=[tuple(sorted(set(t)-{v})) for t in tris if v in t]
        lk_verts=set().union(*map(set,lk_edges))
        assert len(comps(lk_verts,lk_edges))==1
        degree=Counter(x for edge in lk_edges for x in edge)
        assert all(degree[x]==2 for x in lk_verts)
    dual_edges=[]
    for f in adj.values():dual_edges.append((f[0],f[1]))
    assert len(comps(tris,dual_edges))==1
    return verts,adj,tris


def proper_three_colorable(verts,edges):
    neighbors={v:set() for v in verts}
    for a,b in edges:neighbors[a].add(b);neighbors[b].add(a)
    order=sorted(verts,key=lambda v:-len(neighbors[v])); coloring={order[0]:0}
    def backtrack(k):
        if k==len(order):return True
        v=order[k];used={coloring[w] for w in neighbors[v] if w in coloring}
        for c in range(3):
            if c not in used:
                coloring[v]=c
                if backtrack(k+1):return True
                del coloring[v]
        return False
    return backtrack(1)


def analyze(tris, check_coloring=True):
    verts,adj,tris=faces_ok(tris)
    n=len(verts); m=len(adj); f=len(tris); chi=n-m+f
    degree=Counter(v for t in tris for v in t)
    # Independently construct the actual 1-dimensional simplicial double of suspension.
    bvert={('base',e) for e in adj}
    svert={('apex',a,v) for a in (0,1) for v in verts}
    V=bvert|svert
    DE=set()
    for t in tris:
        for a in (0,1):
            for v in t:
                edge=tuple(sorted(set(t)-{v}))
                DE.add(frozenset((('base',edge),('apex',a,v))))
    assert len(V)==m+2*n and len(DE)==6*f==4*m
    # Independently construct the opposite-vertex multigraph.
    Tedges=[]
    for e, tt in adj.items():
        uv=[next(iter(set(t)-set(e))) for t in tt]
        assert len(uv)==2 and uv[0]!=uv[1]
        Tedges.append((uv[0],uv[1]))
    tc=comps(verts,Tedges)
    dc=comps(V,[tuple(e) for e in DE])
    assert len(tc)==len(dc)
    rows=[]
    for C in tc:
        edges_in=[(u,v) for u,v in Tedges if u in C and v in C]
        assert all(u in C and v in C for u,v in edges_in)
        non_base= {('apex',a,v) for a in (0,1) for v in C}
        for comp in dc:
            if non_base & comp: assert non_base <= comp
        direct=next(comp for comp in dc if non_base <= comp)
        assert len(direct)==2*len(C)+len(edges_in)
        d_edges=[e for e in DE if e<=direct]
        beta=len(d_edges)-len(direct)+1
        assert beta==3*len(edges_in)-2*len(C)+1
        assert len(edges_in)*2==sum(degree[v] for v in C)
        rows.append((tuple(sorted(C)),len(edges_in),beta))
    assert sum(r[-1] for r in rows)==7*n-9*chi+len(tc)
    assert 1<=len(tc)<=3
    transversal=[]
    face_sets=[set(t) for t in tris]
    if check_coloring:
        for mask in range(1,1<<n):
            chosen={v for i,v in enumerate(sorted(verts)) if mask & (1<<i)}
            if all(len(chosen & face)==1 for face in face_sets):transversal.append(chosen)
        has_trans=bool(transversal)
        assert (len(tc)>=2)==has_trans
        if len(tc)==3:
            assert len(transversal)==3
        elif len(tc)==2:
            assert len(transversal)==1
        else:assert not transversal
        assert (len(tc)==3)==proper_three_colorable(verts,adj)
        if chi==2:
            assert (len(tc)==3) == all(d%2==0 for d in degree.values())
    return (n,chi,len(tc),tuple(sorted(x[2] for x in rows))),rows


def tetra():return [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
def bipyramid(k):return [(i,(i+1)%k,k+a) for a in (0,1) for i in range(k)]
def octa():return [(a,b,c) for a in (0,1) for b in (2,3) for c in (4,5)]
def face_stellate(tris):
    n=max(max(t) for t in tris)+1
    return [tuple(sorted((n+i,a,b))) for i,t in enumerate(tris) for a,b in combinations(t,2)]
def barycentric(tris):
    ve,adj,tris=faces_ok(tris)
    n=max(ve)+1
    elist=sorted(adj);elist_id={e:n+i for i,e in enumerate(elist)}
    tlist=sorted(tris);tid={t:n+len(elist)+i for i,t in enumerate(tlist)}
    out=[]
    for t in tris:
        for e in combinations(t,2):
            for v in e:out.append((v,elist_id[e],tid[t]))
    return out

def flip_once(tris,rng):
    A={tuple(sorted(t)) for t in tris};m=defaultdict(list)
    for t in A:
        for e in combinations(t,2):m[e].append(t)
    candidates=list(m);rng.shuffle(candidates)
    for e in candidates:
        t1,t2=m[e]
        v=next(iter(set(t1)-set(e)));w=next(iter(set(t2)-set(e)))
        if tuple(sorted((v,w))) in m:continue
        a,b=e
        n1=tuple(sorted((a,v,w)));n2=tuple(sorted((b,v,w)))
        if n1 in A or n2 in A:continue
        return list((A-{t1,t2})|{n1,n2})
    return list(A)

def torus7():return [tuple(sorted(((i+a)%7,(i+b)%7,(i+c)%7))) for tri in ((0,1,3),(0,2,3)) for i in range(7) for a,b,c in [tri]]

def main():
    examples={'tetrahedron':tetra(),'triangular bipyramid':bipyramid(3),'octahedron':octa(),
              'face-stellated tetrahedron':face_stellate(tetra()),
              'barycentric tetrahedron':barycentric(tetra()),'seven-vertex torus':torus7()}
    try:
        import networkx as nx
        G=nx.icosahedral_graph()
        examples['icosahedron']=[t for t in combinations(G.nodes,3) if all(G.has_edge(u,v) for u,v in combinations(t,2))]
    except ImportError:pass
    for name,tris in examples.items():
        meta,rows=analyze(tris)
        print(f'{name}: n,chi,components,component_betti={meta}')
    assert analyze(tetra())[0]==(4,2,1,(11,))
    assert analyze(bipyramid(3))[0]==(5,2,2,(6,13))
    assert analyze(octa())[0]==(6,2,3,(9,9,9))
    assert analyze(face_stellate(tetra()))[0]==(8,2,2,(11,29))
    assert analyze(barycentric(tetra()))[0]==(14,2,3,(25,29,29))
    if 'icosahedron' in examples:assert analyze(examples['icosahedron'])[0]==(12,2,1,(67,))
    rng=Random(20261109);cases=0
    for k in range(3,11):
        tris=bipyramid(k)
        for j in range(12):
            if j%4==0 and len(set().union(*[set(t) for t in tris]))<=11:
                tris=tris+[ ] # keep fixed size; flips preserve valid triangulations
            tris=flip_once(tris,rng)
            analyze(tris,check_coloring=len(set().union(*[set(t) for t in tris]))<=13)
            cases+=1
    print('random_sphere_flip_cases=',cases)
    print('SUSPENSION_DOUBLE_OPPOSITION_TRICHOTOMY_PASS')

if __name__=='__main__':main()
