#!/usr/bin/env python3
"""Exact finite certificate: S4 action on graph of involution-invariant directed forests."""
from itertools import product, permutations, combinations
from collections import deque, defaultdict

# All original arrows of the complete loopless bidirected graph on six labels.
ARCS=[(a,b) for a in range(6) for b in range(6) if a!=b]
def tau(a): return a^1
def translate_arc(e):return (tau(e[0]),tau(e[1]))
ORBIT_SET={tuple(sorted((e,translate_arc(e)))) for e in ARCS}
assert len(ORBIT_SET)==15
ORBITS=sorted(ORBIT_SET)
def is_forest(arcs):
    successor={}
    for a,b in arcs:
        if a in successor:return False
        successor[a]=b
    for a in successor:
        v=a;seen=set()
        while v in successor:
            if v in seen:return False
            seen.add(v);v=successor[v]
    return True
assert sum(is_forest(o) for o in ORBITS)==12

def encode(o):
    a,b=o[0]; i,j=a//2,b//2; phase=(a%2)^(b%2)
    if i==j: return None
    return (i,j,phase)
V=sorted(encode(o) for o in ORBITS if is_forest(o))
assert len(V)==12 and len(set(V))==12
orbit_of={encode(o):o for o in ORBITS if is_forest(o)}
E=[]
for a,b in combinations(V,2):
    if is_forest(orbit_of[a]+orbit_of[b]):E.append((a,b))
assert len(E)==36
# Compare direct original 6-label forest test with a graph-theoretic shortcut.
for a,b in combinations(V,2):
    i,j,p=a;u,v,q=b
    criterion=(j!=v and not(i==v and j==u))
    # Original arrows use one outgoing per label, so reverse roles compared to incoming convention.
    # Outgoing at sources i/u, not targets j/v. The correct condition is distinct SOURCES.
    criterion=(i!=u and not(i==v and j==u))
    assert criterion == ((a,b) in E)

# Connectedness and edge orientation: edges ordered lexicographically by V order.
vi={a:i for i,a in enumerate(V)}
EI=[(vi[a],vi[b]) for a,b in E]
assert all(a<b for a,b in EI)
adj=[[] for _ in V]
for j,(a,b) in enumerate(EI):adj[a].append((b,j));adj[b].append((a,j))
parent={0:None};parent_edge={};todo=deque([0]);tree=set()
while todo:
    a=todo.popleft()
    for b,e in adj[a]:
        if b not in parent:
            parent[b]=a;parent_edge[b]=e;tree.add(e);todo.append(b)
assert len(parent)==12 and len(tree)==11
chords=[e for e in range(len(EI)) if e not in tree]
assert len(chords)==25

def fundamental_cycle(e):
    a,b=EI[e];seq={e:1};at=b
    # Find path on spanning tree from b to a.
    paths={}
    while at is not None:
        paths[at]=True;at=parent[at]
    at=a
    while at not in paths:at=parent[at]
    lca=at
    at=b
    while at!=lca:
        t=parent_edge[at];u,v=EI[t]; z=parent[at]
        sign=1 if (u,v)==(at,z) else -1
        seq[t]=sign;at=z
    stack=[];at=a
    while at!=lca:
        stack.append(at);at=parent[at]
    for at in reversed(stack):
        t=parent_edge[at];z=parent[at];u,v=EI[t]
        sign=1 if (u,v)==(z,at) else -1
        seq[t]=sign
    return seq
cycles={e:fundamental_cycle(e) for e in chords}
for e,chain in cycles.items():
    balance=[0]*len(V)
    for j,c in chain.items():
        a,b=EI[j];balance[a]-=c;balance[b]+=c
    assert not any(balance)

def canon(v):return min(tuple(v),tuple(1-t for t in v))
X=sorted({canon(v) for v in product((0,1),repeat=3)})
assert len(X)==4
stats=defaultdict(list);group_perms=set()
def cyclotype(p):
    visited=set();v=[]
    for i in range(len(p)):
        if i in visited:continue
        j=i;n=0
        while j not in visited:visited.add(j);j=p[j];n+=1
        v.append(n)
    return tuple(sorted(v,reverse=True))

for perm in permutations(range(3)):
    for f in product((0,1),repeat=3):
        if f>tuple(1-t for t in f):continue # quotient by central simultaneous flip
        def act(a):return (perm[a[0]],perm[a[1]],a[2]^f[a[0]]^f[a[1]])
        vp=[vi[act(a)] for a in V]
        assert sorted(vp)==list(range(len(V)))
        p4=tuple(X.index(canon(tuple(f[i]^x[perm.index(i)] for i in range(3)))) for x in X)
        assert sorted(p4)==list(range(4))
        group_perms.add(p4)
        fixed_vertices=sum(i==a for i,a in enumerate(vp))
        signed_edge_trace=0
        emap=[]
        for i,(a,b) in enumerate(EI):
            u,v=vp[a],vp[b]
            if u<v: p=(u,v);sign=1
            else:p=(v,u);sign=-1
            j=EI.index(p)
            emap.append((j,sign))
            if i==j:signed_edge_trace+=sign
        lef=1-fixed_vertices+signed_edge_trace
        # Independent direct trace on H1 using fundamental cycle coordinates.
        direct=0
        for e in chords:
            s=0
            for edge_idx,c in cycles[e].items():
                j,sg=emap[edge_idx]
                if j==e:s+=c*sg
            direct+=s
        assert lef==direct
        stats[cyclotype(p4)].append((lef,fixed_vertices,signed_edge_trace))
assert len(group_perms)==24
expected={
    (1,1,1,1):(1,25,12,36),
    (2,1,1):(6,-1,0,-2),
    (2,2):(3,-3,4,0),
    (3,1):(8,1,0,0),
    (4,):(6,1,0,0),
}
for typ,(cnt,trace,vertex_fix,edge_trace) in expected.items():
    assert len(stats[typ])==cnt
    assert set(stats[typ])=={(trace,vertex_fix,edge_trace)}
    print('cycle_type',typ,'count',cnt,'H1_trace',trace,'vertex_fix',vertex_fix,'signed_edge_trace',edge_trace)
assert len(stats)==5
chars={
 (1,1,1,1):(1,1,3,3,2),
 (2,1,1):(1,-1,1,-1,0),
 (2,2):(1,1,-1,-1,2),
 (3,1):(1,1,0,0,-1),
 (4,):(1,-1,-1,1,0),
}
mult=[]
for j in range(5):
    total=sum(sum(v[0]*chars[typ][j] for v in values) for typ,values in stats.items())
    assert total%24==0
    mult.append(total//24)
assert mult==[1,1,3,4,1]
assert sum(a*b for a,b in zip(mult,[1,1,3,3,2]))==25
print('irreducible_multiplicities_triv_sign_std_signstd_two',*mult)
print('original_arcs',len(ARCS),'arrow_orbits',len(ORBITS),'fixed_graph_vertices',len(V),'fixed_graph_edges',len(E),'rank_H1',len(chords),'residual_group_order',len(group_perms))
print('DIRECTED_FOREST_FIXED_S4_CHARACTER_PASS')
