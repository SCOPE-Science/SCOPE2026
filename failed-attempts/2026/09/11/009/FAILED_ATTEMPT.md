# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified opening of the first collapsed gap and quantitative finite-gap trace defect for a cn^4-perturbed genus-1 Lame Hill operator
- **Round:** 2026-09-07-first-light-01
- **Lane:** 686
- **Disposition:** NO_RESULT
- **Domain:** Integrable Systems
- **Method:** Hill-discriminant interval enclosure of a non-finite-gap perturbation with Dirichlet-interlacing and trace-defect replay

## Problem

Decide certified open-vs-closed for the first collapsed gap of one explicit non-integrable same-period deformation of the genus-1 Lame potential, and certify a quantitative genus-1 trace defect proving departure from the finite-gap locus.

## Attempted claim

For u_*(x)=2*sn(x|1/2)^2+(1/10)*cn(x|1/2)^4 of period L=2K(1/2), the Hill operator H_*=-d^2/dx^2+u_* has an open second gap: periodic/antiperiodic eigenvalues E3^-<E3^+ with certified disjoint two-sided enclosures proving width W=E3^+-E3^- in [1e-3,0.5], and the genus-1 Its-Matveev power-sum defect satisfies d1>=5e-4, all replayable in <=60 s from committed Hill-discriminant interval matrices without a black-box eigensolver.

## Research outcome

Target blocked (float-only width evidence with forbidden eigensolver; d1 formula as stated provably non-vanishing on true-Lame control: 9.3138). Preset fallback attempted (float discriminant bracket points 3.995/4.0/4.08/4.085 located) but blocked (validated-Taylor prototype diverges off-manifold at step 92; no rigorous L/potential/monodromy enclosure in-lane). Clean exit with NO_RESULT; no emergent finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

All eigenvalue/discriminant numbers are non-rigorous float64 scouts (numpy eigvalsh is a forbidden black box; RK4 has no remainder). No certified interval is claimed for any band edge, width, defect, or discriminant sign. Artifacts are scout scripts only.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: All eigenvalue/discriminant numbers are non-rigorous float64 scouts (numpy eigvalsh is a forbidden black box; RK4 has no remainder). No certified interval is claimed for any band edge, width, defect, or discriminant sign. Artifacts are scout scripts only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
