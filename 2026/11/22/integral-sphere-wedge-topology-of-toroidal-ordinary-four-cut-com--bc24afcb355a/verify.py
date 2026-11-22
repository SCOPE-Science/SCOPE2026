"""Exact local/cyclic collapse certificate for the ordinary four-cut complex of C4 x Cn.

No external dependencies. Run with Python 3. This verifies finite local
certificates; the all-n implication uses the locality argument in RESULT.md.
"""
import itertools
import math
from collections import defaultdict

PATS = [(((0, 0), (0, 1), (0, 2), (0, 3)), ((0, 0), (0, 1), (0, 3))), (((0, 0), (0, 1), (0, 2), (1, 0)), ((0, 0), (0, 2), (1, 0))), (((0, 0), (0, 1), (0, 2), (1, 1)), ((0, 0), (0, 2), (1, 1))), (((0, 0), (0, 1), (0, 2), (1, 2)), ((0, 0), (0, 2), (1, 2))), (((0, 0), (0, 1), (0, 2), (3, 0)), ((0, 0), (0, 2), (3, 0))), (((0, 0), (0, 1), (0, 2), (3, 1)), ((0, 0), (0, 2), (3, 1))), (((0, 0), (0, 1), (0, 2), (3, 2)), ((0, 0), (0, 1), (0, 2))), (((0, 0), (0, 1), (1, 0), (1, -1)), ((0, 0), (0, 1), (1, -1))), (((0, 0), (0, 1), (1, 1), (1, 2)), ((0, 0), (0, 1), (1, 2))), (((0, 0), (0, 1), (3, 0), (3, -1)), ((0, 0), (0, 1), (3, -1))), (((0, 0), (0, 1), (3, 1), (3, 2)), ((0, 0), (0, 1), (3, 2))), (((0, 0), (1, 0), (1, 1), (1, 2)), ((0, 0), (1, 0), (1, 2))), (((0, 0), (1, 0), (1, 1), (1, -1)), ((0, 0), (1, 1), (1, -1))), (((0, 0), (1, 0), (1, -2), (1, -1)), ((0, 0), (1, 0), (1, -2))), (((0, 0), (3, 0), (3, 1), (3, 2)), ((0, 0), (3, 0), (3, 2))), (((0, 0), (3, 0), (3, 1), (3, -1)), ((0, 0), (3, 1), (3, -1))), (((0, 0), (3, 0), (3, -2), (3, -1)), ((0, 0), (3, 0), (3, -2))), (((1, 0), (1, 1), (1, 2), (1, 3)), ((1, 0), (1, 1), (1, 3))), (((1, 0), (1, 1), (1, 2), (2, 0)), ((1, 0), (1, 2), (2, 0))), (((1, 0), (1, 1), (1, 2), (2, 1)), ((1, 0), (1, 2), (2, 1))), (((1, 0), (1, 1), (1, 2), (2, 2)), ((1, 0), (1, 1), (1, 2))), (((1, 0), (1, 1), (2, 0), (2, -1)), ((1, 0), (1, 1), (2, -1))), (((1, 0), (1, 1), (2, 1), (2, 2)), ((1, 0), (1, 1), (2, 2))), (((1, 0), (2, 0), (2, 1), (2, 2)), ((1, 0), (2, 0), (2, 2))), (((1, 0), (2, 0), (2, 1), (2, -1)), ((1, 0), (2, 1), (2, -1))), (((1, 0), (2, 0), (2, -2), (2, -1)), ((1, 0), (2, 0), (2, -2))), (((2, 0), (2, 1), (2, 2), (2, 3)), ((2, 0), (2, 1), (2, 3))), (((2, 0), (2, 1), (2, 2), (3, 0)), ((2, 0), (2, 2), (3, 0))), (((2, 0), (2, 1), (2, 2), (3, 1)), ((2, 0), (2, 2), (3, 1))), (((2, 0), (2, 1), (2, 2), (3, 2)), ((2, 0), (2, 1), (2, 2))), (((2, 0), (2, 1), (3, 0), (3, -1)), ((2, 0), (2, 1), (3, -1))), (((2, 0), (2, 1), (3, 1), (3, 2)), ((2, 0), (2, 1), (3, 2))), (((2, 0), (3, 0), (3, 1), (3, 2)), ((2, 0), (3, 0), (3, 2))), (((2, 0), (3, 0), (3, 1), (3, -1)), ((2, 0), (3, 1), (3, -1))), (((2, 0), (3, 0), (3, -2), (3, -1)), ((2, 0), (3, 0), (3, -2))), (((3, 0), (3, 1), (3, 2), (3, 3)), ((3, 0), (3, 1), (3, 3)))]


def connected_tetrahedra(n):
    N=4*n
    edges=set()
    for a in range(4):
        for j in range(n):
            u=a*n+j
            for b,k in [((a+1)%4,j),(a,(j+1)%n)]:
                v=b*n+k
                edges.add(tuple(sorted((u,v))))
    adj=[0]*N
    for u,v in edges:
        adj[u]|=1<<v
        adj[v]|=1<<u
    tetra=[]
    for t in itertools.combinations(range(N),4):
        target=sum(1<<v for v in t)
        seen=1<<t[0]
        while True:
            more=seen
            for v in t:
                if (seen>>v)&1:
                    more|=adj[v]&target
            if more==seen:
                break
            seen=more
        if seen==target:
            tetra.append(t)
    return tetra, adj


