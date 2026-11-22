# Scientific review: signed two-scale circular tent covariances

## Correctness (PASS)

The theorem gives a complete iff criterion for all \(0<b<a\le\pi\) and every \(\lambda\ge0\). Direct integration produces the exact Fourier coefficients \(\widehat T_a(n)\). If \(a/(2\pi)\) is rational, the zeros at every multiple of its denominator impose an exact finite-order divisibility obstruction and reduce the sharp bound to one finite residue maximum. If \(a/(2\pi)\) is irrational, bounded quotient of the sinc factors extends the dense cyclic map \(e^{ina}\mapsto e^{inb}\) to a continuous circle character; its integer winding gives necessity. The geometric-series inequality and density prove the exact constant. Summing nonzero Fourier inequalities proves the zero Fourier mode never intervenes. A Vandermonde argument proves irrational strictness; an explicit alternating vector proves rational failure of strictness. The continuity claims follow from bounded-winding compactness. All steps apply to infinitely many modes, not just checked frequencies.

The analytic proof and numerical checks are separate. The supplemental checker passed 84,177 diagnostics on rational and irrational parameter families, including a symbolic identity and Gram-null vectors. Its floating-point tests are not used for either the character theorem or mathematical exhaustive statements beyond the finite loops explicitly performed.

## Originality (PASS, best-knowledge with residual risk)

Babenko–Kryakin–Staszak (2013, §§2–3) already establish the same normalized tent and its sinc-squared Fourier coefficients, and analyze alternating multi-scale signed tents in a different approximation-theoretic context. In particular, neither the elementary Fourier expression nor the existence of signed tent sums is new. Their results give no iff criterion in terms of a cyclic subgroup of the circle, no exact maximal positive subtraction weight for every pair of radii, and no rational/irrational rigidity comparison.

Emery–Alegría (arXiv:2101.09558, Sections 1–5 and Appendix A) studies truncated-power Euclidean covariance families and range-dependent multivariate sufficiency conditions, not a complete characterization of signed differences on the continuous geodesic circle. Buhmann–Jäger (arXiv:2105.02586, §§4–5) supplies broad spectral support and strict-positive-definiteness criteria on spheres. The present exact two-range Fourier domination and arithmetic topology are not simply equivalent to those positive-support tests: they decide when a fixed *negative* component is dominated across **all** modes and identify the sharp coefficient.

Novelty is assessed against these inspected primary sources and targeted literature comparisons rather than inferred from searches failing to return a match. Earlier periodic-spline, Fourier multiplier-order or covariance-dilation literature might contain a disguised equivalent; independently certified priority is not asserted.

## Value (PASS)

A positive signed subtraction of compactly supported covariance kernels is a natural covariance-shaping problem: it can remove short-range correlation while retaining positive semidefiniteness. The answer is unexpectedly arithmetic, with almost every narrower width forbidden at an irrational base, dense admissible exceptions, exact sharp weights, and a qualitative change in finite-sample strictness between rational and irrational bases. Both the countable-dense law and the exact finite rational test describe structural limitations of this operation, not arbitrary numerical examples.

## Limitations and closest literature

The result is for the linear tent on \(\mathbb T\), two scales, nonnegative subtraction weight, and all finite circle samples. It makes no higher-dimensional, multi-subtraction, smoothness-preservation, or numerical-conditioning claim. It is not asserted to supersede the classical sinc-squared transform, or the general Schoenberg/Fourier positivity theorem. The closest directly overlapping primary source is Babenko–Kryakin–Staszak (2013); Emery–Alegría (2021) motivates the compact covariance setting. Historical priority is best-knowledge only.

Self-review: passed. Independent audit: not yet performed.
