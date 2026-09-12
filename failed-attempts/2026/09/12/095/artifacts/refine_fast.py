"""Fast block version for SA refinement: vectorized Gram via (36,36) matmuls already;
this variant uses slice-weight + tabu + reheating to escape local minima.
Usage: python3 refine_fast.py RJSON SEED ITERS OUT [T0 T1 REHEATS]"""
import numpy as np
import sys
import json
import math
import time

def rand_regular(r, rng):
    if r == 0:
        return np.zeros((9, 9), dtype=np.int64)
    if r == 9:
        return np.ones((9, 9), dtype=np.int64)
    S = rng.choice(9, size=r, replace=False)
    M = np.zeros((9, 9), dtype=np.int64)
    idx = (np.arange(9)[:, None] + S[None, :]) % 9
    M[np.arange(9)[:, None], idx] = 1
    return M[rng.permutation(9)][:, rng.permutation(9)]

def Efull(A):
    G = A @ A.T
    return (int(((G - 6) ** 2).sum()) - 36 * 81) // 2

def main():
    R = np.array(json.loads(sys.argv[1]), dtype=np.int64)
    seed = int(sys.argv[2])
    iters = int(sys.argv[3])
    out = sys.argv[4]
    T0 = float(sys.argv[5]) if len(sys.argv) > 5 else 1.5
    T1 = float(sys.argv[6]) if len(sys.argv) > 6 else 2e-5
    REH = int(sys.argv[7]) if len(sys.argv) > 7 else 4
    rng = np.random.default_rng(seed)
    A = np.zeros((36, 36), dtype=np.int64)
    for i in range(4):
        for j in range(4):
            A[i * 9:(i + 1) * 9, j * 9:(j + 1) * 9] = rand_regular(int(R[i, j]), rng)
    G = A @ A.T
    E = (int(((G - 6) ** 2).sum()) - 36 * 81) // 2
    bestE, bestA = E, A.copy()
    print(f"[seed {seed}] E0={E}", flush=True)
    t0 = time.time()
    seg = iters // (REH + 1)
    step = 0
    for cyc in range(REH + 1):
        for s in range(seg):
            frac = (cyc * seg + s) / iters
            T = T0 * (T1 / T0) ** frac
            ti = int(rng.integers(4))
            tj = int(rng.integers(4))
            a = int(rng.integers(9))
            b = int(rng.integers(9))
            if b == a:
                continue
            c = int(rng.integers(9))
            d = int(rng.integers(9))
            if d == c:
                continue
            x1, x2 = ti * 9 + a, ti * 9 + b
            y1, y2 = tj * 9 + c, tj * 9 + d
            v11 = int(A[x1, y1])
            if v11 == int(A[x2, y2]) or int(A[x1, y2]) == int(A[x2, y1]) or v11 == int(A[x1, y2]):
                continue
            # delta energy via rows x1,x2 only (ordered-pair energy incl. diagonal pairs;
            # E = (S - 36*81)/2 with S = sum_{x,y} (Gxy-6)^2; only rows/cols x1,x2 change):
            # dS = 2 * sum_{y not in {x1,x2}} [(n1o_y-6)^2-(o1_y-6)^2 + (n2o_y-6)^2-(o2_y-6)^2]
            #      + (2x2 block terms, symmetric => factor 2)
            r1 = A[x1].astype(np.float64)
            r2 = A[x2].astype(np.float64)
            dr = np.zeros(36, dtype=np.float64)
            dr[y1] = 1 - 2 * v11
            dr[y2] = 2 * v11 - 1
            Adr = (A @ dr)
            n1o = G[x1, :].astype(np.float64) + Adr
            n2o = G[x2, :].astype(np.float64) - Adr
            n1 = r1 + dr
            n2 = r2 - dr
            n1o[x1] = float(n1 @ n1)
            n2o[x2] = float(n2 @ n2)
            n1o[x2] = float(n1 @ n2)
            n2o[x1] = float(n1 @ n2)
            def sq(v):
                return (v - 6.0) ** 2
            o1 = G[x1, :].astype(np.float64)
            o2 = G[x2, :].astype(np.float64)
            dS = 0.0
            for y in range(36):
                if y == x1 or y == x2:
                    continue
                dS += sq(n1o[y]) - sq(o1[y]) + sq(n2o[y]) - sq(o2[y])
            dS *= 2.0
            for a, oa, na in ((x1, o1, n1o), (x2, o2, n2o)):
                for b, ob, nb in ((x1, o1, n1o), (x2, o2, n2o)):
                    dS += sq(na[b]) - sq(oa[b])
            dE = dS / 2.0
            if dE <= 0 or rng.random() < math.exp(-dE / T):
                A[x1, y1], A[x1, y2], A[x2, y1], A[x2, y2] = 1 - v11, v11, v11, 1 - v11
                # update G rows/cols x1,x2
                G[x1, :] = n1o
                G[:, x1] = n1o
                G[x2, :] = n2o
                G[:, x2] = n2o
                E = E + dE
                if int(round(E)) < bestE:
                    E = Efull(A)
                    G = A @ A.T
                    bestE, bestA = E, A.copy()
                    print(f"[seed {seed} cyc {cyc} step {step}] E={E} T={T:.5f} t={time.time()-t0:.0f}s",
                          flush=True)
                    if E == 0:
                        break
            step += 1
        else:
            step += cyc * 0
            continue
        break
        if bestE == 0:
            break
    E = Efull(bestA)
    with open(out, "w") as f:
        json.dump({"R": R.tolist(), "seed": seed, "E": int(E), "A": bestA.tolist()}, f)
    print(f"[seed {seed}] DONE bestE={E} t={time.time()-t0:.0f}s", flush=True)

if __name__ == "__main__":
    main()
