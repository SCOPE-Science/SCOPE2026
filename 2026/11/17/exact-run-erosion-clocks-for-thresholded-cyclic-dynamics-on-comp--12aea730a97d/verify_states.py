"""Direct vertex-state validation of cyclic successor-contact clocks on cliques."""
from itertools import product
from collections import Counter
from math import comb, factorial


def update(x, q, h):
    m = [x.count(i) for i in range(q)]
    return tuple((v + (m[(v + 1) % q] >= h)) % q for v in x)


def formula(x, q, h):
    m = [x.count(i) for i in range(q)]
    a = [v >= h for v in m]
    if all(a):
        return 0, q
    clocks = []
    for i in range(q):
        if a[i] and not a[(i-1) % q]:
            length = 0
            while length < q and a[(i + length) % q]:
                length += 1
            clocks.append(length-1 + (m[(i-1) % q] > 0))
    return max(clocks, default=0), 1


def observed(x, q, h):
    seen = {}
    v = x
    while v not in seen:
        seen[v] = len(seen)
        v = update(v, q, h)
    return seen[v], len(seen)-seen[v]


if __name__ == '__main__':
    tested = 0
    for q in range(3, 7):
        for h in range(1, 4):
            for n in range(2, 8):
                counts = Counter()
                for x in product(range(q), repeat=n):
                    prediction = formula(x, q, h)
                    got = observed(x, q, h)
                    assert prediction == got, (q, h, n, x, prediction, got)
                    counts[got] += 1
                    tested += 1
                assert sum(counts.values()) == q**n
                sharp = (min(q-2, n-1) if h == 1
                         else min(q-1, (n-1)//h))
                assert max(t for t,p in counts) == sharp, (q,h,n,sharp,counts)
                assert all(p in (1,q) for _,p in counts)
    print('PASS vertex-state independent first-entry/period check')
    print('q=3..6, threshold=1..3, n=2..7; sharp cutoff tested')
    print('tested_configurations=',tested,sep='')
