#!/usr/bin/env python3
"""Independent exhaustive check of coordinate-class edge general position maximality.

Uses directly constructed independent-set flip graphs and graph BFS distances;
never uses the proof's constructive geodesics or assumed isometry.
"""
from collections import deque
from itertools import combinations
import random

def check(n, edge_mask):
    prs=list(combinations(range(n),2))
    adj=[0]*n
    for b,(i,j) in enumerate(prs):
        if edge_mask>>b&1:adj[i]|=1<<j;adj[j]|=1<<i
    verts=[x for x in range(1<<n) if all(not(x>>i&1 and adj[i]&x) for i in range(n))]
    ix={v:k for k,v in enumerate(verts)}
    nei=[[] for _ in verts]
    classes=[]
    for x in verts:
        for k in range(n):
            y=x^(1<<k)
            if x<y and y in ix:
                p,q=ix[x],ix[y]
                nei[p].append(q);nei[q].append(p)
                classes.append((p,q,k))
    ds=[]
    for s in range(len(verts)):
        d=[-1]*len(verts);d[s]=0
        todo=deque([s])
        while todo:
            u=todo.popleft()
            for v in nei[u]:
                if d[v]==-1:d[v]=d[u]+1;todo.append(v)
        assert all(t>=0 for t in d)
        ds.append(d)
    for i,j in prs:
        # A third-coordinate edge can be added iff no shortest path
        # traverses it and changes both coordinates i and j.
        is_maximal=True
        for u,v,k in classes:
            if k in (i,j):continue
            witness=False
            for s,x in enumerate(verts):
                for t,y in enumerate(verts):
                    if ((x^y)>>i&1) and ((x^y)>>j&1):
                        if (ds[s][u]+1+ds[v][t]==ds[s][t] or
                            ds[s][v]+1+ds[u][t]==ds[s][t]):
                            witness=True;break
                if witness:break
            if not witness:
                is_maximal=False;break
        triangle_edge=bool(adj[i]&adj[j]) if adj[i]>>j&1 else False
        if is_maximal != (not triangle_edge):
            raise AssertionError((n,edge_mask,prs[i] if False else (i,j),is_maximal,triangle_edge))
    return len(verts),len(classes),len(prs)

def main():
    checks=0;graphs=0;class_pairs=0;flips=0
    for n in (2,3,4,5):
        for mask in range(1<<(n*(n-1)//2)):
            v,e,p=check(n,mask);graphs+=1;class_pairs+=p;flips+=e
    rng=random.Random(20261106)
    # deterministic range including the n=5 complete and empty graphs
    for n,num in ((6,160),):
        m=n*(n-1)//2
        masks=[0,(1<<m)-1]
        for _ in range(num-2):masks.append(rng.randrange(1<<m))
        for mask in masks:
            v,e,p=check(n,mask);graphs+=1;class_pairs+=p;flips+=e
    print('VERIFY_OK graph_profiles=%d tested_pairs=%d tested_flip_edges=%d direct_BFS_geodesic_criterion=PASS triangle_edge_boundary=PASS'%(graphs,class_pairs,flips))
if __name__=='__main__':main()
