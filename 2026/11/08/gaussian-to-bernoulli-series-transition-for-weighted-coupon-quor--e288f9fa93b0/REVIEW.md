# Scientific review: Gaussian-to-Bernoulli-series weighted-quorum transition

## Correctness — PASS

The ranked \(\ell^2\)-coefficient limit for homogeneous exponential discovery clocks follows from a finite-head characteristic-function expansion with a Gaussian residual tail. The local increment variance is \(O(s_n^3)\), which is enough to invert the strict threshold at scale \(s_n\). Direct cumulants distinguish the Bernoulli-series and Gaussian possibilities, and elementary generalized harmonic-number asymptotics give the transition at Zipf exponent \(1/2\). All boundaries \(0\le\rho\le1\) and \(0<\theta<1\) are covered; no stopping-time moment convergence is assumed or claimed. The standalone exact-rational checker passed 1019 assertions, which support but do not replace the proof.

## Originality — PASS, with residual priority risk

Müller and Šebek (arXiv:2607.08551v1) introduce this weighted quorum setting and state a first-order universality theorem for homogeneous clocks. The new claim is at the fluctuation scale, where the Zipf \(\ell^2\) boundary separates Gaussian and non-Gaussian limits. Own historical findings on the same source concern finite macroscopic atoms or aligned rate-and-weight Zipf models; neither implies the homogeneous diffuse-weight second-order theorem. Searches in the research index and external literature found no direct statement of this phase transition. Withers–Nadarajah's 2010 Edgeworth theory assumes bounded unnormalized weights, while the non-Gaussian harmonic endpoint has non-Lindeberg weights. Allouche–Gobet's 2026 weighted-quantile theory is a serious neighboring literature but its full text was inaccessible. The motivating paper's latter sections were also inaccessible; consequently hidden exact prior coverage is possible, and formal historical priority is not settled.

## Value — PASS

A diffuse-weight hypothesis alone gives the same deterministic first-order quorum time for all weight profiles. The theorem identifies precisely why this universal behavior masks distinct limiting fluctuation shapes, gives their entire ranked-coefficient limit family and an explicit power-law transition at \(\rho=1/2\). The harmonic endpoint's exact non-Gaussian fourth-cumulant signature \(-4/5\) supplies a concrete statistical distinction. This is a natural and reusable description of the uncertainty of threshold completion, not merely a small improvement to a known numeric bound.

Self-review: passed. Independent audit: not yet performed.
