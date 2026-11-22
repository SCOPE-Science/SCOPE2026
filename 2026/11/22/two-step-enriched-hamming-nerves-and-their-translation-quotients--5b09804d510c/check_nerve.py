#!/usr/bin/env python3
"""Independent exact finite-field boundary checks for filtered distance-two nerves.

Usage: python3 check_nerve.py
No dependencies outside Python's standard library. Nondegenerate simplices are
ordered tuples with unequal consecutive vertices and total shortest-path
length at most 2; simplicial boundary omits a vertex with alternating sign.
"""
from itertools import product
from collections import deque
from math import comb


def hamming(d,q):
    V=list(product(range(q),repeat=d))
    adj=[set() for _ in V]
    for i,u in enumerate(V):
        for j,v in enumerate(V):
            if i<j and sum(x!=y for x,y in zip(u,v))==1:
                adj[i].add(j);adj[j].add(i)
    return adj


def cycle(n):
    adj=[set() for _ in range(n)]
    for i in range(n):
        adj[i].add((i+1)%n); adj[i].add((i-1)%n)
    return adj


def nerve_cells(adj):
    n=len(adj)
    dist=[[n+1]*n for _ in range(n)]
    for s in range(n):
        dist[s][s]=0; Q=deque([s])
        while Q:
            v=Q.popleft()
            for u in adj[v]:
                if dist[s][u]>dist[s][v]+1:
                    dist[s][u]=dist[s][v]+1;Q.append(u)
    c0=[(i,) for i in range(n)]
    c1=[(i,j) for i in range(n) for j in range(n) if i!=j and dist[i][j]<=2]
    c2=[(i,j,k) for j in range(n) for i in adj[j] for k in adj[j]]
    return [c0,c1,c2]


def rank_boundary(columns,row_index,p):
    pivots={}
    for cell in columns:
        vec={}
        for i in range(len(cell)):
            face=cell[:i]+cell[i+1:]
            if len(face)>1 and any(face[k]==face[k+1] for k in range(len(face)-1)):
                continue
            r=row_index[face]
            v=(vec.get(r,0)+(1 if i%2==0 else -1))%p
            if v:vec[r]=v
            else:vec.pop(r,None)
        while vec:
            r=min(vec)
            if r not in pivots:
                inv=pow(vec[r],-1,p)
                pivots[r]={k:v*inv%p for k,v in vec.items()}
                break
            a=vec[r]
            for k,v in pivots[r].items():
                t=(vec.get(k,0)-a*v)%p
                if t:vec[k]=t
                else:vec.pop(k,None)
    return len(pivots)


def check(adj,label,predicted=None):
    cells=nerve_cells(adj)
    n,a,b=map(len,cells)
    assert all(len(t)==3 for t in cells[2])
    assert b==sum(len(s)**2 for s in adj)
    # independently ensure all triangle boundaries vanish under d1
    for i,j,k in cells[2]:
        boundary=[((j,k),1),((i,k),-1),((i,j),1)]
        accum={}
        for (u,v),c in boundary:
            if u!=v:
                accum[u]=accum.get(u,0)-c
                accum[v]=accum.get(v,0)+c
        assert all(x==0 for x in accum.values())
    ranks=[]
    for prime in [2,3,5,1000003]:
        row_index={cell:i for i,cell in enumerate(cells[1])}
        r=rank_boundary(cells[2],row_index,prime)
        ranks.append(r)
    assert len(set(ranks))==1, (label,ranks)
    r=ranks[0]
    b1=a-(n-1)-r
    b2=b-r
    if predicted is not None:
        assert b1==0 and b2==predicted, (label,b1,b2,predicted)
    print(f'{label}: C=( {n}, {a}, {b} ), rank(d2)={r} over F2,F3,F5,F1000003, b1={b1}, b2={b2}', flush=True)


def main():
    for d,q in [(1,2),(1,3),(2,2),(2,3),(3,2),(3,3)]:
        expected=q**d*(d*(d+1)//2*(q-1)**2-d*(q-1)+1)-1
        check(hamming(d,q),f'H({d},{q})',expected)
    check(cycle(5),'C5 control')

if __name__=='__main__':main()
