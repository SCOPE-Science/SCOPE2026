"""Independent edge-extension and graph-cycle tests for subdivision waves.

Uses only Python standard library. Tests the exact local phase constraints by
enumerating every ternary label on original nodes and all permitted labels
on inserted edge nodes; independent of the weighted product implementation.
"""
from itertools import combinations, product


def connected(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    reached = {0}
    todo = [0]
    while todo:
        for u in adj[todo.pop()]:
            if u not in reached:
                reached.add(u)
                todo.append(u)
    return len(reached) == n


def has_three_divisible_cycle(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)

    def explore(first, current, seen):
        for nxt in adj[current]:
            if nxt == first and len(seen) >= 3 and len(seen) % 3 == 0:
                return True
            if nxt not in seen and explore(first, nxt, seen | {nxt}):
                return True
        return False
    return any(explore(v, v, {v}) for v in range(n))


def count_by_extensions(n, edges):
    total = 0
    for core in product(range(3), repeat=n):
        candidates = [tuple(sorted({(core[a] - 1) % 3,
                                   (core[b] - 1) % 3})) for a, b in edges]
        for extension in product(*candidates):
            phase = core + extension
            nbr = [[] for _ in phase]
            for j, (a, b) in enumerate(edges, start=n):
                nbr[a].append(j)
                nbr[b].append(j)
                nbr[j].extend([a, b])
            if all(any(phase[w] == (phase[v] + 1) % 3 for w in nbr[v])
                   for v in range(len(phase))):
                total += 1
    return total


def count_by_local_product(n, edges):
    adjacency = [set() for _ in range(n)]
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    total = 0
    for c in product(range(3), repeat=n):
        ways = 1
        for v in range(n):
            k = sum(c[w] == (c[v] + 2) % 3 for w in adjacency[v])
            ways *= 2 ** k - 1
        total += ways
    return total


def main():
    checked = 0
    total_positive = 0
    for n in range(2, 5):
        complete_edges = list(combinations(range(n), 2))
        for mask in range(1 << len(complete_edges)):
            edges = [e for j, e in enumerate(complete_edges) if mask >> j & 1]
            if not connected(n, edges):
                continue
            a = count_by_local_product(n, edges)
            b = count_by_extensions(n, edges)
            c = has_three_divisible_cycle(n, edges)
            assert a == b, (n, edges, a, b)
            assert (a > 0) == c, (n, edges, a, c)
            checked += 1
            total_positive += (a > 0)
    print(f'connected_labelled_graphs_n=2..4={checked}, '
          f'graphs_with_primitive3={total_positive}, local=extensions=cycle_criterion: PASS')
    for n in range(3, 9):
        edges = list(combinations(range(n), 2))
        # Count from color-class sizes, not the explicit coloring sum.
        from math import factorial
        count = 0
        for a in range(1, n - 1):
            for b in range(1, n - a):
                c = n - a - b
                coeff = factorial(n) // (factorial(a) * factorial(b) * factorial(c))
                count += coeff * (2 ** c - 1) ** a * (2 ** a - 1) ** b * (2 ** b - 1) ** c
        if n <= 5:
            assert count_by_local_product(n, edges) == count
        assert count % 3 == 0
        print(f'S(K_{n}): primitive3={count}, temporal_orbits={count // 3}, PASS')
    print('PASS')


if __name__ == '__main__':
    main()
