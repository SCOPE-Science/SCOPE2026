"""Independent exhaustive enumeration of prescribed subsequence-complement fibers.
Run: python3 verify_exhaustive.py
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def expected(n, a, b):
    k = a + b
    if n < k - 1:
        return Counter(), 0
    h = Counter()
    h[1] += choose(n, k)
    if k == 2:
        h[n] += 1
    else:
        for t in range(1, n-k+3):
            h[t] += choose(n-t-1, k-3)
    return +h, choose(n+1, k)


def actual(n, a, b):
    w = '01' * n
    u = '0'*a + '1'*b
    fibers = defaultdict(int)
    positions = range(len(w))
    for ix in combinations(positions, len(u)):
        if ''.join(w[i] for i in ix) != u:
            continue
        deleted = set(ix)
        v = ''.join(ch for i, ch in enumerate(w) if i not in deleted)
        fibers[v] += 1
    return Counter(fibers.values()), sum(fibers.values()), fibers


def main():
    cases = 0
    checked = 0
    for n in range(1, 10):
        for a in range(1, n+3):
            for b in range(1, n+3):
                if a+b > 2*n+1:
                    continue
                observed, E, fibers = actual(n, a, b)
                wanted, Ew = expected(n, a, b)
                assert observed == wanted, (n,a,b,observed,wanted)
                assert E == Ew, (n,a,b,E,Ew)
                assert len(fibers) == choose(n,a+b)+choose(n-1,a+b-2)
                assert all(v.count('0')==n-a and v.count('1')==n-b for v in fibers)
                cases += 1
                checked += E
    print('COMPLEMENT_EXHAUSTIVE_OK', cases, 'parameter triples,', checked, 'embeddings')

if __name__ == '__main__':
    main()
