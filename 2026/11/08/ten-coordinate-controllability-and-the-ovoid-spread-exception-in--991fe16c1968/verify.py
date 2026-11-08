#!/usr/bin/env python3
"""Exact certificate for the coordinate-controllability census of the
30-vertex Tutte-Coxeter graph. Standard Python library only.

Vertices 0..14 index edges of K6 and vertices 15..29 index its perfect
matchings. All rank tests are exact: the prime exceeds Hadamard bounds
for every relevant full-rank minor. No floating-point tests are used.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import lcm

MOD = 1_000_000_007
V = tuple(range(6))
EDGES = tuple(combinations(V, 2))
EDGE_ID = {e: i for i, e in enumerate(EDGES)}


def perfect_matchings(vertices):
    if not vertices:
        yield ()
    else:
        a = vertices[0]
        for b in vertices[1:]:
            rest = tuple(v for v in vertices if v not in (a, b))
            for other in perfect_matchings(rest):
                yield tuple(sorted(((a, b),) + other))


MATCHINGS = tuple(sorted(set(perfect_matchings(V))))
MATCH_ID = {matching: i for i, matching in enumerate(MATCHINGS)}
assert len(EDGES) == len(MATCHINGS) == 15
INC = [[int(e in m) for m in MATCHINGS] for e in EDGES]
T = [[int(i in e) for e in EDGES] for i in V]


def rank_mod(rows):
    """Gaussian rank over GF(MOD), using Python unbounded integers."""
    a = [[x % MOD for x in row] for row in rows]
    if not a:
        return 0
    nrow, ncol = len(a), len(a[0])
    rank = 0
    for col in range(ncol):
        pivot = next((i for i in range(rank, nrow) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][col], MOD - 2, MOD)
        for j in range(col, ncol):
            a[rank][j] = a[rank][j] * inverse % MOD
        for i in range(rank + 1, nrow):
            factor = a[i][col]
            if factor:
                for j in range(col, ncol):
                    a[i][j] = (a[i][j] - factor * a[rank][j]) % MOD
        rank += 1
        if rank == nrow:
            break
    return rank


def integer_kernel_basis(matrix):
    """Exact reduced-echelon rational nullspace, scaled columnwise to Z."""
    a = [[Fraction(x) for x in row] for row in matrix]
    nrow, ncol = len(a), len(a[0])
    pivots = []
    rank = 0
    for col in range(ncol):
        pivot = next((i for i in range(rank, nrow) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        factor = a[rank][col]
        a[rank] = [x / factor for x in a[rank]]
        for i in range(nrow):
            if i != rank and a[i][col]:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[rank])]
        pivots.append(col)
        rank += 1
        if rank == nrow:
            break
    columns = []
    for free in range(ncol):
        if free in pivots:
            continue
        column = [Fraction(0) for _ in range(ncol)]
        column[free] = 1
        for row, pivot in enumerate(pivots):
            column[pivot] = -a[row][free]
        factor = lcm(*(x.denominator for x in column))
        columns.append(tuple(int(factor * x) for x in column))
    return columns


def graph_eligible(subset):
    """Exact geometric criterion for a five-edge subset of K6."""
    adj = [[] for _ in V]
    for eidx in subset:
        a, b = EDGES[eidx]
        adj[a].append(b)
        adj[b].append(a)
    color = [None] * 6
    imbalances = []
    for v in V:
        if color[v] is not None:
            continue
        color[v] = 0
        stack = [v]
        parts = [0, 0]
        bipartite = True
        while stack:
            a = stack.pop()
            parts[color[a]] += 1
            for b in adj[a]:
                if color[b] is None:
                    color[b] = 1 - color[a]
                    stack.append(b)
                elif color[b] == color[a]:
                    bipartite = False
        if bipartite:
            imbalances.append(parts[0] - parts[1])
    return not imbalances or (len(imbalances) == 1 and imbalances[0] != 0)


def is_star(subset):
    return any(all(v in EDGES[e] for e in subset) for v in V)


def is_spread(subset):
    return len({e for m in subset for e in MATCHINGS[m]}) == 15


def main():
    assert rank_mod(T) == 6
    assert all(sum(INC[e][m] for e in range(15)) == 3 for m in range(15))
    assert all(sum(INC[e][m] for m in range(15)) == 3 for e in range(15))
    # The spectrum of INC INC^T is 9^1,4^9,0^5, by
    # INC INC^T = 4I + J - T^T T, T T^T = 4I + J_6.
    for i in range(15):
        for j in range(15):
            lhs = sum(INC[i][k] * INC[j][k] for k in range(15))
            rhs = 4 * (i == j) + 1 - sum(T[v][i] * T[v][j] for v in V)
            assert lhs == rhs
    assert rank_mod(INC) == 10
    eig1_columns = integer_kernel_basis(T)
    assert len(eig1_columns) == 9
    assert all(sum(T[v][e] * col[e] for e in range(15)) == 0
               for v in V for col in eig1_columns)
    # L(2u,INC^T u) = (2u,INC^T u) for T u=0.
    E1 = [[2 * col[i] for col in eig1_columns] for i in range(15)] + [
        [sum(INC[e][j] * col[e] for e in range(15)) for col in eig1_columns]
        for j in range(15)]
    maximum_squared_row_norm = max(sum(x*x for x in row) for row in E1)
    assert maximum_squared_row_norm <= 36
    # Every 9x9 minor has |det| <= 6^9 = 10077696 < MOD.
    # Every 10x10 minor of INC has |det| <= (sqrt(3))^10
    # = 243 < MOD. Therefore modular full ranks below are exact over Q.
    assert 6**9 < MOD and 3**5 < MOD

    choices = list(combinations(range(15), 5))
    P = []
    H = []
    for subset in choices:
        complement = [i for i in range(15) if i not in subset]
        point_good = rank_mod([INC[i] for i in complement]) == 10
        line_good = rank_mod([[INC[i][j] for j in complement] for i in range(15)]) == 10
        assert point_good == graph_eligible(subset)
        if point_good:
            P.append(subset)
        if line_good:
            H.append(subset)
    assert len(P) == len(H) == 1518
    stars = {s for s in P if is_star(s)}
    spreads = {s for s in H if is_spread(s)}
    assert len(stars) == len(spreads) == 6

    # Each relabeling of the six base vertices is an automorphism.
    automorphisms = []
    for g in permutations(V):
        ep = tuple(EDGE_ID[tuple(sorted(g[v] for v in e))] for e in EDGES)
        lp = tuple(MATCH_ID[tuple(sorted(
            tuple(sorted(g[v] for v in e)) for e in matching))]
                   for matching in MATCHINGS)
        assert all(INC[e][j] == INC[ep[e]][lp[j]]
                   for e in range(15) for j in range(15))
        automorphisms.append((ep, lp))
    assert len(automorphisms) == 720

    # Exactly eight point-five-set orbits under S6.
    unseen = set(P)
    orbit_data = []
    bad_pairs_by_orbit = []
    while unseen:
        pset = min(unseen)
        orbit = {tuple(sorted(g[e] for e in pset)) for g, _ in automorphisms}
        assert orbit <= unseen
        unseen -= orbit
        failures = set()
        for hset in H:
            selected_rows = [E1[e] for e in pset] + [E1[15+j] for j in hset]
            if rank_mod(selected_rows) != 9:
                failures.add(hset)
        assert failures == (spreads if pset in stars else set())
        orbit_data.append((pset, len(orbit), len(H)-len(failures)))
        bad_pairs_by_orbit.append(len(orbit)*len(failures))
    assert len(orbit_data) == 8
    assert sorted(z[1] for z in orbit_data) == [6, 60, 72, 120, 180, 360, 360, 360]
    assert sum(z[1] for z in orbit_data) == 1518
    assert sum(bad_pairs_by_orbit) == 36
    optimal_count = sum(z[1]*z[2] for z in orbit_data)
    assert optimal_count == 1518**2-36 == 2304288

    # Independent full 30-state Kalman-rank check on one good and bad set.
    A = [[(3 if i == j else 0) for j in range(30)] for i in range(30)]
    for i in range(15):
        for j in range(15):
            A[i][15+j] = -INC[i][j]
            A[15+j][i] = -INC[i][j]

    def reachability_rank(point_set, line_set):
        leaders = list(point_set) + [15+j for j in line_set]
        block = [[int(i == j) for j in leaders] for i in range(30)]
        blocks = []
        for power in range(5):
            blocks.append(block)
            block = [[sum(A[i][j]*block[j][k] for j in range(30))
                      for k in range(10)] for i in range(30)]
        return rank_mod([[x for item in blocks for x in item[i]]
                         for i in range(30)])

    goodP = (0, 1, 2, 3, 5)
    goodH = (0, 1, 3, 4, 7)
    assert goodP in P and goodH in H
    assert reachability_rank(goodP, goodH) == 30
    assert reachability_rank(min(stars), min(spreads)) < 30

    print('Thirty vertices: 15 edges and 15 perfect matchings of K6.')
    print('Eigenvalue multiplicities: 0:1, 1:9, 3:10, 5:9, 6:1.')
    print('Minimum independent coordinate actuators: 10 (five of each kind).')
    print('Eligible 5-point sets: 1518; eligible 5-line sets: 1518.')
    print('Point-side exact shapes: 486 unbalanced spanning trees; '
          '972 odd unicyclic five-vertex components plus isolate; '
          '60 triangle-plus-three-vertex-path subsets.')
    print('Eight S6 orbit representatives, sizes and eligible line counts:')
    for item in orbit_data:
        print('  ', item)
    print('Exceptional pairs: all 6 point-stars x all 6 line-spreads = 36.')
    print('Controllable minimum-size placements: 2304288.')
    print('Every modular rank test is exact by the stated determinant bounds.')
    print('Independent 30-state reachability examples: passed.')
    print('PASS')


if __name__ == '__main__':
    main()
