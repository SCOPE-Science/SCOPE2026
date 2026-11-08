#!/usr/bin/env python3
"""Exact, dependency-free finite cross-check for VC traces of ultrametric spheres.

The theorem concerns ordinary, nonempty distance spheres (center not added for
positive radius). The checker independently generates all reduced unlabeled
rooted hierarchies on up to eight leaves and enumerates Boolean traces.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
from math import comb

LEAF = "*"


def partitions(n, low=1):
    if n == 0:
        yield ()
    for k in range(low, n+1):
        for tail in partitions(n-k, k):
            yield (k,)+tail


@lru_cache(None)
def trees(n):
    if n == 1:
        return (LEAF,)
    out = set()
    for sizes in partitions(n):
        if len(sizes) < 2:
            continue
        groups = Counter(sizes)
        options = [list(combinations_with_replacement(trees(s), count))
                   for s, count in sorted(groups.items())]
        for chosen in product(*options):
            children = tuple(sorted((c for group in chosen for c in group), key=repr))
            out.add(children)
    return tuple(sorted(out, key=repr))


def leaves(tree, path=()):
    if tree == LEAF:
        return [path]
    return [q for j, child in enumerate(tree) for q in leaves(child, path+(j,))]


def proper_prefix(a,b):
    k=0
    for x,y in zip(a,b):
        if x != y: break
        k+=1
    return k


def sphere_family(points):
    # Distances are H minus common-prefix lengths, giving a strict ultrametric.
    H=max(map(len,points))+1
    return {frozenset(j for j,y in enumerate(points)
                      if (0 if x==y else H-proper_prefix(x,y))==r)
            for x in points
            for r in {0} | {H-proper_prefix(x,y) for y in points if x!=y}}


def node_child_sizes(tree):
    if tree == LEAF: return 1, []
    sizes=[]; nodes=[]
    for child in tree:
        k, subnodes = node_child_sizes(child)
        sizes.append(k)
        nodes.extend(subnodes)
    return sum(sizes), [sizes]+nodes


def predicted_counts(tree):
    n,nodes=node_child_sizes(tree)
    if n==1: return (1,0,0,0)
    root=nodes[0]
    s2=comb(n,2) - (root[0]*root[1] if len(root)==2 else 0)
    s3=0
    for j, sizes in enumerate(nodes):
        if j==0 and len(root)==3: continue
        s3+=sum(a*b*c for a,b,c in combinations(sizes,3))
    return (1,n,s2,s3)


def direct_counts(tree):
    pts=leaves(tree)
    fam=sphere_family(pts)
    counts=[1,0,0,0,0]
    for k in range(1,min(4,len(pts))+1):
        for support in combinations(range(len(pts)), k):
            bitmasks={sum(1<<j for j,v in enumerate(support) if v in concept)
                      for concept in fam}
            counts[k] += (len(bitmasks)==(1<<k))
    return tuple(counts)


def check():
    cases=0; supports=0; shapes={}
    for n in range(1,9):
        shapes[n]=len(trees(n))
        for tree in trees(n):
            direct=direct_counts(tree)
            expected=predicted_counts(tree)
            assert direct[:4] == expected,(tree,direct,expected)
            assert direct[4] == 0,(tree,direct)
            cases+=1
            supports+=sum(comb(n,k) for k in range(1,min(4,n)+1))
    assert shapes == {1:1,2:1,3:2,4:5,5:12,6:33,7:90,8:261},shapes
    # Homogeneous trees: separate closed formulas.
    for b,h in ((2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(4,1),(4,2),(5,1)):
        def make(h):return LEAF if h==0 else tuple(make(h-1) for _ in range(b))
        tree=make(h)
        n=b**h
        predicted=predicted_counts(tree)
        explicit2=2*comb(n//2,2) if b==2 else comb(n,2)
        explicit3=0 if b==2 else comb(b,3)*sum(b**(t+3*(h-t-1)) for t in range(h))-(b**(3*h-3) if b==3 else 0)
        assert predicted == (1,n,explicit2,explicit3),(b,h,predicted)
        if n<=27:
            got=direct_counts(tree)
            assert got[:4] == predicted and got[4] == 0,(b,h,got,predicted)
    print("ULTRAMETRIC_SPHERE_TRACES_PASS",cases,"unlabeled hierarchies",supports,"support tests",shapes)

if __name__ == '__main__': check()
