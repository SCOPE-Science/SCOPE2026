"""Exact small-digraph certificate for site-dependent Moran fixation ranks.

Requirements: Python 3.10+ and SymPy 1.12+. Run: python verify_symbolic.py
No random sampling is used. Every loopless adjacency pattern in the stated
vertex/arc ranges is included, then isomorphic matrices are collapsed.
"""
from itertools import combinations, permutations
from collections import Counter
import sympy as sp

r, t = sp.symbols('r t')


def connected(A):
    n = len(A)
    for reverse in (False, True):
        reached = {0}
        pending = [0]
        while pending:
            v = pending.pop()
            for u in range(n):
                edge = A[u][v] if reverse else A[v][u]
                if edge and u not in reached:
                    reached.add(u)
                    pending.append(u)
        if len(reached) != n:
            return False
    return True


def canonical(A):
    n = len(A)
    return min(tuple(A[p[i]][p[j]] for i in range(n) for j in range(n) if i != j)
               for p in permutations(range(n)))


def representatives(n, maximum_arcs):
    edges = [(i, j) for i in range(n) for j in range(n) if i != j]
    seen = set()
    for m in range(n, maximum_arcs + 1):
        for choice in combinations(edges, m):
            A = [[int((i, j) in choice) for j in range(n)] for i in range(n)]
            if not connected(A):
                continue
            key = canonical(A)
            if key in seen:
                continue
            seen.add(key)
            # Reconstruct canonical matrix, maintaining row-major ordering.
            it = iter(key)
            B = [[0 for _ in range(n)] for _ in range(n)]
            for i, j in edges:
                B[i][j] = next(it)
            yield m, B


def fixation(n, A):
    states = list(range(1, (1 << n) - 1))
    order = {z: i for i, z in enumerate(states)}
    W = [[sp.Rational(A[i][j], sum(A[i])) for j in range(n)] for i in range(n)]
    Q = sp.zeros(len(states))
    b = sp.zeros(len(states), 1)
    for mask in states:
        i = order[mask]
        for source in range(n):
            source_mutant = bool(mask & (1 << source))
            for target in range(n):
                if source_mutant == bool(mask & (1 << target)):
                    continue
                rate = W[source][target] * (r if source_mutant else 1)
                if not rate:
                    continue
                destination = mask ^ (1 << target)
                Q[i, i] += rate
                if destination == (1 << n) - 1:
                    b[i] += rate
                elif destination:
                    Q[i, order[destination]] -= rate
    solution = Q.inv() * b
    return [sp.cancel(solution[order[1 << k]]) for k in range(n)]


def signs(poly):
    sequence = [sp.sign(c) for c in poly.all_coeffs() if c != 0]
    return sum(a != b for a, b in zip(sequence, sequence[1:]))


def main():
    counts = Counter()
    nonzero_comparisons = 0
    exceptional = []
    for n, max_arcs in ((2, 2), (3, 6), (4, 6)):
        for m, A in representatives(n, max_arcs):
            counts[(n, m)] += 1
            fixation_by_vertex = fixation(n, A)
            for i, j in combinations(range(n), 2):
                difference = sp.factor(fixation_by_vertex[i] - fixation_by_vertex[j])
                numerator, denominator = sp.fraction(difference)
                if numerator == 0:
                    continue
                nonzero_comparisons += 1
                shifted = sp.Poly(sp.expand(numerator.subs(r, t + 1)), t)
                count = signs(shifted)
                if count:
                    exceptional.append((n, m, A, i, j, count, difference))
    expected = {(2, 2): 1, (3, 3): 1, (3, 4): 2, (3, 5): 1,
                (3, 6): 1, (4, 4): 1, (4, 5): 4, (4, 6): 16}
    assert dict(counts) == expected, (counts, expected)
    assert len(exceptional) == 1, exceptional
    n, m, A, i, j, variation, difference = exceptional[0]
    assert (n, m, variation) == (4, 6, 1)
    assert A == [[0, 0, 0, 1], [0, 0, 0, 1], [0, 1, 0, 0], [1, 1, 1, 0]]
    assert (i, j) == (1, 3)
    P = 77760*r**10 + 163944*r**9 - 423738*r**8 - 2023272*r**7 \
        - 3747633*r**6 - 4662639*r**5 - 4212709*r**4 \
        - 2570307*r**3 - 956688*r**2 - 185526*r - 11880
    D = 116640*r**14 + 1165428*r**13 + 5613462*r**12 \
        + 17204508*r**11 + 37727010*r**10 + 63686499*r**9 \
        + 86411496*r**8 + 95625178*r**7 + 86411496*r**6 \
        + 63686499*r**5 + 37727010*r**4 + 17204508*r**3 \
        + 5613462*r**2 + 1165428*r + 116640
    assert sp.cancel(difference - r**3*P/D) == 0
    assert all(c > 0 for c in sp.Poly(D, r).all_coeffs())
    assert P.subs(r, 3) < 0 and P.subs(r, 4) > 0
    assert signs(sp.Poly(P, r)) == 1  # Exactly one positive real root, by Descartes and IVT.
    assert signs(sp.Poly(sp.expand(P.subs(r, t+1)), t)) == 1
    print('ISOMORPHISM_CLASS_COUNTS', dict(sorted(counts.items())))
    print('NONIDENTICAL_POSITION_COMPARISONS', nonzero_comparisons)
    print('POSITIVE_r_MINUS_1_SIGN_VARIATION_EXCEPTIONS', len(exceptional))
    print('UNIQUE_EXCEPTION', n, m, i+1, j+1)
    print('EXACT_RATIONAL_DIFFERENCE_AT_r_2', sp.factor(difference.subs(r, 2)))
    print('EXACT_RATIONAL_DIFFERENCE_AT_r_4', sp.factor(difference.subs(r, 4)))
    print('ROOT_BRACKET', (3, 4))
    print('PASS')

if __name__ == '__main__':
    main()
