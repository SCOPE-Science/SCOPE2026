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

# Reproducibility
Run `python3 CHECK.py` using Python 3 standard library. The script reconstructs the exact vertex lists from the source, tallies the image-unit-block multiplicities, checks the explicit finite Perron polynomial for small cutoffs, and compares floating-point Sturm root estimates at several large cutoffs with the analytic Airy constant. It passed 359 deterministic checks. The proof of the infinite Airy-edge limit is the independent variational argument in RESULT.md, not a claim of numerical certification. No external package or file is required.
