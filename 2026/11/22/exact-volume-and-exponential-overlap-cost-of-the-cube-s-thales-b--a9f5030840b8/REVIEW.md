# Scientific review: cubical Thales-ball union volumes

## Correctness — PASS

The ambient union is exactly \(\{x:\|x\|_2^2\le\|x\|_1\}\), because maximization of the ball membership inequality over cube vertices gives the \(\ell_1\) norm. Spherical polar integration and Gaussian radius-direction independence yield a direct coefficient identity from positive half-normal moments. A strictly monotone tilted-index mean has a unique saddle; its positive variance, span-one lattice property, and exponential moments justify the local central limit expansion including the \(d^{-1}\) relative error. The standalone checker reproduces five explicit low-dimensional formulas and the asymptotic ratios at dimensions 16, 32, and 64. No computation is used to infer an infinite theorem.

## Originality — PASS, with priority risk

Pavlík's primary Thales-covering result (arXiv:2611.14277v1) establishes coverage of a polytope and a power-diagram refinement, but does not compute the full Euclidean ambient union volume or its dimension-dependent asymptotic. Zhigljavsky–Noonan (2020) study volume *inside* cubes and other covering-center schemes rather than the *outside-union overhead* of all vertex-to-center diameter balls. Records concerning Thales disks of regular polygons and regular-simplex dilation hierarchies concern different families and invariants. A related polytope-cutout statement concerns product tilings, not an exact union-volume law. Alias and mathematical-implication searches did not identify an equivalent or stronger published formula. The search is not exhaustive and classical overlap-volume literature may contain an equivalent result.

## Mathematical value — PASS

The finding quantifies a natural inefficiency of the canonical, dimension-independent Thales covering construction. It combines a finite exact answer in every dimension with a sharp nontrivial exponential asymptotic, including its polynomial prefactor, answering how much space outside the cube is swept out by its compulsory balls. The growth base separates total ambient volume from the elementary fact that the cube is fully covered. This is neither a renamed covering theorem nor an arbitrary low-dimensional table entry.

## Scope and evidence limitations

This is an exact evaluation of a prescribed arrangement, not an optimal covering theorem. The numerical check is supplementary. The asymptotic is proved by a local central limit theorem under explicit exponential-moment, span-one, and positive-variance assumptions. Historical priority is provisional. Independent mathematical review has not been performed.

Self-review: passed. Independent audit: not yet performed.
