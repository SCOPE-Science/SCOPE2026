"""Direct exhaustive tracing of binary neighbor-majority on the Tietze graph.

Run: python3 check_direct.py. Standard library only.
"""
from collections import Counter
import json

# Independent explicit adjacency for vertices 0,...,11.
NEIGHBORS = (
    (1, 5, 9), (0, 2, 6), (1, 3, 7), (2, 8, 10),
    (6, 7, 11), (0, 7, 8), (1, 4, 8), (2, 4, 5),
    (3, 5, 6), (0, 10, 11), (3, 9, 11), (4, 9, 10),
)
N = len(NEIGHBORS)
assert N == 12 and all(len(n) == 3 for n in NEIGHBORS)
assert all(i in NEIGHBORS[j] for i, row in enumerate(NEIGHBORS) for j in row)


def step(bits):
    nxt = 0
    for i, adj in enumerate(NEIGHBORS):
        # Unlike the second checker, evaluate votes by indexing bits one by one.
        votes = sum((bits >> j) & 1 for j in adj)
        if votes > 1:
            nxt |= 1 << i
    return nxt


def orbit_key(states):
    # Periodic orbit is an unordered singleton or pair.
    return tuple(sorted(states))


def classify():
    entries = Counter()
    orbit_basins = Counter()
    first_witness = None
    seen_orbits = set()
    for initial in range(1 << N):
        path = []
        visits = {}
        x = initial
        while x not in visits:
            visits[x] = len(path)
            path.append(x)
            x = step(x)
            assert len(path) < (1 << N)
        depth = visits[x]
        cyclic = path[depth:]
        period = len(cyclic)
        assert period in (1, 2), (initial, path)
        key = orbit_key(cyclic)
        entries[(depth, period)] += 1
        orbit_basins[key] += 1
        seen_orbits.add(key)
        if depth == 5 and first_witness is None:
            first_witness = initial
    basin_hist = Counter((len(cycle), count) for cycle, count in orbit_basins.items())
    return {
        'orbit_counts': {str(i): sum(len(k) == i for k in seen_orbits) for i in (1, 2)},
        'entry_period': {f'{d},{p}': v for (d, p), v in sorted(entries.items())},
        'basin_hist': {f'{p},{s}': v for (p, s), v in sorted(basin_hist.items())},
        'witness': first_witness,
        'total': sum(orbit_basins.values()),
    }

EXPECTED_ENTRY = {'0,1': 16, '0,2': 274, '1,1': 136, '1,2': 994,
 '2,1': 492, '2,2': 708, '3,1': 360, '3,2': 252,
 '4,1': 432, '4,2': 144, '5,1': 216, '5,2': 72}
EXPECTED_BASINS = {'1,2': 12, '1,38': 2, '1,776': 2,
 '2,2': 6, '2,4': 12, '2,6': 18, '2,8': 36,
 '2,12': 18, '2,14': 18, '2,40': 18, '2,70': 6, '2,76': 5}

if __name__ == '__main__':
    data = classify()
    assert data['orbit_counts'] == {'1': 16, '2': 137}
    assert data['entry_period'] == EXPECTED_ENTRY
    assert data['basin_hist'] == EXPECTED_BASINS
    assert data['total'] == 4096
    assert data['witness'] == 31, data['witness']
    print(json.dumps(data, sort_keys=True))
    print('DIRECT_CHECK_PASSED')
