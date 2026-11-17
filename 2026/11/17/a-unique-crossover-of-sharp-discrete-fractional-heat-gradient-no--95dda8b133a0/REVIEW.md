# Scientific assessment: sharp lattice fractional-heat gradient crossover

## Correctness

**PASS.** The ordinary heat-kernel differences form a positive tridiagonal evolution on the half-line, giving strict radial unimodality without relying on numerical Bessel inequalities. Positive-stable Bochner subordination transfers strict unimodality to every fractional order in the claimed range. Telescoping the difference kernel proves the exact operator norm and exhibits one common step-function extremizer. The probability integral has a single distribution-function sign change at spectral level \(1\). After removing the positive factor \(te^{-t}\), the difference of the two Laplace transforms is strictly decreasing. Its positive initial value follows from the strictly increasing spectral moment, and its negative divergence follows from the interval below level \(1\). This proves one positive simple crossing for every pair of orders. The short- and long-time constants follow from a beta integral and low-frequency rescaling. The packaged finite checker completed without errors; it is corroboration rather than an infinite proof.

## Originality

**PASS, qualified.** The 2014 Ciaurri et al. discrete harmonic-analysis paper supplies ordinary heat-kernel formulas and a fractional discrete Laplacian maximum principle, but does not state a sharp \(\ell^\infty\)-to-discrete-gradient norm for all fractional powers or compare the norms across different orders. Their 2016 fractional-diffusion paper develops the nonlocal generator and regularity framework, but its inspected main results do not contain the unique-crossing criterion. The 2021 Abadias–De León-Contreras work provides estimates for the classical heat and Poisson kernel differences. Chen–Li (2026) is especially close: Proposition 1.2 gives an optimal decay *order* for the \(\ell^1\) first difference of fractional lattice heat kernels, not the exact coefficient in one dimension and not a theorem that all pairs of order-dependent norm curves cross exactly once. Comparable published results concerning generator norms, bounded-input Lipschitz preservation, or \(\ell^1\)-to-\(\ell^\infty\) gradient norms do not imply the present comparison. A hidden older equivalent in Laplace-transform ordering remains a residual priority risk; no independent historical validation is claimed.

## Mathematical value

**PASS.** Sharp smoothing constants, rather than exponent-only decay estimates, are relevant when choosing fractional diffusion order for rough data. The all-pairs single-crossing theorem establishes a structural obstruction to universally ranking fractional orders: the order with the smaller initial contraction deficit eventually becomes the stronger smoother, exactly once. Common extremizers make the contrast operational for the same bounded input, not simply for separately chosen witnesses. The sign-changing spectral distribution and monotone rescaling supply a reusable comparison mechanism. This is not a restatement of generic heat-kernel estimates or a selection of an arbitrary numerical parameter.

## Coverage and limitations

The claims apply only to the infinite one-dimensional unnormalized lattice, orders strictly above zero and at most one, and the bounded-input-to-first-difference norm. The theorem does not imply an order-crossing statement on other geometries or norms. The exact first-public-source evidence is the 2014-01-09 original arXiv submission of Ciaurri et al.; sources from 2016, 2021 and 2026 are supporting comparisons. Numerical checks cannot prove uniqueness. Originality comparison is based on accessed texts and indexed records and cannot establish complete historical uniqueness.

Self-review: passed. Independent audit: not yet performed.
