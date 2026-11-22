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

# Reproduction and limits

The symbolic proof in `RESULT.md` establishes the all-parameter assertion. Two independent finite cross-checkers are provided:

- `python verify_weighted.py` builds the physical integer cross-cut matrix and compares its exact Smith form with the two-factor recurrence for every odd length from three through seventeen and every integer rung weight from minus six to six, 104 cases in total. Expected final marker: `WEIGHTED_SMITH_PASS`.
- `python verify_weighted_schmidt.py` independently constructs the physical adjacency graph and enumerates modular image sizes at lengths three, five, and seven for several prime and composite qudit dimensions, then checks selected pure-state Schmidt spectra by direct numerical diagonalization. Expected marker: `WEIGHTED_SCHMIDT_PASS`.

Both scripts were executed successfully. The direct eigenspectrum tests have floating-point tolerances; integer Smith forms and image-cardinality tests are exact. These finite checks are evidence for implementation consistency, not exhaustive verification for infinitely many lengths and dimensions. The infinite statement follows from the included integral-module and character-orthogonality arguments. Independent validation has not been performed.
