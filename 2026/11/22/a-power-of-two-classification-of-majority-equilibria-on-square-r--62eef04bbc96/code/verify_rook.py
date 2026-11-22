#!/usr/bin/env python3
"""Exact, standard-library-only checks of square-rook majority equilibria."""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import factorial
import json
import random


def conjugate(shape):
    n = len(shape)
    return tuple(sum(length >= j for length in shape) for j in range(1, n + 1))


def complement(shape):
    n = len(shape)
    return tuple(n - k for k in reversed(shape))


def antidual(shape):
    return conjugate(complement(shape))


def extend(shape):
    # Add an empty row and an occupied first column on all nonzero rows.
    return tuple((length + 1 if length else 0) for length in shape) + (0,)


@lru_cache(None)
def shapes(n):
    if n == 1:
        return frozenset({(0,), (1,)})
    zero_bottom = {extend(v) for v in shapes(n - 1)}
    nonzero_bottom = {antidual(v) for v in zero_bottom}
    assert all(v[-1] == 0 for v in zero_bottom)
    assert all(v[-1] > 0 for v in nonzero_bottom)
    assert not zero_bottom.intersection(nonzero_bottom)
    return frozenset(zero_bottom | nonzero_bottom)


def valid(shape):
    n = len(shape)
    col = conjugate(shape)
    return all((shape[i] + col[j] >= n + 1 if j < shape[i]
                else shape[i] + col[j] <= n - 1)
               for i in range(n) for j in range(n))


def partitions_in_square(n):
    def rec(k, m):
        if k == n:
            yield ()
        else:
            for v in range(m, -1, -1):
                for tail in rec(k + 1, v):
                    yield (v,) + tail
    return rec(0, n)


def label_multiplicity(shape):
    n = len(shape)
    counts1 = Counter(shape).values()
    counts2 = Counter(conjugate(shape)).values()
    a = factorial(n)
    b = factorial(n)
    for c in counts1: a //= factorial(c)
    for c in counts2: b //= factorial(c)
    return a * b


def directly_fixed(n, mask):
    # Independent neighbor-by-neighbor vote, without row/column sums.
    for i in range(n):
        for j in range(n):
            p = i * n + j
            old = (mask >> p) & 1
            ones = sum((mask >> (i * n + k)) & 1 for k in range(n) if k != j)
            ones += sum((mask >> (k * n + j)) & 1 for k in range(n) if k != i)
            new = 1 if ones > n - 1 else 0 if ones < n - 1 else old
            if new != old: return False
    return True


def ferrers_canonical(n, mask):
    rows = []
    for i in range(n):
        rows.append(tuple((mask >> (i * n + j)) & 1 for j in range(n)))
    rowdeg = [sum(row) for row in rows]
    coldeg = [sum(rows[i][j] for i in range(n)) for j in range(n)]
    order_i = sorted(range(n), key=lambda i:(-rowdeg[i],i))
    order_j = sorted(range(n), key=lambda j:(-coldeg[j],j))
    ordered = [[rows[i][j] for j in order_j] for i in order_i]
    shape = tuple(sum(row) for row in ordered)
    ferrers = all(ordered[i][j] == int(j < shape[i])
                  for i in range(n) for j in range(n))
    return ferrers, shape


def main():
    results = {'shape_counts':{},'labelled_fixed_counts':{}, 'direct_exhaustion':{},
               'shape_crosscheck':{}, 'random_n5':{}}
    for n in range(1, 11):
        s = shapes(n)
        assert len(s) == 2 ** n
        assert all(valid(v) for v in s)
        assert all(antidual(antidual(v)) == v for v in s)
        results['shape_counts'][str(n)] = len(s)
        results['labelled_fixed_counts'][str(n)] = sum(label_multiplicity(v) for v in s)
    for n in range(1, 9):
        alternatives = {p for p in partitions_in_square(n) if valid(p)}
        assert alternatives == shapes(n), (n,alternatives.symmetric_difference(shapes(n)))
        results['shape_crosscheck'][str(n)] = len(alternatives)
    for n in (2,3,4):
        count = 0
        for mask in range(1 << (n*n)):
            fixed = directly_fixed(n,mask)
            ferrers,shape = ferrers_canonical(n,mask)
            predicted = ferrers and shape in shapes(n)
            assert fixed == predicted, (n,mask,ferrers,shape)
            count += int(fixed)
        assert count == results['labelled_fixed_counts'][str(n)]
        results['direct_exhaustion'][str(n)] = {'states':1 << (n*n),'fixed':count}
    rng = random.Random(23117)
    n=5
    for _ in range(20000):
        mask = rng.getrandbits(n*n)
        fixed = directly_fixed(n,mask)
        ferrers,shape = ferrers_canonical(n,mask)
        assert fixed == (ferrers and shape in shapes(n))
    results['random_n5']={'tested':20000,'seed':23117,'all_agreed':True}
    with open('outputs/verification.json','w',encoding='utf-8') as f:
        json.dump(results,f,indent=2,sort_keys=True)
        f.write('\n')
    print(json.dumps(results,sort_keys=True))

if __name__=='__main__':main()
