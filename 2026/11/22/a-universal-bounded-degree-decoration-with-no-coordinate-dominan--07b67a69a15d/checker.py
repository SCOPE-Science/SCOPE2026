"""Exact finite-graph checks for the double-pendant spectral-mass construction."""
from fractions import Fraction

def adjacency(base_size, base_edges):
    n = 7*base_size
    M = [[0]*n for _ in range(n)]
    def add(i,j): M[i][j] = M[j][i] = 1
    for i,j in base_edges: add(7*i,7*j)
    for v in range(base_size):
        k=7*v
        for j in (1,2,3,4): add(k,k+j)
        add(k+3,k+5)
        add(k+4,k+6)
    return M

def rank_integer(M):
    A = [[Fraction(x) for x in row] for row in M]
    m=len(A); rank=0
    for j in range(m):
        pivot=next((i for i in range(rank,m) if A[i][j]),None)
        if pivot is None: continue
        A[rank],A[pivot]=A[pivot],A[rank]
        pv=A[rank][j]
        for i in range(rank+1,m):
            if A[i][j]:
                z=A[i][j]/pv
                for k in range(j,m): A[i][k]-=z*A[rank][k]
        rank+=1
    return rank

def eigenvectors(base_size, which):
    patterns={0:(0,1,-1,0,0,0,0),1:(0,0,0,1,-1,1,-1),-1:(0,0,0,1,-1,-1,1)}
    pattern=patterns[which]
    for v in range(base_size):
        out=[0]*(7*base_size)
        out[7*v:7*v+7]=pattern
        yield out

def matvec(M,v): return [sum(x*y for x,y in zip(row,v)) for row in M]

def dot(v,w): return sum(x*y for x,y in zip(v,w))

cases=[(1,[]),(2,[(0,1)]),(3,[(0,1),(1,2)]),(4,[(0,1),(1,2),(2,3)]),(4,[(0,1),(1,2),(2,3),(3,0)]),(5,[(0,1),(1,2),(2,3),(3,4),(1,4)])]
tests=0
for N,edges in cases:
    M=adjacency(N,edges)
    for eigenvalue in (0,1,-1):
        eig=list(eigenvectors(N,eigenvalue))
        for i,v in enumerate(eig):
            assert matvec(M,v)==[eigenvalue*x for x in v]
            for j,w in enumerate(eig):
                assert dot(v,w)==(2 if eigenvalue==0 else 4)*(i==j)
            tests+=1
        shifted=[[M[i][j]-(eigenvalue if i==j else 0) for j in range(7*N)] for i in range(7*N)]
        assert 7*N-rank_integer(shifted)==N, (N,eigenvalue)
        tests+=1
    for i in range(N):
        # The three normalized spectral projection diagonal weights at each vertex.
        e0=list(eigenvectors(N,0))[i]; ep=list(eigenvectors(N,1))[i]; em=list(eigenvectors(N,-1))[i]
        for j in range(7):
            got=(Fraction(e0[7*i+j]**2,2),Fraction(ep[7*i+j]**2,4),Fraction(em[7*i+j]**2,4))
            expected=((Fraction(1,2),0,0) if j in (1,2) else ((0,Fraction(1,4),Fraction(1,4)) if j in (3,4,5,6) else (0,0,0)))
            assert got==expected,(N,i,j,got,expected)
            tests+=1
print('PASS', tests, 'exact finite checks on decorated base graphs; infinite claim is proved independently.')
