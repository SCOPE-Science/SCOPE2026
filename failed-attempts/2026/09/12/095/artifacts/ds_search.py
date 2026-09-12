"""Menon (36,15,6) difference set search in Z6 x Z6 via simulated annealing.
State: 15-subset D of 36 group elements. Objective: sum_{g != 0} (N_g - 6)^2,
N_g = #{(d,d') in D^2 : d - d' = g}. Saves design + coset quotient R0.
Usage: python3 ds_search.py SEED ITERS OUTFILE"""
import numpy as np
import sys
import json

def idx(a, b):
    return (a % 6) * 6 + (b % 6)

def energy_of(Dset):
    D = np.array(sorted(Dset))
    pts = np.array([(d // 6, d % 6) for d in D])
    diff = (pts[:, None, :] - pts[None, :, :]) % 6
    H = np.zeros((6, 6), dtype=np.int64)
    for k in range(len(D)):
        for l in range(len(D)):
            if k != l:
                H[diff[k, l, 0], diff[k, l, 1]] += 1
    E = int(((H - 6) ** 2).sum())
    return E, H

def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    iters = int(sys.argv[2]) if len(sys.argv) > 2 else 2000000
    out = sys.argv[3] if len(sys.argv) > 3 else "output/artifacts/ds36.json"
    rng = np.random.default_rng(seed)
    D = set(rng.choice(36, size=15, replace=False).tolist())
    E, _ = energy_of(D)
    best = (E, set(D))
    T0, T1 = 3.0, 1e-4
    import math
    for step in range(iters):
        T = T0 * (T1 / T0) ** (step / iters)
        out_el = rng.choice(sorted(D))
        in_el = rng.integers(36)
        if in_el in D:
            continue
        D2 = set(D)
        D2.discard(out_el)
        D2.add(int(in_el))
        E2, _ = energy_of(D2)
        dE = E2 - E
        if dE <= 0 or rng.random() < math.exp(-dE / T):
            D = D2
            E = E2
            if E < best[0]:
                best = (E, set(D))
                print(f"[{seed} step {step}] E={E} T={T:.4f}", flush=True)
                if E == 0:
                    break
    E, H = energy_of(best[1])
    print(f"FINAL seed={seed} E={E} D={sorted(best[1])}", flush=True)
    if E == 0:
        D = sorted(best[1])
        pts = [(d // 6, d % 6) for d in range(36)]
        # development: blocks = D + g
        Ds = set(D)
        A = np.zeros((36, 36), dtype=int)
        for g in range(36):
            ga, gb = g // 6, g % 6
            for d in D:
                da, db = d // 6, d % 6
                h = idx(da + ga, db + gb)
                A[g, h] = 1
        # H subgroup 2Z6 x 2Z6 (order 9): elements with both coords even
        H = [idx(a, b) for a in (0, 2, 4) for b in (0, 2, 4)]
        # cosets
        reps = []
        seen = set()
        for g in range(36):
            ga, gb = g // 6, g % 6
            cos = frozenset(idx(ga + ha // 6 * 0 + (H[k] // 6), gb + H[k] % 6) for k in range(9))
            # careful: H[k] coords
            cos = frozenset(idx(ga + (H[k] // 6), gb + (H[k] % 6)) for k in range(9))
            if cos not in seen:
                seen.add(cos)
                reps.append(sorted(cos))
        R0 = [[0] * 4 for _ in range(4)]
        for i, Pi in enumerate(reps):
            x = Pi[0]
            for j, Bj in enumerate(reps):
                Bjset = set(Bj)
                R0[i][j] = int(sum(A[g, x] for g in Bjset))
        with open(out, "w") as f:
            json.dump({"D": D, "A": A.tolist(), "classes": reps, "R0": R0}, f)
        print("R0 =", R0, flush=True)

if __name__ == "__main__":
    main()
