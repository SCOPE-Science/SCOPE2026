# Scientific review

## Correctness — PASS

The object is an explicitly specified real-analytic, strictly positive-definite translation-invariant kernel, with top eigenvalues \(2,1,1\) and a gap to the next eigenvalue \(1/2\). Positive definiteness follows from positive Fourier coefficients and a finite Vandermonde test. The RKHS projector is defined explicitly, and both designs have \(m\) distinct sites and tight leading-mode sampling matrices. A unit RKHS vector orthogonal to all regular-grid kernel translates forces loss \(\ge1/3\). For each of the three target modes, a displayed finite combination of staggered-grid translates cancels the two resonant Fourier spikes and interpolates the top Fourier coordinates exactly; the summed residual has the proved \((5/2)\varepsilon(1-2^{1-m})\) upper bound. This is an all-even-\(m\) analytic proof, not an inference from finite tests. The independent finite Gram evaluation checked 16 parameter configurations. Scope: no global optimality claim for the competitor and no finite-precision guarantee.

## Originality — PASS, with historical-priority caveat

Schreiber, arXiv:2611.20336v1 (16 November 2026), §4.3, expressly distinguishes tight-frame sampling quality from spectral alignment for \(m>s\), with a spherical nonoptimality example. Its circle aliasing theorem §4.5 is for periodic Gaussian coefficients, and its reported equispaced behavior concerns that family. It does not state the present analytically positive-definite circle counterexample with an arbitrary loss factor, and its conclusions do not imply a uniform equispaced optimum for all positive Fourier spectra. Wind-Andersen, arXiv:2611.02379v1, analyzes different Fourier sampling Gram perturbation and compensation criteria, not this nonlinear RKHS projector objective. Semantic comparisons with related kernel-landmark, sampled Fourier, and tight-frame results found distinct objects or metrics. A general identity might make the construction conceptually accessible to experts; broad historical nonoccurrence cannot be certified by finite searching.

## Value — PASS

This explicit obstruction answers a practically relevant question suggested by the emerging spectral-landmark criterion: whether equal spacing and tight leading-mode sampling suffice for good RKHS eigenspace capture on a homogeneous circle. It separates spectral-aliasing quality from finite-dimensional frame conditioning even when both leading-mode frames are **equally tight**, with an arbitrarily large loss gap. It provides a mathematical warning against using only leading-eigenfunction tightness to choose landmarks when the kernel has an off-band spectral spike. The nonmonotone kernel is contrived but is analytic, strictly positive definite, has a top-three gap, and admits closed-form tests, making the limitation substantive rather than a normalization artifact.

## Closest sources and remaining limits

- J. Schreiber, *Spectral Landmarks*, arXiv:2611.20336v1 (full HTML inspected, especially §§3–4.5, 7 and Appendix A).
- E. Wind-Andersen, *Alias Geometry and Density Compensation in Perturbed Fourier Sampling*, arXiv:2611.02379v1 (full manuscript text, introduction and alias theory inspected).
- Classical Fourier aliasing and multi-coset sampling provide a mechanism but were not used as a claimed novelty.

Neither global optimality of the staggered design nor numerical-conditioning performance follows. A later or unindexed equivalent construction remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
