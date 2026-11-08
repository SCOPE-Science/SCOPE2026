"""Brute-force the zero-forcing and token-slide state spaces of circular ladders.
The finite computations supplement, but do not replace, the symbolic proof.
"""
from itertools import combinations
from collections import Counter, deque


def graph(n):
    return [tuple(sorted({(v // n) * n + (v % n + d) % n for d in (-1, 1)} |
                          {v + n if v < n else v - n})) for v in range(2 * n)]


def closure(n, neighbors, chosen):
    blue = set(chosen)
    while True:
        new = {next(iter(set(neighbors[v]) - blue)) for v in blue
               if len(set(neighbors[v]) - blue) == 1}
        if not new - blue:
            return frozenset(blue)
        blue |= new


def templates(n):
    U = lambda j: j % n
    L = lambda j: n + j % n
    reps = ((U(0), U(1), U(2), U(3)),
            (U(0), U(1), U(2), L(0)),
            (U(0), U(1), U(-2), L(0)),
            (U(0), U(1), L(0), L(1)),
            (U(1), U(2), L(0), L(1)))
    families = []
    for rep in reps:
        orbit = set()
        for swap in (0, 1):
            for sign in (-1, 1):
                for shift in range(n):
                    orbit.add(frozenset((((v // n + swap) % 2) * n +
                                         (sign * (v % n) + shift) % n) for v in rep))
        families.append(orbit)
    return families


def component_sizes(nodes, adj):
    unseen = set(nodes)
    sizes = []
    while unseen:
        root = unseen.pop()
        comp = {root}
        q = deque([root])
        while q:
            for v in adj[q.popleft()]:
                if v in unseen:
                    unseen.remove(v)
                    comp.add(v)
                    q.append(v)
        sizes.append(len(comp))
    return Counter(sizes)


def main():
    for n in range(5, 13):
        adj = graph(n)
        N = 2 * n
        assert all(len(x) == 3 for x in adj)
        families = templates(n)
        assert all(not families[i] & families[j] for i in range(5) for j in range(i))
        expected = set().union(*families)
        assert list(map(len, families)) == [2*n, 4*n, 4*n, n, 2*n]
        # No three-vertex set forces all. For larger n, this is established by proof.
        if n <= 9:
            for triple in combinations(range(N), 3):
                assert len(closure(n, adj, triple)) < N
        actual = {frozenset(s) for s in combinations(range(N), 4)
                  if len(closure(n, adj, s)) == N}
        assert actual == expected, (n, len(actual), len(expected), len(actual ^ expected))
        slides = {s: {frozenset((s-{v})|{w}) for v in s for w in adj[v]
                      if w not in s and frozenset((s-{v})|{w}) in actual} for s in actual}
        degs = Counter(map(len, slides.values()))
        if n == 5:
            assert degs == Counter({0: 15, 1: 20, 2: 30})
            assert component_sizes(actual, slides) == Counter({1: 15, 4: 10, 5: 2})
        else:
            assert degs == Counter({0: 13*n})
        print(f'n={n:2d}, optimal_sets={len(actual):3d}, degrees={dict(sorted(degs.items()))}, '
              f'components={dict(sorted(component_sizes(actual, slides).items()))}')
    print('EXHAUSTIVE_OK')

if __name__ == '__main__':
    main()
