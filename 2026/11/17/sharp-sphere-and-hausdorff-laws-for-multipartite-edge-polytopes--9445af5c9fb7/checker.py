"""Reproducibility checks for the metric geometry of multipartite edge polytopes.
Uses exact rational arithmetic; optional scipy minimax checks run with --numeric.
The mathematical proof does not depend on finite testing.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
import sys

def compositions(n, start=1):
    if n == 0:
        yield ()
    else:
        for a in range(start, n+1):
            for rest in compositions(n-a, a):
                yield (a,) + rest

def metric_data(sizes):
    N=sum(sizes)
    A=max(sizes); B=N-A
    if 2*A <= N:
        c=[F(2,N)]*N
        R2=F(2)-F(4,N)
    else:
        c=[]
        for a in sizes:
            c.extend([F(1,A) if a==A else F(1,B)]*a)
        R2=F(2)-F(1,A)-F(1,B)
    D2=F(0) if A==1 else F(1,2)+F(1,B)
    return c,R2,D2

def expand_pairs(sizes):
    lab=[]
    for k,a in enumerate(sizes):lab.extend([k]*a)
    return lab,[(i,j) for i,j in combinations(range(len(lab)),2) if lab[i]!=lab[j]]

def run():
    profiles=0; contacts=0; projections=0; strict=0
    for N in range(3,13):
        for sizes in compositions(N):
            if len(sizes)<2:continue
            profiles+=1
            lab,edges=expand_pairs(sizes)
            c,R2,D2=metric_data(sizes)
            norm2=sum(x*x for x in c)
            assert F(2)-norm2==R2, (sizes,R2,norm2)
            A=max(sizes); B=N-A
            for i,j in edges:
                d2=F(2)+norm2-2*(c[i]+c[j])
                assert d2<=R2, (sizes,i,j,d2,R2)
                expected=(2*A<=N or (sizes[lab[i]]==A or sizes[lab[j]]==A))
                assert (d2==R2)==expected,(sizes,i,j,d2,R2)
                contacts+=int(expected)
                strict+=int(not expected)
            for i,j in combinations(range(N),2):
                if lab[i]!=lab[j]:continue
                b=N-sizes[lab[i]]
                target=[F(0)]*N;target[i]=target[j]=F(1)
                y=[F(0)]*N;y[i]=y[j]=F(1,2)
                for t in range(N):
                    if lab[t]!=lab[i]:y[t]=F(1,b)
                gap=sum((target[t]-y[t])**2 for t in range(N))
                assert gap==F(1,2)+F(1,b)
                assert gap<=D2
                for p,q in edges:
                    # (v-y) . (y-target) >= 0, projection condition
                    dot=(y[p]-target[p])+(y[q]-target[q])-sum(yy*(yy-xx) for yy,xx in zip(y,target))
                    assert dot>=0,(sizes,i,j,p,q,dot)
                projections+=1
    print(f'MULTIPARTITE_EDGE_METRIC_EXACT_PASS profiles={profiles} contact_edges={contacts} strictly_inner_edges={strict} missing_vertex_projections={projections}')

if __name__=='__main__':run()
