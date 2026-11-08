"""Exact finite checks of the canonical source/sink-flex cochain and its symmetry.

No third-party modules. The proof in RESULT.md is all-graph; these tests are finite.
"""
from collections import deque, defaultdict
from itertools import combinations, permutations


def check_graph(n, edges):
    edges = tuple(sorted(tuple(sorted(e)) for e in edges))
    incidence = [0] * n
    for k, (a, b) in enumerate(edges):
        incidence[a] |= 1 << k
        incidence[b] |= 1 << k
    assert all(incidence), 'exclude isolated vertices'
    adjacency = set(edges)
    states = 1 << len(edges)

    def status(mask, v):
        out = []
        for j, (a, b) in enumerate(edges):
            if v != a and v != b:
                continue
            bit = (mask >> j) & 1
            out.append((bit == 1 and v == a) or (bit == 0 and v == b))
        if all(out):
            return -1   # source: direction of positive flex is reversed
        if not any(out):
            return +1   # sink: positive flex
        return 0

    flips = [[] for _ in range(states)]
    for mask in range(states):
        flips[mask] = [(v, mask ^ incidence[v], status(mask, v))
                       for v in range(n) if status(mask, v)]
    # Cells of dimension 1 are indexed by a flexed vertex and the two ends;
    # their natural orientation is from sink to source.
    edge_cells = set()
    graph_adj = [[] for _ in range(states)]
    for mask in range(states):
        for v, other, sign in flips[mask]:
            key = (min(mask, other), v)
            edge_cells.add(key)
            graph_adj[mask].append(other)
            assert status(other, v) == -sign

    # Connected components of the 1-skeleton.
    comp = [-1] * states
    components = []
    for x in range(states):
        if comp[x] >= 0:
            continue
        i = len(components)
        Q = deque([x]); comp[x] = i; group = []
        while Q:
            y = Q.popleft(); group.append(y)
            for z in graph_adj[y]:
                if comp[z] < 0:
                    comp[z] = i; Q.append(z)
        components.append(group)

    # Enumerate all cubes, not just 2-cells, to classify the Euler characteristic.
    seen_cells = set()
    count_by_component = defaultdict(lambda: defaultdict(int))
    checked_squares = 0
    for mask in range(states):
        movable = {v: s for v, _, s in flips[mask]}
        for size in range(n + 1):
            for V in combinations(movable, size):
                if any((min(v, w), max(v, w)) in adjacency for v, w in combinations(V, 2)):
                    continue
                corners = [mask]
                for v in V:
                    corners += [z ^ incidence[v] for z in corners]
                key = (V, min(corners))
                if key in seen_cells:
                    continue
                seen_cells.add(key)
                count_by_component[comp[mask]][size] += 1
                if size == 2:
                    v, w = V
                    # Independent axes commute and are unchanged as sources/sinks.
                    v_flip = mask ^ incidence[v]
                    w_flip = mask ^ incidence[w]
                    sign = (status(mask, v) + status(v_flip, w)
                            - status(w_flip, v) - status(mask, w))
                    assert sign == 0, ('2-cocycle', n, edges, mask, V, sign)
                    checked_squares += 1
    euler = []
    for i in range(len(components)):
        chi = sum((-1)**d * f for d, f in count_by_component[i].items())
        assert chi in (0, 1), ('Euler', n, edges, i, chi)
        euler.append(chi)

    aut_checks = 0
    fixed_circular_total = 0
    for p in permutations(range(n)):
        if {tuple(sorted((p[a], p[b]))) for a, b in edges} != adjacency:
            continue
        aut_checks += 1
        new_index = {e: i for i, e in enumerate(edges)}
        emap = [(new_index[tuple(sorted((p[a], p[b])))], p[a] < p[b])
                for a, b in edges]
        def action(mask):
            result = 0
            for k, (j, same) in enumerate(emap):
                b = (mask >> k) & 1
                if (b if same else 1 - b):
                    result |= 1 << j
            return result
        cm = [comp[action(group[0])] for group in components]
        assert len(set(cm)) == len(components)
        for i, group in enumerate(components):
            assert all(comp[action(x)] == cm[i] for x in group)
            assert euler[i] == euler[cm[i]]
        fixed_circular_total += sum(euler[i] == 0 and cm[i] == i
                                    for i in range(len(components)))
        for mask in range(states):
            for v, other, sign in flips[mask]:
                image = action(mask)
                assert status(image, p[v]) == sign
                assert action(other) == (image ^ incidence[p[v]])

    # For each circular component of small graphs, find a directed length-n
    # loop that uses only positive (sink-to-source) flexes.
    core_checks = 0
    if n <= 4:
        for i, group in enumerate(components):
            if euler[i]:
                continue
            found = False
            for start in group:
                stack = [(start, (), (start,))]
                while stack and not found:
                    mask, labels, path = stack.pop()
                    if len(labels) == n:
                        if mask == start and len(set(labels)) == n:
                            found = True
                        continue
                    for v, target, sign in flips[mask]:
                        if sign == 1 and v not in labels:
                            stack.append((target, labels + (v,), path + (target,)))
                if found:
                    break
            assert found, ('missing positive core', n, edges, i)
            core_checks += 1

    return (states, len(seen_cells), checked_squares, aut_checks, core_checks,
            len(components), sum(c == 0 for c in euler), fixed_circular_total)


def connected(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    q = [0]; seen = {0}
    for u in q:
        for v in adj[u]:
            if v not in seen:
                seen.add(v); q.append(v)
    return len(seen) == n


def main():
    cases = []
    for n in (2, 3, 4):
        pairs = list(combinations(range(n), 2))
        for bits in range(1 << len(pairs)):
            ed = [e for k, e in enumerate(pairs) if bits & (1 << k)]
            if connected(n, ed):
                cases.append((n, ed))
    cases.extend([
        (5, [(j, j+1) for j in range(4)]),
        (5, [(0, j) for j in range(1, 5)]),
        (5, [(j, (j+1)%5) for j in range(5)]),
        (5, list(combinations(range(5), 2))),
        (5, [(0,1),(1,2),(2,3),(3,0),(0,4),(2,4)]),
    ])
    totals = [0]*8
    for n, e in cases:
        res = check_graph(n, e)
        totals = [x+y for x,y in zip(totals,res)]
    print('ALL_VERIFY_OK graphs=%d orientations=%d cells=%d squares=%d automorphisms=%d core_cycles=%d components=%d circular_components=%d fixed_circular_character_sum=%d' %
          (len(cases), *totals))


if __name__ == '__main__':
    main()
