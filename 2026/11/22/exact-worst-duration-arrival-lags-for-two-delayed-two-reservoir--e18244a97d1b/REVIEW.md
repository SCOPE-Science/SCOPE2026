# Scientific review: two-pulse threshold-exceedance duration

## Correctness — PASS

The exact post-arrival factorization is algebraically verified. The scalar multiplier decreases strictly for positive lag. The single-pulse threshold crossings partition the lag domain into three intervals with respectively decreasing, strictly increasing, and decreasing exceedance durations. On the middle interval the final downward level crossing occurs more than one reservoir time after the delayed pulse and has positive derivative with respect to lag. The two global candidates and all boundary cases therefore follow analytically, not from numerical search. The standard-library standalone checker also supplies an exact-rational exponential certificate for the strict \(1/4\)-level witness, as well as 1,100 independently bracketed numerical level-set comparisons and 8,008 grid comparisons. Numerically sampled cases alone are not the proof.

## Originality — PASS on inspected evidence

The source literature establishes the two-reservoir/gamma hydrograph, compound-event timing, high-water duration, and threshold-based hydrological analysis. Full accessible article text was inspected for Lyddon and colleagues (2022), Gnecco, Palla and La Barbera (2018), and Lyddon and colleagues (2024). Their investigated functionals are driver coincidence, hydrograph peaks, and simulated inundation area, respectively, not maximization over lag of the summed hydrograph's total strict superlevel duration. Closest mathematical results concerning shifted Nash hydrographs address local crest counts for three/four-stage cascades and different-rate two-stage mixtures. Three relevant full mathematical manuscripts were checked and do not contain the same objective or the exact two-candidate optimization theorem. An exhaustive priority claim cannot be made: translated-density level-set inequalities, generalized temporal risk measures, and historical flood-routing calculations remain residual risks.

## Value — PASS

Time spent above a hazardous discharge threshold is a natural severity metric different from peak flow. The exact classification reveals a nonintuitive planning distinction: synchronous inputs maximize the instantaneous peak but can be strictly inferior for total exposure duration, and only two mathematically interpretable arrival lags need comparison across a continuous control range. The demonstrated relative duration difference exceeds 37% at one normalized threshold. The model is a tractable ideal benchmark, not a prediction for a particular estuary.

## Limits and provenance

Equal instantaneous pulses, a common linear two-reservoir response, zero baseflow, an infinite observation horizon, and a discharge rather than inundation threshold are assumed. The number of threshold values where the two candidates tie is not classified. Independent domain-specialist review, reproducibility outside the stated implementation, and empirical calibration are not asserted.

Self-review: passed. Independent audit: not yet performed.
