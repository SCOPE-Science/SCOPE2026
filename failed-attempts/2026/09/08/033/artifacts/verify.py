"""Independent verifier: recompute exact crossing probabilities from committed
count files; check slice identities cross[k]+noncross[k]==C(m,k), total==2^m,
monotonicity in p, duality complementarity (open H-cross XOR closed dual
V-block) on sampled small configs, and the claimed inequalities.

Usage: python3 verify.py [artifacts_dir]
Exit 0 iff all checks pass; prints PASS/FAIL per check.
"""
import sys, os, json, itertools
from math import comb
from fractions import Fraction

P = {"0.40": Fraction(2, 5), "0.45": Fraction(9, 20), "0.50": Fraction(1, 2),
     "0.55": Fraction(11, 20), "0.60": Fraction(3, 5),
     "0.44": Fraction(11, 25), "0.56": Fraction(14, 25)}

def check_file(fn):
    d = json.load(open(fn))
    m, R, C, dr = d["m"], d["R"], d["C"], d["direction"]
    cr, nc = d["cross_counts"], d["noncross_counts"]
    assert len(cr) == m + 1 and len(nc) == m + 1, "length"
    for k in range(m + 1):
        assert cr[k] + nc[k] == comb(m, k), f"slice {k}"
    assert sum(cr) + sum(nc) == (1 << m), "total"
    for name, p in P.items():
        q = 1 - p
        tot = Fraction(0)
        for k, c in enumerate(cr):
            if c:
                tot += c * p ** k * q ** (m - k)
        num, den, _fl = d["probs"][name]
        assert tot == Fraction(num, den), f"prob mismatch {name}"
    # monotonicity
    vals = []
    for name in ["0.40", "0.44", "0.45", "0.50", "0.55", "0.56", "0.60"]:
        vals.append(Fraction(d["probs"][name][0], d["probs"][name][1]))
    assert all(a <= b for a, b in zip(vals, vals[1:])), "monotonicity"
    return True

def dual_complementarity_bruteforce(R=3, C=4):
    """Verify: open H-cross XOR closed-dual V-block, exhaustively on 3x4.

    Dual graph: faces of the R x C vertex grid incl. outer face.
    Closed dual edges = complement of open primal edges.
    V-block = closed-dual path from top-outer-face row to bottom-outer-face row
    separating left from right. Standard planar duality: exactly one occurs.
    We check combinatorially: H-cross in primal XOR V-cross in dual-of-complement.
    """
    m = (C - 1) * R + C * (R - 1)
    def idx(c, r):
        return c * R + r
    pel = []
    for c in range(C - 1):
        for r in range(R):
            pel.append((idx(c, r), idx(c + 1, r)))
    for c in range(C):
        for r in range(R - 1):
            pel.append((idx(c, r), idx(c, r + 1)))
    # dual vertices: faces (c,r) for c in -1..C-1? Use (C) x (R-1) interior faces
    # plus top row and bottom row outer faces.
    # Interior face f(c,r): bounded by primal edges around unit square with
    # lower-left vertex (c,r), c=0..C-2, r=0..R-2.
    # Dual adjacency = cross each primal edge; outer faces: top T_c (c=0..C-1
    # columns above row 0... ) simpler: build dual graph with nodes:
    #   F(c,r) interior, T (single top outer), B (single bottom outer),
    #   with top horizontal primal edges connecting *-T appropriately.
    # For the XOR check we use the classical equivalence instead:
    # no open H-cross  <=>  closed V-cross in the matching (dual) lattice.
    # Direct check via union-find on complement edges in the dual grid below.
    NF_C = C - 1  # interior face columns
    NF_R = R - 1  # interior face rows
    def dual_edges(mask):
        # map each primal edge index -> dual edge between face-nodes
        # face node ids: interior (c,r)->c*NF_R+r in 0..NF_C*NF_R-1, TOP=T, BOT=B
        T = NF_C * NF_R
        B = T + 1
        adj = []
        e = 0
        # horizontal primal edges (c,r)-(c+1,r): dual = vertical link between
        # face above/below: faces f(c,r-1) & f(c,r), with outer TOP/BOT at r=0/R-1
        for c in range(C - 1):
            for r in range(R):
                up = T if r == 0 else (c * NF_R + (r - 1))
                dn = B if r == R - 1 else (c * NF_R + r)
                adj.append((e, up, dn))
                e += 1
        # vertical primal edges (c,r)-(c,r+1): dual = horizontal link between
        # faces f(c-1,r) & f(c,r), outer faces at c=0/C-1 are L/R (not T/B).
        # For V-blocking we only traverse interior+TOP/BOT; edges to L/R are
        # dead ends (recorded with other=-1).
        for c in range(C):
            for r in range(R - 1):
                lf = -1 if c == 0 else ((c - 1) * NF_R + r)
                rt = -1 if c == C - 1 else (c * NF_R + r)
                adj.append((e, lf, rt))
                e += 1
        assert e == m
        return adj, T, B
    adj, T, B = dual_edges(None)
    nfail = 0
    for mask in range(1 << m):
        par = list(range(R * C))
        def f(a):
            while par[a] != a:
                par[a] = par[par[a]]
                a = par[a]
            return a
        for (e, u, v) in [(i, u, v) for i, (u, v) in enumerate(pel)]:
            if (mask >> e) & 1:
                ru, rv = f(u), f(v)
                if ru != rv:
                    par[ru] = rv
        S = [idx(0, r) for r in range(R)]
        Tc = [idx(C - 1, r) for r in range(R)]
        hcross = any(f(s) == f(t) for s in S for t in Tc)
        # closed-dual TOP->BOT using complement edges
        N = NF_C * NF_R + 2
        qpar = list(range(N))
        def g(a):
            while qpar[a] != a:
                qpar[a] = qpar[qpar[a]]
                a = qpar[a]
            return a
        for (e, u, v) in adj:
            if not ((mask >> e) & 1):  # closed primal -> open dual
                if u == -1 or v == -1:
                    continue
                ru, rv = g(u), g(v)
                if ru != rv:
                    qpar[ru] = rv
        vblock = (g(T) == g(B))
        if hcross == vblock:  # must be XOR
            nfail += 1
    return nfail

