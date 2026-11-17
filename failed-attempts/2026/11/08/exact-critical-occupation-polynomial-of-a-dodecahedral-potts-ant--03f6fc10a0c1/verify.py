"""Exact independent counts of three-state Potts spin configurations on GP(10,2).

Run: python3 verify.py. Only the Python standard library is needed.
"""

from collections import defaultdict
from fractions import Fraction

N = 10
COLORS = tuple((a, b) for a in range(3) for b in range(3))


def transfer_counts():
    """Trace of the 81-state cyclic column transfer with exact integer weights."""
    edges = []
    for state in range(81):
        a, b = COLORS[state // 9]
        c, _ = COLORS[state % 9]
        edges.append(tuple((9 * (state % 9) + next_col,
                            int(a == c) + int(a == b) + int(b == COLORS[next_col][1]),
                            int(a == 2) + int(b == 2))
                           for next_col in range(9)))
    critical = [0] * 7
    proper = [0] * 21
    for first in range(81):
        critical_states = {first: {(0, 0): 1}}
        proper_states = {first: {0: 1}}
        for _ in range(N):
            new_critical = {}
            new_proper = {}
            for state, terms in critical_states.items():
                for dest, bond, third in edges[state]:
                    out = new_critical.setdefault(dest, {})
                    for (old_b, old_k), count in terms.items():
                        b, k = old_b + bond, old_k + third
                        if b + k <= 6:
                            out[(b, k)] = out.get((b, k), 0) + count
            for state, terms in proper_states.items():
                for dest, bond, third in edges[state]:
                    if bond:
                        continue
                    out = new_proper.setdefault(dest, {})
                    for old_k, count in terms.items():
                        k = old_k + third
                        out[k] = out.get(k, 0) + count
            critical_states, proper_states = new_critical, new_proper
        for (b, k), count in critical_states.get(first, {}).items():
            if b + k == 6:
                critical[k] += count
        for k, count in proper_states.get(first, {}).items():
            proper[k] += count
    return critical, proper


def independent_dfs_counts():
    """Enumerate all branches whose partial energy does not exceed six.

    Uses vertices and adjacency rather than transfer states; it provides an
    independent, finite check of the critical coefficient vector.
    """
    vertices = tuple(range(20))
    edge_pairs = set()
    for i in range(10):
        edge_pairs.add(tuple(sorted((i, (i + 1) % 10))))
        edge_pairs.add((i, i + 10))
        edge_pairs.add(tuple(sorted((i + 10, (i + 2) % 10 + 10))))
    assert len(edge_pairs) == 30
    neighbors = {v: set() for v in vertices}
    for a, b in edge_pairs:
        neighbors[a].add(b)
        neighbors[b].add(a)
    assert {len(neighbors[v]) for v in vertices} == {3}

    # An explicit bipartite-frustration witness, with precisely six bad edges.
    outer = [1, 1, 2, 1, 2, 1, 1, 2, 1, 2]
    inner = [2, 2, 1, 1, 1, 2, 2, 1, 1, 1]
    witness = outer + inner
    assert sum(witness[a] == witness[b] for a, b in edge_pairs) == 6

    # Breadth-first traversal maximizes the number of already assigned neighbors.
    order = [0]
    seen = {0}
    for vertex in order:
        for target in sorted(neighbors[vertex]):
            if target not in seen:
                order.append(target)
                seen.add(target)
    assert len(order) == 20
    past = []
    done = set()
    for v in order:
        past.append(tuple(w for w in neighbors[v] if w in done))
        done.add(v)
    spins = [-1] * 20
    coefficients = [0] * 7

    def search(pos, energy, third_count):
        if pos == 20:
            if energy == 6:
                coefficients[third_count] += 1
            return
        v = order[pos]
        for spin in range(3):
            bond = sum(spins[w] == spin for w in past[pos])
            total = energy + bond + (spin == 2)
            if total <= 6:
                spins[v] = spin
                search(pos + 1, total, third_count + (spin == 2))
        spins[v] = -1

    search(0, 0, 0)
    return coefficients


def main():
    critical, proper = transfer_counts()
    dfs = independent_dfs_counts()
    expected = [250, 3000, 13800, 30400, 32760, 15840, 2720]
    assert critical == dfs == expected, (critical, dfs)
    assert [(i, x) for i, x in enumerate(proper) if x] == [(6, 2720), (7, 4160), (8, 320)]
    assert sum(critical) == 98770
    assert sum(proper) == 7200
    total = sum(expected)
    mean = Fraction(sum(j * count for j, count in enumerate(expected)), total)
    variance = Fraction(sum(j*j*count for j, count in enumerate(expected)), total) - mean**2
    assert mean == Fraction(34836, 9877), mean
    assert variance == Fraction(119729580, 97555129), variance
    print("VERIFIED: critical polynomial coefficients", critical)
    print("VERIFIED: proper three-coloring count", sum(proper))
    print("VERIFIED: critical degeneracy", total, "mean", mean, "variance", variance)


if __name__ == '__main__':
    main()
