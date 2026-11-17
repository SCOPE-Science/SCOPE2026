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

# Verification of the marked simultaneous-cross-ratio law

The rigorous proof comprises an exact stereographic reduction, a uniform-integrability argument for Cauchy tails, a tail-integral representation of the constant, and Scheffé's lemma. The included `verify_pentagon_crossratios.py` performs reproducible numerical checks with SciPy and NumPy; these are corroborative only. The script prints `PENTAGON_CROSSRATIO_CHECKS_OK` after quadrature and Rao–Blackwellized simulations. No Lean, computer-assisted infinite certification, or independent mathematical audit is claimed.

The script uses deterministic seed 672019. Its numerical integrand for \(K\) is nonnegative and absolutely integrable. The finite-threshold estimates converge toward the quadrature value within their reported errors, with expected finite-threshold bias. Empirical sampling is not relied upon for the positive-finite constant or the total-variation statement.
