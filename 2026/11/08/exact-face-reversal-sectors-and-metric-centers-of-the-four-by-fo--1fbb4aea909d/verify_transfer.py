#!/usr/bin/env python3
"""Exhaustive transfer-row verification of 4x4 periodic square-ice face flips.

Only the Python standard library is required. All cells and faces are labelled
by pairs (row, column) in {0,1,2,3}^2, with periodic indices.
"""
from collections import Counter, defaultdict, deque

N = 4


def enumerate_orientations():
    transitions = defaultdict(list)
    for incoming in range(16):
        for horizontal in range(16):
            for outgoing in range(16):
                if all(
                    ((horizontal >> j) & 1) + ((outgoing >> j) & 1)
                    == ((horizontal >> ((j - 1) % N)) & 1)
                    + ((incoming >> j) & 1)
                    for j in range(N)
                ):
                    transitions[incoming].append((horizontal, outgoing))
    states = []

    def visit(row, incoming, horizontal_rows, vertical_rows, first_incoming):
        if row == N:
            if incoming == first_incoming:
                states.append((tuple(horizontal_rows), tuple(vertical_rows)))
            return
        for hrow, vrow in transitions[incoming]:
            horizontal_rows.append(hrow)
            vertical_rows.append(vrow)
            visit(row + 1, vrow, horizontal_rows, vertical_rows, first_incoming)
            horizontal_rows.pop()
            vertical_rows.pop()

    for first in range(16):
        visit(0, first, [], [], first)
    assert len(states) == 2970 and len(set(states)) == 2970
    return states


def flux(state):
    horizontal, vertical = state
    return (sum(row & 1 for row in horizontal),
            sum((vertical[0] >> j) & 1 for j in range(N)))


def face_flip(state, row, col):
    h, v = state
    after_row = (row + 1) % N
    after_col = (col + 1) % N
    boundary = ((h[row] >> col) & 1,
                (v[row] >> after_col) & 1,
                (h[after_row] >> col) & 1,
                (v[row] >> col) & 1)
    if boundary not in ((1, 1, 0, 0), (0, 0, 1, 1)):
        return None
    h_new = list(h)
    v_new = list(v)
    h_new[row] ^= 1 << col
    h_new[after_row] ^= 1 << col
    v_new[row] ^= (1 << col) | (1 << after_col)
    return tuple(h_new), tuple(v_new)


def bfs(graph, root):
    dist = {root: 0}
    queue = deque([root])
    while queue:
        source = queue.popleft()
        for target in graph[source]:
            if target not in dist:
                dist[target] = dist[source] + 1
                queue.append(target)
    return dist


def main():
    states = enumerate_orientations()
    pos = {state: k for k, state in enumerate(states)}
    graph = [[] for _ in states]
    for k, state in enumerate(states):
        for i in range(N):
            for j in range(N):
                new = face_flip(state, i, j)
                if new is not None:
                    assert new in pos
                    graph[k].append(pos[new])
    for k, neighbors in enumerate(graph):
        assert len(set(neighbors)) == len(neighbors)
        assert all(k in graph[nbr] for nbr in neighbors)
    assert sum(map(len, graph)) == 2 * 8768

    unseen = set(range(len(states)))
    components = []
    while unseen:
        start = min(unseen)
        component = bfs(graph, start)
        components.append(sorted(component))
        unseen.difference_update(component)
    sizes = Counter(map(len, components))
    assert sizes == {1: 60, 140: 4, 340: 4, 990: 1}
    assert len(components) == 69

    expected_ecc = {
        140: {8: 92, 9: 48},
        340: {8: 28, 9: 168, 10: 96, 11: 32, 12: 16},
        990: {8: 2, 9: 284, 10: 416, 11: 224, 12: 64},
    }
    expected_edges = {140: 320, 340: 960, 990: 3648}
    flux_sector_sizes = defaultdict(list)
    centers = []
    for component in components:
        members = set(component)
        size = len(component)
        sector = flux(states[component[0]])
        assert all(flux(states[k]) == sector for k in component)
        flux_sector_sizes[sector].append(size)
        if size == 1:
            assert any(z in (0, 4) for z in sector)
            continue
        assert all(z in (1, 2, 3) for z in sector)
        ecc = Counter()
        dist_pairs = Counter()
        for start in component:
            distances = bfs(graph, start)
            assert set(distances) == members
            ecc[max(distances.values())] += 1
            for other, distance in distances.items():
                if other > start:
                    dist_pairs[distance] += 1
            if size == 990 and max(distances.values()) == 8:
                centers.append(states[start])
        assert dict(ecc) == expected_ecc[size]
        assert sum(dist_pairs.values()) == size * (size - 1) // 2
        assert sum(map(len, (graph[k] for k in component))) // 2 == expected_edges[size]
        assert min(ecc) == 8
        assert max(ecc) == (9 if size == 140 else 12)
        if sector == (2, 2):
            assert dict(dist_pairs) == {
                1: 3648, 2: 14112, 3: 35904, 4: 66064,
                5: 92224, 6: 102304, 7: 95680, 8: 58579,
                9: 16992, 10: 3632, 11: 352, 12: 64,
            }

    assert len(flux_sector_sizes) == 25
    for (a, b), vals in flux_sector_sizes.items():
        if a in (0, 4) or b in (0, 4):
            assert vals == [1] * len(vals)
        else:
            expected = 990 if a == b == 2 else (340 if a == 2 or b == 2 else 140)
            assert vals == [expected]
    assert set(centers) == {
        ((5, 10, 5, 10), (10, 5, 10, 5)),
        ((10, 5, 10, 5), (5, 10, 5, 10)),
    }

    # Explicit 12-face witness in the central sector.
    source = ((0, 0, 15, 15), (3, 3, 3, 3))
    target = ((15, 15, 0, 0), (6, 6, 6, 6))
    path = [(1, 1), (0, 1), (1, 0), (0, 0),
            (1, 2), (1, 3), (2, 1), (1, 1),
            (2, 0), (1, 0), (3, 3), (3, 2)]
    assert len(path) == 12
    current = source
    for row, col in path:
        current = face_flip(current, row, col)
        assert current is not None
    assert current == target
    assert bfs(graph, pos[source])[pos[target]] == 12
    print('TRANSFER_EXHAUSTIVE_PASS',
          'states=2970 edges=8768 components=69',
          'isolated=60', 'mobile=4x140+4x340+990',
          'radius=8 diameter=12 centers=2',
          'explicit_length12_witness=PASS')


if __name__ == '__main__':
    main()
