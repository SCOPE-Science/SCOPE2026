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

The scientific argument is analytic. The auxiliary checker `CHECK.py` requires Python 3 and SciPy; it verifies independently calculated variance bounds and numerically integrates normalized Gaussian-mixture envelopes for two model choices with Pareto-type waiting tails.

The checker is not an exhaustive mathematical proof or a surrogate for the renewal and Tauberian arguments. Its final output was `All independent quadrature and rare-event bounds passed.`

The proof assumes finite-mean soft renewals, strictly positive stiffnesses, independent switching/Brownian noises, and fixed positive stiff-phase duration. None of the formulas is asserted for an infinite-mean renewal clock or a vanishing soft stiffness.
