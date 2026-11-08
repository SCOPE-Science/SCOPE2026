#!/usr/bin/env python3
"""Finite sanity tests for triangle-edge augmentation and clique-free complexes.
Scientific definitions and self-contained checks; no external dependencies.
"""
from itertools import combinations

def examples():
    return [
        ('edge', 2, [(0,1)]),
        ('path4',4,[(0,1),(1,2),(2,3)]),
        ('cycle4',4,[(0,1),(1,2),(2,3),(3,0)]),
        ('cycle5',5,[(i,(i+1)%5) for i in range(5)]),
        ('two_disjoint_edges',4,[(0,1),(2,3)]),
        ('star5',5,[(0,i) for i in range(1,5)]),
        ('complete_bipartite_2_3',5,[(a,b) for a in range(2) for b in range(2,5)]),
        ('triangle',3,[(0,1),(1,2),(0,2)]),
        ('triangle_with_leaf',4,[(0,1),(1,2),(0,2),(2,3)]),
        ('complete4',4,list(combinations(range(4),2))),
    ]

def rank_mod2(cols):
    pivots={}
    for v in cols:
        while v:
            p=v.bit_length()-1
            if p not in pivots:
                pivots[p]=v
                break
            v^=pivots[p]
    return len(pivots)

def sign_of_list(xs):
    inv=sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))
    return -1 if inv%2 else 1

def test_symmetry(name,n,edlist,simplices,triangle_count):
    autos={
       'edge':[(1,0)],
       'path4':[(3,2,1,0)],
       'cycle4':[(1,2,3,0),(0,3,2,1)],
       'cycle5':[(1,2,3,4,0),(0,4,3,2,1)],
       'two_disjoint_edges':[(2,3,0,1),(1,0,2,3)],
       'star5':[(0,2,1,3,4)],
       'complete_bipartite_2_3':[(1,0,2,3,4),(0,1,3,4,2)],
       'triangle':[(1,0,2)],
       'triangle_with_leaf':[(1,0,2,3)],
       'complete4':[(1,0,2,3)]
    }
    for g in autos[name]:
       assert set(g)==set(range(n))
       emap={e:i for i,e in enumerate(edlist)}
       perm=list(g)+[n+emap[tuple(sorted((g[a],g[b])))] for a,b in edlist]
       reduced_L=-1
       for k,faces in enumerate(simplices):
           for face in faces:
               vs=[i for i in range(len(perm)) if face>>i&1]
               img=[perm[i] for i in vs]
               if sum(1<<i for i in img)==face:
                   reduced_L+=(-1)**k*sign_of_list(img)
       expected=0 if triangle_count else (-1)**(n-1)*sign_of_list(g)
       assert reduced_L==expected,(name,g,reduced_L,expected)
    return len(autos[name])

def run(name,n,edges):
    edges={tuple(sorted(e)) for e in edges}
    m=len(edges); N=n+m
    assert len({x for e in edges for x in e})==n
    edlist=sorted(edges)
    graph_edges=set(edges)
    for j,(a,b) in enumerate(edlist):
        graph_edges.update((tuple(sorted((a,n+j))),tuple(sorted((b,n+j)))))
    all_triangles={frozenset(t) for t in combinations(range(N),3) if all(tuple(sorted(e)) in graph_edges for e in combinations(t,2))}
    expected={frozenset((a,b,n+j)) for j,(a,b) in enumerate(edlist)}
    original_triangles={frozenset(t) for t in combinations(range(n),3) if all(tuple(sorted(e)) in edges for e in combinations(t,2))}
    assert all_triangles==expected|original_triangles
    forb=[sum(1<<i for i in t) for t in all_triangles]
    simplices=[[] for i in range(N)]
    for mask in range(1,1<<N):
        if all((mask & t)!=t for t in forb):
            simplices[mask.bit_count()-1].append(mask)
    ranks=[]
    for k in range(1,N):
        down={s:j for j,s in enumerate(simplices[k-1])}
        cols=[]
        for s in simplices[k]:
            x=0
            for v in range(N):
                if s>>v&1:
                    x ^= 1<<down[s^(1<<v)]
            cols.append(x)
        ranks.append(rank_mod2(cols))
    rank=[0]+ranks+[0]
    bettis=[len(simplices[k])-rank[k]-rank[k+1] for k in range(N)]
    assert sum(((-1)**k)*len(simplices[k]) for k in range(N))==sum(((-1)**k)*bettis[k] for k in range(N))
    assert sum(bettis) > 0
    if not original_triangles:
        expected_b={0:1,n-1:1}
    else:
        expected_b={0:1}
    for k in range(N):
        assert bettis[k] == expected_b.get(k,0),(name,k,bettis[k],expected_b)
    # Prove at the level of the two-skeleton that every missing triangle boundary is nullhomotopic,
    # except the single-edge base case where the complex is the 3-cycle.
    if m>=2:
        for T in all_triangles:
            # Search for an apex z with all three cone triangles allowed.
            possible=[z for z in range(N) if z not in T and all(frozenset((*pair,z)) not in all_triangles for pair in combinations(T,2))]
            # Every triangle with a private w_e has an alternate private w_f apex.
            if any(w>=n for w in T):
                assert possible, (name,'private-cone',T)
            # A triangle of original vertices might require two-stage replacement;
            # it reduces to an edge triangle by coning at the private vertex of one of its edges.
            else:
                a,b,c=sorted(T)
                j=edlist.index((a,b))
                w=n+j
                assert frozenset((a,c,w)) not in all_triangles
                assert frozenset((b,c,w)) not in all_triangles
                # The third cone triangle abw is itself a private-edge forbidden face,
                # whose loop has already been filled via another private apex.
    symmetry_checks=test_symmetry(name,n,edlist,simplices,len(original_triangles))
    print(f'{name:24} base_vertices={n:2} original_triangles={len(original_triangles):2} total_faces={sum(map(len,simplices)):6} face_vector={[len(x) for x in simplices if x]} reduced_betti={{'+','.join(f'{k}:{v}' for k,v in enumerate(bettis) if k>0 and v)+'}'+f' character_checks={symmetry_checks}')

if __name__=='__main__':
    for case in examples(): run(*case)
    print('ALL_VERIFY_OK')
