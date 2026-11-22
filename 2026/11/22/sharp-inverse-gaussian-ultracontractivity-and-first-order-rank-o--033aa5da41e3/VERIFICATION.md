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

# Reproducibility and limits

Run `python CHECK.py` with Python 3, NumPy and SciPy in the directory containing this file. The script tests anisotropic covariance Schur complements and determinant identities, independently computes the exact norm in two ways, checks strict improvement over the known bound, and compares Gaussian row profiles to quadrature, together with a one-dimensional first-order normalized error.

The analytic theorem does not depend on numerical integration or testing. Reproducibility uses an explicit random seed. The check script does not test all dimensions, all times, or all matrices; those universal claims follow only from the proof in `RESULT.md`.

The original mapping paper's nonsharp Proposition 5.2 is the closest inspected literature. The earlier Mehler norm thesis was not exhaustively read. The self-review is recorded in `REVIEW.md` and `AUDIT.json`; no independent audit has been performed.
