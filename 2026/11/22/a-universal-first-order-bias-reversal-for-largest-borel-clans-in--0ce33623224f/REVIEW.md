# Self-review

## Correctness — PASS

The claim concerns the maximum of the Borel-family sizes in a pooled Poisson forest, not the maximum or sum of individual observation totals. The exact CDF equals a Poisson no-exceedance probability. Uniform Stirling expansion of the Borel point mass, with a weighted exponential remainder for the entire tail above a positive scaled threshold, gives an \(O(n^{-1})\) CDF remainder and an explicit signed \(n^{-1/2}\) coefficient. The complementary-error-function identity and the monotonicity of its derivative prove existence and uniqueness of the sign change. The standalone standard-library numerical checker reproduces exact finite-size probability sums at three sample sizes and the correct signs. Limits: fixed strictly positive parameters and compact positive thresholds only; the finite checks are not themselves proofs.

## Originality — PASS, qualified

The original generalized-Poisson model and Borel representation are established by Faroughi–Li–Ren (2024) and older authors. The known inverse-Gaussian **total sum** limit documented by Wolfram Research, and general cluster-mark extreme-value theory of Basrak–Milinčević–Žugec (2022), were compared by object and implication: neither supplies the **first signed correction for largest Borel clan size** or the universal zero of its explicit coefficient. The latter paper's lawful arXiv full text was inspected, including the mark-versus-cluster-size distinction in its Borel/Hawkes sections. General Poisson-point convergence is prior work, not claimed as new. Earlier books or less-accessible articles may contain comparable specialized second-order expansions, so historical priority is provisional rather than independently certified.

## Value — PASS

The largest infection/claim family can govern exposure to a single severe cascading event even when the expected count per sample remains fixed. The limiting maximum law by itself does not tell whether finite-sample tail probabilities are conservative or anticonservative: the first correction gives the sharp \(n^{-1/2}\) magnitude and identifies a unique natural threshold where its direction reverses, without arbitrary parameter slicing. That supplies a concrete finite-sample calibration for near-critical branching risk.

## Scope and independent assessment

Uniform error only on compact subsets of positive thresholds; no finite-\(n\) exact single-crossing claim, no certified decimal root interval, and no second-order constant at the cancellation point. Historical priority remains subject to fuller literature review.

Self-review: passed. Independent audit: not yet performed.
