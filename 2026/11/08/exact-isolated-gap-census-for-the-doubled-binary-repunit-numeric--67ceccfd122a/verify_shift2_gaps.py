#!/usr/bin/env python3
"""Independent finite checks for isolated gaps in the shifted binary-repunit semigroup."""
import heapq


def min_coins(t, coins):
    a = [0] + [10**9] * t
    for k in range(1, t + 1):
        a[k] = 1 + min(a[k - c] for c in coins if c <= k)
    return a


def apery_dijkstra(m, gens):
    dist = [10**12] * m
    dist[0] = 0
    q = [(0, 0)]
    while q:
        d, r = heapq.heappop(q)
        if d != dist[r]:
            continue
        for v in gens:
            s = (r + v) % m
            if d + v < dist[s]:
                dist[s] = d + v
                heapq.heappush(q, (d + v, s))
    return dist


def verify():
    tested = 0
    residues = 0
    isolated = 0
    for n in range(2, 11):
        h = 1 << (n - 1)
        m = (h << 1) - 1
        coins = [(1 << j) - 1 for j in range(1, n)]
        c = min_coins(m - 1, coins)
        gens = [m] + [m + 2 * x for x in coins]
        D = apery_dijkstra(m, gens)
        expected = 3 * (1 << (n - 2)) - 1
        for t in range(m):
            r = 2 * t % m
            w = m * c[t] + 2 * t
            assert D[r] == w, (n, t, w, D[r])
            residues += 1
        assert all(c[t + 1] - c[t] in (-1, 1) for t in range(m - 1))
        assert all(c[h + t] == 1 + c[t + 1] for t in range(h - 1))
        predicted = set()
        for t in range(h, m):
            j = t - h
            kmax = 2 if c[j + 1] > c[j] else 1
            for k in range(1, kmax + 1):
                predicted.add((c[t] - k) * m + 2 * t)
        assert len(predicted) == expected
        F = max(D) - m
        actual = {
            x for x in range(1, F + 1)
            if x < D[x % m] and x - 1 >= D[(x - 1) % m]
            and x + 1 >= D[(x + 1) % m]
        }
        assert actual == predicted, (n, len(actual), len(predicted))
        tested += 1
        isolated += len(actual)
    print(f'VERIFY_OK n_cases={tested} apery_residues={residues} isolated_gaps={isolated} full_gap_census=complete')


if __name__ == '__main__':
    verify()
