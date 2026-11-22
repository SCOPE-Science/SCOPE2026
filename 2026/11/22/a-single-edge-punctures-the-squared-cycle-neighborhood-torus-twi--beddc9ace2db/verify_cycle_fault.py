"""Exact checks for edge-deleted squared-cycle open-neighborhood complexes.

The unrestricted result is proved by the symbolic simplicial-collapse and
surface argument in RESULT.md. This executable checks independently each
finite instance in the stated test range.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

def fs(S): return frozenset(S)
def faces_from_facets(facets):
    faces={fs(())}
    for facet in facets:
        v=sorted(facet)
        for k in range(1,len(v)+1):
            for sub in combinations(v,k): faces.add(fs(sub))
    return faces

def neighborhoods(n, defect):
    adj=[set() for _ in range(n)]
    for v in range(n):
        for d in (1,2):
            w=(v+d)%n
            adj[v].add(w); adj[w].add(v)
    if defect:
        adj[0].remove(defect);adj[defect].remove(0)
    return [fs(a) for a in adj]

def torus_triangles(n):
    A=[fs(((i-2)%n,(i-1)%n,(i+2)%n)) for i in range(n)]
    B=[fs(((i-2)%n,(i+1)%n,(i+2)%n)) for i in range(n)]
    return A,B

def free_pair(K,small,big):
    assert small in K and big in K and len(big)==len(small)+1 and small < big, (small,big)
    cofaces=[f for f in K if f>=small]
    assert set(cofaces)=={small,big},(small,big,cofaces)
    K.remove(small);K.remove(big)

def betti_mod2(K):
    dims=max(map(len,K))
    fsizes=[[tuple(sorted(f)) for f in K if len(f)==k] for k in range(1,dims+1)]
    indices=[{f:i for i,f in enumerate(F)} for F in fsizes]
    ranks=[]
    for k in range(1,dims):
        piv={}
        for f in fsizes[k]:
            b=0
            for i in range(len(f)):
                b ^= (1<<indices[k-1][f[:i]+f[i+1:]])
            while b:
                p=b.bit_length()-1
                if p in piv: b^=piv[p]
                else: piv[p]=b;break
        ranks.append(len(piv))
    return [len(F)-(ranks[i-1] if i else 1)-(ranks[i] if i<len(ranks) else 0) for i,F in enumerate(fsizes)]

def connected_graph(K,n):
    adj=[set() for _ in range(n)]
    for f in K:
        if len(f)==2:
            x,y=tuple(f);adj[x].add(y);adj[y].add(x)
    seen={0};todo=[0]
    while todo:
        x=todo.pop()
        for y in adj[x]-seen:seen.add(y);todo.append(y)
    return len(seen)==n

def check(n,k):
    K=faces_from_facets(neighborhoods(n,k))
    orig=faces_from_facets(neighborhoods(n,0))
    A,B=torus_triangles(n)
    T=faces_from_facets(A+B)
    assert len(A)==len(set(A))==n and len(B)==len(set(B))==n
    assert len(set(A+B))==2*n
    assert [sum(len(f)==j for f in orig) for j in range(1,5)]==[n,4*n,4*n,n]
    assert [sum(len(f)==j for f in T) for j in range(1,4)]==[n,3*n,2*n]
    # A closed, connected orientable surface has a two-triangle torus quotient:
    assert connected_graph(T,n)
    edge_degs=Counter(e for t in A+B for e in map(fs,combinations(t,2)))
    assert len(edge_degs)==3*n and set(edge_degs.values())=={2}
    # All vertex links are six-cycles, so no pseudo-surface singularities.
    for v in range(n):
        lk=[t-{v} for t in A+B if v in t]
        deg=Counter(x for edge in lk for x in edge)
        assert len(lk)==6 and len(deg)==6 and set(deg.values())=={2}
    # Orientation: A_i=(i-2,i-1,i+2), B_i=(i-2,i+2,i+1),
    # consistent with cyclic edge orientations in the torus.
    boundary=Counter()
    for i in range(n):
        for tri in (((i-2)%n,(i-1)%n,(i+2)%n),
                    ((i-2)%n,(i+2)%n,(i+1)%n)):
            for x,y in ((tri[1],tri[2]),(tri[2],tri[0]),(tri[0],tri[1])):
                if x<y: boundary[(x,y)]+=1
                else: boundary[(y,x)]-=1
    assert all(v==0 for v in boundary.values()),[(key,v) for key,v in boundary.items() if v]
    # The two edge-fault orbits are (0,1) and (0,2).
    for i in range(n):
        if i in (0,k): continue
        Q=fs(((i-2)%n,(i-1)%n,(i+1)%n,(i+2)%n))
        U=fs(((i-2)%n,(i-1)%n,(i+1)%n))
        free_pair(K,U,Q)
    for i in range(n):
        if i in (0,k): continue
        V=fs(((i-1)%n,(i+1)%n,(i+2)%n))
        E=fs(((i-1)%n,(i+1)%n))
        free_pair(K,E,V)
    if k==2:
        free_pair(K,fs((n-1,1)),fs((n-2,n-1,1)))
        free_pair(K,fs((1,3)),fs((1,3,4)))
    deleted={B[0],A[1]} if k==1 else {A[0],B[0],A[2],B[2]}
    expected=faces_from_facets(set(A+B)-deleted)
    assert K==expected,('core mismatch',n,k, K^expected)
    assert len([x for x in expected if len(x)==3])==2*n-(2 if k==1 else 4)
    assert [sum(len(f)==j for f in expected) for j in range(1,4)]==[n,3*n-(0 if k==1 else 2),2*n-(2 if k==1 else 4)]
    assert sum((-1)**(len(f)-1) for f in expected if f)==-2
    # Peel all residual triangles, leaving a connected graph.
    while True:
        co=defaultdict(list)
        for f in K:
            if len(f)==3:
                for e in combinations(f,2):co[fs(e)].append(f)
        free=sorted(((e,ts[0]) for e,ts in co.items() if len(ts)==1),key=lambda z:(tuple(sorted(z[0])),tuple(sorted(z[1]))))
        if not free:break
        free_pair(K,*free[0])
    assert all(len(f)<=2 for f in K)
    assert connected_graph(K,n)
    graph_edges=sum(len(f)==2 for f in K)
    assert graph_edges-n+1==3
    # Independent face enumeration and binary boundary elimination.
    full_fault=faces_from_facets(neighborhoods(n,k))
    assert [sum(len(f)==j for f in full_fault) for j in range(1,5)]==[n,4*n-2,4*n-6,n-2]
    assert betti_mod2(full_fault)==[0,3,0,0]
    return graph_edges

if __name__=='__main__':
    for n in range(9,65):
        for k in (1,2):check(n,k)
    print('CYCLE_SQUARE_EDGE_FAULT_VERIFY_OK: 112 independently generated finite instances (n=9..64, both edge orbits)')
