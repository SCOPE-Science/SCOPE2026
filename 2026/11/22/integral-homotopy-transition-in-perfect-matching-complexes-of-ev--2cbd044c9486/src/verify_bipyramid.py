#!/usr/bin/env python3
"""Exact finite certificate checker for perfect-matching complexes of even bipyramids.
Uses only the Python standard library. Run from the package root.
"""
import json
from itertools import combinations
from collections import Counter
from pathlib import Path

CERT=Path(__file__).resolve().parent.parent/'certificates'/'bipyramid-collapse.json'

def graph_edges(m):
    n=2*m
    return [(j,(j+1)%n) for j in range(n)]+[(n,j) for j in range(n)]+[(n+1,j) for j in range(n)]

def recursive_matchings(m):
    n=2*m; E=graph_edges(m)
    incident={v:[] for v in range(n+2)}
    for i,(a,b) in enumerate(E): incident[a].append((i,b));incident[b].append((i,a))
    def rec(rem, chosen):
        if not rem:
            yield tuple(sorted(chosen));return
        a=min(rem)
        for i,b in incident[a]:
            if b in rem:
                yield from rec(rem-{a,b},chosen+[i])
    return set(rec(set(range(n+2)),[]))

def formula_matchings(m):
    n=2*m
    ans=set()
    for a in range(n):
      for b in range(n):
        if (b-a)%2!=1: continue
        remain=set(range(n))-{a,b}; picked=[n+a,2*n+b]
        def rec(rem):
            if not rem:return ()
            v=min(rem)
            for w in ((v+1)%n,(v-1)%n):
                if w in rem:
                    z=rec(rem-{v,w})
                    if z is not None:
                        return (v if w==(v+1)%n else w,)+z
            return None
        rim=rec(remain)
        assert rim is not None
        picked.extend(rim)
        ans.add(tuple(sorted(picked)))
    return ans

def faces(facets):
    allf=set()
    for f in facets:
        for k in range(1,len(f)+1):allf.update(combinations(f,k))
    return allf

def immediate_cofaces(face, allf):
    k=len(face)+1; f=set(face)
    return [z for z in allf if len(z)==k and f.issubset(z)]

def replay_collapses(facets, pairs, final_faces):
    allf=faces(facets); original=Counter(map(len,allf))
    for index,(lo,hi) in enumerate(pairs):
        lo,hi=tuple(lo),tuple(hi)
        assert lo in allf and hi in allf, ('absent',index)
        assert len(hi)==len(lo)+1 and set(lo).issubset(hi), ('pair',index)
        assert immediate_cofaces(lo,allf)==[hi], ('not free',index)
        allf.remove(lo);allf.remove(hi)
    assert allf=={tuple(z) for z in final_faces}, 'core mismatch'
    # Remaining faces automatically form a subcomplex, but check explicitly.
    for z in allf:
        for i in range(len(z)):
            if len(z)>1:assert z[:i]+z[i+1:] in allf
    return allf, dict(sorted(original.items()))

def triangle_closure(core, tree, steps):
    verts={v for z in core if len(z)==1 for v in z}
    edges={z for z in core if len(z)==2}
    triangles={z for z in core if len(z)==3}
    par={v:v for v in verts}
    def root(v):
        while v!=par[v]:v=par[v]
        return v
    known=set()
    for a,b in map(tuple,tree):
        assert (a,b) in edges and root(a)!=root(b)
        par[root(a)]=root(b);known.add((a,b))
    assert len(known)==len(verts)-1
    for edge,triangle in steps:
        edge,triangle=tuple(edge),tuple(triangle)
        assert triangle in triangles and edge in edges and edge not in known
        sides=set(combinations(triangle,2))
        assert edge in sides and len((sides-{edge})&known)==2
        known.add(edge)
    assert known==edges, 'nontrivial edge generator remains'
    return len(tree),len(steps)

def boundary3(core):
    tris=sorted(z for z in core if len(z)==3)
    tets=sorted(z for z in core if len(z)==4)
    ix={x:i for i,x in enumerate(tris)}
    A=[[0]*len(tets) for t in tris]
    for j,t in enumerate(tets):
        for i in range(4):A[ix[t[:i]+t[i+1:]]][j]=(-1)**i
    return A

def bareiss_det(mat):
    a=[row[:] for row in mat];n=len(a);prev=1;sign=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1] if n else 1

def smith_witness(A, data):
    rows=data['minor_rows'];cols=data['minor_cols']
    assert len(A)==26 and len(A[0])==10
    assert len(rows)==len(cols)==8 and len(set(rows))==len(set(cols))==8
    determinant=bareiss_det([[A[i][j] for j in cols] for i in rows])
    assert abs(determinant)==1, determinant
    N=data['kernel_vectors'];assert len(N)==2
    for v in N:
        assert len(v)==10 and any(v)
        assert all(sum(x*y for x,y in zip(row,v))==0 for row in A)
    assert N[0]!=N[1] and any(N[0][i]*N[1][j]!=N[1][i]*N[0][j] for i in range(10) for j in range(10))
    return determinant

def main():
    data=json.loads(CERT.read_text(encoding='utf-8'))
    assert data['purpose']=='exact simplicial collapse and integral boundary certificate'
    for ms in ('3','4','5'):
        m=int(ms);d=data['cases'][ms]
        F=formula_matchings(m);F2=recursive_matchings(m)
        assert F==F2 and len(F)==2*m*m
        core,original=replay_collapses(F,d['collapse_pairs'],d['remaining_faces'])
        assert original=={int(k):v for k,v in d['original_face_counts'].items()}
        assert dict(Counter(map(len,core)))=={int(k):v for k,v in d['remaining_face_counts'].items()}
        if m>=4:
            t,s=triangle_closure(core,d['spanning_tree'],d['triangle_steps'])
            assert s==len([x for x in core if len(x)==2])-t
        else:
            assert not any(len(z)>=3 for z in core)
            verts={z[0] for z in core if len(z)==1}
            edges={z for z in core if len(z)==2}
            seen={min(verts)}
            while True:
                more={v for e in edges for v in e if any(w in seen for w in e)}
                if more<=seen:break
                seen.update(more)
            assert seen==verts, 'core graph not connected'
        if m==5:assert smith_witness(boundary3(core),d['integral_boundary'])==-1
        print(f'm={m}: matching_count={len(F)}, initial_faces={sum(original.values())}, collapses={len(d["collapse_pairs"])}, final_f={dict(Counter(map(len,core)))}, OK')
    print('ALL CERTIFICATES VERIFIED; independent mathematical review not implied')
if __name__=='__main__':main()
