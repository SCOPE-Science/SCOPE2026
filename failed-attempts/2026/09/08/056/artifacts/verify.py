"""Independent Hochster verifier (exact integer arithmetic, no numpy rank).
b(Z_K) = 1 + sum_{J nonempty} [tilde b0 + tilde b1 + tilde b2(J)], tilde b2(J) = #tris(J) - rank(d2|_J).
d2 rank over QQ via Bareiss (exact fractions). Cross-checks census numbers for key complexes."""
from fractions import Fraction
import itertools, json, csv

N = 6
EDGES = [(i, j) for i in range(N) for j in range(i + 1, N)]
EIDX = {e: k for k, e in enumerate(EDGES)}
TRIS = list(itertools.combinations(range(N), 3))


def rank_qq(M):
    M = [[Fraction(x) for x in row] for row in M]
    r = 0
    R = len(M)
    C = len(M[0]) if R else 0
    for c in range(C):
        p = next((i for i in range(r, R) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        for i in range(R):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                for j in range(c, C):
                    M[i][j] -= f * M[r][j]
        r += 1
    return r


def betti(emask, tmask):
    E = [EDGES[e] for e in range(15) if (emask >> e) & 1]
    T = [TRIS[t] for t in range(20) if (tmask >> t) & 1]
    b = 1
    per_J = {}
    for J in range(1, 64):
        V = [i for i in range(N) if (J >> i) & 1]
        EJ = [e for e in E if ((J >> e[0]) & 1) and ((J >> e[1]) & 1)]
        TJ = [t for t in T if all((J >> v) & 1 for v in t)]
        k, e, t = len(V), len(EJ), len(TJ)
        p = list(range(N))

        def f(a):
            while p[a] != a:
                p[a] = p[p[a]]
                a = p[a]
            return a

        for (a, c) in EJ:
            ra, rc = f(a), f(c)
            if ra != rc:
                p[ra] = rc
        comp = len(set(f(v) for v in V))
        r = 0
        if t and e:
            jl = {e2: k2 for k2, e2 in enumerate(EJ)}
            M = [[0] * t for _ in range(e)]
            for j, (a, c, d) in enumerate(TJ):
                for (uv, s) in [((a, c), 1), ((a, d), -1), ((c, d), 1)]:
                    (u, v) = uv
                    x, y = (u, v) if u < v else (v, u)
                    M[jl[(x, y)]][j] = s
            r = rank_qq(M)
        h = (comp - 1) + (e - k + comp - r) + (t - r)
        b += h
        if h:
            per_J[J] = h
    return b, per_J


K6 = (1 << 15) - 1
b, pJ = betti(K6, 0)
print("K6:", b)
b2, _ = betti(8191, 0)
print("runner-up 8191:", b2)
b3, _ = betti(31, 0)
print("flagmax 31:", b3)
OCT_E = K6 & ~((1 << EIDX[(0, 1)]) | (1 << EIDX[(2, 3)]) | (1 << EIDX[(4, 5)]))
print("OCT-graph:", betti(OCT_E, 0)[0])
print("OCT-S2:", betti(OCT_E, 31200)[0])
print("CONE:", betti(sum(1 << EIDX[(min(a, b), max(a, b))] for a, b in [(1, 2), (2, 3), (3, 4), (4, 5), (1, 5), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]), 665)[0])
json.dump({"K6": b, "runnerup_8191": b2, "flagmax_31": b3}, open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-162/output/artifacts/verify.json", "w"))
