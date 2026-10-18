#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, deque

VERTS = [x for x in range(32) if x.bit_count() % 2 == 0]
PIVOT_ORDER = [4,1,6,2,13,10,12,15,8,11,5,7,14,3,0,9]
EXPECTED_F_BY_SIZE = (16,80,160,120,16)
EXPECTED_RANKS = (15,65,95,16)
EXPECTED_BETTI_REDUCED = {3:9}


def bitstr(x):
    return format(x, '05b')


def is_edge(i,j):
    return (VERTS[i] ^ VERTS[j]).bit_count() == 4


def independent(mask):
    ids=[i for i in range(16) if (mask>>i)&1]
    return all(not is_edge(i,j) for i,j in combinations(ids,2))


def gf2_rank(rows):
    rows=[int(x) for x in rows if x]
    rank=0
    while rows:
        pivot=max(rows)
        rows.remove(pivot)
        b=1 << (pivot.bit_length()-1)
        rows=[r ^ pivot if r & b else r for r in rows]
        rows=[r for r in rows if r]
        rank += 1
    return rank


def boundary_rank(k_faces, km1_index):
    # matrix columns are k-dimensional simplices (cardinality k+1),
    # rows are (k-1)-simplices; encode each column as a bit-vector of rows.
    cols=[]
    for face in k_faces:
        col=0
        ids=[i for i in range(16) if (face>>i)&1]
        for v in ids:
            sub=face ^ (1<<v)
            col |= 1 << km1_index[sub]
        cols.append(col)
    return gf2_rank(cols)


def main():
    # Graph checks.
    edges=[(i,j) for i in range(16) for j in range(i+1,16) if is_edge(i,j)]
    deg=[0]*16
    for i,j in edges:
        deg[i]+=1; deg[j]+=1
    assert len(VERTS)==16
    assert len(edges)==40
    assert set(deg)=={5}
    # triangle-free and strongly-regular common-neighbor counts (16,5,0,2)
    nbs=[set() for _ in range(16)]
    for i,j in edges:
        nbs[i].add(j); nbs[j].add(i)
    for i,j in combinations(range(16),2):
        cn=len(nbs[i]&nbs[j])
        assert cn == (0 if j in nbs[i] else 2)

    faces=[m for m in range(1,1<<16) if independent(m)]
    by_size=defaultdict(list)
    for f in faces: by_size[f.bit_count()].append(f)
    fvec=tuple(len(by_size[s]) for s in range(1,6))
    assert fvec==EXPECTED_F_BY_SIZE, fvec
    assert len(faces)==392

    # Sequential repeated-toggle matching.
    unmatched=set(faces)
    pairs=[]
    for p in PIVOT_ORDER:
        bit=1<<p
        staged=[]
        for f in sorted(unmatched):
            if f & bit: continue
            g=f|bit
            if g in unmatched:
                staged.append((f,g))
        # Staging is disjoint because every lower face has a unique toggle partner.
        for a,b in staged:
            assert a in unmatched and b in unmatched
            assert b.bit_count()==a.bit_count()+1
            assert (a & bit)==0 and b==(a|bit)
            unmatched.remove(a); unmatched.remove(b); pairs.append((a,b))
    assert len(pairs)==191
    critical=sorted(unmatched)
    crit_by_dim=defaultdict(list)
    for f in critical: crit_by_dim[f.bit_count()-1].append(f)
    assert {d:len(v) for d,v in crit_by_dim.items()}=={0:1,3:9}

    # Complete Hasse cover set and acyclic Morse orientation.
    face_set=set(faces)
    covers=[]
    for upper in faces:
        if upper.bit_count()<2: continue
        ids=[i for i in range(16) if (upper>>i)&1]
        for v in ids:
            lower=upper^(1<<v)
            if lower in face_set:
                covers.append((lower,upper))
    assert len(covers)==1200
    matched=set(pairs)
    out={f:[] for f in faces}
    indeg={f:0 for f in faces}
    for lower,upper in covers:
        if (lower,upper) in matched:
            a,b=lower,upper  # reverse matched cover: lower -> upper
        else:
            a,b=upper,lower  # unmatched cover directed downward
        out[a].append(b); indeg[b]+=1
    q=deque([f for f in faces if indeg[f]==0])
    seen=0
    while q:
        f=q.popleft(); seen+=1
        for g in out[f]:
            indeg[g]-=1
            if indeg[g]==0: q.append(g)
    assert seen==len(faces), (seen,len(faces))

    # Independent mod-2 simplicial homology computation.
    ranks=[]
    for k in range(1,5):
        km1=by_size[k]
        kfaces=by_size[k+1]
        idx={f:i for i,f in enumerate(km1)}
        ranks.append(boundary_rank(kfaces,idx))
    assert tuple(ranks)==EXPECTED_RANKS, ranks
    # unreduced b0 = f0-r1; for d>=1 b_d=f_d-r_d-r_{d+1}
    betti=[]
    dims=[len(by_size[d+1]) for d in range(5)]
    r=[0]+ranks+[0]
    for d in range(5):
        betti.append(dims[d]-r[d]-r[d+1])
    assert betti==[1,0,0,9,0], betti

    red_euler=sum(((-1)**d)*dims[d] for d in range(5))-1
    assert red_euler==-9

    print('graph=FQ5/Clebsch on even-weight F2^5, adjacency Hamming distance 4')
    print('vertices=16 edges=40 degree=5 strongly_regular=(16,5,0,2)')
    print('nonempty_faces=392')
    print('f_vector=' + repr(EXPECTED_F_BY_SIZE))
    print('hasse_covers=1200')
    print('matched_pairs=191')
    print('critical_cells={0:1,3:9}')
    print('boundary_ranks_F2=' + repr(EXPECTED_RANKS))
    print('reduced_betti_F2={3:9}')
    print('reduced_euler=-9')
    print('pivot_order_vertex_bits=' + repr([bitstr(VERTS[i]) for i in PIVOT_ORDER]))
    print('critical_faces=' + repr([[bitstr(VERTS[i]) for i in range(16) if (f>>i)&1] for f in critical]))
    print('ACYCLIC_MATCHING_OK')
    print('VERIFY_OK')

if __name__=='__main__': main()
