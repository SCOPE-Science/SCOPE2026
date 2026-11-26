"""Standalone finite verification for random-order tree Cholesky fill formulas.
Run: python3 verify.py. Uses Python standard library only.
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import permutations, product
from math import factorial
from random import Random

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def path_edges(n):
    return [(i, i + 1) for i in range(n - 1)]


def star_edges(n):
    return [(0, i) for i in range(1, n)]


def graph_fill(n, edges, order):
    g = [set() for _ in range(n)]
    original = {tuple(sorted(e)) for e in edges}
    for a, b in edges:
        g[a].add(b); g[b].add(a)
    fill = set()
    for v in order:
        nbrs = sorted(g[v])
        for i, a in enumerate(nbrs):
            for b in nbrs[i + 1:]:
                if b not in g[a]:
                    g[a].add(b); g[b].add(a)
                    pair = (a, b)
                    check(pair not in original and pair not in fill, 'repeated fill')
                    fill.add(pair)
        for a in nbrs:
            g[a].remove(v)
        g[v].clear()
    return fill


def distances(n, edges):
    g = [set() for _ in range(n)]
    for a, b in edges:
        g[a].add(b); g[b].add(a)
    out = [[-1]*n for _ in range(n)]
    for s in range(n):
        q = deque([s]); out[s][s] = 0
        while q:
            u = q.popleft()
            for v in g[u]:
                if out[s][v] < 0:
                    out[s][v] = out[s][u] + 1
                    q.append(v)
    return out


def tree_path(n, edges, a, b):
    g = [set() for _ in range(n)]
    for x, y in edges:
        g[x].add(y); g[y].add(x)
    q = deque([a]); prev = {a: None}
    while q:
        x = q.popleft()
        if x == b:
            break
        for y in g[x]:
            if y not in prev:
                prev[y] = x; q.append(y)
    path = [b]
    while path[-1] != a:
        path.append(prev[path[-1]])
    return path[::-1]


def fill_from_paths(n, edges, order):
    original = {tuple(sorted(e)) for e in edges}
    time = {v: i for i, v in enumerate(order)}
    ans = set()
    for a in range(n):
        for b in range(a + 1, n):
            if (a, b) in original:
                continue
            path = tree_path(n, edges, a, b)
            if all(time[v] < min(time[a], time[b]) for v in path[1:-1]):
                ans.add((a, b))
    return ans


def expectation(n, edges):
    D = distances(n, edges)
    return sum((Fraction(2, D[a][b] * (D[a][b] + 1))
                for a in range(n) for b in range(a + 1, n)
                if D[a][b] >= 2), Fraction(0))


def harmonic(n, power=1):
    return sum((Fraction(1, k**power) for k in range(1, n + 1)), Fraction(0))


def pgf(n):
    probs = [Fraction(1)]
    for k in range(3, n + 1):
        next_probs = [Fraction(0)] * (len(probs) + 1)
        for j, p in enumerate(probs):
            next_probs[j] += p * Fraction(2, k)
            next_probs[j + 1] += p * Fraction(k - 2, k)
        probs = next_probs
    return probs


def prufer_edges(seq, n):
    degree = [1] * n
    for x in seq:
        degree[x] += 1
    edges = []
    for x in seq:
        leaf = min(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, x))
        degree[leaf] -= 1; degree[x] -= 1
    left = [i for i in range(n) if degree[i] == 1]
    edges.append(tuple(left))
    return edges


def exact_symbolic_schur(n, edges, order):
    # Unit conductances with a unit diagonal grounding. Every pivot is positive.
    a = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a[i][i] = Fraction(1)
    for i, j in edges:
        a[i][i] += 1; a[j][j] += 1
        a[i][j] -= 1; a[j][i] -= 1
    original = {tuple(sorted(e)) for e in edges}
    alive = set(range(n)); found = set()
    for v in order:
        check(a[v][v] > 0, 'nonpositive pivot')
        neigh = [u for u in alive if u != v and a[v][u] != 0]
        for k in neigh:
            for j in neigh:
                a[k][j] -= a[k][v] * a[v][j] / a[v][v]
        alive.remove(v)
        for i in alive:
            for j in alive:
                if i < j and a[i][j] != 0 and (i,j) not in original:
                    found.add((i,j))
    return found

# All path permutations up to n=8, including exact finite law.
for n in range(2, 9):
    e = path_edges(n)
    counts = Counter()
    for order in permutations(range(n)):
        fill = graph_fill(n, e, order)
        counts[len(fill)] += 1
        check(fill == fill_from_paths(n, e, order), 'path theorem')
        priority = {v: i for i, v in enumerate(order)}
        t = [priority[i] for i in range(n)]
        lmax = sum(t[i] == max(t[:i+1]) for i in range(n))
        rmax = sum(t[i] == max(t[i:]) for i in range(n))
        check(len(fill) == n + 1 - lmax - rmax, 'record identity')
    expected = pgf(n)
    check(all(Fraction(counts[k], factorial(n)) == expected[k]
              for k in range(n - 1)), 'path law')
    mean = sum((k*p for k,p in enumerate(expected)), Fraction(0))
    variance = sum(((k-mean)**2*p for k,p in enumerate(expected)), Fraction(0))
    check(mean == n + 1 - 2*harmonic(n), 'mean')
    check(variance == 2*harmonic(n) - 4*harmonic(n,2) + 2, 'variance')
    check(expectation(n,e) == mean, 'distance expectation')
    check(expected[0] == Fraction(2**(n-1), factorial(n)), 'zero fill chance')
    if n >= 3:
        check(expected[n-2] == Fraction(2, n*(n-1)), 'max fill chance')

# Every labelled tree n<=6: exact expected fill formula and sharp extrema.
for n in range(2, 7):
    lower = n + 1 - 2*harmonic(n)
    upper = Fraction((n-1)*(n-2), 6)
    for seq in product(range(n), repeat=n-2):
        e = prufer_edges(seq,n)
        val = expectation(n,e)
        check(lower <= val <= upper, 'sharp tree bounds')
        degrees = [sum(v in edge for edge in e) for v in range(n)]
        is_path = max(degrees) <= 2
        is_star = max(degrees) == n-1
        check((val == lower) == is_path, 'unique path minimizer')
        check((val == upper) == (is_star or n<=3), 'unique star maximizer')

# Tree/path-pair equivalence for all labelled trees on four vertices.
for seq in product(range(4), repeat=2):
    e = prufer_edges(seq,4)
    exact = Counter()
    for order in permutations(range(4)):
        a = graph_fill(4,e,order)
        b = fill_from_paths(4,e,order)
        check(a == b, 'tree fill path equivalence')
        exact[len(a)] += 1
    observed = sum((Fraction(k*v, factorial(4)) for k,v in exact.items()),Fraction(0))
    check(observed == expectation(4,e), 'tree expected fill')

rng = Random(1729)
for n in range(3, 10):
    edges = prufer_edges([rng.randrange(n) for _ in range(n - 2)],n)
    for _ in range(25):
        order = list(range(n)); rng.shuffle(order)
        check(graph_fill(n,edges,order) == exact_symbolic_schur(n,edges,order),
              'rational matrix elimination')

print('VERIFICATION_OK', CHECKS, 'assertions')
