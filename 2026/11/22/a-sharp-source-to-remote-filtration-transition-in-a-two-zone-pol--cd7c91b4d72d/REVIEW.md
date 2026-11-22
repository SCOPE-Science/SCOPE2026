# Scientific review

## Correctness — PASS

The model matrix has strictly negative trace and positive determinant for every feasible allocation; the steady state is unique and stable. Exact Cramer's-rule concentrations give the stated three objectives. The source objective has a strictly positive derivative; the remote objective has a unique quadratic-denominator maximum at equal split; and the total objective has a strictly increasing derivative numerator, giving one sharp boundary-to-interior transition and a global, never half-or-more remote optimum. The boundary equality case and high-budget limit are proved. The dependency-free checker reproduces diagnostics but is not a substitute for the analytic proof.

## Originality — PASS (provisional priority)

The fixed-sum continuous filtration optimizer, three-objective separation and sharp activation threshold were not found in the searched mathematical findings or the inspected published and openly available studies. Du et al. study two-zone pollutant exposure and removal; Novoselac and Siegel explore cleaner placement; Kikumoto and Ooka optimize spatial placement by adjoint methods. A recent Airgle article already contains the *same two-zone equations* and compares concentrated versus equal-split filtration, including source-only examples. The claim is therefore confined to the precise continuous optimizer, threshold and asymptotics, not the model, discrete cases or concept that allocation matters. Broader engineering optimization literature may contain an equivalent argument.

## Value — PASS

A fixed filtration capacity is a natural investment constraint and a steady whole-building burden is a meaningful, distinct metric from source or protected-room concentrations. An exact budget threshold specifies when cleaning in a non-emitting connected room first helps the whole-building average; the optimal split strictly improves even on the two discrete policies in an existing numerical benchmark, while local exposure objectives disagree. The asymptotic benefit remains a positive fraction, so it is not solely an infinitesimal perturbative effect. This is a motivated model-specific benchmark, not an empirical device recommendation.

## Sources and limits

Du et al. (2012), doi:10.3390/ijerph9124639; Novoselac and Siegel (2009), doi:10.1016/j.buildenv.2009.03.023; Kikumoto and Ooka (2022), doi:10.1002/2475-8876.12318; Airgle multiroom comparison (online, accessed 2026). Distinct model/variables and exact implication comparisons are documented in AUDIT.json. Residual priority risk is the possibility of a general analytic resource-allocation theorem in unsearched literature. No independent scientific audit is claimed.

Self-review: passed. Independent audit: not yet performed.
