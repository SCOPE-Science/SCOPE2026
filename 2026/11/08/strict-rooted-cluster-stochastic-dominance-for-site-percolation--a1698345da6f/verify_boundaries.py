#!/usr/bin/env python3
"""Independent exact certificate via connected rooted clusters and their vacant boundary.
For an exact root cluster U, U must be connected and occupied, and its exterior
vertex-neighbor set must be vacant; every other site is unrestricted.
Run with Python 3, standard library only.
"""
from math import comb
N=16

def adjacency_rook():
    out=[]
    for i in range(N):
        x,y=divmod(i,4); nbr=0
        for j in range(N):
            u,v=divmod(j,4)
            if i!=j and (u==x or v==y): nbr|=1<<j
        out.append(nbr)
    return out

def adjacency_shrikhande():
    out=[]
    for i in range(N):
        x,y=divmod(i,4); nbr=0
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)):
            j=4*((x+dx)%4)+(y+dy)%4
            nbr|=1<<j
        out.append(nbr)
    return out

def connected(U,adj):
    frontier=1; seen=1
    while frontier:
        bit=frontier & -frontier; frontier -= bit
        v=bit.bit_length()-1
        for w in range(N):
            nbit=1<<w
            if (adj[v]&nbit) and (U&nbit) and not(seen&nbit):
                seen|=nbit;frontier|=nbit
    return seen==U

def count_by_boundary(adj):
    out=[[0]*17 for _ in range(17)]
    for k in range(17):
        out[k][0]=comb(15,k)
    for U in range(1,1<<N,2):
        if not connected(U,adj):continue
        t=U.bit_count()
        neighborhood=0
        for v in range(N):
            if U & (1<<v):neighborhood|=adj[v]
        boundary=(neighborhood & ~U).bit_count()
        free=N-t-boundary
        assert 0<=free<=16
        for a in range(free+1):
            out[t+a][t]+=comb(free,a)
    for k in range(17):
        assert sum(out[k])==comb(16,k),(k,sum(out[k]))
    return out

if __name__=='__main__':
    R=count_by_boundary(adjacency_rook())
    S=count_by_boundary(adjacency_shrikhande())
    expectations={4:{3:-12,4:12},5:{3:-36,4:-24,5:60},
                  6:{3:-36,4:-48,5:-30,6:114},
                  7:{3:-12,4:-24,6:-6,7:42},8:{4:-6,8:6}}
    for k in range(17):
        for j in range(17):
            delta=S[k][j]-R[k][j]
            assert delta==expectations.get(k,{}).get(j,0),(k,j,delta)
    print('PASS: exact boundary-sum expansion of all connected root sets (17x17 histograms)')
