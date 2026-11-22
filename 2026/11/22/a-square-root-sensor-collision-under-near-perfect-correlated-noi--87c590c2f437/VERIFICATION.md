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

# Verification and reproducibility

The mathematical proof is contained in `RESULT.md`. Supplementary checks are reproducible with `python verify.py` and the Python dependencies in `requirements.txt`. The output recorded in `verification_output.txt` is from running that exact script against the supplied code.

Exact symbolic checks include the evaluation-norm factorization, the chord-distance critical value and first and second derivatives, and the first-order asymptotic constant. Numerical checks include 2,500 two-point direct determinant/chord evaluations and four differential-evolution location searches with fixed random seed; the searches confirm the predicted collision and information behavior at listed correlations.

**Limits:** Numerical optimization cannot prove uniqueness or exclude unsampled competitors; all global statements use the analytic Rayleigh and chord bounds. The result does not include a formal proof-assistant certificate, independent audit, correlated-error model estimation or data-based validation of fixed correlation across changing sensor locations.
