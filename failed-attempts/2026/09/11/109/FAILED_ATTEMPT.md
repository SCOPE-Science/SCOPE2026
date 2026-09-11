# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Tolerance-1 triple Tverberg number for 13 points in R^3
- **Round:** 2026-09-07-first-light-01
- **Lane:** 987
- **Disposition:** NO_RESULT
- **Domain:** Topological Combinatorics
- **Method:** equivariant deleted-join test map with Volovikov-Ozaydin index and constraint method

## Problem

Decide whether every set of 13 distinct points in R^3 admits a partition into three nonempty disjoint parts covering the set that remains intersecting after deletion of any single point. Formally, for X with |X|=13, do there exist A1,A2,A3 partitioning X such that for every x in X, conv(A1\{x}) intersect conv(A2\{x}) intersect conv(A3\{x}) is nonempty?

## Attempted claim

Every set of 13 points in R^3 in general position admits a partition into three disjoint nonempty parts whose convex hulls intersect even after removing any single point of the set; equivalently the S_3-equivariant 1-tolerant deleted-join test map for these parameters admits no zero-avoiding equivariant map.

## Research outcome

Exhaustive 235092-partition tolerance-1 audits of four general-position 13-point sets in R3 (moment curve t=-6..6 plus three random integer cubes) found surviving triple partitions in every case (290/9/32/20 witnesses), with one moment-curve witness exactly certified over the rationals for all 14 deletion systems; no blocker was found but the universal claim remains unproved, so NO_RESULT with CLEAN_EXIT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Float basis-enumeration LP covers only four configurations and cannot discharge the continuum universal quantifier; 2145 partitions of type (9,2,2) per config were conservatively excluded from UNSAT verdicts (empty restricted-basis family due to Caratheodory column-cap limits); the equivariant-index 17-to-13 gap was not closed; no blocker and no universal proof were produced.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Float basis-enumeration LP covers only four configurations and cannot discharge the continuum universal quantifier; 2145 partitions of type (9,2,2) per config were conservatively excluded from UNSAT verdicts (empty restricted-basis family due to Caratheodory column-cap limits); the equivariant-index 17-to-13 gap was not closed; no blocker and no universal proof were produced.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
