"""Independent permutation-level verifier for cycle cutwidth-optimal orders.

Run: python verification/enumerate_orders.py
Python standard library only. Finite tests corroborate, but do not prove,
the all-n theorem stated in RESULT.md.
"""
from collections import Counter, deque
from itertools import permutations
from math import comb


def cutwidth(order):
    n = len(order)
    seen = set()
    worst = 0
    for x in order[:-1]:
        seen.add(x)
        worst = max(worst, sum((v not in seen)
              for u in seen for v in ((u - 1) % n, (u + 1) % n)))
    return worst


def inversion(a, b):
    rank = {x: i for i, x in enumerate(b)}
    return sum(rank[a[i]] > rank[a[j]]
               for i in range(len(a)) for j in range(i+1, len(a)))


def check(n):
    orders = [p for p in permutations(range(n)) if cutwidth(p) == 2]
    expected = n * (2 ** (n - 2))
    assert len(orders) == expected, (n, len(orders), expected)
    index = {p: i for i, p in enumerate(orders)}
    neighbors = [[] for _ in orders]
    for i, p in enumerate(orders):
        for k in range(n - 1):
            q = p[:k] + (p[k+1], p[k]) + p[k+2:]
            j = index.get(q)
            if j is not None:
                neighbors[i].append(j)
    degrees = Counter(map(len, neighbors))
    assert degrees == {j+2: 2*n*comb(n-3, j) for j in range(n-2)}
    assert sum(map(len, neighbors)) // 2 == n*(n+1)*2**(n-4)

    def bfs(seed):
        distances = [-1]*len(orders)
        distances[seed] = 0
        todo = deque([seed])
        while todo:
            u = todo.popleft()
            for v in neighbors[u]:
                if distances[v] < 0:
                    distances[v] = distances[u] + 1
                    todo.append(v)
        return distances

    full = tuple(range(n))
    start = index[full]
    d = bfs(start)
    assert -1 not in d
    for k in range(n):
        rotated = tuple((x+k) % n for x in range(n))
        assert d[index[rotated]] == (n-1)*min(k,n-k)
    # For orders with the same initial vertex, distance is exactly Kendall.
    # Test all such pairs by BFS from every starting-root-zero state.
    root_indices = [i for i, p in enumerate(orders) if p[0] == 0]
    for i in root_indices:
        d_i = bfs(i)
        for j in root_indices:
            assert d_i[j] == inversion(orders[i], orders[j])
    return (n, len(orders), sum(map(len, neighbors))//2)


if __name__ == '__main__':
    for n in range(3, 9):
        print('PERMUTATION_OK', *check(n))
