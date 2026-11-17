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

# Verification protocol and limits

The theorem is proved analytically in RESULT.md. On Python 3, run `python check.py` to perform 2,400 seeded checks of exact rational conservation/aggregation and supplementary floating-point Lyapunov identities. It prints `PASS: 2400 independent rational vector-field and floating entropy-identity trials` when all assertions pass. This finite test is not used as an infinite proof. Existence, uniqueness, and global convergence follow from the scalar nullcline intersection, the strict analytical Lyapunov identity, compactness and scalar convergence. No independent audit has been performed.
