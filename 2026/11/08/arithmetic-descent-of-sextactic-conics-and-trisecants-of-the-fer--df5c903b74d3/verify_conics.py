"""Exhaustive finite group-law enumeration of six-point sextactic conics.

Every eligible six-subset of E[6]\\E[3] is tested exactly once, and a
reducible conic is recognized by a partition into two collinear triples.
The program computes the complete Frobenius cycle profiles of both conic
sets for the three possible Frobenius actions on E[2] and E[3].
"""
from itertools import combinations, product
from collections import Counter

T = ((1, 0), (0, 1), (1, 1))
B = tuple(product(range(3), repeat=2))
S = tuple((t, b) for t in T for b in B)
index = {v:i for i,v in enumerate(S)}
assert len(S)==len(index)==27

def sum_zero(indices):
    return (sum(S[i][0][0] for i in indices)%2==0 and
            sum(S[i][0][1] for i in indices)%2==0 and
            sum(S[i][1][0] for i in indices)%3==0 and
            sum(S[i][1][1] for i in indices)%3==0)

six=[]; reducible=set()
for subset in combinations(range(27), 6):
    if not sum_zero(subset):
        continue
    six.append(subset)
    if any(sum_zero(triple) for triple in combinations(subset,3)):
        reducible.add(subset)
assert len(six)==8244
assert len(reducible)==2268
assert len(six)-len(reducible)==5976


def action(mode,P):
    t,b=P
    i=T.index(t)
    if mode=='split':return P
    if mode=='cyclic':return T[(i+1)%3],b
    if mode=='involution':return T[(0,2,1)[i]],(b[0],-b[1]%3)
    raise ValueError(mode)


def cycles(objects, fidx):
    all_set=set(objects)
    unseen=set(all_set);profile=Counter()
    def f(subset): return tuple(sorted(fidx[i] for i in subset))
    assert {f(s) for s in all_set}==all_set
    while unseen:
        first=next(iter(unseen));current=first
        length=0
        while True:
            assert current in unseen
            unseen.remove(current);length+=1
            current=f(current)
            if current==first:break
        profile[length]+=1
    return dict(profile)

expect={
 'split':({1:8244},{1:2268},{1:5976}),
 'cyclic':({1:36,3:2736},{1:36,3:744},{3:1992}),
 'involution':({1:76,2:4084},{1:54,2:1107},{1:22,2:2977}),
}
for mode in expect:
    fidx=tuple(index[action(mode,v)] for v in S)
    smooth=[s for s in six if s not in reducible]
    got=(cycles(six,fidx),cycles(reducible,fidx),cycles(smooth,fidx))
    assert got==expect[mode],(mode,got,expect[mode])
    print('CONICS_OK',mode,'all',got[0],'reducible',got[1],'smooth',got[2])
print('VERIFY_SEXTACTIC_CONICS_OK')
