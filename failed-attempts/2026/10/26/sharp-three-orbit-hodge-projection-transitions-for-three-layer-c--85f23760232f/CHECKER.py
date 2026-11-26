"""Exact rational independent check of Hodge norm formulas for K_n Cartesian P_3.

Uses the reduced incidence Laplacian, not the analytical transfer-current formulas.
"""
from fractions import Fraction as F


def invert(M):
    n=len(M)
    T=[[F(M[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next(i for i in range(j,n) if T[i][j]!=0)
        T[j],T[k]=T[k],T[j]
        r=T[j][j]
        T[j]=[x/r for x in T[j]]
        for i in range(n):
            if i!=j and T[i][j]:
                r=T[i][j]
                T[i]=[x-r*y for x,y in zip(T[i],T[j])]
    return [row[n:] for row in T]


def check(n):
    N=3*n
    edges=[]
    types=[]
    for layer in range(3):
        for i in range(n):
            for j in range(i+1,n):
                edges.append((layer*n+i,layer*n+j))
                types.append('Hend' if layer in (0,2) else 'Hmid')
    for layer in range(2):
        for i in range(n):
            edges.append((layer*n+i,(layer+1)*n+i))
            types.append('V')
    m=len(edges)
    B=[[F(0)]*m for _ in range(N-1)]
    for j,(u,v) in enumerate(edges):
        if u<N-1:B[u][j]=-1
        if v<N-1:B[v][j]=1
    L=[[sum(B[i][e]*B[j][e] for e in range(m)) for j in range(N-1)] for i in range(N-1)]
    Linv=invert(L)
    U=[[sum(Linv[i][k]*B[k][e] for k in range(N-1)) for e in range(m)] for i in range(N-1)]
    Q=[[sum(B[k][i]*U[k][j] for k in range(N-1)) for j in range(m)] for i in range(m)]
    h_e=F(2*(n*n+n-1),n*(n+1))
    h_m=F(2*(n*n+4*n-3),n*(n+3))
    v=F(3*n-1,n+1)
    c_e=F(3*n*n+5*n-10,n*(n+3))
    c_m=F((n-1)*(3*n+10),n*(n+3))
    c_v=F(2*(n-1)*(2*n+5),(n+1)*(n+3))
    exp_q={'Hend':h_e,'Hmid':h_m,'V':v}
    exp_c={'Hend':c_e,'Hmid':c_m,'V':c_v}
    for j,category in enumerate(types):
        x=sum(abs(Q[i][j]) for i in range(m))
        y=sum(abs(F(i==j)-Q[i][j]) for i in range(m))
        assert x==exp_q[category],('cut',n,j,category,x,exp_q[category])
        assert y==exp_c[category],('cycle',n,j,category,y,exp_c[category])
    cut=max(exp_q.values())
    cycle=max(exp_c.values())
    assert cut == (h_m if n==2 else v)
    assert cycle == (c_m if n<=5 else c_v)
    print('PASS',n,'vertices',N,'edges',m,'cut',cut,'cycle',cycle)

if __name__=='__main__':
    for n in range(2,9):
        check(n)
