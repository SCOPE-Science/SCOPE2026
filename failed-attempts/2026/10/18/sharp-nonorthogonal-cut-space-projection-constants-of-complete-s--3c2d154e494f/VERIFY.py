#!/usr/bin/env python3
"""Exact-rational verification of split-graph cut projections."""
from fractions import Fraction as F

def invert(A):
    n = len(A)
    a = [[F(x) for x in A[i]] + [F(i == j) for j in range(n)] for i in range(n)]
    for c in range(n):
        pivot = next((r for r in range(c, n) if a[r][c]), None)
        if pivot is None:
            raise AssertionError('singular grounded graph Laplacian')
        a[c], a[pivot] = a[pivot], a[c]
        fac = a[c][c]
        a[c] = [z / fac for z in a[c]]
        for r in range(n):
            if r != c and a[r][c]:
                fac = a[r][c]
                a[r] = [v - fac*w for v, w in zip(a[r],a[c])]
    return [row[n:] for row in a]

def matmul(A, B):
    BT=list(zip(*B))
    return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in BT] for row in A]

def transpose(A):
    return [list(col) for col in zip(*A)]

def check(m,n):
    N=m+n
    edges=[(i,j) for i in range(m) for j in range(i+1,m)] + [(i,m+u) for i in range(m) for u in range(n)]
    E=len(edges)
    B=[[F(int(v==a)-int(v==b)) for a,b in edges] for v in range(N-1)]
    Q=matmul(transpose(B),matmul(invert(matmul(B,transpose(B))),B))
    denominator=2*n*(N-1)+(m-1)*(m+2*n-2)
    t=F((m-2)*(n-1),denominator)
    T=[[F(0) for _ in range(E)] for _ in range(E)]
    for col,(i,j) in enumerate(edges):
        if j<m:
            p=[F(int(a==i)-int(a==j)) for a in range(m)]
            c=F(n,m*N)
        else:
            p=[F(int(a==i))-F(1,m) for a in range(m)]
            c=-F(1,N)
        for row,(a,b) in enumerate(edges):
            T[row][col]=c*(p[a]-p[b] if b<m else p[a])
    R=[[Q[i][j]+t*T[i][j] for j in range(E)] for i in range(E)]
    assert matmul(R,R)==R, 'projection idempotence'
    assert matmul(R,transpose(B))==transpose(B), 'range and identity on cut space'
    assert matmul(Q,R)==R, 'range inclusion'
    norm=max(sum((abs(R[i][j]) for i in range(E)),F(0)) for j in range(E))
    orth=max(sum((abs(Q[i][j]) for i in range(E)),F(0)) for j in range(E))
    predicted=F(2*(N-1)*(m*m+3*m*n-3*m-2*n+2),m*denominator)
    orth_predicted=F(2*m*m+3*m*n-3*m-2*n+2,m*N)
    gain=F((m-2)*(m-1)*(n-1)*(m+2*n-2),m*N*denominator)
    assert norm==predicted, (m,n,'norm',norm,predicted)
    assert orth==orth_predicted, (m,n,'orth',orth,orth_predicted)
    assert orth-norm==gain, (m,n,'gain',orth-norm,gain)
    aa_cols=list(range(m*(m-1)//2))
    ab_cols=list(range(len(aa_cols),E))
    aa_norms={sum((abs(R[i][j]) for i in range(E)),F(0)) for j in aa_cols}
    ab_norms={sum((abs(R[i][j]) for i in range(E)),F(0)) for j in ab_cols}
    assert aa_norms=={norm} and ab_norms=={norm}, (aa_norms,ab_norms)
    return E,t,norm,orth

if __name__=='__main__':
    count=columns=0
    for m in range(2,6):
        for n in range(2,6):
            E,t,lam,orth=check(m,n)
            count+=1;columns+=E
            print('PASS m=%d n=%d edges=%d t=%s min=%s orth=%s'%(m,n,E,t,lam,orth))
    print('ALL PASS configurations=%d columns=%d'%(count,columns))
