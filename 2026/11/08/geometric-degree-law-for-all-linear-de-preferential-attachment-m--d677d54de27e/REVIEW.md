# Self-review

## Correctness

**PASS.** The exact target law follows from independent uniform candidate proposals followed by acceptance against \(1-d_i/D\), and the conditional probability of first rejection is exactly \(1/n\) for every possible history. This implies independent Bernoulli rejections, an almost-sure logarithmic total by exponential concentration and dyadic Borel--Cantelli, and a deterministic histogram-TV bound. The standard uniform recursive process has independent per-vertex future attachments; Poisson approximation at macroscopic birth rank and concentration of histogram counts prove the almost-sure shifted geometric empirical limit. The included exact rational and simulation checks replay but are not used as an infinite proof.

## Originality

**PASS (provisional).** Bandyopadhyay--Sen, arXiv:2508.18144v2, Theorems 2.3--2.6, obtain the empirical geometric law only at \(m=1\) and explicitly state that they could not derive or conjecture the \(m>1\) law. Bandyopadhyay--Joshi, arXiv:2512.12408, also restrict the displayed empirical law to \(m=1\). The classical uniform recursive geometric law alone does not imply the new coupling; actual published research-record repository, source and alias searches found no covering statement. Relevant risks include older general near-uniform recursive graph couplings and unindexed priority results.

## Value

**PASS.** The result resolves the precise missing empirical distribution in a model explicitly studied for multi-edge arrivals and strengthens it with a quantitative pathwise transfer principle. Degree statistics are a central natural observable for evolving networks; the formula distinguishes arrival multiplicity and is not an arbitrary finite slice. It does not solve the corresponding inverse-de-preferential problem or stronger graph-structure comparison.

## Scientific limitations

The statement is for fixed \(m\), the stated sequential linear kernel, and multigraph attachments. It makes no independence or external verification claim; the simulations and finite exact checks do not prove the asymptotics by themselves. Historical priority remains subject to independent specialist review.

Self-review: passed. Independent audit: not yet performed.
