"""Exact exhaustive check of one-patch spectral-capacity degree rules.

Requires Python 3.10+ and SymPy. Every simple labelled graph up to six
vertices is considered; characteristic polynomials and comparisons are exact.
"""
import collections
import functools
import itertools
import json
import sympy as sp

X = sp.Symbol('x')

@functools.lru_cache(None)
def pairs(n):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))

@functools.lru_cache(None)
def matrix(n, mask):
    a = [[0] * n for _ in range(n)]
    for k, (i, j) in enumerate(pairs(n)):
        if (mask >> k) & 1:
            a[i][j] = a[j][i] = 1
    return tuple(tuple(row) for row in a)

def is_connected(n, mask):
    if n <= 1:
        return True
    a = matrix(n, mask)
    reached = {0}
    frontier = [0]
    while frontier:
        v = frontier.pop()
        for w in range(n):
            if a[v][w] and w not in reached:
                reached.add(w)
                frontier.append(w)
    return len(reached) == n

@functools.lru_cache(None)
def after_deletion(n, mask, deleted):
    remap = {old: new for new, old in enumerate(v for v in range(n) if v != deleted)}
    positions = {edge: k for k, edge in enumerate(pairs(n - 1))}
    result = 0
    for k, (i, j) in enumerate(pairs(n)):
        if (mask >> k) & 1 and i != deleted and j != deleted:
            a, b = sorted((remap[i], remap[j]))
            result |= 1 << positions[a, b]
    return result

@functools.lru_cache(None)
def characteristic(n, mask):
    return tuple(int(c) for c in sp.Matrix(matrix(n, mask)).charpoly(X).all_coeffs())

@functools.lru_cache(None)
def perron_bracket(coefficients):
    poly = sp.Poly.from_list(coefficients, gens=X)
    return sp.polys.polytools.intervals(poly, eps=sp.Rational(1, 10**9))[-1][0]

@functools.lru_cache(None)
def compare(a, b):
    """The exact ordering of the largest real roots of monic integer polynomials."""
    if a == b:
        return 0
    la, ua = perron_bracket(a)
    lb, ub = perron_bracket(b)
    if ua < lb:
        return -1
    if ub < la:
        return 1
    gcd = sp.gcd(sp.Poly.from_list(a, gens=X), sp.Poly.from_list(b, gens=X))
    if gcd.degree() > 0:
        for (low, high), _ in sp.polys.polytools.intervals(gcd, eps=sp.Rational(1, 10**9)):
            if not (high < la or low > ua or high < lb or low > ub):
                return 0
    raise ArithmeticError('Overlapping root enclosures without a shared root')

@functools.lru_cache(None)
def relabelings(n):
    oldpairs = pairs(n)
    position = {edge: k for k, edge in enumerate(oldpairs)}
    return tuple(tuple(position[tuple(sorted((perm[i], perm[j])))] for i, j in oldpairs)
                 for perm in itertools.permutations(range(n)))

def canonical(n, mask):
    # Lexicographically minimal edge mask across every vertex permutation.
    best = mask
    for permuted_bits in relabelings(n):
        cand = 0
        for oldbit, newbit in enumerate(permuted_bits):
            if mask >> oldbit & 1:
                cand |= 1 << newbit
        best = min(best, cand)
    return best

def edges_for(n, mask):
    return [list(edge) for k, edge in enumerate(pairs(n)) if mask >> k & 1]

records = []
for n in range(2, 7):
    total = 0
    any_bad = []
    all_bad = []
    for mask in range(1 << len(pairs(n))):
        if not is_connected(n, mask):
            continue
        total += 1
        degrees = [sum(row) for row in matrix(n, mask)]
        polynomials = [characteristic(n - 1, after_deletion(n, mask, v)) for v in range(n)]
        optimum = [v for v in range(n) if all(compare(polynomials[v], t) <= 0 for t in polynomials)]
        maximum = [v for v in range(n) if degrees[v] == max(degrees)]
        if any(v not in optimum for v in maximum):
            any_bad.append(mask)
        if not any(v in optimum for v in maximum):
            all_bad.append(mask)
    summary = {'vertices': n, 'connected_labelled': total,
               'bad_arbitrary_degree_tie': len(any_bad),
               'bad_all_max_degree': len(all_bad)}
    if n in (5, 6):
        exceptions = any_bad if n == 5 else all_bad
        groups = collections.Counter(canonical(n, mask) for mask in exceptions)
        summary['exception_classes'] = [
            {'canonical_mask': m, 'edges': edges_for(n, m), 'labelled_count': count}
            for m, count in sorted(groups.items())]
    records.append(summary)

assert [r['connected_labelled'] for r in records] == [1, 4, 38, 728, 26704]
assert [r['bad_arbitrary_degree_tie'] for r in records[:4]] == [0, 0, 0, 150]
assert [r['bad_all_max_degree'] for r in records] == [0, 0, 0, 0, 540]
assert sorted(g['labelled_count'] for g in records[3]['exception_classes']) == [30, 60, 60]
assert sorted(g['labelled_count'] for g in records[4]['exception_classes']) == [180, 360]

# The explicit canonical-graph spectral inequalities are a second test of the
# two six-vertex classes, not assumptions used in finding those classes.
for group in records[4]['exception_classes']:
    m = group['canonical_mask']
    degrees = [sum(row) for row in matrix(6, m)]
    polynomials = [characteristic(5, after_deletion(6, m, v)) for v in range(6)]
    optimal = [v for v in range(6) if all(compare(polynomials[v], b) <= 0 for b in polynomials)]
    maximum = [v for v in range(6) if degrees[v] == max(degrees)]
    assert not set(optimal).intersection(maximum)
    group['optimum_vertices'] = optimal
    group['maximum_degree_vertices'] = maximum
    group['optimum_characteristic_polynomial'] = [list(polynomials[v]) for v in optimal]
    group['max_degree_characteristic_polynomial'] = [list(polynomials[v]) for v in maximum]

print(json.dumps({'theorem': 'two_threshold_degree_rule', 'exact': True,
                  'enumeration': records}, sort_keys=True, indent=2))
