#!/usr/bin/env python3
"""Independent exact short-odd-cycle census for token graphs."""
from itertools import combinations
from math import comb
from random import Random

def adj(n,edges):
    a=[set() for _ in range(n)]
    for u,v in edges:a[u].add(v);a[v].add(u)
    return a

def cycle_count(a,length):
    n=len(a);res=0
    for root in range(n):
        def walk(v,visited,depth):
            if depth==length:return int(root in a[v] and visited[1]<v)
            return sum(walk(w,visited+[w],depth+1) for w in a[v] if w>root and w not in visited)
        res+=walk(root,[root],1)
    return res

def odd_girth_count(a):
    for g in range(3,len(a)+1,2):
        c=cycle_count(a,g)
        if c:return (g,c)
    return (None,0)

def token_adj(a,k):
    nodes=list(combinations(range(len(a)),k));ids={x:i for i,x in enumerate(nodes)}
    b=[set() for _ in nodes]
    for i,S in enumerate(nodes):
        s=set(S)
        for u in S:
            for v in a[u]-s:
                T=tuple(sorted(s-{u}|{v}));b[i].add(ids[T])
    return b

def eulerian(n):
    row=[1]
    for m in range(2,n+1):
        row=[((i+1)*row[i] if i<len(row) else 0)+((m-i)*row[i-1] if i else 0) for i in range(m)]
    return row

def formula(n,k,g,c):
    E=eulerian(g-1)
    return c*sum(comb(n-g,k-h)*E[h-1] for h in range(1,g) if 0<=k-h<=n-g)

def test(n,edges,which=None):
    a=adj(n,edges);g,c=odd_girth_count(a)
    ks=which or range(1,n)
    for k in ks:
        b=token_adj(a,k)
        if g is None:
            # Verify bipartiteness using BFS rather than searching arbitrarily long odd cycles.
            color={}
            for root in range(len(b)):
                if root in color:continue
                color[root]=0;front=[root]
                for v in front:
                    for w in b[v]:
                        if w not in color:color[w]=1-color[v];front.append(w)
                        assert color[w]!=color[v]
            h,ct=None,0
        else:
            for j in range(3,g,2):assert cycle_count(b,j)==0,(n,k,j)
            h,ct=g,cycle_count(b,g)
        expected=0 if g is None else formula(n,k,g,c)
        assert (h,ct)==(g,expected),(n,edges,k,(g,c),(h,ct),expected)
    return len(ks)

def main():
    cases=0;ks=0
    families=[]
    for n in [3,4,5,6,7,8]:
        families.append((n,[(i,(i+1)%n) for i in range(n)],range(1,min(n,5))))
    families.extend([
       (6,[(0,1),(1,2),(2,3),(3,4),(4,0),(2,5)],range(1,6)),
       (7,[(0,1),(1,2),(2,3),(3,4),(4,0),(2,5),(5,6)],range(1,5)),
       (5,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)],range(1,5)),
       (7,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0),(0,5),(5,6),(6,0)],range(1,5)),
       (5,list(combinations(range(5),2)),range(1,5)),
       (6,list(combinations(range(6),2)),range(1,4)),
    ])
    for n,edges,r in families:
        ks+=test(n,edges,r);cases+=1
    rng=Random(2611)
    for n in (5,6,7):
        all_edges=list(combinations(range(n),2))
        for _ in range(9):
            edges=[e for e in all_edges if rng.random()<.40]
            ks+=test(n,edges,range(1,min(n,4)));cases+=1
    # full triple partition needs no independence assumption
    assert eulerian(4)==[1,11,11,1]
    assert eulerian(6)==[1,57,302,302,57,1]
    print('BASE_AND_TOKEN_ODD_GIRTH_EXHAUSTIVE_CYCLE_ENUMERATION_PASS', 'graph_instances=',cases,'token_cases=',ks)
    print('EULERIAN_ROWS_PASS')
    print('VERIFY_OK')
if __name__=='__main__': main()
