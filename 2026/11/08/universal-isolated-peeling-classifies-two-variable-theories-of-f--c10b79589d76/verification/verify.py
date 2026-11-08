"""Independent finite-graph checks for two-variable peeling signatures.

Requires Python 3.10+ and networkx 3.x; networkx.graph_atlas_g() supplies one
unlabelled representative of every simple graph on at most seven vertices.
The finite orbit calculation is a check, not a proof for arbitrary orders.
"""
from collections import Counter, defaultdict
from itertools import combinations
import networkx as nx


def signature(graph):
    graph = graph.copy()
    layers = []
    while graph.number_of_nodes():
        count = graph.number_of_nodes()
        if count == 1:
            assert not layers, "a last singleton must be absorbed earlier"
            layers.append(("I", 1))
            graph.clear()
            break
        isolates = [v for v, degree in graph.degree() if degree == 0]
        universals = [v for v, degree in graph.degree() if degree == count - 1]
        if isolates:
            assert not universals
            assert not layers or layers[-1][0] != "I"
            layers.append(("I", min(len(isolates), 2)))
            graph.remove_nodes_from(isolates)
        elif universals:
            assert not layers or layers[-1][0] != "U"
            layers.append(("U", min(len(universals), 2)))
            graph.remove_nodes_from(universals)
        else:
            layers.append(("C",))
            break
    return tuple(layers)


def compress(values):
    index = {}
    result = []
    for value in values:
        if value not in index:
            index[value] = len(index)
        result.append(index[value])
    return result


def all_two_pebble_colors(graphs):
    """Greatest bisimulation refinement on all legal 0-, 1-, 2-pebble states.

    None means an unoccupied pebble. Each move replaces one pebble by any
    graph vertex. Equality, adjacency and occupancy are initially recorded.
    Colors are globally shared between all graph instances.
    """
    keys = []
    owner = []
    indexes = {}
    atomic = []
    for graph_id, graph in enumerate(graphs):
        vertices = [None] + list(graph.nodes())
        for first in vertices:
            for second in vertices:
                state = (graph_id, first, second)
                indexes[state] = len(keys)
                keys.append((first, second))
                owner.append(graph_id)
                atomic.append((first is not None, second is not None,
                               first is not None and first == second,
                               first is not None and second is not None
                               and graph.has_edge(first, second)))
    neighbors = []
    for idx, (first, second) in enumerate(keys):
        graph_id = owner[idx]
        vertices = list(graphs[graph_id].nodes())
        neighbors.append((
            [indexes[(graph_id, x, second)] for x in vertices],
            [indexes[(graph_id, first, y)] for y in vertices],
        ))
    colors = compress(atomic)
    for rounds in range(100):
        refinements = [
            (colors[i], frozenset(colors[j] for j in change_first),
             frozenset(colors[j] for j in change_second))
            for i, (change_first, change_second) in enumerate(neighbors)
        ]
        new_colors = compress(refinements)
        if new_colors == colors:
            break
        colors = new_colors
    else:
        raise AssertionError("No fixed point in 100 rounds")
    initial_colors = [colors[indexes[(i, None, None)]] for i in range(len(graphs))]
    return initial_colors, rounds, len(keys)


def min_spectrum_via_series(max_order):
    # R(z)=z+(2z^2+z^4(1+z+z^2))/(1-z-z^2).
    inv = [0] * (max_order + 1)
    inv[0] = 1
    for n in range(1, max_order + 1):
        inv[n] = inv[n-1] + (inv[n-2] if n >= 2 else 0)
    return [int(n == 1) + sum(coeff * inv[n-power]
                                  for power, coeff in ((2, 2), (4, 1),
                                                       (5, 1), (6, 1))
                                  if n >= power)
            for n in range(max_order + 1)]


def main():
    graphs = list(nx.graph_atlas_g())
    assert len(graphs) == 1253
    assert max(len(graph) for graph in graphs) == 7
    sigs = [signature(graph) for graph in graphs]
    colors, iterations, states = all_two_pebble_colors(graphs)
    grouped = defaultdict(set)
    other = defaultdict(set)
    for sig, color in zip(sigs, colors):
        grouped[sig].add(color)
        other[color].add(sig)
    assert len(grouped) == len(other) == 55
    assert all(len(colorset) == 1 for colorset in grouped.values())
    assert all(len(sigset) == 1 for sigset in other.values())
    min_order = {}
    for graph, sig in zip(graphs, sigs):
        min_order[sig] = min(len(graph), min_order.get(sig, 10**9))
    actual = Counter(min_order.values())
    predicted = min_spectrum_via_series(7)
    assert all(actual[n] == predicted[n] for n in range(1, 8))
    assert actual[0] == 1
    # One extra arithmetic check beyond the finite atlas.
    assert min_spectrum_via_series(12) == [0,1,2,2,5,8,14,22,36,58,94,152,246]
    print("Nonisomorphic simple graphs tested:", len(graphs))
    print("Maximum order:", max(len(graph) for graph in graphs))
    print("Legal 0-, 1-, 2-pebble states:", states)
    print("Stable two-pebble refinement rounds:", iterations)
    print("Two-pebble classes:", len(other))
    print("Distinct peeling signatures:", len(grouped))
    print("Mismatched class assignments:", 0)
    print("Min-representative spectrum orders 1..7:",
          [actual[n] for n in range(1, 8)])
    print("Rational series coefficients orders 1..12:",
          min_spectrum_via_series(12)[1:])
    print("PASS")


if __name__ == "__main__":
    main()
