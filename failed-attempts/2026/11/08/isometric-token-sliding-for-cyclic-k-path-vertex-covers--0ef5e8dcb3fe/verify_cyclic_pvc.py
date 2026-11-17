"""Independent exhaustive verification of the cyclic path-cover earth-mover formula.

Run: python3 verify_cyclic_pvc.py
No third-party packages required.
"""
from collections import deque
from itertools import combinations


def is_cover(n, k, mask):
    # All k-vertex paths of the cycle are consecutive windows when 2 <= k < n.
    for start in range(n):
        if not any((mask >> ((start + j) % n)) & 1 for j in range(k)):
            return False
    return True


def earth_mover(n, a, b):
    s = 0
    levels = []
    for i in range(n):
        s += ((a >> i) & 1) - ((b >> i) & 1)
        levels.append(s)
    levels.sort()
    median = levels[n // 2]
    return sum(abs(v - median) for v in levels)


def check(n, k, t):
    states = []
    for positions in combinations(range(n), t):
        mask = sum(1 << v for v in positions)
        if is_cover(n, k, mask):
            states.append(mask)
    indices = {s: j for j, s in enumerate(states)}
    edges = [[] for _ in states]
    for i, mask in enumerate(states):
        for u in range(n):
            if not ((mask >> u) & 1):
                continue
            for v in ((u - 1) % n, (u + 1) % n):
                if (mask >> v) & 1:
                    continue
                nxt = mask ^ (1 << u) ^ (1 << v)
                if nxt in indices:
                    edges[i].append(indices[nxt])
    frozen = (t * k == n)
    if frozen and len(states) != k:
        raise AssertionError(('frozen count', n, k, t, len(states)))
    for root, a in enumerate(states):
        dist = [-1] * len(states)
        dist[root] = 0
        q = deque([root])
        while q:
            u = q.popleft()
            for v in edges[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        for j, b in enumerate(states):
            expected = -1 if frozen and a != b else earth_mover(n, a, b)
            if dist[j] != expected:
                raise AssertionError((n, k, t, a, b, dist[j], expected))
    return len(states)


def main():
    total = 0
    checked = 0
    for n in range(3, 11):
        for k in range(2, n):
            for t in range((n + k - 1) // k, n + 1):
                total += check(n, k, t)
                checked += 1
    print('PYTHON_EXHAUSTIVE_PASS', 'instances=', checked, 'BFS_roots=', total)


if __name__ == '__main__':
    main()
