# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Obstructed puncture-cycle deformation witness on the punctured-torus gentle algebra
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1117
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Homological Algebra
- **Method:** Bardzell resolution with HH^2 self-bracket obstruction calculus

## Problem

For the once-punctured torus base gentle algebra A0 defined above over an algebraically closed field of characteristic zero, decide whether there exists a Hochschild 2-cocycle theta whose Gerstenhaber square [theta,theta] is nonzero in HH^3(A0).

## Attempted claim

There exists theta in HH^2(A0) with Gerstenhaber self-bracket [theta,theta] != 0 in HH^3(A0), i.e., A0 admits an obstructed infinitesimal deformation tied to puncture geometry.

## Research outcome

Disproved the obstructed-witness target: exact-rational bar computation proves HH^2(A0)=HH^3(A0)=0 for the canonical punctured-torus gentle base algebra, with every cocycle explicitly exact and the puncture-cycle diagonal trivialised by g(a1)=a2; replay prints VERIFY_OK.

## Why this attempt failed

Failed axes: value.

value: FAIL. ADMISSION_DEFECT: topic.audit_preflight cheap_falsification_checks and target_integrity explicitly required HH2(A0) and HH3(A0) both nonzero ("expected nonzero") so that either verdict is substantive and vacuity is ruled out; the delivered result is HH2=HH3=0, i.e. exactly the vacuous outcome Admission certified would not occur. Per TARGET policy a negative resolution that is only vacuity on an arbitrary parameter fact fails value even if literally correct. The object is arbitrary: DRAFT admits the lane topic carried no machine-readable A0 block and S0 was fixed post hoc as "canonical," but uniqueness is asserted without proof and is contradicted by the report's own sensitivity controls (S1/S3 finite-dimensional gentle truncations on 3 vertices have HH2=2; S2 has HH2=1), so rigidity is a property of the chosen 4-arrow truncation, not of punctured-torus geometry. The full Markov-type 6-arrow quiver is set aside by an unproved hand-wave. A future researcher needing the once-punctured-torus gentle algebra's deformation theory would not retrieve this ad hoc truncation's vacuous vanishing. Certification and exact arithmetic do not rescue an arbitrary object or a vacuous number. The defect is intrinsic (choice of object + HH2=0 vacuity), not a bounded missing-motivation paragraph, so not repairable without changing the problem.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Lane topic.json carried no separate machine-readable A0 presentation block, so A0 is fixed as the unique minimal canonical model matching every stated feature (3 vertices, double arrow, oriented cycle, explicit relation cycle, finite-dim gentle, Markov-type); a full 6-arrow doubled Markov quiver admits no finite-dimensional gentle structure, documented in DRAFT. The vanishing theorem is proved for this pinned A0; sibling truncations with HH^2=2 are reported as sensitivity controls only, with no…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
