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

# Reproducibility and verification

The proof is symbolic for all integers \(d\ge2\) and every positive \(\lambda,\gamma\); the finite checker is a supplementary algebraic consistency test. Execute `python3 checker.py` with Python 3 and no external packages. The exact-rational test suite checks tournament skew-symmetry, regularity and affine-adjoint identities in representative odd dimensions; it also exhaustively checks tournament regularity criteria at dimensions two through five. The proof separately establishes absorbing-boundary weak evolution and the full Doob transform, which finite tests cannot certify.

The exact survival statement applies to the uniform initial simplex distribution, not to all initial conditions. No external independent audit is represented here.
