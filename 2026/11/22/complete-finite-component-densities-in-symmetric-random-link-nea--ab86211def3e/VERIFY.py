"""Independent finite and asymptotic checks for nearest-neighbor forest component sizes.

Standard library only. Run: python3 VERIFY.py
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import exp

checks = 0

def verify(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def conditional_expected_counts(n, rational=True):
    """Exact reduced Markov chain on unseen-vertex count, tracking expected size counts."""
    F = Fraction if rational else float
    prob = [F(0)] * (n + 1)
    mass = [[F(0)] * (n + 1) for _ in range(n + 1)]
    prob[n] = F(1)
    for unseen in range(n, 0, -1):
        if unseen > 1:
            birth_prob = F(unseen - 1) / F(2 * n - unseen - 1)
            prob[unseen - 2] += birth_prob * prob[unseen]
            for size in range(2, n + 1):
                mass[unseen - 2][size] += birth_prob * (
                    mass[unseen][size] + (prob[unseen] if size == 2 else 0)
                )
        else:
            birth_prob = F(0)
        if unseen < n:
            grow_prob = 1 - birth_prob
            seen = n - unseen
            prob[unseen - 1] += grow_prob * prob[unseen]
            for size in range(2, n + 1):
                change = ((size - 1) * mass[unseen][size - 1]
                          - size * mass[unseen][size]) / seen
                mass[unseen - 1][size] += grow_prob * (mass[unseen][size] + change)
    verify(abs(float(prob[0]) - 1) < 1e-13, 'absorbing total mass')
    return mass[0]


def brute_edge_orders(n):
    edges = list(combinations(range(n), 2))
    counts = [0] * (n + 1)
    all_hist = [0] * (n + 1)
    total = 0
    for order in permutations(edges):
        seen = [False] * n
        parent = list(range(n))
        def root(i):
            while parent[i] != i:
                i = parent[i]
            return i
        for a, b in order:
            if not (seen[a] and seen[b]):
                parent[root(a)] = root(b)
                seen[a] = True
                seen[b] = True
        sizes = {}
        for i in range(n):
            rt = root(i)
            sizes[rt] = sizes.get(rt, 0) + 1
        for v in sizes.values():
            counts[v] += 1
        all_hist[len(sizes)] += 1
        total += 1
    return [Fraction(c, total) for c in counts], [Fraction(x, total) for x in all_hist]


def simpson(f, n=4000):
    if n % 2: raise ValueError('n even')
    h = 1 / n
    value = f(0.0) + f(1.0)
    for i in range(1, n):
        value += (4 if i % 2 else 2) * f(i * h)
    return h * value / 3


def density(k):
    return (k - 1) / 2 * simpson(
        lambda u: u * exp(-2 * u) * (-__import__('math').expm1(-u))**(k - 2)
    )

for n in range(2, 23):
    sizes = conditional_expected_counts(n)
    verify(sum(k * sizes[k] for k in range(2, n + 1)) == n,
           f'expected mass conservation at n={n}')
    verify(sum(sizes) == Fraction(n * (n - 1), 4 * n - 6),
           f'known total component mean at n={n}')
    verify(all(v >= 0 for v in sizes), f'nonnegative expected counts n={n}')
for n in (2, 3, 4):
    expected, hist = brute_edge_orders(n)
    reduced = conditional_expected_counts(n)
    for k in range(n + 1):
        verify(expected[k] == reduced[k], f'edge enumeration n={n}, size={k}')
    verify(sum(hist) == 1, f'finite histogram normalizes at n={n}')

for n in (350, 700):
    expected = conditional_expected_counts(n, rational=False)
    for k in range(2, 9):
        tolerance = 0.012 if n == 350 else 0.006
        verify(abs(float(expected[k])/n - density(k)) < tolerance,
               f'density convergence n={n}, size={k}')

verify(abs(density(2) - (1 - 3 * exp(-2)) / 8) < 1e-12,
       'analytical two-vertex density')
verify(sum(k * density(k) for k in range(2, 180)) > 0.99999999,
       'vertex-mass normalization of limiting density')
verify(abs(sum(density(k) for k in range(2, 180)) - .25) < 1e-10,
       'limiting component density 1/4')
print('VERIFY_OK', checks, 'assertions')
