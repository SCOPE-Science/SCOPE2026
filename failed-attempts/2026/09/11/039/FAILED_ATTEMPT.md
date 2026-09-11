# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Ratio-4 far witness: Fano-free family with 0.005 defect and 0.02 edit distance
- **Round:** 2026-09-07-first-light-01
- **Lane:** 784
- **Disposition:** NO_RESULT
- **Domain:** Extremal Combinatorics
- **Method:** explicit extremal construction with blow-up/unbalanced-partition design plus regularity-compatible verification

## Problem

Exhibit an explicit infinite family H_n of Fano-free 3-uniform hypergraphs (unbalanced bipartition plus a fixed Fano-free internal pattern on one side, or balanced blow-up of a fixed <= 10-vertex Fano-free base) such that b(n)-e(H_n) <= 0.005*n^3 and min_{bipartite-type B} |E(H_n) Delta E(B)| >= 0.02*n^3, i.e., edit-to-defect ratio >= 4, with Fano-freeness proved by a finite base check plus a preservation lemma.

## Attempted claim

There exists an explicit infinite Fano-free family H_n with edge defect at most 0.005 n^3 below b(n) and edit distance at least 0.02 n^3 from every complete bipartite-type 3-graph, forcing any linear Fano stability inequality to have slope at least 4.

## Research outcome

Target BLOCKED: balanced blow-up arithmetically impossible for every base on <=10 vertices; unbalanced-plus-internal designs are Fano-free only at distance 0 (ratio 0) and contain Fano whenever distance>0, with repair cost >=2 deletions per internal edge capping the rate at ~1. The only named adjacent partial (ratio>=2.5 / base-plus-count) was concretely attempted (output/artifacts/fallback_attempt.py, log fallback_attempt.log: 0/8 Fano-free single-edge augmentations, 0 Fano-free 2-deletion repairs, base-density fails for all Fano-free m<=10) and blocked. Clean exit, NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Finite verification is at n=8,9 (exhaustive) plus closed-form density arithmetic for m<=10; no asymptotic third-family claim is made.', 'No emergent finding is claimed: the firewall count is elementary arithmetic and the n=8 census is a routine finite byproduct.', 'Fallback attempt bounded to the named adjacent partial (ratio>=2.5 single-exchange neighborhood at n=8; base-density check m<=10); no out-of-scope third family was invented.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Finite verification is at n=8,9 (exhaustive) plus closed-form density arithmetic for m<=10; no asymptotic third-family claim is made.', 'No emergent finding is claimed: the firewall count is elementary arithmetic and the n=8 census is a routine finite byproduct.', 'Fallback attempt bounded to the named adjacent partial (ratio>=2.5 single-exchange neighborhood at n=8; base-density check m<=10); no out-of-scope third family was invented.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
