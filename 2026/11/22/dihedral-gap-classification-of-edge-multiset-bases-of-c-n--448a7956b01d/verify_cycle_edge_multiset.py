"""Exact independent graph-distance check of the three-gap theorem.

Run with Python 3.10+: python verify_cycle_edge_multiset.py
No third-party dependencies. Exhaustive for 3 <= n <= 28.
"""
from collections import deque
from itertools import combinations
from math import comb


def all_pairs_shortest_cycle(n):
    adj = [[] for _ in range(n)]
    for i in range(n):
        j = (i + 1) % n
        adj[i].append(j)
        adj[j].append(i)
    ans = []
    for i in range(n):
        d = [-1] * n
        d[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    q.append(v)
        ans.append(d)
    return ans


def brute_resolves(ds, n, s):
    fingerprints = set()
    for e in range(n):
        code = tuple(sorted(min(ds[sensor][e], ds[sensor][(e + 1) % n]) for sensor in s))
        if code in fingerprints:
            return False
        fingerprints.add(code)
    return True


def theorem_resolves(n, s):
    a, b, c = s
    gaps = [b-a,c-b,n-c+a]
    return (len(set(gaps)) == 3 and
            not (n % 4 == 2 and n // 2 in gaps))


def formula_count(n):
    u = comb(n-1, 2)-3*((n-1)//2) + 2*(n%3==0)
    if n % 4 == 2:
        u -= 3*(n//2-1)
    assert (n*u)%3==0
    return n*u//3


def verify():
    for n in range(3,29):
        ds=all_pairs_shortest_cycle(n)
        count = 0
        for s in combinations(range(n),3):
            got=brute_resolves(ds,n,s)
            expected=theorem_resolves(n,s)
            if got != expected:
                raise AssertionError(('classification', n,s,got,expected))
            count += got
        if count != formula_count(n):
            raise AssertionError(('formula',n,count,formula_count(n)))
        if n >= 7 and count % (2*n):
            raise AssertionError(('orbit divisibility',n,count))
        if n <= 20 or n%4 == 0:
            print(n, count, (count//(2*n) if n>=7 else 0))
    print('EDGE_MULTISET_CYCLE_BASIS_VERIFY_OK 3<=n<=28')

if __name__ == '__main__':
    verify()
