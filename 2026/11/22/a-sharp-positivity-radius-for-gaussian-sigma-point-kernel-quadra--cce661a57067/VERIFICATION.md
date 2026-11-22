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

The exact derivation is in RESULT.md. Reproduce the independent finite checks with `python verify.py` (Python 3, NumPy); the expected output is `PASS 3774 assertions`.

The numerical script reconstructs and solves full positive-definite kernel matrices and separately computes the two-orbit formulas, checks scalar crossing/sign regimes and sampled monotonicity, and tests selected large-dimensional scalings and the flat-kernel limit. These tests do not certify the all-parameter calculus inequalities; those are proved analytically. Gaussian Gram matrices may be ill-conditioned when the kernel length scale is very large, so the script deliberately uses finite tolerances. No external independent audit or certification is claimed.
