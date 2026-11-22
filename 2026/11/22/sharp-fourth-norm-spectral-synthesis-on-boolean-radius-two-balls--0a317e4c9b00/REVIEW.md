# Review: sharp fourth-norm synthesis on Boolean radius-two balls

## Correctness — PASS

The parity embedding turns the radius-two ball into the origin plus all complete-graph edges. Strict complex convexity of the fourth Walsh moment with the zero-frequency coefficient fixed gives one optimizer; hidden edge-transitive symmetry and conjugation make it a real two-level profile. Character averaging yields the explicit quartic, and its strict convexity gives the unique real cubic root. Counting triangles and four-cycles in the complete graph verifies the exact sign transition. Uniform polynomial moments for Rademacher sums and a coercive moment estimate establish the asymptotic law, not merely a conjectured normal approximation. The included checker passed 214 supplementary exact or numerical checks, and its scope is finite.

## Originality — PASS against the inspected evidence

Iosevich, Li and Yu, arXiv:2609.25404v1 (2026), provide a relevant general synthesis framework and an exact theorem for transitive affine supports whose indicator is an optimizer. A Boolean radius-two Hamming ball has two edge/origin orbits; its optimizing coefficient becomes nonuniform and eventually negative, so their transitive statement does not imply this theorem. Bhowmik, Deodhar and Iosevich, arXiv:2508.12194v1 (2025), give general finite spectral-synthesis bounds rather than this support-specific sharp quartic. Indexed Hamming Turán-mass and Walsh sampling-concentration results solve different optimization problems. The first two primary articles were read in full in available HTML; several indexed records were available only as summaries, which are not enough to declare their full texts noncovering. An older equivalent result remains a literature risk, and no formal uniqueness assertion is made.

## Value — PASS

Boolean Hamming radius-two balls are a canonical Fourier support family; optimizing a synthesis norm over them is motivated independently of finding a favorable finite parameter. The theorem identifies the exact sharp constant and complete complex extremizers for all dimensions, detects the signed-origin transition at dimension five, and proves a Gaussian/chi-square scaling law for large dimensions. These outcomes go substantially beyond a generic spectral-synthesis bound or a finite numerical table.

## Limitations

The proof covers only Boolean groups, Hamming radius two, and the fourth Fourier norm with counting measure. The all-dimensional cubic is implicit but uniquely specified; it is not a universal elementary radical identity. The finite checker independently tests many instances but does not prove the infinite statement. External audit and exhaustive prior-art certification are not claimed.

Self-review: passed. Independent audit: not yet performed.
