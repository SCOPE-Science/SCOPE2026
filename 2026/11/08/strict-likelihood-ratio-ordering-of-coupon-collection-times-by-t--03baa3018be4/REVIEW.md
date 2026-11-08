# Self-review

## Correctness — PASS

The exact joint law counts sequences ending with the first occurrence of the final coupon. The analytic proof uses a stated Toeplitz-order-two lemma, justified through coefficient-ratio monotonicity and convolution, then identifies a strictly positive term in every marked-row determinant. It treats the two-coupon boundary separately, keeps the strict positive-weight assumption explicit, and proves the conditional likelihood-ratio and stochastic consequences. `check.py` has independently recomputed 30,533 exact rational assertions and enumerated short sequences; these finite checks confirm examples, not the infinite proof.

## Originality — PASS (qualified)

Four inspected primary works concern unequal coupon collection: Ferrante–Frigo (2012), Shank–Yang (2013), Anceaume–Busnel–Sericola (2014), and Anceaume–Busnel–Schulte-Geers–Sericola (2015). They analyze unmarked waiting times, quota expectations, or stochastic optimization by varying the probability vector, rather than the joint marked distribution of final type and completion time. Searches also included equivalent likelihood-ratio, reverse-total-positivity and conditional-last-coupon formulations. None of the inspected statements directly covers the strict all-time row determinant in the present result, and accessible related claims concern different stopping events. The potential for implicit older coverage through classical occupancy/total-positivity results remains a priority risk. This review is not an independent novelty certificate.

## Value — PASS

Conditioning on the final type is a natural question in heterogeneous sampling and completeness monitoring. A universal strict likelihood-ratio order gives simultaneous control over all conditional tails and increasing risk functionals, exceeding a single formula or pointwise example. It determines how the observed bottleneck label changes uncertainty about collection duration for every positive probability vector.

## Limits and sources

The analysis assumes iid single arrivals and strictly positive fixed label weights. The supplied finite computation is an independent reproducibility check, not a substitute for analytic reasoning. Historical priority beyond the inspected sources remains uncertain. Primary literature and exact publication information are cited in `RESULT.md`; structured comparisons and residual risks appear in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
