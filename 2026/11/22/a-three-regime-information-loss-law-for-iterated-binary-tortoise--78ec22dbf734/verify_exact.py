"""Standalone exact check of binary tortoise iterates and all inverse fibers.
Scientific reproduction only; uses no external packages.
"""
from collections import Counter
from itertools import product
from math import comb


def recurse_tortoise(w):
    # Recursive Defant--Kravitz definition, not an iterate-gap formula.
    if not w:
        return w
    maximum = max(w)
    components = w.split(maximum)
    if len(components) == 1:
        return w
    transformed = [recurse_tortoise(s) for s in components]
    return transformed[0] + transformed[1] + maximum + ''.join(
        transformed[i] + maximum for i in range(2, len(transformed))
    )


def predicted_fiber(y, k):
    n = len(y)
    r = y.count('1')
    if k == 0:
        return 1
    if r <= k:
        return comb(n, r) if y == '0' * (n-r) + '1' * r else 0
    if not y.endswith('1' * k):
        return 0
    first = y.find('1')
    return comb(first+k, k)


def expected_histogram(n,k):
    if k == 0:
        return Counter({1:2**n})
    if k > n:
        k=n
    h = Counter()
    for r in range(k):
        h[comb(n,r)]+=1
    h[comb(n,k)]+=1
    for a in range(n-k):
        h[comb(a+k,k)]+=2**(n-k-a-1)
    return h


def check():
    inspections = 0
    for n in range(0,13):
        words = [''.join(w) for w in product('01',repeat=n)]
        images = words[:]
        for k in range(n+1):
            counts = Counter(images)
            expected = expected_histogram(n,k)
            assert Counter(counts.values()) == expected,(n,k,'spectrum')
            assert sum(counts.values()) == 2**n
            assert len(counts)==(2**n if k==0 else k+2**(n-k))
            for y,f in counts.items():
                assert f==predicted_fiber(y,k),(n,k,y,f)
            inspections += len(words)
            if k<n:
                images = [recurse_tortoise(w) for w in images]
    print(f'EXACT_OK n=0..12 all k=0..n, {inspections} (word,iteration) instances')
    print('checked complete image sets, every actual fiber and exact multiplicity histograms')

if __name__ == '__main__':
    check()
