"""T1 plausibility scan for lane-20407 target K^24 M^36 >> N^13 over F_p.
Exact enumeration of sumset A+A and product set AA for interval,
geometric-progression (powers of 2), and random sets over F_101 and F_1009.
Run: python3 scan.py  (no dependencies beyond stdlib; deterministic seeds shown)
"""
import random

def stats(A, p):
    N = len(A)
    S = {(a + b) % p for a in A for b in A}
    P = {(a * b) % p for a in A for b in A}
    K = len(S) / N
    M = len(P) / N
    return K, M

def test(p, N, trials=2, seed=0):
    rng = random.Random(seed)
    print(f"p={p}")
    A = list(range(1, N + 1))
    K, M = stats(A, p)
    R = (K ** 24) * (M ** 36) / (N ** 13)
    print(f" interval N={N} K={K:.3f} M={M:.3f} R={R:.3e} p^24/49={p**(24/49):.1f}")
    A = sorted({pow(2, i, p) for i in range(N)})
    K, M = stats(A, p)
    R = (K ** 24) * (M ** 36) / (len(A) ** 13)
    print(f" GP N={len(A)} K={K:.3f} M={M:.3f} R={R:.3e}")
    for t in range(trials):
        A = rng.sample(range(1, p), N)
        K, M = stats(A, p)
        R = (K ** 24) * (M ** 36) / (N ** 13)
        print(f" rand N={N} K={K:.3f} M={M:.3f} R={R:.3e}")
    print()

if __name__ == "__main__":
    for p, N in [(101, 10), (101, 20), (1009, 30), (1009, 60)]:
        test(p, N, 2, seed=20407)
