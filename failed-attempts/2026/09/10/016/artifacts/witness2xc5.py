"""Sharp-witness certification: disjoint union 2xC5 (nu=2, reg=4).
Exact QQ check via Fraction homology + claw/nu certificates + full log.
Chosen witness: G* = 2 disjoint C5s (vertices 0..4, 5..9). It is claw-free
(max degree 2) and disconnected, hence valid for the fallback (finite simple).
"""
import sys
sys.path.insert(0, 'output/artifacts')
from clawreg import adj_from_edges, has_claw, induced_matching_number, _rank_qq, _rank_modp
from fractions import Fraction

n = 10
edges = [(i, (i + 1) % 5) for i in range(5)] + [(5 + i, 5 + (i + 1) % 5) for i in range(5)]
adj = adj_from_edges(n, edges)
print("edges:", edges)
print("claw-free:", not has_claw(n, adj))
print("nu:", induced_matching_number(n, adj))


def faces_of(mask):
    verts = [i for i in range(n) if (mask >> i) & 1]
    F = [[(1 << v) for v in verts]]
    while True:
        prev = F[-1]
        nxt = []
        for f in prev:
            m = max(i for i in range(n) if (f >> i) & 1)
            for v in range(m + 1, n):
                if (f >> v) & 1:
                    continue
                if not ((mask >> v) & 1):
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
        F.append(nxt)
    return F


def htilde(mask, field):
    F = faces_of(mask)
    dimC = [len(f) for f in F]
    idx = [{f: i for i, f in enumerate(F[d])} for d in range(len(F))]
    rk = {0: 1}
    rankfn = _rank_qq if field == 'qq' else (lambda r, c: _rank_modp(r, c, 32003))
    for d in range(1, len(F)):
        if not F[d]:
            rk[d] = 0
            continue
        rows = [[0] * dimC[d] for _ in range(dimC[d - 1])]
        for j, f in enumerate(F[d]):
            vs = [i for i in range(n) if (f >> i) & 1]
            for t, v in enumerate(vs):
                g = f ^ (1 << v)
                if field == 'qq':
                    rows[idx[d - 1][g]][j] += (1 if t % 2 == 0 else -1)
                else:
                    rows[idx[d - 1][g]][j] = (rows[idx[d - 1][g]][j] + (1 if t % 2 == 0 else 32002)) % 32003
        rk[d] = rankfn(rows, dimC[d])
    out = {}
    for k in range(0, len(F)):
        hk = dimC[k] - rk.get(k, 0) - rk.get(k + 1, 0)
        if hk:
            out[k] = hk
    return out


full = (1 << n) - 1
print("Htilde(full) mod32003:", htilde(full, 'fp'))
print("Htilde(full) QQ:", htilde(full, 'qq'))
# reg lower bound: Htilde_3(full) != 0  => beta_{6,10} != 0 => reg >= 4
# Upper bound: exhaustive scan for any k+1 >= 5
N = 1 << n
bad_fp = []
for mask in range(1, N):
    h = htilde(mask, 'fp')
    for k, d in h.items():
        if k + 1 >= 5:
            bad_fp.append((mask, k, d))
            break
print("masks with Htilde_k, k+1>=5 (fp):", bad_fp)
print("=> reg(S/I) mod32003 =", 4 if not bad_fp else ">=5")
# QQ full-table spot check on the witness mask only (cheap) + nu certificate
import itertools
pairs = [(a, b) for a in range(n) for b in range(a + 1, n) if (adj[a] >> b) & 1]
print("num edges:", len(pairs))
# induced matching of size 2 witness:
print("induced-pair witness: (0,1),(5,6)? cross-check:",
      not ((adj[0] >> 5) & 1) and not ((adj[0] >> 6) & 1) and not ((adj[1] >> 5) & 1) and not ((adj[1] >> 6) & 1))
# no induced 3-matching: brute force triples
cnt3 = 0
for t in itertools.combinations(pairs, 3):
    ok = len(set(t[0]) | set(t[1]) | set(t[2])) == 6
    if ok:
        good = True
        for x in range(3):
            for y in range(x + 1, 3):
                for a in t[x]:
                    for b in t[y]:
                        if (adj[a] >> b) & 1:
                            good = False
        if good:
            cnt3 += 1
print("induced 3-matchings:", cnt3)
