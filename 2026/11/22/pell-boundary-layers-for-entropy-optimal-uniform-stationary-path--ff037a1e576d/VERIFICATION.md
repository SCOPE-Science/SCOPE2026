---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The full-length entropy error is proved in RESULT.md by exact cancellation in the two-wall row residual, summed over all rows, and a dimension-independent inverse bound in the sum norm. The original `verify.py` checks the one-wall profile in Pell form and tests finite stochasticity, entropy normalization and qualitative surface convergence; it is not a test of the sharpened rate. The Pell form of the profile is the rational factorization in the proof after writing \(h_k(-1)^k=Ar^{-k}+Br^k\), where \(A=(5+3\sqrt3)/2\), \(B=(5-3\sqrt3)/2\) and \(r=-(2-\sqrt3)\).
