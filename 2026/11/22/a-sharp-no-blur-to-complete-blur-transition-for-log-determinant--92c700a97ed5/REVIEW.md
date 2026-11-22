# Scientific review

## Correctness

**PASS (self-review).** Orthogonal Fourier diagonalization of the two-pixel convolution reduces the exact joint quadratic minimization to one rational-plus-logarithmic scalar function. The all-parameter secant-ratio lemma follows from a derivative with at most one interior sign change from positive to negative; its endpoint values establish the global threshold. A monotone-in-weight comparison proves uniqueness after the jump. The derivative numerator is an upward quadratic with opposite endpoint signs in the metastable window, proving the unique barrier. The auxiliary-scale boundary follows from a strictly decreasing logarithmic function. A standalone high-precision and exact-rational checker supplements, but does not replace, these arguments. The limiting and singular-matrix cases are included because \(\ell,d>0\).

## Originality

**PASS (qualified self-review).** Dworaczyk–Español's Proposition 5 supplies a sufficient *local* no-blur exclusion condition for general simultaneously diagonalizable periodic operators; the new statement is an exact *global* endpoint-only phase transition with a sharp weight and an open metastability interval, on the smallest nontrivial nonnegative periodic blur. Its complete argument is not a mere restatement of the source proposition. Wipf–Zhang's general variational-Bayesian prior mechanism and the older marginal-likelihood papers do not derive this threshold for the specified quadratic log-determinant objective. The closest retrieved mathematical records concerned other spectral penalties, and inspected published-record claims did not overlap. Residual risk: an uncatalogued prior treatment of exactly this scalar reduced functional could subsume the finding; neither semantic search nor the cited papers establishes absolute uniqueness.

## Value

**PASS.** The new objective was motivated to avoid identity/no-blur degeneracy, but this example identifies a sharp parameter regime where enforcing it too strongly eliminates *all* high-frequency contrast rather than selecting an intermediate blur. The exact global-versus-local threshold gap is operationally important: a quasi-Newton optimizer initialized at no blur can remain at a strict, nonoptimal local minimum even though the global fitted blur has become completely degenerate in the opposite direction. Two pixels are the minimal bona fide mass-preserving periodic convolution supporting this failure. The result gives an exact tuning benchmark and an interpretable failure mode, not merely an algebraic counterexample.

## Scope and remaining risks

The assertion is for exactly two pixels, identity image and auxiliary regularizers, a uniform base prior, \(B>0\), and \(\ell,d>0\). It makes no global classification beyond the sharp small-auxiliary-scale regime or for higher-dimensional PSF families. The finite checker is supplementary. Primary-source inspection covered the exact model derivation, the closest theorem, relevant experiments and older blind-deconvolution analyses; an older accessible MIT primary PDF could not be fetched because the host returned HTTP 429, and its abstract alone is not treated as a full-text comparison. Independent auditing and validation remain unperformed.

Self-review: passed. Independent audit: not yet performed.
