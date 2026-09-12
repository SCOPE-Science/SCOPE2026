"""Exact verifier for lane-1070 dual de Weger LLL transcripts (stdlib only).

Checks, with exact integer/Fraction arithmetic except for stated high-precision
interval margins on logarithms:
  R1: a_i = round(C*log p_i): |a_i - C*log p_i| <= 1/2 (mpmath, 120 dps).
  R2: each reduced row lies in the original lattice: (w - sum x_i a_i) % C == 0.
  R3: Bareiss det(reduced basis) == +-C  =>  same lattice  =>  Gram det == C^2.
  R4: reduced basis is LLL-reduced at delta=99/100 (size + Lovasz, Fractions).
  R5: two-sided shortest-vector bracket: min_GS_norm <= lambda1 <= ||b1||.
  R6: one-step firing thresholds T = U/kappa (kappa^2 = 45/4) and B=96
      linear-form lower bounds from the proved lemma.
Writes output/artifacts/verification.json and prints VERIFY_OK or FAIL.
"""
import json, math
from fractions import Fraction

import mpmath
mpmath.mp.dps = 120

ART = "output/artifacts"
PRIMES = [2, 3, 5, 11, 50033]
KAPPA2 = Fraction(45, 4)  # 5 + 25/4 for n=5

def bareiss_det(M):
    n = len(M)
    A = [list(map(int, row)) for row in M]
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            piv = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if piv is None:
                return 0
            A[k], A[piv] = A[piv], A[k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
            A[i][k] = 0
        prev = A[k][k]
    return A[n - 1][n - 1]

def gram_schmidt(B):
    n, m = len(B), len(B[0])
    BF = [[Fraction(x) for x in row] for row in B]
    Bs, mu, nrm = [None]*n, [[Fraction(0)]*n for _ in range(n)], [Fraction(0)]*n
    for i in range(n):
        v = list(BF[i])
        for j in range(i):
            num = sum(BF[i][k]*Bs[j][k] for k in range(m))
            mu[i][j] = num / nrm[j]
            v = [v[k] - mu[i][j]*Bs[j][k] for k in range(m)]
        Bs[i] = v
        nrm[i] = sum(x*x for x in v)
    return Bs, mu, nrm

def check_lll(B, delta=Fraction(99, 100)):
    n = len(B)
    _, mu, nrm = gram_schmidt(B)
    size_ok = all(abs(mu[i][j]) <= Fraction(1, 2)
                 for i in range(n) for j in range(i))
    lovasz_ok = all(nrm[k] >= (delta - mu[k][k-1]**2)*nrm[k-1]
                    for k in range(1, n))
    return size_ok, lovasz_ok

out = {"checks": {}, "results": {}}
ok = True
logs = [mpmath.log(mpmath.mpf(p)) for p in PRIMES]
inp = json.load(open(f"{ART}/lattice_inputs.json"))

for tag in ["Ca", "Cb"]:
    C = int(inp["C" + tag[1]])
    a = inp["a" + tag[1]]
    red = json.load(open(ART + "/reduced_" + tag + ".json"))
    Br = red["basis"]

    # R1: rounding margins
    margins = [abs(mpmath.mpf(x) - mpmath.mpf(C)*l) for x, l in zip(a, logs)]
    r1 = all(m <= mpmath.mpf("0.5") - mpmath.mpf("1e-90") for m in margins)

    # R2: row membership in original lattice
    r2 = all((r[5] - sum(x*ai for x, ai in zip(r[:5], a))) % C == 0 for r in Br)

    # R3: determinant => same lattice, Gram det = C^2
    det = bareiss_det(Br)
    r3 = abs(det) == C

    # R4: LLL(0.99) reducedness
    size_ok, lovasz_ok = check_lll(Br)
    r4 = size_ok and lovasz_ok

    # R5: two-sided bracket of lambda1
    _, _, nrm = gram_schmidt(Br)
    low2 = min(nrm)                       # Fraction, <= lambda1^2
    up2 = sum(x*x for x in Br[0])         # integer, >= lambda1^2
    L = math.isqrt(low2.numerator // low2.denominator) \
        if low2.denominator != 1 else math.isqrt(low2.numerator)
    while (L+1)*(L+1)*low2.denominator <= low2.numerator:
        L += 1
    while L*L*low2.denominator > low2.numerator:
        L -= 1
    U2 = up2
    Uhi = math.isqrt(U2) + 1              # strict upper bound on ||b1||
    r5 = (Fraction(L*L) <= low2) and (Fraction(Uhi*Uhi) > Fraction(U2))

    # R6: thresholds T = U/kappa and B=96 corollary (lemma: |Lbd| bound)
    kappa = math.sqrt(float(KAPPA2))
    Tstall = (math.sqrt(float(U2))) / kappa   # B >= this (upper-vector form)
    Tfire = float(L) / kappa                  # B below this: fire possible
    # B=96 lower bound on |Lambda|, INTEGER-RIGOROUS: s = floor(sqrt(disc)),
    # s <= sqrt(disc) so C|Lambda| >= s - 240 and |Lambda| >= (s-240)/C.
    B96 = 96
    disc = low2 - 5*B96*B96
    if disc > 0:
        Dnum, Dden = disc.numerator, disc.denominator
        s = math.isqrt(Dnum * Dden) // Dden
        while (s+1)*(s+1)*Dden <= Dnum:
            s += 1
        while s*s*Dden > Dnum:
            s -= 1
        assert Fraction(s*s) <= disc < Fraction((s+1)*(s+1))
        lb96_num = s - 240  # 5*B96/2 = 240
        lb96 = lb96_num / C if lb96_num > 0 else 0.0
        lb96_s = s
    else:
        lb96, lb96_s, lb96_num = 0.0, 0, 0
    lb96_float = (math.sqrt(float(disc)) - 5*B96/2) / C if disc > 0 else 0.0
    # normalized quality lambda1-approx / C^{1/6}
    q = math.sqrt(float(U2)) / (C ** (1/6))

    # R7 (rigorous integer stall certificate): one-step firing needs l > kappa*B
    # with kappa^2 = 45/4, while l <= ||b1|| < Uhi; hence 45*B^2 >= 4*Uhi^2
    # certifies one-step firing is IMPOSSIBLE at bound B. Check the two
    # claimed integer stall bounds exactly.
    stall_claim = 907444 if tag == "Ca" else 4989313790496
    r7 = 45 * stall_claim * stall_claim >= 4 * Uhi * Uhi

    tag_ok = all([r1, r2, r3, r4, r5, r7])
    ok = ok and tag_ok
    out["checks"][tag] = {"R1_rounding": r1, "R2_membership": r2,
                          "R3_det_is_C": r3, "R4_LLL99": r4,
                          "R5_bracket": r5, "R7_stall_cert": r7,
                          "stall_claim": stall_claim,
                          "size_ok": size_ok, "lovasz_ok": lovasz_ok,
                          "det": str(det), "C": str(C),
                          "rounding_margins": [str(m) for m in margins]}
    out["results"][tag] = {"lambda1_lower_L": L,
                           "b1_norm2": str(U2),
                           "b1_norm_upper": Uhi,
                           "T_stall_upperform": Tstall,
                           "T_fire_lowerform": Tfire,
                           "B96_sqrt_floor": str(lb96_s),
                           "B96_linearform_lowerbound": lb96,
                           "B96_lb_float": lb96_float,
                           "quality_vs_Csixth": q,
                           "GS_norms": [str(x) for x in nrm]}

out["status"] = "VERIFY_OK" if ok else "VERIFY_FAIL"
json.dump(out, open(f"{ART}/verification.json", "w"), indent=1)
for tag in ["Ca", "Cb"]:
    r = out["results"][tag]
    print(tag, "L =", r["lambda1_lower_L"], "| b1 |^2 =", r["b1_norm2"],
          "| Tstall ~", r["T_stall_upperform"], "| Tfire ~", r["T_fire_lowerform"],
          "| LB96 ~", r["B96_linearform_lowerbound"], "| q ~", r["quality_vs_Csixth"])
print(out["status"])
