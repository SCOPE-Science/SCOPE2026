"""Exact, dependency-free verification of finite triangle-free graph edge perturbations."""
from itertools import combinations, permutations
from fractions import Fraction
from math import comb


def edge_pairs(n):
    return list(combinations(range(n), 2))


def graph_edges(mask, n):
    return {e for j, e in enumerate(edge_pairs(n)) if (mask >> j) & 1}


def triangle_free(edges, n):
    return all(not ({(i, j), (i, k), (j, k)} <= edges)
               for i, j, k in combinations(range(n), 3))


def independent_count(edges, n):
    I = [m for m in range(1 << n)
         if all(not ((m >> a) & 1 and (m >> b) & 1) for a, b in edges)]
    return len(I), sum((a & b) == 0 for a in I for b in I)


def explicit_pair_counts(edges, n):
    """Independent 4-state enumeration, not using independent_count."""
    adjacent = nonadjacent = 0
    for configuration in range(4 ** n):
        state = [(configuration >> (2 * j)) & 3 for j in range(n)]
        if any((state[a] & state[b]) for a, b in edges):
            continue
        nonadjacent += 1
        if all(v != 3 for v in state):
            adjacent += 1
    return adjacent, nonadjacent


def canonical_aug(n, edges, added):
    # Canonicalizes a graph together with the distinguished added edge.
    edge_indices = {e:i for i,e in enumerate(edge_pairs(n))}
    best = None
    for p in permutations(range(n)):
        new_edges = {tuple(sorted((p[a], p[b]))) for a,b in edges}
        e_new = tuple(sorted((p[added[0]], p[added[1]])))
        representation = (sum(1 << edge_indices[e] for e in new_edges), edge_indices[e_new])
        if best is None or representation < best:
            best = representation
    return best


def test():
    first_violations = []
    for n in range(1, 6):
        pairs = edge_pairs(n)
        # Enumeration over ALL labelled graphs on n vertices, no external atlas.
        attempts = reversals = equalities = 0
        canonical = set()
        for mask in range(1 << len(pairs)):
            edges = graph_edges(mask, n)
            if not triangle_free(edges, n):
                continue
            I, B = independent_count(edges, n)
            A_direct, N_direct = explicit_pair_counts(edges, n)
            assert (A_direct, N_direct) == (B, I * I)
            for e in pairs:
                if e in edges:
                    continue
                bigger = edges | {e}
                if not triangle_free(bigger, n):
                    continue
                attempts += 1
                J, C = independent_count(bigger, n)
                if C * I * I == B * J * J:
                    equalities += 1
                if C * I * I < B * J * J:
                    reversals += 1
                    if n == 5:
                        canonical.add(canonical_aug(n, edges, e))
                        first_violations.append((edges, e, (I, B), (J, C)))
        assert equalities == 0
        print(f'n={n}: eligible_labeled_augmentations={attempts}, strict_decreases={reversals}, equalities={equalities}, canonical_decreases={len(canonical)}')
        if n < 5:
            assert reversals == 0
        else:
            assert len(canonical) == 2
    # Identify the two transition classes by their invariant count quadruples.
    cases = {(x[2], x[3]) for x in first_violations}
    assert cases == {((18, 129), (17, 113)), ((15, 119), (14, 103))}, cases
    assert sum(x[2] == (18,129) for x in first_violations) == 20
    assert sum(x[2] == (15,119) for x in first_violations) == 60
    for before, after in sorted(cases):
        I,B = before; J,C = after
        assert C * I * I < B * J * J
        print(f'transition (I,B)=({I},{B}) -> ({J},{C}): R={Fraction(B,I*I)} -> {Fraction(C,J*J)}')
    for m in range(1, 16):
        I_new = 2**m + 1
        B_new = 3**m + 2**(m+1)
        I_old = 2**m + 2
        B_old = 3**m + 3 * 2**m
        numerator = B_new * I_old**2 - B_old * I_new**2
        algebraic = 3**m * (2**(m+1)+3) + 2**m * (-4**m + 2**(m+1) + 5)
        assert numerator == algebraic
        assert (numerator < 0) == (m >= 4)
    print('STAR_ALL_TESTED_EXACT: m=1..15')
    print('ALL_FINITE_AND_SYMBOLIC_IDENTITY_TESTS_PASS')


if __name__ == '__main__':
    test()
