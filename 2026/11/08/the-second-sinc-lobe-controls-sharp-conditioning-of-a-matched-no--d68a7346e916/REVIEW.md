# Scientific review

**Correctness (PASS).** The continuous box-kernel symbol follows by a direct Fourier integral. The derivative numerator and its next two derivatives were checked symbolically; sign convexity proves unique extrema on the relevant lobes. A verified interval grid with global derivative bounds excludes every competing frequency, and exact rounded signs bracket the roots. The attached checker reproduces the strict margins, notably the separation between the first and second positive-sine lobes.

**Originality (PASS, scoped).** The source additive-preconditioning theorem gives uniform spectral bounds for a broad discrete problem, not the exact optimized global frequencies for the calibrated one-dimensional box-kernel Fourier symbol. The nearest 2026 two-level Toeplitz preconditioner concerns a different matrix/preconditioner pair; its reported finite interval is not an implication for these sinc-specific continuous extrema. Explicit searches for the exact multiplier, second-lobe phenomenon and numeric constant, as well as available prior mathematical-record and historical-claim comparisons, did not identify direct coverage. Nonindexed equivalent trigonometric-extremum calculations remain possible.

**Value (PASS).** This is a natural, completely specified kernel and preconditioner from the robust nonlocal setting. An exact spectral-equivalence benchmark is useful for validating symbolic discretizations, mesh-resolution studies and Fourier-mode tests. The unexpected second-lobe worst mode matters because first-lobe-only verification would miss the true minimum. The result makes no claim of improvement to the existing preconditioner or of universality across kernel shapes.

**Closest literature and limits.** Lu et al., arXiv:2609.24143 (primary full HTML inspected, Sections 2-3 and experiments); Zhang et al., J. Sci. Comput. 106 (2026) 21 (bibliographic and abstract material inspected only; full primary text not verified). The spectral constant applies to the whole-line frequency continuum, not a boundary-conditioned FEM matrix. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
