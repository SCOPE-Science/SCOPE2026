"""Exact finite checks for geodesic-general-position complexes of wheel bouquets.
Runs without third-party packages; compares independent shortest-path and local-face
models, then computes mod-two simplicial homology by boundary elimination.
The general homotopy statement is proved separately, not extrapolated from tests.
"""
from collections import deque, defaultdict
from itertools import combinations


def wheel_bouquet(lengths):
    nv = sum(lengths) + 1
    apex = nv-1
    neighbors = [set() for _ in range(nv)]
    def add(u, v):
        neighbors[u].add(v)
        neighbors[v].add(u)
    offset=0
    for l in lengths:
        for j in range(l):
            add(offset+j,offset+(j+1)%l)
            add(offset+j,apex)
        offset+=l
    return neighbors


def distances(neighbors):
    n=len(neighbors)
    d=[]
    for x in range(n):
        v=[-1]*n; v[x]=0; q=deque([x])
        while q:
            a=q.popleft()
            for b in neighbors[a]:
                if v[b]<0:
                    v[b]=v[a]+1; q.append(b)
        assert all(z>=0 for z in v)
        d.append(v)
    return d


def gp_face_by_dist(mask,d):
    verts=[i for i in range(len(d)) if mask>>i&1]
    for a,b,c in combinations(verts,3):
        if (d[a][b]+d[b][c]==d[a][c] or
            d[a][c]+d[c][b]==d[a][b] or
            d[b][a]+d[a][c]==d[b][c]):
            return False
    return True


def gp_face_by_local_formula(mask,lengths):
    apex=sum(lengths)
    has_hub=bool(mask>>apex&1)
    nonempty_petals=0
    offset=0
    for l in lengths:
        local=(mask>>offset)&((1<<l)-1)
        if has_hub:
            if local:
                nonempty_petals+=1
                if local.bit_count()>2:return False
                if local.bit_count()==2 and not any(local==((1<<j)|(1<<((j+1)%l))) for j in range(l)):
                    return False
        else:
            for j in range(l):
                if all(local>>(k%l)&1 for k in (j,j+1,j+2)):
                    return False
        offset+=l
    return not(has_hub and nonempty_petals>1)


def boundary_ranks_mod2(faces_by_dim):
    ranks={}
    for k in sorted(faces_by_dim):
        if k==0: continue
        lower={f:i for i,f in enumerate(faces_by_dim[k-1])}
        pivots={}
        for f in faces_by_dim[k]:
            column=0
            for i in range(f.bit_length()):
                if f>>i&1: column ^= 1<<lower[f^(1<<i)]
            while column:
                p=column.bit_length()-1
                if p in pivots: column^=pivots[p]
                else:
                    pivots[p]=column; break
        ranks[k]=len(pivots)
    return ranks


def homology_from_faces(faces):
    ranks=boundary_ranks_mod2(faces)
    betti={k:len(cols)-ranks.get(k,0)-ranks.get(k+1,0) for k,cols in faces.items()}
    if faces:betti[0]-=1
    return {k:v for k,v in betti.items() if v}


def cycle_model_homology(l):
    faces=defaultdict(list)
    for x in range(1,1<<l):
        if not any(all(x>>(k%l)&1 for k in (j,j+1,j+2)) for j in range(l)):
            faces[x.bit_count()-1].append(x)
    return homology_from_faces(faces)


def predicted_betti(lengths):
    m=len(lengths)
    if m==1:return None
    joint={-1:1}
    for l in lengths:
        next_joint=defaultdict(int)
        for a,av in joint.items():
            for b,bv in cycle_model_homology(l).items():
                next_joint[a+b+1]+=av*bv
        joint=dict(next_joint)
    betti=defaultdict(int, joint)
    betti[1]+=m-1
    betti[2]+=m
    return {k:v for k,v in betti.items() if v}


def verify(lengths):
    g=wheel_bouquet(lengths); d=distances(g)
    faces=defaultdict(list)
    for mask in range(1,1<<len(g)):
        by_distance=gp_face_by_dist(mask,d)
        by_formula=gp_face_by_local_formula(mask,lengths)
        assert by_distance==by_formula,(lengths,mask,by_distance,by_formula)
        if by_distance:faces[mask.bit_count()-1].append(mask)
    computed=homology_from_faces(faces)
    expected=predicted_betti(lengths)
    if expected is not None:assert computed==expected,(lengths,computed,expected)
    print(f'petals={lengths}; vertices={len(g)}; nonempty_faces={sum(map(len,faces.values()))}; mod2_reduced_betti={computed}; prediction={expected}; PASS')

if __name__=='__main__':
    for p in ([4],[4,4],[4,5],[5,5],[4,6],[4,4,4],[4,4,4,4]):verify(p)
