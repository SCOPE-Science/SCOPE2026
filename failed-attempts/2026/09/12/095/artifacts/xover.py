"""Crossover (genetic) driver for fixed-margin refinement.
Representation: per point-class row, permutation of column indices within each tile class.
seedA/seedB: parent JSONs (same R). Child: per row, take each tile's column-set from
a random parent (uniform crossover per (row,tile)), then repair by random switches.
Then short tabu/SA polish. Repeat generations, keep elite.
Usage: python3 xover.py RJSON PA_JSON PB_JSON SEED GENS POLISH OUT"""
import numpy as np
import sys
import json
import math
import time

def Efull(A):
    G = A @ A.T
    return (int(((G - 6) ** 2).sum()) - 36 * 81) // 2

def polish(A, rng, steps, T0=0.35, T1=1e-4):
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

def crossover(A, B, R, rng):
    C = np.zeros((36, 36), dtype=np.int64)
    for i in range(4):
        for x in range(9):
            r = i * 9 + x
            for j in range(4):
                cols = list(range(j * 9, (j + 1) * 9))
                P = A[r, cols].copy() if rng.random() < 0.5 else B[r, cols].copy()
                # repair popcount to R[i,j]
                need = int(R[i, j]) - int(P.sum())
                if need > 0:
                    z = [c for c in range(9) if P[c] == 0]
                    rng.shuffle(z)
                    for c in z[:need]:
                        P[c] = 1
                elif need < 0:
                    o = [c for c in range(9) if P[c] == 1]
                    rng.shuffle(o)
                    for c in o[:-need]:
                        P[c] = 0
                C[r, cols] = P
    return C

def main():
    R = np.array(json.loads(sys.argv[1]), dtype=np.int64)
    PA = np.array(json.load(open(sys.argv[2]))["A"], dtype=np.int64)
    PB = np.array(json.load(open(sys.argv[3]))["A"], dtype=np.int64)
    seed = int(sys.argv[4])
    gens = int(sys.argv[5])
    pol = int(sys.argv[6])
    out = sys.argv[7]
    rng = np.random.default_rng(seed)
    pop = [PA, PB]
    Epop = [Efull(P) for P in pop]
    print(f"[xover {seed}] E0={[int(e) for e in Epop]}", flush=True)
    t0 = time.time()
    for g in range(gens):
        C = crossover(pop[0], pop[1], R, rng)
        C, E = polish(C, rng, pol)
        # keep two best among pop + child (+ mutated best)
        cand = pop + [C]
        Ec = Epop + [E]
        idx = sorted(range(len(cand)), key=lambda k: Ec[k])[:2]
        pop = [cand[k] for k in idx]
        Epop = [Ec[k] for k in idx]
        # inject diversity: mutated copy of best
        if g % 3 == 2:
            M = pop[1].copy()
            for _ in range(300):
                ti = int(rng.integers(4))
                tj = int(rng.integers(4))
                a = int(rng.integers(9))
                b = int(rng.integers(9))
                c = int(rng.integers(9))
                d = int(rng.integers(9))
                if b == a or d == c:
                    continue
                x1, x2 = ti * 9 + a, ti * 9 + b
                y1, y2 = tj * 9 + c, tj * 9 + d
                v11 = int(M[x1, y1])
                if v11 == int(M[x2, y2]) or int(M[x1, y2]) == int(M[x2, y1]) or v11 == int(M[x1, y2]):
                    continue
                M[x1, y1], M[x1, y2], M[x2, y1], M[x2, y2] = 1 - v11, v11, v11, 1 - v11
            M, Em = polish(M, rng, pol // 2)
            if Em < max(Epop):
                pop[1], Epop[1] = M, Em
        print(f"[xover {seed} g {g}] best={int(min(Epop))} pop={[int(e) for e in Epop]} t={time.time()-t0:.0f}s",
              flush=True)
        if min(Epop) == 0:
            break
    b = int(np.argmin(Epop))
    with open(out, "w") as f:
        json.dump({"R": R.tolist(), "seed": seed, "E": int(Epop[b]), "A": pop[b].tolist()}, f)
    print(f"[xover {seed}] DONE bestE={int(Epop[b])} t={time.time()-t0:.0f}s", flush=True)

if __name__ == "__main__":
    main()
