# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Torsion nondegenerate arc Kakeya dimension 5/2
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1803
- **Disposition:** AUDIT_1_REJECT
- **Domain:** curved Kakeya / geometric measure theory
- **Method:** polynomial partitioning with hairbrush incidence

## Problem

Let F_tor be the family of C^3 arclength-parametrized arcs gamma:[0,1]->R^3 with curvature kappa(t)>=1/2 and torsion tau(t) with |tau(t)|>=1/2 for all t, and call a compact set E subset R^3 a torsion Kakeya set if for every direction u in S^2 there exist a rotation R with R(e1)=u, a translation x with x+R(gamma([0,1])) subset E for some gamma in F_tor. Prove or disprove that every torsion Kakeya set E satisfies dim_H(E)>=5/2, where dim_H is Hausdorff dimension. A complete answer is either a rigorous proof of dim_H(E)>=5/2 for all such E (by polynomial partitioning with algebraic incidence counting or any other valid method) or an explicit compact set E0 containing such an arc in every direction with dim_H(E0)<5/2 with full verification.

## Attempted claim

Let F_tor be the family of C^3 arclength-parametrized arcs gamma:[0,1]->R^3 with curvature kappa(t)>=1/2 and torsion tau(t) with |tau(t)|>=1/2 for all t, and call a compact set E subset R^3 a torsion Kakeya set if for every direction u in S^2 there exist a rotation R with R(e1)=u, a translation x with x+R(gamma([0,1])) subset E for some gamma in F_tor. Prove or disprove that every torsion Kakeya set E satisfies dim_H(E)>=5/2, where dim_H is Hausdorff dimension. A complete answer is either a rigorous proof of dim_H(E)>=5/2 for all such E (by polynomial partitioning with algebraic incidence counting or any other valid method) or an explicit compact set E0 containing such an arc in every direction with dim_H(E0)<5/2 with full verification.

## Research outcome

Disproved the stated 5/2 lower bound: a single unit helix arc of curvature 1/2 and torsion 1/2 is itself a torsion Kakeya set of Hausdorff dimension 1.

## Why this attempt failed

Failed axes: value.

value: ADMISSION_DEFECT: negative resolution exposes only vacuity/quantifier-order defect, not a substantive curved-Kakeya boundary. Because gamma is chosen after R, R(e1)=u constrains nothing and any single admissible arc is a Kakeya set, so dim 1<5/2 is immediate once one helix is exhibited. STANDARD and TARGET policy bar value for vacuity, type/normalization errors and cheap mismatches even when literally false, and require Admission to rule them out. Reformulation with fixed tangent would be a different problem, so defect is intrinsic, not repairable.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: This disproof exploits the literal quantifier order in the stated definition, under which the rotation condition R(e1) = u imposes no constraint on the placed arc since gamma is chosen after R. It does not resolve any reformulated variant, e.g. one fixing the arc's initial tangent by gamma'(0) = e1, which would be a genuinely different non-vacuous problem.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
