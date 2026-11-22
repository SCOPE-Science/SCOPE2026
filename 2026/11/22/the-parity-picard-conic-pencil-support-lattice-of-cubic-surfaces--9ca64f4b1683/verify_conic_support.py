"""Exact standard-library reconstruction of cubic-surface conic-pencils.

Run: python3 verify_conic_support.py
All arithmetic is over the integers.  No computer algebra package is needed.
"""
from itertools import combinations
from collections import Counter


def line_classes():
    """Coordinates of H,E_1,...,E_6 in the blow-up lattice."""
    h=(1,0,0,0,0,0,0)
    e=[tuple(int(j==i+1) for j in range(7)) for i in range(6)]
    out=[]
    for i in range(6):
        out.append((f'E{i+1}', e[i]))
    for i,j in combinations(range(6),2):
        out.append((f'L{i+1}{j+1}', tuple(h[k]-e[i][k]-e[j][k] for k in range(7))))
    for i in range(6):
        out.append((f'Q{i+1}', tuple(2*h[k]-sum(e[j][k] for j in range(6) if j!=i) for k in range(7))))
    assert len(out)==27
    return out


def dot(a,b):
    return a[0]*b[0]-sum(a[i]*b[i] for i in range(1,7))


def matrix_rank_mod_p(mat,p):
    work=[[x%p for x in row] for row in mat]
    m=len(work); n=len(work[0]); rank=0
    for c in range(n):
        pivot=next((i for i in range(rank,m) if work[i][c]), None)
        if pivot is None: continue
        work[rank],work[pivot]=work[pivot],work[rank]
        inv=pow(work[rank][c], -1, p)
        work[rank]=[(inv*x)%p for x in work[rank]]
        for i in range(m):
            if i==rank or work[i][c]==0: continue
            z=work[i][c]
            work[i]=[(x-z*y)%p for x,y in zip(work[i],work[rank])]
        rank+=1
    return rank


def bareiss_det(matrix):
    """Integer-preserving fraction-free determinant with exact division."""
    m=[row[:] for row in matrix]
    n=len(m); prev=1; sign=1
    for k in range(n-1):
        if not m[k][k]:
            pivot=next((i for i in range(k+1,n) if m[i][k]),None)
            if pivot is None: return 0
            m[k],m[pivot]=m[pivot],m[k]; sign=-sign
        t=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=t*m[i][j]-m[i][k]*m[k][j]
                assert num%prev==0
                m[i][j]=num//prev
            m[i][k]=0
        prev=t
    return sign*m[-1][-1]


def verify():
    lines=line_classes(); classes=[v for _,v in lines]
    anti=(3,-1,-1,-1,-1,-1,-1)
    for v in classes:
        assert dot(v,v)==-1 and dot(anti,v)==1
    A=[[int(i!=j and dot(classes[i],classes[j])==1) for j in range(27)] for i in range(27)]
    assert all(dot(classes[i],classes[j]) in (0,1) for i in range(27) for j in range(27) if i!=j)
    assert A==[list(row) for row in zip(*A)]
    assert all(sum(row)==10 for row in A)
    # Verify each line supports exactly five disjoint reducible fibers;
    # the two components of a fiber meet and sum to -K - line.
    for i in range(27):
        adj=[j for j in range(27) if A[i][j]]
        pair=[]
        for j,k in combinations(adj,2):
            if A[j][k]:
                assert tuple(classes[j][t]+classes[k][t]+classes[i][t] for t in range(7))==anti
                pair.append((j,k))
        assert len(pair)==5 and sorted([x for p in pair for x in p])==sorted(adj)
        image=tuple(sum(classes[j][t] for j in adj) for t in range(7))
        assert image==tuple(5*(anti[t]-classes[i][t]) for t in range(7))
    A2=[[sum(A[i][k]*A[k][j] for k in range(27)) for j in range(27)] for i in range(27)]
    common=Counter((A[i][j], A2[i][j]) for i in range(27) for j in range(i+1,27))
    assert common==Counter({(1,1):135,(0,5):216}),common
    assert all(A2[i][j] == 5*int(i==j)-4*A[i][j]+5 for i in range(27) for j in range(27))
    det=bareiss_det(A)
    assert det==156250,(det, 156250)
    # Picard-map matrix has rows H,E1,...,E6.  It is surjective mod 5.
    pic=[[classes[j][i] for j in range(27)] for i in range(7)]
    assert matrix_rank_mod_p(pic,5)==7
    assert matrix_rank_mod_p(A,5)==20
    assert all(sum(pic[i][k]*A[k][j] for k in range(27))%5==0 for i in range(7) for j in range(27))
    # A's determinant is 2*5^7; the support image is contained in the
    # independent congruence kernel {coordinate sum=0 mod2, Pic=0 mod5}.
    assert abs(det)==2*5**7
    print('VERIFY_OK')
    print('line labels=27, conic pencils=27, reducible fibers per pencil=5')
    print('common-neighbor counts: meet=1 (135 pairs), skew=5 (216 pairs)')
    print('incidence determinant=156250; rank(mod 5)=20; Pic rank(mod 5)=7')
    print('cokernel=Z/10 plus (Z/5)^6; Smith factors=1^20,5^6,10')

if __name__ == '__main__':
    verify()
