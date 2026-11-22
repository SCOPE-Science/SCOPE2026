# Review of the distribution-free sex-search mating-count comparison

## Correctness — PASS
The hypotheses explicitly require equal numbers of males and females, reusable males, independently sampled search lifetimes, and mutually independent rate-\(a\) pairwise Poisson contacts. The two count laws follow by conditioning on the sum of the male lifetimes and by independent thinning of each female's encounter stream. Their zero masses coincide exactly. The probability-mass ratio is a normalized moment sequence whose first nontrivial term is strictly below one by strict Hölder; moment log-convexity makes its sign relative to one cross only once. The resulting single crossing establishes strict upper-tail domination at every threshold \(2,\ldots,n\). All deterministic and one-pair boundary cases are addressed separately. The accompanying exact-rational checker passed 13,754 assertions and independently checks the explicit exponential example. The finite checks do not replace the argument for arbitrary distributions.

## Originality — PASS on inspected evidence, with priority risks
The nearest directly relevant source, Byers (2012), treats male- and female-searching systems in spatial correlated-random-walk simulations and compares percentages mated. It neither supplies the arbitrary-lifetime count laws nor the zero-mating identity and exact all-threshold ordering in the independent Poisson-encounter reduction. Byers (2007) treats male-searching moths only. Barclay and van den Driessche (1983) analyze population-control equations rather than the full paired stochastic count laws, on the available abstract. Searches for the same claim under Laplace-transform, binomial-mixture, stochastic-order, competitive-attraction, and sex-searching terminology found no equivalent statement in inspected results. General moment log-convexity is established mathematics, not claimed as new. The 1983 full text and some broader stochastic-order literature remain priority risks; an unsuccessful search is not proof of priority.

## Value — PASS
The biologically motivated distinction between trapping searching males and trapping searching females changes not just the expected number of mates but the tail distribution of distinct successful matings. A complete distribution-free classification shows that zero-mating suppression probability is identical in both mechanisms, yet all higher mating thresholds systematically favor reusable male searchers whenever exposure duration is heterogeneous. It gives an exact qualitative benchmark for interpreting sex-search comparisons across different trapping-time laws and deterministic horizons. It does not claim a field-ready model or that the same ordering survives spatially correlated movement, unequal pair rates, or limits on male mating capacity.

## Closest literature and limits
- Byers (2012), *Entomologia Experimentalis et Applicata* 145, 228–237, https://doi.org/10.1111/eea.12006 (complete accessible article inspected).
- Byers (2007), *Environmental Entomology* 36, 1328–1338, https://doi.org/10.1603/0046-225X(2007)36[1328:SOMDAM]2.0.CO;2 (complete accessible article inspected).
- Barclay and van den Driessche (1983), *Researches on Population Ecology* 25, 105–115, https://doi.org/10.1007/BF02528786 (abstract inspected; complete text not obtained).

The theorem is specific to pairwise independent Poisson encounters, symmetric rates and independent search lifetimes. It asserts no empirical validity and no independently established literature priority.

Self-review: passed. Independent audit: not yet performed.
