#!/usr/bin/env python3
"""Exact combinatorial checks for the scale-two graph-metric Rips complex of GP(18,3).
Python 3 standard library only.  No downloaded data or external software required.
"""
from collections import Counter, deque
from itertools import combinations

N = 18
V = 2*N


def graph():
    E = set()
    for i in range(N):
        for a,b in ((i,(i+1)%N),(i,N+i),(N+i,N+(i+3)%N)):
            E.add(tuple(sorted((a,b))))
    A = [set() for _ in range(V)]
    for u,v in E:
        A[u].add(v); A[v].add(u)
    assert len(E)==54 and all(len(a)==3 for a in A)
    return A,E


def distances(A):
    ds = []
    for s in range(V):
        d = {s:0}; q=deque([s])
        while q:
            u=q.popleft()
            for w in sorted(A[u]):
                if w not in d:
                    d[w]=d[u]+1; q.append(w)
        assert len(d)==V
        ds.append([d[i] for i in range(V)])
    return ds


def cliques(square):
    faces=set()
    def visit(base, candidates):
        for j,x in enumerate(candidates):
            f=base+(x,); faces.add(f)
            visit(f,[y for y in candidates[j+1:] if y in square[x]])
    visit((), list(range(V)))
    return faces


def all_hexagons(A):
    found=set()
    def canonical(x):
        y=list(x)
        return min(tuple(z[i:]+z[:i]) for z in (y,y[::-1]) for i in range(6))
    def explore(path):
        if len(path)==6:
            if path[0] in A[path[-1]]:found.add(canonical(path))
            return
        for w in A[path[-1]]:
            if w not in path and (len(path)<5 or w!=path[0]):explore(path+[w])
    for s in range(V):explore([s])
    return found


def boundary_rank(faces,dimension,prime):
    high=sorted(f for f in faces if len(f)==dimension+1)
    low=sorted(f for f in faces if len(f)==dimension)
    idx={f:i for i,f in enumerate(low)}
    pivots={}
    for sigma in high:
        c={}
        for j in range(len(sigma)):
            k=idx[sigma[:j]+sigma[j+1:]]
            c[k]=(-1 if j%2 else 1)%prime
        while c:
            p=max(c)
            if p not in pivots:
                inv=pow(c[p],-1,prime)
                pivots[p]={r:(v*inv)%prime for r,v in c.items()}
                break
            pivot=pivots[p]
            mul=c[p]
            for r,v in pivot.items():
                u=(c.get(r,0)-mul*v)%prime
                if u:c[r]=u
                elif r in c:del c[r]
    return len(pivots)


def freedelete(F,small,big):
    assert small in F and big in F and len(big)==len(small)+1
    assert set(small)<set(big)
    # A free face has exactly one coface of any dimension, namely its maximal partner.
    supers=[f for f in F if set(small)<set(f)]
    assert supers==[big], (small,big,supers)
    F.remove(small);F.remove(big)


def freereduce(word):
    stack=[]
    for z in word:
        if stack and stack[-1]==-z:stack.pop()
        else:stack.append(z)
    while len(stack)>1 and stack[0]==-stack[-1]:stack=stack[1:-1]
    return tuple(stack)


def tietze_2cells(F, square):
    edges=sorted(f for f in F if len(f)==2)
    A=[set() for _ in range(V)]
    for u,v in edges:A[u].add(v);A[v].add(u)
    parent={0:None}; q=deque([0]); tree=set()
    while q:
        u=q.popleft()
        for v in sorted(A[u]):
            if v not in parent:
                parent[v]=u;tree.add(tuple(sorted((u,v))));q.append(v)
    assert len(parent)==V and len(tree)==V-1
    gens={e:k+1 for k,e in enumerate(e for e in edges if e not in tree)}
    assert len(gens)==127
    rel=[]
    for a,b,c in sorted(f for f in F if len(f)==3):
        word=[]
        for u,v in ((a,b),(b,c),(c,a)):
            e=tuple(sorted((u,v)))
            if e in gens:word.append(gens[e] if u<v else -gens[e])
        rel.append(freereduce(word))
    assert len(rel)==150
    initial_lens=Counter(len(r) for r in rel)
    remaining=set(gens.values()); steps=[];maxlen=max(map(len,rel))
    while remaining:
        eligible=[]
        for j,r in enumerate(rel):
            count=Counter(abs(a) for a in r)
            for a in r:
                if count[abs(a)]==1:
                    eligible.append((len(r),j,abs(a)));break
        assert eligible, ('stalled',len(remaining),len(rel))
        _,j,x=min(eligible)
        r=rel[j]; k=next(k for k,a in enumerate(r) if abs(a)==x)
        a=r[k]; tail=r[k+1:]+r[:k]
        sol=freereduce(tuple(-z for z in tail[::-1])) if a>0 else tail
        inv=tuple(-z for z in sol[::-1])
        del rel[j]
        rel=[freereduce(z for t in r for z in (sol if t==x else inv if t==-x else (t,))) for r in rel]
        remaining.remove(x);steps.append([j,x]);maxlen=max(maxlen,max(map(len,rel),default=0))
    assert len(steps)==127 and len(rel)==23 and all(not r for r in rel)
    return {'tree_edges':35,'generators_eliminated':127,'initial_relators':150,
            'remaining_trivial_relators':23,'max_relator_length':maxlen,
            'initial_relator_lengths':dict(sorted(initial_lens.items())),
            'trace':steps}


