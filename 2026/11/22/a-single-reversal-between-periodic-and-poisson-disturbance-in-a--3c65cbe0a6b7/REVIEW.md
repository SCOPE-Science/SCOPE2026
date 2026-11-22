# Scientific review

## Correctness
**PASS.** Renewal-reward occupancy is derived directly from independent cycles. The phase-type suitability probability and both time-average formulae are computed exactly, including equal maturation and senescence rates. Uniqueness rests on a complete derivative-sign argument: the logarithmic elasticity of the comparison kernel decreases strictly from 1 to -2. A standalone checker verifies exact Markov balance equations, separate numerical quadrature and representative crossovers (12,924 assertions). The numerical diagnostics supplement rather than replace the proof.

## Originality
**PASS relative to the inspected literature, with historical-priority risk.** Earlier work established the ecological importance of successional duration distributions and disturbance schedules, and standard renewal theory supplies the occupation formulas. The inspected accessible primary full texts did not establish the exact single-crossing comparison of periodic versus Poisson disturbance for a temporary exponential two-stage suitability window. Earlier more general results may imply this law without presenting it in this form; full access to the particularly relevant Ellner–Fussmann paper was unavailable. Published mathematical searches and the comparison with other known resetting results did not identify direct or stronger coverage. The conclusion is a best-knowledge comparison, not proof of exhaustive priority.

## Value
**PASS.** Habitat maturity and subsequent senescence create a biologically motivated transient window; disturbance variability at a matched mean can either increase or decrease time spent in that window. The unique threshold completely classifies this minimal two-stage model and gives quantitative bounds for any pair of rates. This is useful as an analytically checkable baseline against which richer disturbance-management simulations can be assessed. It is not a claim about metapopulation survival or empirical policy effectiveness.

## Closest literature and limits
Ellner and Fussmann (2003) address successional stage durations and persistence. Wilcox et al. (2006) analyze disturbance and recovery with patch occupancy and extinction. Fraterrigo and Langille (2020) simulate stochastic versus deterministic disturbance effects on mature-stage coverage. These are not asserted to prove the single-crossing theorem; their detailed models and biological response quantities differ. The 2003 paper's full text was not accessible, leaving an explicit comparison risk. The models' disturbance clocks and age-stage mechanisms are not claimed to match observed systems.

Self-review: passed. Independent audit: not yet performed.
