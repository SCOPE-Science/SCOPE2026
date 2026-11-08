#!/usr/bin/env python3
"""Verify minimum singleton rainbow labelings on crown graphs.

No external dependencies. 0 denotes an uncolored vertex, 1..k the service types.
"""
from itertools import combinations, product
from math import comb, factorial


def predicted(n, k):
    if n <= k:
        return 2*n, k**(2*n)
    base = comb(n, k)*factorial(k)**2
    if n > 2*k:
        return 2*k, base
    s = 2*k-n
    return 2*k, base + 2*comb(k,s)*(factorial(n)//(2**(n-k)))*k**s


def valid(labels, n, k):
    palette = set(range(1,k+1))
    for i in range(n):
        if labels[i] == 0 and not palette.issubset(
            labels[n+j] for j in range(n) if i != j
        ):
            return False
        if labels[n+i] == 0 and not palette.issubset(
            labels[j] for j in range(n) if i != j
        ):
            return False
    return True


def structural_type(labels, n, k):
    if n <= k:
        return 'all' if all(labels) else None
    left = {i for i in range(n) if labels[i] != 0}
    right = {i for i in range(n) if labels[n+i] != 0}
    if len(left) == len(right) == k and left == right:
        if set(labels[i] for i in left) == set(range(1,k+1)) and set(labels[n+i] for i in right) == set(range(1,k+1)):
            return 'matched'
    for full_side in (0, 1):
        full = labels[n*full_side:n*(full_side+1)]
        opposite = labels[n*(1-full_side):n*(2-full_side)]
        if not all(full):
            continue
        s = 2*k-n
        if s < 0 or sum(bool(t) for t in opposite) != s:
            continue
        occurrences = {col: [i for i,v in enumerate(full) if v == col] for col in range(1,k+1)}
        if sorted(map(len, occurrences.values())) != [1]*s+[2]*(k-s):
            continue
        singles = {loc[0] for loc in occurrences.values() if len(loc)==1}
        if singles == {i for i,v in enumerate(opposite) if v}:
            return 'one_full'
    return None


def exhaustive(n,k):
    target,_ = predicted(n,k)
    classes = {}
    count = 0
    # Enumerate every configuration of weight at most the predicted minimum,
    # including infeasible smaller weights, directly from labelled supports.
    for weight in range(target+1):
        for supp in combinations(range(2*n),weight):
            for values in product(range(1,k+1),repeat=weight):
                labels=[0]*(2*n)
                for i,v in zip(supp,values):labels[i]=v
                if valid(labels,n,k):
                    assert weight==target, ('Unexpected lighter assignment',n,k,labels)
                    typ=structural_type(labels,n,k)
                    assert typ is not None, ('Unclassified minimum',n,k,labels)
                    count+=1
                    classes[typ]=classes.get(typ,0)+1
    exp=predicted(n,k)
    assert count==exp[1], ('Coefficient disagreement',n,k,count,exp)
    print('CROWN_OK',n,k,'min',target,'functions',count,'types',classes)


def arithmetic_check():
    for k in range(2,16):
        for n in range(k+1,5*k+1):
            w,v=predicted(n,k)
            assert w==2*k and v>=comb(n,k)*factorial(k)**2
            if n>2*k:assert v==comb(n,k)*factorial(k)**2
    print('EXACT_INTEGER_COUNT_BOUNDARIES_OK')


def main():
    for n,k in [(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2),
                (3,3),(4,3),(5,3),(6,3)]:
        exhaustive(n,k)
    arithmetic_check()
    print('VERIFY_OK')

if __name__=='__main__':
    main()
