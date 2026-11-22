# Scientific review

## Correctness — PASS

For every fraction \(p\in[11/50,7/25]\), three and only three critical points follow from two analytic facts: the gamma-mixture second derivative has at most three zeros, and four exact-rational sign evaluations alternate. The first and third critical points maximize locally; the middle minimizes. Exact rational Taylor enclosures establish that the long optimum wins at \(p=11/50\) and the short one at \(p=7/25\). The short branch's envelope derivative in \(p\) exceeds \(1/2\), whereas the long branch's derivative is below \(1/2\); this proves a unique equality of the two *global* maxima. All quantifiers, root intervals and boundaries are explicitly covered; at the equality exactly two optimal durations exist. The checker was run from the attached code and reported 61 rigorous rational assertions. Numerical transition values are diagnostic only. Risk: the theorem relies on the idealized detection and overhead assumptions, not on measured telescope data.

## Originality — PASS, with historical priority risk

The contribution is not the gamma-density mixture modality count or the source-count detection power definition. Ahmed, Goria and Hussein (2008) analyze gamma density mixtures, and Došlá (2009) provides the gamma-mixture rate-separation criterion. Nemiroff (2003) and Macquart (2014) analyze survey timing and overhead using different detection and population models. Kashyap et al. (2010) explain Poisson photon-count detection power. Comparisons of their mathematical statements with the present throughput quotient do not yield the strict, unique **global short-vs-long dwell-time equality** as the bright fraction changes. A related indexed gamma-mixture log-concavity record states a density curvature result, not a global throughput comparison; its linked complete package could not be accessed. Broader unindexed reward-rate results and unexamined source-population models pose unresolved priority risks, so originality assessment is provisional, not an independence or novelty certification.

## Value — PASS

This is a mathematically substantive scheduling boundary rather than a sign check: the same detector, overhead, source rates and source-density normalization admit two far-separated optimal exposure durations, with an exact one-time global switch as source composition changes. The result warns that optimizing a telescope dwell time with a single local numerical search can be structurally unsound for heterogeneous photon-limited populations. The proof gives a two-peak upper bound for arbitrary brightness ratios, two strict endpoint certificates and a monotone relative-height mechanism; it does not assert a physical threshold or optimal policy for real instruments. The rational interval of fractions brackets the genuinely endogenous switching value and is not an arbitrary grid slice.

## Relevant sources and limits

- Nemiroff (2003), *Tile or Stare?*, https://arxiv.org/abs/astro-ph/0301583 : arXiv posted 2003-01-29, the earliest verified public date among motivating sources.
- Ahmed et al. (2008), *Gamma Mixture: Bimodality, Inflexions and L-Moments*, https://doi.org/10.1080/03610920701713286 : full 16-page PDF inspected, density modality only.
- Došlá (2009), *Conditions for bimodality and multimodality of a mixture of two unimodal densities*, https://dml.cz/bitstream/handle/10338.dmlcz/140075/Kybernetika_45-2009-2_6.pdf : full primary text, especially Proposition 6 inspected.
- Kashyap et al. (2010), *On Computing Upper Limits to Source Intensities*, https://arxiv.org/abs/1006.4334 : source-count detection power, partial accessible text.
- Macquart (2014), *Optimization of Survey Strategies for Detecting Slow Radio Transients*, https://arxiv.org/abs/1406.5790 : accessible full HTML read for objectives and conclusions.
- Related indexed gamma-mixture log-concavity result: https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-sharp-log-concavity-threshold-for-equal-shape-gamma-rate-mixtu--e45ac4ab94e8 : summary examined; complete package inaccessible, which is retained as a priority limitation.

Self-review: passed. Independent audit: not yet performed.
