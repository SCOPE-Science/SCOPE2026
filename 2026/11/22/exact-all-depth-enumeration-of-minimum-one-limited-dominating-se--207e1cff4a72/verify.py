#!/usr/bin/env python3
"""Exact optimizer counts for the ternary Sierpinski graph; standalone checks."""
from itertools import product, combinations
from collections import defaultdict

GOOD_OMITTED, SATURATED_SELECTED, NEEDS_EXTERNAL, FREE_SELECTED = range(4)


def compatible(a, b):
    # Each joined pair consists of boundary vertices with just one external edge.
    return (a, b) in {
        (0, 0), (0, 3), (3, 0), (1, 1), (1, 3), (3, 1),
        (2, 3), (3, 2), (3, 3)
    }


def initial_table():
    w = defaultdict(int)
    for f in product(range(3), repeat=3):
        if all(f[f[i]] == i for i in range(3)):
            w[tuple(GOOD_OMITTED if f[i] == i else SATURATED_SELECTED
                    for i in range(3))] += 1
    for i in range(3):
        w[tuple(NEEDS_EXTERNAL if j == i else FREE_SELECTED
                for j in range(3))] += 1
    assert sum(w.values()) == 7
    return dict(w)


def boundary_transfer(w):
    nxt = defaultdict(int)
    for (x, a), (y, b), (z, c) in product(w.items(), repeat=3):
        if (compatible(x[1], y[0]) and compatible(x[2], z[0])
                and compatible(y[2], z[1])):
            nxt[(x[0], y[1], z[2])] += a * b * c
    return dict(nxt)


def transfer_counts(last=6):
    w = initial_table()
    ans = {}
    for n in range(2, last+1):
        ans[n] = sum(count for profile, count in w.items()
                     if NEEDS_EXTERNAL not in profile)
        if n < last:
            w = boundary_transfer(w)
    return ans


def literal_graph(n):
    vertices = list(product(range(3), repeat=n))
    adj = [set() for _ in vertices]
    for i, u in enumerate(vertices):
        for j in range(i+1, len(vertices)):
            v = vertices[j]
            h = next((h for h in range(n) if u[h] != v[h]), None)
            if h is not None and all(u[t] == v[h] and v[t] == u[h]
                                     for t in range(h+1, n)):
                adj[i].add(j)
                adj[j].add(i)
    return vertices, adj


def locally_admissible_omissions():
    vs, adj = literal_graph(2)
    corners = {vs.index((i, i)) for i in range(3)}
    allowed = []
    for omitted in combinations(range(9), 3):
        omitted = frozenset(omitted)
        if any(len(adj[i] & omitted) > 1 for i in range(9) if i not in omitted):
            continue
        if any(not (adj[i] - omitted) and i not in corners for i in omitted):
            continue
        allowed.append(omitted)
    return allowed


def exhaustive_block_count(n):
    # Independent of the four-port recurrence: enumerate literal vertices,
    # literal edges and all locally admissible nine-vertex choices.
    states = locally_admissible_omissions()
    assert len(states) == 7
    words, neighbors = literal_graph(n)
    index = {v: i for i, v in enumerate(words)}
    small_words, _ = literal_graph(2)
    prefixes = list(product(range(3), repeat=n-2))
    blocks = [[index[p+u] for u in small_words] for p in prefixes]
    membership = {v: (b, j) for b, block in enumerate(blocks)
                  for j, v in enumerate(block)}
    cross = []
    for v, nv in enumerate(neighbors):
        for u in nv:
            if v < u and membership[v][0] != membership[u][0]:
                cross.append((membership[v], membership[u]))
    assert len(cross) == (3**(n-1)-3)//2
    # Compute local number of omitted neighbors / chosen neighbors directly
    # using S(2,3) literal adjacency, with no use of table 'compatible'.
    _, small_adj = literal_graph(2)
    local_info = []
    for omitted in states:
        record = []
        for i in range(9):
            if i in omitted:
                record.append((False, len(small_adj[i] - omitted)))
            else:
                record.append((True, len(small_adj[i] & omitted)))
        local_info.append(record)
    compat = defaultdict(lambda: {(a,b) for a in range(7) for b in range(7)})
    for (block_a, local_a), (block_b, local_b) in cross:
        if block_a > block_b:
            block_a, block_b = block_b, block_a
            local_a, local_b = local_b, local_a
        good_pairs = set()
        for a, b in product(range(7), repeat=2):
            x, nx = local_info[a][local_a]
            y, ny = local_info[b][local_b]
            if x and (nx+(not y)>1):
                continue
            if y and (ny+(not x)>1):
                continue
            if not x and (nx+y==0):
                continue
            if not y and (ny+x==0):
                continue
            good_pairs.add((a,b))
        compat[(block_a,block_b)] &= good_pairs
    picked = []
    count = 0
    def extend(k):
        nonlocal count
        if k == len(blocks):
            chosen = set(v for block,state in enumerate(picked)
                         for j,v in enumerate(blocks[block]) if j not in states[state])
            assert len(chosen) == 2*3**(n-1)
            if not all(any(y in chosen for y in neighbors[x]) for x in range(len(words))
                       if x not in chosen):
                return
            if not all(len(neighbors[x]-chosen)<=1 for x in chosen):
                return
            count += 1
            return
        for state in range(7):
            if all((picked[j],state) in compat[(j,k)]
                   for j in range(k) if (j,k) in compat):
                picked.append(state)
                extend(k+1)
                picked.pop()
    extend(0)
    return count


if __name__ == '__main__':
    states = locally_admissible_omissions()
    assert len(states) == 7
    print('SEVEN_LOCAL_PATTERNS_FROM_LITERAL_GRAPH_PASS')
    observed = transfer_counts(6)
    expected = {2:4, 3:10, 4:6656, 5:2496589218858,
                6:90662803920487613562381063188768896464}
    assert observed == expected, (observed, expected)
    print('ALL_DEPTH_CUBIC_TRANSFER_ARITHMETIC_PASS', observed)
    for n in (3,4):
        exact = exhaustive_block_count(n)
        assert exact == observed[n], (n, exact, observed[n])
        print('INDEPENDENT_LITERAL_EDGE_OPTIMUM_EXHAUSTION_PASS', n, exact)
    print('VERIFY_OK')
