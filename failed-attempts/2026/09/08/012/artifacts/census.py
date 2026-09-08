#!/usr/bin/env python3
"""Certified S9-orbit census: rank-4 paving matroids on [9] with <= 2 large hyperplanes.

Pipeline (stdlib only, deterministic, no randomness):
  1. Build the 18 orbit representatives (section 1 of DRAFT).
  2. Validate each: triple-partition axiom, basis exchange, rank 4,
     large-hyperplane recovery (blocks == size>=4 hyperplanes).
  3. S9-orbit enumeration: orbit size, stabilizer order, lex-least check,
     pairwise orbit disjointness.
  4. Tutte polynomial by memoized deletion-contraction under TWO pivot orders;
     cross-check T(1,1)=#bases, T(2,1)=130+#bases, T(1,2)=#spanning (direct).
  5. U(2,5) minor certificate (contraction pair C + 5-set E') per orbit.
  6. Global lemmas: PG(3,2) cap bound (no binary paving (4,9) at all);
     U(2,5) not GF(2)/GF(3)-representable (normalized matrix search);
     explicit ternary quadric 9-set witness (all triples independent, rank 4,
     >=3 large blocks, hence outside the slice).
Writes orbit_table.jsonl + run_meta.json; prints human summary.
"""
import itertools
import json
import sys
import time
import hashlib

N = 9
R = 4
GROUND = tuple(range(N))
ALL3 = [frozenset(t) for t in itertools.combinations(GROUND, 3)]
ALL4 = [frozenset(q) for q in itertools.combinations(GROUND, 4)]
S9_ORDER = 362880  # 9!

# ---------------------------------------------------------------- matroid core
def matroid_from_blocks(blocks):
    """Bases = all 4-sets except those contained in some block."""
    blocks = [frozenset(b) for b in blocks]
    nb = set()
    for b in blocks:
        for q in itertools.combinations(sorted(b), R):
            nb.add(frozenset(q))
    return frozenset(q for q in ALL4 if q not in nb)

def rank_of(S, bases):
    S = set(S)
    return max(len(S & set(b)) for b in bases)

def closure(S, bases):
    S = set(S)
    r = rank_of(S, bases)
    return frozenset(S | {e for e in GROUND if e not in S and rank_of(S | {e}, bases) == r})

def check_exchange(bases):
    B = set(bases)
    bl = list(bases)
    for b1 in bl:
        for b2 in bl:
            if b1 == b2:
                continue
            for x in b1 - b2:
                if not any(((b1 - {x}) | {y}) in B for y in b2 - b1):
                    return False, (sorted(b1), sorted(b2), x)
    return True, None

def hyperplanes(bases):
    """All rank-3 flats (= closures of 3-sets with rank 3)."""
    out = set()
    for t in ALL3:
        if rank_of(t, bases) == 3:
            out.add(closure(t, bases))
    return out

def n_spanning(bases):
    n = 0
    for k in range(N + 1):
        for s in itertools.combinations(GROUND, k):
            if rank_of(s, bases) == R:
                n += 1
    return n

# ---------------------------------------------------------------- Tutte via DC
def tutte_dc(bases, ground, pivot):
    """Tutte polynomial as dict {(i,j): c}; memoized deletion-contraction."""
    memo = {}
    def mulx(p): return {(i + 1, j): c for (i, j), c in p.items()}
    def muly(p): return {(i, j + 1): c for (i, j), c in p.items()}
    def add(p, q):
        d = dict(p)
        for k, v in q.items():
            d[k] = d.get(k, 0) + v
        return d
    def rec(g, bs):
        key = (g, bs)
        if key in memo:
            return memo[key]
        if not g:
            return {(0, 0): 1}
        e = pivot(g)
        rest = tuple(x for x in g if x != e)
        inany = any(e in b for b in bs)
        if not inany:  # loop
            res = muly(rec(rest, bs))
        elif all(e in b for b in bs):  # coloop
            res = mulx(rec(rest, frozenset(b - {e} for b in bs)))
        else:
            bdel = frozenset(b for b in bs if e not in b)
            bcon = frozenset(b - {e} for b in bs if e in b)
            res = add(rec(rest, bdel), rec(rest, bcon))
        memo[key] = res
        return res
    return rec(tuple(ground), frozenset(bases))

def teval(p, x, y):
    return sum(c * (x ** i) * (y ** j) for (i, j), c in p.items())

# ---------------------------------------------------------------- S9 action
def apply_perm_block(blocks, p):
    return tuple(sorted(tuple(sorted(p[e] for e in b)) for b in blocks))

def orbit_data(blocks):
    """Full S9 image set of the block family; returns (orbit_size, is_lex_least)."""
    key0 = apply_perm_block(blocks, tuple(range(N)))
    seen = set()
    least = key0
    for p in itertools.permutations(range(N)):
        k = apply_perm_block(blocks, p)
        seen.add(k)
        if k < least:
            least = k
    return len(seen), (key0 == least), seen

