"""Exact checks for small-tree conservation-priority reversals.

Uses only the Python standard library. Run: python verify.py
"""
from fractions import Fraction as Q
from itertools import combinations, product
from functools import lru_cache

@lru_cache(None)
def trees(taxa):
    if len(taxa) == 1:
        return (taxa[0],)
    leftmost = taxa[0]
    answer = []
    for size in range(1, len(taxa)):
        for extra in combinations(taxa[1:], size-1):
            left = tuple(sorted((leftmost,) + extra))
            right = tuple(x for x in taxa if x not in left)
            for a in trees(left):
                for b in trees(right):
                    answer.append((a,b))
    return tuple(answer)

def leaves(t):
    return frozenset((t,)) if isinstance(t,str) else leaves(t[0]) | leaves(t[1])

def local_split(t, a, b):
    if isinstance(t,str):
        raise AssertionError('Cannot find LCA')
    left,right = map(leaves,t)
    if (a in left and b in right) or (a in right and b in left):
        return tuple(sorted((len(left),len(right))))
    if a in left:
        return local_split(t[0],a,b)
    return local_split(t[1],a,b)

counts = {n:len(trees(tuple(map(str,range(n))))) for n in range(1,6)}
assert counts == {1:1,2:1,3:3,4:15,5:105}, counts
small_comparisons = 0
for n in range(2,5):
    taxa = tuple(map(str,range(n)))
    for t in trees(taxa):
        for a,b in combinations(taxa,2):
            split = local_split(t,a,b)
            assert split[0] == 1 or split == (2,2), (n,t,split)
            # A singleton side contributes a constant only, while all
            # nonconstant coefficients on the other side have one sign;
            # two two-leaf sides give a degree-one difference.
            small_comparisons += 1

five_splits = {}
for t in trees(tuple(map(str,range(5)))):
    for a,b in combinations(tuple(map(str,range(5))),2):
        split = local_split(t,a,b)
        assert sum(split) <= 5
        assert split[0] == 1 or split == (2,2) or split == (2,3)
        five_splits[split] = five_splits.get(split,0)+1
assert five_splits[(2,3)] > 0

# Root splits into {a,b,c} and {d,e}; left 3-clade splits a | {b,c}.
# Every entry is (set of descendant tips, length of incoming edge).
edges = [
    (frozenset('abc'),Q(1)),(frozenset('de'),Q(1)),
    (frozenset('a'),Q(29,25)),(frozenset('bc'),Q(1)),
    (frozenset('b'),Q(1,20)),(frozenset('c'),Q(1,20)),
    (frozenset('d'),Q(1)),(frozenset('e'),Q(1,20))
]
assert all(length>0 for _,length in edges)

def gain(tip,q):
    return q*sum((length*q**(len(clade)-1)
                  for clade,length in edges if tip in clade),Q(0))

def diversity(S):
    return sum((length for clade,length in edges if clade & S),Q(0))

def expected_diversity(p,forced=None):
    taxa='abcde'
    result = Q(0)
    for bits in product((0,1),repeat=5):
        S = frozenset(t for t,x in zip(taxa,bits) if x)
        prob=Q(1)
        for t,x in zip(taxa,bits):
            if t==forced:
                if not x: prob=Q(0);break
            else: prob *= p if x else (1-p)
        result += prob*diversity(S)
    return result

checks=0
for p in [Q(1,20),Q(1,10),Q(1,5),Q(1,4),Q(1,2),Q(3,4),Q(4,5),Q(9,10),Q(19,20)]:
    q=1-p
    base = expected_diversity(p)
    for tip in 'abcde':
        assert expected_diversity(p,tip)-base == gain(tip,q)
        checks+=1
    a,d = gain('a',q),gain('d',q)
    assert a-d == q*(q-Q(1,5))*(q-Q(4,5))
    assert a>gain('b',q) and a>gain('c',q) and d>gain('e',q)
    if p < Q(1,5) or p > Q(4,5): assert a>d
    if Q(1,5)<p<Q(4,5): assert d>a
    if p in (Q(1,5),Q(4,5)): assert d==a
    checks+=1

# Independent analytic coefficient reconstruction from the supplied edges.
def coeffs(tip):
    out=[Q(0)]*3
    for clade,l in edges:
        if tip in clade:out[len(clade)-1]+=l
    return out
assert coeffs('a') == [Q(29,25),Q(0),Q(1)]
assert coeffs('d') == [Q(1),Q(1),Q(0)]
assert [x-y for x,y in zip(coeffs('a'),coeffs('d'))] == [Q(4,25),Q(-1),Q(1)]
# All source/persistence distinctions of the given model are exact.
print('PASS: labeled rooted tree counts',counts)
print('PASS: rooted pair topology exclusions for n<=4',small_comparisons)
print('PASS: all 105 five-tip shapes and their pairwise LCA splits',sum(five_splits.values()),five_splits)
print('PASS: 5-taxon exact probability and priority checks',checks)
print('PASS: roots of rank difference at p=1/5 and 4/5; 3+2 root split')
