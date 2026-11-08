"""Independent finite tests for the cycle-exposure inequality in RESULT.md.

The theorem is proved analytically; this program only checks finite instances.
Requires Python 3 stdlib. Run: python3 verify.py
"""
import itertools
import math

checks = 0

def check(flag, message):
    global checks
    assert flag, message
    checks += 1


def has_simple_path_of_length(start, adj, length):
    def dfs(v, seen, d):
        if d == length:
            return True
        for u in range(len(adj)):
            if adj[v] & (1 << u) and not (seen & (1 << u)):
                if dfs(u, seen | (1 << u), d + 1):
                    return True
        return False
    return dfs(start, 1 << start, 0)


def has_cycle(length, adj):
    n = len(adj)
    def dfs(origin, v, seen, d):
        if d == length:
            return (adj[v] >> origin) & 1
        for u in range(origin + 1, n):
            if (adj[v] >> u) & 1 and not ((seen >> u) & 1):
                if dfs(origin, u, seen | (1 << u), d + 1):
                    return 1
        return 0
    for i in range(n):
        if dfs(i, i, 1 << i, 1):
            return True
    return False


def graph(n, mask):
    adj = [0] * n
    pairs = list(itertools.combinations(range(n), 2))
    for j,(u,v) in enumerate(pairs):
        if (mask >> j) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj, mask.bit_count()

for n in range(2, 7):
    for mask in range(1 << (n * (n - 1) // 2)):
        adj, edges = graph(n, mask)
        for ell in range(3, n + 1):
            # Stronger exposure inequality holds even if the graph already has C_ell.
            exposed = sum(has_simple_path_of_length(v, adj, ell - 1) for v in range(n))
            r = 2 * ell - 3
            check(exposed * r <= (r + 1) * edges,
                  (n, mask, ell, exposed, edges))

for ell in range(3, 18):
    n = 2 * ell - 2
    adj = [0] * n
    for i in range(n - 1):
        adj[i] |= 1 << (i + 1)
        adj[i + 1] |= 1 << i
    exposed = sum(has_simple_path_of_length(v, adj, ell - 1) for v in range(n))
    check(exposed == n, ('path equality witness', ell))
    check(exposed * (2 * ell - 3) == (2 * ell - 2) * (n - 1),
          ('extremal ratio', ell))

for ell in range(3, 12):
    r = 2 * ell - 3
    c = (r + 1) / r
    for n in (2500, 10000, 40000):
        for x in (0.2, 0.6, 1.0, 1.8):
            t = int(x * math.sqrt(n))
            q = 1.0
            for j in range(t):
                q *= 1 - c * j / n
            prediction = math.exp(-(c / 2) * (t * t / n))
            check(abs(q - prediction) < 15 / math.sqrt(n),
                  ('hazard product', ell, n, x, q, prediction))

print('PASS', checks, 'finite exact/combinatorial and floating-point assertions')
