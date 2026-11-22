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
# Verification record

The main theorem is proved analytically in `RESULT.md`. The exact first-index crossing is reduced to \(z=e^{-z}\) with unique root \(W_0(1)\); strict convexity supplies the all-index hazard classification, the product recursion supplies the one-change survival classification, and an explicit positive infinite-product criterion supplies the tail equivalent.

`check.py` is a standalone Python 3 standard-library numerical stress test. Run `python3 check.py` in the extracted directory. It examines several values of both parameters, checks the threshold identity and the sign patterns, computes the real unique crossing and the asymptotic scalar root, and tests that crossing-location errors diminish with increasing scale. All these checks are finite and floating-point; they are supporting diagnostics, **not** a substitute for the infinite-domain proof. The displayed numerical values are not asserted to have independently certified rounding error. No independent mathematical audit was performed.
