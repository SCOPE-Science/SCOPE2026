"""Independent direct return-word enumeration for valuation words.
The domain and expected words are generated separately from the observed returns.
"""
from collections import Counter
from itertools import product


def valuation(t, b):
    v = 0
    while t % b == 0:
        t //= b
        v += 1
    return v


def make_word(b, q, N):
    return [valuation(t, b) % q for t in range(1, N+1)]


def expected(b, q, r):
    B = b**r
    interior = tuple(valuation(t, b) % q for t in range(1, B))
    return [tuple([r] + list(interior))] + [
        tuple([r] + list(interior) + [(r+s) % q] + list(interior))
        for s in range(1, q)]

cases = 0
samples = 0
for b, q in product(range(2, 9), range(2, 7)):
    a = make_word(b, q, 130000)
    for r in range(q):
        positions = [i for i, v in enumerate(a) if v == r]
        observed = [tuple(a[positions[j]:positions[j+1]]) for j in range(len(positions)-1)]
        possible = expected(b, q, r)
        assert set(observed).issubset(set(possible)), (b, q, r, len(observed))
        assert len(set(possible)) == q
        actual_types = {x: i for i,x in enumerate(possible)}
        labels = [actual_types[v] for v in observed]
        if r == 0:
            base_labels = labels
        else:
            assert labels == base_labels[:len(labels)], (b, q, r)
        cases += 1
        samples += len(observed)
print('PASS independent direct checker')
print('parameter triples:', cases)
print('consecutive-return samples:', samples)
print('all observed return words match theorem, all return-type sequences synchronize')
