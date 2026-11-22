"""Standalone exact finite checks of a theorem about zero-forcing sets on theta graphs.

The checks do not prove assertions for all path lengths.  The symbolic argument
in RESULT.md supplies the all-length proof.
"""
from itertools import combinations
from collections import Counter, deque


def graph(length):
    adj = [set(), set()]
    paths = []
    for arm in range(3):
        internal = list(range(len(adj), len(adj) + length - 1))
        adj.extend(set() for _ in internal)
        path = [0] + internal + [1]
        for a, b in zip(path, path[1:]):
            adj[a].add(b)
            adj[b].add(a)
        paths.append(path)
    return adj, paths


def zero_forcing(adjacency, initially_blue):
    blue = set(initially_blue)
    while True:
        additional = set()
        for vertex in blue:
            white = adjacency[vertex] - blue
            if len(white) == 1:
                additional.update(white)
        if not additional:
            return len(blue) == len(adjacency)
        blue.update(additional)


def predicted(length, paths):
    result = set()
    for hub, near in ((0, 1), (1, length - 1)):
        far = length - near
        for i, j in combinations(range(3), 2):
            result.add(frozenset((hub, paths[i][near], paths[j][near])))
            result.add(frozenset((hub, paths[i][near], paths[j][far])))
            result.add(frozenset((hub, paths[i][far], paths[j][near])))
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            for k in range(1, length - 1):
                for endpoint in (1, length - 1):
                    result.add(frozenset((paths[i][k], paths[i][k + 1], paths[j][endpoint])))
    return result


def components(nodes, neighbors):
    remaining = set(nodes)
    sizes = []
    while remaining:
        start = remaining.pop()
        todo = [start]
        size = 0
        while todo:
            current = todo.pop()
            size += 1
            for other in neighbors[current] & remaining:
                remaining.remove(other)
                todo.append(other)
        sizes.append(size)
    return sorted(sizes)


def check(length):
    adj, paths = graph(length)
    predicted_sets = predicted(length, paths)
    actual_sets = {
        frozenset(initial)
        for initial in combinations(range(len(adj)), 3)
        if zero_forcing(adj, initial)
    }
    assert actual_sets == predicted_sets, (length, len(actual_sets), len(predicted_sets))
    assert len(actual_sets) == 12 * length - 6
    assert all(not zero_forcing(adj, initial) for initial in combinations(range(len(adj)), 2))
    jump = {v: set() for v in actual_sets}
    slide = {v: set() for v in actual_sets}
    for v in actual_sets:
        for old in v:
            base = v - {old}
            for new in set(range(len(adj))) - v:
                w = base | {new}
                if w in actual_sets:
                    jump[v].add(w)
                    if new in adj[old]:
                        slide[v].add(w)
    assert components(actual_sets, jump) == [len(actual_sets)]
    if length == 3:
        assert components(actual_sets, slide) == [10, 10, 10]
        assert {len(x) for x in slide.values()} == {2}
    else:
        assert components(actual_sets, slide) == [1] * len(actual_sets)
    return len(actual_sets), sum(map(len, jump.values())) // 2, sum(map(len, slide.values())) // 2


if __name__ == '__main__':
    for length in range(3, 13):
        a, b, c = check(length)
        print(f'length={length} minima={a} jump_edges={b} slide_edges={c}')
    print('VERIFY_OK')
