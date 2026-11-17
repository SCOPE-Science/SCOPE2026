#!/usr/bin/env python3
"""Exact rational verification of clique-windmill Laplacian-simplex facet normal Gram matrices.

Run: python3 check_clique_windmill_angles.py
No third-party dependencies. Each test independently inverts L+J/n.
"""
from fractions import Fraction as F


def inverse(a):
    n=len(a)
    b=[[F(a[i][j]) for j in range(n)]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        j=next(j for j in range(k,n) if b[j][k])
        b[j],b[k]=b[k],b[j]
        d=b[k][k]
        b[k]=[v/d for v in b[k]]
        for i in range(n):
            if i!=k and b[i][k]:
                d=b[i][k]
                b[i]=[b[i][p]-d*b[k][p] for p in range(2*n)]
    return [line[n:] for line in b]


def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def check(s,m):
    n=1+s*m
    lap=[[F(0) for j in range(n)] for i in range(n)]
    for j in range(m):
        nodes=list(range(1+j*s,1+(j+1)*s))
        for v in nodes:
            lap[0][0]+=1;lap[v][v]+=1;lap[0][v]-=1;lap[v][0]-=1
        for a in range(s):
            for b in range(a+1,s):
                x,y=nodes[a],nodes[b]
                lap[x][x]+=1;lap[y][y]+=1;lap[x][y]-=1;lap[y][x]-=1
    J=F(1,n)
    U=inverse([[lap[i][j]+J for j in range(n)] for i in range(n)])
    Lplus=[[U[i][j]-J for j in range(n)] for i in range(n)]
    C=matmul(Lplus,Lplus)
    q=(F(1)-F(1,n**3))/(s*m)
    d=F(s+3,(s+1)**2)-q
    u=F(s+2,(s+1)**2)-q
    for i in range(n):
        for j in range(n):
            if i==0 and j==0: expected=F(n-1,n**3)
            elif i==0 or j==0: expected=-F(1,n**3)
            elif i==j: expected=d
            elif (i-1)//s==(j-1)//s: expected=u
            else: expected=-q
            assert C[i][j]==expected,(s,m,i,j,C[i][j],expected)
    if m==1:
        assert u==-F(1,n**3)
    else:
        assert q>0 and u>0 and d>q
        # cos(cross) is strictly larger than cos(hub) after squaring.
        assert q*q*F(n-1)*n**3>d
    return n*(n-1)//2


def main():
    tests=0
    ridge_checks=0
    for s in range(2,7):
        for m in range(1,6):
            ridge_checks+=check(s,m)
            tests+=1
    print(f'CLIQUE_WINDMILL_ANGLE_PASS exact_parameter_pairs={tests} all_ridges={ridge_checks} max_order=31')

if __name__=='__main__':
    main()
