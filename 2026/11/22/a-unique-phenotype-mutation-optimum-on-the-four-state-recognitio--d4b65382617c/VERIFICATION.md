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

# Reproduction

Use `python CHECK.py` with Python 3 and SymPy. The checker reconstructs the four-point Fourier weights, verifies the rational positive-denominator identity and the degree-ten derivative identity by exact symbolic cancellation, verifies the coefficient sign constraints, isolates a positive root by rational endpoints and reproduces the illustrative numerical threshold.

The symbolic identities are certificate-like executable checks; the theorem for every positive mutation rate and discrimination strength also needs the written Descartes-sign proof in RESULT.md. No exhaustive search over a continuum is implied. The biological interpretation is restricted to the cited weak-selection, large-population approximation. No independent audit has been performed.
