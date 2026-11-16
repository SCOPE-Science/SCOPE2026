# Scientific review

## Correctness — PASS
For every \(N\ge6\), the active-row count and Fourier-zero bound reduce the problem to a sharp cyclic interval expansion. The small boundary case \(N=6\) is handled separately; it cannot be inferred from a coarse asymptotic bound. For two-site signals, the exact two-overlap-row calculation gives two cosets that are identical exactly when the tap curvature lies in \(\mu_N\), proving the full equality and forbidden-gap statements. A five-cycle counterexample confirms the sharpness of the dimension restriction. Exact cyclotomic computations and an exhaustive finite support-bound check independently support the symbolic identities; neither is used as an infinite proof.

## Originality — PASS, with residual historical priority risk
Nicola's original 2022 result identifies all transforms attaining universal support \(N\), not the second support of a fixed three-tap window. Krahmer–Pfander–Rashkov give the *known* prime two-by-three support lower bound \(4N-2\), but do not give the sharp curvature-determined attainability/nonattainability split, the full minimizer class, or the arbitrary-signal composite-order cutoff. The nearest three publicly accessible focused results respectively concern two-tap windows, two-by-two sparse pairs, and phase-only three-by-three pairs; their full statements do not imply this theorem. A differently formulated or unindexed earlier equivalent calculation remains a risk.

## Value — PASS
The first nontrivial support threshold and its extremal classification are natural invariants of finite STFT uncertainty for a fixed short window. The dichotomy says exactly when the strong two-frequency cancellation allowed by an adjacent two-site signal can occur simultaneously, without an equal-modulus assumption, and excludes *all* larger signal supports from near-minimal levels. The sharp six-cycle cutoff and exact forbidden support level materially strengthen a mere numerical support bound. No noise-stability or approximate-recovery guarantee is claimed.

Self-review: passed. Independent audit: not yet performed.
