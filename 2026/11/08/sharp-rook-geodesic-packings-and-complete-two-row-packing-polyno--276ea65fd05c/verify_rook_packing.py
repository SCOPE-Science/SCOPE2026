"""Independent graph-distance checks and constructive rook-geodesic packing witnesses.

Run with Python 3.9 or later: python verify_rook_packing.py
No third-party dependencies.
"""
from collections import Counter, deque
from math import comb, factorial


def local_pattern(rows, cols):
    """Return path triples for a maximum packing of a labelled rows-by-cols board."""
    if rows < 2 or cols < 2:
        raise ValueError('both dimensions must be at least two')

    def shifted(paths, dr=0, dc=0):
        return [tuple((r + dr, c + dc) for r, c in path) for path in paths]

    p23 = [((0, 0), (1, 0), (0, 1)),
           ((1, 2), (0, 2), (1, 1))]
    p33 = [((0, 0), (1, 0), (0, 1)),
           ((2, 2), (0, 2), (2, 0)),
           ((1, 1), (2, 1), (1, 2))]
    p44 = [((0, 1), (1, 1), (0, 2)),
           ((1, 3), (0, 3), (1, 0)),
           ((2, 2), (1, 2), (2, 0)),
           ((3, 1), (2, 1), (3, 0)),
           ((3, 3), (2, 3), (3, 2))]
    if rows >= 5:
        return local_pattern(3, cols) + shifted(local_pattern(rows - 3, cols), 3, 0)
    if rows == 3:
        if cols == 2:
            return [((0, 0), (1, 0), (0, 1)), ((2, 1), (1, 1), (2, 0))]
        if cols == 3:
            return p33
        if cols % 2 == 0:
            return local_pattern(3, 2) + shifted(local_pattern(3, cols - 2), 0, 2)
        return p33 + shifted(local_pattern(3, cols - 3), 0, 3)
    if rows == 4:
        if cols == 2:
            return local_pattern(2, 2) + shifted(local_pattern(2, 2), 2, 0)
        if cols == 3:
            return p23 + shifted(p23, 2, 0)
        if cols == 4:
            return p44
        return local_pattern(4, 3) + shifted(local_pattern(4, cols - 3), 0, 3)
    # rows == 2
    if cols == 2:
        return [((0, 0), (1, 0), (0, 1))]
    if cols == 3:
        return p23
    if cols == 4:
        return p23
    return p23 + shifted(local_pattern(2, cols - 3), 0, 3)


def test_constructive():
    cases = 0
    for m in range(2, 17):
        for n in range(2, 17):
            paths = local_pattern(m, n)
            assert len(paths) == m * n // 3, (m, n, len(paths))
            used = set()
            for path in paths:
                assert len(set(path)) == 3
                for r, c in path:
                    assert 0 <= r < m and 0 <= c < n
                    assert (r, c) not in used
                    used.add((r, c))
                a, b, c = path
                # One common centre, one same-row wing, one same-column wing.
                assert ((a[0] == b[0] and a[1] == c[1] and b[1] != a[1] and c[0] != a[0]) or
                        (a[1] == b[1] and a[0] == c[0] and b[0] != a[0] and c[1] != a[1]))
            cases += 1
    print('CONSTRUCTIONS_OK rectangles', cases, 'range_each_dimension=2..16')


def expected_profiles(n):
    all_by_size = Counter()
    maximal_by_size = Counter()
    for k in range(2 * n // 3 + 1):
        q = n - k
        all_by_size[k] = comb(n, k) * sum(
            comb(k, i) * factorial(q) // factorial(q - i) * factorial(q) // factorial(q - (k - i))
            for i in range(k + 1) if i <= q and k - i <= q)
        if (n + 1) // 2 <= k:
            val = factorial(n) // factorial(q) * comb(q, 2 * k - n) * 2 ** (2 * n - 3 * k)
            if n % 3 == 1 and k == 2 * (n // 3):
                val += factorial(n) // factorial(n // 3)
            maximal_by_size[k] = val
    return all_by_size, maximal_by_size


def test_direct_graph(n):
    N = 2 * n
    adj = [set() for _ in range(N)]
    for u in range(N):
        for v in range(N):
            if v != u and (u // n == v // n or u % n == v % n):
                adj[u].add(v)
    distances = []
    for source in range(N):
        dist = [-1] * N
        dist[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        distances.append(dist)
    paths = set()
    for a in range(N):
        for b in range(a + 1, N):
            if distances[a][b] == 2:
                for mid in adj[a] & adj[b]:
                    paths.add(sum(1 << v for v in (a, mid, b)))
    paths = sorted(paths)
    all_by_size, maximal_by_size = Counter(), Counter()
    def visit(start, occupied, k):
        all_by_size[k] += 1
        if not any((occupied & p) == 0 for p in paths):
            maximal_by_size[k] += 1
        for idx in range(start, len(paths)):
            p = paths[idx]
            if occupied & p == 0:
                visit(idx + 1, occupied | p, k + 1)
    visit(0, 0, 0)
    expected_all, expected_maximal = expected_profiles(n)
    assert all_by_size == expected_all, (n, all_by_size, expected_all)
    assert maximal_by_size == expected_maximal, (n, maximal_by_size, expected_maximal)
    k = 2 * n // 3
    print('DIRECT_OK n', n, 'max_size', k, 'maximum_count', all_by_size[k],
          'total_packings', sum(all_by_size.values()),
          'inclusion_maximal', sum(maximal_by_size.values()))


def main():
    test_constructive()
    for n in range(2, 8):
        test_direct_graph(n)
    print('VERIFY_OK shortest_paths=PASS all_packings=PASS inclusion_maximal=PASS extremal_counts=PASS rectangular_witnesses=PASS')


if __name__ == '__main__':
    main()
