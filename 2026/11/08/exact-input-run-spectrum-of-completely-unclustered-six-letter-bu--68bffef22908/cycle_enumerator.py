"""Exact ordered-alphabet BWT-image enumeration at word length six.

An image L is accepted when its stable last-to-first permutation is a
single six-cycle and its consecutive symbols differ. The input cyclic-run
number equals the Hamming distance from L to its sorted rearrangement.
"""
from collections import Counter
from itertools import product

N = 6

def lf_permutation(last):
    counts = Counter(last)
    first_index = {}
    offset = 0
    for c in sorted(counts):
        first_index[c] = offset
        offset += counts[c]
    seen = Counter()
    result = []
    for c in last:
        result.append(first_index[c] + seen[c])
        seen[c] += 1
    return tuple(result)


def single_cycle(perm):
    if len(perm) != N:
        return False
    cur = 0
    reached = set()
    for _ in range(N):
        if cur in reached:
            return False
        reached.add(cur)
        cur = perm[cur]
    return cur == 0 and len(reached) == N


def census():
    records = {}
    for t in range(1, N + 1):
        alphabet = tuple(range(t))
        for last in product(alphabet, repeat=N):
            if len(set(last)) != t:
                continue
            if any(last[i] == last[i + 1] for i in range(N - 1)):
                continue
            if not single_cycle(lf_permutation(last)):
                continue
            runs = sum(a != b for a, b in zip(last, sorted(last)))
            records[(t, last)] = runs
    return records


def histogram():
    h = Counter()
    for (t, last), runs in census().items():
        h[t, runs] += 1
    return h


if __name__ == '__main__':
    print(sorted(histogram().items()))
