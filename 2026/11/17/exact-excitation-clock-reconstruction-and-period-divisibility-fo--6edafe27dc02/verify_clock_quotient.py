#!/usr/bin/env python3
"""Independent direct-update and bounded-walk checks for ternary CCA/GHM clocks.
Standard library only; run: python3 verify_clock_quotient.py
"""
from itertools import product

H = (0, -2, -1)


def neighbours(n, mask):
    out = [[] for _ in range(n)]
    k = 0
    for j in range(n):
        for i in range(j):
            if mask >> k & 1:
                out[i].append(j)
                out[j].append(i)
            k += 1
    return out


def step(a, nbr, ghm):
    b = list(a)
    for x in range(len(a)):
        if ghm and a[x] != 0:
            b[x] = (a[x] + 1) % 3
        else:
            target = 1 if ghm else (a[x] + 1) % 3
            if any(a[y] == target for y in nbr[x]):
                b[x] = (a[x] + 1) % 3
    return tuple(b)


def walk_max(a, nbr, t, cca):
    n = len(a)
    scores = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in nbr[x]:
            if cca:
                delta = (a[y] - a[x]) % 3
                scores[x][y] = (0, 1, -1)[delta]
            else:
                scores[x][y] = int(a[x] == 0 and a[y] == 1) - int(a[x] == 1 and a[y] == 0)
    totals = []
    for start in range(n):
        dp = [-100000] * n
        dp[start] = 0
        best = 0
        for _ in range(t):
            ndp = [-100000] * n
            for v in range(n):
                if dp[v] <= -10000:
                    continue
                for y in nbr[v]:
                    ndp[y] = max(ndp[y], dp[v] + scores[v][y])
            dp = ndp
            best = max(best, max(dp))
        totals.append(best)
    return totals


def run():
    graphs = 0
    states = 0
    timepoint_tests = 0
    for n in range(1, 5):
        for m in range(1 << (n * (n - 1) // 2)):
            nbr = neighbours(n, m)
            graphs += 1
            for a in product(range(3), repeat=n):
                cca = ghm = tuple(a)
                count_c = [0] * n
                count_g = [0] * n
                states += 1
                for t in range(11):
                    assert all(count_g[x] == (count_c[x] + H[a[x]] + 2) // 3
                               for x in range(n))
                    if t <= 5:
                        assert count_c == walk_max(a, nbr, t, True)
                        assert count_g == walk_max(a, nbr, t, False)
                    timepoint_tests += n
                    if t == 10:
                        break
                    cc = step(cca, nbr, False)
                    gg = step(ghm, nbr, True)
                    for x in range(n):
                        count_c[x] += cc[x] != cca[x]
                        count_g[x] += ghm[x] == 0 and gg[x] == 1
                    cca, ghm = cc, gg
    print('PASS clock quotient and independent walk maxima:', graphs,
          'labelled graphs;', states, 'graph-color pairs;', timepoint_tests,
          'vertex/time tests')


if __name__ == '__main__':
    run()
