"""Exact small-rank verification of the strong Morse subdivided-star collapse."""
from itertools import permutations, combinations, product

def inspect(n):
    center = 0
    inner = tuple(range(1, n + 1))
    leaf = tuple(range(n + 1, 2*n + 1))
    adjacency = {v: set() for v in range(2*n + 1)}
    for u, w in zip(inner, leaf):
        adjacency[center].add(u)
        adjacency[u].add(center)
        adjacency[u].add(w)
        adjacency[w].add(u)
    def a(i): return (leaf[i], inner[i])
    def b(i): return (inner[i], leaf[i])
    def c(i): return (inner[i], center)
    def d(i): return (center, inner[i])
    realized = set()
    for order in permutations(range(2*n + 1)):
        earlier = set()
        matching = []
        for v in order:
            neighbors = adjacency[v] & earlier
            if len(neighbors) == 1:
                matching.append((v, next(iter(neighbors))))
            earlier.add(v)
        realized.add(frozenset(matching))
    maximal = {f for f in realized if not any(f < g for g in realized)}
    predicted = set()
    for k in range(n + 1):
        for I in combinations(range(n), k):
            I = set(I)
            if k == n or n - k >= 2:
                predicted.add(frozenset(
                    [x for i in I for x in (a(i), c(i))] +
                    [b(i) for i in range(n) if i not in I]))
    for i in range(n):
        for side in (a(i), b(i)):
            predicted.add(frozenset(
                [d(i), side] + [x for j in range(n) if j != i for x in (a(j), c(j))]))
    assert maximal == predicted, (n, 'facet comparison', maximal ^ predicted)
    assert len(maximal) == 2**n + n
    assert max(map(len, maximal)) == 2*n
    # Exact dominated-vertex elimination on facets, rather than trusting a homology rank.
    living = set(maximal)
    def delete_dominated(v, apex):
        nonlocal living
        containing = [f for f in living if v in f]
        assert containing and all(apex in f for f in containing), (n, v, apex)
        reduced = {frozenset(f - {v}) for f in living}
        living = {f for f in reduced if not any(f < g for g in reduced)}
    if n >= 2:
        for i in range(n):
            j = (i + 1) % n
            delete_dominated(d(i), a(j))
        for i in range(n):
            delete_dominated(c(i), a(i))
        expected = {frozenset(a(i) if choice[i] else b(i) for i in range(n))
                    for choice in product((False, True), repeat=n)}
        assert living == expected, (n, living ^ expected)
        # The final complex is exactly the join of n copies of S^0.
        assert len(living) == 2**n and all(len(f) == n for f in living)
    else:
        # The length-two path is the known nonbranching exception.
        assert len(maximal) == 3
    return len(realized), len(maximal)

if __name__ == '__main__':
    for n in range(1, 5):
        gradients, facets = inspect(n)
        print(f'n={n} gradients={gradients} maximal_facets={facets}')
    print('VERIFY_OK: exhaustive vertex orders and dominated-vertex reductions, n=1..4')
