# Scientific review

## Correctness — PASS

The constrained two-season recurrence linearizes under reciprocal biomass and admits a globally attracting positive two-cycle exactly when the product of the two seasonal low-density multipliers exceeds one. Substituting that cycle into the actual post-recruitment catches gives the stated rational sustainable-yield formula; its derivative has the sign of a constant minus a strictly increasing fractional-linear function. This proves a unique global optimum in all three endpoint/interior regimes, including equality cases. The exact interior regret follows algebraically from the stationary condition. Independent implementation from the same packaged paths verified 59,764 deterministic assertions, including exact rational checks. Numerical tests are diagnostic, not a substitute for the universal argument.

## Originality — PASS, qualified

A search of published mathematical findings using the precise fixed-aggregate-mortality, two-season proportional-escapement formulation and its aliases did not reveal a dominating exact result. The closest source is Bohner–Streipert (2016), Theorems 3.8–3.10, which covers periodic equilibria and unconstrained optimal effort, but does not give the constrained fixed-product phase law or the exact regret expression. AlSharawi–Rhouma (2010), sections 2–4, optimizes and compares periodic additive catch quotas rather than effort splits at fixed cumulative proportional mortality. Filar–Qiao–Streipert (2020) uses constant multiplicative harvest for risk assessment, and accessible material did not reveal optimization of two distinct harvest fractions. The latter full publisher text was incompletely accessible, so historical priority remains provisional. The theorem is not advertised as independent of general constrained nonlinear optimization techniques.

## Value — PASS

The biologically interpretable control constraint is fixed total instantaneous fishing hazard, whose allocation leaves the persistence criterion unchanged but strongly changes sustainable yield. The theorem supplies a complete global policy classification and finite-deviation loss, including sharp transitions to all-effort-in-one-season solutions. A concrete alternating-crowding example improves catch by roughly 67.78% compared with the equal-effort policy. This is a substantive benchmark for seasonal allocation under a specified nonlinear stock-recruitment mechanism, not a general empirical fishery recommendation.

## Risks and limitations

The model assumes exactly two seasons, fixed growth parameters, density-dependent recruitment of Beverton–Holt form, and post-recruitment proportional harvesting. It excludes implementation costs beyond fixed aggregate hazard, parameter uncertainty, stochasticity, minimum biomass constraints, and price discounting. Full examination of all historical fishery-optimization literature was not possible; the closest 2020 article was available mainly through accessible abstract and opening-page material.

Self-review: passed. Independent audit: not yet performed.
