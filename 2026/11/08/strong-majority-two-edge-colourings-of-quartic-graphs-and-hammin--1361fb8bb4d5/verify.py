"""Reproducible finite checks for quartic strong-majority edge colourings.

Run with Python 3 (standard library only): python verify.py.
The general classification is proved mathematically; finite checks are corroborative.
"""
from collections import deque
from itertools import combinations, product
from math import comb


def edges(graph):
    order = {v: i for i, v in enumerate(graph)}
    return [(v, w) for v in graph for w in graph[v] if order[v] < order[w]]


def canonical_edge(v, w):
    return tuple(sorted((v, w), key=repr))


def distances(graph, sources):
    distances_ = {v: -1 for v in graph}
    queue = deque(sources)
    for v in sources:
        distances_[v] = 0
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if distances_[w] == -1:
                distances_[w] = distances_[v] + 1
                queue.append(w)
    return distances_


def valid_code(graph, code):
    d = distances(graph, code)
    if set(d.values()) != set(range(5)):
        return False
    return all(
        sum(d[w] == d[v] - 1 for w in graph[v]) == d[v]
        and sum(d[w] == d[v] + 1 for w in graph[v]) == 4 - d[v]
        for v in graph
    )


def code_colouring(graph, code):
    d = distances(graph, code)
    return {
        canonical_edge(v, w): int(min(d[v], d[w]) % 2 == 1)
        for v, w in edges(graph)
    }


def strong_majority_direct(graph, colouring):
    edge_list = edges(graph)
    for a, b in edge_list:
        neighbours = [(u, v) for u, v in edge_list
                      if (u, v) != (a, b) and ({a, b} & {u, v})]
        assert len(neighbours) == 6
        for colour in (0, 1):
            if sum(colouring[canonical_edge(u, v)] == colour
                   for u, v in neighbours) > 3:
                return False
    return True


def cube():
    return {v: {v ^ (1 << j) for j in range(4)} for v in range(16)}


def switched_cube():
    graph = cube()
    for u, v in [(1, 9), (2, 10)]:
        graph[u].remove(v)
        graph[v].remove(u)
    for u, v in [(1, 10), (2, 9)]:
        graph[u].add(v)
        graph[v].add(u)
    return graph


def four_cycles(graph):
    verts = list(graph)
    total = 0
    for u, v in combinations(verts, 2):
        common = len(graph[u] & graph[v])
        total += comb(common, 2)
    return total // 2


def twisted_two_cover(graph):
    edge_set = {frozenset((u, v)) for u, v in edges(graph)}
    assert frozenset((0, 1)) in edge_set
    result = {(v, bit): set() for v in graph for bit in (0, 1)}
    for uv in edge_set:
        u, v = tuple(uv)
        twist = (uv == frozenset((0, 1)))
        for bit in (0, 1):
            neighbour_bit = bit ^ int(twist)
            result[u, bit].add((v, neighbour_bit))
            result[v, neighbour_bit].add((u, bit))
    return result


def complete_graph(n):
    return {v: set(range(n)) - {v} for v in range(n)}


def complete_bipartite_four():
    left = [('L', j) for j in range(4)]
    right = [('R', j) for j in range(4)]
    return {v: (set(right) if v in left else set(left))
            for v in left + right}


def exhaustive_colourings(graph):
    E = edges(graph)
    total = 0
    for bits in product((0, 1), repeat=len(E)):
        c = {canonical_edge(*E[j]): bits[j] for j in range(len(E))}
        total += strong_majority_direct(graph, c)
    return total


def main():
    for name, graph in [('K5', complete_graph(5)),
                        ('K44', complete_bipartite_four())]:
        assert exhaustive_colourings(graph) == 0
        print('DIRECT_ALL_COLOURINGS_EXHAUSTIVE_ZERO_OK', name)
    for name, graph, target, expected_cycles in [
        ('Q4', cube(), 16, 24),
        ('switched_Q4', switched_cube(), 8, 22),
    ]:
        assert all(len(graph[v]) == 4 for v in graph)
        assert four_cycles(graph) == expected_cycles
        codes = [{v} for v in graph if valid_code(graph, {v})]
        assert len(codes) == target
        assert all(strong_majority_direct(graph, code_colouring(graph, C))
                   for C in codes)
        print('ALL_SINGLETON_CODES_AND_EDGE_TESTS_OK', name, len(codes),
              'four_cycles', four_cycles(graph))
    graph = twisted_two_cover(cube())
    assert len(graph) == 32 and all(len(graph[v]) == 4 for v in graph)
    assert -1 not in distances(graph, {next(iter(graph))}).values()
    codes = [set(pair) for pair in combinations(graph, 2)
             if valid_code(graph, set(pair))]
    assert len(codes) == 40
    for code in codes:
        d = distances(graph, code)
        assert [sum(x == i for x in d.values()) for i in range(5)] == [2 * comb(4, i) for i in range(5)]
        assert strong_majority_direct(graph, code_colouring(graph, code))
    print('ALL_496_TWO_POINT_CODE_CANDIDATES_OK 40')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
