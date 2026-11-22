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

# Verification status

The submitted result is supported by an explicit mathematical proof and `CHECK.py`. The checker differentiates the exact chord-perimeter expression, reconstructs the Hessian and determinant, verifies the normalization coefficients in dimensions three and four, and compares a separate exact finite-threshold conditional integral in dimensions three, four, five, and seven against the predicted leading law for shrinking thresholds. Run `python CHECK.py` after installing packages in `requirements.txt`.

A successful finite script execution does not prove the infinite asymptotic or uniqueness of the result in earlier literature. Those claims rest on the analytic argument and the documented literature comparison. No independent mathematical audit has been carried out.
