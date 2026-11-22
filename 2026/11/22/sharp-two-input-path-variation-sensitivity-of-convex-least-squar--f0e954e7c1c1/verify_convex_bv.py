#!/usr/bin/env python3
"""Exact-rational certificate for first-variation sensitivity of convex sequence projection.
No third-party packages are needed.  Run with Python 3.9 or later.
"""
from fractions import Fraction as F
from itertools import combinations


def ident(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def inverse(A):
    m = len(A)
    if m == 0:
        return []
    W = [list(map(F, A[i])) + ident(m)[i] for i in range(m)]
    for j in range(m):
        p = next(i for i in range(j, m) if W[i][j] != 0)
        W[j], W[p] = W[p], W[j]
        z = W[j][j]
        W[j] = [a/z for a in W[j]]
        for i in range(m):
            if i != j:
                z = W[i][j]
                W[i] = [a-z*b for a,b in zip(W[i],W[j])]
    return [r[m:] for r in W]


def matmul(A,B):
    if not A: return []
    if not B: return [[] for _ in A]
    return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]


def trans(A): return [list(x) for x in zip(*A)] if A else []


def mv(A,v): return [sum((a*b for a,b in zip(row,v)),F(0)) for row in A]


def matrices(n, active):
    D = [[F(-1 if k==i else 1 if k==i+1 else 0) for k in range(n)] for i in range(n-1)]
    B = [[F(1 if k==i or k==i+2 else -2 if k==i+1 else 0) for k in range(n)] for i in active]
    G = matmul(B,trans(B)) if B else []
    invG = inverse(G)
    P = ident(n)
    if B:
        corr = matmul(trans(B),matmul(invG,B))
        P = [[P[i][j]-corr[i][j] for j in range(n)] for i in range(n)]
    J = [[F(int(i>j)) for j in range(n-1)] for i in range(n)]
    T = matmul(D,matmul(P,J))
    return B,G,invG,P,T


def all_patterns(n):
    for k in range(n-1):
        for a in combinations(range(n-2),k):
            yield a


def curvature(x):
    return [x[i]-2*x[i+1]+x[i+2] for i in range(len(x)-2)]


def norm_v(x):
    return sum((abs(x[i+1]-x[i]) for i in range(len(x)-1)),F(0))


def witness(n,A,j,L):
    B,G,invG,P,T = matrices(n,A)
    x=[F(0),F(0)]
    for i in range(n-2):
        x.append(2*x[-1]-x[-2]+F(int(i not in A)))
    multiplier=[F(1)]*len(A)
    y=[v-sum((B[k][i] for k in range(len(A))),F(0)) for i,v in enumerate(x)]
    assert mv(P,y)==x
    assert curvature(x)==[F(int(i not in A)) for i in range(n-2)]
    h=[F(int(i>j)) for i in range(n)]
    eps=F(1,100)
    y2=[v+eps*q for v,q in zip(y,h)]
    x2=mv(P,y2)
    assert all(curvature(x2)[i]>0 for i in range(n-2) if i not in A)
    assert all(curvature(x2)[i]==0 for i in A)
    if A:
        shifted=[a-eps*b for a,b in zip(multiplier,mv(invG,mv(B,h)))]
        assert min(shifted)>0
        assert [a-b for a,b in zip(x2,y2)]==mv(trans(B),shifted)
    quotient=norm_v([a-b for a,b in zip(x2,x)])/norm_v([a-b for a,b in zip(y2,y)])
    assert quotient==L
    return y, y2, x, x2


def main():
    expected={2:F(1),3:F(1),4:F(6,5),5:F(4,3),6:F(7,5),7:F(28,19),8:F(11,7)}
    total_faces=0
    four_face_norms={}
    for n in range(2,9):
        best=F(-1); arg=None
        for A in all_patterns(n):
            total_faces+=1
            B,G,invG,P,T=matrices(n,A)
            # Independent identity checks on rational face projections
            assert matmul(P,P)==P
            assert mv(P,[F(1)]*n)==[F(1)]*n
            if n==4:
                four_face_norms[A]=max(sum((abs(T[i][j]) for i in range(n-1)),F(0)) for j in range(n-1))
            for j in range(n-1):
                val=sum((abs(T[i][j]) for i in range(n-1)),F(0))
                if val>best:
                    best=val;arg=(A,j)
        assert best==expected[n], (n,best,arg)
        A,j=arg
        witness(n,A,j,best)
        print('N',n,'SHARP',str(best),'ACTIVE',','.join(str(i+1) for i in A) or '-', 'STEP',j+1,'PASS')
    assert total_faces==127
    assert four_face_norms=={():F(1),(0,):F(7,6),(1,):F(7,6),(0,1):F(6,5)}
    print('FOUR_SITE_ALL_ACTIVE_FACES_EXACT_PASS')
    assert expected[3]==1 and expected[4]>1 and expected[8]>F(3,2)
    print('ALL_127_ACTIVE_FACES_AND_EXACT_WITNESSES_PASS')
    print('FIRST_EXPANSIVE_DIMENSION_FOUR_PASS')
    print('ABOVE_AFFINE_FACE_FACTOR_THREE_HALVES_AT_EIGHT_PASS')

if __name__=='__main__': main()
