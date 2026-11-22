# Independent mathematical audit

## correctness

PASS

The unitary DFT on each of two m-point sampling banks decomposes the 2m-by-2m complex measurement into exactly m independent 2-by-2 blocks with trace 2+t²(1-2u) and Gram determinant t²(1-4u sin²(pi alpha)), u=(k/m)(1-k/m). The u=0 block bounds condition below by 1+sqrt(2), uniquely minimizing gain at t²=2. At that gain, evaluating the Gram characteristic polynomial at 2±sqrt2 establishes the full shift plateau sin²(pi alpha)≤1-1/sqrt2 and flat lower squared singular-value band at equality. Monotonicity of the lower root in u above the plateau gives the exact all-shift formula with u_m=floor(m²/4)/m². Determinant vanishes only for even m and half-grid shift; for odd m at half-grid, minimum squared singular value ∼2/(3m²), giving sharp linear condition growth. The m=1 exceptional all-shift case is explicit. Direct independently constructed complex matrices at m=1,2,3,4,7,16 and representative phase shifts matched the fiber eigenvalues.

## originality

PASS

A concrete, global minimax derivative-gain and phase-staggering plateau in confluent Fourier interpolation, plus complete rank/parity singularity and phase-flat lower band, differs from published value-only jitter bounds, generic Fourier–Vandermonde collision estimates and a distinct checkerboard directional-derivative minimax. Numerical equality of the silver-ratio constant does not mean the sampling maps coincide.

## value

PASS

The globally sharp robust staggering interval and its exact phase-flat endpoint identify sensor layouts tolerating derivative-grid shift without any condition penalty, while the odd/even half-step singularity gives a useful sharp reconstruction boundary. This is an independently meaningful numerical sampling design and structural analytic classification, not a relabeling of the checkerboard model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
