#!/usr/bin/env python3
"""Distinct finite checks for the rook-graph general-position enumeration.

Only Python's standard library is needed.  No finite test is used as a
substitute for the all-parameter bijective proof.
"""
from math import comb


def recurrence(M, N):
    """Return coefficient tuples for all rectangle sizes up to M,N."""
    p = {}
    for m in range(M + 1):
        for n in range(N + 1):
            if m == 0 or n == 0:
                p[(m, n)] = (1,)
                continue
            q = [0] * (m * n + 1)
            for j in range(n + 1):
                factor = comb(n, j)
                for degree, coeff in enumerate(p[(m - 1, n - j)]):
                    q[j + degree] += factor * coeff
            for k in range(1, m):
                factor = n * comb(m - 1, k)
                for degree, coeff in enumerate(p[(m - 1 - k, n - 1)]):
                    q[k + 1 + degree] += factor * coeff
            while len(q) > 1 and q[-1] == 0:
                q.pop()
            p[(m, n)] = tuple(q)
    return p


def direct(m, n):
    """Enumerate arbitrary selected board cells by the geodesic condition.

    A corner can be a middle point of a shortest path iff it shares a
    row with one selected corner and a column with another; each
    forbidden triple is constructed from distances in the rook graph.
    This code does not call the recurrence or assume a star forest.
    """
    N = m * n
    masks = set()
    for i in range(m):
        for j in range(n):
            center = 1 << (i * n + j)
            for jj in range(n):
                if jj == j:
                    continue
                for ii in range(m):
                    if ii == i:
                        continue
                    masks.add(center | (1 << (i * n + jj)) | (1 << (ii * n + j)))
    masks = tuple(sorted(masks))
    coeffs = [0] * (N + 1)
    for state in range(1 << N):
        if all((state & mask) != mask for mask in masks):
            coeffs[state.bit_count()] += 1
    while len(coeffs) > 1 and not coeffs[-1]:
        coeffs.pop()
    return tuple(coeffs), (1 << N)


def star_forest(state, m, n):
    """Separately recognize components of the selected incidence graph."""
    adj = [[] for _ in range(m + n)]
    for i in range(m):
        for j in range(n):
            if state >> (i * n + j) & 1:
                adj[i].append(m + j)
                adj[m + j].append(i)
    seen = set()
    for x in range(m + n):
        if x in seen or not adj[x]:
            continue
        comp = []
        stack = [x]
        seen.add(x)
        while stack:
            v = stack.pop()
            comp.append(v)
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        if len(comp) > 2 and sum(len(adj[v]) == len(comp) - 1 for v in comp) != 1:
            return False
        if len(comp) == 2 and len(adj[comp[0]]) != 1:
            return False
    return True


def main():
    polynomials = recurrence(22, 22)
    boards = [(m, n) for m in range(1, 17) for n in range(1, 17)
              if m * n <= 16]
    trials = 0
    for m, n in boards:
        got, checked = direct(m, n)
        trials += checked
        assert got == polynomials[(m, n)], (m, n, got, polynomials[(m, n)])
        for state in range(1 << (m * n)):
            # Separate component recognition compared against
            # the direct no-geodesic-triple test, with the same masks
            # recomputed only for this board.
            selected = [(i, j) for i in range(m) for j in range(n)
                        if state >> (i * n + j) & 1]
            good = True
            for a in selected:
                for b in selected:
                    if b == a:
                        continue
                    for c in selected:
                        if c == a or c == b:
                            continue
                        dab = (a[0] != b[0]) + (a[1] != b[1])
                        dbc = (b[0] != c[0]) + (b[1] != c[1])
                        dac = (a[0] != c[0]) + (a[1] != c[1])
                        if dac == dab + dbc:
                            good = False
                            break
                    if not good:
                        break
                if not good:
                    break
            assert good == star_forest(state, m, n), (m, n, state)

    symmetry = 0
    top_cases = 0
    for m in range(1, 23):
        for n in range(1, 23):
            p = polynomials[(m, n)]
            assert p == polynomials[(n, m)]
            symmetry += 1
            if min(m, n) == 1:
                expected_degree = max(m, n)
                expected_top = 1
            elif m == n == 2:
                expected_degree, expected_top = 2, 6
            elif min(m, n) == 2:
                expected_degree = m + n - 2
                expected_top = 2 ** max(m, n)
            else:
                expected_degree = m + n - 2
                expected_top = m * n
            assert len(p) - 1 == expected_degree, (m, n, p)
            assert p[-1] == expected_top, (m, n, p)
            assert p[0] == 1 and p[1] == m * n
            assert p[2] == comb(m * n, 2) if m * n >= 2 else p[0] == 1
            top_cases += 1

    print('DIRECT_ROOK_GEODESIC_ENUMERATIONS_OK', len(boards), trials)
    print('INDEPENDENT_COMPONENT_CLASSIFICATIONS_OK', trials)
    print('SYMMETRY_CASES_OK', symmetry)
    print('EXTREMAL_AND_LOW_DEGREE_CASES_OK', top_cases)
    for m, n in [(1, 5), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (5, 5)]:
        print('POLYNOMIAL', m, n, list(polynomials[(m, n)]))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
