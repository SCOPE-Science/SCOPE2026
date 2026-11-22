#!/usr/bin/env python3
"""Exhaustive certificate for locating-total code reconfiguration on C3 x C6."""
from collections import Counter, deque

ROWS, COLUMNS = 3, 6
ORDER = ROWS * COLUMNS
NEIGHBORS = []
for c in range(COLUMNS):
    for r in range(ROWS):
        neighbors = [(c, (r + 1) % ROWS), (c, (r - 1) % ROWS),
                     ((c + 1) % COLUMNS, r), ((c - 1) % COLUMNS, r)]
        NEIGHBORS.append(sum(1 << (ROWS * x + y) for x, y in neighbors))


def locating_total(mask):
    signatures = set()
    for v, neighbors in enumerate(NEIGHBORS):
        signature = neighbors & mask
        if signature == 0:
            return False
        if not (mask & (1 << v)):
            if signature in signatures:
                return False
            signatures.add(signature)
    return True


valid = {mask for mask in range(1 << ORDER) if locating_total(mask)}
counts = Counter(mask.bit_count() for mask in valid)
print('SIZE_POLYNOMIAL:', ' '.join(f'{k}:{counts[k]}' for k in sorted(counts)))
assert sum(counts.values()) == len(valid) == 103056
assert all(k >= 6 for k in counts)
minimum = {m for m in valid if m.bit_count() == 6}
assert len(minimum) == 12

# A minimum uses three alternating columns, two vertices per used column,
# and its three omitted row labels are a permutation of (0,1,2).
def phase(m):
    first = [((m >> (3*c)) & 7) for c in range(6)]
    for parity in (0, 1):
        occupied = [first[c] for c in range(parity, 6, 2)]
        empty = [first[c] for c in range(1-parity, 6, 2)]
        if all(x == 0 for x in empty) and all(x.bit_count() == 2 for x in occupied):
            omitted = [next(r for r in range(3) if not x & (1 << r)) for x in occupied]
            if sorted(omitted) == [0,1,2]:
                return parity
    raise AssertionError('Unclassified minimum code')
assert Counter(phase(m) for m in minimum) == {0:6, 1:6}

# Reconfiguration is a single addition or deletion of a detector.
for budget in range(6, 19):
    allowed = {m for m in valid if m.bit_count() <= budget}
    unseen = allowed.copy()
    profiles = Counter()
    components_with_minima = []
    while unseen:
        root = unseen.pop()
        queue = deque([root])
        component = [root]
        while queue:
            mask = queue.popleft()
            for v in range(ORDER):
                changed = mask ^ (1 << v)
                if changed in unseen:
                    unseen.remove(changed)
                    queue.append(changed)
                    component.append(changed)
        profile = (len(component), len(minimum.intersection(component)))
        profiles[profile] += 1
        if profile[1]:
            components_with_minima.append(profile)
    report = sorted((size, minima, multiplicity) for (size,minima),multiplicity in profiles.items())
    print(f'BUDGET_{budget}:', report, 'STATES:', len(allowed))
    if budget == 6: assert report == [(1,1,12)]
    if budget == 7: assert report == [(1,0,216),(13,1,12)]
    if budget == 8: assert report == [(1,0,2259),(132,0,6),(1257,6,2)]
    if budget == 9: assert report == [(1,0,60),(22415,12,1)]
    if budget == 10: assert report == [(48620,12,1)]
    if budget >= 11: assert report == [(len(allowed),12,1)]

# In the budget-nine graph, all pairs of minima are connected. Their
# shortest-path lengths depend only on their relative row patterns.
allowed = {m for m in valid if m.bit_count() <= 9}
minimum_sorted = sorted(minimum)
by_phase = Counter()
for root in minimum_sorted:
    distance = {root:0}
    q = deque([root])
    while q:
        mask = q.popleft()
        for v in range(ORDER):
            changed = mask ^ (1 << v)
            if changed in allowed and changed not in distance:
                distance[changed] = distance[mask] + 1
                q.append(changed)
    assert len(distance) == 22415
    dist_counts = Counter(distance[m] for m in minimum)
    assert dist_counts == {0:1,4:3,6:2,12:6}
    assert all(distance[m] == 12 for m in minimum if phase(m) != phase(root))
    by_phase[phase(root)] += 1
print('MINIMUM_DISTANCE_PROFILE_BUDGET_9:', '0:1 4:3 6:2 12:6')
print('PASS')
