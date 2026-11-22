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

# Reproducibility and verification

The exact domain, quantifiers, boundary cases, and four-facet analytic proof are in `RESULT.md`. The proof verifies all real parameters directly; it does not rely on computations. For supplementary exact rational finite checks, execute `python3 check.py` with Python 3's standard library. The checker enumerates all vertices of the piecewise-affine perturbation subdivision for rational boundary pairs. It reports:

`STEINHAUS_SQUARE_EXACT_RATIONAL_DIAGNOSTIC_OK 18145`

This verifies 18,145 finite assertions including multiple radii and separations, the global pair lower bound, the canonical extremizer's equality, and the explicit real linear isometry. The finite checker is **not** an infinite proof; the proof in `RESULT.md` handles all continuous parameters analytically. The original and related literature were inspected as described in `REVIEW.md` and `AUDIT.json`. Independent mathematical audit has not been performed.
