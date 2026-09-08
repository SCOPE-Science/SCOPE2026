# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified S8 extremal Kronecker multiplicity 17 and full containment in the tensor square of (4,2,1,1)

## 1. Definitions
For partitions λ,μ,ν of n, the Kronecker coefficient is
g(λ,μ,ν) = (1/n!) Σ_C |C| χ_λ(C) χ_μ(C) χ_ν(C),
the sum over conjugacy classes C of S_n, with irreducible characters χ
computed by exact Murnaghan–Nakayama rim-hook recursion over ℤ.
g(λ,μ,ν) is the multiplicity of [ν] in [λ]⊗[μ].

## 2. Theorems (machine-verified, exact integer arithmetic)
- **T1 (S8 maximum).** The S8 Kronecker maximum is exactly 17, attained at
  exactly one ordered triple: ((4,2,1,1),(4,2,1,1),(4,2,1,1)). The full
  22³=10648-entry table has 5048 nonzero entries (5600 vanish). The next
  largest value is 14 (6 ordered triples); 7 ordered triples have value ≥ 14.
- **T2 (full containment).** [(4,2,1,1)]^⊗2 contains all 22 irreducibles of S8.
  In the order (8),(1⁸),(7,1),(2,1⁶),(6,1,1),(4,4),(3,1⁵),(2⁴),(6,2),
  (2²,1⁴),(5,3),(5,1³),(4,1⁴),(2³,1²),(3,3,2),(4,2,2),(3,3,1,1),(5,2,1),
  (3,2,1³),(4,3,1),(3,2²,1),(4,2,1,1), the multiplicities are exactly
  1,1,2,2,4,4,4,4,5,5,6,6,6,6,8,12,12,13,13,14,14,17 (min 1, max 17).
- **T3 (companions).** S6: max 5, unique ordered, at ((3,2,1)³), 511/1331
  nonzero. S7: max 9 with 4 ordered argmax — (4,2,1)³ plus the 3 permutations
  of ((4,2,1),(3,2,1,1),(3,2,1,1)) — and 1599/3375 nonzero.
- **T4 (contrast).** Neighbouring S8 squares are mostly vanishing:
  (7,1)² has 4/22 nonzero, (4,4)² 7/22, (6,2)² 10/22, (2⁴)² 7/22.

## 3. Method (two independent implementations, stdlib only)
- **Method A** (`output/primary_mn.py`, `output/export_A.py`): rim hooks via
  sub-partition enumeration + skew-shape test (connected, no 2×2); character
  recursion peeling the first part of the cycle type; class sizes via
  centralizer formula; dimensions cross-checked against the hook-length
  formula; orthogonality ⟨χ_λ,χ_μ⟩=δ verified for all pairs; every Kronecker
  class sum asserted divisible by n! with nonnegative quotient; full S3
  permutation symmetry and conjugation symmetry g(λᵗ,μᵗ,ν)=g(λ,μ,ν) asserted.
- **Method B** (`output/methodB_replay.py`): rim hooks via row-suffix-count
  peeling with independent boundary/2×2/connectivity tests; recursion peeling
  the last part of the cycle type; independently written class-size routine.
  Reproduces the identical full tables for n=6,7,8 (entrywise agreement),
  identical maxima/argmax/nonzero counts, and the identical 22-entry slice.
- **Cold verifier** (`output/artifacts/verify.py`): re-checks stored tables
  (sizes, class sums, S3 symmetry, nonnegativity, headline counts), recomputes
  the 22 slice class sums from scratch with Method-B characters, checks the
  maximizer identity Σ_C |C|χ(C)³ = 17·40320, and spot-checks orthogonality.
  Result: ALL 24 checks PASS.

## 4. Evidence
- `output/artifacts/kronecker_A.json`: full exact tables for n=6,7,8
  (partitions, conjugacy classes + sizes, flat g-tables, multiplicity
  distributions, maxima, ordered argmax).
- `output/artifacts/slice_4211_square.csv`: the 22-entry square slice.
- `output/artifacts/verify.py`: rerunnable certificate (stdlib only).
- Key distributions: S8 {0:5600, 1:2565, 2:1156, 3:468, 4:343, 5:178, 6:136,
  7:48, 8:35, 9:64, 10:24, 11:12, 12:6, 13:6, 14:6, 17:1};
  S7 {0:1776, 1:1031, 2:380, 3:108, 4:36, 5:36, 8:4, 9:4};
  S6 {0:820, 1:422, 2:76, 3:6, 4:6, 5:1}.
- Class data: 22 classes with sizes summing to 40320; hook-length dimensions
  match χ_λ(1⁸) for all 22+15+11 partitions.

## 5. What is proved vs conjectured
- Proved (by exact computation): T1–T4 and every table entry, conditional on
  correct execution of the deterministic integer code, replayed by two
  independent paths with all internal consistency checks passing.
- Conjecture / open: any analytic explanation of why (4,2,1,1) is extremal;
  no complexity or asymptotic claim is made.

## 6. Limitations and honest caveats
- The proof is computational, not analytic; verification requires running the code.
- The second implementation is an independently written from-scratch
  Murnaghan–Nakayama path, not Sage SymmetricFunctions or GAP (neither was
  installed in this environment). Shared-bug risk is mitigated but not
  eliminated; the orthogonality/divisibility/hook-length/S3 checks are
  independent constraints any bug would have to satisfy simultaneously.
- Originality is triage-level (per-topic literature scan); no priority claim
  over Kronecker literature (Ikenmeyer–Mulmuley–Walter hardness/holes;
  Vallejo Saxl/stability; Zhao square-shape results) is asserted.
- S7 maximizer family form: the topic statement's phrasing ("includes
  ((4,2,1),(3,2,1,1),(3,2,1,1)) permutations") is confirmed as exactly the 3
  nontrivial permutations plus (4,2,1)³.

## 7. Reproduction
Run (stdlib only, seconds–minutes):
`python3 output/export_A.py` (builds tables),
`python3 output/methodB_replay.py` (independent replay + agreement),
`python3 output/artifacts/verify.py` (24-check certificate, ALL PASS).
