"""Simulated annealing over k-subsets of U to maximize 2-sumset coverage mod p.
Exact integer arithmetic for cost. Geometric schedule T0=2.0 -> Tmin=0.01.
Saves best sets + seeds. Then greedy completion/reduction.
"""
import math, random, time, json, sys
import numpy as np

def U_list(p, digits):
    return [x for x in range(p) if all(int(ch) in digits for ch in str(x))]

def coverage_of_idx(idx, M):
    sub = M[np.ix_(idx, idx)]
    # count distinct via numpy unique
    return np.unique(sub).size

def anneal(U, p, k, seed, n_steps=200000, T0=2.0, Tmin=0.01):
    rng = random.Random(seed)
    n = len(U)
    Uarr = np.array(U, dtype=int)
    M = (Uarr[:, None] + Uarr[None, :]) % p
    cur = np.array(sorted(rng.sample(range(n), k)), dtype=int)
    cur_cov = coverage_of_idx(cur, M)
    cur_cost = p - cur_cov
    best = cur.copy(); best_cov = cur_cov
    # geometric schedule: T(t) = T0 * (Tmin/T0)^(t/n_steps)
    ratio = (Tmin / T0) ** (1.0 / n_steps)
    T = T0
    # local copies for speed
    for t in range(n_steps):
        # swap move: replace one in-set index with one out-of-set
        out_pos = rng.randrange(k)
        inset = set(cur.tolist())
        # pick random outside
        while True:
            cand = rng.randrange(n)
            if cand not in inset:
                break
        prop = cur.copy(); prop[out_pos] = cand
        prop_cov = coverage_of_idx(prop, M)
        prop_cost = p - prop_cov
        d = prop_cost - cur_cost
        if d <= 0 or rng.random() < math.exp(-d / T):
            cur = prop; cur_cov = prop_cov; cur_cost = prop_cost
            if prop_cov > best_cov:
                best_cov = prop_cov; best = prop.copy()
                if best_cov == p:
                    break
        T *= ratio
    best_A = sorted(Uarr[best].tolist())
    return best_A, int(best_cov), int(p - best_cov)

def greedy_complete(A, U, p):
    A = sorted(set(A)); Uset = set(U)
    S = set((a+b) % p for a in A for b in A)
    improved = True
    while len(S) < p and improved:
        improved = False
        best_x, best_gain = None, 0
        for x in U:
            if x in set(A):
                continue
            S2 = set((a+b) % p for a in A+[x] for b in A+[x])
            g = len(S2) - len(S)
            if g > best_gain:
                best_gain = g; best_x = x
        if best_gain > 0:
            A = sorted(A + [best_x]); S = set((a+b) % p for a in A for b in A)
            improved = True
    # prune while cover preserved (only relevant if full cover reached)
    changed = True
    while changed and len(S) == p:
        changed = False
        for x in list(A):
            B = [y for y in A if y != x]
            S2 = set((a+b) % p for a in B for b in B)
            if len(S2) == p:
                A = B; S = S2; changed = True
                break
    return A, len(S)

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, default=197)
    ap.add_argument("--dmax", type=int, default=4)
    ap.add_argument("--k", type=int, default=22)
    ap.add_argument("--restarts", type=int, default=20)
    ap.add_argument("--steps", type=int, default=200000)
    ap.add_argument("--seed0", type=int, default=1000)
    ap.add_argument("--out", type=str, default="")
    args = ap.parse_args()
    digits = set(range(args.dmax+1))
    U = U_list(args.p, digits)
    print(f"p={args.p} Dmax={args.dmax} |U|={len(U)} k={args.k} restarts={args.restarts} steps={args.steps}", flush=True)
    t0 = time.time()
    results = []
    for r in range(args.restarts):
        seed = args.seed0 + r
        A, cov, cost = anneal(U, args.p, args.k, seed, n_steps=args.steps)
        # greedy completion/reduction from best
        Ac, covc = greedy_complete(A, U, args.p)
        results.append({"seed": seed, "A": A, "cov": cov, "cost": cost,
                        "A_completed": Ac, "cov_completed": covc, "len_completed": len(Ac)})
        print(f"restart {r} seed={seed}: k-set cov={cov}/{args.p} cost={cost} |completed|={len(Ac)} covc={covc} A={A}", flush=True)
    # summary
    best = max(results, key=lambda d: (d["cov"], -len(d["A"])))
    print(f"BEST cov={best['cov']}/{args.p} seed={best['seed']} A={best['A']}")
    print(f"elapsed {time.time()-t0:.1f}s")
    if args.out:
        with open(args.out, "w") as f:
            json.dump({"p": args.p, "dmax": args.dmax, "k": args.k, "U": U, "results": results, "best": best}, f, indent=1)
        print(f"wrote {args.out}")
