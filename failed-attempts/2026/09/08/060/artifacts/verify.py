"""Self-contained stdlib verifier for the certified group-table transversal /
orthogonal-mate benchmark (orders 7 and 8).

Rebuilds every square from its defining group law (no copied entries except the
explicit mate witnesses, which are CHECKED, not trusted), then verifies:
  - Latin property of all 6 group tables + 5 mate witnesses
  - group axioms (closure/identity/inverses/associativity) of the 6 laws
  - exact transversal counts by exhaustive n! permutation scan
  - explicit transversal witnesses cell-by-cell
  - tau=7 maximal-partial witness for cyclic Z8 + proof T=0 (hence no mate)
  - orthogonality (n^2 distinct pairs) for all 5 claimed Graeco-Latin pairs
Writes output/artifacts/results.json on success. Exit nonzero on any failure.
"""
import itertools, json, os, sys

FAIL = []
def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (" | " + str(detail) if detail else ""))
    if not cond:
        FAIL.append(name)

def is_latin(L):
    n = len(L); S = set(range(n))
    for i in range(n):
        if set(L[i]) != S: return False
        if {L[r][i] for r in range(n)} != S: return False
    return True

def count_transversals(L):
    n = len(L); c = 0; first = None
    for p in itertools.permutations(range(n)):
        if len({L[i][p[i]] for i in range(n)}) == n:
            c += 1
            if first is None: first = list(p)
    return c, first

def check_transversal_witness(L, perm):
    n = len(L)
    if sorted(perm) != list(range(n)): return False
    return len({L[i][perm[i]] for i in range(n)}) == n

def max_partial(L):
    n = len(L); best = [0]; bex = [None]
    def bt(r, cols, syms, chosen):
        if len(chosen) > best[0]:
            best[0] = len(chosen); bex[0] = list(chosen)
        if r == n: return
        if len(chosen) + (n - r) <= best[0]: return
        bt(r + 1, cols, syms, chosen)
        for c in range(n):
            s = L[r][c]
            if c not in cols and s not in syms:
                cols.add(c); syms.add(s); chosen.append((r, c))
                bt(r + 1, cols, syms, chosen)
                chosen.pop(); cols.remove(c); syms.remove(s)
    bt(0, set(), set(), [])
    return best[0], bex[0]

def check_partial_witness(L, cells):
    rows = [r for r, c in cells]; cols = [c for r, c in cells]
    syms = [L[r][c] for r, c in cells]
    return len(set(rows)) == len(cells) and len(set(cols)) == len(cells) and len(set(syms)) == len(cells)

def orth_pairs(A, B):
    n = len(A)
    return len({(A[i][j], B[i][j]) for i in range(n) for j in range(n)})

# ---- group laws (elements labelled 0..n-1 in fixed orders) ----
def cyc(n):
    els = list(range(n))
    def mul(a, b): return (a + b) % n
    return els, mul

def z4xz2():
    els = [(a, b) for a in range(4) for b in range(2)]
    def mul(a, b): return ((a[0] + b[0]) % 4, (a[1] + b[1]) % 2)
    return els, mul

def v8():
    els = list(range(8))
    def mul(a, b): return a ^ b
    return els, mul

def d8():
    els = [(i, j) for j in range(2) for i in range(4)]
    def mul(a, b):
        i, j = a; k, l = b
        return ((i + (k if j == 0 else -k)) % 4, (j + l) % 2)
    return els, mul

def q8():
    umt = {(0, u): (0, u) for u in range(4)}
    umt.update({(u, 0): (0, u) for u in range(4)})
    umt[(1, 1)] = (1, 0); umt[(2, 2)] = (1, 0); umt[(3, 3)] = (1, 0)
    umt[(1, 2)] = (0, 3); umt[(2, 1)] = (1, 3)
    umt[(2, 3)] = (0, 1); umt[(3, 2)] = (1, 1)
    umt[(3, 1)] = (0, 2); umt[(1, 3)] = (1, 2)
    els = [(s, u) for s in range(2) for u in range(4)]
    def mul(a, b):
        s, u = a; t, v = b
        w, un = umt[(u, v)]
        return ((s + t + w) % 2, un)
    return els, mul

def table_of(els, mul):
    idx = {e: i for i, e in enumerate(els)}
    return [[idx[mul(a, b)] for b in els] for a in els]

def check_group(els, mul):
    n = len(els)
    prods = set()
    for a in els:
        for b in els:
            m = mul(a, b)
            if m not in els: return False, "not closed"
            prods.add(m)
    if len(prods) != n: return False, "not a quasigroup table"
    e = next(x for x in els if all(mul(x, a) == a and mul(a, x) == a for a in els))
    for a in els:
        if not any(mul(a, b) == e and mul(b, a) == e for b in els):
            return False, "missing inverse"
    for a in els:
        for b in els:
            for c in els:
                if mul(mul(a, b), c) != mul(a, mul(b, c)):
                    return False, "not associative"
    return True, "order %d" % n

def gf8_mul(a, b):
    p = 0
    while b:
        if b & 1: p ^= a
        a <<= 1
        if a & 8: a ^= 0b1011  # mod x^3+x+1
        b >>= 1
    return p & 7

