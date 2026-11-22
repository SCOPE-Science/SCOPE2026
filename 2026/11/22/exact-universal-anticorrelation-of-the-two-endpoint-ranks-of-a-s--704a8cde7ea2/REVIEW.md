# Scientific assessment

## Correctness — PASS

The finite-horizon statement is derived analytically. Both ranks are exactly identified as negative-prefix and positive-suffix occupation counts. For each overlapping pair of blocks, decomposing the increments into three independent symmetric sums and averaging the three pairwise sign products gives the universal value one. A complete sum over ordered nonnegative block lengths proves the covariance coefficient. The two-block sign identity proves the marginal variance independently. No unproved local-limit theorem or numerical approximation is needed; the critical identities are supported by the sign-conditioning argument and exact finite cases in `check_endpoint_ranks.py`.

## Originality — PASS relative to inspected sources, with priority risk

The 2026 Zhu–Xie paper treats distance correlations between **independent** walks, not within-walk endpoint rank covariance; its finite-variance asymptotics do not imply the exact all-horizon identity here. Ivanovs establishes time-reversal and marginal occupation/extremum equivalences, but not the cross-covariance of the two endpoint ranks. Pitman–Tang analyzes extreme order-statistic **values** near the minimum, not ranks of the initial/final observations. Related indexed results about endpoint *height* correlations, extremal endpoint events, and rank tests have different variables or only special finite horizons. Searches found no equivalent exact formula. The 1972 Aneja–Sen article is a residual risk: its abstract concerns a Dwass rank-distribution method, while its full text was inaccessible and could contain uninspected implications. This review does not claim a proof of absolute priority.

## Value — PASS

The first and last ranks have matching discrete-arcsine marginals yet are coupled nontrivially. An exact all-size negative covariance and a universal limiting correlation \(-1/3\) quantify their dependence, including infinite-variance step laws that are outside Brownian-invariance arguments. The three-block sign identity is a structural reason for the surprising distribution-freeness, so the result is a motivated boundary-dependence law rather than a numerical or renamed marginal formula.

## Scope and remaining limitations

The law requires symmetric, i.i.d., atomless real increments. It determines only the bivariate second-order summary; no complete joint distribution is established. Independent expert assessment and the inaccessible classical text remain outstanding.

Self-review: passed. Independent audit: not yet performed.
