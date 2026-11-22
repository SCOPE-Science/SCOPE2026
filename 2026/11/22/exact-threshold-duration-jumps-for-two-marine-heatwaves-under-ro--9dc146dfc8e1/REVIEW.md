# Scientific review: rolling-window heatwave threshold durations

## Correctness
**PASS.** The mathematical object is an explicitly defined continuous boxcar integral of two equal rectangular inputs. The claimed four closed-superlevel formulas follow by substituting the complete five-piece one-pulse response and checking all ordered breakpoints, including coincidences, \(g=0\), \(q=d\), and \(g=W-q\). In the lower-threshold regime the equality plateau joins the event at the critical gap; in the higher-threshold regime the equality plateau is the entire event at the critical gap. The two right-hand duration drops are therefore exact. Independent exact-rational interval reconstruction agrees in 6,451 deterministic parameter cases. Those checks are diagnostic only; correctness is supplied by the explicit piecewise-affine analysis. No ecological or statistical inference is asserted.

## Originality
**PASS relative to material inspected, with historical-priority risk.** Liu et al. (2014) and the 2013 NOAA report define the 84-day and earlier 12-week accumulation kernels. Little et al. (2022) discuss artifactual persistence of apparent thermal stress due to the window, but do not state or imply the two-pulse threshold-set classification, a common exact critical gap for both threshold regimes, or the exact discontinuities of exceedance duration. Searches for threshold-duration, interval merging, rectangular pulses and boxcar averaging found related physical models and general signal-processing uses, but no implication covering the precise two-pulse result. The mathematical derivation uses standard elementary interval/convolution identities, which are not claimed as novel in isolation. Remaining risks include undiscovered generic signal-processing treatments of two-rectangle boxcar threshold sets and unexamined technical treatments of the DHW metric.

## Value
**PASS.** A duration-above-threshold statistic is a natural derivative of cumulative degree-heating-weeks stress monitoring, and two separated heatwaves are the minimal geometry that can produce apparent stress-duration merging or loss. The complete classification supplies a direct diagnostic for interpreting thresholds: the same fixed total heat dose can yield a one-episode versus two-episode classification or lose a severe-level exceedance; at the exact threshold separation the total time at/above the threshold is discontinuous as the separation increases. Opposite pretransition slopes and exact jump sizes make this a testable benchmark for checking numerical alert-processing conventions. The calculation is simple once the model is fixed, but it is a coherent complete classification of a physically motivated indicator, not a renamed algebraic identity or arbitrary parameter slice. Its utility is confined to the stipulated idealized metric and is not a bleaching forecast.

## Closest literature and limits
- Liu et al. (2014), DOI 10.3390/rs61111579, sections 2.3.2–2.3.4: daily HotSpot/DHW accumulation and additional operational alert criteria.
- Liu et al. (2013), NOAA Technical Report NESDIS 143, section 2.5: heritage DHW accumulation.
- Little et al. (2022), DOI 10.3389/fmars.2022.883271, detection-window analysis: established qualitative persistence of apparent heat stress.
- Relevant separate work on two rainfall pulses routed through a draining store concerns a different operator and does not imply this piecewise-linear boxcar duration law.

The model assumes sharp pulses, equal amplitudes, a window at least twice as long as one pulse and no observation noise. It is not NOAA's seven-day Bleaching Alert Area classification. Priority beyond examined literature and independent replication remain open.

Self-review: passed. Independent audit: not yet performed.
