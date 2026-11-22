"""Direct state evolution, not using incidence or matrix-rank identities.
Run: python verify_states.py
"""
from itertools import combinations
from collections import Counter, defaultdict


def neighbors(n):
    edges = list(combinations(range(n), 2))
    out = [[] for _ in edges]
    for i, a in enumerate(edges):
        for j, b in enumerate(edges):
            if i != j and (len(set(a).intersection(b)) == 1 or
                           {a, b} == {(0, 1), (2, 3)}):
                out[i].append(j)
    return out


def nextstate(state, nbr):
    res = 0
    for i, adj in enumerate(nbr):
        v = 0
        for j in adj:
            v ^= (state >> j) & 1
        res |= v << i
    return res


def compute(n):
    nbr = neighbors(n)
    N = len(nbr)
    canonical = {}
    basin = Counter()
    periods = Counter()
    entries = Counter()
    for initial in range(1 << N):
        x = initial
        path = []
        seen = {}
        while x not in seen:
            seen[x] = len(path)
            path.append(x)
            x = nextstate(x, nbr)
        tau = seen[x]
        per = len(path) - tau
        entries[tau] += 1
        key = min(path[tau:])
        basin[key] += 1
        if tau == 0:
            canonical[key] = per
    for per in canonical.values():
        periods[per] += 1
    q = 2
    recurrent_dimension = n + 1 if n % 2 else 2
    if n % 2:
        fixed = q ** (n - 3)
        p2 = (q ** (n - 1) - fixed) // 2
        p4 = (q ** (n + 1) - q ** (n - 1)) // 4
        target = {1: fixed, 2: p2, 4: p4}
        cutoff = 1
        bound = {0:q**(n+1), 1:q**N}
    else:
        target = {1: q, 2:(q*q-q)//2}
        cutoff = 2 if n == 4 else 3
        bound = {0:q*q, 1:q**(N-n+2), 2:q**(N-(2 if n == 4 else 4)+2), 3:q**N}
    actual = {per:ct for per,ct in periods.items()}
    assert actual == target, (n, actual, target)
    assert max(entries) == cutoff, (n, entries)
    for t in range(cutoff + 1):
        assert sum(v for k,v in entries.items() if k <= t) == bound[t], (n,t,entries,bound)
    for key, size in basin.items():
        assert size == canonical[key] * q ** (N - recurrent_dimension), (n,key,size)
    assert sum(entries.values()) == 1 << N
    print('PASS n=%d, N=%d, %d initial states, entry=%s, primitive-orbits=%s' %
          (n, N, 1<<N, dict(sorted(entries.items())), dict(sorted(periods.items()))))


def four_ary_n4():
    n = 4
    nbr = neighbors(n)
    N = len(nbr)
    q = 4
    # Each F_4 value is two binary coefficients; adding values is XOR.
    values = range(q**N)
    seenstates = set()
    totals = Counter()
    for v in values:
        x = v
        seen = {}
        path = []
        while x not in seen:
            seen[x] = len(path)
            path.append(x)
            digits = [(x >> (2*i)) & 3 for i in range(N)]
            nxt = 0
            for i,adj in enumerate(nbr):
                y = 0
                for j in adj:
                    y ^= digits[j]
                nxt |= y << (2*i)
            x = nxt
        tau = seen[x]
        per = len(path) - tau
        totals[(tau,per)] += 1
    entry = {t:sum(v for (k,p),v in totals.items() if k==t) for t in range(3)}
    assert entry == {0:16, 1:4**4-16, 2:4**6-4**4}, entry
    print('PASS GF(4) n=4, 4096 states, time layers:', entry)

if __name__ == '__main__':
    for n in (4, 5, 6):
        compute(n)
    four_ary_n4()
