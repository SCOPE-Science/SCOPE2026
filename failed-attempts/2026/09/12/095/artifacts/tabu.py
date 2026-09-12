"""Tabu-enhanced refinement with pair-violation-driven moves + column-pair acceptance.
State: 36x36 binary, fixed 9x9 tile margins. Energy E over row pairs.
Move proposal: pick a violated pair (x,y) (dev != 0), pick tile columns to fix it;
accept by full-row-pair delta computed exactly on affected rows (vectorized, correct).
Tabu on (x1,x2,y1,y2) with tenure; aspiration on global improvement.
Usage: python3 tabu.py RJSON SEED ITERS OUT"""
import numpy as np
import sys
import json
import time
from collections import deque

def Efull(A):
    G = A @ A.T
    return (int(((G - 6) ** 2).sum()) - 36 * 81) // 2

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

def main():
    R = np.array(json.loads(sys.argv[1]), dtype=np.int64)
    seed = int(sys.argv[2])
    iters = int(sys.argv[3])
    out = sys.argv[4]
    rng = np.random.default_rng(seed)
    A = np.zeros((36, 36), dtype=np.int64)
    for i in range(4):
        for j in range(4):
            A[i * 9:(i + 1) * 9, j * 9:(j + 1) * 9] = rand_regular(int(R[i, j]), rng)
    Af = A.astype(np.float64)
    G = Af @ Af.T
    E = Efull(A)
    bestE, bestA = E, A.copy()
    print(f"[tabu {seed}] E0={E}", flush=True)
    t0 = time.time()
    tabu = {}
    TEN = 25
    log = max(1, iters // 30)
    T0, T1 = 0.9, 1e-4
    for step in range(iters):
        T = T0 * (T1 / T0) ** (step / iters)
        # pick violated pair
        if rng.random() < 0.75:
            dev = G - 6.0
            np.fill_diagonal(dev, 0)
            w = np.abs(dev)
            ws = w.sum()
            if ws <= 0:
                break
            probs = (w.flatten() / ws)
            k = rng.choice(36 * 36, p=probs)
            x1, x2 = divmod(int(k), 36)
            if x1 == x2:
                continue
            ti = x1 // 9
            # need two rows in same point class for tile-margin preservation: x2 must be in same class
            if x2 // 9 != ti:
                # pick random second row in same class
                x2 = ti * 9 + int(rng.integers(9))
                if x2 == x1:
                    continue
            tj = int(rng.integers(4))
            # find switchable columns in tile tj between rows x1,x2: need (1,0)&(0,1) or (0,1)&(1,0)
            cols = tj * 9 + np.arange(9)
            v1 = A[x1, cols]
            v2 = A[x2, cols]
            P = [c for c in range(9) if v1[c] == 1 and v2[c] == 0]
            M = [c for c in range(9) if v1[c] == 0 and v2[c] == 1]
            if not P or not M:
                continue
            y1 = tj * 9 + P[int(rng.integers(len(P)))]
            y2 = tj * 9 + M[int(rng.integers(len(M)))]
        else:
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
        v11 = int(A[x1, y1])
        if v11 == int(A[x2, y2]) or int(A[x1, y2]) == int(A[x2, y1]) or v11 == int(A[x1, y2]):
            continue
        key = (x1, x2, y1, y2)
        is_tabu = tabu.get(key, -1) > step
        # exact delta via full Gram recompute of the two rows (cheap: 2x36 dot products)
        r1 = Af[x1].copy()
        r2 = Af[x2].copy()
        r1[y1] -= v11
        r1[y2] += v11
        r1n = r1.copy()
        r1n[y1] += 1 - v11
        r1n[y2] += v11 - 0  # net: r1[y1]=1-v11, r1[y2]=v11
        # simpler: construct directly
        n1 = Af[x1].copy()
        n2 = Af[x2].copy()
        n1[y1], n1[y2] = 1 - v11, v11
        n2[y1], n2[y2] = v11, 1 - v11
        o1 = G[x1].copy()
        o2 = G[x2].copy()
        n1o = Af @ n1
        n2o = Af @ n2
        n1o[x1] = float(n1 @ n1)
        n2o[x2] = float(n2 @ n2)
        n1o[x2] = float(n1 @ n2)
        n2o[x1] = float(n1 @ n2)
        # dS over ordered pairs: rows x1,x2 (cols all) counted twice except 2x2 block
        def sq(v):
            return (v - 6.0) ** 2
        dS = 0.0
        for y in range(36):
            if y == x1 or y == x2:
                continue
            dS += sq(n1o[y]) - sq(o1[y]) + sq(n2o[y]) - sq(o2[y])
        dS *= 2.0
        for a2, oa, na in ((x1, o1, n1o), (x2, o2, n2o)):
            for b2, ob, nb in ((x1, o1, n1o), (x2, o2, n2o)):
                dS += sq(na[b2]) - sq(oa[b2])
        dE = dS / 2.0
        improve = (E + dE < bestE - 1e-9)
        if is_tabu and not improve:
            continue
        if dE <= 0 or rng.random() < np.exp(-dE / max(T, 1e-12)):
            A[x1, y1], A[x1, y2], A[x2, y1], A[x2, y2] = 1 - v11, v11, v11, 1 - v11
            Af[x1, y1], Af[x1, y2], Af[x2, y1], Af[x2, y2] = 1 - v11, v11, v11, 1 - v11
            G[x1, :] = n1o
            G[:, x1] = n1o
            G[x2, :] = n2o
            G[:, x2] = n2o
            E = E + dE
            tabu[key] = step + TEN
            if E < bestE - 1e-9:
                E = Efull(A)
                G = Af @ Af.T
                bestE, bestA = E, A.copy()
                print(f"[tabu {seed} step {step}] E={E} T={T:.5f} t={time.time()-t0:.0f}s",
                      flush=True)
                if E == 0:
                    break
        if (step + 1) % log == 0:
            print(f"[tabu {seed} step {step}] E={E:.1f} best={bestE} T={T:.5f}", flush=True)
    E = Efull(bestA)
    with open(out, "w") as f:
        json.dump({"R": R.tolist(), "seed": seed, "E": int(E), "A": bestA.tolist()}, f)
    print(f"[tabu {seed}] DONE bestE={E} t={time.time()-t0:.0f}s", flush=True)

if __name__ == "__main__":
    main()
