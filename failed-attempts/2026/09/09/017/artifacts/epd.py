"""Endpoint-level PD diagrams with twist insertion. Self-contained (stdlib only)."""
from math import comb
import cmath

# Diagram: n crossings; endpoints (c, j), j=0..3 (X-notation positions a,b,c,d).
# edges: dict edge_id -> [(c1,j1),(c2,j2)]. over strand = (0,2) [a->c], under = (1,3) [b->d]
# (matches pdcal over_choice 'ac'; bracket-validated).


def katlas_819():
    raw = [(4, 2, 5, 1), (8, 4, 9, 3), (9, 15, 10, 14), (5, 13, 6, 12),
           (13, 7, 14, 6), (11, 1, 12, 16), (15, 11, 16, 10), (2, 8, 3, 7)]
    return build(raw)


def build(raw):
    edges = {}; nxt = [0]

    def E(x):
        if x not in edges:
            edges[x] = []
        return edges[x]
    cr = {}
    for ci, (a, b, c, d) in enumerate(raw):
        cn = ci + 1
        E(a).append((cn, 0)); E(b).append((cn, 1)); E(c).append((cn, 2)); E(d).append((cn, 3))
        cr[cn] = (a, b, c, d)
    assert all(len(v) == 2 for v in edges.values())
    return cr, edges


def bracket(cr, edges):
    N = len(cr); cl = sorted(cr); res = {}
    for mask in range(1 << N):
        a_ct = 0; ch = {}
        for i, c in enumerate(cl):
            b = (mask >> i) & 1; ch[c] = b
            if b == 0:
                a_ct += 1
        parent = {}
        for c in cr:
            for j in range(4):
                parent[(c, j)] = (c, j)

        def ff(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x

        def uu(x, y):
            rx, ry = ff(x), ff(y)
            if rx != ry:
                parent[rx] = ry
        for e, ends in edges.items():
            uu(ends[0], ends[1])
        for c in cr:
            if ch[c] == 0:
                uu((c, 0), (c, 1)); uu((c, 2), (c, 3))
            else:
                uu((c, 0), (c, 3)); uu((c, 2), (c, 1))
        k = len(set(ff(s) for s in parent))
        base = a_ct - (N - a_ct); e = k - 1
        for j in range(e + 1):
            res[base + 2 * j - 2 * (e - j)] = res.get(base + 2 * j - 2 * (e - j), 0) + comb(e, j) * ((-1) ** e)
    return res


def det_of(B):
    A = cmath.exp(-1j * cmath.pi / 4)
    return abs(sum(c * A ** k for k, c in B.items()))


def insert_twist(cr, edges, eA_side1_end, eB_side1_end, overA=True):
    """Extend a 2-braid twist region by one half-twist. Cut parallel edges eA, eB
    (side1 ends at one crossing, side2 at the next); insert crossing Y with strands
    CROSSING (half-twist): A1 -> B2 and B1 -> A2 through Y.
    overA=True: strand A over B; False: B over A. Returns (cr2, edges2)."""
    eA = next(e for e, ends in edges.items() if eA_side1_end in ends)
    eB = next(e for e, ends in edges.items() if eB_side1_end in ends)
    assert eA != eB
    endsA = edges[eA]; endsB = edges[eB]
    A2 = endsA[1] if endsA[0] == eA_side1_end else endsA[0]
    B2 = endsB[1] if endsB[0] == eB_side1_end else endsB[0]
    Y = max(cr) + 1
    me = max(edges)
    cr2 = dict(cr); edges2 = {e: list(v) for e, v in edges.items()}
    del edges2[eA]; del edges2[eB]
    if overA:
        yA1, yB2, yB1, yA2 = (Y, 0), (Y, 2), (Y, 1), (Y, 3)
    else:
        yA1, yB2, yB1, yA2 = (Y, 1), (Y, 3), (Y, 0), (Y, 2)
    edges2[me + 1] = [eA_side1_end, yA1]
    edges2[me + 2] = [yB2, B2]
    edges2[me + 3] = [eB_side1_end, yB1]
    edges2[me + 4] = [yA2, A2]
    cr2[Y] = (me + 1, me + 3, me + 2, me + 4)
    return cr2, edges2


def comps(cr, edges):
    # directed strand walk with orientation quotient (1 comp knot check)
    port_edge = {}
    for e, ends in edges.items():
        for end in ends:
            port_edge[end] = e
    pair = {}
    for c in cr:
        pair[(c, 0)] = (c, 2); pair[(c, 2)] = (c, 0)
        pair[(c, 1)] = (c, 3); pair[(c, 3)] = (c, 1)
    side_of = {}
    for e, ends in edges.items():
        for i, end in enumerate(ends):
            side_of[(e, end)] = i
    seen = set(); lists = []
    for e, ends in edges.items():
        for s in (0, 1):
            if (e, s) in seen:
                continue
            L = []; cur = (e, s)
            while cur not in seen:
                seen.add(cur); L.append(cur)
                ce, cs = cur
                arr = edges[ce][1 - cs]
                c2 = pair[arr]
                e2 = port_edge[c2]
                cur = (e2, side_of[(e2, c2)])
            lists.append(L)
    pos = {st: i for i, L in enumerate(lists) for st in L}
    done = set(); un = 0
    for i, L in enumerate(lists):
        if i in done:
            continue
        j = pos.get((L[0][0], 1 - L[0][1]), i)
        done.add(i); done.add(j); un += 1
    return un


if __name__ == '__main__':
    cr, edges = katlas_819()
    B = bracket(cr, edges)
    print('D0 bracket:', dict(sorted((k, v) for k, v in B.items() if v != 0)), 'det=%.3f' % det_of(B))
    print('components:', comps(cr, edges))
