# Scientific review

## Correctness

**PASS.** The proof derives the exact scalar score from the published disease-free equilibrium and sufficient invasion inequality. Differentiation reduces its sign to a sum of two power laws. For positive density dependence, the derivative has at most two roots; a unique minimum of the auxiliary function gives a necessary-and-sufficient strict two-turning-point criterion on the supported interval. Denominator positivity and endpoint/equality cases are explicit. A standalone standard-library checker verifies 48 exact rational assertions including each of the 18 supported integer degree classes; there is no reliance on approximate plots to establish strict inequalities.

## Originality

**PASS, with qualified priority.** Ripoll and colleagues (2015), equation (9) and figure 3, provide the same **underlying sufficient-screening ratio**, and the earlier Avinyó–Pellicer–Ripoll–Saldaña chapter provides the analogous formula. Both discuss that its maximum may occur at the minimum or an intermediate degree. Neither inspected presentation states a sharp double-turning criterion or demonstrates two separated subsets of discrete degree classes passing one invasion screen. Juher and Mañosa (2014) prove a related spectral sufficient condition but assume constant migration. This result does not claim originality for the general model, its mean-field equilibrium, or the screening formula. The derived morphology is relatively elementary once that formula is known; an unlocated earlier derivation remains a real priority risk.

## Value

**PASS.** The result addresses a concrete limitation of diagnosing epidemic onset by ranking connectivity: for a natural truncated scale-free degree law, higher-risk classes can be separated by a class failing the same guaranteed-instability screen. The exact criterion identifies the necessary role of the within-degree return probability and the exponent above one, and the finite example proves the phenomenon in every degree class without a numerical scan. This is an interpretable boundary of a commonly used early-invasion screening method, not a general epidemiological prediction.

## Limits

The source screening ratio is sufficient, not necessary, for disease-free instability; its classwise pass/fail set is not a set of realized outbreaks or exact local reproduction numbers. The result concerns degree-based annealed mixing, not arbitrary finite network realizations, and the continuous turning-point theorem is auxiliary to the finite degree classification. The originating expression in prior literature limits the claim's conceptual independence and leaves residual historical-priority uncertainty.

Self-review: passed. Independent audit: not yet performed.
