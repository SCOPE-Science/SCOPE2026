#!/usr/bin/env python3
"""Exhaustive tolerance-1 triple-Tverberg audit for 13-point configs in R^3.

Triple-hull intersection for a fixed ordered 3-partition = LP feasibility:
  3 convex-sum rows + 6 agreement rows = 9 equalities in m unknowns (m=13 full,
  m=12 per deletion). Carathreodory (<=4 support per part in R^3) makes the
  restricted basis enumeration complete. UNSAT verdicts are additionally
  guarded by a nonsingularity flag (at least one nonsingular basis seen).
"""
import sys, os, json, time, math
from itertools import combinations
import numpy as np

B_VEC = np.array([1., 1., 1., 0., 0., 0., 0., 0., 0.])

# ---------------- partitions ----------------
def gen_partitions13(minsize=2):
    n, k = 13, 3
    res = []
    a = [0] * n

    def rec(i, mx):
        if i == n:
            if mx == k - 1:
                c0 = c1 = c2 = 0
                for v in a:
                    if v == 0:
                        c0 += 1
                    elif v == 1:
                        c1 += 1
                    else:
                        c2 += 1
                if c0 >= minsize and c1 >= minsize and c2 >= minsize:
                    res.append(bytes(a))
            return
        for v in range(mx + 2):
            if v > k - 1:
                break
            a[i] = v
            rec(i + 1, mx if mx > v else v)

    rec(1, 0)
    P = np.empty((len(res), n), dtype=np.uint8)
    for i, b in enumerate(res):
        P[i] = np.frombuffer(b, dtype=np.uint8)
    return P


def get_partitions(cache_path):
    if os.path.exists(cache_path):
        P = np.load(cache_path)
        assert P.shape == (235092, 13), P.shape
        return P
    P = gen_partitions13()
    assert P.shape[0] == 235092, P.shape  # S(13,3)-26533 singleton-part ones
    np.save(cache_path, P)
    return P


# ---------------- bases ----------------
def bases_for(sizes):
    m = sum(sizes)
    b0, b1 = sizes[0], sizes[0] + sizes[1]
    out, keys = [], []
    for S in combinations(range(m), 9):
        k0 = sum(1 for c in S if c < b0)
        k1 = sum(1 for c in S if b0 <= c < b1)
        k2 = 9 - k0 - k1
        if k0 == 0 or k1 == 0 or k2 == 0:
            continue
        if k0 > 4 or k1 > 4 or k2 > 4:
            continue
        out.append(S)
        keys.append(max(k0, k1, k2) - min(k0, k1, k2))
    order = np.argsort(np.array(keys), kind="stable")
    return np.array(out, dtype=np.int64)[order]


BASES = {}
def bases(sizes):
    key = tuple(sizes)  # ordered: must match E column-block order
    if key not in BASES:
        BASES[key] = bases_for(key)
    return BASES[key]


# ---------------- LP core ----------------
def build_E(C, lab, active):
    idx = np.where(active)[0]
    labs = lab[idx]
    m0 = [i for i, l in enumerate(labs) if l == 0]
    m1 = [i for i, l in enumerate(labs) if l == 1]
    m2 = [i for i, l in enumerate(labs) if l == 2]
    sizes = (len(m0), len(m1), len(m2))
    if min(sizes) == 0:
        return None
    order = np.array(m0 + m1 + m2)
    pts = C[idx][order]
    m = len(idx)
    n0, n1 = sizes[0], sizes[1]
    E = np.zeros((9, m))
    E[0, :n0] = 1.0
    E[1, n0:n0 + n1] = 1.0
    E[2, n0 + n1:] = 1.0
    for k in range(3):
        E[3 + k, :n0] = pts[:n0, k]
        E[3 + k, n0:n0 + n1] = -pts[n0:n0 + n1, k]
        E[6 + k, :n0] = pts[:n0, k]
        E[6 + k, n0 + n1:] = -pts[n0 + n1:, k]
    return E, (sizes[0], sizes[1], sizes[2])


