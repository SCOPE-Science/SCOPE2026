#!/usr/bin/env python3
"""Exact, dependency-free check of the topology-only phylogenetic rescue cutoff.
No simulations or numerical root finding are used in the exhaustive part.
"""
from functools import lru_cache
from itertools import combinations
from fractions import Fraction
from collections import Counter
from pathlib import Path

LEAF=()

# Each branch of an unlabelled, rooted, unordered full binary tree is a child tuple.
# Subtrees are placed in canonical repr-order to avoid double-counting.
@lru_cache(maxsize=None)
def shapes(n):
    if n==1:
        return (LEAF,)
    return tuple(sorted({tuple(sorted((a,b),key=repr))
        for k in range(1,n)
        for a in shapes(k) for b in shapes(n-k)}, key=repr))

@lru_cache(maxsize=None)
def leaves(tree):
    if tree==LEAF: return 1
    return leaves(tree[0])+leaves(tree[1])

def profiles(tree, ancestors=()):
    if tree==LEAF: return [tuple(sorted(ancestors))]
    return profiles(tree[0],ancestors+(leaves(tree[0]),)) + profiles(tree[1],ancestors+(leaves(tree[1]),))

# The leaf's incoming branch is included once as size 1; other branches correspond
# to the descendant size of the subtree at the child endpoint.

def dominates(a,b):
    return len(a)>=len(b) and all(x<=y for x,y in zip(a,b))

def universal_by_dominance(tree):
    pr=profiles(tree)
    return [a for a in pr if all(dominates(a,b) for b in pr)]

# Independent exhaustive labelled generator: all subsets of labels are split,
# with the smallest label assigned to the first child, so each full binary
# rooted topology is counted once.
@lru_cache(maxsize=None)
def labelled_trees(labels):
    if len(labels)==1: return (labels[0],)
    first=labels[0]
    remaining=labels[1:]
    out=[]
    for k in range(len(labels)-1):
        for subset in combinations(remaining,k):
            a=tuple(sorted((first,)+subset))
            b=tuple(x for x in remaining if x not in subset)
            for left in labelled_trees(a):
                for right in labelled_trees(b):
                    out.append((left,right))
    return tuple(out)

def labeled_profiles(tree, path=()):
    if isinstance(tree,int): return [(tree,tuple(sorted(path)))]
    def sz(t): return 1 if isinstance(t,int) else sz(t[0])+sz(t[1])
    return labeled_profiles(tree[0],path+(sz(tree[0]),)) + labeled_profiles(tree[1],path+(sz(tree[1]),))

# The human-readable certificate enumerates every unlabelled shape and one
# dominance-maximal tip profile. Recompute it rather than trust a cached table.
def shape_notation(t):
    return '*' if t == LEAF else '('+','.join(shape_notation(child) for child in t)+')'

rows=['leaf_count\tshape_number\trooted_shape\tdominating_ascending_clade_sizes']
for n in range(2,8):
    for idx, t in enumerate(shapes(n), 1):
        winner=min(set(universal_by_dominance(t)))
        rows.append(f'{n}\t{idx}\t{shape_notation(t)}\t{",".join(map(str,winner))}')
actual=(Path(__file__).with_name('SHAPE_CERTIFICATE.tsv')).read_text(encoding='utf8')
assert actual == '\n'.join(rows)+'\n', 'Shape certificate does not match enumeration'

EXPECTED_SHAPES=(1,1,1,2,3,6,11)
EXPECTED_LABELLED=(1,1,3,15,105,945,10395)
for n in range(1,8):
    ts=shapes(n)
    assert len(ts)==EXPECTED_SHAPES[n-1], (n,len(ts))
    for t in ts:
        assert len(profiles(t))==n
        assert universal_by_dominance(t), (n,t)
    labelled=labelled_trees(tuple(range(n)))
    assert len(labelled)==EXPECTED_LABELLED[n-1], (n,len(labelled))
    for t in labelled:
        ps=[p for _,p in labeled_profiles(t)]
        assert any(all(dominates(a,b) for b in ps) for a in ps), (n,t)
    print(f'LEAVES={n} SHAPES={len(ts)} LABELLED={len(labelled)} UNIVERSAL_PROFILE=YES')

# Root split: on one side a five-leaf tree (a four-leaf balanced subtree plus
# a singleton); on the other a three-leaf tree (a cherry plus a singleton).
# Every branch has unit length.
PAIR=(LEAF,LEAF)
BAL4=(PAIR,PAIR)
LEFT5=(BAL4,LEAF)
RIGHT3=(PAIR,LEAF)
WITNESS=(LEFT5,RIGHT3)
assert leaves(WITNESS)==8
P=profiles(WITNESS)
assert Counter(P)==Counter({(1,2,4,5):4,(1,5):1,(1,2,3):2,(1,3):1})

def score(profile,q):
    return sum((q**(s-1) for s in profile),Fraction(0))

def rescue(profile,q):
    return q*score(profile,q)
for q, winner in [(Fraction(1,4),(1,2,3)),(Fraction(3,4),(1,2,4,5))]:
    vals={p:rescue(p,q) for p in P}
    assert all(vals[winner]>=v for v in vals.values())
    assert sum(vals[p]==vals[winner] for p in P)==Counter(P)[winner]
    print('WITNESS q=',q,'OPTIMAL_PROFILE=',winner,'GAIN=',vals[winner])

# Recompute expected PD independently using all 2^7 survival configurations for the other taxa.
# The topological expected PD equals the sum of one indicator per rooted edge.
# Here the focal species always survives; every other species survives with 1-q.

def label_leaves(t,counter):
    if t==LEAF: return next(counter)
    return (label_leaves(t[0],counter),label_leaves(t[1],counter))
LT=label_leaves(WITNESS,iter(range(8)))
# Edges = nonempty paths from root; get their descendant leaf sets independently.
def edge_descendants(t):
    d={}
    def walk(node,path=()):
        if isinstance(node,int):
            return frozenset((node,))
        a=walk(node[0],path+(0,)); b=walk(node[1],path+(1,))
        d[path+(0,)]=a;d[path+(1,)]=b
        return a|b
    walk(t)
    assert len(d)==14
    return list(d.values())

EDS=edge_descendants(LT)
def expected_pd(protected,q):
    other=[x for x in range(8) if x!=protected]
    total=Fraction(0)
    for mask in range(1<<7):
        survivors={protected}
        probability=Fraction(1)
        for bit,x in enumerate(other):
            if mask>>bit & 1:
                survivors.add(x);probability*=1-q
            else: probability*=q
        total+=probability*sum(bool(S.intersection(survivors)) for S in EDS)
    return total

PROF_BY_LEAF=dict(labeled_profiles(LT))
for q in (Fraction(1,4),Fraction(3,4)):
    base=sum(Fraction(1)-q**len(S) for S in EDS)
    for x in range(8):
        assert expected_pd(x,q)-base == rescue(PROF_BY_LEAF[x],q)
    print('INDEPENDENT_SURVIVOR_ENUMERATION q=',q,'PASS')

# The difference in gain between a five-side deep leaf and a three-side deep
# leaf is q^3*(q^2+q-1), because the common terminal and cherry terms cancel.
# q^2+q-1 is strictly increasing on (0,1), and has sole zero (sqrt(5)-1)/2.
print('ALL EXACT CERTIFICATES PASSED')
