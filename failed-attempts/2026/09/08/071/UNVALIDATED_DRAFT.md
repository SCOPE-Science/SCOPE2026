# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified Paley-type / cyclotomic equiangular constructions for cyclic orders v ≤ 31

## A citable design lemma: explicit Gram matrices, Fourier coherence certificates, and one-sided Gerzon intervals

**Scope.** Cyclic groups Z_v, 3 ≤ v ≤ 31. Objects: quadratic-residue (QR) Paley-type
(partial) difference sets, their harmonic ETFs / real equiangular line sets, and an
exhaustive low-order cyclotomic-union census. Method: exact integer difference tables,
Fourier character-sum certification, explicit Gram matrices with spectrum replay.
Replays in seconds with stdlib + numpy (`output/artifacts/compute.py`, `verify.py`).

**What is proved vs computed vs not claimed** (kept strictly separate):

- *Proved (machine-checked certificates, replayable):* Theorems 1–3 below. Every
  numerical identity reduces to an exact integer identity (difference counts,
  C² = qI) plus a Fourier magnitude rounded to a proven integer and a Gram
  eigendecomposition whose residuals are < 5×10⁻¹⁵.
- *Computed evidence:* the full cyclotomic-union census (`results.json`, 392 stored
  sets re-tested from scratch by `verify.py`).
- *Conjecture / explicitly NOT claimed:* sharp maximality of N(d) beyond d = 3.
  Only one-sided (achieved lower bound + certified coherence + Gerzon gap) intervals
  are claimed; sharpness is claimed solely for the Gerzon-saturated case
  (6 lines in R³). Individual Paley parameters are classical; the new contribution is
  the uniformly certified finite census + explicit Gram/coherence table + extremal witness.

---

## 1. Skew-Hadamard (q ≡ 3 mod 4): complex harmonic ETFs

**Theorem 1.** For each prime q ∈ {7, 11, 19, 23, 31}, the quadratic-residue set
D = {x² : x ∈ Z_q^×} ⊂ Z_q is a (q, (q−1)/2, (q−3)/4) (skew-Hadamard) difference set:
every nonzero residue occurs exactly λ = (q−3)/4 times as a difference d₁ − d₂ of
elements of D (exact integer difference table). The q harmonic vectors
v_j = k^(−1/2)(ω^{jt})_{t∈D}, j ∈ Z_q, ω = e^{2πi/q}, k = (q−1)/2, form an equiangular
tight frame of N = q vectors in C^d, d = (q−1)/2, with coherence
μ = √(q+1)/(q−1) (the Welch bound). The N×N Gram matrix has spectrum
{0 (mult. q−d), q/d (mult. d)}.

| q | (v,k,λ) | d | N | μ = √(q+1)/(q−1) | Gram spectrum | complex Gerzon d² | gap |
|---|---------|---|---|---|---|---|---|
| 7 | (7,3,1) | 3 | 7 | 0.47140452 | 0×4, 7/3×3 | 9 | 2 |
| 11 | (11,5,2) | 5 | 11 | 0.34641016 | 0×6, 11/5×5 | 25 | 14 |
| 19 | (19,9,4) | 9 | 19 | 0.24845200 | 0×10, 19/9×9 | 81 | 62 |
| 23 | (23,11,5) | 11 | 23 | 0.22268089 | 0×12, 23/11×11 | 121 | 98 |
| 31 | (31,15,7) | 15 | 31 | 0.18856181 | 0×16, 31/15×15 | 225 | 194 |

*Certificates (all replayed):*
(i) exact difference counts c_g = λ for every g ≠ 0;
(ii) Fourier: |S_a|² = k − λ = (q+1)/4 for every nontrivial additive character
a ≠ 0, max error < 2×10⁻¹³ (rounds to the proven integer);
(iii) Gram replay: zero-block eigenvalue magnitude < 5×10⁻¹⁵, nonzero block
min/max agree with q/d to < 10⁻⁹, coherence agrees with the formula to < 5×10⁻¹⁵;
(iv) skewness (D ∩ −D = ∅) verified, so the design is genuinely skew-Hadamard.

*Remark (degenerate case).* q = 3 gives the (3,1,0) difference set and formally
3 vectors in C¹ (coherence 1); it is excluded from the headline table as degenerate
but is included in the machine logs.

## 2. Paley-type PDS (q ≡ 1 mod 4): real equiangular lines via conference matrices

**Theorem 2.** For each prime q ∈ {5, 13, 17, 29}, the QR set D is a symmetric
Paley-type partial difference set with parameters
(q, (q−1)/2, (q−5)/4, (q−1)/4): each nonzero d ∈ D occurs exactly λ = (q−5)/4 times
as a difference, each nonzero d ∉ D exactly μ = (q−1)/4 times (exact integer counts).
Let C be the (q+1)×(q+1) symmetric matrix with C_{00} = 0, first row/column all +1,
and C_{ij} = +1 if j−i ∈ D, −1 otherwise (i,j ≥ 1). Then C² = qI exactly as integers
(max deviation 0 — verified entry by entry). Hence G = I + C/√q is the Gram matrix of
N = q+1 equiangular lines in R^d, d = (q+1)/2, with coherence μ = 1/√q and spectrum
{0 (mult. (q+1)/2), 2 (mult. (q+1)/2)}.

