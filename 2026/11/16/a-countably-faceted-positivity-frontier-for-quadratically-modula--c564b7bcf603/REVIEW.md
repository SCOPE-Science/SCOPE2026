# Mathematical assessment: A countably faceted positivity frontier for quadratically modulated circle heat kernels

## Correctness — PASS
The exact Fourier coefficient is \(q^{k^2}F(\cosh(2\tau k))\), where \(F(y)=2\beta q^4y^2+\alpha qy+1-\beta q^4\). The compact-circle Fourier positivity criterion and leading-coefficient sign reduce the problem to a discrete quadratic envelope. At each proposed vertex the polynomial factors into two adjacent mesh roots and is nonnegative at every sampled mesh point. Segments and terminal ray exhaust the exact convex parameter region. The cusp follows by minimizing a two-term expression on each facet and evaluating its endpoints, yielding distinct liminf and limsup. A consecutive-frequency Vandermonde argument establishes finite-site strictness and missing Fourier modes characterize non-universality. `CHECK.py` supplies reproducible exact-rational finite checks; the general claims are proved in RESULT.md.

## Originality — PASS relative to checked evidence
Arhancet and Li, arXiv:2603.00276 (first public 2026-02-27), provide broad Fourier-positive convex geometry, not the stated theta-kernel section. The fully inspected published theorem https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-circle-covariance-modulation-threshold-and-an-unbounded-fo--3df14ed06eed concerns one signed cosine on a geodesic exponential circle kernel, with rational rather than Gaussian Fourier spectrum. The published result https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-two-harmonic-circle-exponentials-the-sharp-positive-type-cone-an--8f4e14149944 handles exponential-of-two-cosines profiles and a nonnegative-quadrant cone, not a signed quadratic multiplier of a heat kernel. Formula-by-formula comparisons show neither statement implies the countably exposed vertices or cusp constants here. Older specialist theta/Toeplitz covariance literature remains a priority risk and searching does not prove uniqueness.

## Mathematical value — PASS
The two-harmonic multiplier is a natural signed polynomial perturbation of the wrapped Gaussian heat kernel. Its complete positivity region has infinitely many facets and a nonconvergent normalized cusp, both intrinsic geometric properties rather than arbitrary parameter slices. The contrast between strict positive definiteness and universality on spectral boundaries is relevant to covariance and approximation theory. The infinite classification is motivated directly by the Fourier support geometry.

## Limitations and validation
The scope is the circle, positive heat time and exactly two cosine harmonics; no arbitrary torus or higher sphere analog is claimed. The reproducibility script checks finite rational samples, not the proof of the infinite cases. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