def in_cube(n, tet):
    cols={v%n for v in tet}
    return len(cols)==1 or (len(cols)==2 and any(
        (j+1)%n in cols and j in cols for j in cols))


def orbit_faces(n, pattern):
    for off in range(n):
        yield tuple(sorted(a*n+(j+off)%n for a,j in pattern))


def check_cyclic_collapses(n):
    tetra,adj=connected_tetrahedra(n)
    assert len(tetra)==73*n, (n,len(tetra))
    local={t for t in tetra if in_cube(n,t)}
    assert len(local)==37*n
    faces=defaultdict(set)
    for t in tetra:
        for f in itertools.combinations(t,3):
            faces[f].add(t)
    remaining=set(tetra)
    used_faces=set()
    for stage,(tet_pat,face_pat) in enumerate(PATS):
        ts=list(orbit_faces(n,tet_pat))
        fs=list(orbit_faces(n,face_pat))
        assert len(set(ts))==n and len(set(fs))==n, (n,stage)
        assert len(set(ts)&local)==0
        assert len(set(ts)&(set(tetra)-remaining))==0
        assert len(set(fs)&used_faces)==0
        for t,f in zip(ts,fs):
            assert f in tuple(itertools.combinations(t,3)), (n,stage,t,f)
            assert f not in used_faces
            assert faces[f]=={t}, (n,stage,t,f,len(faces[f]))
            # A chosen face has no coface besides t; so deleting it with t
            # is an elementary simplicial collapse in the actual complex.
        for t,f in zip(ts,fs):
            remaining.remove(t)
            used_faces.add(f)
            for g in itertools.combinations(t,3):
                faces[g].remove(t)
    assert remaining==local, (n,len(remaining),len(local))
    assert len(used_faces)==36*n
    # No removed triangle lies entirely in one two-column cube.
    assert all(not in_cube(n,f) for f in used_faces)
    return n,len(tetra),len(local),len(used_faces)


def det_bareiss(A):
    A=[list(row) for row in A]
    n=len(A)
    sign=1
    den=1
    for k in range(n-1):
        if not A[k][k]:
            swap=next((r for r in range(k+1,n) if A[r][k]), None)
            if swap is None:
                return 0
            A[k],A[swap]=A[swap],A[k]
            sign=-sign
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=A[i][j]*p-A[i][k]*A[k][j]
                assert z%den==0
                A[i][j]=z//den
        for i in range(k+1,n):
            A[i][k]=0
        den=p
    return sign*A[-1][-1]


def cube_local_matrix():
    n=8
    triangles=list(itertools.combinations(range(n),3))
    row_id={t:i for i,t in enumerate(triangles)}
    tetras=[]
    for t in itertools.combinations(range(n),4):
        seen={t[0]}
        while True:
            more=seen|{v for u in seen for v in t if (u^v).bit_count()==1}
            if more==seen:
                break
            seen=more
        if len(seen)==4:
            tetras.append(t)
    assert len(tetras)==38
    matrix=[[0]*len(tetras) for _ in triangles]
    pivot_vectors={}
    for j,t in enumerate(tetras):
        column=0
        for k in range(4):
            i=row_id[t[:k]+t[k+1:]]
            matrix[i][j]=(-1)**k
            column^=1<<i
        while column:
            i=column.bit_length()-1
            if i in pivot_vectors:
                column^=pivot_vectors[i]
            else:
                pivot_vectors[i]=column
                break
    assert len(pivot_vectors)==35
    rows=[0,1,2,3,4,6,7,8,9,11,12,13,15,16,18,21,22,23,24,26,27,28,30,31,33,36,37,38,40,41,43,46,47,49,52]
    cols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,36]
    d=det_bareiss([[matrix[i][j] for j in cols] for i in rows])
    assert abs(d)==1, d
    # The binary rank alone does not establish the rational rank.
    # Confirm it independently by exact rational row elimination.
    from fractions import Fraction
    R=[[Fraction(v) for v in row] for row in matrix]
    rank=0
    for col in range(len(tetras)):
        k=next((i for i in range(rank,len(R)) if R[i][col]!=0), None)
        if k is None:
            continue
        R[k],R[rank]=R[rank],R[k]
        z=R[rank][col]
        for i in range(rank+1,len(R)):
            if R[i][col]!=0:
                ratio=R[i][col]/z
                for j in range(col,len(tetras)):
                    R[i][j]-=ratio*R[rank][j]
        rank+=1
    assert rank==35
    # Unit minor means all nonzero Smith invariant factors are one.
    return len(triangles),len(tetras),rank,d

if __name__=='__main__':
    print('cube',cube_local_matrix())
    for n in range(6,14):
        t=check_cyclic_collapses(n)
        print('torus',*t,'betti3',3*n,'betti2',math.comb(4*n-1,3)-70*n)
    print('TOROIDAL_FOUR_CUT_VERIFIED')
