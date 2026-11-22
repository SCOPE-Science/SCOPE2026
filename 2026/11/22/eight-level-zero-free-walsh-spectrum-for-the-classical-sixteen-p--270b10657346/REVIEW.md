# Self-review

**Claim assessed:** the exact eight-level signed Walsh spectrum of all 140 affine two-flats on sixteen points, its zero-free convolution and the unique inverse endpoint norm \(3617/840\). The package makes no higher-dimensional theorem claim.

## Correctness — PASS

The affine-part reduction is exact; the 64 quadratic types split by alternating rank (1, 35, 28), the fifteen nonzero cubic types each split by a line direction lying in or outside a polar radical (8, 56), and the quartic point-indicator halves the quadratic spectrum after translation. All 2,048 classes have a structural evaluation and each represents 32 signings. A standalone two-construction, full-size integer Walsh verifier independently enumerates all 65,536 multipliers and establishes the full reciprocal kernel table and norm. The inverse calculation is finite and exhaustive, not a sampling-based extrapolation.

## Originality — PASS under bounded comparison

The exact 140 blocks and parallel classes are known in de Vries (2008); the complete sixteen-point SQS census is known in Kaski–Östergård–Pottonen (2006); Pavone (2023) studies the same design's subdesign decomposition; Reed–Muller and coding sources provide polynomial/weight facts. None of the inspected material establishes the exact signed spectrum or inverse norm. Searches checked synonymous affine-plane, Boolean Steiner quadruple, Reed–Muller minimum-word shell, and Cayley-adjacency formulations. The strongest residual risk is an unindexed association-scheme spectral computation equivalent to the table; search absence does not prove historical uniqueness.

## Value — PASS

The canonical affine SQS point-coloring model supplies a natural exact invertibility problem and a quantitative full-signal recovery benchmark. All point-sign assignments are classified structurally into just eight eigenvalues, and the exact nontrivial inverse norm quantifies amplification. This is meaningful finite-design information beyond the well-known block-count and code-word weight enumerator; no broader theorem or application is assumed.

## Limits and references

The calculation concerns exactly sixteen points; the analytic multiplier proof does not automatically extend to larger dimensions. The inverse coefficient table is certified by complete integer calculation and should be independently checked before publication. Sources: https://doi.org/10.1007/s10623-008-9207-5 ; https://pottonen.kapsi.fi/sqs16.pdf ; https://doi.org/10.1016/j.ffa.2023.102277 ; https://arxiv.org/abs/0910.0641 ; https://people.math.harvard.edu/~elkies/M256.13/index.html .

Self-review: passed. Independent audit: not yet performed.
