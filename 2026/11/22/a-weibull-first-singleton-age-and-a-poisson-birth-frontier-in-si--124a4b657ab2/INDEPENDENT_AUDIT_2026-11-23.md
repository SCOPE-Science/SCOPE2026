# Independent mathematical audit

## correctness

PASS

The marginal is p(1-p) times the probability of avoiding later retained children, with no deleted-parent factor at the root. Conditional on the site states and retained marks, the parent-choice restrictions in (7) are independent. The avoidance-product tilt leaves the unmarked site states independent, shifts their means by at most O(1/t) at affected labels, and gives deleted-parent fractions with L1 errors O(b_n^{-1/2}) uniformly in positive compact rescaled windows. The log of the normalizing product differs from the sum of one-label log probabilities by O(1/min S) for each fixed marked-set size. This supplies the required joint relative estimates, not just a first moment. Mixed factorial moments then yield independent Poisson interval counts, with diagonals negligible because the largest single mass vanishes. The root contributes O(n^{-p}) and the rest of the initial window has expected mass O(epsilon^{1+p}), so no points are lost near zero. Transforming by cumulative intensity gives the joint fixed-rank Gamma law, including the stated Weibull first-label survival. RESULT.md (4)–(14) is the analytic replay path. VERIFICATION.md and verify.py were inspected, not executed; the reported finite checks do not prove the limit. The conclusion requires fixed p strictly between zero and one and fixed ranks.

## originality

PASS

The supported distinct claim is the birth-label Poisson process for site-isolated retained vertices at the p-dependent rare-age scale, and hence its rank laws. The same-model global size-one density and the original-tree leaf process are credited antecedents. Neither provides the needed uniform age-resolved joint probabilities. No equivalent was established in the bounded search; this is not a historical-priority certification.

## value

PASS

The theorem locates the earliest surviving size-one components, a natural statistic that a global component census cannot resolve. It identifies the retention-dependent birth scale, the full local intensity and correlated rank information in one result. The marked-parent tilt addresses a specific dependency that prevents direct transfer of the oldest-leaf theorem; this is not merely its reparametrization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
