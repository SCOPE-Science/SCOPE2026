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

# Verification evidence

From the standalone file `verify_grassmannian.py`, run `python verify_grassmannian.py` using Python 3 without external dependencies. Exact-rational output:

```text
EXACT_PLUCKER_AND_BILINEAR_IDENTITY_OK 20
EXACT_MOMENTS_AND_SHARP_ENVELOPES_OK 1710
SHARP_EIGENVALUE_MULTIPLICITIES_OK 16
ALL_GRASSMANNIAN_LP_CHECKS_OK
```

The checker independently creates rational four-dimensional rotations, constructs their Plücker coordinates, and verifies the precise bilinear reduction. It evaluates even moments by exact Dirichlet factorial/Pochhammer arithmetic across 1,710 nonzero trace-free diagonal instances, compares sharp endpoints, checks the fourth-moment trace identity, and tests both endpoint spectra at eight even-moment orders. The checker is finite; the proof of inequalities for all real exponents uses strict convexity and does not rely on exhaustiveness of these tests. No independent audit has been performed.
