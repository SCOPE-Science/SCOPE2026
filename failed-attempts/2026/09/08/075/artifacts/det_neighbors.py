"""Exact determinant + determinant-1-neighbourhood lists from Gauss codes (stdlib only).

Method: Fox colouring (determinant) matrix built purely combinatorially from the
Gauss code. Arcs run from one under-visit to the next; each crossing gives the
relation 2*over - incoming_under - outgoing_under = 0. det(K) = |det| of any
(n-1)x(n-1) minor. Exact integer arithmetic via Bareiss fraction-free elimination.
A crossing change at label L swaps the signs of both occurrences of L.

Self-tests: unknot (1), trefoil (3), figure-eight (5), then the two frozen
KnotAtlas Gauss codes must give det 1 (as tabulated).
"""
import json

K34_GAUSS = [1, -4, 2, -1, 3, -7, 4, -2, -5, 11, -6, -3, 7, 10, -8, 5, -9, 6, -10, 8, -11, 9]
K42_GAUSS = [1, -4, 2, -1, 3, -7, 4, -2, -5, 8, -6, -3, 7, 10, -8, 11, -9, 5, -10, 6, -11, 9]
K34_DT = [4, 8, 12, 2, -16, -18, 6, -20, -22, -14, -10]
K42_DT = [4, 8, 12, 2, -18, -20, 6, -10, -22, -14, -16]


def bareiss_det(mat):
    n = len(mat)
    if n == 0:
        return 1
    a = [row[:] for row in mat]
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = -1
            for i in range(k + 1, n):
                if a[i][k] != 0:
                    swap = i
                    break
            if swap == -1:
                return 0
            a[k], a[swap] = a[swap], a[k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * a[k][k] - a[i][k] * a[k][j]) // prev
            a[i][k] = 0
        prev = a[k][k]
        if prev == 0:
            return 0
    return a[n - 1][n - 1]


def coloring_det(gauss):
    m = len(gauss)
    assert m % 2 == 0
    n = m // 2
    labels = sorted(set(abs(x) for x in gauss))
    assert labels == list(range(1, n + 1)), labels
    for L in range(1, n + 1):
        occ = [x for x in gauss if abs(x) == L]
        assert sorted(occ) == [-L, L], (L, occ)
    if n == 1:
        return 1
    pos_of = {}
    for i, x in enumerate(gauss):
        pos_of[x] = i
    under_pos = [pos_of[-L] for L in range(1, n + 1)]  # traversal order per label
    # arcs: order under-visits by traversal position
    order = sorted(range(n), key=lambda j: under_pos[j])
    # arc j = segment starting at the j-th under-visit in traversal order
    under_rank = {}
    for rank, j in enumerate(order):
        under_rank[under_pos[j]] = rank
    # over-arc of label L: which arc contains its over-visit
    trav_under_sorted = sorted(under_pos)
    def arc_of_position(p):
        # arc with index r covers (trav_under_sorted[r], trav_under_sorted[(r+1)%n]]
        # going forward cyclically; find r s.t. p in that half-open interval
        for r, t in enumerate(trav_under_sorted):
            nxt = trav_under_sorted[(r + 1) % n]
            if r < n - 1:
                if t < p <= nxt:
                    return r
            else:
                if p > t or p <= nxt:
                    return r
        raise AssertionError(p)
    over_arc = {}
    under_rank_of = {}
    for L in range(1, n + 1):
        over_arc[L] = arc_of_position(pos_of[L])
        under_rank_of[L] = under_rank[pos_of[-L]]
    M = [[0] * n for _ in range(n)]
    for L in range(1, n + 1):
        r = L - 1
        o = over_arc[L]
        u = under_rank_of[L]
        incoming = (u - 1) % n
        outgoing = u
        M[r][o] += 2
        M[r][incoming] -= 1
        M[r][outgoing] -= 1
    minor = [row[:n - 1] for row in M[:n - 1]]
    return abs(bareiss_det(minor))


def flip(gauss, L):
    return [-x if abs(x) == L else x for x in gauss]


def neighbor_dets(gauss):
    n = len(gauss) // 2
    return {L: coloring_det(flip(gauss, L)) for L in range(1, n + 1)}


def main():
    # ---- self-tests ----
    assert coloring_det([1, -1]) == 1, "unknot kink"
    assert coloring_det([1, -2, 3, -1, 2, -3]) == 3, "trefoil"
    assert coloring_det([1, -2, 3, -4, 2, -1, 4, -3]) == 5, "figure eight"
    d34 = coloring_det(K34_GAUSS)
    d42 = coloring_det(K42_GAUSS)
    assert d34 == 1, d34
    assert d42 == 1, d42
    nb34 = neighbor_dets(K34_GAUSS)
    nb42 = neighbor_dets(K42_GAUSS)
    out = {
        "self_tests": {"unknot": 1, "trefoil": 3, "figure_eight": 5},
        "K11n34": {"DT": K34_DT, "det": d34,
                   "neighbor_dets": [nb34[L] for L in sorted(nb34)]},
        "K11n42": {"DT": K42_DT, "det": d42,
                   "neighbor_dets": [nb42[L] for L in sorted(nb42)]},
    }
    with open("results.json", "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))
    print("det-1 count K11n34:", sum(1 for v in nb34.values() if v == 1),
          "| K11n42:", sum(1 for v in nb42.values() if v == 1))


if __name__ == "__main__":
    main()
