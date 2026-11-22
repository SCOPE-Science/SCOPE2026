# Scientific review

## Correctness — PASS
The claimed supremum is reconstructed on the quotient of real paths by constants. The derivative of the proximal map is computed explicitly on each side of the centered shrinkage sphere. The path-variation rank-one norm reduces to finite cuts and dual sign vectors; the rank-two Rayleigh identity is proved and the exact alternating-sign and midpoint-cut optimizers are exhibited. Near-threshold two-input witnesses show sharpness. Nonattainment for more than two samples is proved by the strict subcritical derivative coefficient along any fixed nonconstant segment. The included executable checker exhaustively validates the formula to nine sites and tests perturbations; these checks are supplementary, not the all-dimensional proof.

## Originality — PASS, qualified
The original group lasso article (Yuan–Lin, first public 2005-12-21) and the accessible broad review (Huang–Breheny–Ma, 2012) contain the shrinkage context but not the path-variation norm. The closest fully inspected sharp cross-norm result for radial retractions calculates weighted coordinate norms for a mathematically different map. Other indexed and accessible prior results concern different projections or coordinatewise shrinkage. A statement-level comparison found no dominating implication or exact prior table. Residual risk: an older, unindexed treatment of centered radial thresholding in a BV quotient could already derive this formula, and full historical priority is not established.

## Mathematical value — PASS
Group soft shrinkage is a natural nonlinearity for structured signal denoising. Its Euclidean nonexpansivity and one-input variation diminution do not answer how a perturbation's variation propagates. The exact formula reveals unexpected amplification growing linearly with sample size, identifies the first expansive dimension, shows that the threshold parameter does not mitigate worst-case amplification, and supplies explicit near-threshold witnesses. This is a motivated sharp stability invariant rather than a routine unmotivated finite example.

## Scope and remaining limitations
Only real uniform paths with one centered Euclidean block and positive common threshold are covered; no weighted graph, irregular mesh, overlapping groups or nonlinear extension is claimed. The maximum is nonattained for dimensions at least three. Computations are finite corroboration; historical novelty is qualified.

Self-review: passed. Independent audit: not yet performed.
