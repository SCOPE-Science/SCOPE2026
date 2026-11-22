# Scientific review: superposed inverse-time creep modes

## Correctness — PASS

The full-domain claim follows from the identity \(R''=-2(S_1S_3-S_2^2)/S_1^3\) and Cauchy–Schwarz, with an equality case requiring all singular times to coincide. The secant argument uses strict concavity through the zero at the earliest singularity; it proves strict late prediction for every pair of observation times. In the two-mode case, explicit rational algebra gives the exact bias, and the derivative of the apparent exponent has a unique zero because \(H(z)=a(1-3z)-bz^2(3-z)\) decreases strictly on \((0,1)\). Its equal-amplitude and large-contrast consequences follow by substitution and asymptotic balance. A self-contained Python checker produced 14,809 passing deterministic diagnostic checks, which complement rather than substitute for the algebraic proof. No noise-robustness or physical calibration statement is claimed.

## Originality — PASS relative to inspected evidence, with residual priority risk

Fukuzono (1985, DOI 10.3313/jls1964.22.2_8) studies single-process inverse-velocity singularity laws; the accessible original paper's abstract and introductory material do not state this superposition theorem. Carlà et al. (2016, DOI 10.1007/s10346-016-0731-5) study filtering and empirical prediction errors from noisy inverse-velocity records, rather than deterministic composition of two different singular times. Ren et al. (2025, DOI 10.3390/app15137449) treat multiple monitoring points but not an additive scalar velocity from independent singular modes. The 2023 improved-inverse-velocity article (DOI 10.1080/19475705.2023.2239991) was available only in search-indexed portions, so no whole-document negative coverage claim is made. Results about summed inverse-time Omori decay also involve positive pole sums, but their reported phenomenon concerns apparent decay exponents under a distinct time domain and does not entail the rational late-forecast bias or the stated unique acceleration-exponent maximum. Generic Cauchy–Schwarz concavity is acknowledged as background and excluded from the originality claim. A broader unseen mathematical study of positive reciprocal-pole sums remains a priority risk.

## Value — PASS

The motivating data-analysis problem is scientifically consequential: slope-displacement measurements can mix kinematic modes, and extrapolating the reciprocal of the mixture is not the same as analyzing each mode. The result isolates two nontrivial structural artifacts—sign-definite late prediction and a spurious, potentially arbitrarily large acceleration exponent—without invoking noise or a change in any constituent physical exponent. It gives a complete exact benchmark for recognizing a limitation of a widely used phenomenological method and supplies quantitative bias and peak formulas. Its relevance is diagnostic, not operational: additive mode superposition may not hold in an instrument, the model diverges formally at failure, and the formulas do not establish safe warning times.

## Closest literature and limitations

- Fukuzono, 1985, https://doi.org/10.3313/jls1964.22.2_8 : original constant-exponent model, but not different-pole velocity aggregation.
- Carlà et al., 2016, https://doi.org/10.1007/s10346-016-0731-5 : filtering/line choice in empirical inverse-velocity forecasting; not the specified deterministic superposition classification.
- Ren et al., 2025, https://doi.org/10.3390/app15137449 : multiple measuring sites analyzed by inverse velocity, not the single summed-velocity signal.
- Relevant 2023 improvement, https://doi.org/10.1080/19475705.2023.2239991 : incomplete full-text access; residual historical-priority risk.

Unproved limits: heterogeneous arbitrary acceleration exponents, noisy inference, unknown mode decomposition, physical identifiability and field-calibrated reliability. These are not claimed.

Self-review: passed. Independent audit: not yet performed.
