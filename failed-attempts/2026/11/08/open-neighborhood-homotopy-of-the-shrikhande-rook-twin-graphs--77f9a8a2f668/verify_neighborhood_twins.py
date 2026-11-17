#!/usr/bin/env python3
"""Exact finite certificate for open-neighborhood complexes of two SRG(16,6,2,2) graphs.

Run: python3 verify_neighborhood_twins.py
Only the Python standard library is needed. 16-bit masks encode all simplices.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from math import gcd
from itertools import combinations

N = 16
V = tuple((i, j) for i in range(4) for j in range(4))

def graphs():
    steps = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1))
    sh = []
    rook = []
    for i, j in V:
        sh.append(frozenset(4*((i+a)%4)+(j+b)%4 for a,b in steps))
        rook.append(frozenset(k for k,(x,y) in enumerate(V)
                              if (x==i or y==j) and (x,y)!=(i,j)))
    return {'Shrikhande': tuple(sh), 'rook': tuple(rook)}

def graph_checks(adj, name):
    assert len(adj)==16
    for a in range(16):
        assert len(adj[a])==6 and a not in adj[a]
        for b in range(16):
            assert (a in adj[b]) == (b in adj[a])
            if a!=b: assert len(adj[a]&adj[b])==2
    # Their induced vertex-neighborhood graphs distinguish the twins.
    local_degrees=sorted(len(adj[v]&adj[0]) for v in adj[0])
    assert local_degrees == ([2]*6 if name=='Shrikhande' else [2]*6)
    # The two regular local graphs are respectively C6 and 2 disjoint triangles.
    seen=set(); components=[]
    for a in sorted(adj[0]):
        if a in seen: continue
        Q=[a];seen.add(a);t=[]
        while Q:
            z=Q.pop();t.append(z)
            for b in adj[z]&adj[0]:
                if b not in seen: seen.add(b);Q.append(b)
        components.append(len(t))
    assert sorted(components) == ([6] if name=='Shrikhande' else [3,3])

def face_list(adj):
    masks=[sum(1<<u for u in A) for A in adj]
    F=set()
    for M in masks:
        sub=M
        while sub:
            F.add(sub)
            sub=(sub-1)&M
    # Second, independent definition: exhaust all 65,535 nonempty subsets.
    direct={f for f in range(1,1<<16) if any((f & ~M)==0 for M in masks)}
    assert F==direct
    assert len(F)==808
    assert tuple(Counter(f.bit_count() for f in F)[i] for i in range(1,7)) == (16,120,320,240,96,16)
    return F

def matching(F):
    active=set(F);pairs=[]
    for v in range(16):
        bit=1<<v
        for f in sorted(active):
            t=f|bit
            if (f&bit)==0 and t in active:
                assert t.bit_count()==f.bit_count()+1
                active.remove(f);active.remove(t)
                pairs.append((f,t))
    assert len(pairs)==375 and len(active)==58
    assert Counter(f.bit_count()-1 for f in active)=={0:1,1:1,2:56}
    used=[x for p in pairs for x in p]
    assert len(set(used))==len(used) and set(used).isdisjoint(active)
    assert set(used)|active==F
    return active,pairs

def acyclic_hasse(F,pairs):
    matched=set(pairs)
    out=defaultdict(list); indeg={f:0 for f in F}; incidences=0
    for upper in F:
        bits=upper
        while bits and upper.bit_count()>=2:
            b=bits & -bits;bits-=b
            lower=upper^b
            assert lower in F
            if (lower,upper) in matched:
                src,dst=lower,upper
            else:
                src,dst=upper,lower
            out[src].append(dst);indeg[dst]+=1;incidences+=1
    Q=deque(f for f,d in indeg.items() if not d)
    visited=0
    while Q:
        f=Q.popleft();visited+=1
        for g in out[f]:
            indeg[g]-=1
            if indeg[g]==0:Q.append(g)
    assert visited==len(F)
    assert incidences==sum(f.bit_count() for f in F if f.bit_count()>1)
    return incidences

def boundary_of_triangle(t):
    vs=[v for v in range(16) if t>>v&1]
    assert len(vs)==3
    return tuple((t^(1<<v), (-1)**j) for j,v in enumerate(vs))

def degree_matrix(active,pairs):
    critedge=[f for f in active if f.bit_count()==2]
    crittri=sorted(f for f in active if f.bit_count()==3)
    assert len(critedge)==1 and len(crittri)==56
    mate={f:t for f,t in pairs if f.bit_count()==2}
    tree_edges={t for f,t in pairs if f.bit_count()==1}
    assert len(mate)==104 and len(tree_edges)==15
    assert critedge[0] not in mate and critedge[0] not in tree_edges
    # Verify the vertex-to-edge matched edges form a spanning tree.
    parent=list(range(16))
    def find(a):
        while parent[a]!=a:
            a=parent[a]
        return a
    for e in tree_edges:
        endpoints=[v for v in range(16) if e>>v&1]
        assert len(endpoints)==2
        a,b=map(find,endpoints)
        assert a!=b
        parent[a]=b
    assert len({find(v) for v in range(16)})==1
    assert len(mate)+len(tree_edges)+len(critedge)==120
    @lru_cache(None)
    def reduce_edge(e):
        """Coefficient of unique critical edge, after eliminating paired 1/2 cells."""
        if e not in mate:
            assert e==critedge[0] or e in tree_edges
            return int(e==critedge[0])
        triangle=mate[e]
        faces=dict(boundary_of_triangle(triangle))
        pivot=faces.pop(e)
        assert pivot in (-1,1)
        return -pivot*sum(a*reduce_edge(b) for b,a in faces.items())
    all_edges={f for f in active if f.bit_count()==2} | set(mate) | tree_edges
    assert len(all_edges)==120
    for e in all_edges: reduce_edge(e)
    degrees=[sum(a*reduce_edge(e) for e,a in boundary_of_triangle(t)) for t in crittri]
    d=0
    for x in degrees: d=gcd(d,abs(x))
    assert d==2
    assert all(x in (-2,0,2) for x in degrees)
    return Counter(degrees), d, critedge[0],len(mate)

def rational_rank_boundary2(F):
    # Exact fraction-free rational rank using SymPy only if installed is not
    # necessary for this self-contained proof: matching degrees certify ranks.
    # Independent small-modulus check on the ORIGINAL boundary matrix below.
    ed=sorted(f for f in F if f.bit_count()==2)
    tr=sorted(f for f in F if f.bit_count()==3)
    pos={f:i for i,f in enumerate(ed)}
    rows=[]
    for t in tr:
        b=0
        for e,_ in boundary_of_triangle(t): b^=1<<pos[e]
        rows.append(b)
    pivot={}
    for v in rows:
        while v:
            i=v.bit_length()-1
            if i in pivot:v^=pivot[i]
            else:pivot[i]=v;break
    assert len(pivot)==104
    return len(pivot)

if __name__=='__main__':
    for name,adj in graphs().items():
        graph_checks(adj,name)
        F=face_list(adj)
        active,pairs=matching(F)
        cover=acyclic_hasse(F,pairs)
        degree_counter,d,critical_edge,nmatched=degree_matrix(active,pairs)
        b2=rational_rank_boundary2(F)
        assert degree_counter==(
            Counter({0:39,2:13,-2:4}) if name=='Shrikhande' else
            Counter({0:38,2:9,-2:9}))
        print(name,'faces',len(F),'cover_incidences',cover,
              'pairs',len(pairs),'criticals',dict(sorted(Counter(f.bit_count()-1 for f in active).items())),
              'critical_edge',hex(critical_edge),'degrees',dict(sorted(degree_counter.items())),
              'gcd',d,'mod2_boundary2_rank',b2,
              'homotopy','M(Z/2,1) wedge 55 S^2')
    print('ALL_CHECKS_PASS')
