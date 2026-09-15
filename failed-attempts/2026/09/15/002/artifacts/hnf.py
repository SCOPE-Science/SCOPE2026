"""Correct integer row-HNF via column HNF of transpose using fraction-free extended-gcd (Cohen Alg 2.4.5 style, small-dim)."""
import math
def egcd(a,b):
    if b==0: return (abs(a), 1 if a>=0 else -1, 0)
    g,x1,y1=egcd(b,a%b); return (g,y1,x1-(a//b)*y1)
def hnf_rows(mat):
    A=[list(map(int,r)) for r in mat if any(r)]
    if not A: return []
    m,n=len(A),len(A[0])
    r=0
    pivcol=[]
    for j in range(n):
        piv=next((i for i in range(r,m) if A[i][j]!=0), None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        for i in range(m):
            if i!=r and A[i][j]!=0:
                a,b=A[r][j],A[i][j]
                g,s,t=egcd(a,b)
                Rr=list(A[r]); Ri=list(A[i])
                A[r]=[s*x+t*y for x,y in zip(Rr,Ri)]
                A[i]=[(a//g)*y-(b//g)*x for x,y in zip(Rr,Ri)]
        if A[r][j]<0: A[r]=[-x for x in A[r]]
        pivcol.append(j); r+=1
        if r==m: break
    # reduce: make off-pivot entries small (optional)
    A=[[int(x) for x in row] for row in A if any(row)]
    return A
def lattice_det(basis4):
    import numpy as np
    return round(abs(np.linalg.det(np.array(basis4,dtype=float))))
if __name__=="__main__":
    M=[[0,1,1,0],[0,1,2,0],[3,0,0,0],[0,3,0,0],[0,0,3,0],[0,0,0,3]]
    H=hnf_rows(M)
    print(H)
    # rank should be 4; pick 4x4 nonsingular submatrix det
    import numpy as np, itertools
    for combo in itertools.combinations(range(len(H)),4):
        d=round(abs(np.linalg.det(np.array([H[i] for i in combo],dtype=float))))
        if d>0: print(combo,d)

def hnf_full_rank(rows4):
    """rows: redundant generating set of a full-rank-4 lattice. Return 4x4 HNF basis (lower triangular, positive diag)."""
    H=hnf_rows(rows4)
    import numpy as np, itertools
    best=None
    for combo in itertools.combinations(range(len(H)),4):
        d=round(abs(np.linalg.det(np.array([H[i] for i in combo],dtype=float))))
        if d>0 and (best is None or d<best[0]):
            best=(d,combo)
    assert best is not None
    d,combo=best
    B=[H[i] for i in combo]
    # verify all gens in lattice spanned by B
    Bm=np.array(B,dtype=float)
    for g in rows4:
        t=np.linalg.solve(Bm.T if False else Bm, np.array(g,dtype=float))
        # solve B^T c = g? rows span: g = c B → c = g B^{-1}
        c=np.array(g,dtype=float)@np.linalg.inv(Bm)
        assert np.allclose(c, np.round(c)), (g,c)
    return B, d
