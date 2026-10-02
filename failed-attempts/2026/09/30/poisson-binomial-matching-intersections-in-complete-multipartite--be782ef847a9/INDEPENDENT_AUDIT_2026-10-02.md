# Independent mathematical audit — SCOPE-20260930-be782ef847a9

Final disposition: **FAILED**.

## Correctness
**PASS** — The transfer-current computation is correct. Solving the complete-multipartite Laplacian for one oriented matching edge gives diagonal kernel entry \((N-1)\sigma/N\) and off-diagonal matching entry \(-\sigma/N\), so every \(q\)-edge submatching has transfer-current matrix \(\sigma(I-J/N)\). Its determinant is \((1-q/N)\sigma^q\). Summing joint inclusions over subsets yields the displayed probability generating function and its Bernoulli factorization; the covariance formula follows from the \(q=1,2\) cases. Boundary probabilities remain in \([0,1]\) for admissible matchings.

## Originality
**FAIL** — Wang and Ge's 2026 theorem gives an exact determinant formula for the number of spanning trees of an arbitrary complete multipartite graph containing any prescribed spanning forest. A prescribed submatching, with all other vertices isolated, is exactly such a forest. Consequently every joint-inclusion probability in the assigned theorem is already a special case of that stronger enumeration theorem; simplifying that special case gives the displayed rank-one expression. Once the \(q\)-subset counts are known, the full PGF, Poisson-binomial factorization and covariance are elementary binomial-generating-function consequences. Under the required implication standard, this matching law is therefore covered even though the broader paper does not state the same distributional wording.

### Equivalent formulations
The assigned inclusion probabilities are direct specializations of the broader forest-enumeration invariant.

### Broader coverage
The general theorem has strictly broader host and forest input than the assigned matching family.

### Exact database or table
Wording absence is nondecisive because the joint counts are a direct special case and determine the distribution.

### Claim versus prior implication
The headline distribution and covariance are mechanically implied by the broader enumeration theorem.

## Value
**FAIL** — The compact distributional packaging is useful, but the only new step beyond a stronger arbitrary-forest counting theorem is specializing its determinant to a matching and performing a binomial generating-function simplification. That is a routine corollary rather than an independent motivated mathematical gap.

## Source inspections
- **On enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest** (https://arxiv.org/abs/2602.03602): complete accessible primary article, including Theorem 4.5 and its determinant formula Method: primary open full-text inspection. Assessment: STRONGER_GENERAL_COVERAGE. Evidence: Theorem 4.5 counts spanning trees containing an arbitrary fixed spanning forest in a complete multipartite graph.

## Checked sources
- https://arxiv.org/abs/2602.03602

## Residual risks
- No correctness defect is asserted; rejection is implication-based coverage and routine value.
