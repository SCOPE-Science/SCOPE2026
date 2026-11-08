"""Exact rational tests for coordinate control on path-product networks.

Only the Python standard library is used. General claims are proved in RESULT.md;
these finite tests detect errors in the normalization and concrete examples.
"""
from fractions import Fraction as Q

def laplacian(n, edges):
    a = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i, j, w in edges:
        w = Q(w)
        a[i][i] += w
        a[j][j] += w
        a[i][j] -= w
        a[j][i] -= w
    return a

def path(n, weights=None):
    if weights is None: weights = [Q(1)] * (n-1)
    assert len(weights) == n-1
    return laplacian(n, [(i, i+1, weights[i]) for i in range(n-1)])

def triangle():
    # Edges 0--1, 0--2 of weight 1, and 1--2 of weight 2.
    return laplacian(3, [(0,1,1),(0,2,1),(1,2,2)])

def kron_sum(a,b,t=1):
    m,p = len(a),len(b)
    t=Q(t)
    c=[[Q(0) for _ in range(m*p)] for _ in range(m*p)]
    for i in range(m):
        for j in range(p):
            for k in range(m):
                c[i*p+j][k*p+j]+=a[i][k]
            for l in range(p):
                c[i*p+j][i*p+l]+=t*b[j][l]
    return c

def rank(matrix):
    if not matrix:return 0
    rows=[list(map(Q, r)) for r in matrix]
    h,w=len(rows),len(rows[0]); pivot=0
    for col in range(w):
        p=next((j for j in range(pivot,h) if rows[j][col]),None)
        if p is None:continue
        rows[pivot],rows[p]=rows[p],rows[pivot]
        s=rows[pivot][col]
        for k in range(col,w):rows[pivot][k]/=s
        for j in range(pivot+1,h):
            f=rows[j][col]
            if f:
                for k in range(col,w):rows[j][k]-=f*rows[pivot][k]
        pivot+=1
        if pivot==h:break
    return pivot

def controllability_rank(a,indices):
    n=len(a)
    vectors=[]
    for i in indices:
        v=[Q(0)]*n; v[i]=Q(1)
        for k in range(n):
            vectors.append(v)
            v=[sum(a[u][j]*v[j] for j in range(n)) for u in range(n)]
    return rank(list(zip(*vectors)))

def count_eigenspace_multiplicity_for_p3_triangle(t):
    # spectrum(P_3)={0,1,3}, spectrum(B)={0,3,5}.
    vals=[Q(a)+Q(t)*Q(b) for a in (0,1,3) for b in (0,3,5)]
    return max(vals.count(x) for x in vals)

def test():
    cases=0
    for n in (3,4,5):
        for t in (Q(1),Q(1,2),Q(2,3),Q(2)):
            a=kron_sum(path(n),path(n),t)
            # One boundary row, one fewer than its length.
            selected=[i*n for i in range(n-1)]
            got=controllability_rank(a,selected)
            assert got == n*n,(n,t,got)
            cases+=1
            if t==1:
                # Isotropic square: multiplicity n-1 makes fewer inputs impossible.
                bad=controllability_rank(a,selected[:-1])
                assert bad < n*n,(n,bad)
                cases+=1
    for t in (Q(1,3),Q(1),Q(2),Q(7,5)):
        a=kron_sum(path(3),triangle(),t)
        r=count_eigenspace_multiplicity_for_p3_triangle(t)
        selected=[i*3+1 for i in range(r)]
        assert controllability_rank(a,selected)==9,(t,r)
        cases+=1
        if r==2:
            assert controllability_rank(a,[1])<9
            cases+=1
    a=kron_sum(path(4,[1,2,3]),triangle(),Q(7,5))
    # This choice is generic for these two factors; a single anchored input suffices.
    assert controllability_rank(a,[1])==12
    cases+=1
    # The concrete triangle has eigenvectors (1,1,1),(-2,1,1),(0,1,-1).
    b=triangle()
    for ev,vec in [(0,[1,1,1]),(3,[-2,1,1]),(5,[0,1,-1])]:
        assert [sum(b[i][j]*vec[j] for j in range(3)) for i in range(3)]==[ev*x for x in vec]
        assert vec[1] != 0
        cases+=1
    print('VERIFY_OK exact_fraction_cases=',cases)

if __name__=='__main__':test()
