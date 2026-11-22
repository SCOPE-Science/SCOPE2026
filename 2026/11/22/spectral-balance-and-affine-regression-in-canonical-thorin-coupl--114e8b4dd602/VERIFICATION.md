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

# Verification notes

Execute `python checker.py` from the directory containing `RESULT.md` and the checker. The checker uses the Python standard library, including `fractions.Fraction`, and has no external data or dependency. It reports exact-rational and numerical diagnostic groups and exits on a failed assertion.

The exact tests reconstruct signed rates from the map \((\lambda,r)\mapsto(r/\lambda,r/\lambda^2)\), verify Jacobians, finite shell membership and Stieltjes-transform cancellation for asymmetric two-sided spectra satisfying the balance condition, and check strict one-sided multi-rate nonaffinity. The complex floating-point tests check gamma HBB factorization with mixed signs and a Gaussian component. The theorem for general measures relies on the Lévy integrability, truncation, joint weak convergence and signed Stieltjes-transform uniqueness proofs in `RESULT.md`. In particular, finite tests do not prove infinite-activity statements or a full distributional classification.

Theorem scope includes arbitrary real Thorin measures with standard Thorin integrability for the joint Lévy result, and the stronger displayed first-moment integrability for the affine conditional-regression equivalence. External independent verification has not been performed.
