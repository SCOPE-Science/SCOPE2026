# Scientific review: age-monotone, lag-free Palm amplification

## Correctness — PASS

The exact uniform-parent and Bernoulli-retention rule gives conditional increment probability \(pS_m/m\). Its first-moment recursion and the \(S_m(S_m+1)\) recursion give the two finite products \(A_m\) and \(B_m\). Accounting for the marked successful birth at \(j\) yields the conditional factor \(R_j=2B_{j-1}/(A_{j-1}A_j)\). Conditional expectation propagation establishes the same multiplier for every later indicator, while the explicit adjacent ratio proves strict increase with age and the gamma product proves the limit. The stand-alone exact-arithmetic verifier passed 145 assertions on exhaustive parent/retention configurations up to eight vertices; the proof, not the census, covers all indices and parameters.

## Originality — PASS, qualified

The accessible full texts of Baur and Bertoin (arXiv:1406.2238), Baur (arXiv:1407.2508), Kürsten (arXiv:1512.05275; exact second moment, equation (44)), Desmarais–Holmgren–Wagner (doi:10.1002/rsa.21142) and Zheng (arXiv:2606.01881) document the root-cluster process, growth laws and urn structure, but the inspected claims do not provide the marked finite-index pair ratio and strict age-monotonicity. The closest indexed research findings concern root-cluster correlations with unmarked degree, leaf, or singleton counts. General Pólya–Hoppe and Simon-process results may imply the identity through specialization; further independent historical-priority review remains necessary. Novelty is not inferred from absence of a search hit.

## Value — PASS

The exact time-labelled factor quantifies how observing one successful root attachment changes all later membership probabilities. The surprising permanent lag-free multiplier is strictly greater than one, increases with the age label of the marked birth, and has a finite sharp limit. This is a natural structural dependence question in random genealogies with bond loss, distinct from static mean or cluster-size distribution. It gives a directly usable predictive pair kernel, not a general conditional distributional or independence theorem.

## Scientific scope and residual risks

The result requires uniform recursive attachment, independent bond-retention with common fixed probability \(0<p<1\), one marked nonroot event, and later observations. The identity does not cover conditioned multi-marked membership, site retention, other attachment distributions or central limit assertions. The infinite claim is proved analytically; computational checks are limited to eight vertices. Its originality is provisional because broader urn formulations might dominate it even without identical terminology.

Self-review: passed. Independent audit: not yet performed.
