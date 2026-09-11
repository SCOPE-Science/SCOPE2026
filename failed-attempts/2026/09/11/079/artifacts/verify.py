"""Lane-896 verification: disproof of the dilated Capparelli companion + mod-7 family.

Stdlib only. Replays:
  D(n) by memoized recursion AND independent iterative DP AND brute-force subsets (n<=10).
  P(n) = (-q;q)_oo (q^12;q^12)/((q^2;q^12)(q^10;q^12)) by two independent expansions.
  Product comparison, prefactor-rescue checks, mod-7 census (all residues fail, m<=8).
Exit banner: VERIFY_OK on success, else raises AssertionError.
"""
from functools import lru_cache
from itertools import combinations

N = 150

# ---- Method A: memoized recursion for D(n) ----
@lru_cache(maxsize=None)
def G(rem, L):
    if rem == 0:
        return 1
    if L == 0:
        bound = rem
    else:
        bound = L - 4 if L % 2 == 0 else L - 2
        bound = min(bound, rem)
    return sum(G(rem - k, k) for k in range(2, bound + 1))

DA = [G(n, 0) for n in range(N + 1)]

# ---- Method B: independent iterative DP ----
G2 = [[0] * (N + 1) for _ in range(N + 1)]
for L in range(N + 1):
    G2[0][L] = 1
for rem in range(1, N + 1):
    for L in range(N, -1, -1):
        bound = rem if L == 0 else min((L - 4 if L % 2 == 0 else L - 2), rem)
        s = 0
        for k in range(2, bound + 1):
            s += G2[rem - k][k]
        G2[rem][L] = s
DB = [G2[n][0] for n in range(N + 1)]
assert DA == DB, "dual-DP mismatch"
D = DA

# ---- Method C: brute-force subset enumeration, n<=10 ----
def D_brute(n):
    if n == 0:
        return 1
    count = 0
    parts = list(range(2, n + 1))
    for r in range(1, len(parts) + 1):
        for combo in combinations(parts, r):
            if sum(combo) != n:
                continue
            s = sorted(combo, reverse=True)
            ok = True
            for i in range(len(s) - 1):
                need = 4 if s[i] % 2 == 0 else 2
                if s[i] - s[i + 1] < need:
                    ok = False
                    break
            if ok:
                count += 1
    return count

for n in range(11):
    assert D_brute(n) == D[n], f"brute mismatch at {n}"
assert D[:9] == [1, 0, 1, 1, 1, 1, 1, 2, 3], D[:9]

# ---- Product method 1: incremental factor multiplication ----
def mul(a, b):
    c = [0] * (N + 1)
    for i, ai in enumerate(a):
        if ai:
            for j in range(N + 1 - i):
                if b[j]:
                    c[i + j] += ai * b[j]
    return c

A = [1] + [0] * N
for k in range(1, N + 1):
    nA = A[:]
    for i in range(N + 1 - k):
        nA[i + k] += A[i]
    A = nA
P1 = A[:]
k = 1
while 12 * k <= N:
    m = 12 * k
    nP = P1[:]
    for i in range(N + 1 - m):
        nP[i + m] -= P1[i]
    P1 = nP
    k += 1
k = 0
while True:
    ms = [m for m in (12 * k + 2, 12 * k + 10) if m <= N]
    if not ms and 12 * k + 2 > N:
        break
    for m in ms:  # multiply by 1/(1-q^m): prefix sums
        for i in range(m, N + 1):
            P1[i] += P1[i - m]
    k += 1

# ---- Product method 2: divisor-sum/log-exp-free direct convolution ----
# Build numerator/denominator polynomials independently, then series divide.
num = [1] + [0] * N
for k in range(1, N + 1):  # (1+q^k)
    for i in range(N - k, -1, -1):
        num[i + k] += num[i]
    if False:
        pass
# NOTE: num currently = prod(1+q^k); fold in prod(1-q^{12k}) separately
numB = [1] + [0] * N
j = 1
while 12 * j <= N:
    m = 12 * j
    for i in range(N - m, -1, -1):
        numB[i + m] -= numB[i]
    j += 1
num = mul(num, numB)
den = [1] + [0] * N
j = 0
while True:
    ms = [m for m in (12 * j + 2, 12 * j + 10) if m <= N]
    if not ms and 12 * j + 2 > N:
        break
    for m in ms:
        nD = den[:]
        for i in range(N + 1 - m):
            nD[i + m] -= den[i]
        den = nD
    j += 1
P2 = [0] * (N + 1)
for n in range(N + 1):
    s = num[n] - sum(den[k] * P2[n - k] for k in range(1, n + 1))
    P2[n] = s
assert P1 == P2, "dual-product mismatch"
P = P1
assert P[:9] == [1, 1, 2, 3, 4, 6, 8, 11, 14], P[:9]

# ---- Product leg: disproof at first coefficient ----
assert D[0] == P[0] == 1, "constant terms must agree (rules out q^c prefactor)"
assert (D[1], P[1]) == (0, 1), "expected first-coefficient mismatch"
# P1=1 analytically: (-q;q)_oo = 1+q+O(q^2); mod-12 factors = 1+O(q^2).
# Prefactor rescues:
Q1 = P[:]  # P*(1-q)
for i in range(N - 1, -1, -1):
    Q1[i + 1] -= P[i]
assert Q1[:5] == D[:5] and Q1[5] != D[5], "P(1-q) rescue must fail at n=5"
Q2 = [0] * (N + 1)  # P/(1+q): (1+q)Q=P
Q2[0] = P[0]
for i in range(1, N + 1):
    Q2[i] = P[i] - Q2[i - 1]
assert Q2[2] != D[2], "P/(1+q) rescue must fail at n=2"
R = [0] * (N + 1)  # R = D/P series
for n in range(N + 1):
    R[n] = D[n] - sum(P[k] * R[n - k] for k in range(1, n + 1))
assert sum(1 for x in R if x != 0) > N // 2, "ratio must be dense nonzero"

# ---- Mod-7 leg: disproof + full residue census ----
assert D[3] == 1 and D[3] % 7 != 0, "minimal mod-7 failure at m=3"
expected_witness = {0: 0, 1: 8, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
for r in range(7):
    m = None
    for cand in range(r, N + 1, 7):
        if D[cand] % 7 != 0:
            m = cand
            break
    assert m == expected_witness[r], f"residue {r}: witness {m}, expected {expected_witness[r]}"
# D(8)=3 by hand: [8],[6,2] (even gap 4),[5,3] (odd gap 2) -> 3 != 0 mod 7.

print("D[:12] =", D[:12])
print("P[:12] =", P[:12])
print("product first mismatch: n=1, D=0 vs P=1")
print("mod-7 minimal failure: m=3, D(3)=1")
print("residue witnesses:", expected_witness)
print("VERIFY_OK")
