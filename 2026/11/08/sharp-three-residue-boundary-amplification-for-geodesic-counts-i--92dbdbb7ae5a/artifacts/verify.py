#!/usr/bin/env python3
"""Exact finite checks for boundary amplification in independent-layer path graphs.
No external packages required.
"""
from fractions import Fraction
from collections import deque
from itertools import product


def layer_count(parts):
    n = sum(parts)
    w = 0
    for i in range(len(parts)):
        term = parts[i]
        for j in range(i+1, len(parts)):
            term *= parts[j]
            w += term
    for i, a in enumerate(parts):
        neighbor_count = (parts[i-1] if i else 0) + (parts[i+1] if i+1<len(parts) else 0)
        w += a*(a-1)//2*neighbor_count
    return n+w


def bfs_count(parts):
    # Counts undirected geodesics, including one trivial path per vertex.
    adj = []
    layer = []
    for i,a in enumerate(parts):
        for _ in range(a):
            layer.append(i)
            adj.append([])
    for u in range(len(layer)):
        for v in range(u):
            if abs(layer[u]-layer[v])==1:
                adj[u].append(v)
                adj[v].append(u)
    tot = len(layer)
    for u in range(len(layer)):
        dist = [-1]*len(layer)
        count = [0]*len(layer)
        dist[u] = 0
        count[u] = 1
        q=deque([u])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if dist[w]<0:
                    dist[w]=dist[v]+1
                    q.append(w)
                if dist[w]==dist[v]+1:
                    count[w]+=count[v]
        assert all(x>=0 for x in dist)
        tot += sum(count[u+1:])
    return tot


def H(parts):
    v=Fraction(3,2)
    for a in parts:
        v=a*v+Fraction(3-a,2)
    return v


def F(s):
    ans=[Fraction(3,2)]
    wins=[()]
    for n in range(1,s+1):
        v,x=max((t*ans[n-t]+Fraction(3-t,2), wins[n-t]+(t,)) for t in range(1,n+1))
        ans.append(v);wins.append(x)
    return ans,wins


def three_core(L,R,m):
    return list(L)+[3]*m+list(reversed(R))


def check():
    # First-principles shortest-path enumeration, independent of layer formula.
    for k in range(2,6):
        for parts in product(range(1,4),repeat=k):
            if sum(parts)>16:
                continue
            assert bfs_count(parts)==layer_count(parts), parts
    print('DIRECT_SHORTEST_PATH_BFS_OK all small positive layer profiles')

    f,w=F(90)
    for s in range(91):
        r=s%3
        if r==0 and s>=3: expected=Fraction(11,2)*3**((s-3)//3)
        elif r==1 and s>=7: expected=Fraction(47,2)*3**((s-7)//3)
        elif r==2 and s>=5: expected=Fraction(23,2)*3**((s-5)//3)
        else:continue
        assert f[s]==expected, (s,f[s],expected)
    for s in range(1,20):
        assert H(w[s])==f[s]
        assert sum(w[s])==s
    print('EXACT_BOUNDARY_RECURRENCE_OK 0..90')

    families={
        0:([1,2],[1,2],Fraction(121,4),Fraction(-9,4)),
        1:([1,2,2],[1,2,2],Fraction(529,4),Fraction(31,4)),
        2:([1,2],[1,2,2],Fraction(253,4),Fraction(11,4)),
    }
    for r,(L,R,A,C) in families.items():
        assert H(L)*H(R)==A
        for m in range(1,36):
            n=sum(L)+sum(R)+3*m
            assert n%3==r
            assert layer_count(three_core(L,R,m))==A*3**m+Fraction(33,2)*m+C
        print('EXACT_THREE_RESIDUE_FAMILY_OK',r,'n_min',sum(L)+sum(R)+3)

    # Every smaller tail profile, including all non-binary parts, is bounded
    # by the proposed residue-wise normalized envelope. We compare cubes to
    # avoid approximate roots (envelope is c_r * 3^(s/3)).
    for s in range(91):
        v=f[s]
        r=s%3
        if r==0: base=Fraction(11,2); k=s//3-1
        elif r==1: base=Fraction(47,2); k=(s-7)//3
        else:base=Fraction(23,2);k=(s-5)//3
        assert v <= base*Fraction(3)**k, (s,v)
    print('EXACT_MOD3_ENVELOPE_OK 0..90')
    print('VERIFY_OK')

if __name__=='__main__':check()
