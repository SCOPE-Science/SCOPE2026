#!/usr/bin/env python3
"""Reproduce the dual-visibility classification and finite prism certificate.

Usage: python3 verify.py [prism_certificate.tsv]
No optional dependencies; all distances and independent visibility checks are computed
directly from graph adjacency.
"""
from collections import deque
from functools import lru_cache
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import sys

def graph(n, m):
    adj = [set() for _ in range(n*m)]
    for a in range(m):
        for i in range(n):
            u = a*n+i
            adj[u].update((a*n+(i-1)%n, a*n+(i+1)%n))
            adj[u].update(b*n+i for b in range(m) if b!=a)
    return [sorted(x) for x in adj]

def shortest(adj, start, end, forbidden=()):
    ban = set(forbidden) - {start, end}
    queue = deque([start])
    parent = {start: -1}
    while queue:
        u = queue.popleft()
        if u == end:
            path = [u]
            while parent[path[-1]] != -1:
                path.append(parent[path[-1]])
            return tuple(reversed(path))
        for v in adj[u]:
            if v not in ban and v not in parent:
                parent[v] = u
                queue.append(v)
    return None

def dual_test(adj, M):
    M = set(M)
    for u,v in combinations(range(len(adj)),2):
        if (u in M) != (v in M):
            continue
        ambient = shortest(adj,u,v)
        permitted = shortest(adj,u,v,M)
        if permitted is None or len(permitted)!=len(ambient):
            return False
    return True

def predicted(n,m):
    if n>=7:
        return set()
    pair = {
        frozenset((a*n+i,a*n+(i+1)%n))
        for a in range(m) for i in range(n)
    }
    if n==5:
        return pair
    four = {
        frozenset((a*n+i,a*n+(i+1)%6,b*n+(i+3)%6,b*n+(i+4)%6))
        for a in range(m) for b in range(a+1,m) for i in range(6)
    }
    return pair | four

def full_small():
    for n,m in ((5,1),(5,2),(5,3),(6,1),(6,2),(6,3),(7,1),(7,2)):
        adj=graph(n,m); p=predicted(n,m); found=set()
        N=n*m
        for mask in range(1,1<<N):
            M = frozenset(i for i in range(N) if (mask>>i)&1)
            if dual_test(adj,M):
                found.add(M)
        assert found==p,(n,m,found^p)
        print("DIRECT_DUAL_SETS_OK",n,m,len(found))

def prism_witness_file(path):
    adj=graph(6,2); M={0,1,9,10}
    rows=[]
    for u,v in combinations(range(12),2):
        if (u in M)!=(v in M):
            continue
        ambient=shortest(adj,u,v)
        avoiding=shortest(adj,u,v,M)
        assert avoiding is not None and len(avoiding)==len(ambient)
        rows.append(f"{u}\t{v}\t{','.join(map(str,avoiding))}")
    assert len(rows)==34
    content="u\tv\tshortest_path\n"+"\n".join(rows)+"\n"
    if path is not None:
        assert Path(path).read_text("utf-8")==content
    for j in range(6):
        M2={0,1,6+j,6+(j+1)%6}
        assert dual_test(adj,M2)==(j==3)
    for j in range(5):
        adj5=graph(5,2)
        M2={0,1,5+j,5+(j+1)%5}
        assert not dual_test(adj5,M2)
    print("PRISM_34_EXPLICIT_SHORTEST_PATHS_OK")
    print("ALL_CROSS_LAYER_OFFSETS_OK")
    return content

def exact_cover_census(m):
    n=6
    universe=(1<<(n*m))-1
    sets=list(predicted(6,m))
    masks=sorted(sum(1<<i for i in z) for z in sets)
    by_vertex=[[] for _ in range(6*m)]
    for s in masks:
        for v in range(6*m):
            if (s>>v)&1:
                by_vertex[v].append(s)
    @lru_cache(None)
    def solve(left):
        if not left:return (0,1)
        # Choose first uncovered vertex; every unordered partition has one unique next class.
        v=(left&-left).bit_length()-1
        best=999999; ways=0
        for c in by_vertex[v]:
            if c&left!=c:continue
            k,w=solve(left^c)
            if k+1<best:
                best=k+1;ways=w
            elif k+1==best:
                ways+=w
        return best,ways
    return solve(universe)

def count_formula(m):
    if m%2==0:
        s=m//2
        return 3*s,comb(2*s,s)*factorial(s)**3
    s=m//2
    return 3*(s+1),2*comb(2*s+1,s)*factorial(s+1)**3

if __name__=="__main__":
    prism_witness_file(sys.argv[1] if len(sys.argv)>1 else None)
    full_small()
    for m in range(1,6):
        found=exact_cover_census(m)
        assert found==count_formula(m),(m,found,count_formula(m))
        print("OPTIMAL_PARTITIONS_OK",m,found[0],found[1])
    print("VERIFY_OK")
