"""S3b: Gauss-code Kauffman-state census (convention-free).
Arcs e_j = segment from occurrence j to j+1 (mod 22). At crossing i with
occurrences p<q: Seifert/oriented smoothing pairs (e_{p-1},e_q),(e_{q-1},e_p);
the other smoothing pairs (e_{p-1},e_{q-1}),(e_p,e_q). Union-find -> circles.
b1 = c - s + 1. State graph (verts=circles, edges=crossings joining the two
smoothing-arc circles; loop if same) bipartite <=> orientable state surface.
"""
import json
from collections import Counter

def load():
    with open("output/artifacts/diagrams.json") as f:
        return json.load(f)

class UF:
    def __init__(self, n):
        self.p = list(range(n))
    def f(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a
    def u(self, a, b):
        ra, rb = self.f(a), self.f(b)
        if ra != rb:
            self.p[ra] = rb

def analyze(gauss):
    N = len(gauss)  # 22
    assert N == 22
    occ = {}
    for j, g in enumerate(gauss):
        occ.setdefault(abs(g), []).append(j)
    assert all(len(v) == 2 for v in occ.values()) and len(occ) == 11
    # check one over (+) one under (-) per crossing
    for i, (p, q) in occ.items():
        assert gauss[p] * gauss[q] < 0, (i, gauss[p], gauss[q])
    cross = sorted(occ.items())  # [(i,(p,q))...]
    res = []
    for mask in range(1 << 11):
        uf = UF(N)
        edge_circles = []  # per crossing: (circle_of_arc1, circle_of_arc2)
        for k, (i, (p, q)) in enumerate(cross):
            bit = (mask >> k) & 1
            a, b, c, d = (p - 1) % N, p, (q - 1) % N, q  # A=e_a,B=e_b,C=e_c,D=e_d
            if bit == 0:  # oriented/Seifert: A-D, C-B
                uf.u(a, d); uf.u(c, b)
                pairs = ((a, d), (c, b))
            else:         # A-C, B-D
                uf.u(a, c); uf.u(b, d)
                pairs = ((a, c), (b, d))
            edge_circles.append(pairs)
        roots = sorted({uf.f(j) for j in range(N)})
        rmap = {r: t for t, r in enumerate(roots)}
        s = len(roots)
        b1 = 11 - s + 1
        # state graph bipartiteness (loop => non-bipartite)
        adj = {t: [] for t in range(s)}
        keys = list(cross)
        loop = False
        for pairs in edge_circles:
            for (x, y) in pairs:
                pass
            # edge endpoints: circle of first arc-pair and second arc-pair
            t1 = rmap[uf.f(pairs[0][0])]
            t2 = rmap[uf.f(pairs[1][0])]
            if t1 == t2:
                loop = True
                break
            adj[t1].append(t2); adj[t2].append(t1)
        bip = True
        if loop:
            bip = False
        else:
            col = {}
            for t in range(s):
                if t in col:
                    continue
                col[t] = 0
                st = [t]
                while st and bip:
                    u = st.pop()
                    for w in adj[u]:
                        if w not in col:
                            col[w] = col[u] ^ 1
                            st.append(w)
                        elif col[w] == col[u]:
                            bip = False
                            break
        res.append((b1, mask, s, bip))
    return res

def main():
    data = load()
    out = {}
    for name in ("K11n34", "K11n42"):
        res = analyze(data[name]["gauss"])
        assert all(r[2] <= 12 for r in res), "circle count exceeds c+1!"
        dist = Counter(r[0] for r in res)
        seif = [r for r in res if r[1] == 0]
        nonor = sorted([r for r in res if not r[3]])
        print(name, "b1dist", dict(sorted(dist.items())))
        print(name, "Seifert-state b1:", seif[0][0], "circles:", seif[0][2])
        print(name, "min nonorientable b1:", nonor[0][0], "count:", len([r for r in res if not r[3]]),
              "example masks:", [(r[1], r[2]) for r in nonor[:5]])
        out[name] = {"b1_dist": {str(k): v for k, v in sorted(dist.items())},
                     "seifert_b1": seif[0][0], "seifert_circles": seif[0][2],
                     "min_nonor_b1": nonor[0][0],
                     "best_nonor": [{"b1": r[0], "mask": r[1], "circles": r[2]} for r in nonor[:10]]}
    with open("output/artifacts/state_census.json", "w") as f:
        json.dump(out, f, indent=1)
    print("wrote output/artifacts/state_census.json")

main()
