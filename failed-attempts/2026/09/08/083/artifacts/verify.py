"""Independent verifier (stdlib only): replays the certified crosscap cog.
Reads output/artifacts/diagrams.json; checks:
 (1) Gauss validity (each crossing once over/once under);
 (2) full 2^11 Kauffman-state b1 census == committed distribution;
 (3) Seifert state has 4 circles (b1=8);
 (4) witness masks give 7 circles, b1=5, and nonorientable state graph
     (odd-cycle/loop), hence explicit nonorientable spanning surfaces with
     b1=5, i.e. crosscap number <= 5 for both knots.
Usage: python3 output/artifacts/verify.py
"""
import json
from collections import defaultdict

EXPECTED_DIST = {'5': 2, '6': 30, '7': 169, '8': 472,
                 '9': 698, '10': 522, '11': 155}
WITNESS = {'K11n34': 1707, 'K11n42': 1435}


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


def analyze(gauss, mask):
    n = len(gauss) // 2
    N = len(gauss)
    occ = defaultdict(list)
    for j, g in enumerate(gauss):
        occ[abs(g)].append(j)
    assert len(occ) == n
    for c, v in occ.items():
        assert len(v) == 2 and gauss[v[0]] * gauss[v[1]] < 0
    cross = sorted(occ)
    uf = UF(N)
    epairs = []
    for k, c in enumerate(cross):
        p, q = occ[c]
        p, q = (p, q) if p < q else (q, p)
        A, B, C, D = (p - 1) % N, p, (q - 1) % N, q
        if (mask >> k) & 1 == 0:
            uf.u(A, D)
            uf.u(C, B)
            epairs.append((A, D, C, B))
        else:
            uf.u(A, C)
            uf.u(B, D)
            epairs.append((A, C, B, D))
    rmap = {}
    for j in range(N):
        r = uf.f(j)
        rmap.setdefault(r, len(rmap))
    s = len(rmap)
    b1 = n - s + 1
    edges = [(rmap[uf.f(a)], rmap[uf.f(c)]) for (a, b, c, d) in epairs]
    loop = any(a == b for a, b in edges)
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    col = {}
    bip = True
    for t in range(s):
        if t in col:
            continue
        col[t] = 0
        st = [t]
        while st and bip:
            x = st.pop()
            for w in adj[x]:
                if w not in col:
                    col[w] = col[x] ^ 1
                    st.append(w)
                elif col[w] == col[x]:
                    bip = False
                    break
        if not bip:
            break
    return s, b1, (not bip) or loop


def main():
    data = json.load(open('output/artifacts/diagrams.json'))
    ok = True
    for name in ('K11n34', 'K11n42'):
        gauss = data[name]['gauss']
        assert len(gauss) == 22, name
        dist = defaultdict(int)
        nonor_min = None
        for mask in range(1 << 11):
            s, b1, nonor = analyze(gauss, mask)
            dist[b1] += 1
            if nonor and (nonor_min is None or b1 < nonor_min):
                nonor_min = b1
        dist = {str(k): v for k, v in sorted(dist.items())}
        assert dist == EXPECTED_DIST, (name, dist)
        s0, b0, _ = analyze(gauss, 0)
        assert (s0, b0) == (4, 8), (name, s0, b0)
        s1, b1, no1 = analyze(gauss, WITNESS[name])
        assert (s1, b1, no1) == (7, 5, True), (name, s1, b1, no1)
        assert nonor_min == 5, (name, nonor_min)
        print(f'{name}: census OK, Seifert b1=8, witness mask {WITNESS[name]} '
              f'b1=5 nonorientable OK')
    print('VERIFY_OK')


main()
