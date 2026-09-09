# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Cheap distinct coverings with minimum modulus 7 inside LCM 10080:
# a certified irredundant 65-class witness and the interval C* in [14, 65]

## Abstract
Let L0 = 10080 and D = {d : d | 10080, d >= 7} (|D| = 66). Let C* be the least
number of congruences in a distinct-modulus covering of Z with all moduli in D
and minimum modulus exactly 7. We prove 14 <= C* <= 65. The lower bound is an
exact reciprocal-sum certificate. The upper bound is a new explicit irredundant
65-class witness (all moduli in D, min 7, LCM exactly 10080) covering all 10080
residues, obtained by deleting one redundant class from the published 66-class
system of Zhang et al. and machine-verified residue by residue. Every one of
the 65 classes owns a private residue. C* is not closed here; the interval is
the certified partial result.

## 1. Setup
A finite family {(a_i mod m_i)} with distinct m_i covers Z iff it covers every
residue mod L = lcm(m_i). Fix L0 = 10080, the minimal LCM for minimum modulus 7
(Zhang et al., arXiv:2607.19029, Theorem 1). Every modulus below divides L0, so
an exact covering check over Z_10080 is valid. D has 66 elements:

7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 28, 30, 32, 35, 36, 40, 42, 45,
48, 56, 60, 63, 70, 72, 80, 84, 90, 96, 105, 112, 120, 126, 140, 144, 160,
168, 180, 210, 224, 240, 252, 280, 288, 315, 336, 360, 420, 480, 504, 560,
630, 672, 720, 840, 1008, 1120, 1260, 1440, 1680, 2016, 2520, 3360, 5040, 10080.

## 2. Theorem (partial)
C* in [14, 65].

### 2.1 Lower bound C* >= 14 (proof)
A family of k distinct moduli covers at most sum 1/m_i of residues (density),
with strict inequality sum > 1 necessary for a distinct covering (Mirsky-Newman
reciprocal obstruction; Zhang et al. Lemma 1). The maximum of that sum over
k-subsets of D is attained at the k smallest divisors. Exactly:

- sum over the 13 smallest = 1669/1680 ≈ 0.99345 <= 1;
- sum over the 14 smallest = 115/112 ≈ 1.02679 > 1.

Hence no distinct family in D with k <= 13 can cover Z, so C* >= 14. Both sums
are exact rational arithmetic (see verify.py).

### 2.2 Upper bound C* <= 65 (witness + verification)
The following 65 classes have pairwise distinct moduli in D, minimum 7, and
LCM exactly 10080:

| # | class | # | class | # | class | # | class |
|---|-------|---|-------|---|-------|---|-------|
| 1 | 6 mod 7 | 18 | 11 mod 40 | 35 | 65 mod 144 | 52 | 404 mod 560 |
| 2 | 7 mod 8 | 19 | 16 mod 42 | 36 | 43 mod 160 | 53 | 578 mod 630 |
| 3 | 8 mod 9 | 20 | 2 mod 45 | 37 | 121 mod 168 | 54 | 505 mod 672 |
| 4 | 6 mod 10 | 21 | 1 mod 48 | 38 | 110 mod 180 | 55 | 281 mod 720 |
| 5 | 9 mod 12 | 22 | 52 mod 56 | 39 | 18 mod 210 | 56 | 472 mod 840 |
| 6 | 8 mod 14 | 23 | 30 mod 60 | 40 | 169 mod 224 | 57 | 553 mod 1008 |
| 7 | 12 mod 15 | 24 | 7 mod 63 | 41 | 185 mod 240 | 58 | 532 mod 1260 |
| 8 | 3 mod 16 | 25 | 28 mod 70 | 42 | 154 mod 252 | 59 | 875 mod 1440 |
| 9 | 14 mod 18 | 26 | 29 mod 72 | 43 | 248 mod 280 | 60 | 124 mod 1680 |
| 10 | 0 mod 20 | 27 | 59 mod 80 | 44 | 203 mod 288 | 61 | 281 mod 2016 |
| 11 | 4 mod 21 | 28 | 10 mod 84 | 45 | 128 mod 315 | 62 | 2044 mod 2520 |
| 12 | 13 mod 24 | 29 | 74 mod 90 | 46 | 313 mod 336 | 63 | 2153 mod 3360 |
| 13 | 26 mod 28 | 30 | 43 mod 96 | 47 | 209 mod 360 | 64 | 5033 mod 5040 |
| 14 | 24 mod 30 | 31 | 93 mod 105 | 48 | 292 mod 420 | 65 | 7193 mod 10080 |
| 15 | 27 mod 32 | 32 | 73 mod 112 | 49 | 75 mod 480 | | |
| 16 | 33 mod 35 | 33 | 64 mod 120 | 50 | 217 mod 504 | | |
| 17 | 5 mod 36 | 34 | 112 mod 126 | 51 | 404→ see row | | |
| | | 34b | 38 mod 140 | | (51 is 404 mod 560) | | |

