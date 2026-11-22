#!/usr/bin/env python3
"""Independent component-cut characterization and small-board exhaustive checks."""
from collections import Counter


def structural(m, n, mask):
    row_neigh = [set() for _ in range(m)]
    col_neigh = [set() for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if (mask >> (i * n + j)) & 1:
                row_neigh[i].add(j)
                col_neigh[j].add(i)
    if any(sum(col_neigh[j] <= {i} for j in range(n)) > 1 for i in range(m)):
        return False
    if any(sum(row_neigh[i] <= {j} for i in range(m)) > 1 for j in range(n)):
        return False
    # Obtain connected components of the selected-cell incidence graph.
    unseen = set(range(m + n))
    component_profiles = []
    while unseen:
        root = next(iter(unseen))
        todo = [root]
        seen = {root}
        while todo:
            v = todo.pop()
            neighbors = ({m + j for j in row_neigh[v]} if v < m
                         else set(col_neigh[v - m]))
            for u in neighbors - seen:
                seen.add(u)
                todo.append(u)
        unseen -= seen
        component_profiles.append((sum(x < m for x in seen), sum(x >= m for x in seen)))
    attainable = {(0, 0)}
    for a, b in component_profiles:
        attainable |= {(x + a, y + b) for x, y in list(attainable)}
    return (2, 2) not in attainable


def distance_property(m, n, mask):
    for r in range(m):
        for c in range(n):
            for u in range(r, m):
                for v in range(n):
                    if (r, c) >= (u, v):
                        continue
                    found = False
                    for p in range(m):
                        for q in range(n):
                            if (p, q) in ((r, c), (u, v)):
                                continue
                            if not ((mask >> (p * n + q)) & 1):
                                continue
                            d1 = int(p != r) + int(q != c)
                            d2 = int(p != u) + int(q != v)
                            if d1 != d2:
                                found = True
                                break
                        if found:
                            break
                    if not found:
                        return False
    return True


expected = {
    (2, 2): {},
    (2, 3): {4: 6, 5: 6, 6: 1},
    (3, 3): {4: 36, 5: 108, 6: 84, 7: 36, 8: 9, 9: 1},
    (3, 4): {5: 72, 6: 456, 7: 648, 8: 477, 9: 220, 10: 66, 11: 12, 12: 1},
    (4, 4): {6: 2016, 7: 6912, 8: 10872, 9: 10960,
             10: 7960, 11: 4368, 12: 1820, 13: 560,
             14: 120, 15: 16, 16: 1},
}
for (m, n), should_be in expected.items():
    census = Counter()
    for mask in range(1 << (m * n)):
        criterion = structural(m, n, mask)
        direct = distance_property(m, n, mask)
        assert criterion == direct, (m, n, mask)
        if criterion:
            census[mask.bit_count()] += 1
    assert dict(census) == should_be, (m, n, census)
    print(f'{m}x{n}: {sum(census.values())} total resolving sets')
print('COMPONENT_CHARACTERIZATION_CHECK_OK')