# ---------------------------------------------------------------- U(2,5) minor
def find_U25_minor(bases):
    """Find contraction pair C and 5-set E' with M/C|E' ~= U(2,5).

    Certificate check: C independent; every pair of E' independent in M/C
    (all 10 pairs are bases of the rank-2 minor); every triple of E' dependent
    in M/C. Then M/C \\ (E \\ (C+E')) is exactly U(2,5)."""
    for C in itertools.combinations(GROUND, 2):
        if rank_of(C, bases) != 2:
            continue
        Cset = set(C)
        rest = [e for e in GROUND if e not in Cset]
        # rank of X in M/C = rank_M(X+C) - 2
        def rcon(X):
            return rank_of(set(X) | Cset, bases) - 2
        cands = [e for e in rest if rcon([e]) == 1]
        for E in itertools.combinations(cands, 5):
            if any(rcon([a, b]) != 2 for a, b in itertools.combinations(E, 2)):
                continue
            if any(rcon(list(t)) != 2 for t in itertools.combinations(E, 3)):
                continue
            if rcon(list(E)) != 2:
                continue
            D = sorted(set(GROUND) - Cset - set(E))
            return sorted(C), sorted(E), D
    return None

def check_U25_witness(bases, C, E):
    Cset, Eset = set(C), set(E)
    assert rank_of(Cset, bases) == 2
    def rcon(X): return rank_of(set(X) | Cset, bases) - 2
    assert rcon(E) == 2
    for a, b in itertools.combinations(E, 2):
        assert rcon([a, b]) == 2, (C, E, (a, b))
    for t in itertools.combinations(E, 3):
        assert rcon(list(t)) == 2, (C, E, t)
    return True

# ---------------------------------------------------------------- global lemmas
def pg32_no9cap():
    """Every 9-subset of F2^4\\{0} contains a dependent triple. Returns count."""
    pts = list(range(1, 16))
    bad_free = 0
    for S in itertools.combinations(pts, 9):
        ok = True
        for a, b, c in itertools.combinations(S, 3):
            if (a ^ b ^ c) == 0:
                ok = False
                break
        if ok:
            bad_free += 1
    return bad_free  # expect 0

def U25_nonrep(q):
    """Exhaustion over normalized [I2|A] (A is 2x3): True if NO U(2,5) rep over GF(q)."""
    assert q in (2, 3)
    for A in itertools.product(range(q), repeat=6):
        cols = [(1, 0), (0, 1),
                (A[0], A[1]), (A[2], A[3]), (A[4], A[5])]
        ok = True
        for i, j in itertools.combinations(range(5), 2):
            d = (cols[i][0] * cols[j][1] - cols[i][1] * cols[j][0]) % q
            if d == 0:
                ok = False
                break
        if ok:
            return False, cols  # found a representation (unexpected)
    return True, None

def rank_mod(vecs, q):
    rows = [list(v) for v in vecs]
    Rr, Cc, rr = len(rows), len(rows[0]), 0
    for c in range(Cc):
        piv = None
        for i in range(rr, Rr):
            if rows[i][c] % q != 0:
                piv = i
                break
        if piv is None:
            continue
        rows[rr], rows[piv] = rows[piv], rows[rr]
        inv = pow(rows[rr][c] % q, -1, q)
        rows[rr] = [(x * inv) % q for x in rows[rr]]
        for i in range(Rr):
            if i != rr and rows[i][c] % q != 0:
                f = rows[i][c] % q
                rows[i] = [(a - f * b) % q for a, b in zip(rows[i], rows[rr])]
        rr += 1
    return rr

def quadric_witness():
    """9 columns in PG(3,3): elliptic-quadric zero set minus one point."""
    Z = [(0,0,1,1),(0,0,1,2),(0,1,0,1),(0,1,0,2),(1,0,0,1),
         (1,0,0,2),(1,1,1,0),(1,1,2,0),(1,2,1,0),(1,2,2,0)]
    W = Z[:9]
    assert rank_mod(W, 3) == 4
    for t in itertools.combinations(W, 3):
        assert rank_mod(list(t), 3) == 3
    # large circuits-blocks of the induced paving matroid: 4-sets of rank 3
    big = []
    for q in itertools.combinations(range(9), 4):
        if rank_mod([W[i] for i in q], 3) == 3:
            big.append(sorted(q))
    return W, big

# ---------------------------------------------------------------- representatives
def build_reps():
    reps = []  # (name, blocks)
    reps.append(("U49", []))
    for a in (4, 5, 6, 7, 8):
        reps.append((f"k1-{a}", [tuple(range(a))]))
    A44 = (tuple(range(4)),)
    cases = [(4,4,0),(4,4,1),(4,4,2),(4,5,0),(4,5,1),(4,5,2),
             (4,6,1),(4,6,2),(4,7,2),(5,5,1),(5,5,2),(5,6,2)]
    for (a,b,t) in cases:
        A = tuple(range(a))
        # B shares first t elements of A, rest fresh
        B = tuple(list(range(t)) + list(range(a, a + (b - t))))
        assert len(set(A) | set(B)) <= 9, (a,b,t)
        assert len(set(A) & set(B)) == t, (a,b,t)
        reps.append((f"k2-{a}-{b}-t{t}", [A, B]))
    return reps

