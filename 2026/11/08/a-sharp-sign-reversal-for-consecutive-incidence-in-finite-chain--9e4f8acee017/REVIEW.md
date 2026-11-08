# Self-review

## Correctness — PASS

The stated domain, update ordering, and independence assumptions are explicit. The exact formula follows by conditioning on the first new-case count and the initial infective's independent recovery, then applying two independently derivable binomial factorial moments. The logarithm of the sign factor has strictly negative second derivative and first derivative \(n-2+\mu\) at the origin; this determines all boundary cases. The large-population expansion has a uniform remainder because \(\mu\) appears only inside a factor between \(1-p\) and \(1\). The embedded executable enumerator checks \(54\) complete rational two-round laws and two exact sign witnesses. These finite computations are corroboration, not the all-size proof.

## Originality — PASS, with residual risk

The primary motivating paper (Boudreau and St-Onge, arXiv:2610.17138v1, §§2.1–2.4 and Supplement S1) defines the finite chain-binomial process and models joint incidence with branching PGFs. It does not give the exact *finite-population* first-two-incidence covariance, a single sharp sign transition, or the second-order \(\sqrt{\log n/n}\) transition scale. The CDC Reed–Frost documentation treats the \(\mu=1\) process and its reproduction number, but no such covariance law. The broader 2018 PGF primer and 2025 multi-region chain-binomial preprint discuss related approximations or spatial count dependence rather than this precise sign boundary. Published mathematical research records found no covering statement; closest comparisons involve deterministic SIR dynamics, cross-pathogen co-infection covariance, or depletion in other discrete probabilistic settings. A classic unindexed two-generation moment calculation may be equivalent; further independent literature review remains warranted.

## Mathematical value — PASS

The theorem provides a natural, exactly defined dependence statistic for early outbreak counts, resolves its complete sign phase diagram, identifies a sharp finite-size threshold and a nontrivial refined large-population scale, and connects it to the usual positive-covariance branching limit. This quantifies the previously qualitative finite-susceptible-population breakdown of the branching approximation. It is not merely a numerical counterexample or a renamed general covariance identity.

## Scientific limitations and closest sources

The result applies only to rounds one and two from a single index case with homogeneous, independent synchronous updates and perfect incidence observation. It does not concern longer-lag autocorrelation or empirical time-series estimates. Closest primary material: Boudreau–St-Onge (2026) §2.1 exact transition law, §§2.2–2.4 incidence PGF and finite-population divergence; CDC Reed–Frost model description; Miller (2018) large-population PGF framework; 2025 multi-region chain-binomial preprint. A possible equivalent result in older chain-binomial moment literature cannot be excluded from indexed searches.

Self-review: passed. Independent audit: not yet performed.
