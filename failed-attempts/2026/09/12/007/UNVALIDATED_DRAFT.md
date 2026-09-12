# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Graded-root distinction of Σ(2,3,7) vs Σ(2,3,11): corrected reduced-root certificate

## 1. Graphs and setup (auditable)

Canonical negative-definite star-shaped Seifert plumbings (verified in
`output/artifacts/verify_target.py`: negative-definite spectra, det +1 / −1,
one bad vertex = center):

- **G7** (Σ(2,3,7)): center −1, legs [−2], [−3], [−7]; s=4.
- **G11** (Σ(2,3,11)): center −2, legs [−2], [−2,−2], [−2,−2,−2,−2,−3]; s=9.

Both have exactly one bad vertex (the center), hence are almost-rational:
lattice cohomology is carried by H⁰, i.e. by the graded root, H^{>0} = 0
(Némethi, cited). Canonical class K from (K,vᵢ) = −eᵢ−2 (exact rational
solve): K²+s = 0 (G7), 8 (G11).

Single consistent weight throughout: **χ(x) = −(x,x+K)/2**, integer-valued
on ℤˢ. One definition (`chi_of` in `laufer.py`) is imported by both
verifiers — the prior sign split is removed. d = (K²+s)/4 − 2·min χ.

## 2. Reduction (no truncation) and corrected engine

One-bad-vertex reduction (Némethi, cited): the graded root is recovered from
w(i) = min{χ(x) : x₀ = i}; {w ≤ n} ⊂ ℤ has the same components/merges as
{χ ≤ n} ⊂ ℤˢ. The ledger below is the full root, not a truncation.

Corrected engine (`laufer.py`): the old one-sided (increment-only) Laufer
walk is replaced by **two-sided global fiber minimization**: greedy
two-sided walk (increment iff pairing ≥ 2, decrement iff pairing ≤ eᵥ,
each step dropping integer χ by ≥ 1) plus exact per-arm dynamic-programming
polish. Legs decouple given x₀ (arms meet only at the center), so each arm
contribution is minimized by exact chain DP inside a box around the real
minimizer whose radius comes from a certified exact-LDL positive-definiteness
lower bound plus the current gap; the loop terminates on strict χ decrease.
Every reported minimizer is certified two-sided Laufer-closed
(eᵥ+1 ≤ (x,Eᵥ) ≤ 1 on all leg vertices) **and** per-arm DP-optimal
(`certify_fiber`; 43/43 G7 fibers, 48/48 G11 fibers over the verdict windows).

Rigorous tail bound from true minima (not edge values): exact real minimum
realmin(i) = A·i²+B·i+C of χ over {x₀=i} via exact Schur complement —
G7: (1/84)i²+(5/21)i; G11: (1/132)i²−(1/44)i — and the window is the proven
envelope realmin(i) > N outside it (N=4: G7 [−31,11], G11 [−22,25]). No fiber
outside can meet levels n ≤ 4, so S₀/S₁/S₂ counts are complete.

## 3. Corrected run ledger (replay: `python3 output/artifacts/verify_target.py` → VERIFY_OK)

Corrected reduced minima (true-χ; closed DP-optimal minimizers in script):

- G7: …, w(−6..−5)=1, w(−4..0)=0, w(1)=1, w(2..6)=0, w(7..11)=1, …; min 0.
  Old error corrected: the negative-side minima now extend to
  S₀ ⊃ {−4,…,0}, not {−1,0} (the one-sided walk had missed decrements).
- G11: …, w(−6..−1)=1, w(0)=0, w(1..2)=1, w(3)=1, w(4)=1, w(5)=1, w(6)=0,
  w(7..12)=1, w(13..18)=2, …; min 0. Prior spurious values
  (w(3)=3, w(6)=5, …) were artifacts of the one-sided walk and are withdrawn.

Component runs Sₙ = {w ≤ n} (N=4 windows):

| n | R7 (G7) | R11 (G11) |
|---|---------|-----------|
| 0 | 2 runs: {−4,…,0} (width 5), {2,…,6} (width 5) | 2 runs: {0} (width 1), {6} (width 1) |
| 1 | 1 run: {−10,…,11} | 1 run: {−6,…,12} |
| 2 | 1 run: {−12,…,11} | 1 run: {−12,…,18} |

Corrected verdict (counts alone no longer 2v1 at S₀ — both split):

1. **R7 ≇ R11 as graded roots.** The S₀ run *shapes* differ: [5,5] vs
   [1,1] — no grading-preserving tree isomorphism maps one pair of
   branches to the other (left/right widths 5,5 vs 1,1; gaps at i=1 vs the
   {1,…,5} gap). The merge data sharpen this: R7 merges at n=1 across a
   single width-1 barrier (w(1)=1); R11 merges at n=1 across a width-5
   barrier (w(1..5)=1), and its second S₀ leaf sits far out at i=6 with a
   distinct minimizer (6,3,4,2,5,4,3,2,1), w=0. The S₁/S₂ envelopes
   (widths 22/24 vs 19/31) are further non-isomorphism witnesses.
2. **d-invariants differ:** d(G7) = 0 − 0 = 0; d(G11) = 8/4 − 0 = 2 —
   an independent homology-cobordism obstruction separating the spheres
   (hence the roots cannot coincide).
3. **Exact-sequence certification, downgraded as instructed:** we do not
   prove the lattice blow-up/surgery exact sequence here; we report
   **observed blow-up stability** of the corrected ledger
   (`stability.py` → STABILITY_OK): attaching a (−1)-leaf to the center
   preserves K²+s and min w (0/0, 8/0) and the S₀ shapes
   (G7 [5,5]-type 2-run, G11 [1,1]-type 2-run persist). Background
   blow-up invariance of lattice cohomology (Némethi, cited) is the route
   by which this stability lifts to a 3-manifold invariant; the sequence
   itself is not re-proved.

## 4. Proved vs cited

- Proved (machine-checked, exact rationals): graph canonicity, K²+s, every
  fiber minimum with two-sided closedness + per-arm DP optimality over the
  full N=4 windows, realmin tail envelopes, S₀/S₁/S₂ run shapes, d-values,
  observed (−1) blow-up stability.
- Cited (not re-proved): Némethi reduction theorem, almost-rational
  H^{>0} = 0, blow-up invariance of lattice cohomology, lattice–Floer
  identification for these graphs.
- Withdrawn: all prior one-sided-walk numbers (notably G7 S₀ = {−1,0} and
  the G11 w(3)=3/w(6)=5 spikes); the old S₂ 1v2 split does not survive
  correction and is replaced by the shape + d-invariant distinction above.

## 5. Replay

```
python3 output/artifacts/verify_target.py   # -> VERIFY_OK
python3 output/artifacts/stability.py       # -> STABILITY_OK
```

Artifacts: `laufer.py` (unified-χ two-sided engine + DP certificates +
tail bound), `verify_target.py` (verdict), `stability.py` (observed
blow-up stability).
