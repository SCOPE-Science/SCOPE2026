"""Basin-hopping driver: iterated kick + full tabu polish, keeps global best.
Designed to escape the E~300 attractor: kicks of increasing strength, long polish.
Usage: python3 basin.py RJSON SEED ROUNDS OUT [KICK]"""
import numpy as np
import sys
import json
import math
import time

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

def kick(A, rng, nsw):
    B = A.copy()
    done = 0
    guard = 0
    while done < nsw and guard < 50000:
        guard += 1
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
        v11 = int(B[x1, y1])
        if v11 == int(B[x2, y2]) or int(B[x1, y2]) == int(B[x2, y1]) or v11 == int(B[x1, y2]):
            continue
        B[x1, y1], B[x1, y2], B[x2, y1], B[x2, y2] = 1 - v11, v11, v11, 1 - v11
        done += 1
    return B

def polish(A, rng, steps, T0=0.9, T1=1e-4):
    A = A.copy()
    G = A @ A.T
    E = (int(((G - 6) ** 2).sum()) - 36 * 81) // 2
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
            E = E2
        else:
            A[x1, y1], A[x1, y2], A[x2, y1], A[x2, y2] = v11, 1 - v11, 1 - v11, v11
    return A, E

def main():
    R = np.array(json.loads(sys.argv[1]), dtype=np.int64)
    seed = int(sys.argv[2])
    rounds = int(sys.argv[3])
    out = sys.argv[4]
    KICK = int(sys.argv[5]) if len(sys.argv) > 5 else 60
    rng = np.random.default_rng(seed)
    A = np.zeros((36, 36), dtype=np.int64)
    for i in range(4):
        for j in range(4):
            A[i * 9:(i + 1) * 9, j * 9:(j + 1) * 9] = rand_regular(int(R[i, j]), rng)
    bestA, bestE = polish(A, rng, 120000)
    print(f"[basin {seed}] E0={bestE}", flush=True)
    t0 = time.time()
    for rd in range(rounds):
        C = kick(bestA, rng, KICK)
        C, E = polish(C, rng, 120000)
        if E < bestE:
            bestE, bestA = E, C.copy()
            print(f"[basin {seed} rd {rd}] NEW BEST E={E} t={time.time()-t0:.0f}s", flush=True)
            if E == 0:
                break
        elif rd % 5 == 0:
            print(f"[basin {seed} rd {rd}] E={E} best={bestE} t={time.time()-t0:.0f}s", flush=True)
    with open(out, "w") as f:
        json.dump({"R": R.tolist(), "seed": seed, "E": int(bestE), "A": bestA.tolist()}, f)
    print(f"[basin {seed}] DONE bestE={bestE} t={time.time()-t0:.0f}s", flush=True)

if __name__ == "__main__":
    main()
