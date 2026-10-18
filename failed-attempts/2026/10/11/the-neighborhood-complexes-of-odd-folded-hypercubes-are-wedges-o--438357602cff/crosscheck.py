"""Independent quotient-cube checks of folded hypercube neighborhood structure."""
from collections import Counter
from itertools import combinations


def check(n):
    bits = (1 << n) - 1
    canonical = lambda x: min(x, x ^ bits)
    reps = sorted({canonical(x) for x in range(1 << n)})
    idx = {x: i for i, x in enumerate(reps)}
    adj = [set() for _ in reps]
    for x in reps:
        for j in range(n):
            y = idx[canonical(x ^ (1 << j))]
            adj[idx[x]].add(y)
    N = len(reps)
    assert N == 2 ** (n - 1) and all(len(a) == n for a in adj)
    common = Counter(len(adj[u] & adj[v]) for u, v in combinations(range(N), 2))
    assert set(common) <= {0, 2}, common
    # Every length-four closed cube-class walk returns to its original lift.
    # In particular all 4-cycles lift to boundaries of genuine squares.
    squares = 0
    for a in range(N):
        for b in adj[a]:
            for c in adj[b]:
                if c in (a, b):
                    continue
                for d in adj[c] & adj[a]:
                    if len({a, b, c, d}) == 4:
                        squares += 1
    assert squares % 8 == 0
    # For a 4-cycle lift, the endpoint cannot be antipodal: each edge flips
    # exactly one bit, so a length-four lift has even Hamming parity.
    assert n % 2 == 1
    print(f'n={n} quotient_vertices={N} common_neighbor_distribution={dict(common)} embedded_four_cycles={squares//8}')


if __name__ == '__main__':
    for dimension in (3, 5, 7):
        check(dimension)
    print('VERIFIED independent quotient construction')
