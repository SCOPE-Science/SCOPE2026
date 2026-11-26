#!/usr/bin/env python3
"""Exact-rational checks for Johnson-graph edge cut/cycle projections.
Uses only the Python standard library. The checks are finite tests, not a
substitute for the general mathematical proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def solve(matrix, target):
    """Solve a nonsingular rational system by pivoted elimination."""
    n = len(target)
    A = [[F(v) for v in row] + [F(target[i])]
         for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next((row for row in range(col, n) if A[row][col]), None)
        assert pivot is not None
        A[col], A[pivot] = A[pivot], A[col]
        scale = A[col][col]
        A[col] = [v / scale for v in A[col]]
        for row in range(n):
            if row == col or not A[row][col]:
                continue
            ratio = A[row][col]
            A[row] = [a - ratio*b for a,b in zip(A[row], A[col])]
    return [A[i][-1] for i in range(n)]


def expected(n, k):
    assert 3 <= k <= n//2
    q = F(k+1) - F(2,n) - F(k*(k-1),n-1)
    vertices = comb(n,k)
    effective_resistance = F(2*(vertices-1), vertices*k*(n-k))
    p = q + 1 - 2*effective_resistance
    return q,p,effective_resistance


def orbit_case(n,k):
    M = [[0]*k for _ in range(k)]
    weights = [comb(k-1,j)*comb(n-k-1,k-1-j) for j in range(k)]
    aa=[]; bb=[]
    for j in range(k):
        a = j*(n-2*k+j)
        b = (k-1-j)**2
        aa.append(a);bb.append(b)
        M[j][j]=n+a+b
        if j: M[j][j-1]=-a
        if j+1<k: M[j][j+1]=-b
    rhs=[0]*k;rhs[k-1]=1
    v=solve(M,rhs)
    assert all(x>0 for x in v)
    assert all(v[j]<v[j+1] for j in range(k-1))
    V = sum((weights[j]*v[j] for j in range(k)),F(0))
    T = sum((weights[j]*aa[j]*(v[j]-v[j-1]) for j in range(1,k)),F(0))
    Q = 2*(n-1)*V+2*T
    q,p,R=expected(n,k)
    assert V==F(1,n)
    assert T==F((k-1)*(n-k-1),2*(n-1))
    assert Q==q
    assert 2*v[-1]==R
    assert Q+1-4*v[-1]==p


def full_graph_case(n,k):
    verts=list(combinations(range(n),k))
    index={u:i for i,u in enumerate(verts)}
    N=len(verts)
    lap=[[0]*N for _ in range(N)]
    edges=[]
    for i,x in enumerate(verts):
        sx=set(x)
        for dropped in x:
            for inserted in range(n):
                if inserted in sx: continue
                y=tuple(sorted((sx-{dropped})|{inserted}))
                j=index[y]
                if i<j:
                    lap[i][i]+=1;lap[j][j]+=1
                    lap[i][j]-=1;lap[j][i]-=1
                    edges.append((i,j))
    A=index[tuple(range(k))]
    B=index[tuple(range(k-1))+(k,)]
    rhs=[0]*(N-1)
    if A<N-1:rhs[A]+=1
    if B<N-1:rhs[B]-=1
    u=solve([row[:N-1] for row in lap[:N-1]], rhs)+[F(0)]
    currents=[abs(u[i]-u[j]) for i,j in edges]
    q,p,R=expected(n,k)
    assert sum(currents,F(0))==q
    assert abs(u[A]-u[B])==R
    assert q+1-2*R==p
    return len(edges)


def main():
    orbit=0
    for n in range(6,56):
        for k in range(3,min(n//2,9)+1):
            orbit_case(n,k)
            orbit+=1
    edge_total=0
    full=[(6,3),(7,3),(8,3),(8,4),(9,3)]
    for n,k in full:
        edge_total += full_graph_case(n,k)
    print(f"JOHNSON_PROJECTION_EXACT_OK orbit_cases={orbit} full_graph_cases={len(full)} full_graph_edges={edge_total}")

if __name__=='__main__':
    main()
