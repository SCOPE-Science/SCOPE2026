# Scientific review: periodic-Parseval Matérn matrix bound

## Correctness — PASS

The stated error identity is verified independently by substituting the definition of the full-periodized kernel and the truncated Fourier series. The finite-period Parseval normalization is \(h^{-d}\sum|h^d\widehat{k}(hj)|^2=h^d\sum|\widehat{k}(hj)|^2\). The difference-density maximum follows from \(\rho\le R\) and \(\int\rho=1\). The lattice sum of squared Fourier coefficients is controlled by the cited half-space bound at its transformed exponent \(2\nu+d/2\), producing the claimed \(2\nu+d/2\) root-mean-square cutoff. The matrix diagonal contributes exactly \(N|e(0)|^2\); arbitrary dependence among off-diagonal entries does not affect the expectation formula. Changing one site affects the normalized off-diagonal U-statistic by at most \(2M^2/N\), giving the displayed concentration exponent. Almost-sure convergence follows by a summable two-sided concentration bound and Borel–Cantelli. Finite verification: 171 assertions passed in the included checker. No infinite theorem is inferred from that finite test.

## Originality — PASS, with residual publication risk

Barnett–Greengard–Rachh, arXiv:2305.11065v1 Section 4, identify the same exponent explicitly as Conjecture 9 and report it as unproved. Their Lemma 4 and Theorem 5 supply deterministic ingredients, but their autocorrelation argument is heuristic. Greengard–Rachh–Barnett, arXiv:2210.10210v2, presents the algorithm and numerical version of the faster estimate but does not prove it. The distinct contribution is full-period L2 localization over the observation-difference cube, which turns the sum of absolute Fourier tails into the sum of squared tails without pointwise regularity of the sampling density, followed by explicit finite-sample concentration. The related Bachmayr et al. periodization work was only checked at abstract level and remains a genuine possible broader predecessor. Relevant later-coverage searches did not return a decisive stronger theorem, which is evidence, not certainty of uniqueness.

## Value — PASS

The prior conjecture explicitly motivates the numerical rank needed to approximate large Matérn covariance matrices, making the gain from the deterministic \((hm)^{-2\nu}\) exponent to the random-site RMS \((hm)^{-2\nu-d/2}\) exponent an intrinsically motivated quantitative result. Explicit constants and the diagonal correction specify parameter and sample-size regimes; concentration makes the benchmark useful beyond an expectation estimate. The result does not claim actual runtime speedups or a matching sharp lower constant.

## Scientific boundaries

The site density must be bounded and sites iid; the alias term must remain small relative to the spectral truncation term; and the almost-sure/probability statements are for fixed discretization parameters as sample size grows. The unresolved precedence risk from uninspected older full text and later specialist work should be checked before external claims of priority.

Self-review: passed. Independent audit: not yet performed.
