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

# Computational and proof verification

Execute `python verify.py` in the directory of the extracted files with Python 3. No external Python packages are required.

The verifier independently uses Euclidean point-to-rectangle distances on a midpoint grid to approximate the parallel area of the three-rectangle union. It compares six families of dimensions at five radii each, verifies the sign before and immediately after the cutoff, and tests the three asymptotic coefficients across several values. Observed result: `PASS 75 grid/area comparisons and first-contact asymptotic checks`.

The mathematical proof does not rely on the grid tolerance: it uses exact inclusion–exclusion of rectangle offsets, an explicit quarter-plane single-elbow correction and an exact two-circle upper-half lens integral. The grid does not certify all radii, every shape or the global uniqueness of an expansion. No external audit has been performed.
