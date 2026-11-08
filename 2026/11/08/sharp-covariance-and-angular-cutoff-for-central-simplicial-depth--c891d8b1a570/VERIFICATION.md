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
The analytical proof derives the mixed covariance and both variances from explicit conditional distributions. A single independent circular-sample verifier checks exact identities symbolically over a finite grid and compares simulated geometric configurations with the exact predictions. Run `python verify.py` in a Python environment with SymPy and NumPy. The script does not establish the theorem for all sample sizes or cutoffs; that is the role of the exact derivation in RESULT.md. The source comparisons do not amount to independent priority certification.
