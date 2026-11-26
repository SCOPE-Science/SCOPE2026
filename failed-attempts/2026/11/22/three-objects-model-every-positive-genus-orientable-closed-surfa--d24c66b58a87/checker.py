"""Independent finite checks for the three-object surface categories.

This executable verifies actual composition tables, elementary free-edge
collapses, surface vertex links, and integral fundamental cycles for odd r.
The mathematical theorem for every odd r is established by the proof, not
by this finite check.
"""
from collections import Counter, defaultdict, deque


def connected_cycle(nodes, edges):
    adjacency = {node: [] for node in nodes}
    for a, b in edges:
        assert a != b
        adjacency[a].append(b)
        adjacency[b].append(a)
    assert all(len(adjacency[a]) == 2 for a in nodes)
    start = next(iter(nodes))
    seen = {start}
    fringe = [start]
    while fringe:
        for b in adjacency[fringe.pop()]:
            if b not in seen:
                seen.add(b)
                fringe.append(b)
    assert seen == set(nodes)
    assert len(edges) == len(nodes)


def check(r):
    assert r >= 3 and r % 2 == 1
    # For each (f_i,g_j), give the composite h_i, or a distinct private h.
    T = {}
    for i in range(r):
        for j in range(r):
            if j == i:
                T[(i, j)] = ("h", i)
            elif j == (i + 1) % r:
                T[(i, j)] = ("h", (i + 2) % r)
            else:
                T[(i, j)] = ("private", i, j)
    counts = Counter(T.values())
    assert len(counts) == r * r - r
    assert all(counts[("h", i)] == 2 for i in range(r))
    assert sum(count == 1 for count in counts.values()) == r * (r - 2)

    kept = [(i, j) for i in range(r) for j in range(r)
            if counts[T[(i, j)]] == 2]
    assert len(kept) == 2 * r
    assert set(kept) == {(i, i) for i in range(r)} | {(i, (i + 1) % r) for i in range(r)}
    # Each discarded 2-cell has a unique h face: valid elementary collapse.
    for (i, j) in T:
        if (i, j) not in kept:
            assert counts[T[(i, j)]] == 1
    f_edges = [("f", i) for i in range(r)]
    g_edges = [("g", i) for i in range(r)]
    h_edges = [("h", i) for i in range(r)]
    all_edges = f_edges + g_edges + h_edges
    incidence = Counter()
    # oriented triangle boundary: f_i + g_j - h_T(i,j)
    oriented_boundary = Counter()
    for (i, j) in kept:
        sign = +1 if j == i else -1
        for edge, coefficient in ((("f", i), 1), (("g", j), 1), (T[(i, j)], -1)):
            incidence[edge] += 1
            oriented_boundary[edge] += sign * coefficient
    assert all(incidence[e] == 2 and oriented_boundary[e] == 0 for e in all_edges)
    # Link at object 0 joins f_i--h_(T(i,j)); at 1 joins f_i--g_j;
    # at 2 joins g_j--h_(T(i,j)). Every link must be one cycle.
    link_a = [(('f', i), T[(i, j)]) for i,j in kept]
    link_b = [(('f', i), ('g', j)) for i,j in kept]
    link_c = [(('g', j), T[(i, j)]) for i,j in kept]
    connected_cycle(f_edges + h_edges, link_a)
    connected_cycle(f_edges + g_edges, link_b)
    connected_cycle(g_edges + h_edges, link_c)
    euler = 3 - len(all_edges) + len(kept)
    genus = (2 - euler) // 2
    assert euler == 3 - r and genus == (r - 1)//2
    print(f"r={r}, genus={genus}, triangles_before={r*r}, private_collapses={r*(r-2)}, remaining_triangles={len(kept)}, edges={len(all_edges)}, Euler={euler}: PASS")


if __name__ == "__main__":
    for r in (3,5,7,9,11,13,15):
        check(r)
    print("All finite structure checks passed (the all-odd-r theorem is analytical).")
