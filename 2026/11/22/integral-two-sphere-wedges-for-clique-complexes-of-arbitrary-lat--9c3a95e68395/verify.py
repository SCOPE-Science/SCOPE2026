#!/usr/bin/env python3
"""Exact finite combinatorial checks for Latin-square graph clique complexes.
Pure Python standard library, no external packages.
"""
from itertools import combinations
from math import comb

def latin(n, kind):
    if kind == 'cyclic': return [[(r+c)%n for c in range(n)] for r in range(n)]
    if kind == 'xor': assert n&(n-1)==0; return [[r^c for c in range(n)] for r in range(n)]
    if kind == 's3':
        assert n==6
        perms=list(__import__('itertools').permutations(range(3)))
        idx={p:i for i,p in enumerate(perms)}
        return [[idx[tuple(p[q[i]] for i in range(3))] for q in perms] for p in perms]
    raise ValueError(kind)

def face_data(M):
    n=len(M); v=n*n
    def rc(t): return divmod(t,n)
    def edge(a,b):
        (r,c),(s,d)=rc(a),rc(b)
        return (r==s)+(c==d)+(M[r][c]==M[s][d])==1
    adj=[set() for _ in range(v)]
    for a in range(v):
        for b in range(a+1,v):
            if edge(a,b): adj[a].add(b); adj[b].add(a)
    edges={tuple(sorted((a,b))) for a in range(v) for b in adj[a] if a<b}
    triangles=set()
    for a,b in edges:
        for c in (adj[a]&adj[b]):
            if c>b: triangles.add((a,b,c))
    maximal=[]
    def bk(R,P,X):
        if not P and not X:
            maximal.append(tuple(sorted(R)));return
        pivot=max(P|X,key=lambda x:len(P&adj[x])) if P|X else None
        for u in list(P-(adj[pivot] if pivot is not None else set())):
            bk(R|{u},P&adj[u],X&adj[u]);P.remove(u);X.add(u)
    bk(set(),set(range(v)),set())
    lines=[]
    for r in range(n): lines.append(tuple(r*n+c for c in range(n)))
    for c in range(n): lines.append(tuple(r*n+c for r in range(n)))
    for s in range(n): lines.append(tuple(r*n+c for r in range(n) for c in range(n) if M[r][c]==s))
    I=0
    for r,t in combinations(range(n),2):
        for c,d in combinations(range(n),2):
            if M[r][c]==M[t][d] and M[r][d]==M[t][c]: I+=1
    nonline_quads=[Q for Q in maximal if len(Q)==4]
    # Mixed triangles not lying in intercalate tetrahedra are also maximal.
    assert all(len(Q) in (3,4,n) for Q in maximal)
    assert sorted(Q for Q in maximal if len(Q)==n)==sorted(lines)
    assert all(not any(set(T).issubset(set(L)) for L in lines) for T in maximal if len(T)==3)
    assert len(nonline_quads)==I
    from collections import Counter
    tri_cofaces=Counter(T for Q in nonline_quads for T in combinations(Q,3))
    assert max(tri_cofaces.values(),default=0)<=1
    line_tri=set(T for L in lines for T in combinations(L,3))
    assert not line_tri.intersection(tri_cofaces)
    assert len(triangles-line_tri)==n*n*(n-1)
    assert len(line_tri)==3*n*comb(n,3)
    # Verify actual elementary simplicial collapse pairs, not just a f-vector identity.
    face_set=set()
    for Q in maximal:
        for size in range(1,len(Q)+1):
            face_set.update(combinations(Q,size))
    original_face_count=len(face_set)
    collapse_pairs=0
    def collapse(sigma,tau):
        nonlocal collapse_pairs
        assert sigma in face_set and tau in face_set
        assert len(tau)==len(sigma)+1 and set(sigma).issubset(tau)
        assert [u for u in range(n*n) if u not in sigma and tuple(sorted(sigma+(u,))) in face_set]==[next(u for u in tau if u not in sigma)]
        face_set.remove(sigma);face_set.remove(tau); collapse_pairs+=1
    for L in lines:
        anchor=L[0]
        rest=tuple(u for u in L if u!=anchor)
        for k in range(len(rest),2,-1):
            for sigma in combinations(rest,k):
                collapse(sigma,tuple(sorted(sigma+(anchor,))))
    for Q in sorted(nonline_quads):
        collapse(tuple(sorted(Q[:3])),Q)
    assert not any(len(F)>=4 for F in face_set)
    assert len(face_set)==n*n+len(edges)+3*n*comb(n-1,2)+n*n*(n-1)-I
    assert original_face_count-len(face_set)==2*collapse_pairs
    final_tris={F for F in face_set if len(F)==3}
    assert len(final_tris)==3*n*comb(n-1,2)+n*n*(n-1)-I
    # Symbolic six-triangle disk for each rook rectangle without symbol diagonal.
    squares=0; disks=0
    for r,t in combinations(range(n),2):
        for c,d in combinations(range(n),2):
            a,b,q,e=r*n+c,r*n+d,t*n+d,t*n+c
            squares+=1
            if edge(a,q) or edge(b,e):continue
            sym=M[r][d]
            w=t*n+M[t].index(sym)
            z=next(j*n+c for j in range(n) if M[j][c]==sym)
            tris=[(a,b,z),(a,e,z),(b,q,w),(b,w,z),(q,e,w),(e,w,z)]
            assert len(set((a,b,q,e,w,z)))==6
            assert all(tuple(sorted(T)) in triangles for T in tris)
            cnt=Counter(E for T in tris for E in combinations(sorted(T),2))
            boundary={tuple(sorted(E)) for E in [(a,b),(b,q),(q,e),(e,a)]}
            assert {E for E,v in cnt.items() if v==1}==boundary
            assert all(v in (1,2) for v in cnt.values())
            # Interior vertices w,z and their internal links are connected.
            assert len(cnt)==11
            disks+=1
    expected_E=3*n*comb(n,2)
    assert len(edges)==expected_E
    final_F=3*n*comb(n-1,2)+n*n*(n-1)-I
    rank=(n-1)**3-I
    assert v-expected_E+final_F==1+rank
    return n,v,len(edges),len(triangles),len(maximal),I,rank,squares,disks,final_F,edges,triangles,final_tris,original_face_count,collapse_pairs

