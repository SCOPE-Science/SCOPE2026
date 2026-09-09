"""Analytic classification of balanced (g,k;p,b) types at chi=1 for g<=3 (§J).

No search ranges: bounds are DERIVED, then only finitely many integer cases.
Inputs: Euler chi = g-3k+3p+2b-1 (Castro-Ozbagci, cited in Takahashi);
Lemma-4.1 inequalities (Takahashi): 2p+b-1 <= k <= g+p+b-1,
0 <= p <= min((g+1-chi)/3, g), (2g-1+chi)/3 <= A <= g-p, A = g+p+b-1-k.

Derivation at chi=1: 3k = g+3p+2b-2. (*)
- g=0: p <= min(0/3,0)=0 -> p=0; (*) 3k=2b-2; k>=b-1 -> b<=1 -> (0,0,1),k=0.
- g=1: p <= min(1/3,1) -> p=0; (*) 3k=2b-1; k>=b-1 -> b<=2; 2b=1 mod 3 -> b=2,k=1.
- g=2: p <= min(2/3,2) -> p=0; (*) 3k=2b; k>=b-1 -> b<=3; 2b=0 mod 3 -> b=3,k=2.
- g=3: p <= min(3/3,3)=1 -> p in {0,1}; (*) 3k=3p+2b+1;
  k>=2p+b-1 -> 4 >= 3p+b (rearranged); k<=g+p+b-1 automatic (reduces to b>=-5);
  A = 2+p+b-k = (5+b)/3 (p cancels!); so 5+b = 0 mod 3 -> b = 1 mod 3.
  p=0: b<=4, b=1 mod 3 -> b in {1,4} -> (k,p,b)=(1,0,1),(3,0,4).
  p=1: b<=1, b=1 mod 3 -> b=1 -> (k,p,b)=(2,1,1).
  Exactly three types. A-values (5+b)/3: 2,2,3 -- all within Lemma-4.1 range.

Cross-check: independent brute-force scan over a WIDE box agrees (no stragglers).
"""
import json

def analytic():
    sols = {(0, 0, 0, 1), (1, 1, 0, 2), (2, 2, 0, 3),
            (3, 1, 0, 1), (3, 2, 1, 1), (3, 3, 0, 4)}  # (g,k,p,b)
    return sols

def brute(g_lo=0, g_hi=5, P=8, B=14, K=14):
    out = set()
    for g in range(g_lo, g_hi + 1):
        for p in range(0, P):
            for b in range(1, B):
                for k in range(0, K):
                    if not (2 * p + b - 1 <= k <= g + p + b - 1):
                        continue
                    if g - 3 * k + 3 * p + 2 * b - 1 != 1:
                        continue
                    A = g + p + b - 1 - k
                    import math
                    if not (0 <= p <= min((g + 1 - 1) / 3, g)):
                        continue
                    if not ((2 * g - 1 + 1) / 3 <= A <= g - p):
                        continue
                    if g <= 3:
                        out.add((g, k, p, b))
    return out

an = analytic()
br = brute()
agree = {t for t in br if t[0] <= 3} == an
# verify Euler + A for each analytic solution
checks = []
for (g, k, p, b) in sorted(an):
    A = g + p + b - 1 - k
    checks.append({"g": g, "k": k, "p": p, "b": b, "A": A,
                   "chi": g - 3 * k + 3 * p + 2 * b - 1})
out = {"analytic_solutions": sorted(an), "brute_agrees": agree,
       "euler_A_checks": checks,
       "g3_A_formula": "A=(5+b)/3",
       "ANALYTIC_CLASSIFICATION_OK": agree and all(c["chi"] == 1 for c in checks)}
print(json.dumps(out, indent=2))
assert agree
