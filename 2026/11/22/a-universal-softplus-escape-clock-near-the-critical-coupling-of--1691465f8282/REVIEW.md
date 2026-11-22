# Scientific review: A universal softplus escape clock near the critical coupling of a Gaussian map

## Correctness — PASS
The exact invariant-antidiagonal reduction and positive squared-amplitude recurrence are derived from the full map. The unique large root is correctly normalized. A compact-layer reciprocal-increment/Riemann-sum argument gives the softplus derivative, and a monotone comparison integral controls all earlier steps before the moving window. Sending the window boundary to negative infinity completes the argument for all fixed offsets; monotone inversion gives the scaled trajectory statement. The checks in `verify.py` pass, but the proof is analytic and not inferred from computations.

## Originality — PASS within inspected evidence
Soula et al. (2023) define the map and analyze its numerical basin geometry. The closest exact critical-coupling theorem (public finding f463338d3c52) gives the logarithmic escape rate at the *fixed* boundary, but not detuned first-passage limits. A related earlier same-map finding (483979a4-5fcf-47cd-ac80-e1a8fb37478a) already gives the subcritical antipodal cycle and is excluded from the new claim. Comparisons distinguish the new joint limit from both static conclusions. Unindexed analytical literature remains a priority risk.

## Value — PASS
The near-critical time-to-escape question is physically and mathematically natural because tiny positive detuning changes unbounded dynamics only after an exceptionally long transient. The full softplus function, not only a leading exponent, quantifies the crossover from the Gaussian feedback-dominated regime to linear coupling-driven geometric escape. The result connects a motivated published system and its sharp critical boundary to finite-observation asymptotics without claiming unrelated global dynamics.

## Limits
This is an invariant-antidiagonal theorem for fixed \(a>0\) and \(r_0>\sqrt2\), with exact arithmetic and positive detuning. No claim about arbitrary full-plane initial conditions or finite-parameter uniform error bounds is made. Priority is limited to inspected sources. Numerical tests are supplementary.

Self-review: passed. Independent audit: not yet performed.
