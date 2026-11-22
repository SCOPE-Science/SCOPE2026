"""Exact graph certificate for prime-degree Fermat standard-line Picard tori.

Uses label arithmetic only.  Runs unconditionally with Python 3 stdlib.
"""
from collections import defaultdict, deque
from math import gcd


def check(m, q):
    assert m >= 3 and all(m % i for i in range(2, int(m ** .5) + 1))
    qm=q % m
    assert gcd(qm,m)==1
    d=1; u=qm
    while u!=1: d+=1; u=(u*qm)%m
    verts=set();edges=[]
    def edge(a,b):
        assert a!=b
        verts.add(a);verts.add(b);edges.append((a,b))
    for t in range(3):
        for a in range(m):
            for b in range(m):
                v=('L',t,a,b)
                edge(v,('H',t,0,a));edge(v,('H',t,1,b))
    for t,s in [(0,1),(0,2),(1,2)]:
        for a in range(m):
            for b in range(m):
                for c in range(m):
                    if (t,s)==(0,1): e=(b+c-a)%m
                    elif (t,s)==(0,2): e=(c-a-b)%m
                    else: e=(a+b-c)%m
                    N=('N',t,s,a,b,c)
                    edge(N,('L',t,a,b));edge(N,('L',s,c,e))
    assert len(verts)==3*m*m+6*m+3*m**3
    assert len(edges)==6*m*m+6*m**3
    R=3*m**3+3*m*m-6*m
    assert len(edges)-len(verts)+1==R+1

    def act(v):
        # All integer fields after the vertex kind and fixed pairing labels are root indices.
        if v[0]=='L': return ('L',v[1],v[2]*qm % m,v[3]*qm % m)
        if v[0]=='H': return ('H',v[1],v[2],v[3]*qm % m)
        return ('N',v[1],v[2],*(x*qm % m for x in v[3:]))
    def canon(e): return frozenset(e)
    edge_set={canon(e) for e in edges}
    assert len(edge_set)==len(edges)
    for a,b in edges: assert canon((act(a),act(b))) in edge_set
    fixed_v={v for v in verts if act(v)==v}
    fixed_e={canon((a,b)) for a,b in edges if act(a)==a and act(b)==b}
    if d>1:
        assert len(fixed_v)==12 and len(fixed_e)==12
        for v in verts-fixed_v:
            u=act(v)
            for _ in range(1,d):
                assert u!=v
                u=act(u)
            assert u==v
    else:
        assert len(fixed_v)==len(verts)
        assert len(fixed_e)==len(edges)
    # Check fixed subgraph connectivity; rank is one in the nonsplit case.
    adj=defaultdict(list)
    for a,b in edges:
        if a in fixed_v and b in fixed_v:
            adj[a].append(b);adj[b].append(a)
    reached={next(iter(fixed_v))};dq=deque(reached)
    while dq:
        for w in adj[dq.popleft()]:
            if w not in reached:
                reached.add(w);dq.append(w)
    assert reached==fixed_v
    assert len(fixed_e)-len(fixed_v)+1==(1 if d>1 else R+1)

    def orbit(v):
        ans=[v];u=act(v)
        while u!=v:
            ans.append(u);u=act(u)
        return frozenset(ans)
    quotient_v={orbit(v) for v in verts}
    quotient_edge=defaultdict(list)
    for a,b in edges:
        quotient_edge[orbit(a)].append((orbit(b), (a,b)))
        quotient_edge[orbit(b)].append((orbit(a), (b,a)))
    # Invariant spanning tree: first choose tree in the fixed subgraph,
    # then attach each free-vertex orbit once to its parent orbit.
    tree=set()
    reached_f={next(iter(fixed_v))};dq=deque(reached_f)
    while dq:
        a=dq.popleft()
        for b in adj[a]:
            if b not in reached_f:
                reached_f.add(b);dq.append(b);tree.add(canon((a,b)))
    done={orbit(v) for v in fixed_v}
    qdq=deque(done)
    while qdq:
        parent=qdq.popleft()
        for child,(a,b) in quotient_edge[parent]:
            if child not in done:
                done.add(child);qdq.append(child)
                e=(a,b)
                for _ in range(d):
                    tree.add(canon(e))
                    e=(act(e[0]),act(e[1]))
    assert done==quotient_v
    assert len(tree)==len(verts)-1
    # Actual connectivity and acyclicity checks, not just counting.
    dj={v:v for v in verts}
    def root(v):
        while dj[v]!=v:
            dj[v]=dj[dj[v]];v=dj[v]
        return v
    for ea in tree:
        a,b=tuple(ea);ra,rb=root(a),root(b)
        assert ra!=rb
        dj[ra]=rb
    assert len({root(v) for v in verts})==1
    assert all(canon((act(a),act(b))) in tree for a,b in (tuple(e) for e in tree))
    free_non_tree=len(edge_set-tree-fixed_e)
    assert free_non_tree == ((R//d)*d if d>1 else 0)
    fixed_non_tree=len(fixed_e-tree)
    assert fixed_non_tree == (1 if d>1 else R+1)
    print('PASS',m,q,'ord',d,'vertices',len(verts),'edges',len(edges),
          'torus-rank',R+1,'fixed-cycle-rank',fixed_non_tree,
          'induced-summands',(R//d if d>1 else 0))

for m,qs in [(5,[11,19,7,13]),(7,[29,13,17]),(11,[23,31,43]),(13,[53,41])]:
    for q in qs: check(m,q)
print('FERMAT_INTEGRAL_PICARD_TORI_VERIFIED')
