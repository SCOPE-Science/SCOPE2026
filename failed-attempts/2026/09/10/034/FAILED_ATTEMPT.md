# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** STS-family stability-cleaning fragment for near-complete linear Fano-free 3-graphs
- **Round:** 2026-09-07-first-light-01
- **Lane:** 575
- **Disposition:** NO_RESULT
- **Domain:** Extremal Combinatorics
- **Method:** Razborov flag-algebra semidefinite method with STS-family stability cleaning, plus certified small-order census as base case

## Problem

In the cell of linear 3-uniform hypergraphs forbidding the Fano plane, whose extremal density is 1 (attained by Fano-free Steiner triple systems), prove an STS-family stability-cleaning fragment: every near-complete linear Fano-free host is within small symmetric-difference edit distance of some (host-dependent) Steiner triple system on the same vertex set, via one replayable linear-flag SDP inequality plus one cleaning deletion step; and certify the exact minimal-order (n=9) near-extremal stability radius as ground truth.

## Attempted claim

For every admissible n ≡ 1 or 3 (mod 6) with n ≥ 1000, every linear Fano-free 3-uniform hypergraph G on n vertices with at least n(n-1)/6 − 10^{−4}·n² edges has symmetric-difference edit distance at most 0.02·n² to some Steiner triple system STS(n) on the same vertex set (host-dependent nearest STS, not a fixed template), proved by a replayable linear-flag SDP inequality bounding the density of a named STS-incompletable flag family plus a one-step cleaning deletion within the stated budget and a dense-partial-STS completion check.

## Research outcome

Target BLOCKED (no SDP stack, no flag inequality, no completion citation; SCOPE016 checked and compatible, not a disproof). Preset fallback ATTEMPTED_AND_BLOCKED (E*_9=12 + k=12/k=11 bands closed analytically, k=10 band and binary two-pipeline byte-replay not closable: ~15.4h projected vs ~15 min left). No original increment. Honest NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No cvxpy/scipy/networkx/nauty in-pass; SDP and canonical-labeling routes unrunnable at required scale', 'k=10 near-extremal band (E*_9-2 slice) not enumerated; d*_9 not pinned', 'AG(2,3)/E*=12 re-verifications reproduce admission record, not new results']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No cvxpy/scipy/networkx/nauty in-pass; SDP and canonical-labeling routes unrunnable at required scale', 'k=10 near-extremal band (E*_9-2 slice) not enumerated; d*_9 not pinned', 'AG(2,3)/E*=12 re-verifications reproduce admission record, not new results']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
