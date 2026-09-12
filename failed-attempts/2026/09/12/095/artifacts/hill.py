"""Hill-climb driver: iterated local search on the fixed-margin refinement landscape.
Each round: short SA burst from current best (low T), keep improvements; perturb on stall.
Usage: python3 hill.py RJSON SEED ROUNDS BURST OUT [T0]"""
import numpy as np
import sys
import json
import math
import time
import subprocess

def Efull(A):
    G = A @ A.T
    return (int(((G - 6) ** 2).sum()) - 36 * 81) // 2

def burst(A, R, rng, steps, T0, T1):
    A = A.copy()
    E, _ = Efull(A), None
    G = A @ A.T
    for step in range(steps):
        T = T0 * (T1 / T0) ** (step / steps)
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
        A[x1, y1], A[x1, y2], A[x2, y1], A[x2, y2] = 1 - v11, v11, v11, 1 - v11
        G2 = A @ A.T
        E2 = (int(((G2 - 6) ** 2).sum()) - 36 * 81) // 2
        dE = E2 - E
        if dE <= 0 or rng.random() < math.exp(-dE / T):
            E, G = E2, G2
        else:
            A[x1, y1], A[x1, y2], A[x2, y1], A[x2, y2] = v11, 1 - v11, 1 - v11, v11
    return A, E

def perturb(A, rng, nswaps=400):
    A = A.copy()
    for _ in range(nswaps):
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
        A[x1, y1], A[x1, y2], A[x2, y1], A[x2, y2] = 1 - v11, v11, v11, 1 - v11
    return A

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
    rounds = int(sys.argv[3])
    burstlen = int(sys.argv[4])
    out = sys.argv[5]
    T0 = float(sys.argv[6]) if len(sys.argv) > 6 else 0.6
    rng = np.random.default_rng(seed)
    A = np.zeros((36, 36), dtype=np.int64)
    for i in range(4):
        for j in range(4):
            A[i * 9:(i + 1) * 9, j * 9:(j + 1) * 9] = rand_regular(int(R[i, j]), rng)
    bestE = Efull(A)
    bestA = A.copy()
    print(f"[hill {seed}] E0={bestE}", flush=True)
    t0 = time.time()
    stall = 0
    for rd in range(rounds):
        B, E = burst(bestA if stall < 3 else perturb(bestA, rng), R, rng, burstlen, T0, 1e-5)
        if E < bestE:
            bestE, bestA = E, B.copy()
            stall = 0
            print(f"[hill {seed} rd {rd}] NEW BEST E={E} t={time.time()-t0:.0f}s", flush=True)
            if E == 0:
                break
        else:
            stall += 1
            if rd % 10 == 0:
                print(f"[hill {seed} rd {rd}] E={E} best={bestE} stall={stall}", flush=True)
    with open(out, "w") as f:
        json.dump({"R": R.tolist(), "seed": seed, "E": int(bestE), "A": bestA.tolist()}, f)
    print(f"[hill {seed}] DONE bestE={bestE} t={time.time()-t0:.0f}s", flush=True)

if __name__ == "__main__":
    main()
