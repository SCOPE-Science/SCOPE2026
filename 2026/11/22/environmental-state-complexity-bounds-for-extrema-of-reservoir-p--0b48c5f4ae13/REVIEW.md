# Scientific review

## Correctness — PASS
The stationary mean is well defined because every regime has positive flushing and the environmental generator is irreducible. The conditional moment equations, detailed-balance symmetrization and zero-count induction establish the bound for all finite \(n\ge2\). The rational three-regime example and its unique maximum have independently reconstructed coefficient identities and exact stationary-balance checks in `checker.py`. Finite tests are supplemental, not an infinite proof.

## Originality — PASS relative to inspected evidence, provisional
Maran (2002) studies randomly varying flushing and residence time. Sinzger-D'Angelo et al. (2023) establish the broader stationary-mean resolvent, and explicitly point to older queueing formulas; that general formula is not claimed as novel here. Inspected theorem statements do not supply the reversible \(n-2\) switching-speed extremum bound or the strictly increasing three-regime hydrological counterexample. Published mathematical research searches for Markov-modulated concentration, environmental-state count, switching-speed extrema and stationary mean found no statement implying the new extremum-count conclusion. An inaccessible 1986 queue primary source, incomplete 2011 empirical source and general Chebyshev-kernel priority remain risks. A failed search is not a proof of priority.

## Value — PASS
Concentration responses under changing environmental persistence need not be monotone, even when both loading and flushing rise with discharge. The universal bound makes a testable distinction between two and three hydrological regimes and limits the number of possible finite switching-rate optima in any reversible finite-state model. The example has a substantial exact 16.7% mean amplification over the slow-switching limit. It is not a field forecast or a general result for nonreversible flow states.

## Source and scope limitations
- Maran (2002), doi:10.1029/2001WR000975, relevant publisher HTML read.
- Sinzger-D'Angelo et al. (2023), doi:10.1007/s00285-023-01973-x, full open-access mathematical sections read.
- Meybeck and Moatar (2011 online), doi:10.1002/hyp.8211, abstract and references only; the complete paper was not used to infer noncoverage.
- Older O'Cinneide–Purdue (1986) theorem was identified via the 2023 full text but was not directly inspected.
- All data and rates in the example are idealized, with no empirical calibration; the stationary mean cannot be equated with health impacts.

Self-review: passed. Independent audit: not yet performed.
