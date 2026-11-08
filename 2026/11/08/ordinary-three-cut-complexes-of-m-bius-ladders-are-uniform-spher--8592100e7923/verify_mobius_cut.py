#!/usr/bin/env python3
"""Standalone exact checks for ordinary three-cut complexes of Mobius ladders.

Only Python's standard library is required. For each n, X is the simplicial
Alexander dual of the ordinary three-cut complex of M_(2n).
"""
from collections import Counter, deque
from itertools import combinations


def adj(n, a, b):
    difference = (a-b) % (2*n)
    return difference in (1, 2*n-1, n)


def connected_triple(n, t):
    a,b,c=t
    return int(adj(n,a,b))+int(adj(n,a,c))+int(adj(n,b,c)) >= 2


def dual_faces(n):
    vertices=range(2*n)
    f={0:{frozenset()}, 1:{frozenset((v,)) for v in vertices},
       2:{frozenset(e) for e in combinations(vertices,2)}}
    f[3]={frozenset(t) for t in combinations(vertices,3) if connected_triple(n,t)}
    f[4]={frozenset(s) for s in combinations(vertices,4)
          if all(frozenset(t) in f[3] for t in combinations(s,3))}
    return f


def max_missing_degree_at_most_one(n, vertices):
    for v in vertices:
        if sum(not adj(n,v,w) for w in vertices if w!=v)>1:
            return False
    return True


def member_by_connected_triples(n, vertices):
    return all(connected_triple(n,t) for t in combinations(vertices,3))


def free_pair(faces, lower, upper):
    p=len(lower)
    assert len(upper)==p+1 and lower<upper
    assert lower in faces[p] and upper in faces[p+1]
    assert sum(lower <= s for s in faces[p+1]) == 1, (lower,upper, 'not free')
    for k in range(p+2,5):
        assert not any(lower <= s for s in faces[k]), (lower,upper, 'higher coface')
    faces[p].remove(lower)
    faces[p+1].remove(upper)


def prescribed_collapse(n):
    faces=dual_faces(n)
    before=tuple(len(faces[s]) for s in range(5))
    assert before==(1,2*n,n*(2*n-1),6*n,n)
    # Each straight rim path has a private distance-two endpoint pair.
    for i in range(2*n):
        free_pair(faces,
                  frozenset(((i-1)%(2*n),(i+1)%(2*n))),
                  frozenset(((i-1)%(2*n),i,(i+1)%(2*n))))
    # Each square has precisely four connected triple faces; they are
    # removed in four elementary collapses, with private rim and diagonals.
    # Stage 1 removes all tetrahedra, so later edge-face freeness is literal.
    for i in range(n):
        a=i; b=(i+1)%(2*n); c=(i+n)%(2*n); d=(i+n+1)%(2*n)
        free_pair(faces,frozenset((a,b,c)),frozenset((a,b,c,d)))
    for i in range(n):
        a=i; b=(i+1)%(2*n); d=(i+n+1)%(2*n)
        free_pair(faces,frozenset((a,b)),frozenset((a,b,d)))
    for i in range(n):
        a=i; c=(i+n)%(2*n); d=(i+n+1)%(2*n)
        free_pair(faces,frozenset((a,d)),frozenset((a,c,d)))
    for i in range(n):
        b=(i+1)%(2*n); c=(i+n)%(2*n); d=(i+n+1)%(2*n)
        free_pair(faces,frozenset((b,c)),frozenset((b,c,d)))
    after=tuple(len(faces[s]) for s in range(5))
    assert after==(1,2*n,2*n*(n-3),0,0)
    graph={v:set() for v in range(2*n)}
    for edge in faces[2]:
        a,b=tuple(edge);graph[a].add(b);graph[b].add(a)
    visited={0};todo=deque([0])
    while todo:
        v=todo.popleft()
        for w in graph[v]-visited:
            visited.add(w);todo.append(w)
    assert len(visited)==2*n
    rank=len(faces[2])-len(faces[1])+1
    assert rank==2*n*(n-4)+1
    return before,after,rank


def exact_dual_test(n):
    N=2*n; size_mask=(1<<N)-1
    faces=dual_faces(n)
    missing3=[]
    for t in combinations(range(N),3):
        if not connected_triple(n,t):
            missing3.append(sum(1<<v for v in t))
    # Independent direct ordinary cut facet calculation.
    facets=[size_mask ^ dis for dis in missing3]
    delta_faces_by_size=[[] for _ in range(N+1)]
    for tau in range(1<<N):
        vertices=tuple(v for v in range(N) if tau>>v&1)
        rule1=member_by_connected_triples(n,vertices)
        rule2=max_missing_degree_at_most_one(n,vertices)
        rule3=(frozenset(vertices) in faces[len(vertices)]) if len(vertices)<=4 else False
        sigma=size_mask ^ tau
        cut_membership=any(sigma & ~facet==0 for facet in facets)
        assert rule1==rule2==rule3==(not cut_membership), (n,tau,rule1,rule2,rule3,cut_membership)
        if cut_membership:
            delta_faces_by_size[sigma.bit_count()].append(sigma)
    reduced_euler=sum((-1)**(k-1)*len(fs) for k,fs in enumerate(delta_faces_by_size))
    rank=2*n*(n-4)+1
    assert reduced_euler==rank
    assert len(delta_faces_by_size[N-2])==0
    assert len(delta_faces_by_size[N-3])==len(facets)
    return [len(fs) for fs in delta_faces_by_size],reduced_euler


def rank_mod_two(columns, row_faces):
    mapping={v:i for i,v in enumerate(row_faces)}
    basis={}
    for mask in columns:
        v=0
        for x in range(mask.bit_length()):
            if mask>>x & 1:
                v ^= 1<<mapping[mask ^ (1<<x)]
        while v:
            idx=v.bit_length()-1
            if idx in basis: v ^= basis[idx]
            else: basis[idx]=v;break
    return len(basis)


def integral_complex_homology_mod_two(n):
    N=2*n
    f,_=exact_dual_test(n)
    full=(1<<N)-1
    bad=[]
    for t in combinations(range(N),3):
        if not connected_triple(n,t):bad.append(sum(1<<j for j in t))
    fac=[full^t for t in bad]
    faces=[[] for _ in range(N+1)]
    for s in range(1<<N):
        if any(s & ~F==0 for F in fac):
            faces[s.bit_count()].append(s)
    assert [len(x) for x in faces]==f
    rank={1:1}
    for k in range(2,N+1):
        if not faces[k]:break
        rank[k]=rank_mod_two(faces[k],faces[k-1])
    betti={k-1:len(faces[k])-rank.get(k,0)-rank.get(k+1,0)
           for k in range(1,N+1) if faces[k]}
    betti={k:v for k,v in betti.items() if v!=0}
    assert betti=={N-4:2*n*(n-4)+1}, (n,betti)
    return betti


def main():
    for n in range(4,14):
        before,after,rank=prescribed_collapse(n)
        print('n=%d: dual faces=%s -> graph=%s, rank=%d [PASS]' %(n,before,after,rank))
    for n in range(4,8):
        fv,euler=exact_dual_test(n)
        print('n=%d: complete 2^(2n) membership comparisons PASS; cut f-vector=%s; reduced Euler=%d [PASS]' %(n,fv,euler))
    for n in (4,5,6):
        homology=integral_complex_homology_mod_two(n)
        print('n=%d: independent mod-2 cut boundary homology=%s [PASS]' %(n,homology))
    print('ALL CHECKS PASSED')

if __name__=='__main__':main()
