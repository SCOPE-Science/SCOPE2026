# Scientific review: Gaussian variation error of Mehler mixtures

## Correctness — PASS

The precise domain is the real one-dimensional class of finite ordinary distributional variation, **not** the Gaussian-BV seminorm. The signed derivative measure represents every admissible function as a constant plus a superposition of half-line jumps. The semigroup law and self-adjointness give an exact three-term squared residual. Bivariate Gaussian tail differentiation yields a normalized derivative which is strictly negative away from the median, using an algebraic correlation-product inequality and strict subadditivity of the error function. This proves the universal sharp norm and uniqueness of the jump location. Equality in the variation integral then forces the derivative measure to be one atom. The semigroup asymptotics follow by valid endpoint expansions. A standalone standard-library checker passed 101 mathematical consistency checks, but these finite checks do not establish the infinite-dimensional claims.

## Originality — PASS (qualified)

The inspected Gaussian BV work of Ambrosio–Da Prato–Pallara proves derivative regularization using a Gaussian-weighted BV measure; the present theorem uses ordinary spatial variation and a sharp Gaussian \(L^2\) identity-residual norm. Mossel–Neeman prove fixed-mass Gaussian noise stability, a different inequality from the two-correlation difference defining the new sharp residual. O'Donnell supplies the historical Sheppard arcsine formula and Mehler identities that are used, not asserted original. The Casarino–Ciatti–Sjögren variation theorem concerns the semigroup time index. Searchable results on Gaussian Hermite coefficient extrema and Poisson-mixture BV residuals have different operators and hypotheses. No checked stronger result implies this whole family and its unique equality classification. An unindexed equivalent or a specialized older Markov approximation theorem remains a real priority risk.

## Value — PASS

The exact result simultaneously handles all positive mixtures, rather than only a single heat time, and converts a sharp approximation problem over all ordinary BV inputs into one rigid Gaussian-median jump. The mixture formula has direct applications to subordinated and randomized smoothing kernels, while its small-time coefficient distinguishes Gaussian OU smoothing from deterministic or circular convolution errors. The combination of all-law sharpness, equality classification and time-scale asymptotics provides a reusable benchmark, not merely a numerical instance or a direct renaming of a standard two-Gaussian probability identity.

## Limitations and priority

The statement does not apply to Gaussian-weighted variation, complex-valued functions, higher-dimensional ordinary BV, signed mixtures or negative correlation. The prior-work comparison does not certify global mathematical novelty. The proof uses established Gaussian quadrant identities and basic variation representation explicitly.

Self-review: passed. Independent audit: not yet performed.
