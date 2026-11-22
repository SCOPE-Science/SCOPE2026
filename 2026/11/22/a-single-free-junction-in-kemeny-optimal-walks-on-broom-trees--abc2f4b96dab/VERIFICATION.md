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

Run `python VERIFY.py` under Python 3 with SymPy and NumPy. The symbolic portion checks the exact expressions for the even and odd cut-weight sums, the slackness polynomial after changing to nonnegative integer parameters, and the KKT multiplier numerator polynomials after introducing a nonnegative offset. Every asserted coefficient inequality is exact rational arithmetic, so its correctness is not a numerical extrapolation. The accompanying finite tests cover 216 admissible parameter pairs and directly compare inverse Laplacian eigenvalue sums on smaller graphs.

# Limits

A successful script execution is a reproducibility check, not an independent audit. The result does not cover nonreversible or nonuniform-stationary walks. The first-public-date evidence applies to the motivating Kemeny source, not to any claim of publication of this theorem.
