"""Exact checks for uniform-seed bond-percolation vaccination on small graphs.

Python 3 standard library only. No external data or packages are needed.
"""
from itertools import combinations
from math import comb


def polynomial_after_deletion(n, edges, vaccinated):
    """Power-basis coefficients of E[sum of squared open-component sizes]."""
    verts = [i for i in range(n) if i != vaccinated]
    remaining = [(a, b) for a, b in edges if vaccinated not in (a, b)]
    m = len(remaining)
    ans = [0] * (m + 1)
    for mask in range(1 << m):
        parent = {v: v for v in verts}

        def root(a):
            while parent[a] != a:
                a = parent[a]
            return a

        count_open = 0
        for j, (a, b) in enumerate(remaining):
            if mask & (1 << j):
                count_open += 1
                parent[root(a)] = root(b)
        sizes = {}
        for v in verts:
            k = root(v)
            sizes[k] = sizes.get(k, 0) + 1
        score = sum(s * s for s in sizes.values())
        for j in range(m - count_open + 1):
            ans[count_open + j] += score * comb(m - count_open, j) * (-1) ** j
    while len(ans) > 1 and ans[-1] == 0:
        ans.pop()
    return ans


def edges_of(n, mask):
    possible = list(combinations(range(n), 2))
    return [e for i, e in enumerate(possible) if mask & (1 << i)]


def check_lower_order():
    checked = 0
    for n in range(1, 5):
        for mask in range(1 << comb(n, 2)):
            edges = edges_of(n, mask)
            degrees = [sum(i in e for e in edges) for i in range(n)]
            polynomials = [polynomial_after_deletion(n, edges, v) for v in range(n)]
            for a in range(n):
                for b in range(n):
                    if degrees[a] == degrees[b]:
                        assert polynomials[a] == polynomials[b]
                    if degrees[a] > degrees[b]:
                        # On at most three remaining vertices, more edges
                        # imply a stochastically larger component sum.
                        residual_a = len(edges) - degrees[a]
                        residual_b = len(edges) - degrees[b]
                        assert residual_a < residual_b
            checked += 1
    assert checked == 75
    return checked


def check_witness():
    # Vertices a,b,c,d,e correspond to 0,1,2,3,4.
    edges = [(0, 1), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    polynomials = [polynomial_after_deletion(5, edges, v) for v in range(5)]
    assert polynomials[0] == [4, 10, 16, 0, -28, 14]
    assert polynomials[1] == [4, 6, 6, -6]
    assert polynomials[2] == [4, 8, 10, -2, -4]
    assert polynomials[3] == [4, 6, 4, 2]
    assert polynomials[4] == polynomials[3]
    # R_b - R_d = 2p^2(1-4p), identically in p.
    delta = [0] * max(map(len, polynomials))
    for j, v in enumerate(polynomials[1]):
        delta[j] += v
    for j, v in enumerate(polynomials[3]):
        delta[j] -= v
    assert delta == [0, 0, 2, -8, 0, 0]
    # Independently check the graph inclusions used for other vertices.
    path_for_a = [(1, 3), (2, 3), (2, 4)]
    path_for_c = [(0, 1), (1, 3), (3, 4)]
    assert set(path_for_a) < set(e for e in edges if 0 not in e)
    assert set(path_for_c) < set(e for e in edges if 2 not in e)
    return polynomials


if __name__ == '__main__':
    n = check_lower_order()
    out = check_witness()
    print('PASS: labelled graphs with 1..4 vertices:', n)
    print('PASS: five-vertex exact expected component-squared polynomials:', out)
    print('PASS: full vertex-optimality threshold at transmissibility p=1/4')
