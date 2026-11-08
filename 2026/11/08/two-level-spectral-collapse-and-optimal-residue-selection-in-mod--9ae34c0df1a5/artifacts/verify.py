#!/usr/bin/env python3
"""Exact independent finite checks of modulo-three Walsh sampling identities."""
from math import comb
from fractions import Fraction

T = (2, 1, -1, -2, -1, 1)
U = (0, 1, 1, 0, -1, -1)


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def spectral_check(H, n, t):
    M = 1 << n
    N = n + 1
    if abs(t) == 1:
        vals = [(M + 4*t)//3, (M + (1-3*n)*t)//3]
        mult = [n, 1]
    else:
        vals = [(M + 4*t)//3, (M + t)//3, (M + (4-3*n)*t)//3]
        mult = [n-1, 1, 1]
    # M*G has eigenvalues as integers in this residue-three setting.
    assert sum(v*m for v,m in zip(vals,mult)) == sum(H[i][i] for i in range(N))
    H2 = matmul(H,H)
    assert sum(v*v*m for v,m in zip(vals,mult)) == sum(H2[i][i] for i in range(N))
    A = [[H[i][j] for j in range(N)] for i in range(N)]
    for v in vals:
        A = matmul(A, [[H[i][j] - (v if i==j else 0) for j in range(N)] for i in range(N)])
    assert all(x == 0 for row in A for x in row)


def check_direct(n,r):
    M=1<<n
    k=(n-2*r)%6
    t,u=T[k],U[k]
    # Columns are 1 and the n Walsh characters (-1)^(x_i).
    H=[[0]*(n+1) for _ in range(n+1)]
    count=0
    for x in range(M):
        if x.bit_count()%3 != r:
            continue
        count+=1
        v=[1]+[1-2*((x>>i)&1) for i in range(n)]
        for i in range(n+1):
            for j in range(n+1):
                H[i][j] += v[i]*v[j]
    assert count == (M+t)//3
    for i in range(n+1):
        for j in range(n+1):
            predicted=count if i==j else (u if i==0 or j==0 else -t)
            assert H[i][j]==predicted, (n,r,i,j,H[i][j],predicted)
    spectral_check(H,n,t)
    return 1


def check_binomial(n,r):
    M=1<<n; k=(n-2*r)%6; t,u=T[k],U[k]
    def N(m,s):
        return sum(comb(m,j) for j in range(m+1) if (j-s)%3==0)
    assert N(n,r)*3==M+t
    assert N(n-1,r)-N(n-1,r-1)==u
    assert N(n-2,r)-2*N(n-2,r-1)+N(n-2,r-2)==-t
    if n>=5:
        if n%2==0:
            a=(M+3*n-1, M-4)
            b=(M+8,M-6*n+8)
        else:
            a=(M+4,M+1-3*n)
            b=(M+6*n-8,M-8)
        assert a[1]>0 and b[1]>0
        assert a[0]*b[1] < b[0]*a[1]
    return 1


def main():
    direct=sum(check_direct(n,r) for n in range(5,11) for r in range(3))
    exact=sum(check_binomial(n,r) for n in range(5,141) for r in range(3))
    # The boundary n=4 exceptional residue r=2 is singular.
    assert (16-6*4+8)==0
    print(f'MOD3_WALSH_SPECTRAL_VERIFY_PASS direct={direct} exact={exact}')

if __name__ == '__main__':
    main()
