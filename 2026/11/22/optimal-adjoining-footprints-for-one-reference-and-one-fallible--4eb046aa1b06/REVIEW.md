# Scientific review

## Correctness
**PASS.** The probability objective follows directly by conditioning on the reference's perfect detection within its footprint. Every overlap can be eliminated with a strict gain to the auxiliary-only portion. Every positive gap can be decreased by moving one interval closer to the symmetric unimodal target prior. For touching intervals, the derivative-to-density ratio is strictly decreasing under strict log-concavity, with opposite signs at zero and the footprint radius. This proves global uniqueness up to reflection and the monotonic auxiliary-reliability law. The Gaussian quadratic transformation is exact. Supplementary `checker.py` passed 26,979 numerical assertions.

## Originality
**PASS on inspected evidence, historical priority provisional.** The 2024 camera-trap study concerns encounter-rate precision under simulated layouts, not an exact asymmetric initial-detection optimizer. Litvak et al. give the two-identical-sensor objective and a bounded-field sufficient no-overlap condition, but not an even-log-concave unequal-reliability uniqueness theorem or the Gaussian closed form. Wettergren and Costa give a numerical sensor-location optimization approach. The present exact comparison has different assumptions and proves a new-to-these-sources structural rule; it does not claim novelty for basic log-concavity or rearrangement principles. A broader, uninspected sensor-location theorem may still subsume the result.

## Value
**PASS.** Sensor clustering versus spreading is a documented field-design choice. A natural reference-plus-auxiliary arrangement has a complete global spacing rule, not merely a local derivative condition: all overlaps and gaps are suboptimal, and the optimal relative translation is unique, reliability-monotone, and explicit for a Gaussian location prior. That removes a two-dimensional nonconvex search for this particular benchmark, while precisely exposing its practical limitations.

## Limitations
The reference camera's perfect sensitivity and hard interval footprint are idealizations; the theorem does not address detection-rate precision, field calibration, unequal footprints, correlated targets, or unrestricted reliability pairs. The cited literature is not an exhaustive priority proof. Only self-review was completed.

Self-review: passed. Independent audit: not yet performed.
