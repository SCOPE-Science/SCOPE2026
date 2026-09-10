"""Core routines for lane-528: claw-free regularity vs induced matching.
Conventions: S/I(G) regularity via Hochster over F_p (default) with QQ check
for witnesses. reg(S/I) = max{k+1 : Htilde_k(Ind(G[W])) != 0 over W}.
"""
import itertools


def adj_from_edges(n, edges):
    adj = [0] * n
    for a, b in edges:
        adj[a] |= (1 << b)
        adj[b] |= (1 << a)
    return adj


def has_claw(n, adj):
    for v in range(n):
        N = [u for u in range(n) if (adj[v] >> u) & 1]
        L = len(N)
        for i in range(L):
            for j in range(i + 1, L):
                if (adj[N[i]] >> N[j]) & 1:
                    continue
                for k in range(j + 1, L):
                    if ((adj[N[i]] >> N[k]) & 1) == 0 and ((adj[N[j]] >> N[k]) & 1) == 0:
                        return True
    return False


def matching_number(n, adj):
    edges = [(a, b) for a in range(n) for b in range(a + 1, n) if (adj[a] >> b) & 1]
    best = [0]

    def rec(idx, used, size):
        if idx == len(edges):
            if size > best[0]:
                best[0] = size
            return
        # bound
        if size + (len(edges) - idx) <= best[0]:
            # weak bound; still do simple prune via remaining vertices
            pass
        a, b = edges[idx]
        # skip
        rec(idx + 1, used, size)
        if not (used >> a) & 1 and not (used >> b) & 1:
            if size + 1 > best[0]:
                best[0] = size + 1
            rec(idx + 1, used | (1 << a) | (1 << b), size + 1)

    rec(0, 0, 0)
    return best[0]


def induced_matching_number(n, adj):
    edges = [(a, b) for a in range(n) for b in range(a + 1, n) if (adj[a] >> b) & 1]
    m = len(edges)
    best = [0]

    def is_induced(chosen):
        # chosen: list of edge indices; check pairwise no cross edge
        for i in range(len(chosen)):
            a, b = edges[chosen[i]]
            for j in range(i + 1, len(chosen)):
                c, d = edges[chosen[j]]
                if ((adj[a] >> c) & 1) or ((adj[a] >> d) & 1) or ((adj[b] >> c) & 1) or ((adj[b] >> d) & 1):
                    return False
        return True

    def rec(idx, used, chosen):
        # prune: even taking all remaining can't beat best
        if len(chosen) + (m - idx) <= best[0]:
            return
        if idx == m:
            if is_induced(chosen) and len(chosen) > best[0]:
                best[0] = len(chosen)
            return
        a, b = edges[idx]
        rec(idx + 1, used, chosen)
        if not (used >> a) & 1 and not (used >> b) & 1:
            chosen.append(idx)
            # incremental induced check
            ok = True
            for j in chosen[:-1]:
                c, d = edges[j]
                if ((adj[a] >> c) & 1) or ((adj[a] >> d) & 1) or ((adj[b] >> c) & 1) or ((adj[b] >> d) & 1):
                    ok = False
                    break
            if ok:
                if len(chosen) > best[0]:
                    best[0] = len(chosen)
                rec(idx + 1, used | (1 << a) | (1 << b), chosen)
            chosen.pop()

    rec(0, 0, [])
    return best[0]


def _rank_modp(rows, ncols, p):
    M = [row[:] for row in rows]
    r = 0
    nrows = len(M)
    for c in range(ncols):
        piv = -1
        for i in range(r, nrows):
            if M[i][c] % p != 0:
                piv = i
                break
        if piv < 0:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c] % p, p - 2, p)
        M[r] = [(v * inv) % p for v in M[r]]
        for i in range(nrows):
            if i != r and M[i][c] % p != 0:
                f = M[i][c] % p
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(ncols)]
        r += 1
    return r


def _rank_qq(rows, ncols):
    from fractions import Fraction
    M = [[Fraction(v) for v in row] for row in rows]
    r = 0
    nrows = len(M)
    for c in range(ncols):
        piv = -1
        for i in range(r, nrows):
            if M[i][c] != 0:
                piv = i
                break
        if piv < 0:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = 1 / M[r][c]
        M[r] = [v * inv for v in M[r]]
        for i in range(nrows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(ncols)]
        r += 1
    return r


