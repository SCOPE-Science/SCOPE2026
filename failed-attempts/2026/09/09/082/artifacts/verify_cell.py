#!/usr/bin/env python3
"""Full-cell verifier: A8 cube base + 3 single-element extension orbits.
Recomputes: bases, Tutte/beta via deletion-contraction, chi' cross-check,
3-connectivity + internal-4-connectivity verdicts, orbit completeness.
Also writes dc_logs.json (deletion-contraction traces) and orbit_table.json.
Exit prints VERIFY_OK on success."""
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

def bases_of(cols, r):
    n = len(cols); B = []
    for S in itertools.combinations(range(n), r):
        if rank_of([cols[i] for i in S]) == r: B.append(sorted(S))
    return B

def mat_apply(rows, v):
    w = 0
    for i, r in enumerate(rows):
        if bin(r & v).count('1') % 2: w |= 1 << i
    return w

# ---------- 1. base A8 ----------
A8 = [1 | ((x & 1) << 1) | ((x & 2) << 1) | ((x & 4) << 1) for x in range(8)]
assert len(set(A8)) == 8 and all(c != 0 for c in A8)
assert rank_mask(A8, 255) == 4
B8 = bases_of(A8, 4)
assert len(B8) == 56, len(B8)

# A8 is 3-connected: no 1- or 2-separations
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
rE8, s8 = seps_of(A8)
assert not any(mn >= 1 and l < 1 for (_, _, l, a, b) in s8 for mn in [min(a, b)])
assert not any(min(a, b) >= 2 and l < 2 for (_, _, l, a, b) in s8)

# ---------- 2. stabilizer + column orbits (completeness of signature table) ----------
S8 = set(A8)
stab = []
nz = list(range(1, 16))
for r0 in nz:
    for r1 in nz:
        if r1 == r0: continue
        bad = {0, r0, r1, r0 ^ r1}
        for r2 in nz:
            if r2 in bad: continue
            bad2 = {a ^ b for a in bad for b in (0, r2)}
            for r3 in nz:
                if r3 in bad2: continue
                rows = (r0, r1, r2, r3)
                if all(mat_apply(rows, c) in S8 for c in A8):
                    stab.append(rows)
assert len(stab) == 1344, len(stab)  # AGL(3,2)
orbits = []; used = set()
for v in range(16):
    if v in used: continue
    o = set(mat_apply(g, v) for g in stab)
    orbits.append(sorted(o)); used |= o
assert sorted(len(o) for o in orbits) == [1, 7, 8], orbits
orb_of = {}
for o in orbits:
    for v in o: orb_of[v] = tuple(o)
assert orb_of[0] == (0,)
assert 0b0001 in orb_of and len(orb_of[0b0001]) == 8
assert 0b0010 in orb_of and len(orb_of[0b0010]) == 7
# transitivity witnesses: every column equivalent to one of 0000/0001/0010
for v in range(16):
    rep = 0 if v == 0 else (0b0001 if orb_of[v] == orb_of[0b0001] else 0b0010)
    assert any(mat_apply(g, v) == rep for g in stab), v

# ---------- 3. orbit representatives + invariants ----------
EXT = {"E0_loop": A8 + [0b0000], "E2_parallel": A8 + [0b0001], "E1_simple": A8 + [0b0010]}

def tutte_logged(cols):
    n = len(cols); full = (1 << n) - 1; rc = {}
    def r(m):
        if m not in rc: rc[m] = rank_mask(cols, m)
        return rc[m]
    memo = {}; log = []
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
        if is_loop:
            res = {(i, j + 1): v for (i, j), v in T(C, D | (1 << e)).items()}
            log.append({"C": C, "D": D, "e": e, "type": "loop", "factor": "y"})
        elif is_coloop:
            res = {(i + 1, j): v for (i, j), v in T(C | (1 << e), D).items()}
            log.append({"C": C, "D": D, "e": e, "type": "coloop", "factor": "x"})
        else:
            A = T(C, D | (1 << e)); B = T(C | (1 << e), D)
            res = dict(A)
            for k, v in B.items(): res[k] = res.get(k, 0) + v
            log.append({"C": C, "D": D, "e": e, "type": "split"})
        memo[key] = res
        return res
    return T(0, 0), log, len(memo)

