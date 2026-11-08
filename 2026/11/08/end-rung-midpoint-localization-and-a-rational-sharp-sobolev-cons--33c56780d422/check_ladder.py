"""Reproduce exact arclength-Sobolev constants for unit-edge ladder graphs.

Python 3 standard library only. Forms a zero-row-sum Laplacian pseudoinverse
using rational Gaussian elimination. All integrations are exact on each edge.
"""
from fractions import Fraction as F


def inverse(M):
    n=len(M)
    A=[list(map(F, row))+[F(int(i==j)) for j in range(n)] for i,row in enumerate(M)]
    for j in range(n):
        p=next(i for i in range(j,n) if A[i][j])
        A[p],A[j]=A[j],A[p]
        v=A[j][j]; A[j]=[z/v for z in A[j]]
        for i in range(n):
            if i != j and A[i][j]:
                c=A[i][j]; A[i]=[a-c*b for a,b in zip(A[i],A[j])]
    return [row[n:] for row in A]


def compute(n):
    N=2*n
    edges=[(i,i+1) for i in range(n-1)]+[(n+i,n+i+1) for i in range(n-1)]+[(i,n+i) for i in range(n)]
    m=len(edges)
    L=[[F(0) for j in range(N)] for i in range(N)]
    for a,b in edges:
        L[a][a]+=1;L[b][b]+=1;L[a][b]-=1;L[b][a]-=1
    A=[[L[i][j]+F(1,N) for j in range(N)] for i in range(N)]
    Q=inverse(A)
    Q=[[Q[i][j]-F(1,N) for j in range(N)] for i in range(N)]
    R=[[Q[i][i]+Q[j][j]-2*Q[i][j] for j in range(N)] for i in range(N)]
    vf=[sum((R[v][a]+R[v][b])/2+(1-R[a][b])/6 for a,b in edges) for v in range(N)]
    peaks=[]
    for a,b in edges:
        c=m-1-m*R[a][b]
        assert c>=0
        delta=vf[b]-vf[a]
        t=F(1,2)+delta/(2*c) if c else F(0)
        t=max(F(0),min(F(1),t))
        peak=(1-t)*vf[a]+t*vf[b]+c*t*(1-t)
        peaks.append((peak,(a,b),t))
    pmax=max(x[0] for x in peaks)
    maximizers=[(e,t) for p,e,t in peaks if p==pmax]
    expected={((0,n),F(1,2)),((n-1,2*n-1),F(1,2))} if n>=3 else None
    if n>=3:assert set(maximizers)==expected,(n,maximizers)
    total=F(0)
    for i,(a,b) in enumerate(edges):
        for j,(c,d) in enumerate(edges):
            if i==j:
                integral=F(1,3)-(1-R[a][b])/6
            else:
                integral=(R[a][c]+R[a][d]+R[b][c]+R[b][d])/4+(1-R[a][b])/6+(1-R[c][d])/6
            total+=integral
    k=pmax/m-total/(2*m*m)
    formula=F(18*n**3-18*n**2-9*n+10,12*(3*n-2)**2)
    assert k==formula,(n,k,formula)
    return k, maximizers

if __name__=='__main__':
    for n in range(2,10):
        k,points=compute(n)
        print('n',n,'sharp_constant_squared',k,'maximizing_edge_count',len(points))
    print('EXACT_RATIONAL_LADDER_GREEN_CHECKS_PASSED 8 sizes, all edges, all edge pairs')
