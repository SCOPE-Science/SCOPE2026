"""Fast incremental simulated annealing for symmetric 2-(100,45,20) lift.

Hard constraints by construction: N symmetric 0/1, N=0 on zero-pattern
(swap-pair blocks). Moves: flip symmetric pair (i,j)/(j,i) or diagonal (i,i).
Gram G=N^TN maintained incrementally in O(n) per flip:
  flipping N[i,j] and N[j,i] (i!=j): d=+-1; col i changes by d*e_j, col j by d*e_i.
  G'[a,b] = G[a,b] + d*(N[a,j]*[b==i] ... ) — implemented directly:
  G += d*(outer(e_j, col_i) + outer(col_i, e_j)) + d^2*(...)+ symmetric for j.
Simplest correct: keep N int8, keep G int32; on flip of (i,j),(j,i):
  recompute rows/cols i,j of G via N[:,i],N[:,j] dot products — O(n^2)=1e4 ops
  in numpy (~10us). At ~50k iters/s this dominates but numpy handles it.
Actually simplest robust: full-vector update:
  Let u = new_col_i - old_col_i (= d*e_j), v = new_col_j - old_col_j (= d*e_i).
  G' = N'^T N' ; with N' = N + u e_i^T + v e_j^T:
  G'[a,b] = G[a,b] + N[a,i]*u_b... do rank updates with numpy outer products.
We implement the O(n^2)-but-vectorized row/col recompute for (i,j) flips:
  only rows/cols {i,j} of G change? No — G[a,b] changes whenever a or b in {i,j}
  (columns i,j changed). Recompute G[i,:],G[:,i],G[j,:],G[:,j] via dots. O(n^2).
  With n=100 that's 4e4 mults ~ fast in numpy (~20-40us) -> ~25k+ iters/s.
Diagonal flip (i,i): only column i changes -> recompute G[i,:],G[:,i]. O(n^2/2).

Objective: f = sum((G-T)^2) + w_m*margin_pen + w_tr*(tr-20)^2, maintained
incrementally for the G part, exactly for margin/trace parts.
Margin: S = block-class slice sums matrix (100x10); flip (i,j) changes S[i,cb(j)],
S[j,cb(i)] (+diag). Track margin penalty delta exactly.
"""
import json, sys, time
import numpy as np

N_PTS = 100
SWAPS = {0:1,1:0,2:3,3:2,4:5,5:4,6:7,7:6,8:9,9:8}
CLS = np.repeat(np.arange(10), 10)

def build(seed):
    rng = np.random.default_rng(seed)
    allowed = np.ones((N_PTS, N_PTS), dtype=bool)
    for i in range(10):
        j = SWAPS[i]
        allowed[i*10:(i+1)*10, j*10:(j+1)*10] = False
    tgt = np.full((N_PTS, 10), 5)
    for i in range(N_PTS):
        tgt[i, SWAPS[int(CLS[i])]] = 0
    N = np.zeros((N_PTS, N_PTS), dtype=np.int64)
    iu = np.triu_indices(N_PTS, 1)
    m = allowed[iu]
    N[iu[0][m], iu[1][m]] = (rng.random(m.sum()) < 0.45).astype(np.int64)
    N = N + N.T
    for b in range(10):
        idx = np.arange(b*10, b*10+10)
        N[np.sort(rng.choice(idx, size=2, replace=False)),
          np.sort(rng.choice(idx, size=2, replace=False))] = 0  # clear below
        pick = rng.choice(idx, size=2, replace=False)
        N[pick, pick] = 1
        # ensure symmetry of diagonal-block off-diag random part untouched
    iu2 = np.triu_indices(N_PTS, 1)
    N[iu2[1][m], iu2[0][m]] = N[iu2[0][m], iu2[1][m]]  # re-symmetrize (diag untouched)
    # fix: upper triangle already set; lower mirrors it. Diagonal has 2 ones/block.
    N = np.triu(N, 1) + np.triu(N, 1).T + np.diag(np.diag(N))
    N[~allowed] = 0
    return N, allowed, tgt

