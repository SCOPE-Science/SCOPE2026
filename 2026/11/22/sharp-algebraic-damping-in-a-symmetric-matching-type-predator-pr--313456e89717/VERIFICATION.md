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

# Reproducibility

Run `python verify.py` with SymPy, NumPy and SciPy. It checks, by symbolic reduction, the exact relative-entropy dissipation identity, the normalized complex two-dimensional response and its rational universal constant. Three finite-time numerical ODE integrations also compare the predicted asymptotic products at time 12,000. They are supplementary checks rather than infinite-time proofs. The analytic proof in RESULT.md supplies the necessary center-manifold and averaging argument.

The theorem concerns the source model's **deterministic** zero-mutation ecological limit. No stochastic population-time estimate or independent validation is claimed.