def triple_hit(E, Bmats, tol=1e-7, batch=25):
    """Batched basis enumeration. Returns (hit, witness_or_None, nonsing)."""
    B = Bmats.shape[0]
    nonsing = False
    for s in range(0, B, batch):
        Sb = Bmats[s:s + batch]
        M = np.stack([E[:, c] for c in Sb], axis=0)  # (Bb,9,9)
        rhs = np.tile(B_VEC, (len(M), 1))
        try:
            X = np.linalg.solve(M, rhs)
            ok_solve = [True] * len(M)
        except np.linalg.LinAlgError:
            X = np.zeros((len(M), 9))
            ok_solve = []
            for j in range(len(M)):
                try:
                    X[j] = np.linalg.solve(M[j], B_VEC)
                    ok_solve.append(True)
                except np.linalg.LinAlgError:
                    ok_solve.append(False)
        for j in range(len(M)):
            if not ok_solve[j]:
                continue
            nonsing = True
            if X[j].min() >= -tol and np.abs(M[j] @ X[j] - B_VEC).max() <= 1e-6:
                return True, X[j], True
    return False, None, nonsing


# ---------------- configs ----------------
def check_genpos(X):
    """Exact integer general-position check: no 3 collinear, no 4 coplanar."""
    n = len(X)
    for i, j, k in combinations(range(n), 3):
        d = X[j] - X[i]
        e = X[k] - X[i]
        if np.cross(d, e).tolist() == [0, 0, 0]:
            return False
    for q in combinations(range(n), 4):
        M = np.stack([X[q[1]] - X[q[0]], X[q[2]] - X[q[0]],
                      X[q[3]] - X[q[0]]]).astype(np.int64)
        if round(float(np.linalg.det(M))) == 0:
            return False
    return True


def cfg_moment(a):
    t = np.arange(a, a + 13)
    return np.stack([t, t ** 2, t ** 3], axis=1)


def cfg_randcube(seed, box=30):
    rng = np.random.default_rng(seed)
    for _ in range(200):
        X = rng.integers(-box, box + 1, size=(13, 3))
        if len(np.unique(X, axis=0)) < 13:
            continue
        if check_genpos(X):
            return X
    raise RuntimeError("no genpos cube found")


def cfg_pert_cube(seed):
    rng = np.random.default_rng(seed)
    base = np.array([[x, y, z] for x in (-5, 5) for y in (-5, 5)
                     for z in (-5, 5)] + [[0, 0, 7], [0, 7,
                                                      0], [7, 0, 0],
                                          [0, 0, 0], [3, 3, 3]])
    for _ in range(500):
        X = base + rng.integers(-2, 3, size=(13, 3))
        if len(np.unique(X, axis=0)) < 13:
            continue
        if check_genpos(X):
            return X
    raise RuntimeError("no perturbed cube found")


def cfg_skew(seed):
    rng = np.random.default_rng(seed)
    for _ in range(500):
        X = np.zeros((13, 3), dtype=np.int64)
        X[:7, 0] = rng.integers(-15, 16, size=7)
        X[:7, 1] = rng.integers(-1, 2, size=7)
        X[:7, 2] = rng.integers(-1, 2, size=7)
        X[7:, 0] = rng.integers(-1, 2, size=6)
        X[7:, 1] = rng.integers(-15, 16, size=6)
        X[7:, 2] = 10 + rng.integers(-1, 2, size=6)
        if len(np.unique(X, axis=0)) < 13:
            continue
        if check_genpos(X):
            return X
    raise RuntimeError("no skew config found")


# ---------------- audit ----------------
_G = {}

def _init(C, P):
    _G["C"] = C
    _G["P"] = P


def _step1(chunk):
    C, P = _G["C"], _G["P"]
    act = np.ones(13, dtype=bool)
    surv, unc = [], 0
    for g in chunk:
        r = build_E(C, P[g], act)
        if r is None:
            continue
        E, sz = r
        hit, _, ns = triple_hit(E, bases(sz))
        if hit:
            surv.append(g)
        elif not ns:
            unc += 1
    return surv, unc