def run(seed, budget, w_m=64.0, w_tr=64.0, verbose=False):
    t0 = time.time()
    rng = np.random.default_rng(seed + 999)
    N, allowed, tgt = build(seed)
    n = N_PTS
    T = 25*np.eye(n) + 20*np.ones((n, n))
    G = N.T @ N
    D = G - T
    f_design = float((D**2).sum())
    S = N.reshape(n, 10, 10).sum(axis=2)
    SM = S - tgt
    f_margin = float((SM**2).sum())
    tr = float(np.trace(N))
    f = f_design + w_m*f_margin + w_tr*(tr-20)**2
    iu = np.triu_indices(n, 0)
    am = allowed[iu]
    cand_r = iu[0][am]; cand_c = iu[1][am]
    ncand = len(cand_r)
    cols = N  # alias
    best = f; best_t = (f_design, f_margin, tr)
    Temp0, Temp1 = 8.0, 0.02
    it = 0; acc = 0
    # precompute col-block index
    cb = CLS
    while True:
        el = time.time() - t0
        if el >= budget:
            break
        frac = el / budget
        Temp = Temp0 * (Temp1/Temp0)**frac
        k = int(rng.integers(ncand))
        i = int(cand_r[k]); j = int(cand_c[k])
        old = N[i, j]
        d = 1.0 - 2.0*old  # +1 if 0->1, -1 if 1->0; new-old = d
        if i != j:
            # design delta: columns i,j change: newcol_i = col_i + d*e_j, newcol_j = col_j + d*e_i
            ci = N[:, i]; cj = N[:, j]
            # G[a,b] new for a or b in {i,j}:
            # G'[i,i] = G[i,i] + 2*d*N[j,i] + 1 ; but N[j,i]=old. similarly [j,j].
            # G'[i,j] = G'[j,i]: (col_i+d e_j).(col_j + d e_i) = G[i,j] + d*(ci[i]+cj[j]) + d^2*(e_j.e_i=0 + ... ) careful:
            # = G[i,j] + d*(N[i,i] + N[j,j]) + d*d*0? (e_j . e_i = 0; cross terms: d*(e_j.col_j + col_i.e_i) = d*(N[j,j]+N[i,i]); d^2 e_j.e_i = 0.
            # G'[i,b] (b not i,j) = G[i,b] + d*N[j,b]; G'[j,b] = G[j,b] + d*N[i,b].
            # So compute delta of f_design over affected entries: rows/cols i,j (2n-1 unique... 4n entries with symmetry).
            # Affected D entries: (i,i),(j,j),(i,j),(j,i), (i,b),(b,i),(j,b),(b,j) for b not in {i,j}.
            # delta = sum ((x+dx)^2 - x^2) = 2x*dx + dx^2.
            Gij = G[i, j]; Gii = G[i, i]; Gjj = G[j, j]
            dGii = 2*d*old + 1.0
            dGjj = 2*d*old + 1.0
            dGij = d*(N[i, i] + N[j, j])
            # vector parts
            Nb_i = N[:, i].astype(np.float64)  # N[j,b] over b
            Nb_j = N[:, j].astype(np.float64)
            # G[i,b] += d*N[j,b]; G[j,b] += d*N[i,b]
            Di = D[i, :].astype(np.float64); Dj = D[j, :].astype(np.float64)
            drow_i = d*Nb_j  # careful: G[i,b] = sum_a N[a,i]N[a,b]; col i gains d at row j -> G[i,b] += d*N[j,b]. Yes Nb_j.
            drow_j = d*Nb_i
            drow_i[i] = dGii; drow_i[j] = dGij
            drow_j[j] = dGjj; drow_j[i] = dGij
            # f_design delta: entries (i,b),(b,i): 2 per b (symmetric), but (i,i) once, (i,j),(j,i) pair:
            # sum over full matrix: delta = 2*sum_b (2*D[i,b]*dr_i[b] + dr_i[b]^2) for b not in {i,j}, plus diag/pair terms:
            # (i,i): 2*D[ii]*dGii + dGii^2 (once)
            # (j,j): once; (i,j)&(j,i): 2*(2*D[ij]*dGij + dGij^2)
            mask = np.ones(n, dtype=bool); mask[i] = False; mask[j] = False
            dd = (2*Di[mask]*drow_i[mask] + drow_i[mask]**2).sum()
            dd += (2*Dj[mask]*drow_j[mask] + drow_j[mask]**2).sum()
            dd *= 2  # symmetry (b,i),(b,j) mirrors
            dd += (2*D[i,i]*dGii + dGii**2)
            dd += (2*D[j,j]*dGjj + dGjj**2)
            dd += 2*(2*D[i,j]*dGij + dGij**2)
            # margin delta: S[i,cb[j]] += d, S[j,cb[i]] += d
            bj = int(cb[j]); bi = int(cb[i])
            dd_m = 0.0
            sm1 = SM[i, bj]; sm2 = SM[j, bi]
            if bj == bi and i != j and False:
                pass
            # careful if (i,bj)==(j,bi)? Only if i==j. Here i!=j, distinct entries unless i==j. But could S[i,bj] and S[j,bi] be same entry? Only if i==j. So independent.
            dd_m = (2*sm1*d + d*d) + (2*sm2*d + d*d)
            dd_tr = 0.0  # off-diag flip doesn't change trace
            delta = dd + w_m*dd_m
        else:
            # diagonal flip: column i changes by d*e_i; G[i,i]+=2*d*N[i,i]+1; G[i,b]+=d*N[i,b] (b!=i)
            dGii = 2*d*old + 1.0
            Nb = N[:, i].astype(np.float64)
            Di = D[i, :].astype(np.float64)
            drow = d*Nb; drow[i] = dGii
            mask = np.ones(n, dtype=bool); mask[i] = False
            dd = 2*(2*Di[mask]*drow[mask] + drow[mask]**2).sum()
            dd += 2*D[i,i]*dGii + dGii**2
            bi = int(cb[i])
            dd_m = 2*SM[i, bi]*d + d*d
            tr_new = tr + d
            dd_tr = w_tr*((tr_new-20)**2 - (tr-20)**2)
            delta = dd + w_m*dd_m + dd_tr
        if delta <= 0 or rng.random() < np.exp(-delta/max(Temp, 1e-12)):
            # apply
            N[i, j] = 1 - old
            if i != j:
                N[j, i] = 1 - old
                # update G rows/cols
                G[i, :] = G[i, :] + drow_i
                G[:, i] = G[i, :]
                G[j, :] = G[j, :] + drow_j
                G[:, j] = G[j, :]
                D = G - T
                SM[i, bj] += d; SM[j, bi] += d
                # f_margin update via dd_m: recompute exactly cheap? keep incremental:
                f_margin += dd_m
                f_design += dd
                f += delta
            else:
                G[i, :] = G[i, :] + drow
                G[:, i] = G[i, :]
                D = G - T
                SM[i, bi] += d
                f_margin += dd_m
                f_design += dd
                tr += d
                f += delta
            acc += 1
            if f < best:
                best = f
                best_t = (f_design, f_margin, tr if i == j else tr)
                if best == 0:
                    break
        it += 1
    el = time.time() - t0
    return {"seed": seed, "iters": it, "accepted": acc, "best": best,
            "best_design": best_t[0], "best_margin": best_t[1],
            "best_trace": best_t[2], "elapsed": round(el, 2)}, N

if __name__ == "__main__":
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 300.0
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    out = sys.argv[3] if len(sys.argv) > 3 else "output/artifacts/fast_sa_seed0.json"
    res, N = run(seed, budget)
    with open(out, "w") as f:
        json.dump(res, f)
    np.save(out.replace(".json", "_N.npy"), N)
    print(json.dumps(res))
