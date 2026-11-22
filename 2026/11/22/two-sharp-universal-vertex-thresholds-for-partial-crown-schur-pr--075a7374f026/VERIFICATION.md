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

# Reproducible finite verification

From this package directory, execute `python3 checks/verify_partial_crown.py` using Python 3 with NumPy and SciPy. The stored script checks all closed-form branches through core size 120, constructs direct singular-value witnesses through core size 20 with multiple duplicate row/column configurations, and compares the theoretical global norm with independently optimized nonsymmetric weights on small rectangular instances. Its expected output is `PARTIAL_CROWN_SCHUR_DIAGNOSTIC_OK 1371`.

All nonstandard universal mathematical steps are derived in `RESULT.md`: Schur/trace duality, joint concavity, symmetry averaging, the exact singular spectrum, and strict one-variable optimization. A numerical optimizer cannot certify global optimality or an all-dimension statement; the analytic proof is the evidence for those assertions. The literature comparison has residual bibliographic risks described in `REVIEW.md` and `AUDIT.json`. No independent mathematical audit has been performed.
