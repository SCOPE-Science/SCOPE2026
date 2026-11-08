"""Exact, standalone support census for blowups of a quadric surface at points on one (1,1)-curve.
This uses a brute-force principal-submatrix test independent of the closed enumerator.
Run: python verify.py
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def predicted(n):
    from math import comb
    def mul(a,b):
        c=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): c[i+j]+=x*y
        return c
    def powpoly(c,m):return [comb(m,i)*c**i for i in range(m+1)]
    F=[0]*(n+2)
    for i,c in enumerate(powpoly(2,n)):F[i]+=2*c
    for i,c in enumerate(powpoly(1,n)):F[i]-=c
    for i,c in enumerate(powpoly(1,n-1)):F[i+2]+=n*c
    P=[0]*(n+2)
    for i,v in [(n-2,comb(n,2)),(n-1,2*n*n-n),(n,2*n*n+1),(n+1,n)]:P[i]+=v
    Z=mul(F,[1,1])
    for i,v in enumerate(P):Z[i+1]-=v
    while Z[-1]==0:Z.pop()
    return Z


def intersection_matrix(n):
    # Index scheme: E_0..E_(n-1), A_0..A_(n-1), B_0..B_(n-1), D.
    s=3*n+1; a=[[0]*s for _ in range(s)]
    for i in range(s):a[i][i]=2-n if i==3*n else -1
    for i in range(n):
        for j in range(n):
            a[i][n+j]=a[n+j][i]=int(i==j)
            a[i][2*n+j]=a[2*n+j][i]=int(i==j)
            a[n+i][2*n+j]=a[2*n+j][n+i]=int(i!=j)
        a[i][3*n]=a[3*n][i]=1
    return a


def is_negative_definite(matrix, indices):
    # Exact LDL of negative intersection matrix: every pivot must be strictly positive.
    m=len(indices)
    if not m:return True
    q=[[-matrix[indices[i]][indices[j]] for j in range(m)] for i in range(m)]
    for j in range(m):
        pivot=q[j][j]
        if pivot <= 0:return False
        for i in range(j+1,m):
            if q[i][j]:
                for k in range(i,m):
                    q[k][i]=q[i][k]=q[i][k]-Fraction(q[i][j]*q[k][j],pivot)
        for i in range(j+1,m):q[i][j]=q[j][i]=0
    return True


def brute(n):
    M=intersection_matrix(n);s=len(M)
    c=Counter()
    # Any positive off-diagonal pairing of two (-1)-curves forbids a support.
    # This filter is merely a speed-up; every surviving matrix is fully tested.
    forbidden=[0]*s
    for i in range(s):
        for j in range(i+1,s):
            if M[i][i]==M[j][j]==-1 and M[i][j]>=1:
                forbidden[i]|=1<<j
                forbidden[j]|=1<<i
    for mask in range(1<<s):
        indices=[];bits=mask;ok=True
        while bits:
            bit=bits&-bits;i=bit.bit_length()-1;bits-=bit
            if forbidden[i]&bits:ok=False;break
            indices.append(i)
        if ok and is_negative_definite(M,indices):c[len(indices)]+=1
    return [c.get(i,0) for i in range(s+1)]


if __name__=='__main__':
    for n in [3,4,5,6]:
        b=brute(n)
        while b[-1]==0:b.pop()
        f=predicted(n)
        assert b==f,(n,b,f)
        expected=4*3**n+(n-2)*2**n-(9*n*n-n+2)//2
        assert sum(b)==expected
        print(f'n={n}; curves={3*n+1}; exact_intersection_matrix_census={b}; chambers={sum(b)}; matches_closed_formula=YES')
    print('ALL_CHECKS_PASSED')
