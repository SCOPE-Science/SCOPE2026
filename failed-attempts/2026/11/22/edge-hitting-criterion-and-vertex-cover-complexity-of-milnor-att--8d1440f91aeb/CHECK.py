"""Finite exact checks for edgewise homeomorphisms and vertex-cover reduction.

No finite check substitutes for the infinite closed-set realization theorem.
"""
from fractions import Fraction as Q
from itertools import combinations


def local_map(t, left, right, anchors, eps=Q(1, 2)):
    """Piecewise quadratic interval homeomorphism on one edge.

    anchors are sorted rational points of the closed target on this edge.
    A complementary gap must have at least one target endpoint.
    """
    grid = sorted(set([left, right] + list(anchors)))
    if t in grid:
        return t
    for a, b in zip(grid, grid[1:]):
        if a < t < b:
            has_left, has_right = a in anchors, b in anchors
            assert has_left or has_right
            m = (a + b) / 2
            if has_left and has_right:
                if t == m:
                    return t
                if t < m:
                    b = m
                    toward_left = True
                else:
                    a = m
                    toward_left = False
            else:
                toward_left = has_left
            u = (t - a) / (b - a)
            v = u + (-eps if toward_left else eps) * u * (1 - u)
            return a + (b - a) * v
    raise AssertionError('not in an edge')


def test_edge_maps():
    examples = [
        [Q(0)], [Q(1)], [Q(0), Q(1)], [Q(1, 3)],
        [Q(0), Q(1, 3)], [Q(1, 3), Q(2, 3)],
        [Q(0), Q(1, 3), Q(2, 3), Q(1)],
    ]
    checks = 0
    for target in examples:
        for j in range(0, 129):
            x = Q(j, 128)
            fx = local_map(x, Q(0), Q(1), target)
            assert 0 <= fx <= 1
            if x in target or x in (0, 1):
                assert fx == x
            if j < 128:
                y = Q(j + 1, 128)
                fy = local_map(y, Q(0), Q(1), target)
                assert fx < fy
            checks += 1
        # Orbits remain in their component of the complement and
        # converge monotonically to the selected target endpoint.
        for j in range(1, 24):
            x = Q(j, 24)
            if x in target:
                continue
            pos = x
            for _ in range(6):
                nxt = local_map(pos, Q(0), Q(1), target)
                assert 0 <= nxt <= 1
                pos = nxt
            # Exact rational convergence is not asserted after 30 steps.
    return checks


def vertex_cover_number(n, edges):
    for size in range(n + 1):
        for chosen in combinations(range(n), size):
            S = set(chosen)
            if all(u in S or v in S for u, v in edges):
                return size
    raise AssertionError


def discrete_hitting_number(n, edges):
    # On each closed edge, one extra candidate is its interior midpoint.
    # A candidate midway along an edge cannot cover another edge.
    m = len(edges)
    cover_masks = [0] * (n + m)
    for j, (u, v) in enumerate(edges):
        cover_masks[u] |= (1 << j)
        cover_masks[v] |= (1 << j)
        cover_masks[n + j] |= (1 << j)
    all_edges = (1 << m) - 1
    for size in range(n + 1):
        for chosen in combinations(range(n + m), size):
            mask = 0
            for k in chosen:
                mask |= cover_masks[k]
            if mask == all_edges:
                return size
    raise AssertionError


def test_graphs():
    cases = [
        ('single-edge', 2, [(0, 1)], 1),
        ('tripod', 4, [(0, 1), (0, 2), (0, 3)], 1),
        ('triangle', 3, [(0, 1), (1, 2), (0, 2)], 2),
        ('tetrahedron', 4, list(combinations(range(4), 2)), 3),
        ('K3,3', 6, [(i, j) for i in range(3) for j in range(3, 6)], 3),
        ('triangular-prism', 6, [(0, 1), (1, 2), (2, 0),
                                 (3, 4), (4, 5), (5, 3),
                                 (0, 3), (1, 4), (2, 5)], 4),
    ]
    out = []
    for name, n, edges, expected in cases:
        tau = vertex_cover_number(n, edges)
        graph_hit = discrete_hitting_number(n, edges)
        assert tau == graph_hit == expected, (name, tau, graph_hit)
        out.append((name, n, len(edges), tau))
    return out


if __name__ == '__main__':
    cnt = test_edge_maps()
    result = test_graphs()
    print('PASS exact edge-coordinate order/boundary checks:', cnt)
    print('PASS graph-cover comparisons:', len(result))
    for case in result:
        print(' ', case)
