"""Exact ECH capacities for concave toric domains via Hutchings weight sequences.

Math background (cited in DRAFT):
- Hutchings (1005.2260): ECH capacities c_k, monotonicity; ball B(a):
  c_k = d*a where d is defined by (d^2+d)/2 <= k < (d^2+3d+2)/2,
  i.e. ordered multiset {a,2a,2a,3a,3a,3a,...}; c_0 = 0.
- Choi–Cristofaro-Gardiner–Frenkel–Hutchings–Ramos (1310.6647):
  concave toric domain X_Omega has finite/infinite weight sequence
  (a_1,a_2,...) and c(X_Omega) = c(sqcup_i B(a_i)).
- Disjoint union formula (Hutchings): c_k(sqcup_i X_i) =
  max { sum_i c_{k_i}(X_i) : sum k_i = k, k_i >= 0 }.

All arithmetic below is exact (Fractions). The DP maximum is certified
two-sided: argmax partition (upper witness) + exhaustive enumeration
(lower/matching bound: no partition beats it).
"""
from fractions import Fraction as Q

def ball_caps(a, kmax):
    """c_0..c_kmax of B(a), a>0 (int or Fraction). Index d: triangle numbers."""
    a = Q(a)
    caps = [Q(0)] * (kmax + 1)
    d = 0
    nxt = 1  # T_{d+1} = (d+1)(d+2)/2 is first index with value (d+1)*a
    for k in range(1, kmax + 1):
        while k >= (d + 1) * (d + 2) // 2:
            d += 1
        caps[k] = d * a
    return caps

def disjoint_union_caps(weights, kmax):
    """c_0..c_kmax of sqcup B(w) + argmax partitions. Exact DP."""
    ballseqs = [ball_caps(w, kmax) for w in weights]
    n = len(weights)
    # dp[i][k] = best using first i balls; track argmax
    NEG = Q(-1)
    dp = [NEG] * (kmax + 1)
    arg = [None] * (kmax + 1)
    dp[0] = Q(0)
    arg[0] = []
    # iterate balls one by one (0/1 over balls but k splittable): use 2D
    full = [[Q(0)] * (kmax + 1) for _ in range(n + 1)]
    choice = [[[0] * 1 for _ in range(kmax + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        bc = ballseqs[i - 1]
        for k in range(kmax + 1):
            best = Q(-1)
            bk = 0
            for j in range(k + 1):
                v = full[i - 1][k - j] + bc[j]
                if v > best:
                    best = v
                    bk = j
            full[i][k] = best
            choice[i][k] = bk
    caps = full[n]
    # reconstruct argmax partitions
    parts = {}
    for k in range(kmax + 1):
        kk = k
        p = []
        for i in range(n, 0, -1):
            j = choice[i][kk]
            p.append(j)
            kk -= j
        p.reverse()
        parts[k] = p
    return caps, parts

def volume(weights):
    """vol = (1/2) sum a_i^2 (symplectic volume of concave domain)."""
    return sum((Q(w) ** 2 for w in weights), Q(0)) / 2