def main():
    A,E=graph();d=distances(A)
    square=[set(v for v in range(V) if v!=u and d[u][v]<=2) for u in range(V)]
    F=cliques(square)
    f=Counter(len(x) for x in F)
    assert f==Counter({1:36,2:162,3:186,4:36}), f
    # Every pair at distance two has exactly one original midpoint.
    distance2=[(u,v) for u in range(V) for v in range(u+1,V) if d[u][v]==2]
    assert len(distance2)==108
    assert all(len(A[u]&A[v])==1 for u,v in distance2)
    tet={tuple(sorted({v}|A[v])) for v in range(V)}
    assert len(tet)==36 and tet=={x for x in F if len(x)==4}
    # The 21 graph hexagons are precisely 18 outer/spoke/inner hexagons and three inner rings.
    expected=[]
    for i in range(N):
        expected.append([i,(i+1)%N,(i+2)%N,(i+3)%N,N+(i+3)%N,N+i])
    for j in range(3):expected.append([N+(j+3*t)%N for t in range(6)])
    def canon(c):return min(tuple(z[i:]+z[:i]) for z in (list(c),list(c)[::-1]) for i in range(6))
    assert {canon(c) for c in expected}==all_hexagons(A)
    exceptional=set()
    for c in expected:
        for t in (c[0::2],c[1::2]):
            tri=tuple(sorted(t))
            assert tri in F
            exceptional.add(tri)
            assert all(not set(tri)<set(tet4) for tet4 in tet)
    assert len(exceptional)==42
    centered=set(t for four in tet for t in combinations(four,3))
    assert len(centered)==144 and centered.isdisjoint(exceptional)
    assert centered|exceptional=={x for x in F if len(x)==3}
    # Check that the centered part B collapses exactly to original G.
    B=set(x for four in tet for q in range(1,5) for x in combinations(four,q))
    assert all((u,) in B for u in range(V))
    for center in range(V):
        small=tuple(sorted(A[center]));big=tuple(sorted({center}|A[center]))
        freedelete(B,small,big)
    for center in range(V):
        for u,v in combinations(sorted(A[center]),2):
            freedelete(B,(u,v),tuple(sorted((center,u,v))))
    graphfaces={(u,) for u in range(V)}|set(E)
    assert B==graphfaces
    assert 36+108==144
    # In G, every outer-disk attaching hexagon has a unique inner edge.
    inner={(min(N+i,N+(i+3)%N),max(N+i,N+(i+3)%N)) for i in range(N)}
    assert len(inner)==18
    for i,c in enumerate(expected[:N]):
        assert set(tuple(sorted((c[j],c[(j+1)%6]))) for j in range(6))&inner=={
            tuple(sorted((N+i,N+(i+3)%N)))}
    # Replacing inner-ring edges via outer paths gives each of three rings degree one.
    for j in range(3):
        used=[(j+3*t+s)%N for t in range(6) for s in range(3)]
        assert sorted(used)==list(range(N))
    # Independent full-complex signed boundary ranks in two coefficient fields.
    for prime in (2,3,5):
        ranks=[boundary_rank(F,k,prime) for k in (1,2,3)]
        assert ranks==[35,127,36],(prime,ranks)
    # A second route to the exact homotopy type uses integral two-cell elimination.
    F2=set(F)
    for v in range(V):freedelete(F2,tuple(sorted(A[v])),tuple(sorted({v}|A[v])))
    assert Counter(len(x) for x in F2)==Counter({1:36,2:162,3:150})
    trace=tietze_2cells(F2,square)
    print('graph vertices=36 original_edges=54 original_cycle_rank=19')
    print('rips_faces=[36,162,186,36] exceptional_hexagons=21 (outer=18, inner=3)')
    print('centered_collapse_pairs=144 remainder_original_graph=yes')
    print('tietze_collapse_of_3cells=36; generator_eliminations=127; surviving_trivial_2cells=23')
    print('tietze_max_word_length=%s; initial_relator_lengths=%s'%(trace['max_relator_length'],trace['initial_relator_lengths']))
    print('signed_boundary_ranks_mod_2_3_5=[35,127,36]')
    print('homotopy_type=wedge_of_23_2spheres (by paired-hexagon CW proof)')
    print('PASS')
    return trace


if __name__=='__main__':
    main()
