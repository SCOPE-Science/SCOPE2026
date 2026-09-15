"""Barrier certificate for naive slice/partition-rank attacks on 4-APs in F_5^n.

Checks (exact integer arithmetic except where noted):
 1. n=1: single-equation solutions vs true 4-APs (false-positive rate).
 2. Local distribution of (w-3x+3y-z) on A0={0,1,2}^4 and closed form
    sols(n) = (81^n + 4)/5 for A0^n via per-coordinate Fourier analysis.
 3. Monomial budgets M(<=n), M(<=2n) and the symmetry lemma
    M(<=2n) = (5^n + M(=2n))/2 > 5^n/2  =>  4*M(<=2n) > 2*5^n (all n).
 4. Brute force: {0,1,2}^2 has no 4 distinct-term AP (lower-bound anchor 3^n).
 5. Grid-search rate optima (single-eq base ~3.834; two-eq trivial).
"""
import itertools

P = 5

def monomial_counts(nvars):
    dp = {0: 1}
    for _ in range(nvars):
        ndp = {}
        for s, c in dp.items():
            for e in range(P):
                ndp[s + e] = ndp.get(s + e, 0) + c
        dp = ndp
    return dp

def M_leq(nvars, t):
    dp = monomial_counts(nvars)
    return sum(c for s, c in dp.items() if s <= t)

# ---- 1. n=1 single equation vs true APs ----
sols = [(w, x, y, z)
        for w, x, y, z in itertools.product(range(P), repeat=4)
        if (w - 3 * x + 3 * y - z) % P == 0]
aps = set()
for a in range(P):
    for d in range(P):
        aps.add((a % P, (a + d) % P, (a + 2 * d) % P, (a + 3 * d) % P))
false_pos = [t for t in sols if t not in aps]
print(f"[1] n=1: single-eq solutions={len(sols)}, true APs={len(aps)}, "
      f"false positives={len(false_pos)} ({len(false_pos)/len(sols):.1%})")

# ---- 2. local distribution on A0={0,1,2} + closed form ----
A0 = [0, 1, 2]
from collections import Counter
v = Counter((w - 3 * x + 3 * y - z) % P
            for w, x, y, z in itertools.product(A0, repeat=4))
print(f"[2] local distribution on A0^4: {dict(sorted(v.items()))} "
      f"(total {sum(v.values())} = 3^4)")
# Fourier check: nontrivial character sums = 17-16 = 1 -> sols(n) = (81^n+4)/5
dp = {0: 1}
for n in range(1, 9):
    ndp = {}
    for s, c in dp.items():
        for a, ca in v.items():
            ndp[(s + a) % P] = ndp.get((s + a) % P, 0) + c * ca
    dp = ndp
    closed = (81 ** n + 4) // 5
    assert dp[0] == closed, (n, dp[0], closed)
    print(f"    n={n}: sols(A0^n)={dp[0]} = (81^{n}+4)/5, |A0|^4={3**(4*n)}, "
          f"sols/|A0|={dp[0]/3**n:.1f} (factor 9^{n}/5={9**n/5:.1f})")

# ---- 3. monomial budgets + symmetry lemma ----
print("[3] slice budgets (single-eq 4M(<=n); two-eq 4M(<=2n)):")
for n in [1, 2, 3, 4, 6, 8, 10, 12]:
    m1 = M_leq(n, n)
    m2 = M_leq(n, 2 * n)
    tot = 5 ** n
    print(f"    n={n}: 4M(<=n)/5^n={4*m1/tot:.4f} "
          f"({'nontrivial' if 4*m1 < tot else 'TRIVIAL'}); "
          f"4M(<=2n)/5^n={4*m2/tot:.4f} "
          f"({'nontrivial' if 4*m2 < tot else 'TRIVIAL, symmetry: M>5^n/2'})")

# ---- 4. {0,1,2}^2 is 4-AP-free ----
pts = list(itertools.product(A0, A0))
S = set(pts)
bad = 0
for x in pts:
    for d in pts:
        if d == (0, 0):
            continue
        q = [((x[0] + k * d[0]) % P, (x[1] + k * d[1]) % P) for k in range(4)]
        if all(r in S for r in q) and len(set(q)) == 4:
            bad += 1
print(f"[4] distinct-4-APs in {{0,1,2}}^2: {bad} (|A|=9=3^2 -> r_4 >= 3^n)")

# ---- 5. rate optima by grid search ----
def best_base(exp):
    best = None
    x = 0.01
    while x < 1.0:
        f = (1 + x + x**2 + x**3 + x**4) / (x ** exp)
        if best is None or f < best[0]:
            best = (f, x)
        x += 0.0002
    return best[0] / 5, best[1]
b1, x1 = best_base(1)    # single-eq threshold n
b2, x2 = best_base(2)    # two-eq threshold 2n
b3, x3 = best_base(8/3)  # hypothetical 3-group degree-8n cert, threshold 8n/3
print(f"[5] optimal bases: single-eq M(<=n): {b1:.4f} (x={x1:.3f}, c1~{5*b1:.4f} "
      f"IF diagonal held); two-eq M(<=2n): {b2:.4f} (trivial, >=1); "
      f"3-group M(<=8n/3): {b3:.4f} (trivial, >=1)")
print("DONE")
