"""Compute exact exchange-distance shells from the Fano deletion catalogue."""

from collections import Counter, deque
from itertools import combinations


def incident(p, line):
    return (line - 7 - p) % 7 in (0, 1, 3)


def omissions():
    points, lines = range(7), range(7, 14)
    quad = {
        frozenset(p for p in points if not incident(p, line))
        for line in lines
    } | {
        frozenset(line for line in lines if not incident(p, line))
        for p in points
    }
    match = {
        frozenset(ps + ls)
        for ps in combinations(points, 2)
        for ls in combinations(lines, 2)
        if all(sum(incident(p, line) for line in ls) == 1 for p in ps)
        and all(sum(incident(p, line) for p in ps) == 1 for line in ls)
    }
    assert quad.isdisjoint(match) and (len(quad), len(match)) == (14, 84)
    return quad, match


def shells(start, neighbors):
    distance = {start: 0}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for w in neighbors[v]:
            if w not in distance:
                distance[w] = distance[v] + 1
                queue.append(w)
    histogram = Counter(distance.values())
    return tuple(histogram[d] for d in range(max(histogram) + 1))


def main():
    quad, match = omissions()
    nodes = quad | match
    expected = {
        1: ({(1,): 14}, {(1, 4, 10, 22, 39, 8): 84}, 168),
        2: ({(1, 30, 67): 14}, {(1, 22, 75): 84}, 1134),
    }
    for r in (1, 2):
        neighbors = {node: set() for node in nodes}
        for a, b in combinations(nodes, 2):
            if len(a & b) == 4 - r:
                neighbors[a].add(b)
                neighbors[b].add(a)
        q_shells = Counter(shells(node, neighbors) for node in quad)
        m_shells = Counter(shells(node, neighbors) for node in match)
        edges = sum(map(len, neighbors.values())) // 2
        assert (q_shells, m_shells, edges) == expected[r]
        print(f"r={r}, edges={edges}, quadrangles={dict(q_shells)}, "
              f"matchings={dict(m_shells)}")


if __name__ == '__main__':
    main()
