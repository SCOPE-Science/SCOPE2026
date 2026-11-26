# Independent mathematical audit

## correctness

PASS

Verified the input length classification against Hamoud's Theorem 2.15, Lemma 3.1 and Corollary 3.3; the first threshold is empty and uniquely removed. For each phase, the shifted threshold is a fixed linear functional of B^q(1,1), including phase r=1, so Cayley–Hamilton with the two specified initial values gives the exact formula. The forward-product convention in this record is the transpose of the one in the cited work (each M is symmetric). The period matrix is primitive, including the one-letter period. Consecutive true gaps, also across block and period boundaries, are positive standard lengths growing as positive constants times λ^q. Thus all dominant gaps and the wrap gap are strict. Since |μ|=1/λ, the stated nearest-integer cutoff is valid; differences from the ideal indicators happen at O(1) integers per phase per period and have finite total harmonic weight. The exact count subtracts one from qS+H; Z=F away from those exceptional cutoffs. For extrema one must use actual thresholds, not discard the exceptional subsequence: Z strictly decreases with N between actual consecutive thresholds, so extremes in each gap occur at its first or last integer. Their phases tend to the appropriate right or left endpoints from the exact spectral asymptotic; the resulting endpoint values also account for wraparound. For the laws, integer Riemann comparison on each exponentially growing annulus works for bounded piecewise continuous g∘F. In the harmonic integral one can shift x+2 to the integration coordinate, with an integrable O(x^(−2)) error in the weight, and each full logarithmic interval contributes the same phase law. The affine branches give the density and mean as written. Ordinary full annuli contribute λ^(−u)/(λ−1); the final partial annulus adds λ^(−u) up to phase u. The limiting densities at phases 1 from below and 0 match almost everywhere, so no missing family member occurs at wraparound. Every phase is approached by integer cutoffs because the spacing tends to zero; M′=(log λ)(F−M) off the finitely many breaks prevents a constant ordinary limiting mean. The normalization S/log λ and c_1 are unchanged under repeating a period, so the actual centered samples and harmonic limit are unchanged. Fibonacci has one branch; for d=2 the Perron coordinate ratio gives c_2/c_1=1+1/√2 and the two branch images overlap nontrivially. Reviewed all frozen support; finite illustrative tests and their logged output are not used as proof. The uploaded checker was not executed.

## originality

PASS

The strongest prior substantially overlaps it: Hamoud gives exact indexing, first-order asymptotics with a non-o(1) error, and the two-eigenvalue formula along complete periods for the standard-word lengths. Treat extending that matrix calculation to fixed linear functionals and eventual nearest-integer rounding as direct refinements, not stand-alone evidence of novelty or value. The contribution that survives comparison is the full centered-count distribution, the different ordinary phase family and quantitative extremal data for all positive periodic directives. These are not the earlier ratio invariant or a rewording of bounded oscillation. Priority remains qualified.

## value

PASS

The motivation is the prior, explicitly identified bounded but irreducibly oscillating error in logarithmic palindromic-prefix counts. A fully computable density, sharp envelope and ordinary-cutoff phase family resolve that error rather than only reproving nonconvergence. The laws separate genuinely different behavior (uniform Fibonacci versus nonuniform constant-two) and explain both the sampling sensitivity and the normalization. The spectral and logarithmic-phase ingredients are elementary; the meaningful output is the complete error description for arbitrary positive periodic directives, not rounding or a few finite examples by themselves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
