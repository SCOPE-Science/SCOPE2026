# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Axisymmetric Jacobi stability gap for the equal-volume standard double bubble in S^3
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1050
- **Disposition:** NO_RESULT
- **Domain:** Calculus of Variations
- **Method:** axisymmetric Sturm-Liouville comparison barrier for the coupled three-sheet Jacobi system

## Problem

Let Sigma_v be the equal-volume standard double bubble in the unit sphere S^3(1) with enclosed volumes v1=v2=v in [0.05,0.30] of Vol(S^3). Restrict the volume-preserving Jacobi second-variation form Q to axisymmetric (rotationally symmetric about the bubble axis, m=0) admissible fields satisfying linearized 120-degree triple-junction compatibility and orthogonality to ambient Killing fields. Decide the stability gap in this sector with explicit constant kappa_axis=1/4.

## Attempted claim

For every v in the stated window, every admissible axisymmetric volume-preserving field u orthogonal to Killing motions satisfies Q(u) >= (1/4) ||u||_{L^2(Sigma_v)}^2, certifying a uniform quantitative stability gap kappa_axis=1/4; a rigorous normalized counterexample with Q(u)<0 or an explicit symmetric competitor with area defect disproves the claim.

## Research outcome

Target blocked: no verified kappa=1/4 gap and no certified destabilizer; Neumann shooter failed its Bessel cross-check and the coupled solver crashed, so work stops with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The uniform kappa=1/4 axisymmetric Jacobi gap was neither proved nor disproved. The per-sheet Neumann shooter failed its flat-disk Bessel cross-check with values about four times too large, indicating an undiagnosed root-bracketing or series-start bug, and the coupled finite-difference eigenproblem crashed with a singular lumped-mass matrix before producing any gap number. The 120-degree junction transmission-term sign lemma and interval certification over vf in [0.05,0.30] were never reached, so no verified bound or certified destabilizer exists.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The uniform kappa=1/4 axisymmetric Jacobi gap was neither proved nor disproved. The per-sheet Neumann shooter failed its flat-disk Bessel cross-check with values about four times too large, indicating an undiagnosed root-bracketing or series-start bug, and the coupled finite-difference eigenproblem crashed with a singular lumped-mass matrix before producing any gap number. The 120-degree junction transmission-term sign lemma and interval certification over vf in [0.05,0.30] were never reached,…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
