# Scientific review

## Correctness
**PASS.** The positive-definite Gram reduction gives exact weight numerators; the outer-weight integrand has an elementary convexity/monotonicity certificate. The central numerator is an explicit entire exponential polynomial whose entire Taylor series is nonnegative for \(a\ge6-\sqrt{30}\), proved by a formula for every degree, including endpoint equality. A negative leading Taylor coefficient proves necessity. An independently evaluated script corroborates the formulas at forty parameter pairs. No finite check is used to infer positivity for all degrees.

## Originality
**PASS, qualified.** The 2015 Gaussian-process quadrature background (arXiv:1504.05994) and the accessible 2018 Matérn/positivity discussion (arXiv:1812.08509, especially its Matérn examples) do not state the closed radius or coefficient certificate. Related indexed results concern the Gaussian covariance (a different cutoff) and the exponential covariance (a different smoothness parameter), neither of which implies this claim. General classical cardinal-function literature presents a bibliographic residual risk. Search absence alone is not used as a proof of uniqueness.

## Value
**PASS.** Positivity of Bayesian quadrature weights is a stated structural question: negative weights can destroy the positive-integrand guarantee. The sharp three-node universal-design cutoff for a standard finite-smoothness covariance complements the Gaussian and exponential cases and provides a simple usable radius rule, rather than an unmotivated numerical slice.

## Limitations
Only three equally symmetric nodes and uniform Lebesgue integration on a finite interval are covered, with no regularization. The exact all-bandwidth question is settled, but there is no claim for arbitrary nodes or higher-dimensional configurations. Independent human scrutiny and exhaustive bibliographic priority checks have not occurred.

Self-review: passed. Independent audit: not yet performed.
