#!/usr/bin/env python3
"""Exact integral Morse-chain computation for staircase rook complexes.

No external packages are required. Run: python3 stirling9_verify.py
The reduced complex includes the empty simplex as a (-1)-cell.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from hashlib import sha256


def stirling(n):
    squares = [(i,j) for i in range(n) for j in range(i,n)]
    rows = [[(v,j) for v,(i,j) in enumerate(squares) if i==r]
            for r in range(n)]
    faces = {}
    def visit(r, used_cols, mask, size):
        if r==n:
            if mask in faces: raise AssertionError('duplicate face')
            faces[mask]=size
            return
        visit(r+1, used_cols, mask, size)
        for v,j in rows[r]:
            if not ((used_cols >> j)&1):
                visit(r+1, used_cols | (1<<j), mask | (1<<v), size+1)
    visit(0,0,0,0)
    return squares,faces


def triangle_number(n,k):
    # Stirling number S(n,k) by recurrence.
    T=[0]*(k+1);T[0]=1
    for j in range(1,n+1):
        old=T[:];T[0]=0
        for a in range(1,k+1):T[a]=old[a-1]+a*old[a]
    return T[k]


def construct_matching(squares, faces):
    remaining=set(faces);up={};down={}
    for v in range(len(squares)):
        for f in tuple(remaining):
            if f & (1<<v):continue
            g=f|(1<<v)
            if g in remaining:
                remaining.remove(f);remaining.remove(g)
                up[f]=g;down[g]=f
    return remaining,up,down


def test_acyclic(faces,up):
    # Orient all unmatched Hasse edges downward and matched edges upward.
    nodes=list(faces);id_of={f:i for i,f in enumerate(nodes)}
    indeg=[0]*len(nodes);edges=[[] for _ in nodes]
    total=0
    for high in nodes:
        if high==0:continue
        x=high
        while x:
            v=x & -x;x-=v
            low=high^v
            if up.get(low)==high: a,b=low,high
            else: a,b=high,low
            ia,ib=id_of[a],id_of[b]
            edges[ia].append(ib);indeg[ib]+=1;total+=1
    queue=deque(i for i,d in enumerate(indeg) if d==0)
    visited=0
    while queue:
        a=queue.popleft();visited+=1
        for b in edges[a]:
            indeg[b]-=1
            if indeg[b]==0: queue.append(b)
    assert visited==len(nodes),('alternating cycle',visited,len(nodes))
    return total


def signed_boundary(simplex):
    x=simplex;s=1
    while x:
        v=x & -x;x-=v
        yield simplex^v,s
        s=-s


def morse_boundaries(critical,up,down,faces):
    @lru_cache(None)
    def project(f):
        if f in down:return {}
        if f not in up:return {f:1}
        g=up[f]
        ans=defaultdict(int)
        sign=0
        for h,c in signed_boundary(g):
            if h==f:sign=c
            else:
                for q,v in project(h).items():ans[q]+=c*v
        assert abs(sign)==1
        return {q:-sign*v for q,v in ans.items() if v}
    groups=defaultdict(list)
    for f in critical:groups[faces[f]].append(f)
    for a in groups.values():a.sort()
    matrices={}
    for d in sorted(groups):
        if d-1 not in groups:continue
        row_index={f:i for i,f in enumerate(groups[d-1])}
        columns=[]
        for g in groups[d]:
            c=defaultdict(int)
            for h,s in signed_boundary(g):
                for q,v in project(h).items():c[row_index[q]]+=s*v
            columns.append({i:v for i,v in c.items() if v})
        matrices[d]=(len(groups[d-1]),columns)
    return groups,matrices


def assert_chain(matrices):
    for d in matrices:
        if d-1 not in matrices:continue
        _,a=matrices[d-1];_,b=matrices[d]
        for col in b:
            prod=defaultdict(int)
            for k,z in col.items():
                for i,w in a[k].items():prod[i]+=z*w
            assert all(v==0 for v in prod.values()),('boundary squared',d)


def smith_all_units(nrow,columns):
    # Exact elementary operations: a unit pivot gives a unimodular direct sum
    # with [1]. Schur complement remains integral; no modular calculations.
    rs=[{} for _ in range(nrow)];cs=[dict(c) for c in columns]
    for j,c in enumerate(cs):
        for i,v in c.items():rs[i][j]=v
    active_rows=set(range(nrow));active_cols=set(range(len(cs)))
    rank=0;maximum=1
    while True:
        best=None
        for j in active_cols:
            for i,v in cs[j].items():
                if abs(v)!=1:continue
                cost=(len(cs[j])-1)*(len(rs[i])-1)
                if best is None or cost<best[0]:best=(cost,i,j)
                if cost==0:break
            if best is not None and best[0]==0:break
        if best is None:break
        _,i,j=best;sgn=cs[j][i]
        row=dict(rs[i]);col=dict(cs[j])
        for k in col:rs[k].pop(j)
        for k in row:cs[k].pop(i)
        rs[i].clear();cs[j].clear()
        active_rows.remove(i);active_cols.remove(j)
        for k,a in col.items():
            if k==i:continue
            for l,b in row.items():
                if l==j:continue
                val=rs[k].get(l,0)-sgn*a*b
                if val:
                    rs[k][l]=val;cs[l][k]=val
                    maximum=max(maximum,abs(val))
                elif l in rs[k]:
                    del rs[k][l];del cs[l][k]
        rank+=1
    leftover=sum(len(cs[j]) for j in active_cols)
    assert leftover==0,('unresolved nonunit Smith entries',leftover)
    return rank,maximum


def run(n):
    squares,faces=stirling(n)
    fvector=Counter(faces.values())
    assert all(fvector[k]==triangle_number(n+1,n+1-k)
               for k in range(n+1)),('Stirling face count',fvector)
    critical,up,down=construct_matching(squares,faces)
    assert len(critical)+2*len(up)==len(faces)
    incidence=test_acyclic(faces,up)
    groups,bounds=morse_boundaries(critical,up,down,faces)
    assert_chain(bounds)
    ranks={};maximum={}
    for d,(nrow,columns) in bounds.items():
        ranks[d],maximum[d]=smith_all_units(nrow,columns)
    betti={}
    for degree in groups:
        # Degree of a simplex with degree+1 rooks is topological degree.
        rank_higher=ranks.get(degree+1,0)
        rank_lower=ranks.get(degree,0)
        b=len(groups[degree])-rank_lower-rank_higher
        assert b>=0
        if b:betti[degree-1]=b
    assert betti.get(-1,0)==0
    if n==8:assert betti=={3:24,4:292,5:1},betti
    if n==9:assert betti=={4:402,5:815},betti
    print('St',n,'faces',len(faces),'incidences',incidence,
          'fvector',dict(sorted(fvector.items())),flush=True)
    print('critical',dict(sorted((a,len(v)) for a,v in groups.items())),
          'Morse boundary ranks',ranks,'maximum pivot-update coefficient',maximum,flush=True)
    print('reduced integral homology, all free:',betti,flush=True)
    return betti

if __name__=='__main__':
    run(8)
    run(9)
    print('STIRLING_INTEGRAL_CERTIFICATE_OK')