def _step2(chunk):
    C, P = _G["C"], _G["P"]
    out = {}
    for g in chunk:
        lab = P[g]
        kill = None
        for d in range(13):
            act = np.ones(13, dtype=bool)
            act[d] = False
            r = build_E(C, lab, act)
            if r is None:
                kill = d
                break
            E, sz = r
            hit, _, _ = triple_hit(E, bases(sz))
            if not hit:
                kill = d
                break
        out[int(g)] = kill  # None => tolerant partition
    return out


def audit(X, P, nproc, tag):
    t0 = time.time()
    C = X.astype(float)
    C = (C - C.mean(axis=0)) / max(C.std(), 1e-12)
    import multiprocessing as mp
    ctx = mp.get_context("fork")
    pool = ctx.Pool(nproc, initializer=_init, initargs=(C, P))
    try:
        idx = np.arange(len(P))
        chunks = np.array_split(idx, max(nproc * 4, 1))
        surv_all, unc = [], 0
        for surv, u in pool.imap_unordered(_step1, [c for c in chunks]):
            surv_all.extend(surv)
            unc += u
        t1 = time.time()
        kills, tolerant = {}, []
        if surv_all:
            schunks = np.array_split(np.array(surv_all),
                                     max(min(len(surv_all),
                                             nproc * 4), 1))
            for out in pool.imap_unordered(_step2, [c for c in schunks]):
                for g, k in out.items():
                    if k is None:
                        tolerant.append(int(g))
                    else:
                        kills[int(g)] = int(k)
        t2 = time.time()
    finally:
        pool.close()
        pool.join()
    return {
        "tag": tag,
        "n_partitions": len(P),
        "n_full_survivors": len(surv_all),
        "n_uncertain": unc,
        "n_tolerant": len(tolerant),
        "tolerant_examples": tolerant[:5],
        "kills_sample": dict(list(kills.items())[:10]),
        "n_killed": len(kills),
        "time_step1": t1 - t0,
        "time_step2": t2 - t1,
        "coords": X.tolist(),
    }


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--nproc", type=int, default=30)
    ap.add_argument("--which", default="moment-6")
    ap.add_argument("--outdir", default="output/artifacts")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--cache", default="output/artifacts/partitions13.npy")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    P = get_partitions(a.cache)
    print("partitions:", len(P), flush=True)

    def get(which):
        if which.startswith("moment"):
            return cfg_moment(int(which.split("-")[1]))
        if which.startswith("cube"):
            return cfg_randcube(int(which[4:]))
        if which.startswith("pert"):
            return cfg_pert_cube(int(which[4:]))
        if which.startswith("skew"):
            return cfg_skew(int(which[4:]))
        raise ValueError(which)

    if a.selftest:
        X = get("moment-6")
        assert check_genpos(X)
        C = X.astype(float)
        C = (C - C.mean(axis=0)) / max(C.std(), 1e-12)
        act = np.ones(13, dtype=bool)
        t0 = time.time()
        H = U = 0
        for g in range(3000):
            E, sz = build_E(C, P[g], act)
            hit, _, ns = triple_hit(E, bases(sz))
            H += bool(hit)
            U += (not hit and not ns)
        print(f"selftest 3000 parts: hits={H} uncertain={U} "
              f"time={time.time()-t0:.2f}s", flush=True)
        return
    X = get(a.which)
    print(a.which, "genpos:", check_genpos(X), flush=True)
    r = audit(X, P, a.nproc, a.which)
    p = os.path.join(a.outdir, f"ledger_{a.which}.json")
    json.dump(r, open(p, "w"))
    print(json.dumps({k: v for k, v in r.items()
                      if k not in ("coords", "kills_sample")},
                     indent=1), flush=True)


if __name__ == "__main__":
    main()
