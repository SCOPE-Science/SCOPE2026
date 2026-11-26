#!/usr/bin/env python3
"""Replay a complete antipodal orbit-cell collapse certificate and F_2 homology."""
import json
import sys
from collections import defaultdict
from pathlib import Path

N=12
HALF=6
FULL=(1<<N)-1

def antipode(mask):
    return ((mask & ((1<<HALF)-1))<<HALF) | (mask>>HALF)

def representative(mask):
    return min(mask,antipode(mask))

def vertex_set(mask):
    return tuple(i for i in range(N) if mask & (1<<i))

def construct():
    adj=[]
    for i in range(N):
        nbr={(i-1)%N,(i+1)%N,(i+HALF)%N}
        adj.append(sum(1<<j for j in nbr))
    faces=[0]
    for i in range(N):
        faces.extend(mask|(1<<i) for mask in list(faces) if not (mask & adj[i]))
    assert len(faces)==197 and len(faces)==len(set(faces))
    fs=set(faces)
    assert all(antipode(f) in fs for f in fs)
    assert all(f!=antipode(f) for f in fs if f)
    # There is no vertex pair in the same half-turn orbit within any face.
    assert all((mask & antipode(mask))==0 for mask in fs)
    cells={(f.bit_count()-1, representative(f)) for f in fs if f}
    assert len(cells)==98
    down={}; up=defaultdict(set)
    for d,f in cells:
        z=(d,f)
        down[z]=set()
        if d:
            for i in vertex_set(f):
                v=(d-1,representative(f^(1<<i)))
                assert v in cells
                down[z].add(v)
                up[v].add(z)
            assert len(down[z])==d+1  # no boundary-face identifications
    return fs,cells,down,up

def replay(cert,fs,cells,down,up):
    assert cert['graph_vertices']==N and cert['halfturn_addition']==HALF
    assert cert['independent_faces_including_empty']==len(fs)
    assert cert['cell_orbits']==len(cells)
    remaining=set(cells)
    ups={z:set(up[z]) for z in cells}
    seen=set()
    for row in cert['collapse_pairs']:
        a=tuple(row['lower']);b=tuple(row['upper'])
        assert a in remaining and b in remaining and a not in seen and b not in seen
        assert a in down[b] and b[0]==a[0]+1
        assert ups[a]=={b}, (a,ups[a],b)
        # Check the orbit pair really lifts to an equivariant elementary collapse.
        aa=a[1]; bb=b[1]
        assert aa & ~bb==0 or aa & ~antipode(bb)==0
        for z in (a,b):
            remaining.remove(z);seen.add(z)
            for lower in down[z]:
                if lower in ups: ups[lower].discard(z)
            ups.pop(z,None)
    assert len(cert['collapse_pairs'])==32
    vector=[sum(z[0]==d for z in remaining) for d in range(5)]
    assert vector==cert['remaining_cells_by_dimension']==[6,16,12,0,0]
    assert sum((-1)**d*vector[d] for d in range(5))==2
    assert all(d<=2 for d,z in remaining)
    # Every surviving cell has its entire cellular boundary still present.
    assert all(down[z]<=remaining for z in remaining)
    return vector

def rank_f2(columns):
    pivots={}
    for col in columns:
        while col:
            i=col.bit_length()-1
            if i not in pivots:
                pivots[i]=col;break
            col ^= pivots[i]
    return len(pivots)

def mod2_betti(cells,down):
    by={d:sorted(z for z in cells if z[0]==d) for d in range(5)}
    ranks={}
    for d in range(1,5):
        idx={z:k for k,z in enumerate(by[d-1])}
        columns=[]
        for z in by[d]:
            mask=0
            for a in down[z]:mask^=(1<<idx[a])
            columns.append(mask)
        ranks[d]=rank_f2(columns)
    betti={d:len(by[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(5)}
    assert betti=={0:1,1:1,2:2,3:0,4:0}
    return betti


def check_pi1_certificate(cert,fs):
    # The independence complex is flag, and these triangular relations kill every
    # non-tree 1-cell generator of its usual edge-path fundamental-group presentation.
    import itertools
    all_edges={tuple(sorted(edge)) for edge in itertools.combinations(range(N),2)
               if sum(1<<i for i in edge) in fs}
    all_tris={frozenset(tri) for tri in itertools.combinations(range(N),3)
              if sum(1<<i for i in tri) in fs}
    assert len(all_edges)==48 and len(all_tris)==76
    data=cert['fundamental_group_certificate']
    tree=[tuple(edge) for edge in data['tree_edges']]
    assert len(tree)==11 and len(set(tree))==11 and set(tree)<=all_edges
    touched={0}
    while True:
        nxt=touched|{j for i,j in all_edges if i in touched}|{i for i,j in all_edges if j in touched}
        if nxt==touched:break
        touched=nxt
    assert touched==set(range(N))
    # The listed edges must themselves form a spanning tree.
    groups=[{v} for v in range(N)]
    for a,b in tree:
        ia=next(i for i,g in enumerate(groups) if a in g)
        ib=next(i for i,g in enumerate(groups) if b in g)
        assert ia!=ib
        groups[ia]|=groups[ib];groups.pop(ib)
    assert len(groups)==1
    known=set(tree)
    for row in data['triangle_fills']:
        tri=row['triangle'];assert frozenset(tri) in all_tris
        ed={tuple(sorted(e)) for e in itertools.combinations(tri,2)}
        missing=tuple(row['added_edge'])
        assert ed-known=={missing} and missing in all_edges
        known.add(missing)
    assert len(data['triangle_fills'])==37 and known==all_edges
    return len(tree),len(data['triangle_fills'])

def main():
    base=Path(__file__).resolve().parent
    cert=json.loads((base/'CERTIFICATE.json').read_text(encoding='utf-8'))
    fs,cells,down,up=construct()
    counts=[sum(z[0]==d for z in cells) for d in range(5)]
    assert counts==[6,24,38,24,6]
    betti=mod2_betti(cells,down)
    tree_count,filled=check_pi1_certificate(cert,fs)
    surviving=replay(cert,fs,cells,down,up)
    print('GRAPH 12 vertices; ANTIPODAL_INDEPENDENT_FACE_COUNT 197')
    print('FREE_ORBIT_CW_FVECTOR',*counts)
    print('SIMPLY_CONNECTED_TREE_AND_TRIANGLE_FILLS',tree_count,filled)
    print('COLLAPSE_PAIRS',len(cert['collapse_pairs']))
    print('SURVIVING_CW_FVECTOR',*surviving)
    print('MOD2_BETTI',*[betti[d] for d in range(5)])
    print('VERIFY_OK')
if __name__=='__main__':main()