def reg_SI_modp(n, adj, p=32003, cap=None, witness=False):
    """Return reg(S/I(G)) via Hochster over F_p. If witness, also return a
    witness subset W and degree k with Htilde_k != 0 attaining reg."""
    best = 0
    bestW = None
    bestk = None
    N = 1 << n
    for mask in range(1, N):
        verts = [i for i in range(n) if (mask >> i) & 1]
        s = len(verts)
        if s - 1 <= best and cap is None:
            # max possible contribution of this W is s-1 (k<=s-2 -> k+1<=s-1);
            # skip only if it cannot beat best. Htilde_{s-1} impossible
            # (need s+1 vertices), so contribution <= s-1.
            if s - 1 <= best:
                continue
        # independent sets of G[W]
        # faces by size: index map for boundary matrices
        idx = {0: 0}
        faces = [[]]  # faces[d] = list of bitmasks with d+1 vertices, d>=0; faces[0]=singletons
        sing = []
        pos = {}
        for v in verts:
            pos[v] = len(sing)
            sing.append(v)
        faces[0] = [(1 << v) for v in verts]
        # build higher faces incrementally
        d = 1
        cur = []
        # pairs
        for ii in range(s):
            for jj in range(ii + 1, s):
                a, b = verts[ii], verts[jj]
                if not ((adj[a] >> b) & 1):
                    cur.append((1 << a) | (1 << b))
        allfaces = [faces[0], cur]
        while allfaces[-1]:
            prev = allfaces[-1]
            prevset = set(prev)
            nxt = []
            # extend each face by a vertex > max to avoid dupes
            for f in prev:
                m = max(i for i in range(n) if (f >> i) & 1)
                for v in verts:
                    if v <= m:
                        continue
                    if (f >> v) & 1:
                        continue
                    # check v nonadjacent to all of f
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
                        nf = f | (1 << v)
                        # all subfaces present automatically by construction? need check:
                        # remove each vertex once, check in prevset -- for induced flag complex ok by induction
                        nxt.append(nf)
            allfaces.append(nxt)
        if not allfaces[-1]:
            allfaces.pop()
        dimC = [len(f) for f in allfaces]  # dimC[d] = # d-faces
        maxd = len(allfaces) - 1
        #Quick: if maxd + 1 <= best then even top homology k=maxd-? contributes
        # k+1 <= maxd (since k<=maxd-1 for reduced nonzero... k=maxd possible if
        # cycles). contribution <= maxd+... keep simple: contribution k+1 <= maxd+1.
        if maxd + 1 <= best:
            continue
        # boundary ranks
        # index maps
        idxmaps = []
        for d_ in range(len(allfaces)):
            idxmaps.append({f: i for i, f in enumerate(allfaces[d_])})
        ranks = {}  # ranks[d] = rank of d_d : C_d -> C_{d-1}, d>=1; ranks[0] = rank of aug
        # augmentation rank: 0 if no vertices else 1 (for nonempty W)
        ranks[0] = 1
        for d_ in range(1, len(allfaces)):
            if not allfaces[d_]:
                ranks[d_] = 0
                continue
            nrows = dimC[d_ - 1]
            ncols = dimC[d_]
            rows = [[0] * ncols for _ in range(nrows)]
            for j, f in enumerate(allfaces[d_]):
                # boundary: alternate sum over removing t-th vertex (ordered)
                vs = [i for i in range(n) if (f >> i) & 1]
                for t, v in enumerate(vs):
                    g = f ^ (1 << v)
                    i = idxmaps[d_ - 1][g]
                    rows[i][j] = (rows[i][j] + (1 if t % 2 == 0 else p - 1)) % p
            ranks[d_] = _rank_modp(rows, ncols, p) if nrows and ncols else 0
        # homology dims
        for k in range(0, maxd + 1):
            ck = dimC[k]
            rk = ranks.get(k, 0)  # rank out of C_k (aug for k=0)
            rkp1 = ranks.get(k + 1, 0)
            hk = ck - rk - rkp1
            if hk > 0 and k + 1 > best:
                best = k + 1
                bestW = mask
                bestk = k
                if cap is not None and best > cap:
                    if witness:
                        return best, bestW, bestk
                    return best
    if witness:
        return best, bestW, bestk
    return best
