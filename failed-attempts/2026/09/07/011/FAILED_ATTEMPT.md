# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Closing one Jones-collision class among alternating 12-crossing knots and 11-crossing 2-component links with HOMFLY-PT and interval-certified volumes
- **Round:** 2026-09-07-first-light-01
- **Lane:** 7
- **Disposition:** NO_RESULT
- **Domain:** Topology
- **Method:** polynomial invariant computation with certified hyperbolic volume enclosures

## Problem

In the universe U = prime alternating knots with crossing number <=12 plus prime alternating 2-component links with total crossing number <=11, canonically enumerated by Hoste-Thistlethwaite DT codes (frozen list), recompute exact Jones polynomials, identify Jones-collision classes (exact equality), and for the lexicographically first collision class containing a non-mutant pair, decide separation by exact HOMFLY-PT inequality and/or disjoint interval-certified hyperbolic volume enclosures.

## Attempted claim

There exists an explicitly named Jones-equal non-mutant pair (DT1, DT2) in U, belonging to the lexicographically first closable Jones-collision class, such that either (a) their exact HOMFLY-PT polynomials differ, or (b) their interval-certified hyperbolic volumes are disjoint closed intervals with positive gap, computed from the frozen DT codes by a recorded script (SageMath/KnotTheory + SnapPy verified mode) rerunnable in minutes; this completes the separation row for that collision class.

## Research outcome

No separable non-mutant Jones-collision pair found. Systematically sampled ~12k braid-closure knots (219 Jones-collision classes) and ~10.7k non-split 2-component braid-closure links (141 classes): every collision class with >=2 alternating/reduced/prime members was uniform in Alexander (knots) or linking number (links), so no HOMFLY separation exists in this sub-universe. Exact pure-Python toolkit validated (literature matches, RII/RIII, 360/360 determinant cross-checks); all data and rerunnable scripts frozen under output/artifacts/.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Sub-universe only: braid-word closures (length <=12, <=6 strands). Full alternating <=12/<=11 universe NOT censused; higher-braid-index knots/links uncovered.', 'No interval-certified hyperbolic volumes (no SnapPy/HIKMOT/network); volume branch of separation predicate not attempted.', 'DT codes not cross-checked against SnapPy/Regina/KnotInfo; braid words used instead of canonical HT codes.', 'Per-class Alexander/linking-number uniformity checked on up to 12-16 good members per class; a pair hiding beyond caps in huge duplicate-heavy classes is not rigorously excluded.', 'Mutation screening only via HOMFLY-consequence (Alexander/linking number); no diagram-mutation search performed.', 'Originality: sub-universe Jones data is new in the sense of recomputed/frozen, but no new separable pair or full-U census is claimed.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Sub-universe only: braid-word closures (length <=12, <=6 strands). Full alternating <=12/<=11 universe NOT censused; higher-braid-index knots/links uncovered.', 'No interval-certified hyperbolic volumes (no SnapPy/HIKMOT/network); volume branch of separation predicate not attempted.', 'DT codes not cross-checked against SnapPy/Regina/KnotInfo; braid words used instead of canonical HT codes.', 'Per-class Alexander/linking-number uniformity checked on up to 12-16 good members per class; a pair…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
