"""Bounded recovery scan for target: conditional sum growth at exponent 81/50.
Reproduces the WORKLOG evidence: subgroup ratios |H+H|/|H|^1.62 and random search.
Run: python3 recovery_scan.py (requires sympy). Prints min subgroup ratio and random-search hits.
"""
import math, random

def prim_root(p):
    n = p - 1
    f, m, d = {}, n, 2
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1
            m //= d
        d += 1 if d == 2 else 2
    if m > 1:
        f[m] = 1
    for g in range(2, p):
        if all(pow(g, n // q, p) != 1 for q in f):
            return g
    return None

def subgroup(p, d):
    g = prim_root(p)
    step = (p - 1) // d
    return set(pow(g, step * i, p) for i in range(d))

def sumset_size(H, p):
    H = list(H)
    S = set()
    for i, a in enumerate(H):
        for b in H[i:]:
            S.add((a + b) % p)
    return len(S)

def sizes(A, p):
    A = list(A)
    P = len(set((a * b) % p for a in A for b in A))
    S = len(set((a + b) % p for a in A for b in A))
    return P, S

def main():
    import sympy as sp
    E = 81 / 50
    worst = []
    for p in sp.primerange(7, 2000):
        n = p - 1
        for d in range(3, int(p ** 0.5)):
            if n % d == 0:
                H = subgroup(p, d)
                s = sumset_size(H, p)
                worst.append((s / (d ** E), p, d, s))
    worst.sort()
    print("subgroup cases:", len(worst))
    print("min ratio:", ["p=%d d=%d S=%d r=%.4f" % (p, d, s, r) for r, p, d, s in worst[:3]])
    random.seed(12345)
    p = 1009
    hits = 0
    trials = 0
    for nn in [8, 12, 16, 20]:
        for _ in range(3000):
            A = random.sample(range(p), nn)
            P, S = sizes(A, p)
            trials += 1
            if P <= 3 * nn:
                hits += 1
                print("low-M set: n=%d M=%.2f S=%d ratio=%.3f" % (nn, P / nn, S, S / (nn ** E)))
    print("random trials %d, low-M hits %d" % (trials, hits))

if __name__ == "__main__":
    main()
