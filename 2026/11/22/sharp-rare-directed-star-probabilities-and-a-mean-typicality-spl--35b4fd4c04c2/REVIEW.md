# Scientific review

## Correctness — PASS
The conditional binomial outdegree law follows from independent uniform coordinates. Gamma density ratios, a factorial-moment envelope and dominated convergence give the exact integral constant; integrating the Poisson tail yields \(\Gamma(r+1-c)/((c-1)\Gamma(r))\). To avoid an invalid rare-event independence assumption, truncate hub log-volumes to \(|Y-\log n|\le K\), where the independent *candidate* count has vanishing mean; a binomial second factorial moment controls multiple candidates. The contribution outside the window vanishes under the same integrable envelope. The finite expected-star formula follows from the minimum rank of one distinguished point. Reproducing `check.py` yielded 203 checks. The finite checks support, but do not certify, the infinite limit.

## Originality — PASS against accessible comparisons
The motivating full text arXiv:2611.01096v1 addresses non-Pareto counts and their stable/Gaussian/Poisson regimes. The closest older source, Bollobás and Brightwell (1995), studies existence thresholds for fixed-degree vertices in random high-dimensional orders, so the existence *threshold* alone is not new. Its accessible abstract does not supply this relative-error rare tail asymptotic or its Gamma prefactor, and the full paper could not be retrieved. Published records for Pareto-frontier/comparability covariances use different statistics. The material risk is potential unstated stronger coverage in the inaccessible 1995 full text or other historical degree-tail results; this is a same-model best-knowledge comparison, not a guarantee of priority.

## Value — PASS
The rare existence probability is a natural structural degree statistic for high-dimensional dominance orders. A sharp equivalent is stronger than an appearance/disappearance threshold, providing the absolute rare-event scale and a fixed-degree family of constants. The theorem simultaneously shows a nonempty region where expected directed-star counts grow polynomially while their actual existence probability vanishes, revealing an expectation-versus-typical geometry mismatch caused by extraordinarily rare domination centers. The result does not depend on choosing an arbitrary finite dimension or a computational slice.

## Closest literature and limits
Bhattacharjee et al., arXiv:2611.01096v1 (full text inspected); Bollobás and Brightwell, *Random high-dimensional orders*, DOI 10.2307/1428102 (abstract inspected, full text unavailable). Results are restricted to fixed \(r\ge2\) and \(e<c<r+1\). The priority risk is explicitly retained and no independent assessment has occurred.

Self-review: passed. Independent audit: not yet performed.
