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

# Verification

`checker.py` implements the saddle in the displayed theorem and an independently evaluated finite-rate Gaussian-mixture integral using log-stabilized numerical quadrature. It verifies the known exact beta normalization, the strictly convex saddle, both strict Gaussian-cost inequalities, the conditional weak-phase selection and the sharp prefactor over contrasting trap stiffnesses, diffusion scales and switching rates. It also verifies the quartic Gaussian-breakdown onset and the two asymptotic expansions at separated displacement scales. The successful observed replay produced `PASS 161 deterministic mathematical assertions`.

Proof dependence: the exact stationary variance-mixture transport equations and its beta normalization; Stirling's beta-function asymptotic; one-dimensional nondegenerate Laplace asymptotics; elementary differentiation and endpoint expansions. Finite quadrature cannot establish uniqueness or infinite-parameter asymptotics by itself; those claims rely on the calculations in `RESULT.md`. No expert, machine-formal, or independent scientific certification is asserted.
