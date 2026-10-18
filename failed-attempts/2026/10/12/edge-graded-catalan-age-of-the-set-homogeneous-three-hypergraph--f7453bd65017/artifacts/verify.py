#!/usr/bin/env python3
"""Independent finite checks for the edge-graded age of an ordered C-set hypergraph.

Uses only the standard library. A plane full binary tree records the restriction of
an ordered two-regular C-relation; on a sorted triple, the edge is present iff
its leftmost leaf splits from the other two at their common ancestor.
"""
from functools import lru_cache
from collections import Counter
from itertools import combinations, permutations
from math import comb

CHECKS=0

def require(test, msg):
    global CHECKS
    CHECKS += 1
    if not test: raise AssertionError(msg)

@lru_cache(None)
def shapes(n):
    if n==1: return ('L',)
    return tuple((a,b) for k in range(1,n) for a in shapes(k) for b in shapes(n-k))

@lru_cache(None)
def leaves(tree):
    return 1 if tree=='L' else leaves(tree[0])+leaves(tree[1])

def is_edge(tree, i, j, k, first=0):
    """All indices are global in increasing order, 0<=i<j<k."""
    if tree=='L':raise AssertionError('triple in singleton')
    left,right=tree
    boundary=first+leaves(left)
    if k<boundary: return is_edge(left,i,j,k,first)
    if i>=boundary:return is_edge(right,i,j,k,boundary)
    if i<boundary<=j:return True
    if j<boundary<=k:return False
    raise AssertionError('uncovered triple split')

def edges(tree):
    return frozenset(t for t in combinations(range(leaves(tree)),3)
                     if is_edge(tree,*t))

def poly_tree_counts(n):
    return Counter(len(edges(s)) for s in shapes(n))

def polynomial_recursion(up_to):
    f={1: Counter({0:1})}
    for n in range(2,up_to+1):
        p=Counter()
        for a in range(1,n):
            b=n-a
            for e,x in f[a].items():
                for d,y in f[b].items():
                    p[e+d+a*comb(b,2)] += x*y
        f[n]=p
    return f

def canon_hypergraph(edge_set,n):
    triples=list(combinations(range(n),3))
    ind={t:i for i,t in enumerate(triples)}
    best=None
    for perm in permutations(range(n)):
        encoded=0
        for t in edge_set:
            mapped=tuple(sorted(perm[x] for x in t))
            encoded |= 1<<ind[mapped]
        if best is None or encoded<best: best=encoded
    return best

def run():
    polys=polynomial_recursion(11)
    for n in range(1,10):
        require(len(shapes(n))==comb(2*(n-1),n-1)//n, ('Catalan',n))
        p=poly_tree_counts(n)
        require(p==polys[n], ('independent tree and recurrence',n,p,polys[n]))
        require(sum(p.values())==len(shapes(n)), ('total',n))
        degree=comb(n,3)
        require(all(p.get(e,0)==p.get(degree-e,0) for e in range(degree+1)),
                ('palindromicity',n))
        require(max(p)==degree, ('maximum degree',n))
    for n in range(1,7):
        observed=[edges(t) for t in shapes(n)]
        require(len(set(observed))==len(observed), ('distinct ordered shapes',n))
        canon={canon_hypergraph(e,n) for e in observed}
        require(len(canon)==len(observed), ('unlabeled hypergraph types',n))
        print('n=%d, types=%d, sorted edge-count distribution=%s' %
              (n,len(canon),sorted(poly_tree_counts(n).items())))
    require(set(polys[5])==set(range(11))-{5},'five-world gap')
    require(sum(polys[6].values())==42,'six-world Catalan')
    require(set(polys[6])==set(range(comb(6,3)+1)),'six-world full-support base')
    for n in range(6,10):
        require(set(polys[n])==set(range(comb(n,3)+1)), ('full support',n))
    require(sum(polys[7].values())==132,'seven-world Catalan')
    # Tuple orbit count: partitions of coordinate positions into r equality
    # classes, bijection of these classes to ordered distinct points, and
    # a rooted planar full binary shape of those points.
    S=[[0]*9 for _ in range(9)]
    S[0][0]=1
    for n in range(1,9):
        for r in range(1,n+1): S[n][r]=S[n-1][r-1]+r*S[n-1][r]
    orbit=[]
    from math import factorial
    for n in range(1,9):
        count=sum(S[n][r]*factorial(r)*len(shapes(r)) for r in range(1,n+1))
        orbit.append(count)
        require(count>=factorial(n)*len(shapes(n)), ('tuple orbit lower bound',n))
    print('all tuple orbit counts (n=1..8):',orbit)
    print('VERIFY_OK',CHECKS,'exact assertions; exhaustive plane-tree shapes through n=9; permutation-isomorphism classification through n=6')

if __name__=='__main__':run()
