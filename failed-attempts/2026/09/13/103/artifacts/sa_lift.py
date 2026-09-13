"""Bounded heuristic lift search for symmetric 2-(100,45,20) with Bush-type
partition + partition-preserving orthogonal polarity (canonical choice:
p = 5 disjoint class-swaps, pi = id, zero blocks on swap pairs, trace 20).

Hard constraints (by construction): N symmetric 0/1, zero pattern.
Soft (penalties): design eqns ||N^2-(25I+20J)||_F^2, block margins 5, trace 20.
Moves: single symmetric-pair flips. Time-boxed simulated annealing with
restarts from best. Success = total penalty 0 with full verification.
"""
import json, time, sys
import numpy as np

def build_problem(seed=0):
    rng = np.random.default_rng(seed)
    n = 100
    cls = np.repeat(np.arange(10), 10)
    swaps = {0:1,1:0,2:3,3:2,4:5,5:4,6:7,7:6,8:9,9:8}
    allowed = np.ones((n, n), dtype=bool)
    for i in range(10):
        j = swaps[i]
        allowed[i*10:(i+1)*10, j*10:(j+1)*10] = False
    # target slice sums: row i, block-class J -> 0 if J==swaps[cls[i]] else 5
    tgt = np.full((n, 10), 5, dtype=int)
    for i in range(n):
        tgt[i, swaps[int(cls[i])]] = 0
    # init: random symmetric respecting mask, density ~0.5 on allowed upper triangle
    N = np.zeros((n, n), dtype=np.int8)
    iu = np.triu_indices(n, 1)
    m = allowed[iu]
    flip = (rng.random(m.sum()) < 0.5)
    N[iu[0][m], iu[1][m]] = flip.astype(np.int8)
    N = (N + N.T).astype(np.int8)
    # diagonal: exactly 2 ones per diagonal block (trace 20), at allowed spots
    # (whole diagonal allowed since swap pairs are off-diagonal blocks)
    for b in range(10):
        idx = np.arange(b*10, b*10+10)
        pick = rng.choice(idx, size=2, replace=False)
        N[pick, pick] = 1
    T = (25*np.eye(n) + 20*np.ones((n, n))).astype(np.int64)
    return N, allowed, tgt, T, cls

def objective(N, allowed, tgt, T, w_m, w_tr):
    G = N.astype(np.int64) @ N.astype(np.int64)
    f_design = int(((G - T)**2).sum())
    S = N.reshape(100, 10, 10).sum(axis=2).astype(np.int64)
    f_margin = int(((S - tgt)**2).sum())
    tr = int(np.trace(N))
    f_tr = (tr - 20)**2
    return f_design + w_m*f_margin + w_tr*f_tr, f_design, f_margin, tr

def anneal(time_budget, seed=0, w_m=64, w_tr=64, log_every=20000):
    t0 = time.time()
    rng = np.random.default_rng(seed)
    N, allowed, tgt, T, cls = build_problem(seed)
    iu_all0 = np.triu_indices(100, 0)
    amask = allowed[iu_all0]  # candidate flip positions (upper triangle incl diag)
    cand_r = iu_all0[0][amask]; cand_c = iu_all0[1][amask]
    ncand = len(cand_r)
    cur, fd, fm, tr = objective(N, allowed, tgt, T, w_m, w_tr)
    best = cur; bestN = N.copy(); bestinfo = (fd, fm, tr)
    Temp0, Temp1 = 60.0, 0.15
    it = 0; acc = 0
    log = [{"iter": 0, "total": cur, "design": fd, "margin": fm, "trace": tr,
            "elapsed": 0.0}]
    while True:
        el = time.time() - t0
        if el >= time_budget:
            break
        frac = el / time_budget
        Temp = Temp0 * (Temp1/Temp0)**frac
        # batch of flips per temperature eval to amortize python overhead? No:
        # single flip per numpy eval (matmul dominates anyway).
        k = rng.integers(ncand)
        i, j = int(cand_r[k]), int(cand_c[k])
        old = N[i, j]
        N[i, j] = 1 - old
        if i != j:
            N[j, i] = 1 - old
        new, fd2, fm2, tr2 = objective(N, allowed, tgt, T, w_m, w_tr)
        d = new - cur
        if d <= 0 or rng.random() < np.exp(-d/max(Temp, 1e-9)):
            cur, fd, fm, tr = new, fd2, fm2, tr2
            acc += 1
            if new < best:
                best = new; bestN = N.copy(); bestinfo = (fd2, fm2, tr2)
                if best == 0:
                    break
        else:
            N[i, j] = old
            if i != j:
                N[j, i] = old
        it += 1
        if it % log_every == 0:
            log.append({"iter": it, "total": cur, "best": best, "design": fd,
                        "margin": fm, "trace": tr, "elapsed": round(time.time()-t0, 2)})
        # periodic restart from best (basin hopping) every 200k iters
        if it % 200000 == 0 and (cur > best):
            N = bestN.copy()
            cur, fd, fm, tr = best, bestinfo[0], bestinfo[1], bestinfo[2]
    el = time.time() - t0
    return {"iters": it, "accepted": acc, "best": best,
            "best_design": bestinfo[0], "best_margin": bestinfo[1],
            "best_trace": bestinfo[2], "elapsed": round(el, 2),
            "w_m": w_m, "w_tr": w_tr, "seed": seed, "log": log}, bestN

if __name__ == "__main__":
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 60.0
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    out = sys.argv[3] if len(sys.argv) > 3 else "output/artifacts/sa_log.json"
    res, bestN = anneal(budget, seed)
    with open(out, "w") as f:
        json.dump(res, f)
    np.save(out.replace(".json", "_bestN.npy"), bestN)
    print(json.dumps({k: v for k, v in res.items() if k != "log"}))
