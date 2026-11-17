#!/usr/bin/env python3
"""Exact certificate for the ordinary matching complex of P4 Cartesian C4.
Requires Python >=3.10 and SymPy 1.14.0. No data downloads.
"""
import collections
import functools
import json
from pathlib import Path
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def graph_edges():
    # Vertices are (r,c) encoded as 4*r+c, 0<=r,c<4.
    e = set()
    for r in range(4):
        for c in range(4):
            u = 4*r+c
            if r < 3:
                e.add(tuple(sorted((u, u+4))))
            e.add(tuple(sorted((u,4*r+(c+1)%4))))
    return sorted(e)


def generate_faces(edges):
    incident = [0]*16
    for j,(u,v) in enumerate(edges):
        incident[u] |= 1<<j
        incident[v] |= 1<<j
    blocked = [incident[u]|incident[v] for u,v in edges]
    result=[]
    def visit(face, used, start):
        result.append(face)
        for j in range(start,len(edges)):
            if not (used & (1<<j)):
                visit(face|(1<<j), used|blocked[j],j+1)
    visit(0,0,0)
    assert len(result) == len(set(result))
    return result


def bd(face):
    bits=[]
    j=0
    while face:
        bit=face&-face
        bits.append((bit, -1 if j%2 else 1))
        face-=bit
        j+=1
    return bits


def complete_certificate():
    edges=graph_edges()
    assert len(edges)==28
    faces=generate_faces(edges)
    face_set=set(faces)
    face_counts=collections.Counter(s.bit_count()-1 for s in faces if s)
    assert len(faces)==21497
    live=face_set.copy()
    pairs=[]
    mate={}
    for j in range(len(edges)):
        # The empty face is excluded from the nonaugmented face-poset matching.
        current=[(a,a|(1<<j)) for a in sorted(live) if a and not (a&(1<<j)) and (a|(1<<j)) in live]
        for a,b in current:
            assert a in live and b in live
            live.remove(a);live.remove(b)
            mate[a]=b;mate[b]=a
        pairs.extend(current)
    assert 0 in live
    critical=collections.Counter(s.bit_count()-1 for s in live if s)
    assert critical=={0:1,4:12,5:37}
    assert len(pairs)==10723
    # Directed Hasse graph: reverse every matched covering edge.
    arrows=collections.defaultdict(list)
    indeg=collections.Counter()
    incidences=0
    for s in faces:
        if not s:continue
        for bit,_ in bd(s):
            a=s^bit
            if not a:continue
            if mate.get(a)==s:
                arrows[a].append(s);indeg[s]+=1
            else:
                arrows[s].append(a);indeg[a]+=1
            incidences+=1
    q=collections.deque(s for s in faces if s and indeg[s]==0)
    visited=0
    while q:
        s=q.popleft();visited+=1
        for t in arrows[s]:
            indeg[t]-=1
            if indeg[t]==0:q.append(t)
    assert visited==len(faces)-1, 'Hasse directed cycle detected'
    crit4=sorted(s for s in live if s.bit_count()==5)
    crit5=sorted(s for s in live if s.bit_count()==6)
    i4={s:i for i,s in enumerate(crit4)}
    up={a:b for a,b in pairs}

    @functools.lru_cache(None)
    def reduction(a):
        # Projection of a 4-simplex along gradient paths to critical 4-cells.
        if a in i4:return {i4[a]:1}
        if a not in up:return {}
        b=up[a]
        ab_sign=next(sign for bit,sign in bd(b) if (b^bit)==a)
        result=collections.defaultdict(int)
        for bit,sign in bd(b):
            c=b^bit
            if c==a:continue
            for idx,v in reduction(c).items():
                result[idx]-=ab_sign*sign*v
        return {k:v for k,v in result.items() if v}

    matrix=[]  # one entry per column of the integral Morse boundary
    for s in crit5:
        result=collections.defaultdict(int)
        for bit,sign in bd(s):
            for idx,v in reduction(s^bit).items():
                result[idx]+=sign*v
        matrix.append([result[j] for j in range(len(crit4))])
    A=Matrix(matrix).T
    assert A.shape==(12,37)
    expected=json.loads((Path(__file__).parent/'boundary.json').read_text())
    assert expected['columns_37_by_rows_12']==matrix
    assert expected['critical_4_faces_masks']==crit4
    assert expected['critical_5_faces_masks']==crit5
    assert expected['ordered_graph_edges']==[list(e) for e in edges]
    assert expected['face_counts_dimension']==dict(sorted((str(k),v) for k,v in face_counts.items()))
    assert sum(v!=0 for v in A)==108
    assert A.rank()==10
    left_relations=[[-1,1,1,-1,-1,-1,1,0,0,-1,1,0],[1,-1,0,1,0,1,-1,1,1,1,0,1]]
    for relation in left_relations:
        assert Matrix([relation])*A==Matrix.zeros(1,37)
    idx_rows=list(range(10))
    idx_cols=[0,1,2,4,6,7,8,14,16,17]
    assert A.extract(idx_rows,idx_cols).det()==-1
    D=smith_normal_form(A,domain=ZZ)
    invariant_factors=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
    assert invariant_factors==[1]*10
    # Independent simplicial homology over F2; no Morse reduction used.
    faces_in_dim=collections.defaultdict(list)
    for s in faces:
        if s:faces_in_dim[s.bit_count()-1].append(s)
    ranks={0:0}
    for d in range(1,8):
        lower={s:i for i,s in enumerate(faces_in_dim[d-1])}
        pivots={}
        for s in faces_in_dim[d]:
            c=0
            for bit,_ in bd(s):c^=1<<lower[s^bit]
            while c:
                p=c.bit_length()-1
                if p in pivots:c^=pivots[p]
                else:pivots[p]=c;break
        ranks[d]=len(pivots)
    betti={d:len(faces_in_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0) for d in range(8)}
    assert betti=={0:0,1:0,2:0,3:0,4:2,5:27,6:0,7:0}
    return dict(vertices=16, edges=len(edges), faces_including_empty=len(faces),
                dimension_face_counts={str(k):v for k,v in sorted(face_counts.items())},
                face_poset_cover_relations=incidences, matched_pairs=len(pairs),
                critical_cells={str(k):v for k,v in sorted(critical.items())},
                acyclic_faces_checked=visited, integral_morse_boundary_shape=[12,37],
                integral_boundary_nonzero_entries=108, integral_boundary_rank=10,
                unit_minor_determinant=-1, smith_nonzero_diagonal=invariant_factors,
                original_simplicial_F2_boundary_ranks={str(k):v for k,v in ranks.items()},
                original_reduced_F2_betti={str(k):v for k,v in betti.items()},
                integral_homotopy_wedge={'S4':2,'S5':27}, status='P4_C4_INTEGRAL_WEDGE_PASS')

if __name__=='__main__':
    print(json.dumps(complete_certificate(),sort_keys=True,indent=2))
