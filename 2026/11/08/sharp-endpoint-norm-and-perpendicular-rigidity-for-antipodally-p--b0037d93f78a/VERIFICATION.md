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

Execute `python3 check_circle.py` from the directory containing this document and the checker. The checker uses only Python standard-library modules. Successful output ends in `ALL_ANTIPODAL_ATOM_TRIGONOMETRIC_PROJECTION_CHECKS_OK`.

The code checks the Gram matrix at multiple rational mass parameters by exact fractions; reconstructs the integral-kernel row norm by independent uniform-circle midpoint quadrature; tests the analytically identified extremizing evaluation positions and input-sign witnesses; checks exact norm endpoints, differential formulas, and numerical instances of the strict angular derivative margin. All parameter-uniform claims are proved by algebra and calculus in `RESULT.md`; the checker samples parameters and is not an infinite certificate. In particular the inequality \(2\sqrt3>\pi\) is used in the analytic proof, not inferred from numerical data.

The sharp norm statement applies only to the real three-dimensional first-harmonic space and measures with positive continuous mass \(\(0<1-w<1\)\). The limiting pure two-atom measure fails to represent that space faithfully; only a one-sided norm limit is asserted.
