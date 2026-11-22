# Scientific review

## Correctness

**PASS.** A killed Dirichlet-system Schur complement yields the exact gateway identity \(P=(d+\beta z)/(d+\kappa+\beta)\), where \(\beta=\alpha/(1+\alpha R)>0\), so the sign of adding a side route is precisely the sign of \(z-d/(d+\kappa)\), independent of entry strength. The reflecting path recurrence gives \(z=\cosh(\theta/2)/\cosh((n+1/2)\theta)\). Strict monotonicity from a killed first-passage representation proves a unique rate threshold; the hyperbolic equation proves monotonicity in the number of stepping stones and the \(n^2\) asymptotic. A standard-library rational checker confirms 270 exact examples, further explicit expressions and asymptotic illustrations. The proof, not its finite tests, supports the quantified result.

## Originality

**PASS on inspected evidence, subject to historical priority risk.** Kervellec et al. (2024) model occupancy using a commute-time-based accessibility proxy and do not derive a mortality-conditioned new-route criterion. Balakrishnan et al. (2019) establish mortal first-passage methods and scaling, which cover techniques used here but do not supply the stated all-entry-strength route-installation classification and sharp quadratic permeability threshold. Gounaris and Katifori (2023) address Braess-type behavior of mean first-passage exploration time without independent killing, not the mortal probability criterion. Classical electrical monotonicity and Markov resolvents are antecedents, not claimed novelties. Searches for mortal-walk edge-addition paradoxes, killed target hitting, and stepping-stone thresholds found no directly covering statement. An unknown specialized result using general resolvent machinery remains possible; independent validation and exhaustive historical priority analysis have not occurred.

## Value

**PASS.** Electrical conductance increases under every route installation in this family, yet the endpoint-success probability can decrease. The exact threshold isolates the parameter determining that discrepancy and its independence from entry conductance; the quadratic law quantifies the permeability needed as corridors grow longer. This is a motivated limit on using static circuit-based connectivity as a proxy for viability-limited dispersal, without presenting a field-level intervention prescription.

## Closest literature and limitations

Kervellec et al., *Methods in Ecology and Evolution*, 2024, https://doi.org/10.1111/2041-210X.14418 (ecological connectivity and occupancy). Balakrishnan et al., *Physical Review E*, 2019, https://arxiv.org/abs/1901.10226 (mortal random walks). Gounaris and Katifori, 2023, https://arxiv.org/abs/2303.02146 (exploration-time Braess analog). Specific limitations include homogeneous mortality, no empirical calibration, and no conclusion about commute-time distance. The searched literature is not a complete historical bibliography.

Self-review: passed. Independent audit: not yet performed.
