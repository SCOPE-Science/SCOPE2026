#!/usr/bin/env python3
"""Reconstruct and verify the elementary collapse of the full-symmetry
Shrikhande independence-complex quotient. Python 3 standard library only.

Usage: python3 verify.py [certificate.json]
"""
import json
import sys
from collections import Counter, defaultdict
from itertools import product, combinations
from pathlib import Path

N = 4
VERTICES = list(product(range(N), repeat=2))
INDEX = {v: i for i, v in enumerate(VERTICES)}
D = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}

def adj(i,j):
    a,b=VERTICES[i],VERTICES[j]
    return i!=j and ((a[0]-b[0])%4,(a[1]-b[1])%4) in D

def faces():
    out=[]
    for k in range(1,17):
        for p in combinations(range(16),k):
            if all(not adj(i,j) for i,j in combinations(p,2)):
                out.append(sum(1<<v for v in p))
        if k>=5:
            assert not any(x.bit_count()==k for x in out)
            break
    return sorted(out)

def automorphisms():
    groups=[]
    for a,b,c,d in product(range(4),repeat=4):
        def linear(v): return ((a*v[0]+b*v[1])%4,(c*v[0]+d*v[1])%4)
        if {linear(v) for v in D}!=D: continue
        for t in VERTICES:
            perm=tuple(INDEX[((linear(v)[0]+t[0])%4,(linear(v)[1]+t[1])%4)] for v in VERTICES)
            assert len(set(perm))==16
            assert all(adj(i,j)==adj(perm[i],perm[j]) for i in range(16) for j in range(i))
            groups.append(perm)
    assert len(groups)==len(set(groups))==192
    nbr={j for j in range(16) if adj(0,j)}
    assert len(nbr)==6
    assert all(sum(adj(u,v) for v in nbr)==2 for u in nbr)
    # Connected 2-regular neighbor graph has six vertices, hence is a 6-cycle.
    q=[next(iter(nbr))]
    while len(q)<6:
        nxt=next((v for v in nbr if adj(q[-1],v) and v not in q),None)
        assert nxt is not None
        q.append(nxt)
    assert adj(q[-1],q[0])
    outer=set(range(16))-nbr-{0}
    fingerprints=[frozenset(v for v in nbr if adj(w,v)) for w in outer]
    assert len(outer)==len(set(fingerprints))==9
    # Every origin-fixing automorphism acts faithfully on the six neighbors,
    # hence has size <= Aut(C_6)=12. The displayed 192 maps are all automorphisms.
    return groups

def compute():
    F=faces(); G=automorphisms()
    assert Counter(m.bit_count() for m in F)=={1:16,2:72,3:96,4:16}
    face_index={f:i for i,f in enumerate(F)}
    trans=[]
    for g in G:
        row=[]
        for f in F:
            image=sum(1<<g[v] for v in range(16) if (f>>v)&1)
            row.append(face_index[image])
        trans.append(tuple(row))
    strict_sub=[tuple(i for i,p in enumerate(F) if p!=f and (p&f)==p) for f in F]
    chains=set()
    def extend(end,history):
        chain=history+(end,)
        chains.add(chain)
        for parent in strict_sub[end]:
            extend(parent,chain)
    for i in range(len(F)):
        extend(i,())
    assert len(chains)==2680
    canon=lambda seq:min(tuple(g[i] for i in seq) for g in trans)
    cells=sorted({canon(seq) for seq in chains})
    assert len(cells)==43
    ids={c:i for i,c in enumerate(cells)}
    assert Counter(len(c)-1 for c in cells)=={0:8,1:17,2:14,3:4}
    boundaries=[]
    for c in cells:
        boundaries.append(tuple(ids[canon(c[:j]+c[j+1:])] for j in range(len(c))) if len(c)>1 else ())
    for c in cells:
        if len(c)<3: continue
        v=defaultdict(int)
        for j,f in enumerate(boundaries[ids[c]]):
            for k,e in enumerate(boundaries[f]): v[e]+=(-1)**(j+k)
        assert all(x==0 for x in v.values()),'boundary squared nonzero'
    return F,G,cells,boundaries

def check(F,G,cells,boundaries,cert):
    assert cert['cell_counts']==[8,17,14,4]
    assert cert['independence_face_counts']==[16,72,96,16]
    assert cert['group_size']==192
    assert cert['all_cell_chains']==[list(c) for c in cells]
    assert len(cert['pairs'])==21
    alive=set(range(len(cells)))
    for step,(f,c) in enumerate(cert['pairs'],1):
        assert f in alive and c in alive,('removed cell',step)
        assert len(cells[c])==len(cells[f])+1,('dimension',step)
        assert f in boundaries[c],('not a face',step)
        assert sum(f in boundaries[k] for k in alive)==1,('not a free face',step)
        alive-={f,c}
        # Closure check at every stage, excluding removed cells.
        assert all(set(boundaries[k])<=alive for k in alive),('closure',step)
    assert len(alive)==1 and len(cells[next(iter(alive))])==1
    assert cert['remaining_vertex']==next(iter(alive))
    print('SHRIKHANDE_FULL_AUTOMORPHISM_QUOTIENT_COLLAPSES_OK')
    print('vertices=16 edges=48 automorphisms=192 nonempty_independent_faces=200 flags=2680')
    print('quotient_cells_by_dim=8,17,14,4 collapses=21 remains_one_vertex')

def main():
    F,G,cells,boundaries=compute()
    cp=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('certificate.json')
    if len(sys.argv)>1 and sys.argv[1]=='--generate':
        active=set(range(len(cells)))
        cofaces=defaultdict(set)
        for i,bd in enumerate(boundaries):
            for j in bd: cofaces[j].add(i)
        pairs=[]
        for _ in range(21):
            pair=next(((f,next(iter(cofaces[f]&active))) for f in range(len(cells)) if f in active and len(cofaces[f]&active)==1),None)
            assert pair is not None
            pairs.append(pair);active.difference_update(pair)
        assert len(active)==1
        print(json.dumps(dict(group_size=192,independence_face_counts=[16,72,96,16],cell_counts=[8,17,14,4],all_cell_chains=[list(c) for c in cells],pairs=pairs,remaining_vertex=next(iter(active))),separators=(',',':')))
    else:
        check(F,G,cells,boundaries,json.loads(cp.read_text(encoding='utf-8')))
if __name__=='__main__':main()
