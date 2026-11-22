#!/usr/bin/env python3
"""Exact finite certificates for Morse complexes of one-edge-fault triangular prisms.

Runs with standard Python 3 only. Faces are exhaustive incidence-arrow masks.
No external data, generated tables, or third-party packages are required.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N_VERTICES = 6
EDGES = ((0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5))
EXPECTED = {"rung": (960, (16,98,284,381,180), (16,16), 7, (9,9)),
            "rim":  (1008,(16,98,286,397,210), (4,20), 4, (0,16))}


def directed_arrow_options(edges):
    return [(source, edge_id, target)
            for edge_id,(u,v) in enumerate(edges)
            for source,target in ((u,v),(v,u))]


def is_face(mask, arrows):
    used_v=set(); used_e=set(); successors={}
    for i,(u,edge_id,v) in enumerate(arrows):
        if not (mask>>i)&1:continue
        if u in used_v or edge_id in used_e:return False
        used_v.add(u); used_e.add(edge_id); successors[u]=v
    for u in successors:
        path=set();x=u
        while x in successors:
            if x in path:return False
            path.add(x);x=successors[x]
    return True


def all_faces(arrows):
    return {x for x in range(1<<len(arrows)) if is_face(x,arrows)}


def acyclic_bit_matching(faces, n):
    free=set(faces); pairs=[]
    for bit in range(n):
        to_pair=[]
        for f in sorted(free):
            g=f | (1<<bit)
            if g!=f and g in free:
                to_pair.append((f,g))
        for f,g in to_pair:
            assert f in free and g in free
            free.remove(f);free.remove(g)
        pairs.extend(to_pair)
    return free,pairs


def verify_matching(faces,critical,pairs):
    matched=set();direction=defaultdict(list);indeg=Counter()
    low_to_high=dict(pairs)
    assert all(g.bit_count()==f.bit_count()+1 and g&f==f for f,g in pairs)
    for f,g in pairs:
        assert f not in matched and g not in matched
        matched.update((f,g))
    assert matched|critical == faces and not (matched&critical)
    for g in faces:
        for bit in range(g.bit_length()):
            if not (g>>bit)&1:continue
            f=g ^ (1<<bit)
            if f not in faces:continue
            if low_to_high.get(f)==g:a,b=f,g
            else:a,b=g,f
            direction[a].append(b);indeg[b]+=1
    queue=deque(f for f in faces if indeg[f]==0); seen=0
    while queue:
        x=queue.popleft();seen+=1
        for y in direction[x]:
            indeg[y]-=1
            if indeg[y]==0:queue.append(y)
    assert seen==len(faces), (seen,len(faces))


def signed_boundary(g):
    return [(g^(1<<i), (-1)**j)
        for j,i in enumerate(i for i in range(g.bit_length()) if (g>>i)&1)]


def morse_d4(critical,pairs):
    matched_low_to_high=dict(pairs)
    lower=sorted(x for x in critical if x.bit_count()==4)
    higher=sorted(x for x in critical if x.bit_count()==5)
    lower_set=set(lower)
    @lru_cache(None)
    def reduce_low(f):
        if f in lower_set:return {f:1}
        g=matched_low_to_high.get(f)
        if g is None:return {} # f is eliminated as an upper cell of a lower-dimensional pair
        coeff_f=dict(signed_boundary(g))[f]
        result=defaultdict(int)
        for t,coeff in signed_boundary(g):
            if t==f:continue
            for w,c in reduce_low(t).items():result[w]-=coeff_f*coeff*c
        return {w:c for w,c in result.items() if c}
    matrix=[]
    for g in higher:
        sums=defaultdict(int)
        for f,c in signed_boundary(g):
            for w,v in reduce_low(f).items():sums[w]+=c*v
        matrix.append([sums[w] for w in lower])
    return lower,higher,matrix


def unit_diagonalize(rows):
    """Only unimodular integer row/column operations (determinant ±1); exact unit factors."""
    a=[row[:] for row in rows]
    nr=len(a); nc=len(a[0]) if nr else 0
    t=0
    while t<min(nr,nc):
        pivot=next(((i,j) for i in range(t,nr)
                    for j in range(t,nc) if abs(a[i][j])==1),None)
        if pivot is None:break
        i,j=pivot
        a[t],a[i]=a[i],a[t]
        for row in a:row[t],row[j]=row[j],row[t]
        if a[t][t]==-1:a[t]=[-v for v in a[t]]
        for h in range(nr):
            if h==t:continue
            coeff=a[h][t]
            if coeff:a[h]=[u-coeff*v for u,v in zip(a[h],a[t])]
        for k in range(nc):
            if k==t:continue
            coeff=a[t][k]
            if coeff:
                for h in range(nr):a[h][k]-=coeff*a[h][t]
        t+=1
    assert all(a[i][j]==(1 if i==j and i<t else 0)
               for i in range(nr) for j in range(nc)), 'Nonunit residual block'
    return t


def rank_mod2(columns):
    pivots={}
    for vector in columns:
        while vector:
            leading=vector.bit_length()-1
            if leading not in pivots:
                pivots[leading]=vector;break
            vector^=pivots[leading]
    return len(pivots)


def direct_mod2_betti(faces):
    by_dimension={k:sorted(f for f in faces if f.bit_count()==k+1)
                  for k in range(5)}
    ranks={0:0,5:0}
    for k in range(1,5):
        idx={f:i for i,f in enumerate(by_dimension[k-1])}
        columns=[]
        for g in by_dimension[k]:
            column=0
            for f,coeff in signed_boundary(g):column^=1<<idx[f]
            columns.append(column)
        ranks[k]=rank_mod2(columns)
    betti=[len(by_dimension[k])-ranks[k]-ranks[k+1] for k in range(5)]
    betti[0]-=1 # reduced H_0
    return betti,ranks


def compute(which,edges):
    arrows=directed_arrow_options(edges)
    faces=all_faces(arrows)-{0}
    critical,pairs=acyclic_bit_matching(faces,len(arrows))
    verify_matching(faces,critical,pairs)
    low,hi,d4=morse_d4(critical,pairs)
    rank=unit_diagonalize(d4)
    assert sum(x.bit_count()==1 for x in critical)==1
    assert all(x.bit_count() in (1,4,5) for x in critical)
    betti=[len(low)-rank,len(hi)-rank]
    mod2_betti,mod2_ranks=direct_mod2_betti(faces)
    assert tuple(mod2_betti)==(0,0,0,*betti),(which,mod2_betti,betti)
    fvector=tuple(sum(1 for f in faces if f.bit_count()==k) for k in range(1,6))
    exp_faces,exp_fvector,exp_critical,exp_rank,exp_betti=EXPECTED[which]
    assert (len(faces)+1,fvector,(len(low),len(hi)),rank,tuple(betti)) == (
        exp_faces,exp_fvector,exp_critical,exp_rank,exp_betti)
    print(f"{which}: faces={len(faces)+1}, fvector={fvector}, "
          f"matched_pairs={len(pairs)}, critical=(one 0-cell, {len(low)} 3-cells, {len(hi)} 4-cells), "
          f"unit_rank={rank}, reduced_betti3_4={tuple(betti)}, "
          f"direct_mod2_betti={mod2_betti}, direct_mod2_boundary_ranks={mod2_ranks}, "
          "HASSE_ACYCLIC PASS; UNIT_DIAGONAL PASS")


def main():
    compute('rung',EDGES[:-1])
    compute('rim',EDGES[1:])
    print('ALL CHECKS PASSED')

if __name__ == '__main__':main()
