# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Comeager unique ergodicity and smooth conjugacy for rank-3 Vershik systems
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1088
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Descriptive Set Theory
- **Method:** Hjorth turbulence and Baire-category generic ergodicity arguments

## Problem

In the Polish space of essentially simple ordered Bratteli diagrams of rank at most 3 with Vershik minimal homeomorphisms, is the uniquely ergodic locus with good full-support invariant measures a dense G-delta comeager set on which topological conjugacy is smooth via the Borel trace invariant on a fixed clopen partition?

## Attempted claim

In the Polish space of simple ordered Bratteli diagrams of rank at most 3 with Vershik minimal homeomorphisms, the systems that are uniquely ergodic with a good full-support invariant measure form a dense G-delta comeager set, and topological conjugacy restricted to this comeager set is smooth, classified by the Borel trace value on a fixed clopen partition.

## Research outcome

Disproved the rank-3 comeager trace-smoothness target with an explicit uniform-trace non-conjugate pair: stationary X and one-head-nonstationary Y, both uniquely ergodic with good full-support measures, identical (1/3,1/3,1/3) trace, K0xQ dimensions 3 vs 2. Exact script verifies 30/30 checks.

## Why this attempt failed

Failed axes: correctness.

correctness: Replayed exact arithmetic: M1 det 4 rank 3 charpoly (6,9,4), A det 0 rank 2 charpoly (2,-8,0), heights 4^(n-1)(1,1,1), flow consistency and tower mass 1/3, simplicity via A*M1 and M1*A strictly positive, and proper max/min uniqueness for the one-head Y all check (30/30 ALL_OK). Unique ergodicity and Akin-goodness from uniform cylinder mass (1/3)/4^{n-1} are correctly proved. Trace collision (1/3,1/3,1/3) at every level is correct. The essential non-conjugacy inference is false: K0 is a direct limit, tail maps M1 are isomorphisms over Q (det 4), so colimit of Q^3 --A--> Q^3 --M1--> ... is isomorphic to Q^3 (map V2->colimit is iso by tail invertibility), not Q^2. Rank(A*M1)=2 is head rank, not eventual rank. Hence K0(X)xQ and K0(Y)xQ are both Q^3 (dim 3 vs 3), the stated 3-vs-2 distinction collapses, and non-conjugacy is unproved. Same tail implies same rational limit and same order-unit image (4,4,4), so GPS Q-dimension cannot separate this pair.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The refutation defeats the smoothness-by-trace half (hence the conjunction) and does not decide whether the uniquely-ergodic good-measure locus is comeager. Completeness is the defeated component; Borelness of the trace and of the relation are not disputed. Simplicity/properness/minimality and the K0 conjugacy invariant rely on the cited classical Herman-Putnam-Skau and Giordano-Putnam-Skau theorems; the colliding pair itself is new and explicit.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
