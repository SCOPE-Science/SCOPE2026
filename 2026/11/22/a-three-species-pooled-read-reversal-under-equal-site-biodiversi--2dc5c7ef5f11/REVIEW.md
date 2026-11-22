# Self-review

## Correctness

**PASS.** The event of complete three-taxon recovery in two first-site reads is exactly the disjoint union of the outcomes \(BC\) and \(CB\), giving \(2bc\). In the pooled design, four labeled reads containing three taxa have multinomial patterns \((2,1,1)\) in each of three orders of the repeated taxon, giving \(12uvw\). Subtraction gives \(bc(3a-1)/2\) with strictly positive multiplier. The single-taxon inequalities, sharp two-taxon obstruction, eventual large-depth reversal and optimized-split qualification have independent elementary proofs. Rational enumeration in `checker.py` passed 1,771 compositions and additional assertions; it supports, but does not prove, the real-parameter theorem. Boundaries \(bc=0\) and the tie at \(a=1/3\) are stated explicitly.

## Originality

**PASS within inspected evidence, priority provisional.** Exact source/claim, equivalence, broader-coverage and table comparisons found no prior statement implying simultaneous strict marginal-detection domination by equal-site sampling but a reversed three-species complete-inventory probability, with the sharp \(a=1/3\) boundary. Sato et al. (2017) and Courtaillac et al. (2024) concern empirical pooled-read detection; Altermatt et al. (2023) studies sampling-effort dependencies; an inspected two-habitat biodiversity finding treats **without-replacement expected richness**, and an inspected three-species coupon-collector finding treats **variance of completion time**. The relevant underlying probability calculations are classical. Direct navigation of one older full source was restricted, and unrestricted mathematical priority has not been independently established.

## Value

**PASS.** The example addresses a meaningful distinction between an eDNA survey's per-taxon sensitivity and a complete multi-taxon inventory objective. It proves that marginal-detection comparisons cannot decide the joint objective once three taxa are involved, isolates the smallest possible taxon count, and gives an exact parameter threshold independent of the two less widespread taxa's imbalance. The contrasting high-depth and optimized-allocation results prevent a misleading unconditional recommendation for pooling. These make it a motivated design-boundary counterexample rather than merely a computational curiosity.

The biological read-label model deliberately excludes real capture, extraction, amplification and contamination effects; no practical superiority is inferred.

Self-review: passed. Independent audit: not yet performed.
