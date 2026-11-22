# Scientific review: sharp five-node heat-stencil positivity restoration

## Correctness — PASS

The exact five-by-five stencil equals \(D-D^2/12\) and has eigenvalues \(0,-\alpha,-\alpha,-\beta,-\beta\) with the specified exact radicals. The Fourier inversion has exactly three orbit entries; all diagonal and nearest-neighbor entries are strictly positive for every positive time. For the distance-two entry, the derivative is a difference of two exponentials with strictly ordered decay exponents, so it has one negative-to-positive change of sign. Since the entry begins at zero with negative derivative and tends to \(1/5\), it crosses zero exactly once at the claimed positive threshold. The resulting complete entrywise classification is fully proved for every real time, not extrapolated from finite samples. The delivered symbolic/numeric verifier independently passed its exact projectors and 7,260 high-precision comparisons. Risk: none detected in the five-node assumptions; finite tests are supporting checks only.

## Originality — PASS, provisional

A directly relevant full published finite-range signed-stencil analysis [4] studies precisely the same classical operator and gives finite-periodic *eventual* positivity and nonsharp dimension-dependent bounds; its text explicitly leaves sharp finite-cycle horizons undetermined. Its conclusions do not supply either the unique exact five-node transition or the complete ten-entry sign law. A separate published backward-Euler lattice-resolvent classification [5] concerns a different functional calculus and therefore does not entail the exponential semigroup threshold. General eventual-positivity principles [2], inverse-positive elliptic discretizations [3], and the different Gauss--Lobatto high-order positivity scheme [1] likewise do not determine the full sign law. Exact and alias searches did not identify a matching theorem, but an older equivalent specialized calculation remains a concrete priority risk. Published record partitioning or absence of a keyword match is not itself evidence of novelty.

## Value — PASS

Five nodes are the first periodic grid where all five shifts of this classical fourth-order stencil represent distinct points. The exact restoration threshold is therefore a natural first full-stencil benchmark, not an arbitrary parameter slice. The sharp classification separates semigroup energy stability and mass conservation from the discrete maximum principle, supplies a reproducible sign-onset/recovery test for implementations, and resolves a finite-size value unprovided by the closest asymptotic/sufficiency literature. The finding is intentionally narrow: it does not derive a new general mesh-size law, nor does it claim an improvement in convergence accuracy.

## Closest literature and limits

Relevant material read: Hu--Zhang Sections 2/3.5 [1]; Chen et al. Section VI [2]; Cross--Zhang Section 2.2 [3]; full accessible scientific findings in [4] and [5]. Remaining historical risk: older periodic fourth-order finite-difference heat literature might contain this \(n=5\) specialization without the exact wording. Independent audit and historical-priority confirmation have not been performed.

Self-review: passed. Independent audit: not yet performed.

## References

1. https://arxiv.org/html/2103.16790v2
2. https://arxiv.org/html/2009.03581v1
3. https://arxiv.org/html/2010.07282v3
4. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-negative-outer-jumps-force-persistent-lattice-sign-oscillation-a--904e3c4eba47
5. https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-one-third-is-the-sharp-positivity-recovery-threshold-for-backwar--f6b8d51838a7
