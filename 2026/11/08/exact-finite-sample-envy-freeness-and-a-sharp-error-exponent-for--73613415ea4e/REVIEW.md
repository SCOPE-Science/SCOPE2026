# Review of the two-agent stochastic welfare-optimal fairness law

## Correctness

PASS. The utility differences of the two agents sum to the strictly positive total of itemwise value gaps, so their envy events are disjoint and symmetric. The one-agent difference has density \(1+z\) for \(-1<z<0\) and \(z\) for \(0<z<1\), yielding an exact transform. Expansion and bilateral Laplace inversion lead to a finite rational formula; exponential tilting followed by a nonlattice local limit theorem supplies the sharp prefactor. The relevant transform, sign factors, strict inequalities, and boundary \(m=1\) were reconstructed. Standalone rational and simulation checks passed; finite checks do not prove the asymptotic.

## Originality

PASS on the available public and published-record comparison, with residual priority uncertainty. Dickerson et al. (2014), Theorem 2, already show that allocating each good to the highest-valuing agent is eventually envy-free with high probability. Zeng and Psomas (2019), Proposition 3.1, restate qualitative eventual-fairness guarantees for online independent items. Manurangsi and Suksompong (2017) establish high-probability welfare-optimal allocations in a group model; Bai and Gölz (2021) address asymmetric distributions; Bu and Tao (2026) classify worst-case decision complexity. These do not imply a closed finite uniform-model probability or a sharp error exponent with prefactor. Published-record searches concerning random optimal allocations, exact probability, uniform values, and large deviations did not reveal direct coverage; the closest records concern ordinal assignment lotteries, not the present additive cardinal mechanism.

## Mathematical value

PASS. The calculation closes a natural quantitative gap between qualitative almost-sure eventual fairness and actual finite-item guarantees in the canonical stochastic model. It identifies exact rational reliability for every sample size and the sharp large-deviation law needed for tight confidence-level calibration. This is a motivated precise invariant, not a new claim of general welfare compatibility or a routine restatement of a Chernoff bound.

## Limitations and residual risks

The two-agent uniform and full-independence restrictions are essential to the stated exact formula. No independent audit or publication-priority certification has been performed, and equivalent calculations in unindexed literature remain possible. Numerical checks corroborate but cannot establish infinite-sample limits.

Self-review: passed. Independent audit: not yet performed.
