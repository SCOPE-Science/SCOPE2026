#!/usr/bin/env python3
"""Exact rational checks for two successive coordinate updates on regular graphs.
No packages beyond the Python standard library are used.
"""
from fractions import Fraction as F
from itertools import product

def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]

def mult(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def trans(A):
    return [list(row) for row in zip(*A)]

def quad(v,A):
    return sum((v[i]*A[i][j]*v[j] for i in range(len(v)) for j in range(len(v))),F(0))

def graphs():
    for n in range(3,9):
        yield 'cycle-'+str(n),n,[(i,(i+1)%n) for i in range(n)]
    for n in range(2,8):
        yield 'clique-'+str(n),n,[(i,j) for i in range(n) for j in range(i+1,n)]
    yield 'bipartite-3-3',6,[(i,j) for i in range(3) for j in range(3,6)]
    yield 'cube-3',8,[(i,i^(1<<b)) for i in range(8) for b in range(3) if i < (i^(1<<b))]
    # Petersen graph: outer 5-cycle, inner 5-star, 5 spokes.
    yield 'Petersen',10,[(i,(i+1)%5) for i in range(5)]+[(5+i,5+((i+2)%5)) for i in range(5)]+[(i,5+i) for i in range(5)]

def check():
    cases=0
    for name,n,edges in graphs():
        A=[[F(0) for j in range(n)] for i in range(n)]
        for i,j in edges:A[i][j]=A[j][i]=F(1)
        degrees=[sum(row) for row in A]
        assert len(set(degrees))==1, name
        d=int(degrees[0])
        for c in (F(1,10*d),F(1,2*d),F(3,4*d)):
            H=[[F(i==j)-c*A[i][j] for j in range(n)] for i in range(n)]
            P=[]
            for i in range(n):
                Z=eye(n)
                for j in range(n):Z[i][j]-=H[i][j]
                P.append(Z)
            # Exact Hessian-normalized expected squared-energy loss.
            D=[[F(0) for j in range(n)] for i in range(n)]
            for i,j in edges:
                for a,b in ((i,j),(j,i)):
                    T=mult(P[b],P[a])
                    E=mult(mult(trans(T),H),T)
                    for k in range(n):
                        for l in range(n):
                            D[k][l]+=(H[k][l]-E[k][l])/F(n*d)
            W=[[(F(2)+c*c)*F(i==j)+F(2)*c*A[i][j]/d for j in range(n)] for i in range(n)]
            theory=mult(mult(H,W),H)
            theory=[[x/n for x in row] for row in theory]
            assert D==theory,(name,c,'mean-loss-matrix')
            lam=F(1)-c*d
            best=lam*(F(2)+F(2)*c+c*c)/n
            e=[F(1) for _ in range(n)]
            assert quad(e,D)/quad(e,H)==best,(name,c,'constant-mode')
            # For every possible ordered pair, the constant-mode loss obeys
            # the global upper bound, with equality iff it is an edge.
            for i,j in product(range(n),repeat=2):
                T=mult(P[j],P[i])
                M=mult(mult(trans(T),H),T)
                drop=quad(e,H)-quad([sum((T[a][k]*e[k] for k in range(n)),F(0)) for a in range(n)],H)
                k=F(1) if i==j else (F(2)+F(2)*c+c*c if A[i][j] else F(2))
                assert drop==lam*lam*k,(name,c,i,j)
                assert drop/quad(e,H)<=best,(name,c,i,j,'bound')
                assert (drop/quad(e,H)==best)==bool(A[i][j]),(name,c,i,j,'equality')
            # The analytical eigenmode inequality, tested at spectrum-independent
            # rational a in [-d,d], follows from a nonnegative factorization.
            for h in range(25):
                a=F(d*(h-12),12)
                f=lambda t: (F(1)-c*t)*(F(2)+c*c+F(2)*c*t/d)
                factor=c*(d-a)/d * (d*c*c+F(2)*c*(d+a)+F(2)*(d-1))
                assert f(a)-f(d)==factor and factor>=0
            cases+=1
    print(f'PASS: {cases} graph/coupling cases, exact rational pair and matrix identities, spectra inequalities.')
if __name__=='__main__':check()
