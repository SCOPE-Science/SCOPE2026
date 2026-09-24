#!/usr/bin/env python3
"""Mine witnesses + independent cross-checks from restriction_tables.json."""
import json, math
from collections import Counter

D = json.load(open("output/artifacts/restriction_tables.json"))
P = D["pairs"]

def parts(n):
    if n == 0:
        yield ()
        return
    def rec(n, mx, cur):
        if n == 0:
            yield tuple(cur)
            return
        for f in range(min(mx, n), 0, -1):
            yield from rec(n - f, f, cur + [f])
    yield from rec(n, n, [])

def hook_dim(lam):
    n = sum(lam)
    d = 1
    for r in range(len(lam)):
        for c in range(lam[r]):
            h = (lam[r] - c) + sum(1 for rr in range(r + 1, len(lam)) if lam[rr] > c)
            d *= h
    return math.factorial(n) // d

def transpose(lam):
    if not lam:
        return ()
    m = max(lam)
    return tuple(sum(1 for r in lam if r > c) for c in range(m))

def dom_leq(a, b):
    # a dominates b? return relation string
    n = sum(a)
    sa = [sum(a[:k]) for k in range(1, max(len(a), len(b)) + 1)]
    la = list(a) + [0] * (max(len(a), len(b)) - len(a))
    lb = list(b) + [0] * (max(len(a), len(b)) - len(b))
    pa = [sum(la[:k]) for k in range(1, len(la) + 1)]
    pb = [sum(lb[:k]) for k in range(1, len(lb) + 1)]
    if pa == pb:
        return "equal"
    if all(x >= y for x, y in zip(pa, pb)):
        return "a-dom-b"
    if all(x <= y for x, y in zip(pa, pb)):
        return "b-dom-a"
    return "incomparable"

print("=== induced-dimension check: sum_l mult(a,b;l)dim(l) == [G:H] dim(a)dim(b) ===")
for key, T in P.items():
    m_n = key.split("x")
    m, n = int(m_n[0]), int(m_n[1])
    N = m * n
    idx = math.factorial(N) // (math.factorial(m) * math.factorial(n))
    tbl = T["table"]
    ok = True
    for ab, row in tbl.items():
        a, b = ab.split("|")
        da = hook_dim(tuple(map(int, a.split(",")))) if a else 1
        db = hook_dim(tuple(map(int, b.split(",")))) if b else 1
        s = sum(v * hook_dim(tuple(map(int, l.split(",")))) for l, v in row.items())
        if s != idx * da * db:
            ok = False
            print("FAIL", key, ab, s, idx * da * db)
    print(key, "induced-dim check:", "OK" if ok else "FAIL")

print("=== trivial x trivial row: mult([m],[n];l) == delta(l,[N]) ===")
for key, T in P.items():
    m, n = map(int, key.split("x"))
    N = m * n
    tk = ",".join([str(N)])
    ak = str(m) + "|" + str(n)
    row = T["table"][ak]
    bad = [(l, v) for l, v in row.items() if v != (1 if l == tk else 0)]
    print(key, "trivial-row:", "OK delta" if not bad else f"FAIL {bad}")

print("=== two-row census per pair (alpha,beta two-row; lambda two-row) ===")
for key, T in P.items():
    m, n = map(int, key.split("x"))
    tw = [k for k in T["table"]
          if len(list(map(int, k.split("|")[0].split(",")))) <= 2
          and len(list(map(int, k.split("|")[1].split(",")))) <= 2]
    sub = 0
    mx = 0
    am = None
    for k in tw:
        for l, v in T["table"][k].items():
            if len(list(map(int, l.split(",")))) <= 2 and v:
                sub += 1
                if v > mx:
                    mx = v
                    am = (k, l)
    print(f"{key}: two-row-support rows={len(tw)} nonzero two-row-triples={sub} max={mx} at {am}")

print("=== (2,k) chain: alpha=[2], beta=[k-1,1], lambda=[2k-j,j] matrix ===")
for k in [2, 3, 4, 5, 6]:
    key = f"2x{k}"
    N = 2 * k
    bk = f"{k-1},1" if k > 2 else "1,1"
    # note beta=[k-1,1]: for k=2 that's [1,1]. ok
    row = P[key]["table"][f"2|{bk}"]
    vals = []
    for j in range(0, N // 2 + 1):
        l = f"{N-j},{j}" if j > 0 else f"{N}"
        vals.append((l, row[l]))
    print(key, vals)

print("=== (2,k) chain: alpha=[2], beta=[k] (trivial), lambda two-row ===")
for k in [2, 3, 4, 5, 6]:
    key = f"2x{k}"
    N = 2 * k
    row = P[key]["table"][f"2|{k}"]
    vals = []
    for j in range(0, N // 2 + 1):
        l = f"{N-j},{j}" if j > 0 else f"{N}"
        vals.append((l, row[l]))
    print(key, vals)

print("=== sign x sign rows ===")
for key, T in P.items():
    m, n = map(int, key.split("x"))
    ak = ",".join(["1"] * m) + "|" + ",".join(["1"] * n)
    row = T["table"][ak]
    nz = sorted([(l, v) for l, v in row.items() if v], key=lambda t: -t[1])[:6]
    print(key, "top signxsign:", nz)

print("=== zero-density + argmax dominance relation ===")
for key, T in P.items():
    tot = T["n_entries"]
    nz = T["n_nonzero"]
    a, b, l = T["argmax"]
    print(f"{key}: nonzero {nz}/{tot} ({100*nz/tot:.1f}%), max={T['max_mult']} at a={a} b={b} l={l}")
    print(f"   transpose(a)={list(transpose(tuple(a)))} transpose(b)={list(transpose(tuple(b)))} transpose(l)={list(transpose(tuple(l)))}")
