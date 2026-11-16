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

The mathematical proof checks the defining moments, normalizations, rank and singular values for all erasure subsets, and the axis-triple census. The supplemental executable `verify_icosa_erasure.py` is self-contained and uses only Python standard-library modules.

Execute `python3 verify_icosa_erasure.py` from this directory. The observed run reported `PASS`, checked 299 erasure subsets with at most three deletions, verified all 220 triple categories and 20 axis triangles, reconstructed a nine-column orthonormal harmonic sampling matrix, and completed 1,317 scalar checks.

Numerical checks use a tolerance of \(3\cdot10^{-12}\) and are not a substitute for the exact moment, kernel, eigenvalue and Seidel-trace arguments. All statements for four or more erasures follow exactly from the nine-dimensional rank bound. No external independent audit was performed.
