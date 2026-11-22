#!/usr/bin/env python3
"""Reproduce finite checks for a restricted Rule-232 inverse-fiber theorem.

Standard-library-only; numbers denote cyclic indexed bits and true Boolean majority.
The infinite statements follow from the separate constructive proof, not these tests.
"""
from collections import Counter
from itertools import product
from functools import lru_cache

@lru_cache(None)
def nonshort_compositions(t):
    """Number of ordered decompositions of t into parts of size at least 3."""
    if t == 0:
        return 1
    if t < 0:
        return 0
    return sum(nonshort_compositions(t - h) for h in range(3, t+1))

def factor(gap):
    return 1 if gap == 2 else nonshort_compositions(gap - 2) if gap >= 5 else 0

def gaps(word):
    positions = [i for i, v in enumerate(word) if v]
    return [((positions[(j+1) % len(positions)]-positions[j]) % len(word)) or len(word)
            for j in range(len(positions))]

def admissible(word):
    return all(not(word[i] and word[(i + 1) % len(word)]) for i in range(len(word)))

def majority(word):
    n = len(word)
    return tuple(int(word[(i-1) % n] + word[i] + word[(i+1) % n] >= 2)
                 for i in range(n))

def predicted_nonzero(word):
    if not any(word):
        raise ValueError('requires nonzero word')
    result = 1
    for g in gaps(word):
        result *= factor(g)
    return result

# Counts of periodic zero-output predecessors (no cyclic 11 or 101).
def zero_fiber(n):
    if n in (1, 2):
        return 1
    vals = [0, 1, 1, 4]  # index 0 unused
    for j in range(4, n + 1):
        vals.append(vals[-1] + vals[-3])
    return vals[n]

def expected_counts(n):
    """Compute output/unique counts by a renewal recurrence with no word search."""
    max_g = n
    allowed = {2: 1, **{g: 1 for g in range(5, max_g+1)}}
    unique = {2: 1, 5: 1, 6: 1, 7: 1}
    def cycle_sum(weights):
        # Coefficient [z^n] of -log(1 - sum(weights[g] z^g)) times n.
        # For k ones, its count is (n/k)*[z^n] A(z)^k.
        a = [0] * (n+1)
        a[0] = 1
        result = 0
        for k in range(1, n+1):
            nxt = [0]*(n+1)
            for t in range(n+1):
                if a[t]:
                    for g,w in weights.items():
                        if t + g <= n:
                            nxt[t+g] += a[t]*w
            a = nxt
            if a[n]:
                assert n*a[n] % k == 0
                result += n*a[n]//k
        return result
    return 1 + cycle_sum(allowed), cycle_sum(unique) + int(n <= 2)

def check(n):
    observed = Counter()
    for word in product((0,1), repeat=n):
        if admissible(word):
            observed[majority(word)] += 1
    count = 0
    singleton = 0
    for y in product((0,1), repeat=n):
        actual = observed[y]
        if any(y):
            predicted = predicted_nonzero(y)
            assert actual == predicted, ('fiber', n, y, actual, predicted)
        else:
            predicted = zero_fiber(n)
            assert actual == predicted, ('zero fiber', n, actual, predicted)
        count += (actual > 0)
        singleton += (actual == 1)
    n_out, n_singletons = expected_counts(n)
    assert count == n_out, ('image count',n,count,n_out)
    assert singleton == n_singletons, ('singleton count',n,singleton,n_singletons)
    return count,singleton,observed[(0,)*n],sum(observed.values())

if __name__ == '__main__':
    for n in range(1, 16):
        print(f'n={n} image,singletons,zero-fiber,inputs={check(n)}')
    assert [factor(g) for g in range(2, 13)] == [1,0,0,1,1,1,2,3,4,6,9]
    print('VERIFY_OK: all cyclic inputs, all outputs, and renewal counts through length 15')
