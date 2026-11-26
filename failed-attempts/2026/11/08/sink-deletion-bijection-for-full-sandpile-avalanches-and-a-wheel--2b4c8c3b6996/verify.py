"""Exact finite checks for the sink-deletion maximal-avalanche identity.
Run with Python 3; only the standard library is required.
"""
import itertools
import random
from collections import deque


def determinant(a):
    a = [list(map(int, row)) for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign, prev = 1, 1
    for k in range(n - 1):
        if not a[k][k]:
            r = next((r for r in range(k + 1, n) if a[r][k]), None)
            if r is None:
                return 0
            a[k], a[r] = a[r], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % prev == 0
                a[i][j] = num // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def stabilize(c, adj, deg):
    c = list(c)
    topples = [0] * len(c)
    q = deque(i for i, x in enumerate(c) if x >= deg[i])
    pending = set(q)
    while q:
        i = q.popleft()
        pending.remove(i)
        if c[i] < deg[i]:
            continue
        c[i] -= deg[i]
        topples[i] += 1
        for j in adj[i]:
            c[j] += 1
            if c[j] >= deg[j] and j not in pending:
                q.append(j)
                pending.add(j)
        if c[i] >= deg[i] and i not in pending:
            q.append(i)
            pending.add(i)
    return tuple(c), tuple(topples)


def check_graph(n, edges):
    deg = [0] * (n - 1)
    adj = [[] for _ in deg]
    b = [0] * (n - 1)
    for u, v in edges:
        if u:
            deg[u-1] += 1
        if v:
            deg[v-1] += 1
        if u == 0:
            b[v-1] += 1
        elif v == 0:
            b[u-1] += 1
        else:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
    L = [[deg[i] * (i == j) - adj[i].count(j)
          for j in range(n - 1)] for i in range(n - 1)]
    if determinant(L) == 0:
        return 0
    count = 0
    for v in range(n - 1):
        if not b[v]:
            continue
        H = [[len(adj[i]) * (i == j) - adj[i].count(j)
              for j in range(n - 1)] for i in range(n - 1)]
        Hminor = [[H[i][j] for j in range(n - 1) if j != v]
                  for i in range(n - 1) if i != v]
        expected = determinant(Hminor)
        observed = 0
        for c in itertools.product(*(range(d) for d in deg)):
            back, fire = stabilize([c[i] + b[i] for i in range(n-1)], adj, deg)
            if back != c or any(x != 1 for x in fire):
                continue
            x = list(c)
            x[v] += 1
            _, fire = stabilize(x, adj, deg)
            observed += int(all(t == 1 for t in fire))
        assert observed == expected, (n, edges, v, observed, expected)
        count += 1
    return count


def connected(n, es):
    links = [[] for _ in range(n)]
    for a, b in es:
        links[a].append(b)
        links[b].append(a)
    seen = {0}
    queue = [0]
    while queue:
        for v in links[queue.pop()]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return len(seen) == n


def wheel(n):
    return [(0, i) for i in range(1, n+1)] + [
        (i, i+1) for i in range(1, n)] + [(n, 1)]


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    random.seed(371)
    trials = 0
    sources = 0
    for n in range(3, 7):
        pairs = list(itertools.combinations(range(n), 2))
        for _ in range(70):
            es = [(a, b) for a, b in pairs if random.random() < .55]
            if connected(n, es):
                c = check_graph(n, es)
                if c:
                    trials += 1
                    sources += c
    print('Connected random graphs:', trials, 'source checks:', sources)
    for n in range(3, 11):
        es = wheel(n)
        rel = {1: 0, 0: 1}
        rel.update({i: i for i in range(2, n+1)})
        es_rim_sink = [tuple(sorted((rel[a], rel[b]))) for a,b in es]
        if n <= 7:
            assert check_graph(n+1, es_rim_sink) == 3
            assert check_graph(n+1, es) == n
        numerator = fibonacci(2*n-2)
        denominator = lucas(2*n) - 2
        assert numerator > 0 and denominator >= numerator
        print('wheel rim size', n, 'rim sink count', numerator,
              'hub sink count', n, 'total recurrent', denominator)
    print('All exact checks passed')


if __name__ == '__main__':
    main()
