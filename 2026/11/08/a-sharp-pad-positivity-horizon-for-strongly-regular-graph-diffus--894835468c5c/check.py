#!/usr/bin/env python3
"""Exact rational replay of Padé graph-heat transition formulas.

Run: python3 check.py
Only Python's standard library is required.
"""
from fractions import Fraction as F
from itertools import combinations
from math import isqrt


def petersen():
    sets=list(combinations(range(5),2))
    return [[int(i!=j and not(set(a)&set(b))) for j,b in enumerate(sets)] for i,a in enumerate(sets)]

def triangular(n):
    sets=list(combinations(range(n),2))
    return [[int(i!=j and bool(set(a)&set(b))) for j,b in enumerate(sets)] for i,a in enumerate(sets)]

def rook(q):
    pts=[(i,j) for i in range(q) for j in range(q)]
    return [[int(i!=j and (a[0]==b[0] or a[1]==b[1])) for j,b in enumerate(pts)] for i,a in enumerate(pts)]

def shrikhande():
    pts=[(i,j) for i in range(4) for j in range(4)]
    steps={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
    return [[int(i!=j and ((b[0]-a[0])%4,(b[1]-a[1])%4) in steps)
             for j,b in enumerate(pts)] for i,a in enumerate(pts)]

def laplacian(A):
    n=len(A); k=sum(A[0]);
    return [[F(k if i==j else -A[i][j]) for j in range(n)] for i in range(n)]

def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]

def inv(A):
    n=len(A); rows=[[F(z) for z in A[i]]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        pivot=next((r for r in range(c,n) if rows[r][c]),None)
        assert pivot is not None
        rows[c],rows[pivot]=rows[pivot],rows[c]
        z=rows[c][c]; rows[c]=[v/z for v in rows[c]]
        for r in range(n):
            if r!=c and rows[r][c]:
                z=rows[r][c]; rows[r]=[rows[r][j]-z*rows[c][j] for j in range(2*n)]
    return [r[n:] for r in rows]

def spectral(A):
    n=len(A); deg=[sum(row) for row in A]
    assert len(set(deg))==1
    k=deg[0]; assert 0<k<n-1
    adj=set(); nonadj=set()
    for i in range(n):
        for j in range(i+1,n):
            c=sum(A[i][z]*A[j][z] for z in range(n))
            (adj if A[i][j] else nonadj).add(c)
    assert len(adj)==len(nonadj)==1
    lam,mu=adj.pop(),nonadj.pop()
    disc=(lam-mu)**2+4*(k-mu)
    rt=isqrt(disc); assert rt*rt==disc
    a=F(2*k-lam+mu-rt,2)
    b=F(2*k-lam+mu+rt,2)
    assert 0<a<b
    return n,k,lam,mu,a,b

def exact_step(L,h):
    n=len(L); L2=mm(L,L)
    den=[[F(12*(i==j))+6*h*L[i][j]+h*h*L2[i][j] for j in range(n)] for i in range(n)]
    num=[[F(12*(i==j))-6*h*L[i][j]+h*h*L2[i][j] for j in range(n)] for i in range(n)]
    return mm(inv(den),num)

def predicted_offdiag(edge,n,a,b,h):
    Da=12+6*a*h+a*a*h*h
    Db=12+6*b*h+b*b*h*h
    if edge:
        P=12+F(6)*a*b*h/n+a*b*(F(a+b,n)-1)*h*h
        return 12*h*P/(Da*Db)
    return 12*a*b*h*h*(6+(a+b)*h)/(n*Da*Db)

def run():
    cases=[('Petersen',petersen()),('Triangular_5',triangular(5)),('Triangular_6',triangular(6)),
           ('Triangular_7',triangular(7)),('Rook_3',rook(3)),('Rook_4',rook(4)),('Shrikhande',shrikhande())]
    count=0
    for name,A in cases:
        n,k,lam,mu,a,b=spectral(A)
        assert a+b==2*k-lam+mu
        assert a*b==n*mu
        assert (a+b<n)==(2*k-lam+mu<n)
        L=laplacian(A)
        for h in [F(1,10),F(1,2),F(1),F(2),F(4),F(10)]:
            T=exact_step(L,h)
            for i in range(n):
                assert sum(T[i])==1
                assert T[i][i]>0
                for j in range(n):
                    if i!=j:
                        assert T[i][j]==predicted_offdiag(A[i][j],n,a,b,h), (name,i,j,h)
                        if not A[i][j]: assert T[i][j]>0
                        count+=1
            signs={T[i][j]>0 for i in range(n) for j in range(n) if i!=j and A[i][j]}
            assert len(signs)==1
        print(name, 'N=',n,'alpha=',a,'beta=',b,'threshold=', 'finite' if a+b<n else 'unconditional')
    print('VERIFY_OK exact_offdiagonal_entries=',count)

if __name__=='__main__':run()
