# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact Gordian distance two for a nominated alternating Montesinos pair via biquandle separation
- **Round:** 2026-09-07-first-light-01
- **Lane:** 204
- **Disposition:** NO_RESULT
- **Domain:** Low-Dimensional Topology
- **Method:** Alexander-biquandle coloring enumeration with explicit crossing-change paths and determinant corroboration

## Problem

Exhibit one certified pair of alternating 3-tangle Montesinos knots at 10-11 crossings with exact Gordian distance 2: a lower bound d>=2 from Alexander-biquandle coloring-count separation with independent recount plus determinant corroboration, and an upper bound d<=2 from an explicit two-crossing-change path with logged diagrams.

## Attempted claim

There exists an explicitly named pair of alternating 3-tangle Montesinos knots at 10-11 crossings (frozen rational parameters, Conway notations, PD codes) whose Gordian distance equals exactly 2: Alexander-biquandle coloring counts over the stated finite ring provably separate the relevant crossing-change neighborhoods giving d>=2, and a logged two-crossing-change path transforms one diagram into the other giving d<=2.

## Research outcome

Resumed after 2 disconnects with bounded atomic substeps. Froze alternating pretzel-Montesinos diagrams K10=P(3,3,4) (10x) and K11=P(3,3,5) (11x) with audit: 1 knot component, alternating, planar Euler V-E+F=2, dual-face 2-colorable. Two independent exact determinant computations agree: Tait spanning-tree counts and Fox coloring minors give det(K10)=33, det(K11)=39 (trefoil control = 3); mod-p Fox nullities separate the diagrams (K10: 9/121/13 vs K11: 9/11/169 colorings at p=3/11/13). This certifies DISTINGUISHABILITY (Gordian distance >= 1) only. No rigorous d>=2 obstruction was obtained: Goeritz LDL signatures ran with unsigned incidence and are not certified knot signatures, and distinct determinants/coloring counts alone do not imply d>=2. The explicit two-step crossing path was not built. Honest NO_RESULT on both the exact-distance-2 target and the d>=2 fallback lemma.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Rotation-system cyclic order was patched empirically to satisfy Euler=2; embedding correctness rests on Euler face-count + shading bipartiteness + knot-circuit checks, not on external table lookup.', 'Goeritz LDL numbers were computed with unsigned incidence and are NOT claimed as knot signatures; no signature-difference lower bound is claimed.', 'S1 writhe values (+2/-11) were internally inconsistent and are disregarded; no writhe-dependent claim is made.', 'Distinct determinants / distinct Fox coloring counts distinguish the knots (d>=1) but do not imply d>=2; no valid d>=2 obstruction (Murasugi-signature, Jones-at-root, or 1-crossing-neighbor analysis) was completed in the lane.', 'Two upstream stream disconnects forced short bounded substeps; the explicit two-step upper-bound crossing path was not constructed.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Rotation-system cyclic order was patched empirically to satisfy Euler=2; embedding correctness rests on Euler face-count + shading bipartiteness + knot-circuit checks, not on external table lookup.', 'Goeritz LDL numbers were computed with unsigned incidence and are NOT claimed as knot signatures; no signature-difference lower bound is claimed.', 'S1 writhe values (+2/-11) were internally inconsistent and are disregarded; no writhe-dependent claim is made.', 'Distinct determinants / distinct…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
