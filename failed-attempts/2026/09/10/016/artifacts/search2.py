"""Test the induction crux: for claw-free G, does there exist x with
nu(G - N[x]) <= nu(G) - 1? Also collect sharp-shape data."""
import sys
sys.path.insert(0, 'output/artifacts')
from clawreg import adj_from_edges, has_claw, induced_matching_number, reg_SI_modp


def closed_nbhd_del(n, adj, x):
    keep = [v for v in range(n) if v != x and not ((adj[x] >> v) & 1)]
    idx = {v: i for i, v in enumerate(keep)}
    m = len(keep)
    e = []
    for ii in range(m):
        for jj in range(ii + 1, m):
            if (adj[keep[ii]] >> keep[jj]) & 1:
                e.append((ii, jj))
    return m, adj_from_edges(m, e), keep


def del_vertex(n, adj, x):
    keep = [v for v in range(n) if v != x]
    idx = {v: i for i, v in enumerate(keep)}
    m = len(keep)
    e = []
    for ii in range(m):
        for jj in range(ii + 1, m):
            if (adj[keep[ii]] >> keep[jj]) & 1:
                e.append((ii, jj))
    return m, adj_from_edges(m, e), keep


def has_nu_drop_vertex(n, adj):
    nu = induced_matching_number(n, adj)
    good = []
    for x in range(n):
        m, a2, keep = closed_nbhd_del(n, adj, x)
        nu2 = induced_matching_number(m, a2)
        if nu2 <= nu - 1:
            good.append(x)
    return good


def contains_induced_C5(n, adj):
    from itertools import combinations
    for S in combinations(range(n), 5):
        cnt = 0
        for i in range(5):
            for j in range(i + 1, 5):
                if (adj[S[i]] >> S[j]) & 1:
                    cnt += 1
        if cnt == 5:
            # check connected C5 (5 edges + connected => C5)
            seen = {S[0]}
            stack = [S[0]]
            while stack:
                v = stack.pop()
                for w in S:
                    if ((adj[v] >> w) & 1) and w not in seen:
                        seen.add(w)
                        stack.append(w)
            if len(seen) == 5:
                return S
    return None


if __name__ == "__main__":
    # reload n=6 sharp data: recompute sharps, test C5 containment + nu-drop
    from search1 import all_graphs_edges
    n = 6
    nodrop = []
    sharps_noC5 = []
    nclaw = 0
    nsharp = 0
    for edges in all_graphs_edges(n):
        adj = adj_from_edges(n, edges)
        if has_claw(n, adj):
            continue
        nclaw += 1
        nu = induced_matching_number(n, adj)
        good = has_nu_drop_vertex(n, adj)
        if not good:
            nodrop.append((edges, nu))
        reg = reg_SI_modp(n, adj)
        if reg == 2 * nu:
            nsharp += 1
            if nu == 1 and contains_induced_C5(n, adj) is None:
                sharps_noC5.append((edges, nu, reg))
    print("clawfree=%d sharp=%d nodrop=%d sharps_nu1_noC5=%d" % (nclaw, nsharp, len(nodrop), len(sharps_noC5)))
    for (e, nu) in nodrop[:20]:
        print("NODROP", e, nu)
    for (e, nu, reg) in sharps_noC5[:20]:
        print("SHARP-NOC5", e, nu, reg)
