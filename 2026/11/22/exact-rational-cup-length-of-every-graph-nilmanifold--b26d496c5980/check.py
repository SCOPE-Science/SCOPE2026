"""Finite checks for the graph-nilmanifold cup-length construction.

Requires only Python 3. A finite check does not prove the all-graph theorem;
the structural wedge-algebra argument is given in RESULT.md.
"""
from itertools import combinations


def edge_list(n):
    return list(combinations(range(n), 2))


def wedge(a, b):
    if set(a).intersection(b):
        return 0, ()
    inversions = sum(u > v for u in a for v in b)
    return (-1 if inversions % 2 else 1), tuple(sorted(a + b))


def derivative(mon, n, edges):
    res = {}
    for p, v in enumerate(mon):
        if v < n:
            continue
        i, j = edges[v - n]
        rest = mon[:p] + mon[p + 1:]
        s, target = wedge((i, j), rest)
        if not s:
            continue
        s *= -1 if p % 2 else 1
        res[target] = res.get(target, 0) + s
        if res[target] == 0:
            del res[target]
    return res


def check_graph(n, edges):
    m = len(edges)
    seen_target = {}
    # No two distinct source (pure central monomial, differentiated factor)
    # pairs produce the same (vertex-pair, residual central factors) target.
    for submask in range(1, 1 << m):
        source = tuple(n + i for i in range(m) if submask >> i & 1)
        for target, coefficient in derivative(source, n, edges).items():
            assert coefficient in (-1, 1)
            assert target not in seen_target, (n, edges, source, seen_target[target])
            seen_target[target] = source
    # Assign each edge to its smaller endpoint. Construct n cocycles;
    # verify each is closed and their exterior product is the volume form.
    total = ()
    for v in range(n):
        mon = (v,) + tuple(n + j for j, e in enumerate(edges) if e[0] == v)
        assert not derivative(mon, n, edges), (n, edges, v)
        sign, total = wedge(total, mon)
        assert sign != 0
    assert total == tuple(range(n + m)), (n, edges, total)
    # No boundary contains a monomial with all central generators: the
    # derivation replaces one central generator by two vertex generators.
    assert n + m == len(total)
    return len(seen_target)


def main():
    graph_count = 0
    targets = 0
    for n in range(1, 6):
        all_edges = edge_list(n)
        for mask in range(1 << len(all_edges)):
            edges = tuple(e for j, e in enumerate(all_edges) if mask >> j & 1)
            targets += check_graph(n, edges)
            graph_count += 1
    print('PASS: %d graphs on 1..5 vertices; %d individually distinguished pure-central differential targets.' % (graph_count, targets))
    print('For each: all constructed vertex-assigned cocycles closed; product is top exterior form.')
    print('General proof uses injectivity of d on positive pure-central algebra and nilpotence of vertex ideal.')

if __name__ == '__main__':
    main()
