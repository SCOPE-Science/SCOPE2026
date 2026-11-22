"""Direct finite checks for multipartite peak runs and random-initial-color stabilization."""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import factorial


def falling(a, j):
    out = 1
    for v in range(j):
        out *= a - v
    return out if j <= a else 0


def multinomial_occupancy_at_least(N, k, demands):
    # Exact probability that every named class has at least its specified count.
    total = 0
    for labels in product(range(k), repeat=N):
        counts = Counter(labels)
        if all(counts[c] >= demands[c] for c in range(k)):
            total += 1
    return Fraction(total, k**N)


def joint_tail(parts, k, js):
    N = sum(parts)
    J = sum(js)
    if J > N:
        return Fraction(0)
    positive = [c for c in range(k) if js[c]]
    occupancy = multinomial_occupancy_at_least(N, k, js)
    enumerator = 0
    for chosen in product(range(len(parts)), repeat=len(positive)):
        m = [0] * len(parts)
        for c, i in zip(positive, chosen):
            m[i] += js[c]
        count = 1
        for a, t in zip(parts, m):
            count *= falling(a, t)
        enumerator += count
    return occupancy * Fraction(enumerator, falling(N, J))


def run_lengths(vertices, perm, colors, k):
    groups = [[] for _ in range(k)]
    for v in perm:
        groups[colors[v]].append(vertices[v])
    runs = []
    for g in groups:
        if not g:
            runs.append(0)
        else:
            runs.append(next((i for i, x in enumerate(g) if x != g[0]), len(g)))
    return tuple(runs)


def brute_law(parts, k):
    verts = tuple(i for i, a in enumerate(parts) for _ in range(a))
    N = len(verts)
    law = Counter()
    for perm in permutations(range(N)):
        for colors in product(range(k), repeat=N):
            law[run_lengths(verts, perm, colors, k)] += 1
    den = factorial(N) * k**N
    return {a: Fraction(b, den) for a, b in law.items()}


def verify():
    cases = [((1, 1, 1), 1), ((1, 1, 1), 2),
             ((1, 1, 1), 3), ((2, 1, 1), 2),
             ((2, 2, 1), 2), ((1, 2, 2), 3),
             ((2, 2, 2), 1), ((2, 2, 2), 2),
             ((1, 2, 3), 2)]
    comparisons = 0
    for parts, k in cases:
        law = brute_law(parts, k)
        N = sum(parts)
        assert sum(law.values()) == 1
        for js in product(range(0, N+1), repeat=k):
            if sum(js) > N:
                continue
            observed = sum((pr for counts, pr in law.items()
                            if all(counts[c] >= js[c] for c in range(k))), Fraction(0))
            expected = joint_tail(parts, k, js)
            assert expected == observed, (parts, k, js, expected, observed)
            comparisons += 1
        if k >= 2:
            p_low = sum((pr for counts, pr in law.items() if counts[0] <= 1), Fraction(0))
            p_geo = 1 - sum(Fraction(a*a, N*N) for a in parts)
            lower = Fraction(1-sum(Fraction(a*a,N*N) for a in parts),N-1)
            assert p_low - p_geo >= lower, (parts,k,p_low,p_geo,lower)
    # Exact convergence of one-color tails to geometric mixtures in a balanced example.
    for r in (2, 3, 4):
        for n in (10, 50, 200):
            parts = (n,) * r
            N = r * n
            for j in (1, 2, 3, 4, 5):
                tail = sum((Fraction(falling(a,j),falling(N,j)) for a in parts), Fraction(0))
                limit = Fraction(r, r**j)
                assert abs(tail-limit) <= Fraction(j*(j-1), N), (r,n,j)
    # For one initial color, the first-run probability error has an exact formula.
    for parts in [(1,1,1), (2,3,1), (4,4), (6,5,3)]:
        N = sum(parts)
        empirical_one = 1 - sum(Fraction(falling(a,2),falling(N,2)) for a in parts)
        mixture_one = 1 - sum(Fraction(a*a, N*N) for a in parts)
        exact_gap = Fraction(1-sum(Fraction(a*a,N*N) for a in parts),N-1)
        assert empirical_one - mixture_one == exact_gap
    print('DIRECT_LABEL_COLOR_ENUMERATION_PASS cases=',len(cases),'joint_tails=',comparisons)
    print('EXACT_TAIL_IDENTITY_AND_RATE_WITNESSES_PASS')
    print('VERIFY_OK')

if __name__ == '__main__':
    verify()
