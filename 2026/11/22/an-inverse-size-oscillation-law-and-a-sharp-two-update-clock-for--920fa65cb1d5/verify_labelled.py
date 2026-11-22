#!/usr/bin/env python3
"""Direct labelled-graph verification for three-colour tie-retaining plurality.

Only standard Python is needed. By default tests m=2,...,5; the optional
--extended flag also enumerates all 531441 initial states for m=6.
"""
from collections import Counter
import sys

EXPECTED = {
    2: (39, 3, 6, 1),
    3: (33, 54, 108, 2),
    4: (147, 153, 1314, 2),
    5: (339, 915, 6630, 2),
    6: (861, 3270, 41100, 2),
}


def run(m):
    n = 2 * m
    total = 3 ** n
    neigh = [tuple(j for j in range(n) if j != i and j != (i ^ 1))
             for i in range(n)]
    nxt = [0] * total
    for number in range(total):
        x = number
        colors = [0] * n
        for v in range(n):
            colors[v] = x % 3
            x //= 3
        target = 0
        power = 1
        for v in range(n):
            c0 = c1 = c2 = 0
            for u in neigh[v]:
                c = colors[u]
                if c == 0: c0 += 1
                elif c == 1: c1 += 1
                else: c2 += 1
            maximum = max(c0, c1, c2)
            if (c0 == maximum) + (c1 == maximum) + (c2 == maximum) == 1:
                new = (c0, c1, c2).index(maximum)
            else:
                new = colors[v]
            target += power * new
            power *= 3
        nxt[number] = target

    # Functional-graph traversal is separate from the update implementation.
    # period[x] is the least eventual period, entry[x] the first entry depth.
    seen = [0] * total
    period = [0] * total
    entry = [0] * total
    orbit_count = Counter()
    for start in range(total):
        if seen[start]:
            continue
        path = []
        index = {}
        x = start
        while not seen[x]:
            index[x] = len(path)
            seen[x] = start + 1
            path.append(x)
            x = nxt[x]
        if seen[x] == start + 1:
            first = index[x]
            p = len(path) - first
            orbit_count[p] += 1
            for y in path[first:]:
                period[y] = p
                entry[y] = 0
            path = path[:first]
        for y in reversed(path):
            period[y] = period[x]
            entry[y] = entry[x] + 1
            x = y

    basin2 = sum(p == 2 for p in period)
    result = (orbit_count[1], orbit_count[2], basin2, max(entry))
    assert result == EXPECTED[m], (m, result, EXPECTED[m])
    assert sum(orbit_count.values()) > 0
    assert set(period) <= {1, 2}
    assert all(nxt[nxt[nxt[nxt[x]]]] == nxt[nxt[x]]
               for x in range(total))
    print('m=%d states=%d fixed=%d two_cycle_orbits=%d '
          'period2_basin=%d max_entry=%d' % ((m, total) + result))


if __name__ == '__main__':
    for m in range(2, 7 if '--extended' in sys.argv else 6):
        run(m)
    print('DIRECT GRAPH VERIFICATION PASS')
