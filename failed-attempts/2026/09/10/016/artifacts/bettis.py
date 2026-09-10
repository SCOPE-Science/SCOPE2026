"""Bigraded Betti tables of sharp witnesses via Hochster; test the
extremal-shape clause: is the top strand (j-i = reg) supported in a single
homological degree i?"""
import sys
sys.path.insert(0, 'output/artifacts')
from clawreg import adj_from_edges, has_claw, induced_matching_number, reg_SI_modp
from search1 import all_graphs_edges
from search2 import contains_induced_C5
import itertools


def homology_dims(n, adj, p=32003):
    """Reduced homology dims of Ind(G) over F_p, all degrees. Returns dict k->dim."""
    from clawreg import _rank_modp
    verts = list(range(n))
    if n == 0:
        return {-1: 1}  # empty complex: Htilde_{-1} = 1
    allfaces = [[(1 << v) for v in verts]]
    while True:
        prev = allfaces[-1]
        nxt = []
        for f in prev:
            m = max(i for i in range(n) if (f >> i) & 1)
            for v in range(m + 1, n):
                if (f >> v) & 1:
                    continue
                ok = True
                g = f
                while g:
                    lsb = g & (-g)
                    u = lsb.bit_length() - 1
                    if (adj[v] >> u) & 1:
                        ok = False
                        break
                    g ^= lsb
                if ok:
                    nxt.append(f | (1 << v))
        if not nxt:
            break
        allfaces.append(nxt)
    dimC = [len(f) for f in allfaces]
    idxmaps = [{f: i for i, f in enumerate(allfaces[d])} for d in range(len(allfaces))]
    ranks = {0: 1}
    for d in range(1, len(allfaces)):
        if not allfaces[d]:
            ranks[d] = 0
            continue
        nrows, ncols = dimC[d - 1], dimC[d]
        rows = [[0] * ncols for _ in range(nrows)]
        for j, f in enumerate(allfaces[d]):
            vs = [i for i in range(n) if (f >> i) & 1]
            for t, v in enumerate(vs):
                g = f ^ (1 << v)
                rows[idxmaps[d - 1][g]][j] = (rows[idxmaps[d - 1][g]][j] + (1 if t % 2 == 0 else p - 1)) % p
        ranks[d] = _rank_modp(rows, ncols, p)
    out = {}
    for k in range(0, len(allfaces)):
        hk = dimC[k] - ranks.get(k, 0) - ranks.get(k + 1, 0)
        if hk:
            out[k] = hk
    return out


def betti_table(n, adj, p=32003):
    """Full bigraded table {(i,j): dim} via Hochster."""
    from collections import defaultdict
    tab = defaultdict(int)
    N = 1 << n
    for mask in range(1, N):
        W = [i for i in range(n) if (mask >> i) & 1]
        j = len(W)
        # induced subgraph
        idx = {v: t for t, v in enumerate(W)}
        m = j
        e = [(idx[a], idx[b]) for a in W for b in W if a < b and ((adj[a] >> b) & 1)]
        a2 = adj_from_edges(m, e)
        h = homology_dims(m, a2, p)
        for k, d in h.items():
            i = j - k - 1
            if i >= 0:
                tab[(i, j)] += d
    return dict(tab)


def has_triangle(n, adj):
    for a in range(n):
        for b in range(a + 1, n):
            if not ((adj[a] >> b) & 1):
                continue
            for c in range(b + 1, n):
                if ((adj[a] >> c) & 1) and ((adj[b] >> c) & 1):
                    return True
    return False


if __name__ == "__main__":
    n = 6
    nsharp = 0
    multi_strand = []
    noC5_sharp = 0
    tri_and_high = []
    for edges in all_graphs_edges(n):
        adj = adj_from_edges(n, edges)
        if has_claw(n, adj):
            continue
        nu = induced_matching_number(n, adj)
        reg = reg_SI_modp(n, adj)
        if reg != 2 * nu or nu == 0:
            continue
        nsharp += 1
        tab = betti_table(n, adj)
        top = sorted([(i, j) for (i, j) in tab if j - i == reg])
        idegs = sorted(set(i for (i, j) in top))
        c5 = contains_induced_C5(n, adj) is not None
        tri = has_triangle(n, adj)
        if not c5:
            noC5_sharp += 1
        if len(idegs) > 1:
            multi_strand.append((edges, nu, reg, top, c5, tri))
        if tri and any(i >= 2 for (i, j) in top):
            tri_and_high.append((edges, nu, reg, top))
    print("nsharp(nu>=1)=%d noC5=%d multi_strand=%d tri_and_high=%d" % (nsharp, noC5_sharp, len(multi_strand), len(tri_and_high)))
    for (e, nu, reg, top, c5, tri) in multi_strand[:15]:
        print("MULTI", e, "nu=%d reg=%d top=%s C5=%s tri=%s" % (nu, reg, top, c5, tri))