(Flat machine-readable list: (6,7),(7,8),(8,9),(6,10),(9,12),(8,14),(12,15),
(3,16),(14,18),(0,20),(4,21),(13,24),(26,28),(24,30),(27,32),(33,35),(5,36),
(11,40),(16,42),(2,45),(1,48),(52,56),(30,60),(7,63),(28,70),(29,72),(59,80),
(10,84),(74,90),(43,96),(93,105),(73,112),(64,120),(112,126),(38,140),(65,144),
(43,160),(121,168),(110,180),(18,210),(169,224),(185,240),(154,252),(248,280),
(203,288),(128,315),(313,336),(209,360),(292,420),(75,480),(217,504),(404,560),
(578,630),(505,672),(281,720),(472,840),(553,1008),(532,1260),(875,1440),
(124,1680),(281,2016),(2044,2520),(2153,3360),(5033,5040),(7193,10080).)

Direct enumeration over Z_10080 confirms all 10080 residues are covered (run
`python3 output/artifacts/verify.py` → VERIFY_OK). Its provenance: it equals
the published Zhang et al. 66-class feasible system at L0 = 10080 with the
single class (233 mod 1120) removed; the remaining 65 still cover everything,
so one modulus of the published system is redundant. The 65 moduli have LCM
exactly 10080 and minimum exactly 7.

### 2.3 Irredundancy (for the stated residues)
For the residue choices above, every class has at least one private residue
(residue covered by it alone). Coverage-count histogram over Z_10080:
covered once: 5926; twice: 3785; thrice: 365; four times: 4; uncovered: 0.
Per-class private counts range from 1 (moduli 2016, 3360, 10080) to 736
(mod 8); all 65 are positive. So no single class can be dropped without
changing residues. (This does not prove global minimality of 65.)

## 3. What is NOT claimed
- Exact C* is not determined; the gap 14..65 is open.
- No claim is made that 64 classes are impossible, or that the 65-witness is
  uniquely minimal, or that the divisor-completed 66-universe needs all 66.
- Coordinate-ascent + kick re-optimization after dropping any one large modulus
  (10080/5040/3360/2520/2016/1680) reached only ~9524–9796/10080 in the
  time-boxed trials; reported as heuristic evidence of a strong local optimum,
  not a lower-bound proof.

## 4. Reproduction
`python3 output/artifacts/verify.py` (stdlib only) checks distinctness,
D-membership, min = 7, LCM = 10080, full 10080-residue coverage, and the exact
fractions 1669/1680 and 115/112, printing VERIFY_OK.

## 5. Prior work and originality
Zhang et al. (arXiv:2607.19029) proved Lmin(7) = 10080 and exhibited one
66-class feasible system; they optimize LCM, not cardinality. The redundancy
finding (one class removable, explicit irredundant 65-subsystem with private-
residue certificate) and the exact 14-lower-bound pairing are new relative to
abstract-level triage; the 65-system itself is derived from, not independent
of, their construction, and is credited accordingly. No competing
minimal-cardinality table for this universe was found at triage.
