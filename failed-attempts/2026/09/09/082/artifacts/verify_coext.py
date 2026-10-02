#!/usr/bin/env python3
"""Literal rank-5 coextension verifier: N(c)/8 = A8 for all c in GF(2)^8.
Enumerates 16 row-cosets, Aut(A8)-orbits (sizes 1/8/7), per-orbit Tutte/beta
via deletion-contraction with chi' cross-check, and exhaustive separator scans
(3-connectivity + internal-4-connectivity verdicts). Prints VERIFY_COEXT_OK."""
import itertools, json

def rank_of(cols):
    piv = {}
    for c in cols:
        v = c
        while v:
            b = v.bit_length() - 1
            if b in piv: v ^= piv[b]
            else: piv[b] = v; break
    return len(piv)

def rank_mask(cols, m):
    return rank_of([cols[i] for i in range(len(cols)) if (m >> i) & 1])

def mat_apply(rows, v):
    w = 0
    for i, r in enumerate(rows):
        if bin(r & v).count('1') % 2: w |= 1 << i
    return w

A8 = [1 | ((x & 1) << 1) | ((x & 2) << 1) | ((x & 4) << 1) for x in range(8)]
B8 = set(S for S in itertools.combinations(range(8), 4) if rank_of([A8[i] for i in S]) == 4)
assert len(B8) == 56

def Nc(cvec):
    cols = [A8[j] | (((cvec >> j) & 1) << 4) for j in range(8)] + [1 << 4]
    return cols

# 1. contraction N(c)/8 = A8 for ALL 256 c
for cvec in range(256):
    cols = Nc(cvec)
    assert rank_of(cols) == 5, cvec
    cb = set(S for S in itertools.combinations(range(8), 4)
             if rank_mask(cols, sum(1 << i for i in S) | (1 << 8)) == 5)
    assert cb == B8, cvec

# 2. stabilizer perms + row space cosets
S8 = set(A8)
stab_rows = []
for r0 in range(1, 16):
    for r1 in range(1, 16):
        if r1 == r0: continue
        bad = {0, r0, r1, r0 ^ r1}
        for r2 in range(1, 16):
            if r2 in bad: continue
            bad2 = {a ^ b for a in bad for b in (0, r2)}
            for r3 in range(1, 16):
                if r3 in bad2: continue
                rows = (r0, r1, r2, r3)
                if all(mat_apply(rows, c) in S8 for c in A8):
                    stab_rows.append(rows)
assert len(stab_rows) == 1344
def perm_of(g):
    return [A8.index(mat_apply(g, c)) for c in A8]
perms = [perm_of(g) for g in stab_rows]
rows8 = []
for i in range(4):
    m = 0
    for j in range(8):
        if (A8[j] >> i) & 1: m |= 1 << j
    rows8.append(m)
rowsp = set()
for s in range(16):
    v = 0
    for i in range(4):
        if (s >> i) & 1: v ^= rows8[i]
    rowsp.add(v)
assert len(rowsp) == 16
canon = lambda c: min(c ^ w for w in rowsp)
reps = []
seen = set()
for c in range(256):
    k = canon(c)
    if k not in seen: seen.add(k); reps.append(k)
assert len(reps) == 16
def act(p, c):
    q = [0]*8
    for i, v in enumerate(p): q[v] = i
    r = 0
    for j in range(8):
        if (c >> q[j]) & 1: r |= 1 << j
    return canon(r)
orbits = []; used = set()
for c in reps:
    if c in used: continue
    o = set(act(p, c) for p in perms)
    orbits.append(sorted(o)); used |= o
assert sorted(len(o) for o in orbits) == [1, 7, 8], [len(o) for o in orbits]

