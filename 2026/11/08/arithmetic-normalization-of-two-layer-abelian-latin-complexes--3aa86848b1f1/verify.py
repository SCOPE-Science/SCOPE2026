#!/usr/bin/env python3
"""Independent finite combinatorial checks for two-level group-sum complexes.
Run: python3 verify.py; standard library only. Vertex labels: (shore,tuple)."""
from itertools import product,combinations
from collections import defaultdict,deque

def group(mods):
    return list(product(*(range(m) for m in mods)))
def add(x,y,mods):
    return tuple((a+b)%m for a,b,m in zip(x,y,mods))
def neg(x,mods):
    return tuple((-a)%m for a,m in zip(x,mods))
def mul(t,k,mods):
    return tuple((a*k)%m for a,m in zip(t,mods))
def rank2(rows,cols):
    piv={}
    for x in rows:
        while x:
            p=x.bit_length()-1
            if p not in piv:
                piv[p]=x; break
            x^=piv[p]
    return len(piv)
def check(mods,t):
    A=group(mods); n=len(A); z=(0,)*len(mods)
    assert t in A and t!=z
    H={mul(t,k,mods) for k in range(n)}
    m=len(H); d=n//m
    assert m>=2 and n==m*d
    cosets=[]; remaining=set(A)
    while remaining:
        a=min(remaining)
        c={add(a,h,mods) for h in H}
        cosets.append(c); remaining-=c
    assert len(cosets)==d
    idx={a:i for i,C in enumerate(cosets) for a in C}
    vertices=[(i,a) for i in range(3) for a in A]
    vid={v:i for i,v in enumerate(vertices)}
    triangles=[]
    for a,b in product(A, repeat=2):
        c=neg(add(a,b,mods),mods)
        for delta in (z,t):
            triangles.append(tuple(sorted((vid[(0,a)],vid[(1,b)],vid[(2,add(c,delta,mods))]))))
    triangles=set(triangles)
    assert len(triangles)==2*n*n
    edges={tuple(sorted(e)) for tri in triangles for e in combinations(tri,2)}
    assert len(edges)==3*n*n
    incident=defaultdict(list)
    for j,tri in enumerate(sorted(triangles)):
        for e in combinations(tri,2): incident[e].append(j)
    assert all(len(incident[e])==2 for e in edges)
    # Verify complete tripartite one-skeleton and incidence links.
    for v in range(3*n):
        link_edges={tuple(sorted((x,y))) for tri in triangles if v in tri
                    for x,y in [tuple(i for i in tri if i!=v)]}
        lk_vertices={w for e in link_edges for w in e}
        assert len(lk_vertices)==2*n and len(link_edges)==2*n
        adj=defaultdict(set)
        for a,b in link_edges: adj[a].add(b);adj[b].add(a)
        assert all(len(adj[w])==2 for w in lk_vertices)
        seen=set(); cycles=[]
        for x in lk_vertices:
            if x in seen: continue
            q=[x];seen.add(x);c=0
            for u in q:
                c+=1
                for w in adj[u]:
                    if w not in seen: seen.add(w);q.append(w)
            cycles.append(c)
        assert len(cycles)==d and sorted(cycles)==[2*m]*d
    # Every triangle lies in one of the d^2 surface sheets (coset pair).
    sheets=defaultdict(set)
    for tri in triangles:
        a,b,c=(vertices[v][1] for v in tri)
        i,j,k=idx[a],idx[b],idx[c]
        assert all(idx[x]==i for x in cosets[i])
        sheets[(i,j)].add(tri)
    assert len(sheets)==d*d
    memberships=defaultdict(set)
    for sheet,tris in sheets.items():
        vs={v for tri in tris for v in tri}
        es={tuple(sorted(e)) for tri in tris for e in combinations(tri,2)}
        assert len(vs)==3*m and len(es)==3*m*m and len(tris)==2*m*m
        assert all(sum(e[0] in tri and e[1] in tri for tri in tris)==2 for e in es)
        for v in vs:memberships[v].add(sheet)
    assert len(memberships)==3*n
    assert all(len(s)==d for s in memberships.values())
    assert sum(len(s) for s in memberships.values())==3*n*d
    # Incidence graph of surface-sheets and old vertices, graph cycle rank.
    nodes_s=list(sheets); nodes_v=list(memberships)
    adj=defaultdict(set)
    for v, ss in memberships.items():
        for sheet in ss:
            adj[('v',v)].add(('s',sheet));adj[('s',sheet)].add(('v',v))
    seen=set();q=[('s',nodes_s[0])];seen.add(q[0])
    for u in q:
        for w in adj[u]:
            if w not in seen:seen.add(w);q.append(w)
    assert len(seen)==d*d+3*n
    b=3*n*d-(d*d+3*n)+1
    assert b>=0
    # Independent mod-two chain ranks for the complete simplicial complex.
    E=sorted(edges); EI={e:i for i,e in enumerate(E)}
    F=sorted(triangles)
    rowsB1=[(1<<e[0])^(1<<e[1]) for e in E]
    rowsB2=[sum(1<<EI[tuple(sorted(e))] for e in combinations(tri,2)) for tri in F]
    r1=rank2(rowsB1,len(vertices));r2=rank2(rowsB2,len(E))
    b0=len(vertices)-r1; b1=len(E)-r1-r2; b2=len(F)-r2
    assert b0==1 and b2==d*d and b1==n*n+d*d-3*n+1,(mods,t,b0,b1,b2)
    g=(m-1)*(m-2)//2
    assert 2*g*d*d+b==b1
    print(f'mods={mods}, t={t}, n={n}, ord={m}, d={d}; f=({3*n},{3*n*n},{2*n*n}); sheets={d*d} genus={g}; graphloops={b}; Betti_F2=(1,{b1},{b2})')

cases=[((3,),(1,)),((4,),(1,)),((4,),(2,)),((6,),(2,)),((6,),(3,)),
       ((8,),(2,)),((2,2),(1,0)),((2,4),(0,1)),((3,3),(1,0)),
       ((2,2,2),(1,1,1))]
for mods,t in cases:check(mods,t)
print('ALL_TWO_LEVEL_CHECKS_OK')
