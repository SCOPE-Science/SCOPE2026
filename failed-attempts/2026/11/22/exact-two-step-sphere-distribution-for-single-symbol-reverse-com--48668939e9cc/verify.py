#!/usr/bin/env python3
"""Independent exhaustive finite checks for the exact-two reverse-complement insertion spectrum.

The all-length proof is in RESULT.md; bounded tests here are independent regression checks.
"""
from collections import defaultdict
from itertools import combinations, product


def complement(q):
    assert q >= 2 and q % 2 == 0
    return tuple(i ^ 1 for i in range(q))


def insert_complement(word, i, comp):
    return word[:i + 1] + (comp[word[i]],) + word[i + 1:]


def descendants(word, comp):
    n = len(word)
    return {insert_complement(insert_complement(word, i, comp), j, comp)
            for i in range(n) for j in range(n + 1)}


def canonical_words(word, comp):
    n = len(word)
    candidates = {}
    for i, j in combinations(range(n), 2):
        candidates[('P', i, j)] = tuple(v for k, a in enumerate(word)
              for v in ((a, comp[a]) if k == i or k == j else (a,)))
    for i, a in enumerate(word):
        candidates[('A', i)] = word[:i] + (a, comp[a], a) + word[i+1:]
        candidates[('B', i)] = word[:i] + (a, comp[a], comp[a]) + word[i+1:]
    return candidates


def deficit(word, comp):
    result = 0
    i = 0
    previous = None
    while i < len(word):
        j = i + 1
        while j < len(word) and word[j] == word[i]:
            j += 1
        if previous is not None and word[i] == comp[previous]:
            result += j - i
        previous, i = word[i], j
    return result


def predicted_polynomials(q, nmax):
    prev = {0: q}  # n=1
    if nmax >= 1:
        yield 1, prev
    curr = {0: q*(q-1), 1: q}  # n=2
    if nmax >= 2:
        yield 2, curr
    for n in range(3, nmax + 1):
        out = defaultdict(int)
        for k, v in curr.items():
            out[k] += (q-1)*v
            out[k+1] += 2*v
        for k, v in prev.items():
            out[k+1] -= q*v
        prev, curr = curr, {k:v for k,v in out.items() if v}
        yield n, curr


class UnionFind:
    def __init__(self, keys): self.parent = {k:k for k in keys}
    def root(self, k):
        while self.parent[k] != k:
            self.parent[k] = self.parent[self.parent[k]]
            k = self.parent[k]
        return k
    def merge(self, a, b): self.parent[self.root(a)] = self.root(b)


def verify_rewrites(word, comp, candidates):
    n = len(word)
    uf = UnionFind(candidates)
    for i in range(n-1):
        if word[i+1] == comp[word[i]]:
            uf.merge(('A',i), ('A',i+1))
            j = i + 1
            while j + 1 < n and word[j] == comp[word[i]] and word[j+1] == comp[word[i]]:
                uf.merge(('P',i,j), ('A',j+1))
                j += 1
    by_output = defaultdict(list)
    for key, value in candidates.items(): by_output[value].append(key)
    for keys in by_output.values():
        assert len({uf.root(k) for k in keys}) == 1, ('missed rewrite', word, keys)
    assert len({uf.root(k) for k in candidates}) == len(by_output), ('spurious rewrite', word)


def check(q, maxlen):
    comp = complement(q)
    polynomials = dict(predicted_polynomials(q, maxlen))
    cases = 0
    for n in range(1, maxlen + 1):
        histogram = defaultdict(int)
        for x in product(range(q), repeat=n):
            actual = descendants(x, comp)
            predicted = n*(n+3)//2 - deficit(x, comp)
            assert len(actual) == predicted, ('formula', q, x, len(actual), predicted)
            candidates = canonical_words(x, comp)
            assert set(candidates.values()) == actual, ('candidate completeness', q, x)
            verify_rewrites(x, comp, candidates)
            histogram[n*(n+3)//2 - len(actual)] += 1
            cases += 1
        assert dict(histogram) == polynomials[n], ('generating polynomial', q, n, histogram, polynomials[n])
        print('PASS', 'q=',q, 'n=',n,'words=',q**n,'loss_polynomial=',sorted(histogram.items()))
    return cases


if __name__ == '__main__':
    cases = 0
    for q, m in ((2,11), (4,7), (6,5)):
        cases += check(q,m)
    print('ALL CHECKS PASSED; total sources:', cases)
