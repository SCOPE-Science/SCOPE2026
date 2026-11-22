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

# Verification

`python3 verify.py` uses only Python 3 standard-library operations. In the recorded run it printed `PENULTIMATE_SIGN_PRODUCT_DIAGNOSTIC_OK 595`. It reconstructed all sign rows and all \(2^{n-1}-1\) equality coordinates for integer orders \(4\) through \(8\), verified the two missing-row norm factors, the stationarity equation, the exact Cauchy–Schwarz intermediate inequality on rational examples, and numerical bounds on deterministic fractional samples.

The full general-order claim is established by the symbolic pigeonhole, scalar-optimization, explicit-witness and compactness arguments in RESULT.md, **not** by extrapolating finitely many tests. Floating-point comparisons are diagnostic only. The package makes no independent-validation or exhaustive-bibliography claim.
