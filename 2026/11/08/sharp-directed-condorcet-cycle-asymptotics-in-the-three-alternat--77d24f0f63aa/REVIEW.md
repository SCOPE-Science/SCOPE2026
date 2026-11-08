# Scientific review

## Correctness — PASS

The ranking weights are enumerated exactly. The remote-pair event is binomial with \(p=\phi^2(2+\phi)/[(1+\phi)(1+\phi+\phi^2)]<1/2\). Under its probability tilt, the adjacent pairwise comparisons retain the exact positive gap \(\delta=(1-\phi^2)/[2(1+2\phi)(2+\phi)]\), providing exponential control on failures. The opposite cycle has a strictly smaller exponential base by a positive polynomial factorization. The remaining binomial tail has its exact \(n^{-1/2}\) normalization by Stirling and controlled successive-mass ratios. The theorem holds for each fixed \(0<\phi<1\) and odd \(n\to\infty\), not uniformly at \(\phi=1\). Reproducible finite checks: 171 passed. The infinite-population assertion follows from the analytic proof, not numerical experiments.

## Originality — PASS within checked evidence; priority not independently certified

The 2015 Lackner–Lackner preprint (arxiv:1505.05852) establishes Mallows single-peakedness bounds, not this cycle-event equivalent. The closely related 2025 Caizergues et al. paper (arxiv:2505.06028) analyzes the chance that a named candidate is a Condorcet winner; the introduction expressly excludes the probability that the majority relation is transitive (Section 1, 'Related Work'). Its Mallows case computes a different event, including a last-candidate winner rate with two pairwise constraints, and supplies machinery that could be adapted but no inspected statement implying the cycle theorem and its oriented exponential gap. The 2020 Xia paper was accessible at abstract level only; the available abstract supports general smooth probability bounds rather than this exact coefficient. Earlier print-focused treatments of Condorcet probabilities may contain related equivalents; the historical comparison is limited by access.

## Mathematical value — PASS

The complete fixed-dispersion exponential base, explicit polynomial prefactor, and universal dominant cycle orientation address a natural quantitative question for noisy preference aggregation. The tilted-margins lemma explains why a three-comparison paradox reduces asymptotically to one rare pairwise inversion despite correlated comparisons inside ballots. This is not a generic application of the binomial tail without an additional orientation and joint-margin proof. It gives a reusable benchmark for evaluating large-electorate ranking cultures while remaining restricted to three alternatives.

## Residual risks and scientific limits

Full historical priority is unverified; especially Gehrlein's earlier monographic literature was not exhaustively available. The endpoint \(\phi=1\), even electorates, and correlated preference draws are excluded. Full-text inspections were conducted for arxiv:1505.05852 (open journal HTML) and arxiv:2505.06028 (public arXiv HTML). The arxiv:2006.06875 comparison uses the accessible abstract, not a claimed full-text absence.

Self-review: passed. Independent audit: not yet performed.
