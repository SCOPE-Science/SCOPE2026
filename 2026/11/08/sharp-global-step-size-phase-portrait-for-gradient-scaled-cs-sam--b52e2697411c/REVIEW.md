# Scientific review

## Correctness
**PASS (self-review).** All dimensions and hypotheses are explicit: a scalar convex quadratic, positive curvature-scale slope, nonnegative perturbation, positive step and exact arithmetic. Substitution yields the stated rational map. Strict decrease of \(F_\rho\) and increase of \(tF_\rho(t)\) produce the global amplitude comparison, including overshoot cases. At the critical step, the reciprocal-increment argument proves the sharp \(1/k\) coefficient for nonterminating orbits. At larger steps, the unique positive fixed amplitude is shown globally attracting except finite zero-hit cases. The exact rational witness and 11,865 supplemental checks in `CHECK.py` agree with the analytic proof. The checks alone do not prove infinite-time convergence.

## Originality
**PASS (qualified).** The 2026 CS-SAM source introduces the algorithm and gives general sufficient steps but not the exact global rational-map classification with positive gradient-dependent scaling. Its conventional SAM two-cycle and constant-scale CS-SAM example are not equivalent. Earlier fixed-radius SAM work gives cycles for a different iteration; existing gradient-scaled descent analysis gives complexity bounds for a single normalized step. A separate 2026 adaptive-radius paper updates the perturbation based on past sharpness and uses a different map. Searches of public mathematical research records and relevant literature did not identify the full claimed equivalence; this is a best-knowledge comparison, not proof of historical uniqueness. A possible unindexed scalar rational recurrence remains a residual risk.

## Value
**PASS.** The sharp global parameter boundary answers when a curvature-scaled perturbation algorithm converges to its true minimizer versus a stable, nonoptimal oscillator. It exposes a stabilizing-but-nonconvergent effect of positive gradient-dependent scaling: supercritical steps remain bounded, unlike their constant-scale counterpart, while large perturbations exceeding conservative general theory can still be convergent on this exact test class. The critical \(1/k\) rate and explicit limit-cycle amplitude support quantitative step-size diagnostics beyond a routine local Jacobian calculation.

## Literature and limitations
Relevant inspected primary sources: Oikonomou--Loizou (arXiv:2610.29192v1), Bartlett--Long--Bousquet (JMLR 24(316), 2023), Vankov and collaborators (arXiv:2410.10800v3), Rossi--Campelo--Oliveira (arXiv:2610.20415v1). Proof scope is scalar, deterministic, exact arithmetic with a strictly positive curvature-scale slope; it does not establish global convergence in the motivating paper's full objective classes. The novelty check cannot exclude inaccessible or unindexed equivalent analyses.

Self-review: passed. Independent audit: not yet performed.
