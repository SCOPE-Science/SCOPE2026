# Scientific review: two-coset conditioning on separated unit intervals

## Correctness — PASS

The precise setting is two disjoint *unit* intervals with separation \(d=m+\delta>1\), \(0<\delta<1\), and all frequencies in \(\mathbb Z\cup(\mathbb Z+\tau)\). The two intervals are projected to their common fractional coordinate. Their integer lifts are \(m\) and \(m+1\) on two sets of positive measure, so Parseval reduces the full synthesis operator to exactly two types of two-by-two matrices. The squared singular values of either matrix are \(2\pm2|\cos(\pi n\tau)|\). The essential infimum and supremum give sharp bounds and a pointwise inverse proves completeness. The two-phase minimax has unique optimal fractional shifts \(\pm1/(2m+1)\); its proof checks both possibilities for the integer difference between the nearest half-integers. The integer-separation case uses only a single fiber, explaining the discontinuity. Exact finite integrals and numerical fiber checks from the included checker independently support these identities, but the universal theorem does not depend on finite enumeration.

## Originality — PASS relative to inspected evidence

Zhou (2026, arXiv:2610.33987v1, Corollary 2.7) characterizes **orthonormal** spectrality for interval convolutions and implies that noninteger two-point shifts cannot yield an exponential orthonormal basis; it does not give the sharp nonorthogonal two-coset Riesz profile. Frederick–Okoudjou (2021) and Kolountzakis (2015) supply the general multi-tile fiber/Vandermonde machinery, which is acknowledged as prior work and directly motivates the calculation, but their cited constructions do not by themselves evaluate the arithmetic minimax for consecutive integer lifts. Belov–Mironov (2022/2024) and Caragea–Lee (2021/2022) address Riesz basis existence/complementation on unions of intervals, without an inspected matching two-coset optimal-shift theorem. Search comparisons against mathematical research records found nearby results on explicit nonsharp union bounds and finite two-point Riesz geometry, but no statement implying this exact continuum, noninteger-gap optimum. Some older specialist literature could still contain an equivalent calculation; priority requires independent verification.

## Mathematical value — PASS

The two-coset problem is a natural, explicitly reconstructible family in the gap between spectrality (orthogonality) and general Riesz basis existence. The theorem identifies the **best** possible frame conditioning in this family, proves the complete optimizer classification, and reveals the unexpected independence from the fractional length of the gap. The discontinuity when the gap becomes an integer is a sharp boundary phenomenon: arbitrarily small positive-measure fibers enforce a fixed stability penalty. This is quantitative structural information, not merely restating general Riesz existence.

## Limitations and residual checks

The optimization is not global over all exponential Riesz bases. Values concern the ratio of squared Riesz bounds; the synthesis operator condition number is its square root. No claim concerns unequal interval lengths, overlaps, or spectral perturbation estimates under a topology weaker than essential supremum. The general multi-tile literature may contain an unindexed special-case calculation. Independent audit and publication-priority confirmation have not been performed.

Self-review: passed. Independent audit: not yet performed.
