# Scientific review: mixed Poisson Fourier kernels

## Correctness — PASS

For each positive pair of scales and interior weight, the explicit second derivative reduces every real root to the level equation \(R_t(u)=W\) on \(1/3<u<t/3\); outside this interval its sign is fixed. The quotient-rule derivative factors into a strictly positive factor and the quadratic \(5u^2-(t+1)u+t\). Its discriminant becomes positive exactly for \(t>9+4\sqrt5\). The ordered critical levels then give the complete one-, two-, or three-positive-root census, with multiplicities at the boundaries; positive roots mirror to real roots. The rational quartic witness, three bracketing intervals, and Descartes bound are independently checked in check.py. The proof is analytic for all parameters; computational comparisons are not extrapolated.

## Originality — PASS relative to checked sources

The October 1, 2026 paper by Kwaśnicki studies representations of bell-shaped kernels using elliptic diffusion, while Kwaśnicki's January 2025 paper proves bell shape of individual Poisson kernels of a specified operator class. A convex **arithmetic average of distinct heights** is not asserted by either theorem to belong to that operator class; neither gives the exact second-derivative threshold or the weight chamber. Došlá (2009) gives conditions for *multiple modes* in mixtures of different-location densities, including Cauchy families, not curvature counts for a common center. The wider Kwaśnicki–Simon characterization was read at abstract level only and presents residual risk. Searches of published results returned a Cauchy-mixture quadrature paper and a distinct Cauchy-wavelet cusp paper, but no implication of this level-set discrimination. Searches cannot prove global priority. An older equivalent curvature calculation may remain undiscovered.

## Value — PASS

The Fourier multipliers \(w e^{-a|\xi|}+(1-w)e^{-b|\xi|}\) are natural positive blends of Poisson semigroup filters. A single Poisson kernel has exactly two curvature sign changes; even though every positive blend stays strictly unimodal, the exact criterion \(b/a>2+\sqrt5\) marks when it can have six, and the entire transition-weight chamber and multiplicity boundaries are classified. This identifies a sharp structural failure of curvature simplicity in a natural infinite two-parameter family, rather than a single counterexample or a routine reparameterization. It is limited to second derivatives, not full bell shape.

## Closest literature and limits

Kwaśnicki, *Bell-shaped functions are Poisson kernels*, arXiv:2610.01717 (2026-10-01); Kwaśnicki, *Poisson kernels on the half-plane are bell-shaped*, arXiv:2501.16068 (2025-01-27); Došlá, *Conditions for bimodality and multimodality of a mixture of two unimodal densities*, *Kybernetika* 45 (2009) 279–292; Kwaśnicki and Simon, *Characterisation of the class of bell-shaped functions*, arXiv:1910.07752 (2019-10-17). The latter abstract was inspected but not the entire primary text; another unindexed direct Cauchy-mixture curvature theorem could subsume the result. No assertion of independent audit or global uniqueness is made.

Self-review: passed. Independent audit: not yet performed.
