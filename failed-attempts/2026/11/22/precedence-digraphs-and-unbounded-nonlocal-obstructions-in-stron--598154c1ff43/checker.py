#!/usr/bin/env python3
"""Exact finite cross-checks for strong matching precedence and flag obstructions.

Uses only the Python standard library. Not a proof of the infinite theorems.
Run: python3 checker.py
"""
import itertools
import json


def adj(n, edges):
    ns = [set() for _ in range(n)]
    for u, v in edges:
        assert 0 <= u < n and 0 <= v < n and u != v
        ns[u].add(v)
        ns[v].add(u)
    return ns


def oriented_pairs(ns):
    return [(v, u) for v in range(len(ns)) for u in sorted(ns[v])]


def precedences(ns, selected):
    arcs = set()
    for v, u in selected:
        assert u in ns[v]
        arcs.add((u, v))
        arcs.update((v, w) for w in ns[v] if w != u)
    return arcs


def dag(n, arcs):
    incoming = [0] * n
    outgoing = [[] for _ in range(n)]
    for u, v in arcs:
        incoming[v] += 1
        outgoing[u].append(v)
    available = [i for i, d in enumerate(incoming) if d == 0]
    count = 0
    while available:
        u = available.pop()
        count += 1
        for v in outgoing[u]:
            incoming[v] -= 1
            if incoming[v] == 0:
                available.append(v)
    return count == n


def strong_matching(ns, order):
    seen = set()
    pairs = set()
    for v in order:
        prior = ns[v] & seen
        if len(prior) == 1:
            pairs.add((v, next(iter(prior))))
        seen.add(v)
    return pairs


def maximal_masks(ns, pairs):
    ids = {p: i for i, p in enumerate(pairs)}
    masks = set()
    for order in itertools.permutations(range(len(ns))):
        m = 0
        for p in strong_matching(ns, order):
            m |= 1 << ids[p]
        masks.add(m)
    return tuple(masks)


def check_graph(n, edges):
    ns = adj(n, edges)
    pairs = oriented_pairs(ns)
    assert len(pairs) <= 14, 'finite replay scoped to at most seven edges'
    facets = maximal_masks(ns, pairs)
    count = 0
    for mask in range(1 << len(pairs)):
        choices = [pairs[i] for i in range(len(pairs)) if mask & (1 << i)]
        expected = dag(n, precedences(ns, choices))
        obtained = any((mask & f) == mask for f in facets)
        assert expected == obtained, (n, edges, choices, expected, obtained)
        count += 1
    return count


def prufer_tree(n, code):
    degree = [1] * n
    for v in code:
        degree[v] += 1
    edges = []
    for v in code:
        u = min(i for i in range(n) if degree[i] == 1)
        edges.append((u, v))
        degree[u] -= 1
        degree[v] -= 1
    u, v = (i for i in range(n) if degree[i] == 1)
    edges.append((u, v))
    return edges


def compatible_pairs(ns, choice):
    return all(dag(len(ns), precedences(ns, [a, b]))
               for a, b in itertools.combinations(choice, 2))


def cycle_cover(n):
    # For even n, even indices cover every edge; for odd n include the last vertex.
    return list(range(0, n, 2))


def cycle_test(n):
    ns = adj(n, [(i, (i + 1) % n) for i in range(n)])
    cover = cycle_cover(n)
    choices = [(v, (v - 1) % n) for v in cover]
    assert len(choices) == (n + 1) // 2
    assert compatible_pairs(ns, choices), (n, 'not pairwise compatible')
    assert not dag(n, precedences(ns, choices)), (n, 'expected global obstruction')
    for i in range(len(choices)):
        subset = choices[:i] + choices[i+1:]
        assert dag(n, precedences(ns, subset)), (n, i, 'non-minimal')
    return len(choices)


def check_forest_conflicts(n, edges):
    ns = adj(n, edges)
    incidences = oriented_pairs(ns)
    conflicts = 0
    for a, b in itertools.combinations(incidences, 2):
        v, u = a
        w, z = b
        predicted = (v == w or
                     (w in ns[v] and ((u == w and z == v) or
                                      (u != w and z != v))))
        actual = not dag(n, precedences(ns, [a, b]))
        assert actual == predicted, (n, edges, a, b)
        conflicts += actual
    expected = (sum(len(x)*(len(x)-1)//2 for x in ns) +
                sum(1+(len(ns[v])-1)*(len(ns[w])-1) for v,w in edges))
    assert conflicts == expected, (n, edges, conflicts, expected)
    return conflicts


def check_small_cycle_flag(n):
    ns = adj(n, [(i,(i+1)%n) for i in range(n)])
    ps = oriented_pairs(ns)
    facets = maximal_masks(ns, ps)
    for k in range(3, len(ps)+1):
        for subset in itertools.combinations(range(len(ps)),k):
            choices = [ps[i] for i in subset]
            if compatible_pairs(ns, choices):
                mask = sum(1 << i for i in subset)
                assert any((mask & f) == mask for f in facets), (n, choices)
    return len(facets)


def main():
    graphs = []
    for n in (2, 3, 4):
        poss = list(itertools.combinations(range(n), 2))
        for mask in range(1 << len(poss)):
            es = [p for i, p in enumerate(poss) if mask & (1 << i)]
            if es:
                graphs.append((n, es))
    # Five-node sample: cycles, house, complete bipartite, bowtie and sparse patterns.
    graphs += [
        (5, [(i, (i+1)%5) for i in range(5)]),
        (5, [(i, (i+1)%5) for i in range(5)] + [(0, 2)]),
        (5, [(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]),
        (5, [(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)]),
        (5, [(0,1),(1,2),(2,3),(3,4)]),
    ]
    for n in (5, 6):
        all_codes = list(itertools.product(range(n), repeat=n-2))
        indices = sorted(set([0, len(all_codes)//7, len(all_codes)//3,
                              len(all_codes)//2, 2*len(all_codes)//3,
                              6*len(all_codes)//7, len(all_codes)-1]))
        for idx in indices:
            graphs.append((n, prufer_tree(n, all_codes[idx])))
    checks = sum(check_graph(n, edges) for n, edges in graphs)
    forest_cases = 0
    for n, edges in graphs:
        if len(edges) == n-1:
            # Connectedness follows for the generated tree cases, not all graph cases.
            ns = adj(n, edges)
            seen = {0}
            while True:
                nxt = seen | set().union(*(ns[v] for v in seen))
                if nxt == seen: break
                seen = nxt
            if len(seen) == n:
                check_forest_conflicts(n, edges)
                forest_cases += 1
    cycle_flag_facets = {n:check_small_cycle_flag(n) for n in (3,4)}
    assert [cycle_test(n) for n in range(5, 13)] == [(n+1)//2 for n in range(5,13)]
    print(json.dumps({'status':'PASS', 'graph_instances':len(graphs),
                      'subset_dag_vs_order_comparisons':checks,
                      'forest_conflict_formula_instances': forest_cases,
                      'small_cycle_flag_facets': cycle_flag_facets,
                      'minimal_nonface_cycles_tested':list(range(5,13))},sort_keys=True))


if __name__ == '__main__':
    main()
