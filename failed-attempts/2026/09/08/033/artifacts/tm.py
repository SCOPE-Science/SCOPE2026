"""Exact transfer-matrix enumeration of crossing-count polynomials on R x C grids.

Graph: vertices (col,row), col=0..C-1, row=0..R-1, free boundary.
  m = (C-1)*R + C*(R-1) edges.
Directions: H = left-to-right open crossing; V = top-to-bottom open crossing.

Two-sided connectivity flags:
  H: famA = connected-to-left-edge, famB = connected-to-right-edge.
  V: famA = connected-to-top-edge,  famB = connected-to-bottom-edge.
A configuration crosses iff some open component carries both flags.
Checked at every step (init, each transfer, final).

Exactness: polynomial sum c_k B^k as ONE Python int, B = 2^(m+1).
Decode by divmod; self-checks: slice sums == C(m,k), total == 2^m.
"""
from functools import lru_cache


def make_solver(R, C, direction):
    assert direction in ("H", "V")
    A = R - 1

    def canon(raw_part, fa, fb):
        mapping = {}
        part = [0] * R
        fla, flb = [], []
        for v, b in enumerate(raw_part):
            if b not in mapping:
                mapping[b] = len(fla)
                fla.append(False)
                flb.append(False)
            part[v] = mapping[b]
            if fa[v]:
                fla[mapping[b]] = True
            if fb[v]:
                flb[mapping[b]] = True
        return (tuple(part), tuple(fla), tuple(flb))

    def find(par, a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    def seed(col):
        """(ownA, ownB) flag seeds for a fresh column col."""
        if direction == "H":
            return ([col == 0] * R, [col == C - 1] * R)
        else:
            return ([j == 0 for j in range(R)], [j == R - 1 for j in range(R)])

    def init_states():
        out = []
        sA, sB = seed(0)
        for mask in range(1 << A):
            par = list(range(R))
            for j in range(A):
                if (mask >> j) & 1:
                    ra, rb = find(par, j), find(par, j + 1)
                    if ra != rb:
                        par[ra] = rb
            roots = [find(par, j) for j in range(R)]
            fa = [sA[j] for j in range(R)]
            fb = [sB[j] for j in range(R)]
            # merge flags within column-0 blocks
            comps = {}
            for j in range(R):
                r = roots[j]
                a, b = comps.get(r, (False, False))
                comps[r] = (a or fa[j], b or fb[j])
            nfa = [comps[roots[j]][0] for j in range(R)]
            nfb = [comps[roots[j]][1] for j in range(R)]
            # NOTE: for C==1 the seed already carries both flags; crossing here is real.
            key = canon(roots, nfa, nfb)
            crossed = any(a and b for a, b in zip(key[1], key[2]))
            out.append((key, bin(mask).count("1"), crossed))
        return out

    @lru_cache(maxsize=None)
    def trans(part, fla, flb, col):
        """All (newkey, dk, crossed) over (hmask, vmask) into column col."""
        sA, sB = seed(col)
        res = []
        for hmask in range(1 << R):
            for vmask in range(1 << A):
                par = list(range(2 * R))
                for a in range(R):
                    for b in range(a + 1, R):
                        if part[a] == part[b]:
                            ra, rb = find(par, a), find(par, b)
                            if ra != rb:
                                par[ra] = rb
                for j in range(R):
                    if (hmask >> j) & 1:
                        ra, rb = find(par, j), find(par, R + j)
                        if ra != rb:
                            par[ra] = rb
                for j in range(A):
                    if (vmask >> j) & 1:
                        ra, rb = find(par, R + j), find(par, R + j + 1)
                        if ra != rb:
                            par[ra] = rb
                roots = [find(par, R + j) for j in range(R)]
                # gather flags from old side (via canonical block flags) + seeds
                comp = {}
                for a in range(R):
                    r = find(par, a)
                    x, y = comp.get(r, (False, False))
                    comp[r] = (x or fla[part[a]], y or flb[part[a]])
                for j in range(R):
                    r = find(par, R + j)
                    x, y = comp.get(r, (False, False))
                    comp[r] = (x or sA[j], y or sB[j])
                nfa = [comp[roots[j]][0] for j in range(R)]
                nfb = [comp[roots[j]][1] for j in range(R)]
                key = canon(roots, nfa, nfb)
                crossed = any(a and b for a, b in zip(key[1], key[2]))
                dk = bin(hmask).count("1") + bin(vmask).count("1")
                res.append((key, dk, crossed))
        return res

    return init_states, trans


def enumerate_case(R, C, direction):
    from math import comb
    m = (C - 1) * R + C * (R - 1)
    A = R - 1
    B = 1 << (m + 1)
    BP = [1]
    for _ in range(2 * R):
        BP.append(BP[-1] * B)
    init_states, trans = make_solver(R, C, direction)
    dp = {}
    cross = 0
    for key, dk, crossed in init_states():
        if crossed:
            cross += BP[dk]
        else:
            dp[key] = dp.get(key, 0) + BP[dk]
    for step in range(C - 1):
        col = step + 1
        # crossed configs stay crossed; later edges are free:
        # multiply crossing pool by (1+B)^{E_new}
        E_new = R + A  # R horizontals + A new-column verticals
        cross = cross * ((1 + B) ** E_new)
        ndp = {}
        for (part, fla, flb), val in dp.items():
            for key, dk, crossed in trans(part, fla, flb, col):
                add = val * BP[dk]
                if crossed:
                    cross += add
                else:
                    ndp[key] = ndp.get(key, 0) + add
        dp = ndp
    noncross = 0
    for val in dp.values():
        noncross += val
    cr = [0] * (m + 1)
    nc = [0] * (m + 1)
    x, y = cross, noncross
    for k in range(m + 1):
        x, r = divmod(x, B)
        cr[k] = r
        y, r = divmod(y, B)
        nc[k] = r
    assert x == 0 and y == 0, "base-B overflow: increase B"
    assert sum(cr) + sum(nc) == (1 << m), "total configs"
    for k in range(m + 1):
        assert cr[k] + nc[k] == comb(m, k), f"slice k={k}"
    return {"R": R, "C": C, "direction": direction, "m": m,
            "cross_counts": cr, "noncross_counts": nc}
