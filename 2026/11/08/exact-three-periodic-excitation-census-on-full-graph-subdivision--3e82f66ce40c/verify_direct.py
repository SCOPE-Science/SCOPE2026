"""Direct dynamics tests for a three-state excitation rule on full subdivisions.

Uses only Python's standard library. A graph is (vertex_count, edges) with
original vertices labelled 0,...,vertex_count-1 and edges as unordered pairs.
The subdivision gives one new vertex per edge, in listed edge order.
"""
from itertools import combinations, product


def expected(n, edges):
    total = 0
    for c in product(range(3), repeat=n):
        weight = 1
        for v in range(n):
            degree = sum(c[w] == (c[v] + 2) % 3
                         for a, b in edges
                         for w in ((b,) if a == v else (a,) if b == v else ()))
            weight *= (1 << degree) - 1
            if not weight:
                break
        total += weight
    return total


def actual(n, edges):
    count = n + len(edges)
    neighbors = [[] for _ in range(count)]
    for j, (a, b) in enumerate(edges, start=n):
        neighbors[j].extend((a, b))
        neighbors[a].append(j)
        neighbors[b].append(j)

    def update(state):
        result = []
        for v, value in enumerate(state):
            if value != 0:
                result.append((value + 1) % 3)
            else:
                result.append(int(any(state[w] == 1 for w in neighbors[v])))
        return tuple(result)

    count_3 = 0
    fixed = 0
    for state in product(range(3), repeat=count):
        after = update(update(update(state)))
        if after == state:
            if update(state) == state:
                fixed += 1
            else:
                count_3 += 1
    return fixed, count_3


def main():
    graphs = [
        ('triangle', 3, [(0, 1), (1, 2), (2, 0)]),
        ('complete-four', 4, list(combinations(range(4), 2))),
        ('four-cycle', 4, [(0, 1), (1, 2), (2, 3), (3, 0)]),
        ('bipartite-2-by-3', 5, [(a, b) for a in range(2) for b in range(2, 5)]),
        ('six-cycle', 6, [(i, (i + 1) % 6) for i in range(6)]),
    ]
    states = 0
    for title, n, edges in graphs:
        predicted = expected(n, edges)
        fixed, periodic = actual(n, edges)
        assert fixed == 1
        assert periodic == predicted, (title, predicted, periodic)
        states += 3 ** (n + len(edges))
        print(f'{title}: |V(S(H))|={n + len(edges)}, fixed=1, '
              f'primitive3={periodic}, exact_formula={predicted}, PASS')
    print(f'PASS total_states={states}')


if __name__ == '__main__':
    main()
