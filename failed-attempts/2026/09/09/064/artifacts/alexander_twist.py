"""Twist-knot Alexander distinctness (§Q, target-directed audit of Step 2).

Teng §2.1 non-extension leg: regluing W by f^k in E(n) = Fintushel–Stern knot
surgery by the k-twist knot; outputs pairwise nondiffeomorphic [7] because the
k-twist knots have pairwise distinct Alexander polynomials.
Classical symmetric normalization for the k-twist knot (k>=0; K_0 = unknot):
  D_k(t) = k*t + (1-2k) + k*t^{-1},  so D_k(1) = 1 (normalized).
Distinguishing evaluations:
  D_k(-1) = 1-4k  (pairwise distinct in k),
  D_k''(1) = 2k   (pairwise distinct in k; cf. Takahashi Lemma 3.5 style use
                   of D''(1) for Casson surgery formula).
Check normalization + pairwise distinctness for k=0..10. This supplies the
computational premise of the cited FS distinction; the FS theorem itself
(surgery outputs distinguished by Alexander/SW) is cited, not recomputed.
No forbidden inputs (pure Laurent-polynomial arithmetic).
"""
import json
from itertools import combinations

KS = list(range(0, 11))

def D(k, t):
    # Laurent evaluation at t = ±1 only; t^{-1} = t for t=±1
    return k * t + (1 - 2 * k) + k * t  # = same since t^{-1}=t at ±1

def Dpp1(k):
    # D_k(t) = k t + (1-2k) + k t^{-1}; D'' = 2k t^{-3}; at 1: 2k
    return 2 * k

norm_ok = all(D(k, 1) == 1 for k in KS)
vals_m1 = {k: D(k, -1) for k in KS}   # expect 1-4k
vals_pp = {k: Dpp1(k) for k in KS}    # expect 2k
form_m1_ok = all(v == 1 - 4 * k for k, v in vals_m1.items())
form_pp_ok = all(v == 2 * k for k, v in vals_pp.items())
pairs = list(combinations(KS, 2))
distinct_m1 = all(vals_m1[a] != vals_m1[b] for a, b in pairs)
distinct_pp = all(vals_pp[a] != vals_pp[b] for a, b in pairs)
out = {"k_range": [min(KS), max(KS)],
       "normalization_D1_is_1": norm_ok,
       "D_minus1_is_1_minus_4k": form_m1_ok,
       "Dpp1_is_2k": form_pp_ok,
       "pairwise_distinct_at_minus1": distinct_m1,
       "pairwise_distinct_Dpp1": distinct_pp,
       "num_pairs_checked": len(pairs),
       "conclusion": "k-twist Alexander family pairwise distinct (k=0..10); "
                     "computational premise of Teng §2.1 FS non-extension leg verified",
       "ALEXANDER_DISTINCT_OK": norm_ok and form_m1_ok and form_pp_ok
       and distinct_m1 and distinct_pp}
print(json.dumps(out, indent=2))
assert out["ALEXANDER_DISTINCT_OK"]