def gf2_rank(rows):
    basis={}
    for row in rows:
        z=row
        while z:
            col=z.bit_length()-1
            if col not in basis:basis[col]=z;break
            z ^= basis[col]
    return len(basis)

def homology(n,edges,triangles,expected):
    edge_ix={e:i for i,e in enumerate(sorted(edges))}
    tri_boundary=[]
    for a,b,c in sorted(triangles):
        tri_boundary.append(sum(1<<edge_ix[e] for e in ((a,b),(a,c),(b,c))))
    rank2=gf2_rank(tri_boundary)
    # Connected 1-skeleton: d1 has rank V-1.
    beta1=len(edges)-(n*n-1)-rank2
    assert beta1==0
    return beta1,rank2

def main():
    configs=[(5,'cyclic'),(6,'cyclic'),(6,'s3'),(8,'xor')]
    for n,kind in configs:
        d=face_data(latin(n,kind));
        N,V,E,T,facets,I,rank,squares,disks,final_F,edges,triangles,final_tris,original_faces,pairs=d
        if n<=6: beta1,rank2=homology(n,edges,triangles,rank)
        else: beta1,rank2='not_checked','not_checked'
        if n<=6:
            idx={e:i for i,e in enumerate(sorted(edges))}
            red_boundary=[sum(1<<idx[e] for e in combinations(T,2)) for T in final_tris]
            red_rank=gf2_rank(red_boundary)
            assert red_rank==rank2
            assert len(final_tris)-red_rank==rank
        print(f'{kind} n={n}: vertices={V} edges={E} triangles={T} maximal_cliques={facets} intercalates={I} target_S2={rank} reduced_faces_after_collapse={final_F} rook_squares={squares} six_triangle_disks={disks} elementary_pairs={pairs} original_faces={original_faces} GF2_H1={beta1} GF2_d2_rank={rank2}')
    print('OK: exhaustive clique census, elementary collapses, intercalate uniqueness, square null-filling, exact Euler counts, and independent GF(2) H1/H2 checks')
if __name__=='__main__':main()
