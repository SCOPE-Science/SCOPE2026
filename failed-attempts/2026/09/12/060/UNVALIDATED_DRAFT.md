# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# lane-1196 DRAFT — Conductor obstruction in the stated 11a1 model, with certified local data

## 1. What was attempted (target)
The admitted target asked for a base-layer Heegner 17-indivisibility certificate for
"E=11a1 over K=Q(sqrt(-19)) at p=17" with the explicit equation

    E_stated : y^2 + y = x^3 - x^2 - 10x + 20.

The required certificate was: (i) preliminary gate (p=17 good ordinary, primes
dividing the conductor split in K, mod-17 irreducibility with two Frobenius
witnesses), then (ii) a complete decision on the conductor-1 Heegner point y_K
(infinite order + 17-indivisibility via explicit point, height bound, mod-17 Kummer
class), or a rigorous disproof (torsion / 17-divisible / Sha[17] obstruction).

## 2. Blocking discovery (exact computation, reproducible)
For a model [a1,a2,a3,a4,a6] = [0,-1,1,-10,c], b2 = -4, b4 = -20, b6 = 81,
b8 = -181 - 80(c-20)/20... directly: with c = 20, b8 = -181 and

    Delta(E_stated) = -b2^2 b8 - 8 b4^3 - 27 b6^2 + 9 b2 b4 b6 = -51931 = -11 * 4721,

with 4721 prime (trial division to sqrt(4721) < 69 leaves no divisor) and
c4 = b2^2 - 24 b4 = 496 = 16 * 31, coprime to Delta. Hence E_stated is semistable
of conductor 51931 = 11 * 4721, NOT conductor 11. Its j-invariant is
-122023936/51931, not the 11a1 value. The sign-flipped model c = -20 instead gives
Delta = -161051 = -11^5, conductor 11, and traces a3 = -1, a7 = -2 matching the
LMFDB newform 11.2.a.a (signature of a single-sign typo +20/-20). The literal
model's traces a3 = 2, a7 = -1, a13 = 1 already differ from 11.2.a.a, confirming
E_stated is not in the 11a1 isogeny class. Consequently the "conductor-1 Heegner
point on X_0(11)" object of the target does not exist on the literal curve: its
Heegner parametrization would live on X_0(51931), whose Jacobian has dimension
> 1000, so the admitted X_0(11)-based route is structurally blocked, not merely
incomplete. A sign-corrected level-11 route would abandon the literal target and
still lacks the height + Kummer + division-polynomial certificate, so it cannot be
reported as a completed adjacent result either.

## 3. Certified local facts about the literal model (all machine-checked)
(a) Good ordinary at 17: brute-force count #E_stated(F_17) = 16, so a_17 = 2, and
    17 does not divide the conductor; a_17 mod 17 = 2 != 0.
(b) Splitting: (-19/11) = +1 (since -19 = 3 = 5^2 mod 11), (-19/17) = +1
    (since -19 = 15 = 7^2 mod 17). At literal level, (-19/4721) = +1 as well
    (-19 = 1 = 1^2 mod 4721), so the Heegner hypothesis would formally hold at
    level 51931 too.
(c) Mod-17 irreducibility with THREE independent witnesses (stronger than the two
    required): l = 7 (a = -1), l = 23 (a = 1), l = 31 (a = -7). For each, the trace
    is outside the split-Borel set {x + l/x : x in F_17^*} AND the discriminant
    a_l^2 - 4l mod 17 (7, 11, 10 respectively) is a non-residue mod 17
    (QR(17) = {1,2,4,8,9,13,15,16}). Each witness alone excludes both Borel types;
    irreducibility follows from any single one.
(d) Explicit infinite-order point: P = (0,4) lies on E_stated (16 + 4 = 20).
    #E(F_2) = 5 (prime) and #E(F_3) = 2, with good reduction at both (2,3 coprime
    to 51931). Reduction mod 2 sends P to a nonzero point of a group of order 5,
    so ord(P) is a multiple of 5; reduction mod 3 lands in a group of order 2
    whose kernel is a 3-group, so the prime-to-3 part of ord(P) divides 2 —
    contradiction with 5 | ord(P) unless ord(P) is infinite.
(e) Split-prime Kummer non-divisibility (aligned with the target's local-condition
    requirement): l = 83 satisfies (-19/83) = +1 (64 = 8^2 mod 83) and good
    reduction; #E_stated(F_83) = 85 = 5 * 17; Pbar = (0,4) has exact order 85
    (5P = (33,18) != O, 17P = (56,21) != O, 85P = O); |17E(F_83)| = 5 and
    Pbar is not in 17E(F_83). So the Kummer class of P is nonzero mod 83 — a local
    17-indivisibility certificate for the EXPLICIT point P (independent split-prime
    confirmations at l = 853, 881, 1013, 1151 show the same pattern).

## 4. What is NOT claimed
No complete Heegner-point (in)divisibility decision, no BSD or Sha(E/K)[17] claim,
no statement about the true 11a1 curve beyond the trace comparison used to diagnose
the typo, no anticyclotomic tower or mu-invariant consequence. The Heegner
identification step of the target was not completed for either model.

## 5. Reproduction
Run (pure Python 3 stdlib, exact integer arithmetic; sympy used only for prime
enumeration in one supplement, cross-checked by brute force):
  python3 output/artifacts/lane1196_target_audit.py
  python3 output/artifacts/lane1196_kummer_irred.py
Both scripts print every number quoted above. All counts are brute-force point
enumerations; all group operations use the explicit [0,-1,1,-10,20] chord-and-tangent
formulas; Kronecker values are witnessed by explicit square roots.