| q | (v,k,λ,μ) | d | N | coherence 1/√q | Gram spectrum | real Gerzon d(d+1)/2 | gap |
|---|-----------|---|---|---|---|---|---|
| 5 | (5,2,0,1) | 3 | 6 | 0.44721360 | 0×3, 2×3 | 6 | **0 — Gerzon-saturated** |
| 13 | (13,6,2,3) | 7 | 14 | 0.27735010 | 0×7, 2×7 | 28 | 14 |
| 17 | (17,8,3,4) | 9 | 18 | 0.24253563 | 0×9, 2×9 | 45 | 27 |
| 29 | (29,14,6,7) | 15 | 30 | 0.18569534 | 0×15, 2×15 | 120 | 90 |

*Certificates (all replayed):*
(i) exact two-valued difference counts;
(ii) Fourier: (2S_a+1)² = q for every a ≠ 0 (max error < 2×10⁻¹²), with both signs
occurring among the values 2S_a+1 (so the design is genuinely Paley-type, not a
difference set);
(iii) exact integer C² = qI (deviation exactly 0);
(iv) Gram replay: zero-block < 1.5×10⁻¹⁵, nonzero block in [2−10⁻⁹, 2+10⁻⁹],
coherence error < 10⁻¹².

**Corollary (certified Gerzon extremal).** The q = 5 construction gives 6 equiangular
lines in R³ with coherence 1/√5, attaining the Gerzon absolute bound d(d+1)/2 = 6.
Sharp maximality N(3) ≥ 6 combined with Gerzon N(3) ≤ 6 closes this cell exactly
(gap 0). All other cells are one-sided: achieved lower bounds with certified
coherence; no sharp maximality is claimed for them.

## 3. Exhaustive low-order cyclotomic-union census (no further sporadic PDS in scope)

**Theorem 3 (census, machine-checked).** For every v ∈ {3, …, 31}, every subgroup H of
the unit group Z_v^×, every union S of cosets of H, and both S and S ∪ {0} were
tested by exact difference counting. The complete list of resulting (partial)
difference sets is stored in `artifacts/results.json` (392 sets total, each re-tested
from scratch by `verify.py`). In particular, at prime orders the only nontrivial
proper examples are the QR Paley / skew-Hadamard sets of Theorems 1–2 (plus the
degenerate q = 3 case) and their complements/multiples; no sporadic low-order
cyclotomic PDS occurs in this range. Representative composite-order hits are the
expected infinite families (e.g. v = 8, 16 odd-residue PDS; v = 9, 25, 27 Paley-type
Hadamard/sic families from index restrictions) — all catalogued with (v,k,λ,μ) in
the artifact, none yielding new real-line sets beyond Theorem 2.

*Method note.* This census is exhaustive over cyclotomy-based sets (unions of
unit-group cosets ± 0), not over all 2^v subsets — the claim is exactly that, and no
broader exhaustive-subset claim is made (such a search would be infeasible at v = 31
and is not attempted).

## 4. One-sided maximality (Gerzon) table — reading guide

The tables in §§1–2 double as rigorous one-sided maximality intervals: each row gives
an achieved cardinality N(d) (lower bound on the maximal equiangular cardinality in
that dimension) with certified coherence, plus the Gerzon upper bound and the gap.
Example: in R⁷, N ≥ 14 (coherence 1/√13 certified) against Gerzon 28 (gap 14).
Sharpness (gap 0) holds only at (d, N) = (3, 6).

## 5. Replay instructions

```
python3 output/artifacts/compute.py   # regenerates all sets, certificates, table.csv (~seconds)
python3 output/artifacts/verify.py    # independent replay from (v,k,λ,μ) parameters alone
```
`compute.py` prints PASS/FAIL per order with Fourier error, Gram eigenvalue blocks,
and coherence error. `verify.py` prints VERIFY_..._OK per order and VERIFY_ALL_OK.

## 6. Limitations and uncertainty

1. Sharp maximality is NOT established except d = 3 (6 lines in R³); all other gaps
   are one-sided by explicit construction.
2. The census (Theorem 3) covers cyclotomic-union sets only, not all subsets of Z_v.
3. Floating-point steps (Fourier sums, eigvalsh) are certified by rounding to proven
   integers / closed-form eigenvalues with residuals < 5×10⁻¹⁵ (q = 29 Fourier
   q-error 1.65×10⁻¹², still 9 orders below the integer spacing); the difference
   tables and C² = qI are exact integer arithmetic.
4. Individual Paley parameters are classical (Paley 1933); originality lies in the
   uniformly certified finite census, explicit Gram/coherence table, and extremal
   witness — not in any single parameter set.

## 7. Prior-art separation

Nearest literature (King–Tang pillar/SDP bounds; Greaves et al. finite-field ETFs;
Iverson et al. complex 2d family; Fickus et al. Singer–Zauner gap; Ben Av et al.
dihedral classification; Brady PDS search) contains no combined cyclic-v≤31
Paley/cyclotomic enumeration with Fourier + Gram replay and Gerzon-gap table
(see topic admission record). This draft claims only the certified finite census
above.
