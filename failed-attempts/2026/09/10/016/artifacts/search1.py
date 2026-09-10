"""Search for counterexamples to reg(S/I(G)) <= 2*nu(G) among claw-free graphs.
Also compare beta (min maximal matching) vs 2*nu.
"""
import sys, itertools, random
sys.path.insert(0, 'output/artifacts')
from clawreg import adj_from_edges, has_claw, induced_matching_number, reg_SI_modp


def min_maximal_matching(n, adj):
    edges = [(a, b) for a in range(n) for b in range(a + 1, n) if (adj[a] >> b) & 1]
    best = [10 ** 9]

    def is_maximal(chosen):
        used = 0
        for (a, b) in chosen:
            used |= (1 << a) | (1 << b)
        for (a, b) in edges:
            if not (used >> a) & 1 and not (used >> b) & 1:
                return False
        return True

    # branch and bound: try small matchings first via iterative deepening
    m = len(edges)
    for K in range(0, m + 1):
        found = [False]

        def rec(idx, chosen):
            if found[0]:
                return True
            if len(chosen) == K:
                if is_maximal(chosen):
                    found[0] = True
                    return True
                return False
            if idx == m:
                return False
            # prune: even filling up to K, can we cover? simple prune skip
            a, b = edges[idx]
            # take if disjoint
            used = 0
            for (c, d) in chosen:
                used |= (1 << c) | (1 << d)
            if not (used >> a) & 1 and not (used >> b) & 1:
                chosen.append((a, b))
                if rec(idx + 1, chosen):
                    return True
                chosen.pop()
            if rec(idx + 1, chosen):
                return True
            return False

        if rec(0, []):
            return K
    return None


def check(n, adj, tag=""):
    if has_claw(n, adj):
        return None
    nu = induced_matching_number(n, adj)
    reg = reg_SI_modp(n, adj)
    ok = (reg <= 2 * nu)
    return (ok, nu, reg, tag)


def all_graphs_edges(n):
    pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
    M = len(pairs)
    for mask in range(1 << M):
        yield [(pairs[i]) for i in range(M) if (mask >> i) & 1]


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "n6"
    if mode == "n6":
        n = 6
        total = 0
        nclaw = 0
        worst_gap = 0
        worst = []
        sharp = []
        viol = []
        for edges in all_graphs_edges(n):
            total += 1
            adj = adj_from_edges(n, edges)
            if has_claw(n, adj):
                continue
            nclaw += 1
            nu = induced_matching_number(n, adj)
            reg = reg_SI_modp(n, adj)
            gap = 2 * nu - reg
            if gap < 0:
                viol.append((edges, nu, reg))
            if gap < worst_gap:
                worst_gap = gap
            if gap == 0:
                sharp.append((edges, nu, reg))
        print("total=%d clawfree=%d viol=%d sharp=%d worst_gap=%d" % (total, nclaw, len(viol), len(sharp), worst_gap))
        for (e, nu, reg) in viol[:10]:
            print("VIOL", e, nu, reg)
        print("num sharp:", len(sharp))
        for (e, nu, reg) in sharp[:20]:
            print("SHARP", e, nu, reg)
