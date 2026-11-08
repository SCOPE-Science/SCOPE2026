# Scientific assessment

## Correctness — PASS

For every \(0<\alpha<1\), real \(\beta\), and integer \(r\ge1\), the quadrature model and independence assumptions are explicit. Decomposing each estimate into the first random stratum and all remaining strata gives a pathwise \(o(1)\) remainder via bounded variation of the power-log integrand away from zero. Inversion of the first-panel threshold yields the exact positive fixed-error tail constant; the median's binomial exceedance identity raises the tail power by \(r\). The power-log series test and both Borel–Cantelli lemmas, using **independent complete designs across sample sizes**, prove the precise strong-law boundary and the almost-sure unbounded-spike complement. The proof independently establishes convergence in mean and the fixed-sample moment thresholds. The standalone 889-check test supports algebra and finite asymptotics; no infinite conclusion relies on the finite computation.

## Originality — PASS, qualified

The relevant primary source is Hofstadler–Rudolf, *Consistency of randomized integration methods*, arXiv:2203.17010v1, Section 3, especially Proposition 3.4 and Example 3.6. That source establishes a broadly applicable **sufficient** strong law for medians of randomized integration rules under \(L^p\) and replica-count conditions, but neither an exact \((\alpha,\beta,r)\) if-and-only-if frontier nor the probability equivalent, critical logarithmic threshold, and almost-sure unbounded-spike complement here. Loh (1996), Section 3, covers classical LHS strong laws under stronger moment assumptions; Goda–L'Ecuyer (2022) analyzes medians of randomized QMC rules on smooth spaces, rather than singular one-dimensional independently jittered strata. Literature and indexed research records were compared using full claims, not merely coincident topics. Novelty is assessed for the combined exact quantitative classification, not for the classical binomial tail or Borel–Cantelli proof ingredients. A prior equivalent result in unindexed specialist literature remains possible.

## Value — PASS

A fixed-cost median of independently stratified quadrature estimates is a natural robust integration design when endpoint singularities cause infinite per-run variance. This result resolves its **exact** strong-law replica requirement, including a logarithmic endpoint invisible to coarse \(L^p\) bounds. It gives an explicit and practically interpretable contrast: three replicas yield finite individual-sample variance for every integrable pure-power singularity but nevertheless fail to converge almost surely for \(\alpha\ge2/3\) under independent full re-randomization. The restriction to this motivated benchmark is important and does not yield general guarantees for nested, deterministic, or multivariate integration rules.

## Comparison and limitations

Closest sources: https://arxiv.org/abs/2203.17010 (full text, §3); https://doi.org/10.1214/aos/1069362310 (Loh 1996, §3); https://arxiv.org/abs/2201.09413 (median QMC, §§1–3); https://arxiv.org/abs/2002.07859 (nested scrambling, abstract only). Exact claims in the accessible prior research collection on randomized quadrature, Latin hypercubes, and power-log boundaries are not implication-equivalent to the present fixed-error median tail law. The source search does not constitute a universal publication-priority proof; independent validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