def tutte_beta(cols):
    n = len(cols); full = (1 << n) - 1; rc = {}
    def r(m):
        if m not in rc: rc[m] = rank_mask(cols, m)
        return rc[m]
    memo = {}; nsteps = [0]
    def T(C, D):
        key = (C, D)
        if key in memo: return memo[key]
        alive = full ^ D; todo = alive ^ C
        if todo == 0: return {(0, 0): 1}
        e = (todo & (-todo)).bit_length() - 1
        rC = r(C)
        is_loop = (r(C | (1 << e)) == rC)
        rT = r(C | todo) - rC; rTe = r(C | (todo ^ (1 << e))) - rC
        is_coloop = (rT > rTe)
        assert not (is_loop and is_coloop)
        nsteps[0] += 1
        if is_loop: res = {(i, j + 1): v for (i, j), v in T(C, D | (1 << e)).items()}
        elif is_coloop: res = {(i + 1, j): v for (i, j), v in T(C | (1 << e), D).items()}
        else:
            A = T(C, D | (1 << e)); B = T(C | (1 << e), D); res = dict(A)
            for k, v in B.items(): res[k] = res.get(k, 0) + v
        memo[key] = res
        return res
    P = T(0, 0)
    return P, nsteps[0], len(memo)

def chi_beta(cols):
    n = len(cols); full = (1 << n) - 1
    rE = rank_mask(cols, full); tot = 0
    for m in range(1 << n):
        rx = rank_mask(cols, m)
        if rx < rE: tot += ((-1) ** bin(m).count('1')) * (rE - rx)
    return ((-1) ** (rE + 1)) * tot

def seps_of(cols):
    n = len(cols); full = (1 << n) - 1
    rE = rank_mask(cols, full)
    rc = {m: rank_mask(cols, m) for m in range(1 << n)}
    out = []
    for X in range(1, full):
        Y = full ^ X
        if X > Y: continue
        a, b = bin(X).count('1'), bin(Y).count('1')
        out.append((X, Y, rc[X] + rc[Y] - rE, a, b))
    return rE, out

F9 = lambda X: sorted(i for i in range(9) if (X >> i) & 1)
table = {}
for o in orbits:
    c = o[0]; cols = Nc(c)
    P, steps, ns = tutte_beta(cols)
    beta = P.get((1, 0), 0)
    assert beta == chi_beta(cols), (c, beta)
    nb = sum(1 for S in itertools.combinations(range(9), 5) if rank_of([cols[i] for i in S]) == 5)
    assert sum(P.values()) == nb, (c, sum(P.values()), nb)
    rE, seps = seps_of(cols)
    assert rE == 5
    k1 = [(X, Y, l) for (X, Y, l, a, b) in seps if min(a, b) >= 1 and l < 1]
    k2 = [(X, Y, l) for (X, Y, l, a, b) in seps if min(a, b) >= 2 and l < 2]
    v3 = [(X, Y, l) for (X, Y, l, a, b) in seps if min(a, b) >= 3 and l < 3]
    conn3 = (not k1 and not k2)
    int4 = conn3 and not v3
    table[format(c, '08b')] = {"orbit_size": len(o), "rank": rE, "nbases": nb,
        "beta": beta, "dc_steps": steps, "dc_states": ns, "is_3conn": conn3,
        "n1": len(k1), "n2": len(k2), "n3viol": len(v3), "int4": int4,
        "sep3_sample": [[F9(X), F9(Y), l] for (X, Y, l) in v3[:6]],
        "sep1_sample": [[F9(X), F9(Y), l] for (X, Y, l) in k1[:2]],
        "sep2_sample": [[F9(X), F9(Y), l] for (X, Y, l) in k2[:4]]}

# headline: betas 0/6/7 matching the rank-4 signature table; none internally 4-connected
bybeta = sorted((v["beta"], k) for k, v in table.items())
assert [b for b, _ in bybeta] == [0, 6, 7], bybeta
for k, v in table.items():
    assert not v["int4"], (k, v)
# the minwt-1 orbit (parallel-type): must fail 3-connectivity via a 2-separation;
# the minwt-2 orbit (simple-type analogue): record its status honestly
for k, v in table.items():
    print(k, "orbsz=", v["orbtsz"] if "orbtsz" in v else v["orbit_size"],
          "bases=", v["nbases"], "beta=", v["beta"], "3conn=", v["is_3conn"],
          "n1=", v["n1"], "n2=", v["n2"], "n3viol=", v["n3viol"], "int4=", v["int4"])
    if v["sep3_sample"]: print("   3sep e.g.", v["sep3_sample"][:3])
    if v["sep2_sample"]: print("   2sep e.g.", v["sep2_sample"][:2])
    if v["sep1_sample"]: print("   1sep e.g.", v["sep1_sample"][:2])

with open("output/artifacts/coext_table.json", "w") as f:
    json.dump(table, f, indent=1)
print("VERIFY_COEXT_OK")