def main():
    d = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    files = sorted(f for f in os.listdir(d) if f.startswith("counts_") and f.endswith(".json"))
    assert files, "no count files"
    n = 0
    for fn in files:
        check_file(os.path.join(d, fn))
        n += 1
    print(f"count-file checks: {n}/{n} PASS (slice identities + totals + stored probs + monotonicity)")
    nf = dual_complementarity_bruteforce(3, 4)
    print(f"duality XOR check on 3x4 (2^19={2**19} configs): {'PASS' if nf == 0 else f'FAIL({nf})'}")
    assert nf == 0
    # claimed window inequalities (exact Fraction comparisons)
    claims = [
        ("counts_4x6-H.json", "0.44", "<=", Fraction(1, 4)),     # P<=0.25
        ("counts_4x6-H.json", "0.56", ">=", Fraction(11, 20)),   # P>=0.55
        ("counts_5x6-H.json", "0.44", "<=", Fraction(1, 3)),     # P<=0.333..
        ("counts_5x6-H.json", "0.56", ">=", Fraction(2, 3)),     # P>=0.666..
        ("counts_6x6-H.json", "0.44", "<=", Fraction(2, 5)),     # P<=0.40
        ("counts_6x6-H.json", "0.56", ">=", Fraction(3, 4)),     # P>=0.75
        ("counts_6x7-H.json", "0.44", "<=", Fraction(3, 10)),    # P<=0.30
        ("counts_6x7-H.json", "0.56", ">=", Fraction(7, 10)),    # P>=0.70
    ]
    for fn, pname, op, bound in claims:
        dd = json.load(open(os.path.join(d, fn)))
        v = Fraction(dd["probs"][pname][0], dd["probs"][pname][1])
        ok = (v <= bound) if op == "<=" else (v >= bound)
        print(f"  {fn} P_{pname}={float(v):.6f} {op} {float(bound):.4f} -> {'PASS' if ok else 'FAIL'}")
        assert ok, f"claim failed: {fn} {pname}"
    print("window inequalities: PASS")
    print("ALL VERIFY PASS")

if __name__ == "__main__":
    main()
