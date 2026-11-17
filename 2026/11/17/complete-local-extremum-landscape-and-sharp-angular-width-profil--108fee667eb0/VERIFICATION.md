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

# Verification procedures and limits

`python3 check_permuto_width.py` runs with the Python standard library. A successful replay reports:

`PERMUTO_WIDTH_CHECKS_PASS integer_inequalities=48534 cut_profiles=275 sharp_geodesics=275 maxima_permutations=5910`

The integer checks cover bounded zero-sum grids in block sizes from 2 to 8. The width and sharp angular formulas are additionally sampled at every block-size split for 3 through 24 coordinates, with each extremal tangent vector constructed explicitly. The sorted-chamber maximum is checked on 5,910 permuted integer gradients in dimensions 3 through 7. These tests are corroborative only: they do not explore an infinite range of dimensions or the continuum of real directions. The proof of those statements is contained in RESULT.md.

Source comparison included the full arXiv web texts of arXiv:1904.11029 and arXiv:1911.11159, and the NIST definition of Gini mean difference. Those documents establish the known geometric and functional background, not independent verification of the new local-extremum theorem. Independent mathematical review remains unperformed.
