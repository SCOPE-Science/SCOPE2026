# Scientific review: two-harmonic bidirectional self-calibration

## Correctness — PASS

The stated domain includes a smooth positive field, a common positive first-order length, periodic steady-state scans at equal known speed, a constant unknown spatial offset, independent positive gains and arbitrary baselines. Fourier integration proves the transfer factor and exact cancellation of the unknown source coefficient. The ratio phase invariant eliminates the offset and has derivative \(-12\ell^2/[(1+\ell^2)(1+4\ell^2)]<0\), taking the exact open range \((-\pi,0)\). It gives an invertible rational cubic, followed by exact gain and registration recovery. Necessity and sufficiency concern the two nonzero complex harmonic ratios, not arbitrary full traces; the constructed positive two-harmonic field realizes all such ratio data. A one-harmonic family proves sharp failure. The exact rational witness, long-/short-length asymptotics, and higher-harmonic cross-checks are consistent. Residual risk is model mismatch/noise rather than an unproved mathematical step; numerical tests supplement, not substitute for, the proof.

## Originality — PASS on inspected evidence

Hübner et al. (2014) explicitly develops first-order moving sensor corrections, demonstrates opposite-direction spatial effects, and determines response times through separate laboratory reference steps. Buehler et al. (2021) characterizes instrument e-folding times using calibration gas; Hofman et al. (preprint 2024; journal 2024) evaluates portable monitoring under reference comparison, GPS and drift effects. None of the inspected contents supplies the simultaneous unknown-field/unknown-registration inverse from two Fourier harmonics, its exact feasible ratio region, or its minimality and boundary conditioning. General transfer-function and Fourier-phase identities are classical and not claimed as original. Related published mathematical records on phase ambiguity and bidirectional tomography involve different measurements and do not logically imply this theorem. Full historical uniqueness is not certified: older blind identification literature and some full texts remain a priority risk.

## Value — PASS

Mobile monitoring along varying pollutant fields creates genuine response-time, registration and gain-confounding problems. The complete theorem explains a viable information source independent of the unknowable pollutant field: phase curvature across two harmonics in opposite-direction scans. Its exact feasibility condition is falsifiable, gives the minimal harmonic requirement, and exposes catastrophic parameter conditioning at both response-time extremes. This is a natural and potentially reusable identifiability benchmark; no unsupported claim about field performance, deployability or novel first-order filtering is needed.

## Literature and limitations

Primary environmental measurement sources: https://doi.org/10.5194/amt-7-2967-2014, https://doi.org/10.5194/amt-14-995-2021, https://doi.org/10.20944/preprints202406.1513.v1, https://doi.org/10.3390/s24175653. The earliest verified publicly posted motivating version is the preprint dated 21 June 2024. The older 2014 work's complete primary PDF text was inspected, including the laboratory-response and opposite-direction correction sections. The 2024 journal abstract and public preprint record were inspectable, but complete preprint text was unavailable; the latter empirical work does not resolve the mathematical priority question. Full prior-art coverage is not represented as certain.

Self-review: passed. Independent audit: not yet performed.
