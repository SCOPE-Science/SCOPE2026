# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Maximal minimal faithful permutation degree among nonabelian groups of orders 32 and 64
- **Round:** 2026-09-07-first-light-01
- **Lane:** 151
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Computational Group Theory
- **Method:** Schreier-Sims base-strong-generating-set computation with core-free subgroup enumeration and coset-action faithfulness certification

## Problem

Survey all finite nonabelian groups G of orders 32 and 64: compute the minimal faithful permutation degree mu(G), the least index sum over subgroups with trivial core intersection, with explicit minimizing core-free families, and certify a maximal-mu witness G* with an integer gap over its same-order competitors.

## Attempted claim

There exists an explicitly presented nonabelian 2-group G* of order N* in {32,64} and an explicit family of core-free subgroups H*_1,...,H*_k with trivial core intersection such that the certified index sum mu(G*) = sum [G*:H*_i] = M* equals the per-order maximum and exceeds mu(G) of every other nonabelian group G of order N* by an explicit integer gap >= 1, verifiable by replay from committed presentations, core computations, and coset-action kernels.

## Research outcome

Certified exact mu(G) table for 29 explicit 2-groups (orders 32/64) with minimizing families, family-relative maxima (32 at C32,Q32; 64 at C64,Q64) and integer gaps (14, 30), plus a reusable stdlib faithful-degree audit pipeline; full SmallGroups-window census explicitly NOT claimed.

## Why this attempt failed

Failed axes: value.

value: FAIL: arbitrary tool-limited fragment with no independently retrievable headline. Promised scope was all nonabelian groups of orders 32 and 64 (51+267 SmallGroups census with per-order maximal witness and integer gap); delivered is 15+14 selected groups (only 8 nonabelian of order 32, 7 nonabelian of order 64), explicitly a benchmark fragment because no GAP/SmallGroups was available. Even the abelian part is incomplete: order-64 abelian types require 11 partitions of 6 but only 7 are present (missing e.g. [16,2,2],[8,4,2],[8,2,2,2],[4,2,2,2,2]). Selection is a convenience sample of easy constructions (cyclics, dihedral-like, direct products, 3 extraspecial extensions), not a group-theoretic natural class motivated before computation. Family-relative maxima/gaps (32 at C32/Q32 gap 14; 64 at C64/Q64 gap 30) are not global results: global maxima mu=|G| at cyclic groups are trivial upper bounds, and next-values 18/34 are only within the fragment. 14/29 values are direct Johnson sums; cyclic/quaternion/dihedral cases are elementary textbook exercises; remaining mixed-product/extraspecial values are narrow data without general criterion, interpretation, or downstream use. The reusable stdlib pipeline is tooling, not a substantive result. The saving clause for exact invariants does not apply: the 29-set is not a natural pre-motivated object, much of the table is mechanically implied, and a future researcher needing mu(2-groups 32/64) would need the complete census or a formula, not this fragment. Honest scope limitation does not create headline value. Defect is intrinsic arbitrary scope plus missing substantive result, not a bounded add-on.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Partial result only: 29-group benchmark subfamily, NOT the full 51+267 SmallGroups census over orders 32/64 (no GAP/SmallGroups available in-lane). Maxima and gaps are claimed only within the surveyed family. Groups identified by committed Cayley tables/presentations, not SmallGroups IDs. No Schreier-Sims BSGS logs (brute-force Cayley-table methods used instead, exhaustive at these orders).

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
