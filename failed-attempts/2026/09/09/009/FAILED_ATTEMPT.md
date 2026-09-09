# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Nill reductivity census over all 4319 three-dimensional reflexive polytopes with Demazure-root dimensions and sharpness witnesses
- **Round:** 2026-09-07-first-light-01
- **Lane:** 294
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Convex Geometry
- **Method:** exact barycenter computation with Demazure-root enumeration and triangulation-volume cross-check

## Problem

Over the complete Kreuzer-Skarke classification of 4319 three-dimensional reflexive polytopes, compute each polytope barycenter and Demazure-root set exactly, partition the classes into Nill barycenter-zero (hence reductive) versus nonzero, determine reductive automorphism dimensions, and exhibit explicit non-reductive witnesses testing sharpness of the sufficient criterion, all with replay logs.

## Attempted claim

Exact partition of the 4319 3D reflexive classes into barycenter-zero (reductive by Nill) and barycenter-nonzero sets with counts, full Demazure-root dimension table, dimension extremals, and at least one certified non-reductive witness proving the barycenter-zero sufficient condition is not necessary (or a certified sharpness verdict with gap).

## Research outcome

Certified exact audit of Nill reductivity criteria on 7 reflexive 3-polytopes with a sufficient-but-not-necessary sharpness instance (prismQ), a reproduced non-reductive witness (Nill Ex 2.16 simplex), and two extremal bound attainments, all replayable via a stdlib verifier.

## Why this attempt failed

Failed axes: value.

value: Strongest headline (Theorem B: prismQ reductive with b!=0, plus 7-row certified table) is correct and new as explicit data but independently low value. Reasons: (1) Abstract sharpness 'bP=0 not necessary' is already implied by Nill Remark 4.3 pairwise independence (ii holds => reductive with b!=0 exists); draft admits this, so no new theoretical layer. (2) Panel scope is arbitrary: 7 chosen polytopes, not the admitted complete 4319 census nor the fallback natural simplicial subfamily; no KS IDs, no argument why Q=conv((1,0),(0,1),(-1,-1),(0,-1)) or H are natural beyond yielding desired b!=0/b=0 contrast. Product E1xQ is explained but not pre-motivated as a needed object. (3) Most entries mechanically implied or textbook: b=0 for 5 symmetric cases by symmetry; simplex barycenters are vertex averages; W root counts reproduce Nill Ex.2.16; E3* dim15 and cube 6 root-facets are standard P^3/(P^1)^3 illustrations of Nill bounds. Only new numbers are routine centroids (-1/6, duals) of ad-hoc prisms. (4) No downstream need shown for these specific numbers; K-stability/G-Fano programs need verdicts for concrete classes but draft cites no use of prismQ/H. This is textbook illustration plus unexplained enumeration: certification alone does not rescue an arbitrary object. Honest panel-only limitation is respected but does not create value. Intrinsic low value / arbitrary scope => FAIL, not a presentational gap.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Panel-only (7 explicit polytopes); no claim over the full 4319 KS classification. Theory (Prop 2.2, Thm 4.2/2.21, Cor 3.3, Ex 2.16) credited to Nill math/0407491. Barycenters are Euclidean volume centroids per Nill Def 4.1.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
