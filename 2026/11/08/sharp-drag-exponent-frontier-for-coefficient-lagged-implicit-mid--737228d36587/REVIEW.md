# Self-review

## Correctness (C) — PASS

The specified stage solver is derived, rather than assumed: when both two-stage midpoint rows are \((1/4,1/4)\), identical prior stage guesses yield identical frozen drag coefficients, which yield the common scalar stage relation \(y=x/[1+h(1+\epsilon)\alpha(z)/2]\). The positive implicit root is unique because \(yD_m(y)\) increases strictly. The logarithmic slope factorizes as two strictly increasing fractions multiplied by \(m\), proving the global logarithmic contraction for \(0<m\le1\) and the unique repelling-root transition for \(m>1\). An anti-monotone-iteration argument proves that the nonconvergent regime has actual period-two limits; it is not inferred from the derivative alone. For \(m=2\), eliminating the two-cycle equations determines its existence, values and multiplier exactly; the neutral endpoint is handled by absence of any distinct two-cycle. Exact symbolic identities and numerical stress tests are reproduced by `verify.py` and support, rather than replace, these arguments.

## Originality (O) — PASS, with priority limits

The starting 2026 source's substantive method and stage coefficients were inspected. Its analyses and experiments treat nonlinear coefficient Picard iteration but do not assert the exact square-root global log-contraction theorem or the growth-exponent/2-cycle frontier for the specified scalar midpoint case. The related 2025 GIRK paper treats drag solvers but was not found to imply this state-dependent stage-iteration classification. General fixed-point iteration and period-doubling theory are longstanding; those tools alone do not supply the particular gas--dust stage identification and exponent dichotomy. Searches of published mathematical records, source/claim aliases, broader fixed-point theory and accessible prior findings found no covering statement. Absence from searchable records does not establish priority: an earlier equivalent reciprocal-quadratic-map identity or a less visible coefficient-lagging study could subsume the quadratic corollary, and some older full texts were not completely examined.

## Value (V) — PASS

The threshold \(m=1\) is not an arbitrary parameter slice: it is exactly the drift dependence of the Epstein--Baines stopping-time approximation used in the motivating 2026 method. It gives a no-step-restriction convergence guarantee for this selected midpoint nonlinear stage solve, together with a computable log-error contraction bound. The companion sharp superlinear counter-regime explains how a unique nonlinear implicit solution can coexist with a stable Picard coefficient oscillation, and the exact \(m=2\) frontier provides a reproducible stress test. The result does not overclaim global solver convergence, generic numerical stability or a new principle of one-dimensional dynamics.

## Limits and prior-work qualification

Closest method sources: Chen et al. (2026), arXiv:2610.18979v1, Sections II.4--II.5 and III.3; Tedeschi-Prades et al. (2025), arXiv:2511.07562, introduction and methods; Chan--Mulet (1999) and Mezzadri--Galligani (2017) on different lagged diffusivity settings. Specific applications of general anti-monotone fixed-point theory may constitute implicit prior coverage, and no assertion of universal novelty is made. The result is mathematically supported within the stated scalar scope; no independent verification has occurred.

Self-review: passed. Independent audit: not yet performed.
