# Scientific review

## Correctness — PASS

The exact source mass function is normalized by its standardization. Full support proves the strict \(0<R_n<n\) bound. The beta-binomial first and second factorial moments give a rare-count expansion at fixed \(q\ne0\), yielding the two leading mass deviations and therefore the sharp total-variation constant. The unweighted beta-binomial moment identity approaches the upper endpoint; a diagonal selection in \(q\) and \(\beta\) approaches the lower endpoint; connectedness and continuity fill the complete interval. Exact rational and asymptotic checks were replayed with `check_dispersion.py`. Risks: finite checks do not prove the infinite statements; the analytical asymptotic is pointwise in fixed parameters.

## Originality — PASS (best knowledge)

Reyes et al. (2024), especially their Proposition 1, Proposition 2, Figure 3 and conclusions, already give the mass function, moment formulas, and coefficient-of-variation comparisons. The new theorem is not the weighted construction, nor a new normalization, nor the elementary bounded-support variance inequality. It establishes the sharp entire **equimean-binomial** dispersion image and a quantitative rare-count Bernoulli transition not reported there. The 2020 Gómez-Déniz et al. model is Poisson-based with infinite support and a distinct dispersion benchmark, and Simone's 2022 discretized-Beta model is a different distribution. Query comparisons with relevant mathematical records found no statement covering these results. Residual risk: an unindexed paper or a broadly stated generic quadratic-tilting theorem may provide equivalent coverage; independent priority review is needed.

## Value — PASS

The range of a model's variance relative to the binomial having its own mean is a natural statistical-model-selection invariant. Determining its **complete sharp image** resolves whether the Reyes et al. model, originally motivated by overdispersed binomial data, is intrinsically restricted to overdispersion: it is not. The universal Bernoulli rare-count limit identifies a concrete mechanism for severe underdispersion at every nonzero tilt. This is a motivated structural classification, not a choice of arbitrary parameters or a numerical recomputation.

## Scope and risks

No statement is made about fixed-mean or fixed-shape dispersion regions; no numerical check is used as an asymptotic proof. The published source's moment calculations and the elementary universal variance bound are acknowledged. The work has no independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
