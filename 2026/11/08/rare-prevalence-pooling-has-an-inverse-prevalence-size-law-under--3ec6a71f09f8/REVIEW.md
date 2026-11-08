# Self-review

## Correctness — PASS

All assumptions are stated: infinite exchangeable beta-mixture, perfect tests, no dilution or size cap, singleton tested only once, and the low-prevalence restriction \(\alpha=\kappa p<1\). Exact beta integration yields \(Q_k\). The signed finite difference follows by one recursion; the ratio of its threshold factor has numerator-minus-denominator \(k(1-\alpha)+2(\kappa-\alpha)>0\). Gamma-ratio bounds ensure an actual finite crossing. The special singleton is compared separately, using the negative asymptotic sign of \(C_k-1\). Compact-parameter uniform log-product expansions prove location and cost asymptotics. The standalone arithmetic tests are supporting diagnostics, not a replacement for this proof.

## Originality — PASS within inspected literature, provisional

The 2011 clustered-testing paper already provides the beta-binomial negative-pool formula and correlated-test savings, so neither is new. The 2021 beta-binomial comparison proves the correlated optimum is not smaller than the independent optimum but does not state the integer one-crossing law or the unrestricted fixed-correlation \(p^{-1}\) scale and \(p\log(1/p)\) cost. The 2023 exchangeable-partition paper solves finite partitioning more generally, but its methodology does not by itself give this closed asymptotic statement; the problem and probability object overlap, not the asserted theorem. Searches of archived disease-screening work and prior mathematical results yielded no equivalent. Residual priority risk persists for specialized group-testing asymptotics and inaccessible older appendices. The 2010 working-paper date is verified only to the month, not to a calendar day.

## Value — PASS

Fixed positive intracluster dependence changes the rare-event optimum from the classical inverse-square-root prevalence scale to inverse prevalence; this is an order-of-magnitude design-law change for correlated infectious-status sampling, and not a numeric optimization or a routine parameter substitution. The exact unimodality rule permits global pool-size selection without arbitrary search cutoffs. The practical significance is conditional: finite clusters, dilution, misclassification and operational constraints can suppress the limiting regime.

Self-review: passed. Independent audit: not yet performed.
