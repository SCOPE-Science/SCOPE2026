"""SA refinement search: 36x36 binary matrix with fixed 9x9 tile margins R,
row-pair energy E = sum_{x<y} (inner(x,y)-6)^2. E=0 (+fixed margins) = symmetric 2-(36,15,6).
Usage: python3 refine.py RJSON SEED ITERS T0 T1 OUT
RJSON: e.g. '[[6,3,3,3],[3,6,3,3],[3,3,6,3],[3,3,3,6]]'"""
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
    for a in range(9):
        M[a, [(a + int(d)) % 9 for d in S]] = 1
    M = M[rng.permutation(9)][:, rng.permutation(9)]
    return M

def energy(A):
    G = A @ A.T
    tot = int(((G - 6) ** 2).sum())
    return (tot - 36 * 81) // 2, G

def main():
    R = np.array(json.loads(sys.argv[1]), dtype=np.int64)
    seed = int(sys.argv[2])
    iters = int(sys.argv[3])
    T0 = float(sys.argv[4]) if len(sys.argv) > 4 else 3.0
    T1 = float(sys.argv[5]) if len(sys.argv) > 5 else 1e-4
    out = sys.argv[6] if len(sys.argv) > 6 else "output/artifacts/refined.json"
    rng = np.random.default_rng(seed)
    A = np.zeros((36, 36), dtype=np.int64)
    for i in range(4):
        for j in range(4):
            A[i * 9:(i + 1) * 9, j * 9:(j + 1) * 9] = rand_regular(int(R[i, j]), rng)
    E, _ = energy(A)
    bestE = E
    bestA = A.copy()
    print(f"[seed {seed}] E0={E}", flush=True)
    t_start = time.time()
    log = max(1, iters // 40)
    for step in range(iters):
        T = T0 * (T1 / T0) ** (step / iters)
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
        v11 = A[x1, y1]
        if v11 == A[x2, y2] or A[x1, y2] == A[x2, y1] or v11 == A[x1, y2]:
            continue
        # switchable: [[1,0],[0,1]] <-> [[0,1],[1,0]]
        A[x1, y1], A[x1, y2], A[x2, y1], A[x2, y2] = 1 - v11, v11, v11, 1 - v11
        E2, _ = energy(A)
        dE = E2 - E
        if dE <= 0 or rng.random() < math.exp(-dE / T):
            E = E2
            if E < bestE:
                bestE = E
                bestA = A.copy()
                print(f"[seed {seed} step {step}] E={E} T={T:.5f} t={time.time()-t_start:.0f}s",
                      flush=True)
                if E == 0:
                    break
        else:
            A[x1, y1], A[x1, y2], A[x2, y1], A[x2, y2] = v11, 1 - v11, 1 - v11, v11
        if (step + 1) % log == 0:
            print(f"[seed {seed} step {step}] E={E} best={bestE} T={T:.5f}", flush=True)
    with open(out, "w") as f:
        json.dump({"R": R.tolist(), "seed": seed, "E": int(bestE), "A": bestA.tolist()}, f)
    print(f"[seed {seed}] DONE bestE={bestE} t={time.time()-t_start:.0f}s", flush=True)

if __name__ == "__main__":
    main()