def chi_beta(cols):
    n = len(cols); full = (1 << n) - 1
    rE = rank_mask(cols, full); tot = 0
    for m in range(1 << n):
        rx = rank_mask(cols, m)
        if rx < rE: tot += ((-1) ** bin(m).count('1')) * (rE - rx)
    return ((-1) ** (rE + 1)) * tot

results, logs = {}, {}
for name, cols in EXT.items():
    n = len(cols)
    B = bases_of(cols, 4)
    loops = [i for i in range(n) if cols[i] == 0]
    pp = [[i, j] for i in range(n) for j in range(i + 1, n) if cols[i] != 0 and cols[i] == cols[j]]
    P, log, ns = tutte_logged(cols)
    beta = P.get((1, 0), 0)
    assert beta == chi_beta(cols), (name, beta)
    t11 = sum(P.values())
    assert t11 == len(B), (name, t11, len(B))
    rE, seps = seps_of(cols)
    assert rE == 4
    k1 = [(X, Y, l) for (X, Y, l, a, b) in seps if min(a, b) >= 1 and l < 1]
    k2 = [(X, Y, l) for (X, Y, l, a, b) in seps if min(a, b) >= 2 and l < 2]
    v3 = [(X, Y, l) for (X, Y, l, a, b) in seps if min(a, b) >= 3 and l < 3]
    conn3 = (not k1 and not k2)
    int4 = conn3 and all(min(bin(X).count('1'), bin(Y).count('1')) <= 3 for (X, Y, l) in v3)
    F = lambda X: sorted(i for i in range(n) if (X >> i) & 1)
    results[name] = {"newcol": format(cols[8], '04b'), "rank": rE, "nbases": len(B),
        "T11": t11, "loops": loops, "parpairs": pp, "beta": beta, "dc_states": ns,
        "dc_steps": len(log), "is_3conn": conn3, "n1": len(k1), "n2": len(k2),
        "n3viol": len(v3), "int4": int4,
        "threesep_sample": [[F(X), F(Y), l] for (X, Y, l) in v3[:10]],
        "onesep_sample": [[F(X), F(Y), l] for (X, Y, l) in k1[:2]],
        "twosep_sample": [[F(X), F(Y), l] for (X, Y, l) in k2[:4]],
        "tutte": sorted([list(k) + [v] for k, v in P.items()])}
    logs[name] = log

# ---------- 4. headline assertions ----------
assert results["E0_loop"]["beta"] == 0 and results["E0_loop"]["nbases"] == 56
assert results["E0_loop"]["loops"] == [8] and not results["E0_loop"]["is_3conn"]
assert results["E2_parallel"]["beta"] == 6 and results["E2_parallel"]["nbases"] == 84
assert results["E2_parallel"]["parpairs"] == [[0, 8]] and not results["E2_parallel"]["is_3conn"]
assert results["E1_simple"]["beta"] == 7 and results["E1_simple"]["nbases"] == 88
assert results["E1_simple"]["loops"] == [] and results["E1_simple"]["parpairs"] == []
assert results["E1_simple"]["is_3conn"] and not results["E1_simple"]["int4"]
assert results["E1_simple"]["n3viol"] == 10
# pairwise non-isomorphic via (loop, parallel-pair) profile + bases/beta
sig = {n: (tuple(r["loops"]), tuple(map(tuple, r["parpairs"])), r["nbases"], r["beta"]) for n, r in results.items()}
assert len(set(sig.values())) == 3
# E1's killer 4|5 separation with lambda 2
assert any(sorted(len(a) for a in [s[0], s[1]]) == [4, 5] and s[2] == 2 for s in results["E1_simple"]["threesep_sample"])
# every column of GF(2)^4 accounted: 1 + 8 + 7 = 16
assert sum(sorted(len(o) for o in orbits)) == 16

with open("output/artifacts/orbit_table.json", "w") as f:
    json.dump(results, f, indent=1)
with open("output/artifacts/dc_logs.json", "w") as f:
    json.dump({k: {"steps": v, "nsteps": len(v)} for k, v in logs.items()}, f)
print("E0:", results["E0_loop"]["nbases"], "bases beta", results["E0_loop"]["beta"])
print("E2:", results["E2_parallel"]["nbases"], "bases beta", results["E2_parallel"]["beta"])
print("E1:", results["E1_simple"]["nbases"], "bases beta", results["E1_simple"]["beta"])
print("VERIFY_OK")
