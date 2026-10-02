# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **failed**.

Correctness: PASS. The algebra is correct for the displayed truncated Hamiltonian. The nonlinear-gradient coefficient has sign p-1. Mass-preserving scaling gives the stated three powers; stationarity gives the virial identity; at kappa=2 substitution collapses the scale energy to H2 times the square of lambda-squared minus one. The hyperbolic-secant integral ratio and first-order critical-power displacement are also reproduced by the inspected symbolic verifier. These statements concern only Derrick scaling of the truncated nonrelativistic Hamiltonian.

Originality: FAIL. The core sign-switch claim is mechanically visible in the source Hamiltonian that the record itself quotes: the coefficient is proportional to 1-1/p. Once that already-given Hamiltonian is accepted, the kappa=2 square identity is a standard mass-preserving Derrick-scaling consequence and the near-critical shift is a direct first-order expansion. The 2026 primary source explicitly studies the same arbitrary-p SS+VV family, its nonrelativistic modified NLSE and the kappa=2 stability transition. The audit could not retrieve its full text, but originality does not survive because the claimed final theorem is algebraically implied by the exact prior formula that the finding takes as its premise, rather than supplying an independent new structural input.

Scientific value: PASS. Correcting the sign of a stability diagnostic across an advertised parameter range is scientifically meaningful, and the p=1 boundary is a natural model boundary. The failure is originality, not usefulness: the calculation exposes a source conclusion that should not be applied uniformly in p.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
