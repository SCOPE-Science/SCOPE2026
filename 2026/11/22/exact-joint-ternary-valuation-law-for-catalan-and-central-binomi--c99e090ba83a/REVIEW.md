# Review of the joint ternary binomial–Catalan valuation law

## Correctness (PASS)

The exact claim has a self-contained carry proof from Kummer's theorem: \(\nu_3(C_n)=\nu_3\binom{2n}{n}-\nu_3(n+1)\). Trailing base-three digit \(2\) runs cancel the first carries. The remaining two carry states give the matrix in RESULT.md and the rational function after an explicitly invertible formal-series matrix. The digit constructions establish every allowed valuation pair and rule out the sole excluded corner. Symbolic differentiation gives exact finite-depth covariance; the dominant eigenvalue and the tight geometric trailing-run distribution give the joint normal limit. The separately checked exact integer implementation matched all 29,523 nonzero-depth indices below \(3^9\) and 800 direct binomial values. The computations corroborate rather than replace the all-depth proof.

## Originality (PASS within inspected evidence)

The exact marginal Catalan three-adic valuation generating function and Gaussian limit are already published; the proof reproduces them as a specialization rather than claiming them as new. A separate published joint result concerns central and threefold binomial valuations and has bounded covariance, so it neither implies the present exact Catalan normalization coupling nor the triangular support. The classical identity relating Catalan and central binomial valuations does not determine cross frequencies from either marginal. Relevant 2013 Catalan congruences concern individual subsequences, and the accessible 1973 divisibility abstract concerns runs of divisible Catalan numbers. The latter full paper was not inspected, so an earlier implicit version of the joint law cannot be excluded. Searches did not identify an equivalent statement; lack of a match is not a proof of novelty.

## Value (PASS)

For the canonical numerator–normalization pair \(\binom{2n}{n}\) and \(\binom{2n}{n}/(n+1)\), the joint prime-adic divisibility distribution answers more than either single-sequence census: it determines all mixed frequencies, the exact realizable triangular support and its upper boundary, and a sharp covariance law. The covariance grows like \(L/2\), contrasting with bounded covariance for a well-studied different binomial pair; it therefore quantifies a real dependence mechanism induced by the Catalan denominator. The result is a natural complete classification, not an arbitrary finite sample.

## Limitations and closest literature

Only prime three and full ternary blocks are covered; no multi-prime, arbitrary-cutoff, or local-limit assertion is made. The closest full inspected results were the published individual Catalan ternary valuation census and the published joint central/threefold-binomial valuation census. Kummer's theorem, OEIS A067397, and classical Catalan divisibility are acknowledged. Historical priority remains subject to incomplete access to Alter–Kubota (1973). Scientific checks are same-model only.

Self-review: passed. Independent audit: not yet performed.
