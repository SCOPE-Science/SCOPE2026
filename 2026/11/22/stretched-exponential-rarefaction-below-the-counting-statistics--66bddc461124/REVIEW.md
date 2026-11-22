# Scientific review

## Correctness — PASS

The proof starts from the *exact* killed Brownian kernel and the stationary equilibrium-renewal mixture, valid when the population exceeds two. Integrating the kernel over the shrinking interval gives the exact conditional binomial parameter, including its absorbing-image correction. A uniform Gaussian-tail estimate controls that correction for all young ages, and the complementary-error-function expansion gives the sharp exponent for the exceptional older ages. A polynomially shrinking bracket about the unique age solving the count constraint separates binomial fluctuation cost from excursion-survival cost, proving the two-sided logarithmic equivalent. Conditioning on the rare event and comparing exponential speeds proves age localization. This holds for each fixed parameter pair in the specified open domain. Numerical quadratures and binomial CDF calculations in `verify.py` independently check normalization, conditional probability and the direction of asymptotic convergence; they are not treated as an infinite proof.

## Originality — PASS (qualified)

The primary full article, Biroli–Majumdar–Schehr, *First Passage Resetting Gas*, https://arxiv.org/abs/2512.00440, Eqs. (10)–(15) and (36)–(38), already supplies the exact stationary mixture and the lower edge \(\operatorname{erf}(\ell)\). The present claim is not for those known facts, but for the sharp **finite-population, subedge, macroscopic core-count** logarithmic rate and its conditioned clock. The article explicitly stops at the statement that those rarefied configurations are very unlikely. The more general CIID paper https://arxiv.org/abs/2307.15351 treats the method of mixing, not the size-dependent event-driven tail. Research records on mirror-threshold single-digit counts and fixed-population far-left excursions do not imply a rarefaction law for \(\kappa N\) core particles. Searches found no equivalent or stronger theorem, but absence from the inspected index is not proof of priority. Unindexed equivalent work, potential uninspected supplements, and the exact-integral implicit reducibility are residual risks.

## Value — PASS

The positive lower support endpoint from the original paper leaves an identifiable mathematical gap: how rapidly does its apparently forbidden region become accessible at finite population size? The result shows a continuum of nontrivial fractional exponents, rather than a naive speed-\(N\) binomial large deviation, and identifies the physical rare-event mechanism through the reset age. This describes measurable finite-size rarefaction in a natural many-particle model and distinguishes atypical long excursions from ordinary fluctuations. No arbitrary numerical slice, parameter tuning or routine normalization check is offered as the contribution.

Self-review: passed. Independent audit: not yet performed.
