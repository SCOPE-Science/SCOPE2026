---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the mixed-axis stationary-entanglement classification

From the package directory, run `python checker.py` with SymPy and NumPy available. This reconstructs the stationary matrix from the displayed rational expressions; symbolically checks the exact two rationalized partial-transpose branches and the eighth-degree sign polynomial; verifies coefficientwise positivity of the polynomial certifying exclusion of the second branch; verifies the decisive relationship between the middle coefficients of the first-branch polynomial; and solves independently assembled complex \(16\times16\) Lindblad generators for 130 randomized strictly positive parameter tuples.

For each of those 130 tuples, the checker compares the explicit stationary state with direct linear-system solution, trace, positive-semidefiniteness, and direct Wootters-eigenvalue concurrence. Another 120 independent random triples check one positive polynomial root and the concurrence signs on either side. The completed run printed `PASS: symbolic coefficient certificate, one-crossing argument, independent 16x16 master equation and direct concurrence; numeric assertions: 880`. Exact symbolic coefficient positivity establishes the all-positive-parameter claims; random cases are finite consistency tests, not a substitute for the analytic proof.

Scope limitation: the modeled noise operators are precisely \(X\otimes I\) and \(I\otimes Z\) with Poisson *joint* state resets to \(\lvert00\rangle\). No many-body, thermal or arbitrary-noise universality is established. Independent experimental validation, independent audit, and comprehensive priority certification have not been performed.
