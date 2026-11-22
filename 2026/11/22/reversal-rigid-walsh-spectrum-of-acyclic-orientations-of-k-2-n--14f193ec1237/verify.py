"""Exact independent checks of the acyclic-orientation Fourier theorem.

Run: python3 verify.py
Uses Python standard library only and integer arithmetic throughout.
"""
from collections import Counter


def formula(n, mask):
    counts = [0, 0, 0, 0]
    for j in range(n):
        counts[(mask >> (2 * j)) & 3] += 1
    x, z, y, w = counts  # binary labels 01, 10 in integer order
    if y + z:
        return 0 if (y + z) % 2 else 2 * (3 ** x) * ((-1) ** y)
    return 2 * (3 ** x) - 2 ** n


def direct_acyclic(n, mask):
    # Edge bit 0: left vertex a -> right vertex j; 1: right j -> a.
    # Edge bit 1: left vertex b -> right vertex j; 1: right j -> b.
    graph = [[] for _ in range(n + 2)]
    for j in range(n):
        v = j + 2
        for a in range(2):
            bit = (mask >> (2 * j + a)) & 1
            u, dest = (a, v) if bit == 0 else (v, a)
            graph[u].append(dest)
    color = [0] * (n + 2)
    def visit(u):
        color[u] = 1
        for v in graph[u]:
            if color[v] == 1 or (color[v] == 0 and not visit(v)):
                return False
        color[u] = 2
        return True
    return all(color[u] or visit(u) for u in range(n + 2))


def fwht(a):
    span = 1
    while span < len(a):
        for b in range(0, len(a), 2 * span):
            for i in range(b, b + span):
                p, q = a[i], a[i + span]
                a[i], a[i + span] = p + q, p - q
        span *= 2


def verify():
    for n in range(2, 8):
        size = 4 ** n
        f = []
        for mask in range(size):
            columns = [(mask >> (2 * j)) & 3 for j in range(n)]
            allowed = not (1 in columns and 2 in columns)
            if n <= 5:
                assert allowed == direct_acyclic(n, mask), (n, mask)
            f.append(int(allowed))
        assert sum(f) == 2 * (3 ** n) - 2 ** n
        fwht(f)
        assert all(f[m] == formula(n, m) for m in range(size)), n
        assert sum(v == 0 for v in f) == size // 2
        assert min(abs(v) for v in f if v) == 2
        assert max(abs(v) for v in f) == 2 * (3 ** n) - 2 ** n
        assert all((f[m] == 0) == (m.bit_count() % 2 == 1) for m in range(size))
        print('n=', n, 'orientations=', f[0], 'rank=', size // 2,
              'nullity=', size // 2, 'distinct values=', len(Counter(f)))
    print('All exact checks passed.')

if __name__ == '__main__':
    verify()
