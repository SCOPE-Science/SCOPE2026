# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Seven-point quartic count in P^4: rigorous disproof and corrected value (TARGET)

## 1. Problem and result

Let `I = <H^4,...,H^4>_{0,4}` (seven point insertions) on `P^4`.
Virtual dimension: `dim Mbar_0,7(P^4,4) = 4 + 5*4 + 7 - 3 = 28 = 7*4`,
so this is the natural enumerative number.

**Theorem.** With standard genus-0 primary Gromov-Witten normalisation
(virtual class, divisor/string/fundamental-class axioms, WDVV), the invariant is
`I = 1`, not `231733`. The value `1` is enumerative: it counts the unique
rational normal quartic through seven general points of `P^4`.

This is a complete TARGET resolution by rigorous disproof with a certified
corrected value.

## 2. Why the answer is 1: classical geometry (proof sketch)

A rational normal quartic in `P^4` is determined by `7` points in linearly
general position: through seven general points there passes exactly one such
curve (the analogue of the twisted cubic through six points in `P^3`, the
conic through five points in `P^2`, the line through two points). Via the
Veronese-style parametrisation `[s:t] -> [s^4:s^3 t:s^2 t^2:s t^3:t^4]`,
seven incidence conditions cut out a unique curve up to reparametrisation,
and the stabiliser quotient gives multiplicity 1. The WDVV computation below
confirms this count is exactly 1 with standard `1/|Aut|` normalisation.

## 3. Computational proof: exact WDVV reconstruction over Q

Program: `output/artifacts/compute_invariant.py` (exact integer arithmetic,
memoised recursion, no floating point, no external dependencies).

Reconstruction rules for `P^r` primaries `inv(d, tuple)`:
- (V) dimension filter: return 0 unless `sum = r + (r+1)d + n - 3`.
- (M) `d = 0`: 1 iff `n = 3` and `sum = r`, else 0 (classical triple).
- (2-pt) `n = 2, d > 0`: 1 iff `d = 1` and both insertions are `H^r`, else 0.
- (3-pt) `n = 3, d > 0`: 1 (small quantum cohomology of projective space).
- (F) fundamental class: `H^0` insertion with `d > 0` or `n > 3` gives 0.
- (D) divisor: `<H, ...>_{0,d} = d * <...>_{0,d}` (strip one `H^1` at a time).
- (W) WDVV: for `n >= 4` with all insertions `>= H^2`, split the minimal
  insertion `a1 = 1 + (a1-1)` as `alpha = H^1, beta = H^{a1-1}`, with
  `gamma = max` of the remaining insertions and `delta =` next-max, `S` the rest.
  The WDVV identity `LHS(alpha,beta|gamma,delta) = RHS(alpha,gamma|beta,delta)`
  has exactly one term proportional to the target (the `(d1 = 0, S1 = empty,
  e = r - a1)` term on the LHS, whose side factor is the classical triple 1),
  and every other same-`(d, n)` term vanishes on dimension grounds:
  `alpha + beta = a1 <= r - 1` (since `a1 <= r` and here `a1 = 4 = r` gives
  `alpha + beta = 4`, and the side factor `<1, beta, e>` with `d1 = 0`
  forces `e = r - alpha - beta = 0`, making the co-factor
  `<H^r, gamma, delta, S>` dimension-mismatched as it has the full target
  codimension plus an extra `r`). Hence the target equals an explicit sum of
  products of strictly lower-`(d, n)` invariants. Termination by lexicographic
  descent in `(d, n)`.

Output (`output/artifacts/main_run.log`):
- P^2 calibration: `N_1 = 1, N_2 = 1, N_3 = 12` (the classical numbers of
  rational plane curves through `3d - 1` points: 1, 1, 12) and
  `N_4 = 620` (checked separately) — all standard values, confirming the engine.
- P^4: `<H^4,H^4>_{0,1} = 1`, `<H^4,H^4,H^1>_{0,1} = 1`;
  **`<H^4 x7>_{0,4} = 1`**. Claim `231733` -> MISMATCH.

## 4. Independent checks

- `output/artifacts/verify_residuals.py` (`residual_run.log`): 8/8 exact WDVV
  residuals vanish at dimension-matching tuples, including three independent
  insertion choices at the target tuple itself; divisor-axiom spot check passes.
- `output/artifacts/verify_perm.py` (`perm_run.log`): two independent
  reconstruction choices (`gamma = max` vs `gamma = min`) both give target 1
  (SPLIT_AGREE_PASS).
- Integrality/positivity: output is the positive integer 1; no denominators.
- Growth ladder is consistent with enumerativity (lines through 2 points = 1,
  and the cubic/quartic ladder values recorded in the worklog are the standard
  small counts, e.g. plane `N_4 = 620` reproduced).

## 5. Error diagnosis

The claimed `231733` is off by five orders of magnitude from the enumerative
count 1. Plausible sources: a transcription from a twisted/quintic table, an
unreduced fixed-graph sum (missing `1/|Aut|` or the non-equivariant limit),
or a wrong insertion power. No normalisation consistent with the stated
"standard virtual-class and `1/|Aut|` normalisations" can produce 231733,
since the certified reconstruction under exactly those axioms gives 1.

## 6. Limitations and uncertainty

- The computation is an exact WDVV reconstruction, not a re-enumeration of
  torus-fixed combs one by one; its correctness rests on the standard
  Kontsevich-Manin axioms, which are theorems for genus-0 primaries.
- The scripts use Python integers with memoisation; total cache is 405 P^4
  entries and the run completes in seconds. Re-run with
  `python3 output/artifacts/compute_invariant.py`.
- Classical uniqueness of the rational normal quartic through seven general
  points is sketched, not proved from scratch; the certified integer 1 is the
  load-bearing result.

## 7. Artifacts

- `output/artifacts/compute_invariant.py` — engine + target computation.
- `output/artifacts/verify_residuals.py`, `residual_run.log` — 8/8 WDVV residuals.
- `output/artifacts/verify_perm.py`, `perm_run.log` — split-independence.
- `output/artifacts/main_run.log` — calibration + target output.