def main():
    t0 = time.time()
    reps = build_reps()
    assert len(reps) == 18, len(reps)
    rows = []
    seen_union = set()
    for name, blocks in reps:
        blocks = [tuple(sorted(b)) for b in blocks]
        bases = matroid_from_blocks(blocks)
        assert len(bases) > 0, name
        assert rank_of(GROUND, bases) == 4, name
        # triple-partition axiom: each triple in at most one block (then exactly one hyperplane)
        for i in range(len(blocks)):
            assert len(blocks[i]) >= 4 or len(blocks) == 0, name
            for j in range(i+1, len(blocks)):
                assert len(set(blocks[i]) & set(blocks[j])) <= 2, (name, blocks)
        covered = sum(1 for t in ALL3 for b in blocks if set(t) <= set(b))
        # each triple in <=1 block
        for t in ALL3:
            assert sum(1 for b in blocks if set(t) <= set(b)) <= 1, (name, t)
        # basis exchange
        ok, info = check_exchange(bases)
        assert ok, (name, info)
        # large-hyperplane recovery
        H = hyperplanes(bases)
        big = sorted([sorted(h) for h in H if len(h) >= 4])
        assert big == sorted([sorted(b) for b in blocks]), (name, big)
        # S9 orbit
        osize, isleast, seen = orbit_data(blocks)
        assert isleast, (name, "not lex least")
        assert S9_ORDER % osize == 0, name
        assert seen.isdisjoint(seen_union), (name, "orbit overlap!")
        seen_union |= seen
        # Tutte, two pivots
        pmax = tutte_dc(bases, GROUND, pivot=lambda g: g[-1])
        pmin = tutte_dc(bases, GROUND, pivot=lambda g: g[0])
        assert pmax == pmin, (name, "pivot disagreement")
        T11, T21, T12 = teval(pmax,1,1), teval(pmax,2,1), teval(pmax,1,2)
        assert T11 == len(bases), name
        assert T21 == 130 + len(bases), name
        assert T12 == n_spanning(bases), name
        # U(2,5) minor
        wit = find_U25_minor(bases)
        assert wit is not None, (name, "no U25 minor")
        C, E, D = wit
        check_U25_witness(bases, C, E)
        # hyperplane type partition (sorted block sizes + small-hyperplane count)
        nsmall = sum(1 for h in H if len(h) == 3)
        rows.append({
            "name": name,
            "blocks": [sorted(b) for b in blocks],
            "n_bases": len(bases),
            "n_hyperplanes_small": nsmall,
            "orbit_size": osize,
            "stabilizer_order": S9_ORDER // osize,
            "T11": T11, "T21": T21, "T12": T12,
            "tutte_poly": sorted([[i,j,c] for (i,j),c in pmax.items()]),
            "U25_contract": C, "U25_ground": E, "U25_delete": D,
        })
        print(f"{name}: blocks={[sorted(b) for b in blocks]} nb={len(bases)} "
              f"orb={osize} stab={S9_ORDER//osize} T=({T11},{T21},{T12}) C={C} E={E}", flush=True)
    # ---- global lemmas
    assert pg32_no9cap() == 0
    print("PG(3,2): 0 triple-independent 9-sets among C(15,9)=5005. [no binary paving (4,9)]", flush=True)
    for q in (2, 3):
        nor, _ = U25_nonrep(q)
        assert nor, q
        print(f"U(2,5): no normalized [I2|A] representation over GF({q}).", flush=True)
    W, big = quadric_witness()
    print(f"Quadric witness: 9 cols rank 4, all C(9,3)=84 triples independent; "
          f"{len(big)} rank-3 4-sets (large blocks), e.g. {big[:4]}", flush=True)
    assert len(big) >= 3
    # max pairwise intersection among witness blocks (non-sparse-paving check, informational)
    mi = 0
    for i in range(len(big)):
        for j in range(i+1, len(big)):
            mi = max(mi, len(set(big[i]) & set(big[j])))
    print(f"Witness max block-block intersection: {mi}", flush=True)
    # ---- write artifacts
    with open("output/artifacts/orbit_table.jsonl", "w") as f:
        for r in rows:
            f.write(json.dumps(r, sort_keys=True) + "\n")
    blob = "".join(json.dumps(r, sort_keys=True) + "\n" for r in rows)
    meta = {
        "n_orbits": len(rows),
        "S9": S9_ORDER,
        "slice": "nblocks_large<=2",
        "sha256_orbit_table": hashlib.sha256(blob.encode()).hexdigest(),
        "elapsed_s": round(time.time() - t0, 1),
        "deps": "python3 stdlib only",
        "witness_blocks": big,
        "witness_max_intersection": mi,
    }
    with open("output/artifacts/run_meta.json", "w") as f:
        json.dump(meta, f, indent=2, sort_keys=True)
    print("elapsed %.1fs  sha256=%s" % (meta["elapsed_s"], meta["sha256_orbit_table"]))

if __name__ == "__main__":
    main()
