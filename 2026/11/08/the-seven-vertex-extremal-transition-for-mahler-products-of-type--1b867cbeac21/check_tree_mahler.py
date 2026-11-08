"""Exact exhaustive certificate for type-B tree-root-polytope Mahler products.

Enumerates every labeled tree on 2..7 vertices through its unique Pruefer word.
Uses two independent subset recurrences for matchings and fence-poset linear
extensions; a canonical rooted-tree string groups the labeled results into
unlabeled classes. Also checks low-dimensional primal/polar convex-hull volumes.
"""
from functools import lru_cache
from itertools import product
from fractions import Fraction
from math import factorial
from collections import Counter, defaultdict
import heapq


def pruefer_edges(seq, n):
    d=[1]*n
    for v in seq:d[v]+=1
    leaves=[i for i in range(n) if d[i]==1];heapq.heapify(leaves)
    edges=[]
    for v in seq:
        u=heapq.heappop(leaves)
        edges.append((min(u,v),max(u,v)))
        d[u]-=1;d[v]-=1
        if d[v]==1:heapq.heappush(leaves,v)
    u=heapq.heappop(leaves);v=heapq.heappop(leaves)
    edges.append((min(u,v),max(u,v)))
    return tuple(sorted(edges))


def adj_matrix(edges,n):
    adj=[0]*n
    for u,v in edges:adj[u]|=1<<v;adj[v]|=1<<u
    return adj


def canonical_tree(edges,n):
    adj=adj_matrix(edges,n)
    @lru_cache(None)
    def rooted(u,parent):
        return '(' + ''.join(sorted(rooted(v,u) for v in range(n)
                    if (adj[u]>>v)&1 and v!=parent)) + ')'
    return min(rooted(i,-1) for i in range(n))


def matching_count(adj,n):
    @lru_cache(None)
    def f(mask):
        if not mask:return 1
        bit=mask&-mask;i=bit.bit_length()-1
        mask2=mask^bit
        return f(mask2)+sum(f(mask2^(1<<j)) for j in range(n)
                if (adj[i]>>j)&1 and (mask2>>j)&1)
    return f((1<<n)-1)


def linear_extensions(adj,n):
    # A tree is bipartite: orient edges from color-0 vertices to color-1 vertices.
    colors=[-1]*n;colors[0]=0;stack=[0]
    while stack:
        i=stack.pop()
        for j in range(n):
            if (adj[i]>>j)&1:
                if colors[j]==-1:colors[j]=1-colors[i];stack.append(j)
                else: assert colors[j]!=colors[i]
    pre=[0]*n
    for i in range(n):
        if colors[i]==1:pre[i]=adj[i]
    @lru_cache(None)
    def f(mask):
        if mask==(1<<n)-1:return 1
        return sum(f(mask | (1<<i)) for i in range(n)
                   if not (mask>>i)&1 and (pre[i]&mask)==pre[i])
    return f(0)


def verify_census():
    results={}
    for n in range(2,8):
        categories={};named={};count=0
        for word in product(range(n),repeat=n-2):
            edges=pruefer_edges(word,n);adj=adj_matrix(edges,n)
            M=matching_count(adj,n);L=linear_extensions(adj,n)
            shape=canonical_tree(edges,n)
            if shape in categories:
                assert categories[shape]==(M,L,M*L)
            else:categories[shape]=(M,L,M*L);named[shape]=edges
            count+=1
        assert count==n**(n-2)
        best=max(t[2] for t in categories.values())
        maximizers=[s for s,t in categories.items() if t[2]==best]
        print('dimension',n,'labeled',count,'unlabeled',len(categories),
              'max_numerator',best,'max_ratio',Fraction(best,factorial(n)),
              'maximizer_count',len(maximizers),
              'winner_edges',named[maximizers[0]])
        results[n]=(categories,named,maximizers)
    assert [len(results[n][0]) for n in range(2,8)]==[1,1,2,3,6,11]
    # Path is the unique maximum through n=6 among unlabelled trees;
    # n=2,3 are single-class cases.
    for n in range(2,7):
        pshape=canonical_tree(tuple((i,i+1) for i in range(n-1)),n)
        assert results[n][2]==[pshape]
    cats,named,max7=results[7]
    spider=((0,1),(0,2),(0,3),(1,4),(2,5),(3,6))
    sp=canonical_tree(spider,7)
    path=canonical_tree(tuple((i,i+1) for i in range(6)),7)
    assert max7==[sp],(max7,sp)
    assert cats[sp]==(20,288,5760)
    assert cats[path]==(21,272,5712)
    print('seven_tree_census:')
    for s,(m,l,q) in sorted(cats.items(),key=lambda t:(-t[1][2],t[0])):
        print(' ',s,'M',m,'L',l,'M*L',q,'ratio',Fraction(q,5040))
    print('EXACT_TREE_CENSUS_PASSED',sum(n**(n-2) for n in range(2,8)))


def hull_checks():
    import numpy as np
    from scipy.spatial import ConvexHull,HalfspaceIntersection
    examples={
       'P4':(4,[(0,1),(1,2),(2,3)]),
       'P5':(5,[(0,1),(1,2),(2,3),(3,4)]),
       'P6':(6,[(0,1),(1,2),(2,3),(3,4),(4,5)]),
       'S222':(7,[(0,1),(0,2),(0,3),(1,4),(2,5),(3,6)]),
    }
    for name,(n,edges) in examples.items():
        a=np.eye(n);pts=[]
        for i in range(n):pts.extend([a[i],-a[i]])
        for i,j in edges:
            for s,t in product((-1,1),repeat=2):pts.append(s*a[i]+t*a[j])
        pts=np.array(pts)
        primary=ConvexHull(pts).volume
        verts=HalfspaceIntersection(np.column_stack((pts,-np.ones(len(pts)))),
                                    np.zeros(n)).intersections
        dual=ConvexHull(verts).volume
        adj=adj_matrix(edges,n)
        M=matching_count(adj,n);L=linear_extensions(adj,n)
        targetp=2**n*M/factorial(n)
        targetd=2**n*L/factorial(n)
        assert abs(primary-targetp)<1e-6*max(1,targetp),(name,primary,targetp)
        assert abs(dual-targetd)<1e-6*max(1,targetd),(name,dual,targetd)
        print('hull',name,'primal',primary,'polar',dual,'vertices',len(pts),len(verts))
    print('INDEPENDENT_HULL_CHECKS_PASSED',len(examples))

if __name__=='__main__':
    verify_census()
    hull_checks()
