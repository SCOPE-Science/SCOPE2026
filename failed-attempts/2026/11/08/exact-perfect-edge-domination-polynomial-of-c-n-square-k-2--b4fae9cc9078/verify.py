"""Standalone exact check for perfect edge domination on circular ladders.

No nonstandard dependencies.  The finite transition graph is an exact
infinite-family certificate; the separate graph-edge enumeration is a
small-order consistency check, not an extrapolation.
"""
from collections import Counter
from itertools import product


def bit(s, k):
    return (s >> k) & 1


def top(s):
    return bit(s, 2)


def bottom(s):
    return bit(s, 1)


def rung(s):
    return bit(s, 0)


def locally_admissible(a, b, c):
    """Check the three edges belonging to column b.

    a, b, c encode triples (top horizontal, bottom horizontal, rung),
    with 1 indicating selection in the edge set.
    """
    return (
        (rung(b) == 1 or top(a) + top(b) + bottom(a) + bottom(b) == 1)
        and (top(b) == 1 or top(a) + top(c) + rung(b) + rung(c) == 1)
        and (bottom(b) == 1 or bottom(a) + bottom(c) + rung(b) + rung(c) == 1)
    )


def transition_graph():
    vertices = tuple(product(range(8), repeat=2))
    edges = {
        (a, b): tuple((b, c) for c in range(8) if locally_admissible(a, b, c))
        for a, b in vertices
    }
    return vertices, edges


def lies_on_directed_cycle(v, adj):
    """Finite breadth-first reachability, with a positive-length return."""
    frontier = list(adj[v])
    reached = set(frontier)
    while frontier:
        u = frontier.pop()
        if u == v:
            return True
        for w in adj[u]:
            if w not in reached:
                reached.add(w)
                frontier.append(w)
    return False


def certifying_finite_state_graph():
    vertices, adj = transition_graph()
    assert len(vertices) == 64
    assert sum(len(v) for v in adj.values()) == 102
    cyclic = {v for v in vertices if lies_on_directed_cycle(v, adj)}
    cycle = [(0, 2), (2, 3), (3, 0), (0, 4), (4, 5), (5, 0)]
    expected = set(cycle) | {(7, 7)}
    assert cyclic == expected, (cyclic, expected)
    assert (7, 7) in adj[(7, 7)]
    assert all(cycle[(i + 1) % 6] in adj[cycle[i]] for i in range(6))
    assert all([w for w in adj[v] if w in cyclic] == [cycle[(i + 1) % 6]]
               for i, v in enumerate(cycle))
    assert [w for w in adj[(7, 7)] if w in cyclic] == [(7, 7)]
    assert sum(top(a) + bottom(a) + rung(a) for a, _ in cycle) == 6
    assert top(7) + bottom(7) + rung(7) == 3
    print('FINITE_TRANSITION_CERTIFICATE_OK',len(vertices),
          sum(len(v) for v in adj.values()),sorted(cyclic))


def edges_of_prism(n):
    assert n >= 3
    e = []
    for i in range(n):
        e.append((2 * i, 2 * ((i + 1) % n)))
        e.append((2 * i + 1, 2 * ((i + 1) % n) + 1))
        e.append((2 * i, 2 * i + 1))
    assert len(e) == 3 * n
    assert len(set(tuple(sorted(pair)) for pair in e)) == len(e)
    return e


def adjacency_masks(edges):
    return tuple(sum(1 << k for k, f in enumerate(edges)
                     if k != j and (e[0] in f or e[1] in f))
                 for j, e in enumerate(edges))


def direct_valid(mask, adjacent):
    """Use the graph's original edge incidences, not local constraints."""
    for j, neighbor_mask in enumerate(adjacent):
        if not (mask >> j) & 1 and (mask & neighbor_mask).bit_count() != 1:
            return False
    return True


def direct_all_edge_subsets(n):
    adjacent = adjacency_masks(edges_of_prism(n))
    out = Counter()
    for mask in range(1 << (3 * n)):
        if direct_valid(mask, adjacent):
            out[mask.bit_count()] += 1
    predicted = Counter({3*n: 1})
    if n % 6 == 0:
        predicted[n] = 6
    assert out == predicted, (n, out, predicted)
    return out


def check_explicit_periodic(n):
    assert n >= 6 and n % 6 == 0
    sequence = [0, 2, 3, 0, 4, 5] * (n // 6)
    masks = []
    adjacent = adjacency_masks(edges_of_prism(n))
    for shift in range(6):
        mask = sum(((sequence[(i + shift) % n] >> (2 - k)) & 1) << (3*i+k)
                   for i in range(n) for k in range(3))
        assert mask.bit_count() == n
        assert direct_valid(mask, adjacent)
        masks.append(mask)
    assert len(set(masks)) == 6


def main():
    certifying_finite_state_graph()
    for n in range(3, 8):
        print('DIRECT_GRAPH_EXHAUSTIVE_OK',n, dict(sorted(direct_all_edge_subsets(n).items())))
    for n in (6, 12, 18, 24):
        check_explicit_periodic(n)
    print('PERIODIC_CONSTRUCTIONS_CHECKED_OK', '6,12,18,24')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
