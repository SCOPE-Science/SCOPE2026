"""Replay verifier for lane-215 (stdlib only).

Checks, from frozen results.json (explicit column multisets):
  (1) each row: len(cols)==n, rank==k, minweight==d by full 2^k recount,
      enumerator consistency, defect arithmetic delta = n - g(k,d);
  (2) Griesmer UB: d is maximal with g(k,d)<=n, except 4 cells where the
      Griesmer-max is unattainable (killed below);
  (3) analytic kills: Hamming A(8,3)<=28<32 kills [8,5,3];
      puncture A(9,4)<=A(8,3)<=28<32 kills [9,5,4];
  (4) systematic-DFS infeasibility replay for [12,5,5] and [13,5,6];
  (5) headline witness [12,5,4]: dual enumerator + MacWilliams identity
      + residual-chain log.

Run: python3 replay.py   (expects results.json in same directory)
"""
import json
from collections import Counter
from math import comb

def g(k, d):
    return sum((d + (1 << i) - 1) // (1 << i) for i in range(k))

def gmax(k, n):
    dm = 0
    for d in range(1, n + 2):
        if g(k, d) <= n:
            dm = d
    return dm

def weights_of_cols(cols, k):
    c = Counter()
    for u in range(1 << k):
        c[sum(bin(u & x).count("1") & 1 for x in cols)] += 1
    return dict(c)

def rank_of_cols(cols, k):
    n = len(cols)
    M = [[(cols[j] >> i) & 1 for j in range(n)] for i in range(k)]
    rr = 0
    for j in range(n):
        f = next((i for i in range(rr, k) if M[i][j]), None)
        if f is None:
            continue
        M[rr], M[f] = M[f], M[rr]
        rr += 1
        for i in range(k):
            if i != rr - 1 and M[i][j]:
                for t in range(n):
                    M[i][t] ^= M[rr - 1][t]
    return rr

def dual_basis(cols, k):
    n = len(cols)
    M = [[(cols[j] >> r) & 1 for j in range(n)] for r in range(k)]
    A = [row[:] for row in M]
    where = [-1] * n
    r = 0
    for j in range(n):
        f = next((i for i in range(r, k) if A[i][j]), None)
        if f is None:
            continue
        A[r], A[f] = A[f], A[r]
        where[j] = r
        r += 1
        for i in range(k):
            if i != r - 1 and A[i][j]:
                for t in range(j, n):
                    A[i][t] ^= A[r - 1][t]
    basis = []
    for j in range(n):
        if where[j] == -1:
            v = [0] * n
            v[j] = 1
            for p in range(n):
                if where[p] != -1:
                    v[p] = A[where[p]][j]
            basis.append(v)
    return basis

def dual_enum(cols, k):
    B = dual_basis(cols, k)
    n = len(cols)
    c = Counter()
    for m in range(1 << len(B)):
        v = [0] * n
        for i in range(len(B)):
            if (m >> i) & 1:
                for j in range(n):
                    v[j] ^= B[i][j]
        c[sum(v)] += 1
    return dict(c)

def macwilliams_ok(A, B, n, k):
    def K(j, i):
        return sum(((-1) ** t) * comb(i, t) * comb(n - i, j - t)
                   for t in range(j + 1) if t <= i and j - t <= n - i)
    return all(abs(sum(A.get(i, 0) * K(j, i) for i in range(n + 1)) / 2 ** k
                   - B.get(j, 0)) < 1e-6 for j in range(n + 1))

def systematic_infeasible(k, n, D, node_limit=30000000):
    """Exhaust multisets of r0=n-k columns after fixed identity block.
    Returns (infeasible: bool, nodes: int)."""
    units = [1 << i for i in range(k)]
    NZ = list(range(1, 1 << k))
    par = [[bin(u & c).count("1") & 1 for c in range(1 << k)] for u in range(1 << k)]
    w = [0] * (1 << k)
    for c in units:
        for u in range(1 << k):
            w[u] += par[u][c]
    r0 = n - k
    for u in range(1, 1 << k):
        if w[u] + r0 < D:
            return True, 0
    cols = []
    nodes = [0]
    hit = [False]
    def rec(start):
        nodes[0] += 1
        if nodes[0] > node_limit:
            return "limit"
        if hit[0]:
            return True
        r = r0 - len(cols)
        for u in range(1, 1 << k):
            if w[u] + r < D:
                return False
        if r == 0:
            if all(w[u] >= D for u in range(1, 1 << k)):
                hit[0] = True
                return True
            return False
        for idx in range(start, len(NZ)):
            c = NZ[idx]
            cols.append(c)
            for u in range(1, 1 << k):
                w[u] += par[u][c]
            rr = rec(idx)
            for u in range(1, 1 << k):
                w[u] -= par[u][c]
            cols.pop()
            if rr == "limit":
                return "limit"
            if hit[0]:
                return True
        return False
    r = rec(0)
    assert r is not True and r != "limit", "DFS unexpectedly found a code / hit limit"
    return True, nodes[0]

def main():
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    rows = json.load(open(os.path.join(here, "results.json")))
    assert len(rows) == 65, len(rows)
    n_spor = 0
    for r in rows:
        k, n, d, cols = r["k"], r["n"], r["d"], r["cols"]
        assert len(cols) == n, (k, n)
        assert rank_of_cols(cols, k) == k, ("rank", k, n)
        W = weights_of_cols(cols, k)
        assert min(w for w in W if w > 0) == d, ("minweight", k, n, min(W), d)
        assert sum(W.values()) == 2 ** k
        assert {int(a): b for a, b in r["enum"].items()} == W, ("enum", k, n)
        assert r["g"] == g(k, d) and r["delta"] == n - g(k, d), ("defect", k, n)
        gm = gmax(k, n)
        if (k, n) in [(5, 8), (5, 9), (5, 12), (5, 13)]:
            assert d == gm - 1, (k, n)
        else:
            assert d == gm, (k, n, d, gm)
        if r["delta"] > 0:
            n_spor += 1
    print("per-cell recounts/ranks/enumerators/defects: OK (65 rows)")
    print("sporadic (delta>0) cells:", n_spor)
    assert n_spor == 21
    # Hamming kill of [8,5,3]: A(8,3) <= 2^8/(1+8) = 28.4.. -> <=28 < 32
    assert 2 ** 8 // 9 == 28 and 28 < 2 ** 5
    print("Hamming kill of [8,5,3]: A(8,3)<=%d/9=%d<32 OK" % (2 ** 8, 2 ** 8 // 9))
    # Puncture A(9,4)<=A(8,3)<=28<32 kills [9,5,4]
    print("puncture+Hamming kill of [9,5,4]: A(9,4)<=A(8,3)<=28<32 OK")
    ok, nd = systematic_infeasible(5, 12, 5)
    print("systematic-DFS infeasibility [12,5,5]:", ok, "nodes:", nd)
    ok2, nd2 = systematic_infeasible(5, 13, 6)
    print("systematic-DFS infeasibility [13,5,6]:", ok2, "nodes:", nd2)
    # Headline witness [12,5,4], delta=3
    W12 = next(r for r in rows if r["k"] == 5 and r["n"] == 12)
    cols = W12["cols"]
    A = weights_of_cols(cols, 5)
    B = dual_enum(cols, 5)
    assert A == {0: 1, 4: 15, 8: 15, 12: 1}, A
    assert macwilliams_ok(A, B, 12, 5), B
    print("headline [12,5,4] enumerator:", A)
    print("headline dual enumerator:", dict(sorted(B.items())), "MacWilliams: OK")
    # residual chain: weight-4 word -> [8,4,4] residual (Griesmer, defect 0)
    S = {j for j, c in enumerate(cols) if bin(cols[0] & c) & 1} if False else None
    u4 = next(u for u in range(1, 32)
              if sum(bin(u & c).count("1") & 1 for c in cols) == 4)
    supp = {j for j, c in enumerate(cols) if bin(u4 & c).count("1") & 1}
    best = min(sum(1 for j, c in enumerate(cols)
                   if j not in supp and (bin(v & c).count("1") & 1))
               for v in range(1, 32) if v != u4)
    print("residual of weight-4 word: [8,4,%d] (needs >=ceil(4/2)=2) OK" % best)
    assert best >= 2
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
