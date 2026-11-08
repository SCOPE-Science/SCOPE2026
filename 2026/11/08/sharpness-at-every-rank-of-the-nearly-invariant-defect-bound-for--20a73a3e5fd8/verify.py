#!/usr/bin/env python3
"""Exact rational finite-matrix corroboration of the stated all-rank theorem.

This finite computation is not a proof for infinitely many perturbation ranks.
"""
from fractions import Fraction


def rank(matrix):
    if not matrix:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    nr, nc = len(a), len(a[0]); pivot_row=0
    for col in range(nc):
        pivot = next((i for i in range(pivot_row,nr) if a[i][col]),None)
        if pivot is None:
            continue
        a[pivot_row],a[pivot]=a[pivot],a[pivot_row]
        lead = a[pivot_row][col]
        a[pivot_row] = [v/lead for v in a[pivot_row]]
        for j in range(pivot_row+1,nr):
            if a[j][col]:
                coef = a[j][col]
                a[j] = [a[j][q]-coef*a[pivot_row][q] for q in range(nc)]
        pivot_row+=1
        if pivot_row==nr:
            break
    return pivot_row


def mm(a,b):
    return [[sum(a[i][t]*b[t][j] for t in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def run(r):
    N,k,h=8*r+8,3*r+3,5*r+5
    ai=[3*i+1 for i in range(1,r+1)]
    bi=[h+2*i for i in range(1,r+1)]
    assert 0<min(ai)<=max(ai)<h-1 and h<min(bi)<=max(bi)<N-1
    S=[[int(row==col+1) for col in range(N)] for row in range(N)]
    B=[[int(row+1==col) for col in range(N)] for row in range(N)]
    Tk=[[int(row==col+k) for col in range(N)] for row in range(N)]
    P=[[0]*N for _ in range(N)]
    for a,b in zip(ai,bi): P[k+a][b]=1
    T=[[Tk[row][col]-P[row][col] for col in range(N)] for row in range(N)]
    columns=[]
    for j in range(h,N):
        v=[0]*N;v[j]=1
        if j in bi: v[ai[bi.index(j)]]=1
        columns.append(v)
    M=[[v[row] for v in columns] for row in range(N)]
    J=[[int(row==col)-(int(row in ai and col==bi[ai.index(row)]) if row in ai else 0)
        for col in range(N)] for row in range(h)]
    assert rank(P)==r
    assert rank(T)==h
    assert rank(M)==k
    assert all(not v for v in M[0])
    assert all(x==0 for row in mm(T,M) for x in row)
    assert all(x==0 for row in mm(J,M) for x in row)
    assert rank(J)==h
    SstarM=mm(B,M)
    assert rank([[M[row][j] for j in range(k)]+[SstarM[row][j] for j in range(k)] for row in range(N)])==k+2*r+1
    assert rank(mm(J,SstarM))==2*r+1
    return N,k,2*r+1


if __name__=='__main__':
    for r in range(1,8):
        print('rank',r,'dimension, kernel, defect',*run(r))
    print('EXACT_MONOMIAL_TTO_SHARPNESS_OK')
