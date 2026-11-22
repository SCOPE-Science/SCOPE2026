# Scientific assessment

## Correctness — PASS
The ODE has the all-ones feasible equilibrium by construction. Differentiating yields the stated exact stage blocks, and the fast block is semisimple with normalized left and right eigenvectors. Its spectral projection gives \(-2I+\delta C\) with no hidden averaging assumptions. The two-species minimality follows from the centered quadratic characteristic polynomial, while the three-species orientation switch follows from the directed-cycle spectrum. At \(L=50\), a positive real root proves instability in one orientation and exact Routh--Hurwitz determinants prove stability in the other. The included standalone checker independently rebuilds the six-dimensional characteristic polynomials.

## Originality — PASS (literature-bounded)
The 2026 Garmire--O'Dwyer work treats large demographic turnover by setting both leading stage rates equal and obtains a covariance-based random-matrix threshold. The 2025 structured-community-matrix paper considers general stage interactions and numerical community stability rather than the fixed-size fast-rate orientation comparison. Previous related mathematics for symmetric, undirected, zero-average stage interactions concerns a finite-rate instability threshold and does not imply the directed three-species sign-reversal or the generalized asymmetric projection. Searches also compared directional-cycle and stage-specific stability literature; no stronger claim covering the exact asymmetric fast-turnover classification was established. Residual risk: a general singular-perturbation or structured-population theorem not found in the inspected literature may implicitly contain the compression identity. This is a priority limitation, not an assertion that searches prove uniqueness.

## Value — PASS
Zero aggregate species-to-species interaction and nominally very fast demography might seem to ensure cancellation. The exact result shows that unbalanced replenishment weights can revive interactions and even reverse the local persistence verdict, with the first possible orientation effect at three species. It supplies a precise model-design boundary, not merely a small numerical change or a renamed May threshold.

## Limits and closest comparisons
The result is about local stability of a specified two-way stage-exchange gLV system, not general age-structured biology or persistence. The 2026 source's balanced fast-turnover calculation, the 2025 general stage-community framework, and the 2021 ecological stage-stability study are credited. A separate related zero-average two-stage construction addresses symmetric exchange and an undirected graph; its parameters and conclusions are not claimed as new here. Priority beyond the searched sources remains open.

Self-review: passed. Independent audit: not yet performed.
