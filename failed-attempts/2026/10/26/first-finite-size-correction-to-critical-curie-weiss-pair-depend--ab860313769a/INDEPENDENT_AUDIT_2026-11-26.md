# Independent mathematical audit

## correctness

PASS

The formula holds for distinct spins in the stated β=1, zero-field normalization. In the frozen method the Stirling factor and sextic entropy term give g(x)=x²/2−x⁶/30 for W=M/N^{3/4}; normalized ratios, not bare weights, give the coefficient Cov(W²,g)=−a²/5. Quartic tails are negligible outside the growing central window; full-lattice integration of smooth quartic-weighted polynomials has error O(h²) on either lattice translate by a second-derivative bound, h=2N^{-3/4}, which is smaller than the required O(N^-1) for the scaled moment. Exchangeability subtracts the N diagonal terms exactly. An independent continuous calculation gives the same answer: Gaussian decoupling makes the spins conditionally independent with conditional mean tanh t and mixing density proportional to exp[−N(t²/2−log cosh t)]. Thus c_N=E tanh²t. For t=N^-1/4 x the mixing law expands against exp(−x⁴/12) with relative correction N^-1/2 x⁶/45; tanh²t=N^-1/2 x²−(2/3)N^-1x⁴+O(N^-3/2 x⁶). The potential is bounded below by a positive multiple of t⁴ near zero, has its unique global minimum at zero and grows quadratically at infinity, allowing termwise normalized integration with the claimed remainder. The coefficient is (μ₈−μ₂μ₆)/45−2μ₄/3=−(1+a²/5) using μ₂=a, μ₄=3, μ₆=9a, μ₈=45.

## originality

FAIL

Already covered as a direct moment consequence of Can and Pham (2017), not merely of the leading quartic limit. In exactly the same model, Theorem 1.4 prints the normalized first distribution correction using p₂(t)=(t²/2−t⁶/30)e^{−t⁴/12}. Crucially, their proof in §§3.2–3.3 gives the pointwise central expansion with an integrable polynomial times the quartic weight at order O(N^-1), as well as an exponentially small outer sum. Multiply that expansion by x² for the numerator and use it unweighted for the denominator. Summing the weighted remainder still gives relative O(N^-1); the grid spacing is 2N^-3/4 and the whole-line quadrature for each displayed smooth term costs O(N^-3/2) after multiplication by the spacing. Normalizing gives E[W²]=a+N^-1/2[(μ₄−a²)/2−(μ₈−aμ₆)/30]+O(N^-1)=a−N^-1/2a²/5+O(N^-1). The exact identity c_N=(√N E[W²]−1)/(N−1) now gives the frozen coefficient and remainder. It is immaterial that the source chooses a distribution tail, rather than a distinct-spin pair, as its named statistic: the very same local expansion and error control already settle this moment.

## value

FAIL

Critical pair dependence and the susceptibility correction are natural observables, and the formula is useful as a concise corollary or reference calculation. But the frozen record's proposed new narrow exact fact is mechanically implied by the published correction profile and its established remainder. Applying the second-moment observable and subtracting the known diagonal contribution offers no surviving independent exact invariant, new regime or structural extension. No repair is warranted on the available result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
