"""Finite independent checks for size-bounded connected-subtree shattering.

Run with Python 3 and NetworkX: python check_subtree_shattering.py
The general theorem requires a mathematical proof; this checker tests finite cases.
"""
from collections import defaultdict
import networkx as nx


def mul(a, b):
    o = defaultdict(int)
    for (i,j), ai in a.items():
        for (k,l), bj in b.items():
            o[(i+k, j+l)] += ai*bj
    return dict(o)


def polynomial_by_recurrence(g):
    n = len(g)
    root = next(iter(g))
    parent = {root: None}
    order = [root]
    for v in order:
        for w in g.neighbors(v):
            if w not in parent:
                parent[w]=v
                order.append(w)
    A, B = {}, {}
    for v in reversed(order):
        ch = [w for w in g[v] if parent.get(w)==v]
        P = {(0,0): 1}
        sumA = defaultdict(int)
        for w in ch:
            for ij,x in A[w].items():sumA[ij] += x
            new = dict(A[w]); new[(0,0)] = new.get((0,0),0)+1
            P=mul(P,new)
        Av=defaultdict(int); Bv=defaultdict(int)
        for (i,j),x in P.items():
            Av[(i+1,j)] += x
            Bv[(i+1,j)] += x
        Av[(1,0)] -= 1; Av[(1,1)] += 1
        Bv[(1,0)] -= 1; Bv[(1,1)] += 1
        for (i,j),x in sumA.items():
            Bv[(i+1,j)] -= x
            Bv[(i+1,j+1)] += x
        A[v] = {k:x for k,x in Av.items() if x}
        B[v] = {k:x for k,x in Bv.items() if x}
    ans=defaultdict(int)
    for b in B.values():
        for k,x in b.items():ans[k]+=x
    return dict(ans)


def graph_mask(g):
    nodes=list(g)
    return [[int(g.has_edge(v,w)) for w in nodes] for v in nodes]


def connected(mask, adj, n):
    if not mask:return False
    bit=mask & -mask
    seen=bit
    stack=[bit.bit_length()-1]
    while stack:
        v=stack.pop()
        for w in range(n):
            if adj[v][w] and mask & (1<<w) and not seen & (1<<w):
                seen |=1<<w;stack.append(w)
    return seen==mask


def hull(mask, adj, n):
    if mask.bit_count()<2:return mask
    from collections import deque
    vertices=[x for x in range(n) if mask & (1<<x)]
    result=mask
    start=vertices[0]
    for end in vertices[1:]:
        prev={start:-1};queue=deque([start])
        while queue and end not in prev:
            v=queue.popleft()
            for w in range(n):
                if adj[v][w] and w not in prev:
                    prev[w]=v;queue.append(w)
        at=end
        while at!=-1:
            result |=1<<at
            at=prev[at]
    return result


def leaves(mask, adj, n):
    if mask.bit_count()==1:return mask
    out=0
    for v in range(n):
        if mask & (1<<v):
            deg=sum(adj[v][w] for w in range(n) if mask & (1<<w))
            if deg==1:out|=1<<v
    return out


def check(g):
    adj=graph_mask(g);n=len(g);full=1<<n
    connected_subtrees=[m for m in range(1,full) if connected(m,adj,n)]
    direct=defaultdict(int)
    for m in connected_subtrees:
        direct[(m.bit_count(),leaves(m,adj,n).bit_count())]+=1
    byrec=polynomial_by_recurrence(g)
    assert direct==byrec,('recurrence',n,sorted(g.edges()),direct,byrec)
    hulls=[hull(m,adj,n) for m in range(full)]
    for r in range(1,n+1):
        concepts=[0]+[m for m in connected_subtrees if m.bit_count()<=r]
        for S in range(full):
            shattered=len({c&S for c in concepts})==1<<S.bit_count()
            predicted=(S==0 or (hulls[S].bit_count()<=r and S==leaves(hulls[S],adj,n)))
            assert shattered==predicted,('shattering',n,r,sorted(g.edges()),S,shattered,predicted)
        trace=defaultdict(int)
        for S in range(1,full):
            if hulls[S].bit_count()<=r and S==leaves(hulls[S],adj,n):
                trace[S.bit_count()]+=1
        from_poly=defaultdict(int)
        for (i,j),value in direct.items():
            if i<=r: from_poly[j]+=value
        assert dict(trace)==dict(from_poly),('poly',n,r,trace,from_poly)
    return full*n


def run():
    instances=0; supports=0
    g=nx.empty_graph(1)
    supports+=check(g);instances+=1
    for n in range(2,9):
        for g in nx.nonisomorphic_trees(n):
            supports+=check(g);instances+=1
    print('BOUNDED_SUBTREE_SHATTERING_PASS',instances,'tree_shapes',supports,'support_radius_cases')
    for m in range(2,13):
        g=nx.star_graph(m)
        poly=polynomial_by_recurrence(g)
        full=[sum(v for (i,j),v in poly.items() if j==k) for k in range(m+2)]
        assert full[1]==m+1
        assert full[2]==m+(m*(m-1)//2)
        for k in range(3,m+1):assert full[k] == __import__('math').comb(m,k)
    print('STAR_FACETS_PASS',11)

if __name__=='__main__':run()


def betti_star(m,r):
    g=nx.star_graph(m)
    n=m+1;adj=graph_mask(g)
    faces=defaultdict(list)
    for S in range(1,1<<n):
        h=hull(S,adj,n)
        if h.bit_count()<=r and leaves(h,adj,n)==S:
            faces[S.bit_count()-1].append(S)
    ranks={}
    maxd=max(faces)
    for d in range(1,maxd+1):
        lower={f:i for i,f in enumerate(faces[d-1])}
        basis={}
        for face in faces[d]:
            vector=0
            for v in range(n):
                if face & 1<<v:
                    vector ^= 1<<lower[face^(1<<v)]
            while vector:
                pivot=vector.bit_length()-1
                if pivot in basis: vector ^= basis[pivot]
                else:
                    basis[pivot]=vector;break
        ranks[d]=len(basis)
    return {d:len(v)-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)
            for d,v in faces.items() if len(v)-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)}


def homology_checks():
    import math
    cases=0
    for m in range(3,9):
        for r in range(1,m+2):
            actual=betti_star(m,r)
            if r==1: expected={0:m}
            elif r==2: expected={}
            else:
                expected={1:m-1}
                if r<=m:
                    dim=r-2
                    expected[dim]=expected.get(dim,0)+math.comb(m-1,r-1)
            assert actual==expected,(m,r,actual,expected)
            cases+=1
    print('STAR_HOMOLOGY_PASS',cases)

if __name__=='__main__':homology_checks()
