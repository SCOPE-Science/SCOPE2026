# Independent mathematical audit — 2026-10-01

## Final claim assessed

Critical Derrick scaling reverses at p=1 in the SS+VV Dirac reduction

## Correctness — PASS

PASS. The algebra is correct for the displayed truncated Hamiltonian. The nonlinear-gradient coefficient has sign p-1. Mass-preserving scaling gives the stated three powers; stationarity gives the virial identity; at kappa=2 substitution collapses the scale energy to H2 times the square of lambda-squared minus one. The hyperbolic-secant integral ratio and first-order critical-power displacement are also reproduced by the inspected symbolic verifier. These statements concern only Derrick scaling of the truncated nonrelativistic Hamiltonian.

## Originality — FAIL

FAIL. The core sign-switch claim is mechanically visible in the source Hamiltonian that the record itself quotes: the coefficient is proportional to 1-1/p. Once that already-given Hamiltonian is accepted, the kappa=2 square identity is a standard mass-preserving Derrick-scaling consequence and the near-critical shift is a direct first-order expansion. The 2026 primary source explicitly studies the same arbitrary-p SS+VV family, its nonrelativistic modified NLSE and the kappa=2 stability transition. The audit could not retrieve its full text, but originality does not survive because the claimed final theorem is algebraically implied by the exact prior formula that the finding takes as its premise, rather than supplying an independent new structural input.

### equivalent_formulations

Searches: Resultary semantic search: nonlinear Dirac SS VV Derrick scaling p=1 critical exponent; 2609.18170 1-1/p Derrick

Evidence: The audited sign switch is exactly the sign of the pre-existing coefficient 1-1/p in the quoted nonrelativistic Hamiltonian.

Reasoning: Rephrasing the coefficient sign as a p=1 Derrick phase boundary does not avoid the implication from the source formula.

### broader_coverage

Searches: arXiv:2609.18170; PhysRevE.82.036604 nonlinear Dirac arbitrary nonlinearity modified NLSE

Evidence: The new 2026 source treats the arbitrary-p mixed interaction and nonrelativistic stability; older work already treats next-order pure scalar/vector modified-NLSE stability.

Reasoning: The mixed coefficient continuously interpolates already known opposite-sign endpoint corrections; no new nonstandard lemma is needed for the displayed sign classification.

### exact_database_or_table

Searches: published mathematical record semantic search for p=1 Derrick sign switch

Evidence: No numerical table is relevant; the claimed boundary is obtained symbolically from the existing Hamiltonian coefficient.

Reasoning: The exact answer is mechanically encoded in a prior formula rather than hidden in a database.

### claim_vs_prior_implication

Searches: arXiv:2609.18170 arbitrary p modified NLSE stability; Cooper Khare Mihaila Saxena 2010 modified NLSE

Evidence: The primary-source abstract confirms arbitrary p, nonrelativistic reduction, and stability discussion; the record quotes the exact coefficient from that reduction.

Reasoning: Standard scaling and Taylor expansion of that formula imply the final claim, so the claim is covered under the required implication standard.

## Scientific value — PASS

PASS. Correcting the sign of a stability diagnostic across an advertised parameter range is scientifically meaningful, and the p=1 boundary is a natural model boundary. The failure is originality, not usefulness: the calculation exposes a source conclusion that should not be applied uniformly in p.

## Source inspections

- **Two-Parameter Family of Nonlinear Dirac Equations With Scalar-Scalar plus Vector-Vector Interactions** — https://arxiv.org/abs/2609.18170. Material read: Primary-source abstract/indexed statement material; full text retrieval attempts through ordinary open interfaces were unavailable. Assessment: DECISIVE_PRIOR_FORMULA_AS_STATED_BY_FINDING. Evidence: The source treats arbitrary p, the nonrelativistic modified NLSE and stability near the kappa=2 transition; the audited record explicitly imports the coefficient whose sign gives its main boundary.
- **Solitary waves in the nonlinear Dirac equation with arbitrary nonlinearity** — https://doi.org/10.1103/PhysRevE.82.036604. Material read: Primary abstract and indexed article material. Assessment: BACKGROUND_ENDPOINT_STABILITY. Evidence: It derives a next-order modified NLSE and discusses Derrick stability with a kappa=2 threshold for pure interactions.

## Limitations and residual risks

The exact trichotomy is only for the displayed truncated nonrelativistic Hamiltonian; the critical-power displacement is first-order in the nonrelativistic parameter.

- The 2026 source full text could not be retrieved in this run; however the originality failure relies on the exact prior Hamiltonian formula explicitly adopted by the finding itself.
- Derrick scaling does not establish spectral or orbital stability of the parent nonlinear Dirac equation.

## Disposition

**failed**
