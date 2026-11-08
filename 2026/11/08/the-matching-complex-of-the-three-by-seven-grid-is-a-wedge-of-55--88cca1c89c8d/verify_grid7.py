#!/usr/bin/env python3
"""Standalone exact finite check of the 3-by-7 grid matching-complex homotopy calculation."""
from collections import Counter,deque
from functools import lru_cache
import hashlib
import json

def graph_edges(rows=3,cols=7):
    edges=[]
    for i in range(rows):
        for j in range(cols):
            if i+1<rows:edges.append(((i,j),(i+1,j)))
            if j+1<cols:edges.append(((i,j),(i,j+1)))
    return edges

def all_faces(edges):
    m=len(edges); masks=[]
    for i,(u,v) in enumerate(edges):
        clash=0
        for j,(a,b) in enumerate(edges):
            if i!=j and (u==a or u==b or v==a or v==b):clash |= 1<<j
        masks.append(clash)
    faces=set()
    def add(start,face):
        faces.add(face)
        for i in range(start,m):
            if not (masks[i]&face):add(i+1,face | 1<<i)
    add(0,0)
    return faces

def toggle_matching(faces,order):
    remaining=faces.copy();up={};down={}
    for i in order:
        bit=1<<i
        for lo in tuple(remaining):
            if lo&bit:continue
            hi=lo|bit
            if hi in remaining:
                remaining.remove(lo);remaining.remove(hi)
                up[lo]=hi;down[hi]=lo
    return remaining,up,down

def check_acyclic(faces,up,down):
    # At each upper face, reverse its matched incidence; all other incidences descend.
    # Kahn topological order for Hasse digraph, including empty cell.
    indegree={f:0 for f in faces}
    for f in faces:
        q=f
        while q:
            b=q&-q;q-=b;lo=f^b
            if lo not in indegree:continue
            if down.get(f)==lo:indegree[f]+=1
            else:indegree[lo]+=1
    Q=deque(f for f,d in indegree.items() if not d)
    visited=0
    while Q:
        f=Q.popleft(); visited+=1
        if f in up:
            x=up[f];indegree[x]-=1
            if indegree[x]==0:Q.append(x)
        q=f
        while q:
            b=q&-q;q-=b;lo=f^b
            if lo not in indegree or down.get(f)==lo:continue
            indegree[lo]-=1
            if indegree[lo]==0:Q.append(lo)
    return visited==len(faces),visited

def incidence(upper, lower):
    b=upper^lower
    assert b and b&(b-1)==0
    idx=(upper&(b-1)).bit_count()
    return -1 if idx&1 else 1

def differential(critical,up,down):
    small=sorted(x for x in critical if x.bit_count()==7)
    big=sorted(x for x in critical if x.bit_count()==8)
    assert len(small)==59 and len(big)==4, (len(small),len(big))
    to_index={f:i for i,f in enumerate(small)}
    @lru_cache(maxsize=None)
    def reduce(face):
        if face in to_index:return ((to_index[face],1),)
        if face in down:return () # zero: this is the upper element of a lower-dimensional matched pair
        assert face in up,(face,'unmatched')
        higher=up[face];pivot=incidence(higher,face)
        totals={}
        q=higher
        while q:
            b=q&-q;q-=b;lo=higher^b
            if lo==face:continue
            coeff=-pivot*incidence(higher,lo)
            for idx,w in reduce(lo):
                totals[idx]=totals.get(idx,0)+coeff*w
        return tuple((i,c) for i,c in sorted(totals.items()) if c)
    columns=[]
    for top in big:
        vals={}
        q=top
        while q:
            b=q&-q;q-=b;lo=top^b
            sgn=incidence(top,lo)
            for idx,w in reduce(lo):vals[idx]=vals.get(idx,0)+sgn*w
        columns.append([vals.get(i,0) for i in range(len(small))])
    return small,big,columns,reduce.cache_info()

def primitive_rank(columns):
    # An explicit integer determinant +/-1 for a 4-by-4 minor suffices.
    import itertools
    mat=list(zip(*columns))
    def det(a):
        n=len(a)
        if n==1:return a[0][0]
        return sum(((-1)**k)*a[0][k]*det([row[:k]+row[k+1:] for row in a[1:]]) for k in range(n))
    for inds in itertools.combinations(range(len(mat)),4):
        minor=[list(mat[i]) for i in inds]
        d=det(minor)
        if abs(d)==1:return inds,d,minor
    return None

if __name__=='__main__':
    edges=graph_edges();faces=all_faces(edges)
    assert len(edges)==32 and len(faces)==196785
    crit,up,down=toggle_matching(faces,range(len(edges)))
    assert len(up)==len(down)==(len(faces)-len(crit))//2
    assert Counter(x.bit_count()-1 for x in crit)=={6:59,7:4}
    ok,visited=check_acyclic(faces,up,down)
    assert ok,(visited,len(faces))
    low,high,cols,cache=differential(crit,up,down)
    certificate=primitive_rank(cols)
    assert certificate is not None,cols
    fvec=Counter(f.bit_count() for f in faces)
    assert -sum((-1)**k*c for k,c in fvec.items())==55
    # The augmented empty simplex is paired with precisely one vertex.
    # Deleting the empty simplex and that pair makes the vertex critical.
    assert 0 in up and up[0].bit_count()==1
    assert 0 not in crit
    # Unaugmented face-poset matching: former mate of empty is the critical vertex.
    up0={lo:hi for lo,hi in up.items() if lo}
    down0={hi:lo for hi,lo in down.items() if lo}
    ok_unaug,seen_unaug=check_acyclic(faces-{0},up0,down0)
    assert ok_unaug and seen_unaug==len(faces)-1
    assert len(crit)==63 and len(up0)==98360
    # Signed 4x4 unimodular minor certifies integral primitive rank four.
    minor_rows=certificate[0]
    minor_matrix=certificate[2]
    assert all(len(column)==59 for column in cols)
    assert len(cols)==4
    # A second exact mod-two elimination checks the integer-minor rank.
    mod2=[sum((c&1)<<i for i,c in enumerate(col)) for col in cols]
    pivots={}
    for vec in mod2:
        while vec:
            i=vec.bit_length()-1
            if i not in pivots:
                pivots[i]=vec; break
            vec ^= pivots[i]
    assert len(pivots)==4
    encoded=json.dumps(cols,separators=(',',':')).encode('utf-8')
    print('GRID7_MORSE_OK', 'vertices',21,'grid_edges',len(edges),'faces_including_empty',len(faces),
          'pairs_including_empty',len(up),'critical_6cells',len(low),'critical_7cells',len(high),
          'critical_0cell_after_unaugmentation',1, 'acyclic_hasse_nodes',visited,'acyclic_nonempty_nodes',seen_unaug,
          'unimodular_row_indices',minor_rows,'minor',minor_matrix,'det',certificate[1],
          'mod2_boundary_rank',len(pivots),'Euler_reduced',55,
          'morse_boundary_sha256',hashlib.sha256(encoded).hexdigest(),
          'face_vector_including_empty',sorted(fvec.items()),'memo',cache)
