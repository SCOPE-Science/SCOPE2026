#!/usr/bin/env python3
"""Exact checks of centered first-order Sobolev evaluation on unit-edge trees.
Only the Python standard library is required.
"""
from fractions import Fraction as F
from collections import deque
from itertools import product


def edges_from_prufer(code):
    k = len(code) + 2
    degree = [1] * k
    for a in code: degree[a] += 1
    edges = []
    for a in code:
        b = min(i for i in range(k) if degree[i] == 1)
        edges.append((a, b))
        degree[a] -= 1
        degree[b] -= 1
    u, v = [i for i in range(k) if degree[i] == 1]
    edges.append((u,v))
    return edges


def solve(A,b):
    n=len(b)
    A=[[F(t) for t in row]+[F(b[i])] for i,row in enumerate(A)]
    for j in range(n):
        p=next(i for i in range(j,n) if A[i][j])
        A[j],A[p]=A[p],A[j]
        z=A[j][j]
        A[j]=[x/z for x in A[j]]
        for i in range(n):
            if i!=j:
                z=A[i][j]
                A[i]=[x-z*y for x,y in zip(A[i],A[j])]
    return [row[-1] for row in A]


def q_green(edges,root):
    n=len(edges); N=n+1
    deg=[0]*N; L=[[0]*N for _ in range(N)]
    for u,v in edges:
        deg[u]+=1;deg[v]+=1
        L[u][u]+=1;L[v][v]+=1
        L[u][v]-=1;L[v][u]-=1
    b=[F(int(i==root)) - F(deg[i],2*n) for i in range(N)]
    h=[F(0)]+solve([row[1:] for row in L[1:]],b[1:])
    # Along a unit edge, g(t)=(1-t)h_u+t h_v-t(1-t)/(2n).
    # Integral is (h_u+h_v)/2 - 1/(12n).
    mean=sum(((h[u]+h[v])/2-F(1,12*n)) for u,v in edges)/n
    g_at_root=h[root]-mean
    # The explicit derivative is h_v-h_u+(2t-1)/(2n), so
    # its squared edge integral is (h_v-h_u)^2+1/(12 n^2).
    energy=sum((h[v]-h[u])**2+F(1,12*n*n) for u,v in edges)
    assert g_at_root == energy
    return g_at_root


def q_cuts(edges,root):
    n=len(edges); N=n+1
    adj=[[] for _ in range(N)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    parent=[-1]*N; parent[root]=root
    order=[root]
    for u in order:
        for v in adj[u]:
            if parent[v]<0:
                parent[v]=u;order.append(v)
    assert len(order)==N
    subtree=[0]*N
    for u in reversed(order[1:]):
        subtree[parent[u]] += subtree[u]+1
    s=[subtree[u] for u in order[1:]]
    return (F(n,3)+sum(t*(t+1) for t in s))/n**2


def main():
    tested=0; comparisons=0
    for N in range(2,8):
        if N<=5:
            codes=product(range(N),repeat=N-2)
        else:
            # Additional deterministically selected Prüfer codes of higher order.
            codes=([((7*i*i+3*i*j+j*j+N)%N) for j in range(N-2)] for i in range(90))
        for code in codes:
            edges=edges_from_prufer(code)
            n=N-1
            vals=[]
            for v in range(N):
                c=q_cuts(edges,v)
                g=q_green(edges,v)
                assert c==g, (edges,v,c,g)
                vals.append(c)
                comparisons+=1
            degrees=[sum(1 for a,b in edges if v in (a,b)) for v in range(N)]
            leaves=[i for i,d in enumerate(degrees) if d==1]
            sharp=max(vals)
            assert sharp==max(vals[v] for v in leaves)
            assert F(1)-F(2,3*n)<=sharp<=F(n,3)
            is_star=max(degrees)==n
            is_path=max(degrees)<=2
            if n>=3:
                assert (sharp==F(1)-F(2,3*n))==is_star
                assert (sharp==F(n,3))==is_path
            tested+=1
    print('EXACT_INDEPENDENT_QUADRATIC_GREEN_COMPARISONS_PASSED',comparisons)
    print('TREE_EXTREMAL_BOUNDS_AND_EQUALITY_CASES_PASSED',tested)
    print('ALL_UNIT_TREE_SOBOLEV_CHECKS_PASSED')

if __name__=='__main__': main()