GROUPS = {
    "Z7": cyc(7), "Z8cyc": cyc(8), "Z4xZ2": z4xz2(),
    "V8": v8(), "D8": d8(), "Q8": q8(),
}
TABLES = {}
for name, (els, mul) in GROUPS.items():
    ok, det = check_group(els, mul)
    check("group-axioms." + name, ok, det)
    TABLES[name] = table_of(els, mul)
    check("latin." + name, is_latin(TABLES[name]))

# ---- exact transversal counts (exhaustive) ----
EXPECTED_T = {"Z7": 133, "Z8cyc": 0, "Z4xZ2": 384, "V8": 384, "D8": 384, "Q8": 384}
COUNTED = {}
for name, L in TABLES.items():
    t, first = count_transversals(L)
    COUNTED[name] = (t, first)
    check("transversal-count." + name, t == EXPECTED_T[name], "T=%d expected %d" % (t, EXPECTED_T[name]))

# ---- explicit transversal witnesses ----
WIT = {
    "Z7": [0, 1, 2, 3, 4, 5, 6],
    "Z4xZ2": [0, 2, 3, 4, 5, 7, 6, 1],
    "V8": [0, 2, 4, 6, 3, 1, 7, 5],
    "D8": [0, 1, 4, 5, 3, 2, 7, 6],
    "Q8": [0, 1, 3, 2, 6, 7, 5, 4],
}
for name, perm in WIT.items():
    check("transversal-witness." + name, check_transversal_witness(TABLES[name], perm), str(perm))

# ---- cyclic order-8: transversal-free, tau=7 certificate ----
Z8 = TABLES["Z8cyc"]
tau, cells = max_partial(Z8)
TAU_WIT = [(1, 0), (2, 1), (3, 2), (4, 3), (5, 5), (6, 6), (7, 7)]
check("Z8.T==0", COUNTED["Z8cyc"][0] == 0, "exhaustive 8! scan")
check("Z8.tau==7", tau == 7, "computed max=%d" % tau)
check("Z8.tau-witness", len(TAU_WIT) == 7 and check_partial_witness(Z8, TAU_WIT), str(TAU_WIT))
check("Z8.no-mate", COUNTED["Z8cyc"][0] == 0,
      "mate needs 8 disjoint transversals; T=0 forbids it")

# ---- orthogonal mates ----
B7 = [[(2 * i + j) % 7 for j in range(7)] for i in range(7)]          # formula witness
C8 = [gf8_mul(2, i) for i in range(8)]
check("V8.C-is-perm", sorted(C8) == list(range(8)), str(C8))
BV8 = [[C8[i] ^ j for j in range(8)] for i in range(8)]                # GF(8) construction
BZ4 = [[1,0,2,5,7,3,4,6],[4,3,0,6,5,2,1,7],[7,1,3,4,6,0,2,5],[6,4,7,1,2,5,3,0],
       [0,6,1,3,4,7,5,2],[2,5,4,0,1,6,7,3],[3,7,5,2,0,4,6,1],[5,2,6,7,3,1,0,4]]
BD8 = [[1,0,2,5,3,4,7,6],[5,1,0,2,7,6,3,4],[6,7,4,3,5,0,1,2],[4,3,6,7,2,5,0,1],
       [0,5,3,1,6,2,4,7],[3,2,1,0,4,7,6,5],[2,6,7,4,0,1,5,3],[7,4,5,6,1,3,2,0]]
BQ8 = [[1,0,2,4,3,6,7,5],[5,2,0,1,4,7,6,3],[6,1,5,7,0,3,4,2],[7,4,1,6,2,5,3,0],
       [0,7,4,3,6,2,5,1],[3,5,7,0,1,4,2,6],[2,6,3,5,7,0,1,4],[4,3,6,2,5,1,0,7]]
MATES = {"Z7": B7, "V8": BV8, "Z4xZ2": BZ4, "D8": BD8, "Q8": BQ8}
HOST = {"Z7": "Z7", "V8": "V8", "Z4xZ2": "Z4xZ2", "D8": "D8", "Q8": "Q8"}
for name, B in MATES.items():
    A = TABLES[HOST[name]]
    n = len(A)
    check("mate-latin." + name, is_latin(B))
    check("mate-orthogonal." + name, orth_pairs(A, B) == n * n,
          "distinct pairs=%d need %d" % (orth_pairs(A, B), n * n))

tB7, _ = count_transversals(B7)
check("mate-T.B7", tB7 == 133, "T=%d" % tB7)

# ---- results.json ----
here = os.path.dirname(os.path.abspath(__file__))
res = {"squares": {}, "mates": {}, "notes": "stdlib-only; counts by exhaustive n! scan"}
for name, L in TABLES.items():
    t, first = COUNTED[name]
    e = {"order": len(L), "latin": True, "T": t}
    if name in WIT: e["transversal_witness_perm"] = WIT[name]
    if name == "Z8cyc":
        e["tau"] = 7; e["tau_witness_cells"] = TAU_WIT; e["has_orthogonal_mate"] = False
    else:
        e["tau"] = len(L); e["has_orthogonal_mate"] = True
    res["squares"][name] = e
for name, B in MATES.items():
    res["mates"][name] = {"host": HOST[name], "matrix": B,
                          "distinct_pairs": orth_pairs(TABLES[HOST[name]], B)}
with open(os.path.join(here, "results.json"), "w") as f:
    json.dump(res, f, indent=1)
print("wrote results.json")

if FAIL:
    print("FAILURES:", FAIL); sys.exit(1)
print("ALL CHECKS PASSED")
